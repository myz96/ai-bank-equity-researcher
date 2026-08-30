# NAB — cti — FY25 vs FY24

**Movement (cash basis):** 46.5ppt → 47.3ppt (+0.8ppt) | **Attribution confidence:** 75/100

*Read from: row 'Cost to income ratio', column FY24 -> column FY25*

NAB's cash cost-to-income ratio (CTI) increased by 80 basis points (0.8 ppt) in FY25 to 47.3%, up from 46.5% in FY24. This deterioration was driven by operating expense growth of 4.6% outpacing the implied operating income growth. A key driver was a $130 million increase in payroll review and remediation costs; excluding this, underlying expenses grew only 3.2%. The statutory CTI also rose, increasing by 110 bps to 49.6%.

> [ev-1] NAB/FY25/results_book, PDF p15: "Cost to income ratio 49.6% 48.5% 110 bps 50.2% 48.9% 130 bps"
> [ev-2] NAB/FY25/results_book, PDF p15: "Cost to income ratio 47.3% 46.5% 80 bps 47.8% 46.8% 100 bps"
> [ev-3] NAB/FY25/results_book, printed p18: "Total operating expenses(1) 9,848 9,413 4.6 5,043 4,805 5.0"
> [ev-4] NAB/FY25/results_book, printed p18: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."

### expense_growth — "Operating expenses"
*unquantified | confidence 80/100*

Total operating expenses increased by $435 million or 4.6% to $9,848 million (ev-3, ev-4). Excluding $130 million for payroll review and remediation, underlying expenses grew 3.2% (ev-4). Expense growth exceeded income growth, raising the ratio.
> [ev-3] NAB/FY25/results_book, printed p18: "Total operating expenses(1) 9,848 9,413 4.6 5,043 4,805 5.0"
> [ev-4] NAB/FY25/results_book, printed p18: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."

### income_growth — "Operating income"
*unquantified | confidence 60/100*

Income growth is derived from the CTI movement and expense levels. With CTI rising 0.8 ppt on $9,413m FY24 expenses, implied income growth was approximately 2.5%, trailing expense growth of 4.6% (ev-1, ev-2, ev-3).
> [ev-1] NAB/FY25/results_book, PDF p15: "Cost to income ratio 49.6% 48.5% 110 bps 50.2% 48.9% 130 bps"
> [ev-2] NAB/FY25/results_book, PDF p15: "Cost to income ratio 47.3% 46.5% 80 bps 47.8% 46.8% 100 bps"
> [ev-3] NAB/FY25/results_book, printed p18: "Total operating expenses(1) 9,848 9,413 4.6 5,043 4,805 5.0"

## Notable items
- Payroll review and remediation costs ($130m)

## Source disagreements
- **Basis of CTI Movement** (definitional): 0.8 ppt increase (Cash basis) vs 1.1 ppt increase (Statutory basis)
  Preferred: Cash basis. The bank reports two CTI measures. Cash earnings is the primary basis per vocabulary. Statutory CTI moved differently due to notable items.

## Limitations
- No explicit operating income level provided for FY24/FY25 to calculate exact jaws contribution.
- Quantified driver contributions are unquantified as evidence does not provide a walk chart or explicit income growth rate.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T12:40:56+00:00
- seconds: 28.9
- cost_usd: 0.0013
- tokens: 35010 in / 2006 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
