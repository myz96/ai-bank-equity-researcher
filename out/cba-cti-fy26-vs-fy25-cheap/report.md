# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 80/100

*Read from: row 'Operating expenses to total operating income (%)', column FY25 -> column FY26*

CBA's headline cost-to-income ratio improved by 20 basis points (0.2 ppt) from 45.7% in FY25 to 45.5% in FY26. This improvement was driven by operating income growth outpacing expense growth.

### income_growth — "Total operating income"
*unquantified | confidence 90/100*


> [ev-23] CBA/FY26/profit_announcement, printed p2: "Total operating income"
> [ev-27] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"

### expense_growth — "Total operating expenses"
*unquantified | confidence 90/100*

Total operating expenses grew 6% (ev-1). While lower than income growth, this increase exerted upward pressure on the ratio.
> [ev-1] CBA/FY26/profit_announcement, PDF p31: "Total operating expenses 13,755 12,996 6"

## Source disagreements
- **Underlying CTI definition and direction** (definitional): 44.9% (FY26) / 45.2% (FY25): Profit Announcement (ev-2, ev-5) vs 45.2% (FY26) / 44.7% (FY25): Profit Announcement Narrative (ev-6)
  Preferred: Profit Announcement Table (ev-2). The table explicitly labels 'Underlying operating expenses to underlying operating income' as 44.9% for FY26 and 45.2% for FY25. The narrative text (ev-6) appears to contain a typo or mislabeling of the periods/basis, contradicting the primary KPI table.

## Limitations
- No validated walk chart is available to quantify the exact ppt contribution of income vs expense growth.
- Driver contributions are unquantified due to lack of a primary comparison walk; confidence is capped at 80.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T13:29:31+00:00
- seconds: 123.8
- cost_usd: 0.0023
- tokens: 44179 in / 7251 out
- orchestration: pipeline
