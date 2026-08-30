# NAB — cti — FY25 vs FY24

**Movement (cash basis):** 46.5ppt → 47.3ppt (+0.8ppt) | **Attribution confidence:** 70/100

*Read from: row 'Cost to income ratio', column FY24 -> column FY25*

NAB's cash cost-to-income ratio (CTI) increased by 80 basis points (0.8 ppt) to 47.3% in FY25 from 46.5% in FY24. The movement was driven by operating expense growth of 4.6%, which outpaced the implied operating income growth. A key driver was a $130 million increase in payroll review and remediation costs; excluding this, underlying expenses grew only 3.2%. Statutory CTI also rose, increasing by 110 bps to 49.6%.

> [ev-1] NAB/FY25/results_book, PDF p15: "Cost to income ratio 49.6% 48.5% 110 bps 50.2% 48.9% 130 bps"
> [ev-2] NAB/FY25/results_book, PDF p15: "Cost to income ratio 47.3% 46.5% 80 bps 47.8% 46.8% 100 bps"
> [ev-3] NAB/FY25/results_book, printed p18: "Total operating expenses(1) 9,848 9,413 4.6 5,043 4,805 5.0"
> [ev-4] NAB/FY25/results_book, printed p18: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."

### expense_growth — "Operating expenses"
*unquantified | confidence 80/100*


> [ev-3] NAB/FY25/results_book, printed p18: "Total operating expenses(1) 9,848 9,413 4.6 5,043 4,805 5.0"
> [ev-4] NAB/FY25/results_book, printed p18: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."

### income_growth — "Operating income"
*unquantified | confidence 60/100*

The CTI increase implies operating income growth lagged behind the 4.6% expense growth. However, the specific operating income levels or growth rate for FY24 and FY25 are not provided in the evidence records, preventing a quantified jaws contribution.

## Notable items
- $130 million increase in payroll review and remediation costs

## Source disagreements
- **Basis of CTI Movement** (definitional): 49.6% (Statutory), ev-1 vs 47.3% (Cash), ev-2
  Preferred: Cash basis. The bank reports two CTI measures: statutory and cash earnings. Per instructions, the primary basis is cash. Both moved up, but the statutory increase (110 bps) differs from the cash increase (80 bps).

## Limitations
- Quantified contributions for income and expense growth cannot be calculated because operating income levels for FY24 and FY25 are not provided in the evidence records. The delta is attributed to the net effect of expense growth outpacing income growth.
- Confidence is capped at 80 for expense growth as it is derived from computed deltas rather than a direct walk chart contribution.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T16:32:14+00:00
- seconds: 44.5
- cost_usd: 0.0014
- tokens: 35110 in / 2322 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
