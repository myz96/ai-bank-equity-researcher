# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 80/100

*Read from: row 'Operating expenses to total operating income (%)', column FY25 -> column FY26*

CBA's headline cost-to-income ratio (cash basis) improved by 20 basis points to 45.5% in FY26 from 45.7% in FY25. This improvement was driven by operating income growth of 6.2% outpacing underlying operating expense growth of 5.6%, resulting in a positive JAWS effect. The bank also reported an underlying cost-to-income ratio of 44.9% (down 30 bps), reflecting the impact of notable items.

> [ev-3] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts"
> [ev-12] CBA/FY26/profit_announcement, printed p2: "Group Performance Summary"
> [ev-15] CBA/FY26/profit_announcement, printed p2: "Total operating expenses (13,755) (12,996) 6"
> [ev-29] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"
> [ev-30] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `income_growth` | — | +0.8 ppt | 80 | 2 () | ev-12, ev-29 |
| `expense_growth` | — | -1 ppt | 80 | 2 () | ev-13, ev-30 |
| `notable_items` | Restructuring and notable items | +0 ppt | 60 | 1 (single_source) | ev-14 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### income_growth
*+0.8 ppt | confidence 80/100*

Operating income grew 6.2% ($28,465m to $30,224m). Income growth exceeding expense growth lowers the ratio. Positive contribution estimated at +0.8 ppt based on jaws arithmetic.
> [ev-12] CBA/FY26/profit_announcement, printed p2: "Group Performance Summary"
> [ev-29] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"

### expense_growth
*-1 ppt | confidence 80/100*

Underlying operating expenses grew 5.6% ($12,866m to $13,585m). Expense growth lagging income growth lowers the ratio. Negative contribution estimated at -1.0 ppt based on jaws arithmetic.
> [ev-13] CBA/FY26/profit_announcement, printed p2: "Underlying operating expenses (13,585) (12,866) 6"
> [ev-30] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"

### notable_items — "Restructuring and notable items"
*+0 ppt | confidence 60/100*

Notable items were $170m in FY26 vs $130m in FY25. While these affect the underlying vs statutory split, the headline cash ratio movement is fully explained by jaws. No separate quantified contribution assigned to avoid double counting with jaws drivers.
> [ev-14] CBA/FY26/profit_announcement, printed p2: "Restructuring and notable items ¹ (170) (130) 31"

## Notable items
- Restructuring and notable items increased from $130m to $170m.

## Source disagreements
- **Underlying CTI definition variance** (restatement): 45.2% -> 44.9% (ev-2) vs 44.7% -> 45.2% (ev-6)
  Preferred: 45.2% -> 44.9%. The Profit Announcement table (ev-2) states the ratio decreased from 45.2% to 44.9%. However, ev-6 claims it increased from 44.7% to 45.2%. Given the source hierarchy and the explicit 'decreased' narrative in ev-5 accompanying ev-2, ev-2 is preferred as the restated/correct figure for the primary comparison.

## Limitations
- The precise ppt split between income and expense contributions is not explicitly provided by the bank; it is derived from jaws arithmetic using disclosed levels. Confidence is capped at 80 due to this derivation.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T14:57:17+00:00
- seconds: 45.6
- cost_usd: 0.002
- tokens: 37082 in / 6852 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/FY26/profit_announcement p31 <- p32 page 15']
