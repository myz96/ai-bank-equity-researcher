# CBA — cash_earnings — FY26 vs FY25

**Movement (cash basis):** 10252$m → 10982$m (+730$m) | **Attribution confidence:** 40/100

*Read from: row 'Net profit after tax from continuing operations – cash basis', column FY25 (12 months ended Jun 2025) -> column FY26 (12 months ended Jun 2026)*

CBA's underlying cash NPAT rose $730 million (+7.1%) to $10,982 million in FY26. Growth was driven by a $1,563 million increase in Net Interest Income and $196 million in other operating income, partially offset by a $719 million rise in underlying operating expenses.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `nii` | Net interest income | +1563 $m | 90 | 2 () | ev-23, ev-24, ev-25 |
| `other_operating_income` | Other operating income | +196 $m | 85 | 1 (single_source) | ev-1, ev-2, ev-3, ev-4, ev-5, ev-6 |
| `operating_expenses` | Underlying operating expenses | -719 $m | 85 | 1 (single_source) | ev-11, ev-12, ev-13, ev-14, ev-15 |
| *residual (unexplained)* | — | -209 $m | — | — |

### nii — "Net interest income"
*+1563 $m | confidence 90/100*

NII increased from $24,023 million to $25,586 million. The bank attributes this to volume growth and margin stability, though NIM compressed slightly from 2.08% to 2.05%. Cited as the primary driver of income growth.
> [ev-23] CBA/FY26/profit_announcement, PDF p28: "Net interest income 25,586 24,023 7 12,891 12,695 2"
> [ev-24] CBA/FY26/profit_announcement, PDF p28: "Net interest margin (%) 2.05 2.08 (3)bpts 2.06 2.04 2bpts"
> [ev-25] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"

### other_operating_income — "Other operating income"
*+196 $m | confidence 85/100*

Increased by $196 million (+4%) to $4,638 million, driven by higher commissions ($135m) and other income ($46m), partially offset by lower trading income (-$9m).
> [ev-1] CBA/FY26/profit_announcement, PDF p30: "Other operating income was $4,638 million, an increase of $196 million or 4% on the prior year."
> [ev-2] CBA/FY26/profit_announcement, PDF p30: "Commissions increased by $135 million or 6% to $2,234 million"
> [ev-3] CBA/FY26/profit_announcement, PDF p30: "Lending fees increased by $12 million or 1% to $924 million"
> [ev-4] CBA/FY26/profit_announcement, PDF p30: "Trading income decreased by $9 million or 1% to $1,190 million"
> [ev-5] CBA/FY26/profit_announcement, PDF p30: "Funds management income increased by $12 million or 10% to $134 million"
> [ev-6] CBA/FY26/profit_announcement, PDF p30: "Other income increased by $46 million or 42% to $156 million"

### operating_expenses — "Underlying operating expenses"
*-719 $m | confidence 85/100*

Underlying operating expenses increased by $719 million (+6%) to $13,585 million. Key drivers include staff costs (+$288m) and IT services (+$393m). This is an expense increase, so it reduces earnings.
> [ev-11] CBA/FY26/profit_announcement, PDF p31: "Underlying operating expenses were $13,585 million, an increase of $719 million or 6% on the prior year."
> [ev-12] CBA/FY26/profit_announcement, PDF p31: "Staff expenses increased by $288 million or 4% to $8,258 million"
> [ev-13] CBA/FY26/profit_announcement, PDF p31: "Occupancy and equipment expenses decreased by $19 million or 2% to $938 million"
> [ev-14] CBA/FY26/profit_announcement, PDF p31: "Information technology services expenses increased by $393 million or 16% to $2,782 million"
> [ev-15] CBA/FY26/profit_announcement, PDF p31: "Other expenses increased by $57 million or 4% to $1,607 million"

### credit_impairment_charge — "Loan impairment expense"
*unquantified | confidence 60/100*

The movement in credit impairment charges for FY26 vs FY25 is not explicitly quantified in dollars in the provided evidence records. While divisional impairment changes are noted (e.g., NZ +$106m, IB&M +$18m), a consolidated delta is missing from the text/tables. Contribution is null due to lack of specific evidence.
> [ev-32] CBA/FY26/results_presentation, printed p56: "RBS vs FY25 • Income +10% • Expenses +9% • Impairment expense ($45m)"
> [ev-33] CBA/FY26/results_presentation, printed p56: "BB vs FY25 • Income +4% • Expenses +4% • Impairment expense ($16m)"
> [ev-34] CBA/FY26/results_presentation, printed p56: "IB&M vs FY25 • Income +6% • Expenses +16% • Impairment expense +$18m"
> [ev-35] CBA/FY26/results_presentation, printed p56: "NZ (NZD) vs FY25 • Income +6% • Expenses +6% • Impairment expense +$106m"

### tax_and_other — "Tax and minorities"
*unquantified | confidence 60/100*



## Limitations
- The bridge does not fully reconcile to the $730m delta because the consolidated dollar movements for Credit Impairment and Tax are not explicitly stated in the provided evidence records. A residual of -$209m remains unexplained.
- Divisional impairment data is available but cannot be reliably aggregated to a consolidated figure without explicit confirmation that there are no inter-segment eliminations or other adjustments.
- Failed check: drivers_reconcile (drivers +1040.0 + residual -209.0 != delta +730.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T03:40:11+00:00
- seconds: 95.3
- cost_usd: 0.0024
- tokens: 43045 in / 8403 out
- orchestration: pipeline
