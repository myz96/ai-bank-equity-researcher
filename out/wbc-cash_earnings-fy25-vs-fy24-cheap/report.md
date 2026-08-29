# WBC — cash_earnings — FY25 vs FY24

**Movement (ex_notables basis):** 7113$m → 6972$m (-141$m) | **Attribution confidence:** 40/100

*Read from: row 'Net profit excluding Notable Items', column Full Year Sept 2024 -> column Full Year Sept 2025*

WBC's cash earnings (net profit ex-notables) decreased $141m (-2%) to $6,972m in FY25 vs FY24. The decline was driven by higher operating expenses (+$972m), partially offset by lower credit impairment charges (+$113m). Net interest income and other operating income provided modest growth.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `nii` | Net interest income | +557 $m | 80 | 1 (single_source) | ev-1 |
| `other_operating_income` | Non-interest income | +144 $m | 80 | 1 (single_source) | ev-32 |
| `operating_expenses` | Operating expenses | -972 $m | 80 | 1 (single_source) | ev-34 |
| `credit_impairment_charge` | Impairment (charges)/benefits | +113 $m | 80 | 1 (single_source) | ev-35 |
| `tax_and_other` | Income tax expense | +34 $m | 80 | 1 (single_source) | ev-36 |
| *residual (unexplained)* | — | -17 $m | — | — |

### nii — "Net interest income"
*+557 $m | confidence 80/100*

NII increased $557m (3%) to $19,473m, supported by volume growth in loans and business lending.
> [ev-1] WBC/FY25/results_announcement, PDF p11: "Net interest income 19,473 18,916 3"

### other_operating_income — "Non-interest income"
*+144 $m | confidence 80/100*

Other operating income rose $144m (5%) to $2,991m, driven by fee and wealth management growth.
> [ev-32] WBC/FY25/results_announcement, PDF p9: "Non-interest income 2,991 2,847 5 1,567 1,424 10"

### operating_expenses — "Operating expenses"
*-972 $m | confidence 80/100*

Underlying operating expenses increased $972m (9%) to $11,916m, primarily due to staff and technology costs.
> [ev-34] WBC/FY25/results_announcement, PDF p9: "Operating expenses (11,916) (10,944) 9 (6,218) (5,698) 9"

### credit_impairment_charge — "Impairment (charges)/benefits"
*+113 $m | confidence 80/100*

Credit impairment charges decreased by $113m (21%) to $424m, providing a positive contribution to earnings.
> [ev-35] WBC/FY25/results_announcement, PDF p9: "Impairment (charges)/benefits (424) (537) (21) (174) (250) (30)"

### tax_and_other — "Income tax expense"
*+34 $m | confidence 80/100*

Tax expense decreased slightly by $34m (1%) to $3,135m, contributing positively to net profit.
> [ev-36] WBC/FY25/results_announcement, PDF p9: "Income tax expense (3,135) (3,169) (1) (1,555) (1,580) (2)"

## Notable items
- Hedging items

## Limitations
- The sum of quantified drivers (-$124m) does not fully reconcile to the total delta (-$141m), leaving a residual of -$17m. This may be due to rounding or minor unmapped components.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Failed check: movement_from_variant (the row you read is a 'excluding notable' variant: row 'Net profit excluding Notable Items', column Full Year Sept 2024 -> column Full Year Sept 2025. Read the headline measure instead, and report the variant as context or as a disagreement)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T13:47:39+00:00
- seconds: 289.5
- cost_usd: 0.0037
- tokens: 60681 in / 14330 out
- orchestration: pipeline
