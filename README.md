# ai-bank-equity-researcher

An agent that does first-pass equity research on Australian banks.

You give it a bank, a reporting period, and a headline metric. It explains
how that metric moved against the prior comparable period, breaks the
movement into drivers, and gives each claim a confidence score with quotes
from the bank's own documents as evidence.

**Metrics in scope:** net interest margin, cash earnings, return on equity,
CET1 ratio, credit impairment charge, cost-to-income ratio. All figures in
AUD. Periods follow each bank's own financial calendar.

## Results at a glance

| Suite | Movements | Brier | Confidently-wrong | Cost/case | Note |
|---|---|---|---|---|---|
| Dev (25 cases, CBA/NAB/WBC) | 24/25 | 0.039 | 0.0 | $0.01–0.13 | the one miss gave itself confidence 0 |
| Holdout (8 frozen cases, incl. FY21 era) | 7/8 | 0.015 | 0.0 | $0.01–0.08 | the one miss gave itself confidence 0 |
| Sealed exam (10 questions, Macquarie, unseen bank) | 10/10 answered | — | — | ~$0.05 | found 82% of required pages, stated 78% of gold facts |

The design goal is one-sided on purpose. A wrong answer at low confidence
is a research lead. A wrong answer at high confidence gets an analyst
fired. So confidence is a score the model gives itself, code can only push
that score down (never up), and the harness tracks wrong-but-confident
claims as their own number so they can never hide inside an average.
Across every suite above, no wrong claim ever shipped at confidence 85 or
higher — both wrong movements gave themselves confidence 0.

The narrative layer has its own graded numbers, from the two-judge
protocol over the same runs: the reports state 57 of 84 (68%) of the gold
explanations across dev and holdout, and 19 of 84 (23%) clear the strictest
bar — both judges agree the note states the fact AND every load-bearing
number appears in the cited quotes. 25 items were flagged to human review
on judge disagreement rather than force-scored. The sealed exam showed the
same shape (78% stated, 32% fully grounded). Quote-completeness is the
system's weakest column and the first target in Next steps. Scorecards:
`evals/results/*-judge.md`.

There is also a speed option (`--combo fast`): about 4 minutes a case. Its
movement numbers hold, but it let one wrong claim ship at high confidence
on the dev suite (rate 0.026 vs the default's 0.0). That trade is written
up in `evals/results/fast-*-finalcode.md`.

Every scorecard is in `evals/results/`. The main ones: the dev baseline,
`agentic-holdout-final.md`, and the two sealed-exam cards
(`mqg-exam-frozen-20260902.md`, `mqg-exam-resit-20260902.md`).

## Quick start

```bash
# 1. Install (Python 3.12+, uv)
uv sync

# 2. Provide an OpenRouter key
echo 'OPENROUTER_API_KEY=sk-or-...' > .env

# 3. Download the documents listed in the committed manifests
set -a && source .env && set +a
uv run python scripts/fetch_corpus.py

# 4. Run a case
uv run bank-equity-researcher analyse --bank CBA --metric nim --period FY26
# -> out/cba-nim-fy26-vs-fy25-agentic/{report.md, attribution.json}
# The default model (glm-5.3-flash) takes 6-30 minutes a case. It is the
# most accurate option. In a hurry, add `--combo fast`: ~4 minutes and
# ~$0.01 a case, less accurate on the "why" layer.

# 5. Run the eval harness
uv run bank-equity-researcher evals run --suite dev --combo agentic
# -> evals/results/<stamp>-agentic-dev.md (scorecard) and .jsonl (detail)
```

`analyse` picks the comparison period automatically (a full year compares
to the prior full year, a half to the prior comparable half); override with
`--comparator`. `ask` answers a free-form question from the same documents
with the same citation rules. `discover` builds the document list for a new
bank by browsing its investor-relations pages; `manifest/anz.json` was
built this way.

## What an output looks like

`out/<case>/report.md` is the analyst note: the movement, the driver table
with a confidence score per driver, short narratives grounded in the bank's
own words, the unexplained residual, any disagreements between sources,
limitations, and citations (document, PDF page, word-for-word quote).
`attribution.json` is the same content in machine-checkable form, plus a
record of how it was made: models used, document content hashes, cost, and
every evidence record. Any claim can be audited months later without
rerunning anything.

## How it works, in one paragraph

One tool-calling model researches in a loop. Its tools: `plan_research`
(say where the answer should live before searching), `search_pages` (find
pages by keyword and by meaning), `read_page`, `read_chart` (read waterfall
charts from the page image), `cite` (turn quotes into evidence records —
each quote is checked word-for-word against the page, and a paraphrase is
rejected), `follow_references` (jump to "refer Note 2.2"-style pointers,
where the "why" usually lives), `bank_language` (the bank's own names for
things), and `submit`. The model is never allowed to guess: every number in
the answer must trace to a checked quote. After submit, code validates the
answer — walk arithmetic, units and signs, comparison checks, tolerances —
and any failed check is shown in the output and pushes confidence down,
never hidden. Budgets on tool calls, cost, and time exist only to stop a
runaway; they are set high enough that a normal run never touches them. The
full reasoning behind these choices is in [DESIGN.md](DESIGN.md).

## Evals

Gold answers were built by hand: each value was sighted on a printed page
of the bank's own documents, and the page is recorded next to the value.
Scoring has three states — correct, incorrect, or unscored (when the gold
cannot verify a claim, it is left out rather than guessed at). If a bank
publishes two valid ways to split a movement, both count. Narrative claims
are graded by two judge models from different companies: a fact passes only
if the note states it AND the cited quotes back it up; if the judges
disagree, a human is flagged instead of a tie-break. The test sets are
layered to prevent contamination: a dev set (iterated on freely), a frozen
holdout (run once at a code freeze), and a sealed exam held outside the
repository (written by an independent model, run once at the end).
DESIGN.md's appendix records the judgment calls.

## Next steps (designed, not built)

Ideas from the failure analysis. Each is written down here instead of
built, so the current system stays simple and measured.

- **Frontier planner, cheap researcher.** Have a stronger model write the
  research plan (one short call), then let the cheap model do the research
  against it. The plan is where depth is decided; carrying it out is
  bookkeeping the cheap model already does well.
- **Measure the plan step's own lift.** Rerun the suites with
  `plan_research` turned off and compare scorecards, so the step's cost is
  priced against its gain.
- **A quote-completeness nudge for questions.** At submit, list any stated
  number that no cited quote prints, and ask once for the quote or a
  limitation. A nudge-and-retry, never a deletion — the hard version was
  ruled out because it would punish honest prose (see DESIGN.md, "the two
  answer shapes").
- **A cheap checker pass.** A second cheap-model call that reads only the
  draft answer and names unquoted claims and unopened documents, feeding
  one revision. Checking is easier than writing for small models.

## Layout

- `src/bank_equity_researcher/` — plain Python: `agent/` (the research
  loop), `tools/` (documents, retrieval, references, chart reads,
  discovery), `validation/` (the answer contract and its checks),
  `judging/`, `evals/`, and shared top-level modules (cli, config, llm,
  render, taxonomy)
- `DESIGN.md` — the design doc: the four owned decisions
- `manifest/` + `scripts/fetch_corpus.py` — document sources; `data/` is
  gitignored and rebuilt from the manifests
- `registry/` — per-bank language maps (labels, never numbers)
- `evals/gold/` + `evals/results/` — gold cases and every scorecard
- `out/` — case artifacts, generated locally per run (gitignored)
- `tests/` — 450 tests, all offline
