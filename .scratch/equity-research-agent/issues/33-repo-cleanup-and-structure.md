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

The user expects SEVERAL critique passes ("we will have to run a few of
these to make sure we actually capture everything") — re-run the critique
after the cleanup round and after the head-to-head settles the shells.

SCHEDULED (user, 2026-08-30): this ticket executes on Tue 2026-09-01 — the
full review skill and the code simplification skills run SIX times until
the repo and folders are clean. Code freezes at the end of that day; the
sealed/quarantine milestone runs on the frozen result.

## Constraints

- Moves and logic changes NEVER share a commit. Restructure commits are
  import-only.
- Tests stay green at every commit (226+ as of c22f3c0); artifact and CLI
  contracts unchanged; a suite spot-check (3 cases) after the move.
- SEQUENCING: after the agent build + head-to-head land, BEFORE the milestone
  code freeze — the sealed run must execute on the cleaned, frozen layout.
- The usual gates: leakage scan, no tolerance changes, coordinator commits.
