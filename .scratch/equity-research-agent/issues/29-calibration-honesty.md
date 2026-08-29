# 29 — Calibration and reporting honesty (Codex findings 2, 9, 10, 11, 12)

Type: task
Status: open

## Question

Make the reports claim only what the data supports (docs/reviews/codex-eval-review-2026-08-27.md):

1. **Coverage first (finding 2)**: every scorecard leads with the evaluable populations — cases run/crashed, claims scored/unscored/abstained — then reports movement, driver, and whole-attribution calibration as SEPARATE populations. High-confidence movement failures must enter a calibration population (currently invisible to Brier).
2. **Uncertainty (finding 9)**: report raw numerators, Wilson intervals, and case-cluster structure with every rate; label single-run numbers "descriptive for this run only". No externally-quoted calibration claim without repeated runs and case-cluster bootstrap.
3. **Scorecard metadata (finding 10)**: record commit hash, model IDs, case manifest, gold-file hash, and retry policy in every scorecard header so runs are comparable experiments.
4. **Threshold boundary (finding 11)**: decide whether the single-source cap value (85) belongs inside the confidently-wrong population; align the cap and the threshold so a capped claim is not automatically "confident" (e.g. cap to 84 or threshold to >85), and document the choice.
5. **Per-check reporting (finding 12)**: report each deterministic check's outcome by name and stage (pass/fail/not-applicable), not a lossy count of "Failed check:" strings.

## Progress 2026-08-29: the citation-grounding judge is landed

The judge is built, tested and run end to end on the saved dev artifacts. It closes
ticket 30 item 2 (finding 7, "coverage is not correctness") and it carries
three pieces of this ticket's honesty work: coverage first (finding 2), the
descriptive-for-this-run label (finding 9), and the scorecard header (finding
10).

Items 1, 3, 4 and 5 of this ticket are NOT done. Only the judge landed.

### What the judge does

`src/bank_equity_researcher/judge.py` is new. One gold fact gets two narrow
questions, and each question goes to both judges in `config.Combo.judges` —
`deepseek/deepseek-v4-pro-0813` and `qwen/qwen3.7-flash`, two model families:

1. Does the answer state this fact? `stated` | `partial` | `absent`
2. Do the cited quotes entail this fact? `entailed` | `not-entailed`

The two questions are two separate calls. One call is cheaper, but the judge
then reads its own "stated" answer before it rules on entailment, and a note
that states a fact well drags the entailment answer with it. Separate calls
keep the grounding question independent of the fluency question. Temperature is
0 and both replies are parsed strictly through `llm.chat_json`.

Verdict rules, in order:

- An unreadable reply flags the fact for a human. A reply flags when it does
  not parse, when the key is missing, when the value sits outside the
  vocabulary, or when the call fails. A judge that cannot answer the question
  is not evidence that the answer is right.
- Judges that disagree ON THE VERDICT flag the fact for a human. There is no
  tie-break. One judge saying `partial` while the other says `absent` is NOT a
  verdict disagreement: both say the note does not state the fact, and the item
  fails under either reading. A human is flagged for a decision the judges
  could not make, never for a difference of wording. The split is still
  recorded in the verdict reason.
- Both judges agreeing on `stated` AND `entailed` is a pass.
- Any other agreement is a fail.
- Empty citations are `not-entailed` without a call. Nothing cannot entail
  anything, and paying a model to confirm that wastes money.

The judge reads the note's own prose and the quotes the note cites, never a
whole document. `answer_prose` strips the quote lines and the provenance block
from report.md: a note that pastes a supporting quote has not itself stated the
fact, and a judge reading both cannot tell the two apart. The answer window is
6000 characters and truncation is recorded in the verdict, so an absent fact is
distinguishable from a fact that fell off the end.

### Item 2 of ticket 30: the crossref fact check is real

`score_crossref` now reports two populations and never blends them:

- **Location coverage** — the share of gold `required_locations` the answer
  cited. It measures the retriever.
- **Fact accuracy** — the share of `gold_answer_facts` the judges rule BOTH
  stated by the answer AND entailed by its cited quotes.

A case carries `passes` only when coverage is 100% and fact accuracy is at
least 75% (`CROSSREF_COVERAGE_PASS`, `CROSSREF_FACT_PASS`, both commented at
the constant). An unjudged case gets `passes: None` — not decidable is not
passing. The scorecard prints both columns, the flagged count, and every judged
fact with its reason.

The crossref holdout suite was NOT run. It stays frozen for a milestone.

### Item 3: narrative checklist grading for dev cases

`evals judge --suite dev` grades every dev case's `narrative_checklist` against
its SAVED `out/<slug>/` artifact. It reads `report.md` and `attribution.json`,
runs no pipeline stage, and fetches no document. The only model calls are the
judges'.

This makes the gold README's promise executable: "checklist items are never
value-scored; they are graded by citation-grounding (does the note say it, and
does the cited page support it)". Before today the harness ignored them.

### Tests

`tests/test_judge.py` mocks both judge models and table-tests the verdict
logic. Every row names the mistake it stops: agreement pass, agreement fail,
verdict disagreement, wording split, malformed reply in four shapes, an
unreachable judge, and empty citations. Two crossref rows show the finding-7
counterexample directly — full location coverage with judged facts failing does
NOT pass the case. `uv run pytest -q`: 83 passed.

### The run

```
uv run bank-equity-researcher evals judge --suite dev --combo cheap
```

`evals/results/20260829-0438-cheap-dev-judge.md` and its `.jsonl`. 170 judge
calls, USD 0.0791, about 13 minutes. No pipeline call and no document fetch.

- cases in the dev suite: 25; cases judged: 15; cases not judged: 10 (no saved
  artifact — the NAB and WBC FY25 dev cases landed in gold today)
- checklist items judged: 43
- **items passed: 1/43 (2%)**
- stated but not entailed: 4; not stated: 32
- flagged: 6 — 4 judge split, 2 unreachable judge

An earlier run at 20260829-0425 is kept beside it. It ran the same protocol and
gave the same picture, with three extra flags from a transient DNS failure. The
two runs together are the only repeatability evidence there is, and it is thin.

### What the run found

The judge works and the reports fail it. 1/43 is a measurement of the NARRATIVE
layer only. The numeric scorecard is unaffected and unchanged: the frozen dev
baseline still reads 15/15 movements OK, Brier 0.058.

1. **The reports do not carry the "why" layer.** 32 of 43 items are `absent` or
   `partial`: the note names the driver and its bps, but drops the sub-split,
   the footnote, or the comparison the checklist asks for. Example: CBA ROE
   1H26 never mentions statutory ROE beside cash ROE, and never mentions the
   2025 final DRP $643m on-market purchase. This is a concrete iteration target
   for ticket 22 (narrative enrichment), and it is the first time the harness
   can see it.
2. **Where the note DOES state the reason, its cited quotes often do not carry
   it.** 4 items are stated but not entailed. That is the ungrounded-narrative
   failure the judge exists to catch. Example: CBA NIM 1H26 states "portfolio
   mix +1" and both judges agree the note states it, but the cited quotes never
   carry the +1 or the at-call deposit growth behind it.
3. **The evidence set, not the author, is the deeper bottleneck.** Several
   checklist facts sit on pages the pipeline never extracted (PA p48 dividend
   footnotes, slide 24 and slide 27 income and investment-spend tables). The
   author cannot state what it was never shown. This repeats the ticket 25 root
   cause: page starvation.
4. **The one pass shows the judge is not stuck.** CBA CET1 FY26 states the 2026
   interim dividend $530m on-market purchase and its -10bpts CET1 impact, and
   the quotes it cites carry both numbers. Both judges rule it stated and
   entailed. The judge also returned `stated` 5 times and `entailed` 4 times
   elsewhere, so neither vocabulary is dead.
5. **The two judges agree far more than they split.** 4 splits in 43 items, and
   3 of the 4 sit on `partial` against `stated` — the boundary of "how much of
   the fact must the note carry". They split on entailment once.
6. **Two items were flagged by an unreachable judge, not by judgement.** The
   flag behaviour is correct — a judge that cannot answer is not evidence that
   the answer is right — but it is a rerun signal. The scorecard counts judge
   splits and unreachable judges apart for that reason.

### Open, and deliberately not done here

1. **A human has not adjudicated the flagged items.** The judge produces the
   queue; it does not close it. The flagged facts are the HITL work.
2. **The checklist rate has no repeat run and no case-cluster bootstrap.** The
   scorecard says so on its face and labels the number descriptive for this run
   only (finding 9). Do not quote it outside the repo.
3. **The pass thresholds are asserted, not measured.** `CROSSREF_FACT_PASS` is
   0.75 by argument, not by evidence. The user should ratify both crossref
   thresholds.
4. **10 dev cases have no artifact.** The NAB and WBC FY25 dev cases landed in
   gold today and no pipeline run has produced their artifacts yet. The
   scorecard reports them as not judged rather than as zeros.
5. **The remaining items of this ticket (1, 3, 4, 5) are untouched.** Only the
   judge landed. Item 3 is partly served: `scorecard_meta` now stamps commit,
   gold hash and model ids on the crossref and judge scorecards, but not yet on
   the metric scorecards.
6. **The `stated` boundary needs a decision.** The judge splits concentrate on
   `partial` against `stated`. If a note that names the driver without the
   sub-split should count as stating the fact, the checklist gold needs
   splitting into the reason and its magnitude; if not, the current strictness
   is right. This is a gold-design call, not a judge bug.

### Files

- `src/bank_equity_researcher/judge.py` — new; the judge, the verdict rules and
  the artifact adapters.
- `src/bank_equity_researcher/evals.py` — the real crossref fact check, the
  `passes` rule and its two constants, `run_judge_suite`, `scorecard_meta`,
  `artifact_dir`, `run_stamp`.
- `src/bank_equity_researcher/cli.py` — the `evals judge` action.
- `tests/test_judge.py` — new; the verdict table with mocked judges.
- `CONTEXT.md` — three glossary entries: citation grounding, narrative
  checklist, location coverage.
- `evals/results/20260829-0438-cheap-dev-judge.{md,jsonl}` — the run.

