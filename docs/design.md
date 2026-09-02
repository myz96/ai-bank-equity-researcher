# Design doc: the four owned decisions

Status: FINAL 2026-09-02. All suites run and committed; scorecards under
`evals/results/`.

This document records the four design decisions the project owns end-to-end:
tools, context management, memory, and evals. Each section states the
decision, the evidence behind it, and the alternatives that lost. The ADRs in
`docs/adr/` hold the point-in-time rationale; the wayfinder tickets in
`.scratch/equity-research-agent/issues/` hold the full decision history.

## The task

Given a bank, a period, and a headline metric, explain the movement against
the prior comparable period, attribute it to drivers, and produce a
confidence-rated attribution that cites the evidence behind every claim.
Banks: CBA, NAB, Westpac (ANZ unseen; Macquarie sealed). Metrics: NIM,
cash earnings, ROE, CET1, credit impairment charge, cost-to-income.

The one-sentence thesis that fell out of the work: **movement numbers are a
solved cheap-model problem; the "why" layer is a context problem, not a
model-size problem.** The four decisions below all serve that split.

## Decision 1 — Tools: a closed loop over a deterministic estate

(ADR-0002, ADR-0004, ADR-0005)

The product is one tool-calling model researching in a closed loop
(`agent/research_agent.py` + `agent/toolbox.py`). The tool surface is small
and each tool wraps machinery code fully controls:

- `plan_research` — the model's first call lists where the answer's pieces
  should live; the loop reads the plan back once at submit time.
- `search_pages` — pooled hybrid retrieval (BM25 + bge-small) over the
  case's whole corpus, fanned over 1-3 query phrasings per call.
- `read_page` / `read_chart` — page text, and vision reads of walk charts
  (endpoints and bars validated by arithmetic; a misread chart must fail a
  sum check, not become a citation).
- `cite` — turns quotes into evidence records; every quote is checked
  verbatim against the page at mint time, and a paraphrase is rejected back
  to the model.
- `follow_references` / `bank_language` — deterministic note-pointer
  scanning and the registry's label vocabulary.
- `submit` — the answer, which then faces the validator estate: unit and
  sign conventions, comparison classification, walk arithmetic, tolerance
  checks, a movement-grounding cap, and the confidence caps.

Roles: z-ai/glm-5.3-flash drives the loop (the accuracy flagship);
qwen3.7-flash reads charts; deepseek-v4-pro + qwen3.7-flash judge (two
model families; disagreement flags a human). A `fast` combo swaps
deepseek-v4-flash into the same loop for evaluators in a hurry — its
movements hold, but it breaks the confidently-wrong guarantee on dev
(0.026 vs the flagship's 0.0), which is exactly the trade the scorecards
document.

Why this shape: the failure mode that matters in equity research is a
confident wrong number. Every deterministic layer exists because a model
produced a plausible artifact that arithmetic caught — endpoint bars
repeated as movements, comparative columns read as the wrong period, a
movement grounded by a note number. The validators turn those from silent
contaminations into visible failed checks that cap confidence.

Rejected: the open-loop pipeline this project built first (retired at tag
`pipeline-baseline-final`; the bake-off below is why); a frontier agent per
query (the quality ceiling, at ~100x the per-case price, with nothing
catching it when it slips); agent frameworks (the estate is plain Python in
five small packages; a framework would hide exactly the layer we control).

## Decision 2 — Context management: let the model choose pages, hold it to evidence

(ADR-0002, ADR-0005)

Documents are 100-200 page PDFs; six can be in scope for one case. Nothing
fits in one window and most pages are irrelevant. Version one assembled
context deterministically: retrieval nominated pages, a fixed budget picked
them, models never chose. It was good enough for numbers — and it exposed
the project's central finding, **page starvation**: on the judge's
narrative checklist ("does the note state the bank's own why"), the open
loop scored ~0, because the why-layer lives on pages retrieval never ranks
(audited notes in appendices, footnote targets, divisional sub-splits).

The five-arm bake-off isolated the cause. Four anchor cases, one judge
protocol, identical for every arm:

| arm | loop | checklist | movement | cost/case |
|---|---|---|---|---|
| cheap pipeline | open | 0/15 | 4/4 | $0.002-0.005 |
| glm-5.3 author, same context | open | 1/15 | 4/4 | $0.22-0.86 |
| Sonnet agentic | closed | 6/15 | 4/4 | ~40k tokens |
| Fable agentic | closed | 3/15 | 4/4 | ~25k tokens |
| Codex agentic | closed | 1/15* | 4/4 | quota |

*Codex's row carries 5 judge flags and a citation-style interaction; its
numbers match gold with zero residual.

The glm control row is decisive: a reasoner ~100x the price, on the same
starved context, gained one checklist item. The gap is the loop, not the
tier — closed-loop arms follow references while reasoning (the exemplar is
CBA's Note 2.2 on PDF p118, which decomposes the impairment movement
exactly and is reachable only by reading "refer Note 2.2" on the income
statement; retrieval ranks it near zero for every query).

So the decision: context is assembled BY the model, INSIDE the loop, under
never-guess rules — and the deterministic estate holds it to evidence at
every step. Budgets (80 tool calls, $1, 30 minutes) are runaway rails, not
steering; the build round measured that a rail that shapes a run violates
the design, so they sit far above observed need. Two depth mechanisms were
added after the sealed exam priced the remaining gap as retrieval depth:
the research plan the loop reads back, and the query fan (both general —
the model steers itself; code holds it to its own commitments). On the
sealed exam they lifted location coverage 73% -> 82%, strongest on the two
weakest answers.

Cost of the trade: the loop is slow. A per-call latency measurement run
during development showed ~97% of wall time inside model requests —
glm-flash thinks for 20-300 seconds per call across 25-80 calls. That is
the accuracy flagship's price; the `fast` combo answers in ~4 minutes for
evaluators who need the machine to move.

## Decision 3 — Memory: a versioned registry, not a vector store

(ADR-0003)

What the system remembers between runs is exactly what a sector analyst
carries between reporting seasons: how each bank talks. The registry
(`registry/*.json`) maps each bank's verbatim disclosure labels to a
canonical driver taxonomy — walk-bar names, basis vocabulary, calendar
balance dates. Two properties are load-bearing:

1. **No financial numbers.** The registry stores language, never values. A
   remembered number is a leak waiting to contaminate a fresh case; a
   remembered label is just vocabulary. This rule made the holdout design
   defensible, and it shaped the sealed bank too: Macquarie's registry is a
   deliberate skeleton (names and calendar only), because distilling its
   language after the exam questions were authored could steer the agent.
2. **Versioned and reviewable.** The registry is JSON in git. Every
   addition is a diff a reviewer can read.

Session memory lives in the artifacts: every answer carries provenance
(models, document hashes, cost, seconds) and its full
evidence records, so any claim is auditable months later without rerunning
anything. Process memory is the wayfinder map plus tickets.

Rejected: a vector store of "learned facts" (unauditable,
contamination-prone); fine-tuning (nothing here needs weights; everything
needs provenance).

## Ruling — the two answer shapes hold evidence to different standards (user, 2026-09-01)

A metric case and a free question run the same research loop but face
different code checks, on purpose.

- A metric case asks for a known shape: one movement and drivers that each
  carry one number. Because we know the shape, the code checks it hard: a
  claimed number must appear in the quotes it cites, or its confidence
  drops to 80; a movement no cited record states caps at 20.
- A free question has no fixed shape. A fact is a full sentence; it can
  hold several numbers or a phrase like "roughly doubled". A hard number
  check here would be fragile and would punish good answers. So the code
  checks only that every citation points at a real, word-for-word quote,
  and the judges check every fact against its quotes during evals.

In short: where we know what the answer must contain, code enforces it.
Where we do not, we keep the checks loose rather than over-engineer ones
that break on honest prose.

## Decision 4 — Evals: calibration first, judges second, holdouts sealed

(`docs/design/eval-review-guide.md`)

The eval harness answers three questions in order of importance:

1. **Is a stated number right?** Gold cases carry values page-sighted in
   primary disclosure with printed provenance strings. Scoring is
   three-state (correct / incorrect / unscored) with the GRADER'S OWN
   tolerances (deliberately not shared with the product's validators, so a
   loosened product tolerance surfaces as eval failures); coherent
   alternative framings score as variants; an unverified gold value is
   quarantined, never graded; an invented taxonomy child cannot fill a
   parent slot.
2. **Is confidence honest?** Confidence is a single 0-100 self-report that
   code can only cap downward (fatal check -> 40; a claim whose quotes do
   not print its number -> 80; a movement no cited record states -> 20; an
   ungrounded answer -> 20). Overrides are sparse and each carries its
   experiment: the single-source cap was deleted when a replay measured it
   capping already-capped claims, and the caps-off ablation
   (`evals/results/audits/capsoff-*`) measured the raw self-report rates
   the scorecards disclose beside every confidently-wrong number. Final:
   dev Brier 0.039, holdout 0.015, confidently-wrong 0.0 everywhere for
   the flagship — across 33 graded movement cases the two wrong movements
   both self-reported confidence 0.
3. **Does the narrative say true things?** The judge protocol asks two
   narrow questions per fact — does the note state it, and do the cited
   quotes entail it — each to two judge models from different families.
   Only stated-AND-entailed passes; disagreement flags a human; a fail
   under a truncated quote or answer window flags rather than counting
   against the answer (an evaluator budget shortfall is not an answer
   error).

The holdout estate is layered because iteration contaminates: 25 dev cases
(iterated on freely), 8 frozen in-repo holdout cases (run once at the
freeze: 7/8 movements, Brier 0.015, the one miss at confidence 0), and a
sealed 10-question Macquarie exam authored by an independent model against
documents alone, held outside the repository, and administered twice under
a freeze-first protocol: the frozen agent (73% location coverage) and the
final agent (82%). One disclosure stands: the coordinator accidentally saw
the gold for one question; the agent never did, and that question's marks
carry the caveat in both scorecards.

Rejected: LLM-judge-only scoring (coverage is not correctness); a single
blended quality score (it hides exactly the confidently-wrong tail we care
about); historical holdout claims (no repo-resident case predates
iteration, so we refuse to call any of them pristine).

## Costs

Whole project: ~USD 230 of OpenRouter spend, dominated by the frontier
bake-off arms and judge runs; the product itself answers a case for
$0.01-0.13 in 6-30 minutes (flagship) or ~$0.01 in ~4 minutes (fast). The
frontier ceiling stays ~100x the flagship's price per case; the system's
job was to close the insight gap without paying that gap in price, and the
sealed exam measures how much of it closed.
