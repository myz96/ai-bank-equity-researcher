# WBC — cash_earnings — FY25 vs FY24

**Movement (ex_notables basis):** 7113$m → 6972$m (-141$m) | **Attribution confidence:** 40/100

*Read from: row 'Net profit excluding Notable Items', column Full Year Sept 2024 -> column Full Year Sept 2025*

WBC's cash earnings (net profit excluding Notable Items) decreased by $141 million (-2%) to $6,972 million in FY25 from $7,113 million in FY24. Statutory net profit also fell 1% to $6,916 million. Total operating income grew 3% to $22,464 million, while underlying operating expenses rose 9% to $11,916 million.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `nii` | Net interest income | +557 $m | 80 | 1 (single_source) | ev-1, ev-2, ev-30 |
| `other_operating_income` | Non-interest income | +144 $m | 80 | 1 (single_source) | ev-31, ev-39, ev-40 |
| `operating_expenses` | Operating expenses | -972 $m | 80 | 1 (single_source) | ev-17, ev-18, ev-33 |
| `credit_impairment_charge` | Impairment (charges)/benefits | +113 $m | 80 | 1 (single_source) | ev-25, ev-34 |
| `tax_and_other` | Income tax expense | +24 $m | 80 | 1 (single_source) | ev-35 |
| *residual (unexplained)* | — | +0 $m | — | — |

### nii — "Net interest income"
*+557 $m | confidence 80/100*

NII increased by $557 million (+3%) to $19,473 million, driven by volume growth in average loans and liquid assets, partially offset by margin compression.
> [ev-1] WBC/FY25/results_announcement, PDF p11: "Net interest income 19,473 18,916 3"
> [ev-2] WBC/FY25/results_announcement, PDF p11: "Core net interest income 18,191 17,608 3"
> [ev-30] WBC/FY25/results_announcement, PDF p9: "Net interest income 19,473 18,916 3 9,904 9,569 4"

### other_operating_income — "Non-interest income"
*+144 $m | confidence 80/100*

Other operating income grew by $144 million (+5%) to $2,991 million, supported by higher net fees and trading income.
> [ev-31] WBC/FY25/results_announcement, PDF p9: "Non-interest income 2,991 2,847 5 1,567 1,424 10"
> [ev-39] WBC/FY25/results_announcement, PDF p53: "Net fees 1,732 1,672 4 887 845 5"
> [ev-40] WBC/FY25/results_announcement, PDF p53: "Total non-interest income 3,004 2,835 6 1,562 1,442 8"

### operating_expenses — "Operating expenses"
*-972 $m | confidence 80/100*

Underlying operating expenses increased by $972 million (+9%) to $11,916 million, primarily due to higher staff and technology costs.
> [ev-17] WBC/FY25/results_announcement, PDF p18: "Total operating expenses (11,916) (10,944) 9 (6,218) (5,698) 9"
> [ev-18] WBC/FY25/results_announcement, PDF p18: "Full Year 2025 - Full Year 2024 Total operating expenses increased 9% to $11,916 million."
> [ev-33] WBC/FY25/results_announcement, PDF p9: "Operating expenses (11,916) (10,944) 9 (6,218) (5,698) 9"

### credit_impairment_charge — "Impairment (charges)/benefits"
*+113 $m | confidence 80/100*

Credit impairment charges decreased by $113 million (-21%) to $424 million, providing a positive contribution to earnings as loan loss provisions were lower than the prior year.
> [ev-25] WBC/FY25/results_announcement, PDF p8: "Impairment (charges)/benefits (424) (537) (21) (174) (250) (30)"
> [ev-34] WBC/FY25/results_announcement, PDF p9: "Impairment (charges)/benefits (424) (537) (21) (174) (250) (30)"

### tax_and_other — "Income tax expense"
*+24 $m | confidence 80/100*

Tax expense decreased slightly by $24 million (-1%) to $3,135 million, contributing positively to the bottom line.
> [ev-35] WBC/FY25/results_announcement, PDF p9: "Income tax expense (3,135) (3,169) (1) (1,555) (1,580) (2)"

## Notable items
- Hedging items reduced net profit after tax in 2025 by $56 million (2024: $123 million reduction).

## Limitations
- The bridge reconciles the movement in 'Net profit excluding Notable Items' (cash basis). The statutory profit movement differs slightly due to the change in notable items impact.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Failed check: drivers_reconcile (drivers -134.0 + residual +0.0 != delta -141.0, tol 1.0)
- Failed check: movement_from_variant (the row you read is a 'excluding notable' variant: row 'Net profit excluding Notable Items', column Full Year Sept 2024 -> column Full Year Sept 2025. Read the headline measure instead, and report the variant as context or as a disagreement)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T18:11:31+00:00
- seconds: 107.6
- cost_usd: 0.0037
- tokens: 61124 in / 14255 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
