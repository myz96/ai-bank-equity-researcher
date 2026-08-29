# CBA — cash_earnings — FY21 vs FY20

**Movement (cash basis):** 7225$m → 8653$m (+1428$m) | **Attribution confidence:** 75/100

*Read from: row 'Cash NPAT – continuing operations', column FY20 -> column FY21*

CBA's cash earnings (NPAT) increased $1,428 million to $8,653 million in FY21 from $7,225 million in FY20. The primary driver was a $1,964 million reduction in credit impairment charges, partially offset by higher operating expenses and lower trading income.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `credit_impairment_charge` | Loan impairment expense | +1964 $m | 90 | 2 () | ev-14, ev-15, ev-16, ev-17, ev-18, ev-19, ev-27 |
| `nii` | Net interest income | +229 $m | 85 | 1 (single_source) | ev-12, ev-13 |
| `other_operating_income` | Other banking income | +170 $m | 85 | 1 (single_source) | ev-1, ev-2, ev-3, ev-4, ev-5, ev-6 |
| `operating_expenses` | Operating expenses | -115 $m | 75 | 1 (single_source) | ev-28, ev-29 |
| *residual (unexplained)* | — | -820 $m | — | — |

### credit_impairment_charge — "Loan impairment expense"
*+1964 $m | confidence 90/100*

Loan impairment expense decreased by $1,964 million (78%) to $554 million, driven by significant reductions in Retail Banking (-$900m), Business Banking (-$551m), and NZ (-$297m).
> [ev-14] CBA/FY21/profit_announcement, PDF p39: "Loan impairment expense was $554 million, a decrease of $1,964 million or 78% on the prior year."
> [ev-15] CBA/FY21/profit_announcement, PDF p39: "A decrease in Retail Banking Services of $900 million or 87% to $134 million"
> [ev-16] CBA/FY21/profit_announcement, PDF p39: "A decrease in Business Banking of $551 million or 70% to $233 million"
> [ev-17] CBA/FY21/profit_announcement, PDF p39: "A decrease in New Zealand of $297 million to a benefit of $5 million"
> [ev-18] CBA/FY21/profit_announcement, PDF p39: "A decrease in Institutional Banking and Markets of $257 million or 73% to $96 million"
> [ev-19] CBA/FY21/profit_announcement, PDF p39: "An increase in Corporate Centre and Other of $41 million or 75% to $96 million"
> [ev-27] CBA/FY21/results_presentation, printed p9: "Loan Impairment Expense $m"

### nii — "Net interest income"
*+229 $m | confidence 85/100*

Net interest income increased by $229 million (1%) to $18,839 million, reflecting volume growth and margin dynamics.
> [ev-12] CBA/FY21/profit_announcement, printed p12: "Net interest income - "cash basis" 18,839 18,610 1 9,468 9,371 1"
> [ev-13] CBA/FY21/profit_announcement, printed p12: "Net interest income was $18,839 million, an increase of $229 million or 1% on the prior year."

### other_operating_income — "Other banking income"
*+170 $m | confidence 85/100*

Other banking income increased by $170 million (4%) to $5,007 million. Growth was led by lending fees (+$142m) and other income (+$109m), offset by a decrease in trading income (-$88m).
> [ev-1] CBA/FY21/profit_announcement, printed p14: "Other banking income - "cash basis" 5,007 4,837 4 2,588 2,419 7"
> [ev-2] CBA/FY21/profit_announcement, printed p14: "Other banking income was $5,007 million, an increase of $170 million or 4% on the prior year."
> [ev-3] CBA/FY21/profit_announcement, printed p14: "Commissions increased by $7 million to $2,564 million"
> [ev-4] CBA/FY21/profit_announcement, printed p14: "Lending fees increased by $142 million or 14% to $1,128 million"
> [ev-5] CBA/FY21/profit_announcement, printed p14: "Trading income decreased by $88 million or 9% to $852 million"
> [ev-6] CBA/FY21/profit_announcement, printed p14: "Other income increased by $109 million or 31% to $463 million"

### operating_expenses — "Operating expenses"
*-115 $m | confidence 75/100*

Underlying operating expenses increased by approximately $115 million. This is derived from the total operating expense increase of $276 million (from $7,686m to $7,962m) less the increase in remediation costs of $114 million ($461m to $575m).
> [ev-28] CBA/FY21/results_presentation, printed p9: "Ex-Remediation Operating Expenses $m"
> [ev-29] CBA/FY21/results_presentation, printed p9: "Remediation Operating Expenses $m"

### tax_and_other — "Tax and minorities"
*unquantified | confidence 0/100*

The impact of tax and minority interests on the year-on-year movement is not explicitly quantified in the provided evidence records. It is included in the residual.

## Source disagreements
- **Cash NPAT Definition** (definitional): 8,653 - CBA/FY21/results_presentation (ev-24) vs 10,181 - CBA/FY21/profit_announcement (ev-11)
  Preferred: 8,653. The results presentation (ev-24) labels its figure as 'Cash NPAT – continuing operations', which aligns with the standard core profit metric used for operational analysis. The profit announcement table (ev-11) lists 'Cash basis net profit' as 10,181 but also shows a statutory figure of 8,801. Given the context of analyzing underlying performance drivers against FY20 (where ev-24 shows 7,225), the 8,653 figure is the consistent continuing operations measure. The 10,181 figure likely includes discontinued operations or non-controlling interests adjustments not present in the FY20 comparable.

## Limitations
- The operating expense figure used is an estimate derived by subtracting remediation costs from total operating expenses, as separate underlying/opex lines were not fully explicit in the provided text snippets.
- Tax impact is not explicitly quantified in the evidence, leading to a large residual.
- Disagreement exists between two reported Cash NPAT figures; the continuing operations figure was selected for consistency with the FY20 baseline.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-28T12:05:05+00:00
- seconds: 93.2
- cost_usd: 0.0026
- tokens: 48316 in / 9134 out
- orchestration: pipeline
