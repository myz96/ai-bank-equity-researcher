# Sealed Macquarie exam — RE-SIT on the improved agent, marked 2026-09-02

Same 10 sealed questions as the frozen run; the agent at final cleanup code
(e602309-era) with the depth mechanisms (plan_research, search variants),
the fixed MQG data layer, and the latency tracer. Marked by the same script;
NOTE: the re-sit's judging ran the NEW judge semantics (truncation flags),
so its flag count reads higher than the frozen run's for the same behaviour.

| Question | Coverage | Grounded | Stated | Flagged | Conf |
|---|---|---|---|---|---|
| why-niti-is-not-nim | 5/5 | 4/6 | 6/6 | 1 | 86 |
| second-half-profit-swing (caveat) | 3/5 | 1/7 | 6/7 | 6 | 85 |
| roe-jump-and-allocation | 5/5 | 1/7 | 3/7 | 2 | 85 |
| capital-surplus-versus-cet1 | 4/5 | 3/6 | 6/6 | 3 | 88 |
| credit-impairment-granularity | 5/6 | 2/6 | 4/6 | 3 | 85 |
| two-expense-income-ratios | 3/4 | 3/7 | 7/7 | 4 | 88 |
| three-year-quality-of-earnings | 2/4 | 0/6 | 1/6 | 5 | 88 |
| first-half-profit-up-roe-down | 4/4 | 1/6 | 5/6 | 2 | 80 |
| bfs-volume-versus-margin | 5/6 | 4/7 | 7/7 | 1 | 90 |
| markets-facing-half-divergence | 4/5 | 2/7 | 6/7 | 4 | 88 |

TOTALS: answered 10/10 | coverage 40/49 (82%) | stated 51/65 (78%) |
fully-grounded 21/65 (32%) | flagged 31 | judge cost $0.309

## Frozen vs re-sit (the plan-lift read)

| Measure | Frozen | Re-sit | Delta |
|---|---|---|---|
| Location coverage | 36/49 (73%) | 40/49 (82%) | +4 pages |
| Stated facts | 48/65 (74%) | 51/65 (78%) | +3 |
| Fully-grounded | 18/65 (28%) | 21/65 (32%) | +3 |

The two worst frozen answers moved most: capital-surplus 2/5 -> 4/5 and
markets-divergence 2/5 -> 4/5 — exactly the missing-page failure mode the
plan step and query fan target. Two questions regressed (second-half-swing
5/5 -> 3/5; three-year stated 5/6 -> 1/6): single-run variance cuts both
ways at n=10, so the honest claim is "the depth mechanisms lift coverage,
strongest on the weakest answers", not a per-question guarantee.

## Latency (the tracer's first full run)

All 10 cases carry traces. The answer to "why so slow" is now measured: in
the median case ~97% of wall time is inside model requests (e.g. 2104s
total, 2086s in requests, 0 retries, 0s slept), with single glm-flash
replies running to 250-294s. On a stable network the retry machinery cost
approximately nothing; yesterday's day-long run was the network, not the
agent.
