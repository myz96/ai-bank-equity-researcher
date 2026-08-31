# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 40/100

*Read from: row 'Total loan impairment expense', column Total loan impairment expense 31 Dec 24 -> column Total loan impairment expense 31 Dec 25*

CBA's credit impairment charge was broadly flat at $319 million in 1H26 (vs $320 million in 1H25), a decrease of $1 million. The annualised loss rate decreased by 1 basis point to 6 bps on average gross loans and acceptances. This stability masked significant offsetting movements: Retail Banking Services saw a large increase in charges (+$153 million) driven by consumer finance losses, while Business Banking charges fell sharply (-$129 million). Institutional Banking swung to a benefit, and New Zealand charges also declined.

> [ev-1] CBA/1H26/profit_announcement, PDF p109: "Total loan impairment expense"
> [ev-2] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense was $319 million, a decrease of $1 million on the prior comparative period."
> [ev-7] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense annualised as a percentage of average gross loans and acceptances (GLAAs) decreased 1 basis point to 6 basis points."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Retail Banking Services | +153 $m | 80 | 1 (single_source) | ev-6, ev-8, ev-19 |
| `collective.asset_quality` | Business Banking | -129 $m | 80 | 1 (single_source) | ev-3, ev-9 |
| `write_backs_recoveries` | Institutional Banking and Markets | -17 $m | 80 | 1 (single_source) | ev-4, ev-10 |
| `collective.asset_quality` | New Zealand | -12 $m | 80 | 1 (single_source) | ev-5, ev-11 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.asset_quality — "Retail Banking Services"
*+153 $m | confidence 80/100*

Retail charges increased by $153 million to $232 million. The bank attributes this mainly to losses within the consumer finance portfolio, which drove the annualised loss rate up 1 basis point to 7 bps (ev-6, ev-19).
> [ev-6] CBA/1H26/profit_announcement, printed p18: "An increase in Retail Banking Services of $153 million to an expense of $232 million"
> [ev-8] CBA/1H26/profit_announcement, printed p18: "Retail Banking Services 232 193 79"
> [ev-19] CBA/1H26/profit_announcement, PDF p45: "Consumer loan impairment expense (LIE) as a percentage of average gross loans and acceptances (GLAAs) was 7 basis points, an increase of 1 basis point on the prior half, mainly driven by losses within the consumer finance portfolio."

### collective.asset_quality — "Business Banking"
*-129 $m | confidence 80/100*

Business Banking charges decreased by $129 million to $91 million. While the text does not explicitly name the driver for this specific divisional delta, it is the primary contributor to the overall net decrease.
> [ev-3] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million"
> [ev-9] CBA/1H26/profit_announcement, printed p18: "Business Banking 91 135 220"

### write_backs_recoveries — "Institutional Banking and Markets"
*-17 $m | confidence 80/100*

Institutional Banking moved from a $9 million charge to an $8 million benefit, a swing of $17 million. This reflects recoveries or write-backs outweighing new provisions in this segment.
> [ev-4] CBA/1H26/profit_announcement, printed p18: "A decrease in Institutional Banking and Markets of $17 million to a benefit of $8 million"
> [ev-10] CBA/1H26/profit_announcement, printed p18: "Institutional Banking and Markets (8) 40 9"

### collective.asset_quality — "New Zealand"
*-12 $m | confidence 80/100*

New Zealand charges decreased by $12 million to $4 million, contributing to the overall stability despite retail headwinds.
> [ev-5] CBA/1H26/profit_announcement, printed p18: "A decrease in New Zealand of $12 million to an expense of $4 million"
> [ev-11] CBA/1H26/profit_announcement, printed p18: "New Zealand 4 39 16"

## Limitations
- The bank does not provide a granular bridge splitting the total movement into canonical drivers (e.g., volume vs asset quality) for each division. Contributions are inferred from divisional deltas.
- Failed check: drivers_reconcile (drivers -5.0 + residual +0.0 != delta -1.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T23:19:58+00:00
- seconds: 66.1
- cost_usd: 0.0024
- tokens: 47013 in / 7854 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
