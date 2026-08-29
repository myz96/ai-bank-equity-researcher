# NAB — cti — FY25 vs FY24

**Movement (cash basis):** 37.1ppt → 34ppt (-3.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'Cost to income ratio', column FY24 -> column FY25*

NAB's headline CTI improved by 310 bps (3.1 ppt) to 34.0% in FY25, driven by a Jaws effect where operating expenses grew faster (+4.6%) than operating income (+2.9%). This improvement was partially offset by $130m in notable payroll review and remediation costs.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `notable_items` | Payroll review and remediation charges | +1.3 ppt | 80 | 1 (single_source) | ev-2, ev-4 |
| *residual (unexplained)* | — | -4.4 ppt | — | — |

### income_growth — "Operating income growth"
*unquantified | confidence 90/100*

Narrative: Operating income grew +2.9% (ev-3, ev-5). Income growth is slower than expense growth, exerting negative pressure on the ratio.
> [ev-3] NAB/FY25/results_book, PDF p5: "Revenue increased by 2.9% with key drivers including volume growth and higher Markets & Treasury (M&T) income, partially offset by higher customer-related remediation charges and the impact from business disposals and run-offs."
> [ev-5] NAB/FY25/results_book, PDF p5: "FY25 v FY24 drivers of cash earnings change (%) Income Expenses Underlying profit 2.9 4.6 1.3"

### expense_growth — "Operating expense growth"
*unquantified | confidence 90/100*

Narrative: Operating expenses grew +4.6% (ev-2, ev-4, ev-5). Expense growth outpaced income growth, exerting positive pressure on the ratio.
> [ev-2] NAB/FY25/results_book, printed p18: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."
> [ev-4] NAB/FY25/results_book, PDF p5: "Expenses increased by 4.6% including $130 million related to payroll review and remediation charges."
> [ev-5] NAB/FY25/results_book, PDF p5: "FY25 v FY24 drivers of cash earnings change (%) Income Expenses Underlying profit 2.9 4.6 1.3"

### notable_items — "Payroll review and remediation charges"
*+1.3 ppt | confidence 80/100*

Narrative: $130m in payroll review and remediation costs increased expenses. On a ~$9.4bn expense base, this adds approx 1.3ppt to the ratio.
> [ev-2] NAB/FY25/results_book, printed p18: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."
> [ev-4] NAB/FY25/results_book, PDF p5: "Expenses increased by 4.6% including $130 million related to payroll review and remediation charges."

## Notable items
- Payroll review and remediation charges ($130m)

## Limitations
- Cannot quantify exact ppt contribution of jaws drivers without explicit bank bridge.
- Residual likely reflects base effect of denominator growth.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-29T13:36:36+00:00
- seconds: 152.5
- cost_usd: 0.0018
- tokens: 40209 in / 4343 out
- orchestration: pipeline
