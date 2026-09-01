# Design doc: the four owned decisions

Status: DRAFT 2026-08-30. All bake-off rounds are measured and committed;
final polish before submission.

> STALE SECTIONS (2026-09-01): parts of this draft still describe the
> open-loop pipeline as the current shell. That shell is retired — frozen at
> the tag `pipeline-baseline-final` and deleted from main; the closed-loop
> research agent (`research_agent.py`, ADR-0005) is the product. The rewrite
> ships with the final report.

This document records the four design decisions the project owns end-to-end:
tools, context management, memory, and evals. Each section states the
decision, the evidence behind it, and the alternatives that lost. The ADRs in
`docs/adr/` hold the point-in-time rationale; the wayfinder tickets in
`.scratch/equity-research-agent/issues/` hold the full decision history.

## The task

Given a bank, a period, and a headline metric, explain the movement against
the prior comparable period, attribute it to drivers, and produce a
confidence-rated attribution that cites the evidence behind every claim.
Banks: CBA, NAB, Westpac (ANZ and one sealed bank held out). Metrics: NIM,
cash earnings, ROE, CET1, credit impairment charge, cost-to-income.

The one-sentence thesis that fell out of the work: **movement numbers are a
solved cheap-model problem; the "why" layer is a context problem, not a
model-size problem.** The four decisions below all serve that split.

## Decision 1 — Tools: deterministic core, models only at the edges

(ADR-0002, ADR-0004; tickets 03, 07, 13, 14)

The pipeline is imperative where the domain is known and agentic where it is
not. Code owns: document manifests and caching, page retrieval, walk/bridge
arithmetic, unit and scale harmonisation, comparison classification,
tolerance checks, confidence caps, provenance stamps. Models own exactly
three narrow jobs:

1. **Text extraction** (qwen3.7-flash): one page in, structured facts out,
   verbatim quotes only.
2. **Vision walk reads** (qwen3.7-flash): waterfall charts have no text
   layer; a vision call returns endpoints and bars, then code validates the
   sum, drops endpoint-bars, and harmonises scale slips (a misread chart must
   fail arithmetic, not become a citation).
3. **Authoring** (qwen3.7-flash in the default combo): assemble the evidence
   into the attribution under rules that forbid guessing; every number the
   author emits is checked against a cited evidence record by code.

Model access goes through OpenRouter so tiers stay swappable per role
(`config.Combo`). Two independent judge models from different families
(deepseek-v4-pro + qwen3.7-flash) grade narrative claims; disagreement flags
a human instead of resolving by tie-break.

Why this shape: the failure mode that matters in equity research is a
confident wrong number. Every deterministic layer exists because a model
produced a plausible artifact that arithmetic caught — endpoint bars repeated
as movements, endpoints converted at a different scale than bars, comparative
columns read as the wrong period. The validators (`validate.py`) turn those
from silent contaminations into visible failed checks that cap confidence.

Rejected: a single frontier agent per query (the benchmark ceiling — right
answers at ~1000x the cost, and nothing catches it when it slips); vision for
all tables (text-layer extraction matches it on clean tables at a fraction of
the cost); LangChain-style frameworks (the pipeline is ~10 files of plain
Python; a framework would hide exactly the layer we need to control).

## Decision 2 — Context management: a page budget, and what broke it

(Tickets 03, 19, 27, 32; ADR-0002)

Documents are 100-200 page PDFs; six of them can be in scope for one case.
Nothing fits in one context window, and most pages are irrelevant. The
pipeline assembles context deterministically: local embedding retrieval
(bge-small) plus metric-specific queries nominate pages; a budget
(14 text pages for the primary document, 7 for others) selects them with
document-type ranking (profit announcement > presentation > ASX release) and
period priority; walk pages get vision reads; everything else gets text
extraction. Per-case cost: $0.002-0.005, one to three minutes.

This is an **open loop**: pages are chosen once, before any reasoning. It
proved to be simultaneously good enough and the single biggest limitation:

- Good enough: 25/25 dev cases produce correct movements or honest failures;
  Brier 0.035; zero confidently-wrong claims; 36/36 claims at confidence 85+
  correct (commit 9a9d13d).
- The limitation: on the judge's narrative checklist ("does the note state
  the bank's own why"), the open loop scores ~0. The why-layer lives on pages
  retrieval never ranks — audited notes in appendices, footnote targets,
  divisional sub-splits. We named this **page starvation**.

The five-arm bake-off (ticket 32) isolated the cause. Four anchor cases, one
judge protocol, identical for every arm:

| arm | loop | checklist | movement | cost/case |
|---|---|---|---|---|
| cheap pipeline | open | 0/15 | 4/4 | $0.002-0.005 |
| glm-5.3 author, same context | open | 1/15 | 4/4 | $0.22-0.86 |
| Sonnet agentic | closed | 6/15 | 4/4 | ~40k tokens |
| Fable agentic | closed | 3/15 | 4/4 | ~25k tokens |
| Codex agentic | closed | 1/15* | 4/4 | quota |

*Codex's row carries 5 judge flags and a citation-style interaction; its
numbers match gold with zero residual.

The glm control is the decisive row: a reasoner ~100x the price, on the same
starved context, gained one checklist item. The closed-loop agents win
because they **follow references while reasoning** — the exemplar is CBA's
Note 2.2 (PDF p118), which decomposes the impairment movement exactly
(+150 collective, −17 individual, −71 write-backs = +62) and is reachable
only by reading "refer Note 2.2" on the income statement. Retrieval ranks
that appendix page near zero for every query.

The response is not "buy a bigger model"; it is **deterministic
reference-following** (ticket 22): after page selection, code scans selected
pages for note references, printed-page references, and footnote markers,
resolves them against a per-document notes index, and adds up to four target
pages to the extraction set. Followed pages carry an extraction hint naming
the reference that reached them, and the author is instructed to explain
from the bank's own words rather than restate the numbers.

Round 2 measured this engineered arm on the same anchors: **0/15 → 3/15**
at a worst-case cost of $0.0048 per case, with the suite improving alongside
(Brier 0.032, confidently-wrong 0.0). The impairment case now carries the
Note 2.2 provision-type bridge — the exact find that made the closed-loop
arms the exemplar — inside a $0.003 pipeline run. The residual gap to the
Sonnet row decomposes into two mechanical fixes (headline facts cannot
entail in the current report shape; walk-page annotations need a vision
read to pair numbers with labels) and two facts outside a FY-vs-FY scope,
not into a loop-shape deficit. The standing plan: one more cheap-tier
iteration on those fixes; adopt a hybrid (cheap numbers + one Sonnet-tier
closed-loop why-pass) only if the anchors still sit below the closed-loop
bar after it. Reference-following also proved a point the bake-off table
understates: an instructive failure inside the round — the author mixed
bars from two published walks into a table describing no real walk — was
caught by the suite's confidently-wrong metric and fixed with a
NEVER-MIX-FRAMINGS rule the same day. The eval harness, not a bigger
model, is what makes cheap-tier iteration safe.

## Decision 3 — Memory: a versioned registry, not a vector store

(ADR-0003; tickets 04, 11)

What the system remembers between runs is exactly what a sector analyst
carries between reporting seasons: how each bank talks. The registry
(`registry/*.json`) maps each bank's verbatim disclosure labels to a
canonical driver taxonomy — walk-bar names, basis vocabulary, calendar
balance dates, restatement flags. Two properties are load-bearing:

1. **No financial numbers.** The registry stores language, never values. A
   remembered number is a leak waiting to contaminate a fresh case; a
   remembered label is just vocabulary. This rule made the holdout design
   defensible: the sealed cases test the same code and registry with zero
   possibility of memorised answers.
2. **Versioned and reviewable.** The registry is JSON in git. Every addition
   is a diff a reviewer can read. When NAB restated its divisions, the fix
   was a labelled registry entry, not a re-embedding.

Session memory (what happened this run) lives in the artifacts themselves:
every attribution carries provenance (models, documents with content hashes,
cost, seconds) and its full evidence records, so any claim is auditable
months later without rerunning anything. Process memory (why decisions were
made) is the wayfinder map plus tickets — 32 of them at last count.

Rejected: a vector store of "learned facts" (unauditable, contamination-prone,
and the retrieval problem it solves is one we already solve per-case);
fine-tuning (nothing here needs weights; everything needs provenance).

## Decision 4 — Evals: calibration first, judges second, holdouts sealed

(Tickets 02, 05, 17, 28-31; `docs/design/eval-review-guide.md`)

The eval harness answers three questions in order of importance:

1. **Is a stated number right?** Gold cases carry values page-sighted in
   primary disclosure with printed provenance strings. Scoring is
   three-state (correct / incorrect / unscored) with per-unit tolerances;
   coherent alternative framings score as variants, not as errors; an
   unverified gold value is quarantined, never graded (the FY25 notables
   $130m level was quarantined until sighted on two printed pages, then
   restored).
2. **Is confidence honest?** Confidence is a single 0-100 self-report that
   code can only cap downward (fatal check → 40, single-source → 85, no
   primary walk → 85). We track Brier score and a confidently-wrong rate
   (claims at 85+ that are wrong). Current: Brier 0.035, confidently-wrong
   0.0, 36/36 at 85+. The design goal is asymmetric: a low-confidence wrong
   answer is a research lead; a high-confidence wrong answer is a fired
   analyst.
3. **Does the narrative say true things?** Numeric scoring cannot grade "the
   bank attributes the decline to liquids". The judge protocol asks two
   narrow questions per checklist fact — does the note state it, and do the
   cited quotes entail it — each to two judge models from different
   families. Only stated-AND-entailed passes; judge disagreement flags a
   human. Empty citations are not-entailed by rule: nothing entails nothing.

The holdout estate is layered because iteration contaminates: 25 dev cases
(iterated on freely), 13 in-repo quarantined cases (Codex-designed slate,
frozen, honestly labelled *prospective* quarantine), and 5 sealed cases plus
one sealed bank held entirely outside the repository, administered once at
the final milestone under a freeze-first protocol. An independent model
(Codex) designed the quarantine slate specifically because it had not
iterated on the pipeline.

Rejected: LLM-judge-only scoring (coverage is not correctness — citing the
right page proves retrieval, not truth); a single blended "quality score"
(it hides exactly the confidently-wrong tail we care about); historical
holdout claims (no repo-resident case predates iteration, so we refuse to
call any of them pristine).

## Costs

Whole project to date: ~USD 3 of OpenRouter spend. Per case: $0.002-0.005
(default combo), one to three minutes. The frontier benchmark that anchors
the quality ceiling costs three orders of magnitude more per case; the
system's job is to close the insight gap without paying that gap in price.
