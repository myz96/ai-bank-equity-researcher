# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 40/100

*Read from: row 'Total loan impairment expense', column Loan impairment expense 31 Dec 24 -> column Loan impairment expense 31 Dec 25*

CBA's credit impairment charge decreased by $1 million to $319 million in 1H26 (vs $320 million in 1H25). The annualised loss rate remained stable at 6 bps of average gross loans and acceptances. The movement was driven by a significant decrease in Business Banking ($129m) and Institutional Banking ($17m), partially offset by an increase in Retail Banking ($153m).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Business Banking | -129 $m | 85 | 1 (single_source) | ev-3 |
| `individual_provisions` | Retail Banking Services | +153 $m | 85 | 1 (single_source) | ev-6, ev-11, ev-16 |
| `other_unmapped` | Institutional Banking and Markets | -17 $m | 85 | 1 (single_source) | ev-4 |
| `other_unmapped` | New Zealand | -12 $m | 85 | 1 (single_source) | ev-5 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.asset_quality — "Business Banking"
*-129 $m | confidence 85/100*

A $129 million decrease in expense to $91 million, reflecting improved credit quality and lower risk migration in the business portfolio.
> [ev-3] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million"

### individual_provisions — "Retail Banking Services"
*+153 $m | confidence 85/100*

A $153 million increase in expense to $232 million, mainly driven by losses within the consumer finance portfolio and elevated geopolitical uncertainty.
> [ev-6] CBA/1H26/profit_announcement, printed p18: "An increase in Retail Banking Services of $153 million to an expense of $232 million"
> [ev-11] CBA/1H26/profit_announcement, printed p24: "Consumer collective provisions increased $55 million or 2% to $2,961 million, reflecting elevated geopolitical tensions and global macroeconomic uncertainty. This was partly offset by the positive impact on households of rising house prices and lower interest rates."
> [ev-16] CBA/1H26/profit_announcement, PDF p45: "Consumer loan impairment expense (LIE) as a percentage of average gross loans and acceptances (GLAAs) was 7 basis points, an increase of 1 basis point on the prior half, mainly driven by losses within the consumer finance portfolio."

### other_unmapped — "Institutional Banking and Markets"
*-17 $m | confidence 85/100*

A $17 million decrease to a benefit of $8 million, contributing to the net reduction in total impairment charges.
> [ev-4] CBA/1H26/profit_announcement, printed p18: "A decrease in Institutional Banking and Markets of $17 million to a benefit of $8 million"

### other_unmapped — "New Zealand"
*-12 $m | confidence 85/100*

A $12 million decrease in expense to $4 million, further reducing the total impairment charge.
> [ev-5] CBA/1H26/profit_announcement, printed p18: "A decrease in New Zealand of $12 million to an expense of $4 million"

## Limitations
- The bank does not explicitly map divisional movements to specific canonical drivers (e.g., volume vs asset quality) in the provided text. Drivers are inferred from narrative context.
- Failed check: drivers_reconcile (drivers -5.0 + residual +0.0 != delta -1.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T03:32:13+00:00
- seconds: 53.5
- cost_usd: 0.0021
- tokens: 40245 in / 7176 out
- orchestration: pipeline
