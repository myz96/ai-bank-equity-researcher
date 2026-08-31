# 33 — Pre-submission cleanup: simplify code, restructure the package

Type: task
Status: open (user-requested 2026-08-30)

## Question

The repo grew by accretion: pipeline rounds, a bake-off, a pivot to the
closed-loop agent (ADR-0005), and ~30 result files. Before the project is
presented, run a cleanup round so a reviewer can navigate it cold. The user's
ask, verbatim in spirit: run code-simplification subagents to clean the
architecture, remove duplicate functions, and move files into folders that
say what they are — agent, tools, validation, judging, evals.

## Scope

1. **Simplification sweep (delegated subagents, gated as usual).**
   - Duplicate-function sweep across `src/bank_equity_researcher/` — the
     pipeline and the research agent both wrap the same estate; collapse any
     copies into one shared function.
   - Dead-code sweep after the pivot: paths the agent shell made unreachable.
     The open-loop pipeline itself STAYS (it is the measured baseline arm);
     dead code is smaller than that.
   - Over-engineering check against ADR-0005: general and simple; anything
     clever-and-brittle gets flagged, not silently rewritten.
2. **Package restructure** (behaviour-neutral, moves only, imports updated):
   - `agent/` — research_agent (the closed-loop shell)
   - `tools/` — retrieve, extract, refs, corpus, render
   - `validation/` — validate, schema
   - `judging/` — judge
   - `evals/` (harness code) — evals
   - root keeps cli, config, llm, pipeline (baseline shell), taxonomy
   - Exact grouping is the executor's call; the test is "a stranger finds
     the file from its folder name".
3. **Repo-level tidy:** archive old scorecards under `evals/results/archive/`
   (keep the frozen baseline, the bake-off files, and the latest cards at the
   top level); prune `tmp/`; check `prototypes/` is labelled as history.

## Input 2: the unpreconditioned necessity audit (2026-08-31)

`docs/reviews/necessity-audit-20260831.md` — fresh-eyes, barred from every
prior finding list, quantified against all 90 saved artifacts. Its 15
findings and its hardcoded-override register (evidence-backed-and-firing /
evidence-backed-never-fires / unevidenced / unnecessary) are this ticket's
SECOND backlog, alongside the Codex critique. Its five named ablations gate
the deletions: never-firing checks, the caps-off experiment (running
2026-08-31), reference-following re-ablation, citation-parser upstream
instrumentation, and pipeline-freeze-at-tag. Also fix before submission:
README metric drift (finding 12) and the judge MAX_QUOTES=24 window that
binds on 25/90 metric artifacts while the questions suite got 48.

## Input: the Codex architecture critique (2026-08-30)

The user commissioned an independent Codex critique in a parallel session;
it is saved at `docs/reviews/codex-architecture-critique-2026-08-30.md`
(brief beside it) with file:line evidence per finding. It IS this ticket's
backlog. Highlights:

- Finding 1 (eval routing bug) was FIXED immediately (runner_for in
  config.py, test added) because it corrupted any suite-level agent eval.
- The "delete or merge today" list (findings 2-8): merge the two shells'
  finalisation policy (~180-260 lines), restrict submit citations to
  cite-minted ids, generate tool schemas with Pydantic, delete dead
  contract fields, drop automatic corroboration-disagreement synthesis,
  prune unused registry metadata, move baseline-only retry helpers out of
  shared validate.py.
- NOT to delete without ablation: refs.py (the Note 2.2 regression is the
  must-pass), metric prompt trims, extraction scoring.
- The "load-bearing: do not cut" list at the end of the critique is the
  cleanup round's guardrail — paste it into every cleanup subagent brief.
- Under-tested validators named by the critique (annotate_walks,
  corroborate, check_comparison_leak, ...) get table-driven tests BEFORE
  they are moved.
- OVERRIDE AUDIT (user directive 2026-08-31): enumerate every hardcoded
  line that overrides agent self-judgment (caps, thresholds, forced rules); each must cite the experiment/run backing it in its
  comment (defect number, artifact, scorecard). One without traceable
  evidence is deleted. Overrides stay sparse by policy (validate.py docstring).

The user expects SEVERAL critique passes ("we will have to run a few of
these to make sure we actually capture everything") — re-run the critique
after the cleanup round and after the head-to-head settles the shells.

SCHEDULED (user, 2026-08-30, revised same evening): the holdout milestone
moved to Mon NIGHT, so this ticket executes Tue 2026-09-01 AFTER the
holdout run. Consequence: every cleanup change must be behaviour-neutral —
moves, dedupe, simplification with identical outputs. Gate: after the six
passes, a dev subset re-runs and must score identically to the holdout-run
commit; any behaviour delta reverts. The report cites the holdout commit.

## Constraints

- Moves and logic changes NEVER share a commit. Restructure commits are
  import-only.
- Tests stay green at every commit (226+ as of c22f3c0); artifact and CLI
  contracts unchanged; a suite spot-check (3 cases) after the move.
- SEQUENCING: after the agent build + head-to-head land, BEFORE the milestone
  code freeze — the sealed run must execute on the cleaned, frozen layout.
- The usual gates: leakage scan, no tolerance changes, coordinator commits.

## Cleanup execution, waves 1-3 (agent, 2026-08-31)

Spec: `docs/reviews/necessity-audit-20260831.md`. Guardrail: the "Load-bearing:
do not cut" list at the end of `docs/reviews/codex-architecture-critique-2026-08-30.md`.
Base commit ae0231f. Net: 420 insertions, 2075 deletions (-1655 lines); src
Python 9738 -> 8477 lines. Tests 430 -> 419, all green. Ruff errors 29 -> 27.

### Wave 1 — never-fired overrides and dead scaffolding: DONE

Deleted five overrides the estate never exercised (0 firings in 90 saved
attributions, verified by grep and by replay):

- `comparison_leak_cap_80` (validate.py) — the check still names the offender.
- `component_column_cap_80` (validate.py) — same.
- off-unit -> 60 (`drop_off_unit_contributions`) — the drop itself stays.
- stripped-claim -> 20 (`schema.enforce_evidence_gate`) — the strip stays.
- `corroborate`'s cross-source divergence branch, with the bare `gap <= 3`
  reason-picker inside it. `single_source` -> 85 and the `corroborated_N`
  marker are untouched.

Also deleted: the `render.py` dead `narrative` local, three `PRICES` entries no
combo names, the `agentic-luna` combo, and `__init__.hello()`.

Replay over all 90 saved artifacts: 340/340 cap decisions byte-identical, 64
capped, and all 19,936 quote/number verdicts identical.

### Wave 1 — finding 3 (unit-declaration subsystem): NOT CUT, and why

The audit's own gate PASSES: with the subsystem deleted, all 340 cap decisions
are still byte-identical. But the audit's unrun experiment 4 — what the
machinery prevents UPSTREAM, at the `extract.py` mint gate — comes back
non-zero. Measured both ways:

- 11 of 6,523 model-supplied NumberFacts in the estate change gate verdict, all
  one class: a `($bn)` row header read as `$m`, a 1000x scale error. Named
  artifacts: cba-cet1-1H26 ev-15, cba-cet1-FY21 ev-27 and ev-52, cba-roe-1H26
  ev-16, nab-cash_earnings-FY25 ev-26.
- 11 named regression tests fail, parameterised on those exact quotes:
  `test_a_billions_row_does_not_print_the_same_number_in_millions` (5 cases),
  `test_a_billions_row_does_not_state_a_millions_claim`,
  `test_a_percent_row_does_not_mint_a_dollar_fact`,
  `test_the_invented_dollar_fact_no_longer_survives_its_own_mint`,
  `test_a_basis_point_table_does_not_ground_a_points_claim` (2 cases, a
  factor-100 inversion).

Finding 3's "0 of 340" is true and is the wrong measurement: it reads the cap
path, and the subsystem earns its place on the mint path. Kept whole.

### Wave 2 — the five never-failing checks: NOT CUT, guardrail conflict

The critique names all five verbatim, in the do-not-cut list ("Wrong-column
detection at movement and component level"; "unit/sign/basis/variant handling
and the factor-100 identity correction") and again in its `validate.py` verdict
("Keep ... movement and component column checks, headline-variant/basis checks,
identity scaling"). Per the brief, this is a stop-and-record, so the
`evals run` gate was not spent.

Independent reason to keep them, found while checking the conflict: **the
zero-fail counts are an artifact of measurement position.** Each check runs
AFTER the corrector that repairs the exact defect it detects
(research_agent.py: `settle_ratio_scale` :1430 then `check_ratio_level` :1464;
`_settle_basis` :1364 then `check_movement_basis` :1469). Demonstrated on the
real NAB FY25 ROE submission, which the docstring records as `1160 -> 1140`:

    check_ratio_level(Movement(1160.0, 1140.0, -20.0, "ppt"), "ppt")
    -> failed: "movement_level_not_ratio_sized (1160 is not the level of a
       ratio stated in ppt; the ceiling is 200 ...)"
    check_ratio_level(Movement(11.6, 11.4, -0.2, "ppt"), "ppt")   # as stored
    -> passed: "movement_level_is_ratio_sized"

The estate only ever stores the corrected form. A 0-fail count over saved
artifacts therefore measures that the corrector works; it says nothing about
whether the check is dead. Finding 4 needs re-running against pre-correction
submissions before any of these five is cut.

### Wave 3 — pipeline freeze at tag: DONE

Tag `pipeline-baseline-final` -> ae0231f (annotated; re-point if the coordinator
commits wave 1 first). Deleted `pipeline.py` (661), `author.py` (505),
`ask.py` (289), `tests/test_pipeline_evidence.py` (204), the `cheap` and
`normal` combos, and the pipeline branch of `runner_for` /
`question_runner_for`. The crossref and questions suites now reach the agent
only. A retired combo name raises a `KeyError` naming the tag, so a run can
never measure the agent under a stale label; `evals rescore` still scores old
artifacts by slug, so nothing in the estate became unscoreable.

Relocated, not deleted:

- `validate.py` gains `default_comparator`, `_month_name`, `build_period_note`
  (from pipeline.py) and `_movement_source`, `_BASIS_WORDS`, `primary_basis`,
  `_basis_printed`, `drop_off_unit_contributions`, `settle_charge_sign`,
  `_settle_basis` (from author.py). Bodies unchanged.
- `render.py` gains `slugify` and `render_answer` (from ask.py).
- `extract.py` and `refs.py` untouched.
- `tests/test_author_normalisers.py` -> `tests/test_movement_normalisers.py`,
  with the relocated-function tests kept and re-pointed at `validate.py`. The
  delta-harmoniser test moved to `test_research_agent.py`, where the surviving
  copy of the harmoniser lives.

Gates, verbatim:

- `uv run pytest -q` -> 419 passed.
- `analyse --bank CBA --metric nim --period FY26 --combo agentic-cheap` -> ran
  clean: movement 208 -> 205 bps, 7 drivers, 0 failed checks, confidence 90, 36
  tool calls, $0.0334, budget_exhausted=no. The pre-existing artifact was saved
  and restored afterwards, so the estate is byte-identical and the dev
  scorecards stay reproducible.
- `evals rescore --suite dev --combo agentic-cheap --label wave3-rescore-check`
  -> reproduces `agentic-cheap-dev-final.md` exactly: all 25 case rows
  identical, scored_claims 34, unscored_claims 39, cases_scored 6, brier 0.039,
  confidently_wrong_rate 0.0, 70-84: 7 claims 86% correct, 85-94: 27 claims
  100% correct.
- Cap replay after wave 3: 340/340 and 19,936/19,936 identical to the ae0231f
  baseline.

### Kept instead of cut, with reasons

| item | reason |
|---|---|
| unit-declaration subsystem (finding 3) | 11 estate facts + 11 named regression tests; audit measured the cap path, the value is on the mint path |
| the five never-failing checks (finding 4) | named in the do-not-cut guardrail; zero-fail counts are post-corrector |
| `settle_charge_sign`, percent->bps lifts | fired for NAB roe (rounds 2/3), per the brief |
| `research_agent._keep_valid` malformed-item drop | a defensive parse guard; deleting it makes a malformed reply fatal |
| the agent's final citation gate | "verbatim quote verification" is on the do-not-cut list |
| `enforce_evidence_gate`'s strip | on the do-not-cut list; only its ->20 override went |
| `PRICES["openai/gpt-5.6-luna"]`, `PRICES["z-ai/glm-5.3"]` | orphaned once `agentic-luna` and `normal` went, but the audit named neither; flagged for a follow-up sweep |

### Follow-ups for the coordinator

1. Re-point `pipeline-baseline-final` if wave 1 lands as its own commit first.
2. Finding 4 needs the pre-correction ablation described above before any of
   the five checks is reconsidered.
3. `README.md` and `docs/design.md` still describe two shells and the
   `cheap`/`normal` combos. Left untouched per the brief.
4. Two `PRICES` entries are now orphaned (see the table above).
