# NAB — cash_earnings — FY25 vs FY24

**Movement (cash basis):** 7102$m → 7091$m (-11$m) | **Attribution confidence:** 40/100

*Read from: row 'Cash earnings', column FY24 (Sep 2024) -> column FY25 (Sep 2025)*

NAB's cash earnings decreased by $11 million to $7,091 million in FY25 from $7,102 million in FY24. The decline was driven by higher operating expenses and lower credit impairment write-backs, partially offset by an increase in net interest income.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `nii` | Net interest income | +644 $m | 85 | 1 (single_source) | ev-1, ev-8, ev-9 |
| `other_operating_income` | Other operating income | -67 $m | 85 | 1 (single_source) | ev-14, ev-15, ev-16, ev-17 |
| `operating_expenses` | Operating expenses (underlying) | -305 $m | 80 | 1 (single_source) | ev-21 |
| `notable_items` | Payroll review and remediation | -130 $m | 80 | 2 () | ev-21, ev-72 |
| `credit_impairment_charge` | Credit impairment charge | -105 $m | 80 | 1 (single_source) | ev-41, ev-47 |
| `tax_and_other` | Income tax expense | -27 $m | 85 | 1 (single_source) | ev-31, ev-33 |
| *residual (unexplained)* | — | +0 $m | — | — |

### nii — "Net interest income"
*+644 $m | confidence 85/100*

NII increased by $644 million due to volume growth (+$22.5bn IEA) and a 3bps margin improvement, partially offset by a $74 million hedge movement.
> [ev-1] NAB/FY25/results_book, PDF p17: "Net interest income ($m) 17,398 16,754 3.8% 8,953 8,445 6.0%"
> [ev-8] NAB/FY25/results_book, PDF p17: "Net interest income increased by $644 million or 3.8%. This includes a decrease of $74 million due to movements in economic hedges, offset in other operating income. Excluding this movement, the underlying increase of $718 million or 4.3% was due to higher average interest earning assets and net interest margin."
> [ev-9] NAB/FY25/results_book, PDF p17: "Average interest earning assets increased by $22.5 billion or 2.3% reflecting growth primarily in business lending and, to a lesser extent, in housing lending, partially offset by a reduction in high-quality liquid assets (HQLA)."

### other_operating_income — "Other operating income"
*-67 $m | confidence 85/100*

Decreased by $67 million, primarily due to a $132 million drop in fees and commissions, partially offset by higher trading income.
> [ev-14] NAB/FY25/results_book, printed p16: "Total other operating income 3,415 3,482 (1.9) 1,592 1,823 (12.7)"
> [ev-15] NAB/FY25/results_book, printed p16: "Other operating income decreased by $67 million or 1.9%."
> [ev-16] NAB/FY25/results_book, printed p16: "Net fees and commissions decreased by $132 million or 5.8%."
> [ev-17] NAB/FY25/results_book, printed p16: "Trading income increased by $33 million or 2.8%."

### operating_expenses — "Operating expenses (underlying)"
*-305 $m | confidence 80/100*

Underlying operating expenses increased by $305 million (ex payroll review/remediation), driven by personnel and technology costs.
> [ev-21] NAB/FY25/results_book, printed p18: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."

### notable_items — "Payroll review and remediation"
*-130 $m | confidence 80/100*

Increased by $130 million compared to FY24, representing a notable cost item excluded from the underlying expense trend.
> [ev-21] NAB/FY25/results_book, printed p18: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."
> [ev-72] NAB/FY25/investor_presentation, printed p36: "Payroll review and remediation3"

### credit_impairment_charge — "Credit impairment charge"
*-105 $m | confidence 80/100*

Impairment charges increased by $105 million (from -$728m to -$833m), reducing earnings. This includes a decrease in write-backs of $83 million.
> [ev-41] NAB/FY25/results_book, PDF p75: "Credit impairment charge (833) - - - (833)"
> [ev-47] NAB/FY25/results_book, PDF p45: "Credit impairment write-back 122 205 (40.5) 27 95 (71.6)"

### tax_and_other — "Income tax expense"
*-27 $m | confidence 85/100*

Tax expense increased by $27 million due to higher pre-tax earnings and a slightly higher effective tax rate.
> [ev-31] NAB/FY25/results_book, PDF p23: "Income tax expense ($m) 3,002 2,975 0.9% 1,490 1,512 (1.5%)"
> [ev-33] NAB/FY25/results_book, PDF p23: "Income tax expense increased by $27 million or 0.9% due to higher cash earnings before income tax and a higher effective tax rate."

## Notable items
- Payroll review and remediation costs ($130m)

## Limitations
- Expenses are claimed on the underlying/notable split; the bank equally publishes the combined headline framing, so both claims are capped at 80.
- Failed check: drivers_reconcile (drivers +10.0 + residual +0.0 != delta -11.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-29T13:32:12+00:00
- seconds: 160.8
- cost_usd: 0.0052
- tokens: 76976 in / 22004 out
- orchestration: pipeline
