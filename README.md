# ai-bank-equity-researcher

An agent that does first-pass banking-sector equity research on Australian banks.

Given a bank, a reporting period, and a headline metric, the agent explains how
the metric moved against the prior comparable period, attributes the movement to
drivers, and produces a confidence-rated attribution that cites the evidence
behind each driver.

**Metrics in scope:** net interest margin, cash earnings, return on equity, CET1
ratio, credit impairment charge, cost-to-income ratio. All figures in AUD.
Periods follow each bank's own financial calendar.

## Results at a glance (closed-loop agent, final code)

| Suite | Movements | Brier | Confidently-wrong | Cost/case | Note |
|---|---|---|---|---|---|
| Dev (25 cases, CBA/NAB/WBC) | 24/25 | 0.039 | 0.0 | $0.01–0.13 | the one miss self-reported confidence 0 |
| Holdout (8 frozen cases incl. FY21 era) | 7/8 | 0.015 | 0.0 | $0.01–0.08 | the one miss self-reported confidence 0 |
| Sealed exam (10 questions, Macquarie, unseen bank) | 10/10 answered | — | — | ~$0.05 | location coverage 82%, facts stated 78% |

The design goal is asymmetric: a low-confidence wrong answer is a research
lead; a high-confidence wrong answer is a fired analyst. Confidence is a
single self-report that code can only cap downward, and the harness tracks
the confidently-wrong tail separately so it can never hide inside an
average. Across every suite above, no wrong claim ever shipped at
confidence 85+ — both wrong movements declared confidence 0 themselves.

A speed option exists (`--combo fast`, deepseek-v4-flash in the same loop,
~4 min/case): its movements hold but it breaks the confidently-wrong
guarantee on dev (0.026 vs the flagship's 0.0) — the trade is documented in
evals/results/fast-*-finalcode.md.

Scorecards: `evals/results/` (dev baseline, `agentic-holdout-final.md`,
`mqg-exam-frozen-20260902.md`, `mqg-exam-resit-20260902.md`). Artifacts are
generated locally per run under `out/` (gitignored).

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
# -> out/cba-nim-fy26-vs-fy25-agentic/{report.md, attribution.json}
# The default combo (glm-5.3-flash) takes 6-30 minutes a case; that is the
# accuracy flagship. In a hurry, add `--combo fast` (deepseek-v4-flash in the
# same loop): ~4 minutes and ~$0.01 a case. Movement numbers hold across both;
# the insight layer is the difference — on the hard-question probe the fast
# arm found 0/3 required pages where the default covered 11/15 across the
# suite (evals/results/20260831-0916-agentic-ds-questions.md).

# 5. Run the eval harness
uv run bank-equity-researcher evals run --suite dev --combo agentic
# -> evals/results/<stamp>-agentic-dev.md (scorecard) and .jsonl (detail)
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

A closed-loop research agent (`research_agent.py`) drives the analysis: one
tool-calling model navigates the corpus with a small tool set —
`search_pages`, `read_page`, `read_chart`, `cite`, `follow_references`,
`bank_language`, `submit` — under never-guess rules. Code owns everything
known: manifests, retrieval, the verbatim-citation gate at `cite` time, walk
arithmetic, unit and sign conventions, comparison classification, tolerance
checks, and confidence caps. Everything the agent produces is checked by
arithmetic against cited evidence; failed checks surface in the output and
cap confidence, never silently dropped. Budgets (tool calls, cost, wall
clock) are runaway rails, not steering. The full rationale lives in [DESIGN.md](DESIGN.md).

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
milestone. DESIGN.md's appendix records the judgment calls.

## Next steps (designed, not built)

Ideas the failure analysis produced. Each is written down here instead of
built, so the current system stays simple and measured.

- **Frontier planner, cheap researcher.** `plan_research` is the highest
  leverage point per token: have a frontier model write the plan (one short
  call), then let the cheap model execute the research against it. The plan
  is where depth is decided; execution is bookkeeping the cheap model
  already does well.
- **Measure the plan step's own lift.** Rerun the dev and holdout suites
  with `plan_research` disabled and compare scorecards, so the mechanism's
  cost (one bounce per case) is priced against its coverage gain.
- **A quote-completeness bounce for questions.** At submit, list any stated
  number that no cited quote prints and ask once for the quote or a
  limitation. A bounce-and-retry, never a strip — the hard version was
  ruled out as fragile for free prose (see DESIGN.md, "the two answer
  shapes").
- **A cheap verifier pass.** A second cheap-model call that reads only the
  draft answer and names unquoted claims and unopened documents, feeding
  one revision. Critique is easier than generation for weak models.

## Layout

- `src/bank_equity_researcher/` — plain Python: `agent/` (the closed loop),
  `tools/` (corpus, retrieval, references, chart reads, discovery),
  `validation/` (the contract and checks), `judging/`, `evals/`, and
  cross-cutting top-level modules (cli, config, llm, render, taxonomy)
- `DESIGN.md` — the design doc: the four owned decisions
- `manifest/` + `scripts/fetch_corpus.py` — document sources; `data/` is
  gitignored and rebuilt from the manifests
- `registry/` — per-bank disclosure-language maps (labels, never numbers)
- `evals/gold/` + `evals/results/` — gold cases and every scorecard
- `out/` — case artifacts, generated locally per run (gitignored)
- `tests/` — the executable specification (450 tests, offline)
