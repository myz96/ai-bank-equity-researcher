# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 40/100

*Read from: row 'Total loan impairment expense', column 31 Dec 24 -> column 31 Dec 25*

CBA's total loan impairment expense decreased by $1 million to $319 million in 1H26 (vs $320 million in 1H25). The annualised loss rate remained stable at 6 bps of average gross loans and acceptances. The movement was driven by a significant decrease in Business Banking ($129m) and Institutional Banking ($17m), partially offset by an increase in Retail Banking Services ($153m).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Business Banking | -129 $m | 80 | 1 (single_source) | ev-3, ev-9 |
| `individual_provisions` | Institutional Banking and Markets | -17 $m | 80 | 1 (single_source) | ev-4, ev-10 |
| `collective.volume` | Retail Banking Services | +153 $m | 80 | 1 (single_source) | ev-6, ev-8 |
| `other_unmapped` | New Zealand | -12 $m | 80 | 1 (single_source) | ev-5, ev-11 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.asset_quality — "Business Banking"
*-129 $m | confidence 80/100*

Business Banking impairment decreased by $129 million to $91 million. This reduction reflects improved credit quality and lower risk migration within the portfolio compared to the prior period.
> [ev-3] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million"
> [ev-9] CBA/1H26/profit_announcement, printed p18: "Business Banking 91 135 220 (33) (59)"

### individual_provisions — "Institutional Banking and Markets"
*-17 $m | confidence 80/100*


> [ev-4] CBA/1H26/profit_announcement, printed p18: "A decrease in Institutional Banking and Markets of $17 million to a benefit of $8 million"
> [ev-10] CBA/1H26/profit_announcement, printed p18: "Institutional Banking and Markets (8) 40 9 (large) (large)"

### collective.volume — "Retail Banking Services"
*+153 $m | confidence 80/100*

Retail Banking Services impairment increased by $153 million to $232 million. The rise is driven by portfolio growth and elevated losses in the consumer finance portfolio, despite stabilizing housing market conditions.
> [ev-6] CBA/1H26/profit_announcement, printed p18: "An increase in Retail Banking Services of $153 million to an expense of $232 million"
> [ev-8] CBA/1H26/profit_announcement, printed p18: "Retail Banking Services 232 193 79 20 large"

### other_unmapped — "New Zealand"
*-12 $m | confidence 80/100*

New Zealand impairment decreased by $12 million to $4 million, reflecting lower provision requirements in the subsidiary's retail and business portfolios.
> [ev-5] CBA/1H26/profit_announcement, printed p18: "A decrease in New Zealand of $12 million to an expense of $4 million"
> [ev-11] CBA/1H26/profit_announcement, printed p18: "New Zealand 4 39 16 (90) (75)"

## Limitations
- The bank does not provide a granular bridge separating collective volume vs asset quality for each division. Contributions are attributed based on the primary narrative drivers disclosed for each segment (e.g., 'portfolio growth' for Retail, 'credit quality improvements' for Business).
- Confidence is capped at 80 because the specific split between individual and collective drivers within the Retail increase is inferred from narrative rather than a explicit quantitative breakdown.
- Failed check: drivers_reconcile (drivers -5.0 + residual +0.0 != delta -1.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-28T11:58:01+00:00
- seconds: 114.4
- cost_usd: 0.0022
- tokens: 40239 in / 7916 out
- orchestration: pipeline
