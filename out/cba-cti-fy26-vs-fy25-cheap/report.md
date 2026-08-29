# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 80/100

*Read from: row 'Operating expenses to total operating income (%)', column FY25 -> column FY26*

CBA's headline cost-to-income ratio improved by 20 basis points (0.2 ppt) from 45.7% in FY25 to 45.5% in FY26. This improvement was driven by operating income growth outpacing underlying operating expense growth.

### income_growth — "Total operating income"
*unquantified | confidence 90/100*

Operating income grew 6.2% (ev-24), exceeding expense growth and driving the ratio down.
> [ev-24] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"
> [ev-3] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts"

### expense_growth — "Underlying operating expenses"
*unquantified | confidence 90/100*

Underlying operating expenses grew 5.6% (ev-25), slower than income growth.
> [ev-25] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"
> [ev-3] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts"

## Source disagreements
- **Ratio Variant Definition** (definitional): 45.5% (total/cash) vs 44.9% (underlying/ex_notables)
  Preferred: 45.5%. The task requires the headline measure defined in bank vocabulary as 'Operating expenses to total operating income'. The underlying ratio is a different metric.

## Limitations
- No primary walk chart extracted for this specific comparison. Driver contributions are unquantified because the evidence provides aggregate growth rates rather than a JAWS decomposition table.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-28T12:27:50+00:00
- seconds: 100.8
- cost_usd: 0.0022
- tokens: 43551 in / 6800 out
- orchestration: pipeline
