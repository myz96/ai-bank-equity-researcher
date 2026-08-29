# CBA — cash_earnings — 1H26 vs 1H25

**Movement (cash basis):** 5132$m → 5445$m (+313$m) | **Attribution confidence:** 90/100

*Read from: row 'Net profit after tax from continuing operations ("cash basis")', column 31 Dec 24 -> column 31 Dec 25*

CBA's cash earnings increased $313 million (+6%) to $5,445 million in 1H26, driven by a $761 million rise in Net Interest Income and a $163 million increase in Other Operating Income. These were partially offset by higher Underlying Operating Expenses ($348 million) and Tax ($94 million), while Credit Impairment remained broadly flat.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `nii` | Net interest income - "cash basis" | +761 $m | 85 | 1 (single_source) | ev-1, ev-3, ev-4 |
| `other_operating_income` | Other operating income | +163 $m | 85 | 1 (single_source) | ev-54, ev-55, ev-56, ev-57, ev-60 |
| `operating_expenses` | Underlying operating expenses | -348 $m | 80 | 1 (single_source) | ev-16, ev-12, ev-14 |
| `notable_items` | Restructuring and notable items | -170 $m | 80 | 1 (single_source) | ev-17, ev-46 |
| `credit_impairment_charge` | Loan impairment expense/(benefit) | -1 $m | 85 | 1 (single_source) | ev-21, ev-27 |
| `tax_and_other` | Corporate tax expense | -94 $m | 85 | 1 (single_source) | ev-31, ev-33 |
| *residual (unexplained)* | — | +2 $m | — | — |

### nii — "Net interest income - "cash basis""
*+761 $m | confidence 85/100*

NII increased $761 million (6%), driven by an $96 billion (8%) growth in average IEA volumes, partly offset by a 4 bps decline in NIM.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "Net interest income - "cash basis" 12,695 12,089 11,934"
> [ev-3] CBA/1H26/profit_announcement, printed p12: "Net interest income was $12,695 million, an increase of $761 million or 6% on the prior comparative period."
> [ev-4] CBA/1H26/profit_announcement, printed p12: "The result was driven by a $96 billion or 8% increase in average interest earning assets to $1,232 billion, partly offset by a 4 basis point decrease in net interest margin to 2.04%."

### other_operating_income — "Other operating income"
*+163 $m | confidence 85/100*

Other operating income rose $163 million (8%), supported by increases in commissions ($61m), trading income ($84m), and lending fees ($16m).
> [ev-54] CBA/1H26/profit_announcement, printed p14: "Other operating income was $2,326 million, an increase of $163 million or 8% on the prior comparative period."
> [ev-55] CBA/1H26/profit_announcement, printed p14: "Commissions increased by $61 million or 6% to $1,146 million"
> [ev-56] CBA/1H26/profit_announcement, printed p14: "Lending fees increased by $16 million or 4% to $465 million"
> [ev-57] CBA/1H26/profit_announcement, printed p14: "Trading income increased by $84 million or 16% to $603 million"
> [ev-60] CBA/1H26/profit_announcement, printed p14: "Other operating income 2,326 2,279 2,163 2) 8"

### operating_expenses — "Underlying operating expenses"
*-348 $m | confidence 80/100*

Underlying operating expenses increased $348 million (5%), reflecting higher staff costs ($169m) and IT services ($134m). Restructuring items are reported separately.
> [ev-16] CBA/1H26/profit_announcement, PDF p31: "Underlying operating expenses 6,720 6,494 6,372 3 5"
> [ev-12] CBA/1H26/profit_announcement, PDF p31: "Staff expenses 4,139 4,000 3,970 3 4"
> [ev-14] CBA/1H26/profit_announcement, PDF p31: "Information technology services expenses 1,321 1,202 1,187 10 11"

### notable_items — "Restructuring and notable items"
*-170 $m | confidence 80/100*

Restructuring and notable items of $170 million were incurred in 1H26, compared to nil in the prior period.
> [ev-17] CBA/1H26/profit_announcement, PDF p31: "Restructuring and notable items ¹ 170 130 – 31 n/a"
> [ev-46] CBA/1H26/profit_announcement, printed p2: "Restructuring and notable items (170) (130) – 31 n/a"

### credit_impairment_charge — "Loan impairment expense/(benefit)"
*-1 $m | confidence 85/100*

Loan impairment expense decreased by $1 million to $319 million, remaining broadly stable year-on-year despite retail headwinds offset by business improvements.
> [ev-21] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense/(benefit) 319 406 320 (21) -"
> [ev-27] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense was $319 million, a decrease of $1 million on the prior comparative period."

### tax_and_other — "Corporate tax expense"
*-94 $m | confidence 85/100*


> [ev-31] CBA/1H26/profit_announcement, PDF p35: "Corporate tax expense ($M) 2,367 2,218 2,273 7 4"
> [ev-33] CBA/1H26/profit_announcement, PDF p35: "Corporate tax expense for the half year ended 31 December 2025 was $2,367 million, an increase of $94 million or 4% on the prior comparative period, reflecting a 30.3% effective tax rate."

## Notable items
- Restructuring and notable items: $170 million (1H26) vs $0 million (1H25).

## Limitations
- The sum of quantified drivers is +$311 million against a total delta of +$313 million. A residual of +$2 million remains unexplained, likely due to rounding or minor unmapped components.
- Expenses are claimed on the underlying/notable split; the bank equally publishes the combined headline framing, so both claims are capped at 80.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T13:06:13+00:00
- seconds: 125.6
- cost_usd: 0.0044
- tokens: 69009 in / 17874 out
- orchestration: pipeline
