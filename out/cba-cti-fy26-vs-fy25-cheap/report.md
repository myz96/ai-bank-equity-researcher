# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 90/100

*Read from: row 'Operating expenses to total operating income (%)', column FY25 -> column FY26*

CBA's headline cost-to-income ratio (cash basis) improved by 20 basis points to 45.5% in FY26 from 45.7% in FY25. This improvement was driven by operating income growth of 6.2% outpacing underlying operating expense growth of 5.6%. The bank also reported an underlying cost-to-income ratio of 44.9%, down 30 basis points from 45.2%.

> [ev-2] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts 45.2 45.9 (70)bpts"
> [ev-23] CBA/FY26/profit_announcement, printed p3: "Operating expenses to total operating income (%) | 45.5 | 45.7 | (20)bpts"
> [ev-29] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"
> [ev-30] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `income_growth` | Total operating income | -0.12 ppt | 90 | 2 () | ev-29, ev-12 |
| `expense_growth` | Underlying operating expenses | +0.12 ppt | 85 | 2 () | ev-30, ev-13, ev-10, ev-9, ev-8 |
| `notable_items` | Restructuring and notable items | +0 ppt | 85 | 1 (single_source) | ev-14, ev-2 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### income_growth — "Total operating income"
*-0.12 ppt | confidence 90/100*


> [ev-29] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"
> [ev-12] CBA/FY26/profit_announcement, printed p2: "Total operating income"

### expense_growth — "Underlying operating expenses"
*+0.12 ppt | confidence 85/100*

Underlying operating expenses grew 5.6% ($12,866m to $13,585m). Key drivers included IT services (+11%) and occupancy (+2%), partially offset by staff expense decreases (-$20m in H1).
> [ev-30] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"
> [ev-13] CBA/FY26/profit_announcement, printed p2: "Underlying operating expenses"
> [ev-10] CBA/FY26/profit_announcement, PDF p32: "Information technology services expenses increased by $140 million or 11% to $1,461 million,"
> [ev-9] CBA/FY26/profit_announcement, PDF p32: "Occupancy and equipment expenses increased by $8 million or 2% to $473 million."
> [ev-8] CBA/FY26/profit_announcement, PDF p32: "Staff expenses decreased by $20 million to $4,119 million,"

### notable_items — "Restructuring and notable items"
*+0 ppt | confidence 85/100*

Notable items were $170m in FY26 vs $130m in FY25. While these affect statutory results, the headline cash CTI excludes them. The net impact on the cash ratio is zero as they are excluded from both numerator and denominator.
> [ev-14] CBA/FY26/profit_announcement, printed p2: "Restructuring and notable items ¹"
> [ev-2] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts 45.2 45.9 (70)bpts"

## Notable items
- Restructuring and notable items increased from $130m to $170m.

## Limitations
- The Jaws decomposition is calculated manually as no walk chart was provided for the Group Cash CTI. The narrative cites H1 expense details which may not fully represent the full year mix.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T12:37:56+00:00
- seconds: 51.0
- cost_usd: 0.0021
- tokens: 38119 in / 7366 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/FY26/profit_announcement p31 <- p32 page 15']
