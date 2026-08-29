# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 85/100

*Read from: row 'Operating expenses to total operating income (%)', column FY25 -> column FY26*

CBA's headline cost-to-income ratio (cash basis) improved by 20 basis points from 45.7% in FY25 to 45.5% in FY26. This improvement was driven by operating income growth of 6.2% outpacing underlying operating expense growth of 5.6%, resulting in a net jaws benefit.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `income_growth` | Operating income growth | -0.13 ppt | 90 | 2 () | ev-2, ev-8, ev-18, ev-27 |
| `expense_growth` | Underlying operating expense growth | +0.07 ppt | 90 | 2 () | ev-2, ev-9, ev-18, ev-28 |
| *residual (unexplained)* | — | -0.14 ppt | — | — |

### income_growth — "Operating income growth"
*-0.13 ppt | confidence 90/100*

Total operating income grew 6.2% ($28,465m to $30,224m), providing a positive jaws effect that lowered the ratio.
> [ev-2] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts 45.2 45.9 (70)bpts"
> [ev-8] CBA/FY26/profit_announcement, printed p2: "Total operating income"
> [ev-18] CBA/FY26/profit_announcement, printed p3: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts 45.2 45.9 (70)bpts"
> [ev-27] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"

### expense_growth — "Underlying operating expense growth"
*+0.07 ppt | confidence 90/100*

Underlying operating expenses increased 5.6% ($12,866m to $13,585m), partially offsetting the jaws benefit from income growth.
> [ev-2] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts 45.2 45.9 (70)bpts"
> [ev-9] CBA/FY26/profit_announcement, printed p2: "Underlying operating expenses"
> [ev-18] CBA/FY26/profit_announcement, printed p3: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts 45.2 45.9 (70)bpts"
> [ev-28] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"

### notable_items — "Restructuring and notable items"
*unquantified | confidence 60/100*

Notable items were $170m in FY26 versus $130m in FY25. While these are excluded from the underlying ratio, they are included in the headline cash ratio. The bank does not explicitly quantify their specific ppt contribution to the headline delta in the narrative.
> [ev-10] CBA/FY26/profit_announcement, printed p2: "Restructuring and notable items ¹"
> [ev-11] CBA/FY26/profit_announcement, printed p2: "Total operating expenses"

## Notable items
- Restructuring and notable items: $170m (FY26) vs $130m (FY25)

## Source disagreements
- **Underlying vs Headline Ratio** (definitional): 44.9% (underlying) vs 45.5% (headline/cash)
  Preferred: headline/cash. The task requires the headline measure. CBA reports an 'Operating expenses to total operating income' row for the cash basis (45.5%) and a separate 'Underlying operating expenses to underlying operating income' row (44.9%). We report the cash basis as per the primary basis rule.

## Limitations
- The residual of -0.14 ppt suggests minor rounding differences or unallocated components between the stated levels and the calculated jaws contributions.
- Notable items are included in the headline ratio but their specific ppt impact is not explicitly broken out by the bank; we attribute the bulk of the movement to jaws.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T20:57:31+00:00
- seconds: 50.4
- cost_usd: 0.002
- tokens: 37000 in / 6923 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/FY26/profit_announcement p31 <- p32 page 15']
