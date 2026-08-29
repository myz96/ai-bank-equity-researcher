# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 40/100

*Read from: row 'Total loan impairment expense', column 31 Dec 24 -> column 31 Dec 25*

CBA's credit impairment charge (Loan Impairment Expense) was essentially flat at $319 million in 1H26, a decrease of $1 million from the $320 million reported in 1H25. The annualised loss rate decreased by 1 basis point to 6 bps on average gross loans and acceptances. This stability masked significant offsetting movements across divisions: Retail Banking Services saw a sharp increase in charges (+$153 million), while Business Banking (-$129 million), Institutional Banking and Markets (-$17 million), and New Zealand (-$12 million) all contributed to the decline.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Retail Banking Services | +153 $m | 85 | 1 (single_source) | ev-6, ev-8, ev-20 |
| `collective.asset_quality` | Business Banking | -129 $m | 85 | 1 (single_source) | ev-3, ev-9, ev-15 |
| `individual_provisions` | Institutional Banking and Markets | -17 $m | 80 | 1 (single_source) | ev-4, ev-10, ev-16 |
| `other_unmapped` | New Zealand | -12 $m | 85 | 1 (single_source) | ev-5, ev-11 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.asset_quality — "Retail Banking Services"
*+153 $m | confidence 85/100*

Retail charges increased by $153 million to $232 million. The bank attributes this mainly to losses within the consumer finance portfolio, driving the consumer loss rate up 1 basis point to 7 bps (ev-6, ev-8, ev-20).
> [ev-6] CBA/1H26/profit_announcement, printed p18: "An increase in Retail Banking Services of $153 million to an expense of $232 million"
> [ev-8] CBA/1H26/profit_announcement, printed p18: "Retail Banking Services 232 193 79"
> [ev-20] CBA/1H26/profit_announcement, PDF p45: "Consumer loan impairment expense (LIE) as a percentage of average gross loans and acceptances (GLAAs) was 7 basis points, an increase of 1 basis point on the prior half, mainly driven by losses within the consumer finance portfolio."

### collective.asset_quality — "Business Banking"
*-129 $m | confidence 85/100*

Business Banking charges fell by $129 million to $91 million. Corporate collective provisions decreased $5 million reflecting improvements in credit quality, though partially offset by growth and macro uncertainty (ev-3, ev-9, ev-15).
> [ev-3] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million"
> [ev-9] CBA/1H26/profit_announcement, printed p18: "Business Banking 91 135 220"
> [ev-15] CBA/1H26/profit_announcement, printed p24: "Corporate collective provisions decreased $5 million to $2,581 million, reflecting improvements in credit quality. This was offset by portfolio growth, elevated geopolitical tensions and global macroeconomic uncertainty."

### individual_provisions — "Institutional Banking and Markets"
*-17 $m | confidence 80/100*

IB&M moved from a $9 million charge to an $8 million benefit ($17 million improvement). Corporate individually assessed provisions increased $56 million driven by downgrades for single-name customers, but IB&M's specific result reflects broader benefits or recoveries not fully detailed in the aggregate corporate IAP change (ev-4, ev-10, ev-16).
> [ev-4] CBA/1H26/profit_announcement, printed p18: "A decrease in Institutional Banking and Markets of $17 million to a benefit of $8 million"
> [ev-10] CBA/1H26/profit_announcement, printed p18: "Institutional Banking and Markets (8) 40 9"
> [ev-16] CBA/1H26/profit_announcement, printed p24: "Corporate individually assessed provisions increased $56 million or 9% to $694 million, mainly driven by downgrades for a small number of single name customers."

### other_unmapped — "New Zealand"
*-12 $m | confidence 85/100*

New Zealand charges decreased by $12 million to $4 million. No further driver breakdown is provided for this division in the text (ev-5, ev-11).
> [ev-5] CBA/1H26/profit_announcement, printed p18: "A decrease in New Zealand of $12 million to an expense of $4 million"
> [ev-11] CBA/1H26/profit_announcement, printed p18: "New Zealand 4 39 16"

## Limitations
- The bank does not provide a granular bridge splitting the total movement into 'volume', 'asset quality', and 'overlays' for each division. Drivers are attributed based on the narrative explanations linked to the divisional P&L changes.
- Failed check: drivers_reconcile (drivers -5.0 + residual +0.0 != delta -1.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T20:45:38+00:00
- seconds: 68.5
- cost_usd: 0.0027
- tokens: 50875 in / 9159 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
