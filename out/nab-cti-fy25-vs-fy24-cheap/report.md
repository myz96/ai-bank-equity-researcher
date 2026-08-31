# NAB — cti — FY25 vs FY24

**Movement (cash basis):** 46.5ppt → 47.3ppt (+0.8ppt) | **Attribution confidence:** 80/100

*Read from: row 'Cost to income ratio', column Sep 24 -> column Sep 25*

NAB's cash cost-to-income ratio (CTI) increased by 80 basis points (0.8 ppt) in FY25 to 47.3% from 46.5% in FY24. This deterioration was driven by operating expense growth of 4.6%, which outpaced the bank's operating income growth. The statutory CTI also rose, increasing by 110 bps to 49.6%. A key driver of the expense increase was $130 million in payroll review and remediation costs.

> [ev-1] NAB/FY25/results_book, PDF p15: "Cost to income ratio 49.6% 48.5% 110 bps 50.2% 48.9% 130 bps"
> [ev-2] NAB/FY25/results_book, PDF p15: "Cost to income ratio 47.3% 46.5% 80 bps 47.8% 46.8% 100 bps"
> [ev-3] NAB/FY25/results_book, printed p18: "Total operating expenses(1) 9,848 9,413 4.6 5,043 4,805 5.0"
> [ev-4] NAB/FY25/results_book, printed p18: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."

### expense_growth — "Operating expenses"
*unquantified | confidence 80/100*

Total operating expenses grew 4.6% ($9,413m to $9,848m), a $435m increase. Excluding $130m for payroll review and remediation, underlying expenses grew 3.2%. Expense growth outran income growth, raising the ratio.
> [ev-3] NAB/FY25/results_book, printed p18: "Total operating expenses(1) 9,848 9,413 4.6 5,043 4,805 5.0"
> [ev-4] NAB/FY25/results_book, printed p18: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."

### income_growth — "Operating income"
*unquantified | confidence 60/100*

Implied by the CTI movement and expense growth, operating income growth was lower than the 4.6% expense growth. Specific income drivers are not quantified in the provided evidence records.
> [ev-2] NAB/FY25/results_book, PDF p15: "Cost to income ratio 47.3% 46.5% 80 bps 47.8% 46.8% 100 bps"
> [ev-3] NAB/FY25/results_book, printed p18: "Total operating expenses(1) 9,848 9,413 4.6 5,043 4,805 5.0"

## Notable items
- Payroll review and remediation costs ($130m)

## Source disagreements
- **Basis of CTI** (definitional): 0.8 ppt increase (Cash) vs 1.1 ppt increase (Statutory)
  Preferred: Cash. The bank reports both Cash and Statutory CTI. Per instructions, the primary basis (Cash) is used for the headline movement. The Statutory CTI moved differently due to notable items.

## Limitations
- No walk chart or explicit income growth rate was provided in the evidence records. Income growth was derived implicitly from the CTI delta and expense growth. Therefore, specific ppt contributions for income and expense cannot be precisely quantified without the explicit income figure.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T23:40:31+00:00
- seconds: 26.3
- cost_usd: 0.0014
- tokens: 35778 in / 2586 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
