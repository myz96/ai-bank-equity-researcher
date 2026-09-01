# Sealed Macquarie exam — FROZEN agent run, marked 2026-09-02 00:15

Protocol: 10 Codex-authored questions, gold sealed outside the repo; the
agent (frozen at holdout-freeze-20260831 + grace ladder) saw question texts
only. Marked by the two-judge protocol via scratchpad/mark_mqg_exam.py.
Numbers only here — no gold content.

Handicaps disclosed: the frozen code ran with the pre-cleanup MQG data layer
(doc_types outside the vocabulary -> no slide-page mapping, text walk
tolerance; no registry skeleton) and without the depth mechanisms
(plan_research, query variants). Both err conservative. The
second-half-profit-swing marks carry the coordinator gold-exposure caveat
(one question's gold was accidentally seen by the coordinator, never by the
agent).

| Question | Coverage | Grounded | Stated | Flagged | Conf |
|---|---|---|---|---|---|
| why-niti-is-not-nim | 4/5 | 3/6 | 5/6 | 1 | 88 |
| second-half-profit-swing (caveat) | 5/5 | 1/7 | 5/7 | 5 | 86 |
| roe-jump-and-allocation | 5/5 | 2/7 | 5/7 | 1 | 88 |
| capital-surplus-versus-cet1 | 2/5 | 1/6 | 3/6 | 3 | 90 |
| credit-impairment-granularity | 3/6 | 1/6 | 2/6 | 3 | 78 |
| two-expense-income-ratios | 3/4 | 3/7 | 6/7 | 4 | 78 |
| three-year-quality-of-earnings | 3/4 | 1/6 | 5/6 | 2 | 88 |
| first-half-profit-up-roe-down | 4/4 | 2/6 | 4/6 | 1 | 80 |
| bfs-volume-versus-margin | 5/6 | 4/7 | 7/7 | 0 | 88 |
| markets-facing-half-divergence | 2/5 | 0/7 | 6/7 | 4 | 88 |

TOTALS: answered 10/10 | location coverage 36/49 (73%) | stated 48/65 (74%)
| fully-grounded 18/65 (28%) | flagged 24 | judge cost $0.254

Reading: on a bank never seen in development, the agent finds ~3/4 of the
required pages and states ~3/4 of the gold facts; the weak column stays
citation quote-completeness (the same column every arm, frontier included,
loses on the dev questions). The re-sit on the improved agent (plan step,
query variants, cleaned data layer) runs tonight; its delta against this
table is the plan-lift measurement.
