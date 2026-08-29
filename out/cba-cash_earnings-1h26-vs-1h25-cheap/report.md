# CBA — cash_earnings — 1H26 vs 1H25

**Movement (cash basis):** 5132$m → 5445$m (+313$m) | **Attribution confidence:** 40/100

*Read from: row 'Cash NPAT continuing ops', column 31 Dec 24 -> column 31 Dec 25*

CBA's cash earnings (NPAT) rose $313m (+6.1%) to $5,445m in 1H26 vs 1H25. Growth was driven by a $924m increase in operating income, partially offset by a $348m rise in operating expenses and a $27m increase in credit impairment charges.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `nii` | Net interest income | +924 $m | 80 | 1 (single_source) | ev-22 |
| `other_operating_income` | Other operating income | +163 $m | 85 | 1 (single_source) | ev-4, ev-5, ev-6, ev-7 |
| `operating_expenses` | Operating expenses | -348 $m | 80 | 1 (single_source) | ev-16 |
| `credit_impairment_charge` | Loan impairment expense | -27 $m | 60 | 1 (single_source) | ev-26 |
| *residual (unexplained)* | — | -404 $m | — | — |

### nii — "Net interest income"
*+924 $m | confidence 80/100*

NII increased from $14,097m to $15,021m. This is the primary driver of the $924m income growth.
> [ev-22] CBA/1H26/results_presentation, printed p25: "Net interest income 14,097 15,021"

### other_operating_income — "Other operating income"
*+163 $m | confidence 85/100*

Other operating income grew by $163m to $2,326m, driven by higher commissions ($61m), trading income ($84m), and lending fees ($16m).
> [ev-4] CBA/1H26/profit_announcement, printed p14: "Other operating income was $2,326 million, an increase of $163 million or 8% on the prior comparative period."
> [ev-5] CBA/1H26/profit_announcement, printed p14: "Commissions increased by $61 million or 6% to $1,146 million"
> [ev-6] CBA/1H26/profit_announcement, printed p14: "Lending fees increased by $16 million or 4% to $465 million"
> [ev-7] CBA/1H26/profit_announcement, printed p14: "Trading income increased by $84 million or 16% to $603 million"

### operating_expenses — "Operating expenses"
*-348 $m | confidence 80/100*

Headline operating expenses increased by $348m to $6,720m. The bank reports underlying expense growth of ~$200m; the remainder reflects notable/restructuring items.
> [ev-16] CBA/1H26/results_presentation, printed p8: "Operating expenses 1H25 6,372 1H26 6,720 +6.6%"

### credit_impairment_charge — "Loan impairment expense"
*-27 $m | confidence 60/100*

Credit impairment charges increased by $27m year-on-year, reducing profit. This is consistent with the RBS segment reporting an impairment increase of $153m.
> [ev-26] CBA/1H26/results_presentation, printed p55: "RBS vs 1H25 • Income +6% • Expenses +7% • Impairment expense +$153m"

### tax_and_other — "Tax and minorities"
*unquantified | confidence 0/100*

No explicit tax rate or tax dollar movement is provided in the evidence records for this comparison. Assumed to be captured in the residual.

## Notable items
- Restructuring and other notable items are embedded within the headline operating expense figure of $6,720m.

## Limitations
- No walk chart was extracted for the 1H25 vs 1H26 comparison.
- Tax impact is not explicitly quantified in the provided evidence.
- Residual is large (-$404m), likely due to unquantified tax movements and the split between underlying and notable expenses.
- Failed check: drivers_reconcile (drivers +712.0 + residual -404.0 != delta +313.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T03:28:53+00:00
- seconds: 59.7
- cost_usd: 0.0023
- tokens: 41893 in / 7680 out
- orchestration: pipeline
