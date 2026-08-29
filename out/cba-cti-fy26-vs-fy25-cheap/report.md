# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 85/100

*Read from: row 'Operating expenses to total operating income (%)', column FY25 -> column FY26*

CBA's headline cost-to-income ratio improved by 20 basis points (0.2 ppt) from 45.7% in FY25 to 45.5% in FY26. This improvement was driven by operating income growth outpacing operating expense growth.

### income_growth — "Total operating income"
*unquantified | confidence 90/100*

Operational income grew 6.2% (ev-21, ev-25), outpacing expense growth and driving the ratio down.
> [ev-21] CBA/FY26/profit_announcement, printed p2: "Total operating income"
> [ev-25] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"

### expense_growth — "Total operating expenses"
*unquantified | confidence 90/100*

Operating expenses grew 5.8% (ev-1, ev-24), slower than income growth, supporting the ratio improvement.
> [ev-1] CBA/FY26/profit_announcement, PDF p31: "Total operating expenses 13,755 12,996 6"
> [ev-24] CBA/FY26/profit_announcement, printed p2: "Total operating expenses"

## Source disagreements
- **Underlying vs Headline CTI** (definitional): 44.9% (underlying, ev-2) vs 45.5% (total/headline, ev-3)
  Preferred: 45.5% (total/headline). The task requires the headline measure ('Operating expenses to total operating income'). The underlying measure excludes notable items and is a different metric.

## Limitations
- No primary walk chart was provided for the FY25-FY26 comparison. Driver contributions are not quantified in ppt as the evidence does not support a precise arithmetic split of the jaws effect beyond identifying the direction of growth rates.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T03:44:14+00:00
- seconds: 60.9
- cost_usd: 0.0023
- tokens: 45213 in / 7197 out
- orchestration: pipeline
