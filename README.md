# ai-bank-equity-researcher

An agent that does first-pass banking-sector equity research on Australian banks.

Given a bank, a reporting period, and a headline metric, the agent explains how
the metric moved against the prior comparable period, attributes the movement to
drivers, and produces a confidence-rated attribution that cites the evidence
behind each driver.

**Metrics in scope:** net interest margin, cash earnings, return on equity, CET1
ratio, credit impairment charge, cost-to-income ratio. All figures in AUD.
Periods follow each bank's own financial calendar.

## Results at a glance (dev suite, 25 cases across CBA / NAB / WBC)

| Measure | Value |
|---|---|
| Movements correct | 25/25 |
| Claims at confidence 85+ correct | 36/36 (100%) |
| Confidently-wrong rate (wrong claims at 85+) | 0.0 |
| Brier score | 0.035 |
| Cost per case | USD 0.002–0.005 |
| Wall time per case | 1–3 minutes |

The design goal is asymmetric: a low-confidence wrong answer is a research
lead; a high-confidence wrong answer is a fired analyst. Confidence is a
single self-report that code can only cap downward, and the harness tracks
the confidently-wrong tail separately so it can never hide inside an average.

A five-arm bake-off (cheap pipeline, stronger-reasoner control, and three
frontier agents) showed movement numbers are tier-independent while the
"why" layer is loop-dependent — the full story and the decision it produced
are in the [design doc](docs/design.md).

## Quick start

```bash
# 1. Install (Python 3.12+, uv)
uv sync

# 2. Provide an OpenRouter key
echo 'OPENROUTER_API_KEY=sk-or-...' > .env

# 3. Rebuild the document cache from the committed manifests
set -a && source .env && set +a
uv run python scripts/fetch_corpus.py

# 4. Run a case
uv run bank-equity-researcher analyse --bank CBA --metric nim --period FY26
# -> out/cba-nim-fy26-vs-fy25-cheap/{report.md, attribution.json}

# 5. Run the eval harness
uv run bank-equity-researcher evals run --suite dev --combo cheap
# -> evals/results/<stamp>-cheap-dev.md (scorecard) and .jsonl (detail)
```

`analyse` picks the comparator automatically (FY → prior FY, half → prior
comparable period); override with `--comparator`. `ask` answers a free-form
question from the corpus with the same citation discipline. `discover`
agentically builds a manifest for a new bank; `manifest/anz.json` was built
this way and is the unseen-bank test path.

## What an output looks like

`out/<case>/report.md` is the analyst note: movement, basis, driver table
with per-driver confidence, narratives grounded in the bank's own words,
residual, disagreements between sources, limitations, and citations
(document, PDF page, verbatim quote). `attribution.json` is the same content
as a machine-checkable contract, plus provenance: models used, document
content hashes, cost, seconds, and every evidence record — any claim is
auditable months later without rerunning anything.

## How it works, in one paragraph

Code owns everything known: manifests, retrieval, page budgets, deterministic
reference-following (notes and footnotes are followed by code, not by a
model), walk arithmetic, unit and sign conventions, comparison
classification, tolerance checks, and confidence caps. Cheap models do three
narrow jobs — extract facts from a page, read waterfall charts, assemble the
attribution under never-guess rules — and everything they produce is checked
by arithmetic against cited evidence. Failed checks surface in the output
and cap confidence; they are never silently dropped. The full rationale
lives in the [design doc](docs/design.md) and the ADRs.

## Evals

Gold cases carry values page-sighted in primary disclosure with printed
provenance strings. Scoring is three-state (correct / incorrect / unscored)
with per-unit tolerances; coherent alternative framings score as variants;
an unverified gold value is quarantined, never graded. Narrative claims are
graded by a two-judge protocol (different model families): a fact passes
only if the note states it AND the cited quotes entail it; judge
disagreement flags a human. The holdout estate is layered — dev cases,
a frozen in-repo quarantine slate designed by an independent model, and a
sealed case set held outside the repository, administered once at the final
milestone. `docs/design/eval-review-guide.md` documents every judgment call.

## Layout

- `src/bank_equity_researcher/` — the agent (~12 files of plain Python)
- `docs/design.md` — the design doc: the four owned decisions
- `docs/adr/` — architecture decision records
- `docs/design/` — driver taxonomy, frontier benchmarks, eval review guide
- `CONTEXT.md` — the domain glossary (walk vs bridge, bases, conventions)
- `manifest/` + `scripts/fetch_corpus.py` — document sources; `data/` is
  gitignored and rebuilt from the manifests
- `registry/` — per-bank disclosure-language maps (labels, never numbers)
- `evals/gold/` + `evals/results/` — gold cases and every scorecard
- `out/` — case artifacts, including the frontier benchmark arms
  (`out/baseline-*`)
- `.scratch/equity-research-agent/` — the wayfinder map and the full
  decision history (32 tickets)
