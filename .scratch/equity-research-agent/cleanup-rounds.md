# Cleanup round matrix — minimum 6 per axis per reviewer family (user, 2026-09-01)

Reviewers: FABLE = Claude subagents. SOL = GPT-Sol via the codex CLI.
A Codex CLEANUP-AUDIT round counts one round each for SOL simplifier, sweep,
and pruning (it adversarially covers all three axes in one pass).
Every round from here is propose-only; fixes are applied centrally between
rounds behind the standing gate (suite green, dev rescore identical to
pre-cleanup-baseline, no new ruff).

| Axis | FABLE done | FABLE target | SOL done | SOL target |
|---|---|---|---|---|
| Code review | 5 | 6 | 0 | 6 |
| Simplifier | 3 | 6 | 1 (audit r1) | 6 |
| Comment sweep | 4 | 6 | 1 (audit r1) | 6 |
| Test pruning | 3 | 6 | 1 (audit r1) | 6 |
| Architecture | 1 | 6 | 1 (+r2 in flight) | 6 |

Counting rules: a round counts when its report lands AND its accepted
findings are applied and committed (or it says CONVERGED/CONSOLIDATED).
Past-6 rounds stop early only if the last two consecutive rounds on that
axis found nothing.

Update this table as rounds land; each round's verdict goes to issues/34.
