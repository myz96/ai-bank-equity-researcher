# CBA — cash_earnings — FY21 vs FY20

**Movement (cash basis):** 7225$m → 8653$m (+1428$m) | **Attribution confidence:** 40/100

CBA's cash earnings (NPAT) increased $1,428 million (+19.8%) to $8,653 million in FY21. The growth was primarily driven by a significant reduction in credit impairment charges ($1,964m benefit), partially offset by higher tax expenses ($568m). Net interest income contributed positively ($229m), while other operating income provided a modest boost ($170m). Operating expense movements were not explicitly quantified as a delta in the provided evidence.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `credit_impairment_charge` | Loan impairment expense | +1964 $m | 85 | 1 (single_source) | ev-12 |
| `tax_and_other` | Corporate tax expense | -568 $m | 85 | 1 (single_source) | ev-6 |
| `nii` | Net interest income | +229 $m | 85 | 1 (single_source) | ev-10, ev-11 |
| `other_operating_income` | Other banking income | +170 $m | 85 | 1 (single_source) | ev-1 |
| *residual (unexplained)* | — | -539 $m | — | — |

### credit_impairment_charge — "Loan impairment expense"
*+1964 $m | confidence 85/100*

Loan impairment expense decreased by $1,964 million compared to FY20, representing a major positive contribution to earnings. This was driven by lower provisions across Retail, Business Banking, and Institutional segments, with NZ moving to a benefit.
> [ev-12] CBA/FY21/profit_announcement, PDF p39: "Loan impairment expense was $554 million, a decrease of $1,964 million or 78% on the prior year."

### tax_and_other — "Corporate tax expense"
*-568 $m | confidence 85/100*

Corporate tax expense increased by $568 million due to higher pre-tax profits, reducing net profit after tax. The effective tax rate was 29.3%.
> [ev-6] CBA/FY21/profit_announcement, printed p20: "Corporate tax expense was $3,590 million, an increase of $568 million or 19% on the prior year, reflecting a 29.3% effective tax rate."

### nii — "Net interest income"
*+229 $m | confidence 85/100*

Net interest income increased by $229 million or 1% on the prior year, contributing positively to the earnings growth.
> [ev-10] CBA/FY21/profit_announcement, printed p12: "Net interest income - "cash basis" 18,839 18,610 1"
> [ev-11] CBA/FY21/profit_announcement, printed p12: "Net interest income was $18,839 million, an increase of $229 million or 1% on the prior year."

### other_operating_income — "Other banking income"
*+170 $m | confidence 85/100*

Other banking income increased by $170 million, driven by higher commissions, lending fees, and other income, partly offset by lower trading income.
> [ev-1] CBA/FY21/profit_announcement, printed p14: "Other banking income was $5,007 million, an increase of $170 million or 4% on the prior year."

## Limitations
- The provided evidence does not contain a quantified delta for underlying operating expenses. Consequently, a residual of -$539 million exists, which likely includes the operating expense movement and any unmapped items. Confidence is capped because the full bridge cannot be reconciled without the expense delta.
- Failed check: drivers_reconcile (drivers +1795.0 + residual -539.0 != delta +1428.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-27T07:46:03+00:00
- seconds: 81.0
- cost_usd: 0.0018
- tokens: 31122 in / 6477 out
- orchestration: pipeline
