# Session state — 2026-09-01 (cleanup day), pre-departure snapshot

Written ~12:00 HKT before the user travels (laptop may sleep ~13:30; train
~16:00 for 5h). Everything below is committed; nothing depends on a live
session.

## Schedule (locked)

- Mon night: freeze + holdout — DONE (tag holdout-freeze-20260831).
- Tue Sep 1 (TODAY): cleanup day — in progress, see below.
- Wed Sep 2: write report, transcript, submit. Hard deadline Sep 3.

## Background runs (frozen checkout /Users/michaelzhao/swe/mqg-exam-frozen)

- Macquarie exam: 10 sealed questions. Overnight network outage killed the
  first run at 2/10 (all 5 retry passes burned). RELAUNCHED ~10:25 with
  nohup+caffeinate: scratchpad run-mqg-exam-frozen.sh, log
  mqg-exam-frozen.log, markers examdone-<qid>, sentinel DONE-examrun.
  If it dies again: relaunch the same script (it skips finished questions).
  Mark with scratchpad/mark_mqg_exam.py when 10/10 (matches "# Q:" headers).
- Holdout suite: relaunched 10:00 (evals run --suite holdout --combo
  agentic). Crossref suite: 09:27. Both alive at last check.
- The frozen checkout runs WITHOUT today's MQG fixes (old doc_types, no
  registry) — both handicaps are conservative (can only under-score).
  User decision pending: re-sit the exam on fixed code, or keep the frozen
  run and note the handicap.

## Cleanup track (main), all commits gated by: 443 tests green + dev rescore
byte-identical to evals/results/pre-cleanup-baseline.md + no new ruff

DONE (rounds logged in issues/34):
1. Code-review skill: 5 cycles, CONVERGED (rounds 7-11, commits 94a987a,
   e30cc26, fe32b82, a9393d3, 65d154b). Big catches: MQG doc_type vocabulary,
   missing registry/mqg.json (skeleton only — measures deferred past the
   sealed exam to avoid steering), basis-invention chain (primary_basis None,
   "as reported" default).
2. Simplifier rounds 1-2 (1936b31, b786981): retry ladder unified
   (llm._completion), dead pipeline-era estate deleted (follow_references,
   printed_numbers, _format_quotes, Tolerance.unit), case_slug/_start_run/
   _provenance/_budget_hit/_recover_minted/_cap_drivers extracted,
   LIVE_COMBO constant.
3. Comment sweep wave 1 (1a91014): -115 lines narration/history; receipts
   and constraints kept per the override policy. Wave 2 (fresh-eyes
   convergence check over all 16 src files) launched ~12:00 — gate + commit
   its result before anything else touches src.

4. Restructure — DONE (661f313): agent/ tools/ validation/ judging/ evals/
   subpackages; evals.py -> evals/harness.py; lint 21 -> 15.

REMAINING (in order):
5. improve-codebase-architecture skill — BLOCKED on the user: the skill
   refuses model invocation. The user must type
   /mattpocock-skills:improve-codebase-architecture themselves.
6. Test pruning — DONE (a2f3da4): 443 -> 349 tests in 13 behaviour-named
   files; review-round files dissolved; receipts kept.
7. Final proof — IN FLIGHT: live spot-check (CBA nim FY26) running detached
   on the cleaned code (scratchpad run-spotcheck.sh, log spotcheck.log,
   marker DONE-spotcheck). When it lands clean: cleanup day closes.
   Scorecard estate in evals/results/ deliberately NOT thinned: comments
   cite audit paths, and the README declares "every scorecard" — thinning
   would break receipts for marginal tidiness.

## Report obligations (Wednesday, do not lose)

- Disclose the post-freeze infra-only grace ladder (llm.py NETWORK_GRACE
  comment carries the sentence).
- Disclose the frozen-exam handicaps (old MQG doc_types, no registry).
- Sealed-set caveat: coordinator accidentally saw gold for ONE question (the
  segment-swing/CGM one) — the agent was unaffected; mark that question's
  result with the caveat.
- README results table is retitled as the retired baseline's; replace with
  the holdout/exam numbers when they land. docs/design.md carries a STALE
  SECTIONS banner — full rewrite is report work.

## Resume instructions after sleep/travel

- Reopen laptop, type "continue". Detached runners resume on wake; a case in
  flight at sleep fails its clock and the runner's retry passes re-run it.
- User may set `sudo pmset -a disablesleep 1` for the train (revert with 0;
  never in a closed bag).
- Patchy hotspot is fine (grace ladder); a multi-hour outage burns the exam
  runner's 5 passes — relaunch the script.
- Monitor task polls every 10 min; its "exam running" signal can go stale —
  trust pgrep + log tails, not the monitor line.
