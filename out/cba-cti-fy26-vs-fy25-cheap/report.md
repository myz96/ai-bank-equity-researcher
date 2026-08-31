# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 90/100

*Read from: row 'Operating expenses to total operating income (%)', column FY25 -> column FY26*

CBA's headline cost-to-income ratio (cash basis) improved by 20 basis points to 45.5% in FY26 from 45.7% in FY25. This improvement was driven by operating income growth of 6.2% outpacing underlying operating expense growth of 5.6%. The underlying cost-to-income ratio also improved by 30 basis points to 44.9%, reflecting the same jaws dynamic without notable items.

> [ev-2] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts 45.2 45.9 (70)bpts"
> [ev-12] CBA/FY26/profit_announcement, printed p2: "Total operating income"
> [ev-30] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"
> [ev-29] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `income_growth` | — | +0.8 ppt | 80 | 2 () | ev-12, ev-29 |
| `expense_growth` | — | -1 ppt | 80 | 1 (single_source) | ev-30, ev-46 |
| `notable_items` | Restructuring and notable items | +0 ppt | 80 | 2 () | ev-14, ev-47 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### income_growth
*+0.8 ppt | confidence 80/100*

Operational income grew 6.2% ($28,465m to $30,224m), providing a positive contribution to the ratio as it expanded faster than expenses.
> [ev-12] CBA/FY26/profit_announcement, printed p2: "Total operating income"
> [ev-29] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"

### expense_growth
*-1 ppt | confidence 80/100*

Underlying operating expenses grew 5.6% ($12,866m to $13,585m). While rising, this growth was slower than income, contributing to the overall ratio improvement.
> [ev-30] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"
> [ev-46] CBA/FY26/results_presentation, printed p24: "Underlying operating expenses 13,585 5.6% 2.2%"

### notable_items — "Restructuring and notable items"
*+0 ppt | confidence 80/100*

Notable items were $170m in FY26 vs $130m in FY25. The impact on the headline ratio is netted within the total expense/income figures, but the primary driver remains the underlying jaws.
> [ev-14] CBA/FY26/profit_announcement, printed p2: "Restructuring and notable items ¹"
> [ev-47] CBA/FY26/results_presentation, printed p24: "Restructuring and notable items 170"

## Notable items
- Restructuring and notable items increased from $130m to $170m.

## Limitations
- The bank reports both 'total' and 'underlying' ratios. The movement analyzed here uses the 'total' (cash) basis as per the headline row definition. The underlying ratio moved -30 bpts.
- Capped at 80: income_growth +0.8 ppt, expense_growth -1 ppt. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-31T00:51:53+00:00
- seconds: 62.9
- cost_usd: 0.0023
- tokens: 39308 in / 8620 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/FY26/profit_announcement p31 <- p32 page 15']
