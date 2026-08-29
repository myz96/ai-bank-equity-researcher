# CBA — cash_earnings — FY26 vs FY25

**Movement (cash basis):** 10252$m → 10982$m (+730$m) | **Attribution confidence:** 95/100

*Read from: row 'Net profit after tax from continuing operations – cash basis', column FY25 -> column FY26*

CBA's cash earnings (NPAT) rose $730 million (+7%) to $10,982 million in FY26. Growth was driven by a $1,563 million increase in Net Interest Income and a $196 million rise in Other Operating Income. These gains were partially offset by a $719 million increase in underlying operating expenses, a $62 million rise in credit impairment charges, and a $208 million increase in corporate tax expense.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `nii` | Net interest income | +1563 $m | 85 | 1 (single_source) | ev-23, ev-25, ev-26 |
| `other_operating_income` | Other operating income | +196 $m | 85 | 1 (single_source) | ev-1, ev-2, ev-3, ev-4, ev-5, ev-6 |
| `operating_expenses` | Underlying operating expenses | -719 $m | 85 | 1 (single_source) | ev-7, ev-8, ev-9, ev-10, ev-11 |
| `credit_impairment_charge` | Loan impairment expense | -62 $m | 85 | 1 (single_source) | ev-18 |
| `notable_items` | Restructuring and notable items | -40 $m | 85 | 1 (single_source) | ev-15 |
| `tax_and_other` | Corporate tax expense | -208 $m | 85 | 1 (single_source) | ev-20 |

### nii — "Net interest income"
*+1563 $m | confidence 85/100*

NII increased $1,563 million (+7%), driven by an $92 billion (8%) growth in average interest-earning assets, which was partly offset by a 3 bps decline in NIM to 2.05%.
> [ev-23] CBA/FY26/profit_announcement, PDF p28: "Net interest income 25,586 24,023 7 12,891 12,695 2"
> [ev-25] CBA/FY26/profit_announcement, PDF p28: "Net interest income was $25,586 million, an increase of $1,563 million or 7% on the prior year."
> [ev-26] CBA/FY26/profit_announcement, PDF p28: "The result was driven by a $92 billion or 8% increase in average interest earning assets to $1,246 billion, partly offset by a 3 basis point decrease in net interest margin to 2.05%."

### other_operating_income — "Other operating income"
*+196 $m | confidence 85/100*

Other operating income grew $196 million (+4%) to $4,638 million, supported by increases in commissions ($135m), other income ($46m), and funds management income ($12m).
> [ev-1] CBA/FY26/profit_announcement, PDF p30: "Other operating income was $4,638 million, an increase of $196 million or 4% on the prior year."
> [ev-2] CBA/FY26/profit_announcement, PDF p30: "Commissions increased by $135 million or 6% to $2,234 million"
> [ev-3] CBA/FY26/profit_announcement, PDF p30: "Lending fees increased by $12 million or 1% to $924 million"
> [ev-4] CBA/FY26/profit_announcement, PDF p30: "Trading income decreased by $9 million or 1% to $1,190 million"
> [ev-5] CBA/FY26/profit_announcement, PDF p30: "Funds management income increased by $12 million or 10% to $134 million"
> [ev-6] CBA/FY26/profit_announcement, PDF p30: "Other income increased by $46 million or 42% to $156 million"

### operating_expenses — "Underlying operating expenses"
*-719 $m | confidence 85/100*

Underlying operating expenses rose $719 million (+6%) to $13,585 million. Increases were led by IT services (+$393m) and staff costs (+$288m), partially offset by lower occupancy (-$19m).
> [ev-7] CBA/FY26/profit_announcement, PDF p31: "Underlying operating expenses were $13,585 million, an increase of $719 million or 6% on the prior year."
> [ev-8] CBA/FY26/profit_announcement, PDF p31: "Staff expenses increased by $288 million or 4% to $8,258 million"
> [ev-9] CBA/FY26/profit_announcement, PDF p31: "Occupancy and equipment expenses decreased by $19 million or 2% to $938 million"
> [ev-10] CBA/FY26/profit_announcement, PDF p31: "Information technology services expenses increased by $393 million or 16% to $2,782 million"
> [ev-11] CBA/FY26/profit_announcement, PDF p31: "Other expenses increased by $57 million or 4% to $1,607 million"

### credit_impairment_charge — "Loan impairment expense"
*-62 $m | confidence 85/100*

Credit impairment charges increased by $62 million (from $726m to $788m), reducing earnings. This reflects higher provisions across the portfolio.
> [ev-18] CBA/FY26/profit_announcement, printed p2: "Loan impairment expense (788) (726) 9 (469) (319) 47"

### notable_items — "Restructuring and notable items"
*-40 $m | confidence 85/100*

Notable/restructuring items increased by $40 million (from -$130m to -$170m), representing a larger drag on earnings compared to the prior year.
> [ev-15] CBA/FY26/profit_announcement, printed p2: "Restructuring and notable items ¹ (170) (130) 31 – (170) (large)"

### tax_and_other — "Corporate tax expense"
*-208 $m | confidence 85/100*

Corporate tax expense increased by $208 million (from $4,491m to $4,699m), reflecting higher pre-tax profits and effective tax rates.
> [ev-20] CBA/FY26/profit_announcement, printed p2: "Corporate tax expense (4,699) (4,491) 5 (2,332) (2,367) (1)"

## Notable items
- Restructuring and notable items: -$170m (FY26) vs -$130m (FY25)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-28T12:15:43+00:00
- seconds: 85.6
- cost_usd: 0.0023
- tokens: 34073 in / 10011 out
- orchestration: pipeline
