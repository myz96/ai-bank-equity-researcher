# 34 — Overnight src/ review rounds (Sun night → Mon morning)

Type: task
Status: claimed (user-directed 2026-08-30 ~23:30)

## Directive

Run as many iteration cycles through the night as possible; a fully working
closed-loop agent by Monday morning. After the question-mode build lands:
code-review subagents over src/ ONLY — Claude reviewer subagents AND Codex
reviewers, alternating rounds. Keep going until the reviews STABILISE: no new
confirmed findings, or proposed fixes start being regressions. If Codex fails
(quota), report it in the morning — the user will upgrade the plan.

## Protocol per round

1. Two independent reviewers over src/bank_equity_researcher/ at the current
   commit: one fresh Claude subagent, one Codex session (pty launcher —
   background codex hangs without one; see the 2026-08-30 diagnosis).
2. Findings verified before fixing (a plausible finding is not a real one);
   confirmed fixes applied in a gated round (tests green, no tolerance
   loosening, leakage scan); suite spot-check on 3 cases.
3. Stop condition: a round with zero new confirmed findings, or fixes that
   regress the suite. Log each round's findings/outcomes below.

## Round log

(appended as rounds complete)
