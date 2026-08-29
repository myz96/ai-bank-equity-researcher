# WBC — cash_earnings — FY25 vs FY24

**Movement (ex_notables basis):** 7113$m → 6972$m (-141$m) | **Attribution confidence:** 40/100

*Read from: row 'Net profit excluding Notable Items', column Full Year Sept 2024 -> column Full Year Sept 2025*

Westpac's cash earnings (net profit excluding Notable Items) declined $141 million or 2% to $6,972 million in FY25, compared to $7,113 million in FY24. Statutory profit was $6,916 million (FY24: $6,990 million). Total operating income increased 3% to $22,464 million (FY24: $21,763 million), driven by a 3% rise in net interest income and a 5% rise in non-interest income. However, pre-provision profit fell 3% to $10,548 million as operating expenses rose 9% to $11,916 million, partially offset by a 21% reduction in impairment charges.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `nii` | Net interest income | +557 $m | 80 | 1 (single_source) | ev-1, ev-2, ev-3, ev-8, ev-9, ev-10 |
| `other_operating_income` | Non-interest income | +144 $m | 80 | 1 (single_source) | ev-33, ev-42, ev-43 |
| `operating_expenses` | Operating expenses | -972 $m | 80 | 1 (single_source) | ev-17, ev-18, ev-19 |
| `notable_items` | Fit for Growth restructuring expenses | -273 $m | 80 | 1 (single_source) | ev-16, ev-19 |
| `credit_impairment_charge` | Impairment (charges)/benefits | +113 $m | 80 | 1 (single_source) | ev-26, ev-37 |
| `tax_and_other` | Income tax expense | +34 $m | 80 | 1 (single_source) | ev-39 |
| *residual (unexplained)* | — | +0 $m | — | — |

### nii — "Net interest income"
*+557 $m | confidence 80/100*

NII increased $557 million (3%) to $19,473 million. The bank attributes this to higher core NII ($18,191 million, up 3%), reflecting volume growth and stable margins, partially offset by a $17 million decline in Treasury & Markets income due to a stronger prior year performance.
> [ev-1] WBC/FY25/results_announcement, PDF p11: "Net interest income 19,473 18,916 3"
> [ev-2] WBC/FY25/results_announcement, PDF p11: "Core net interest income 18,191 17,608 3"
> [ev-3] WBC/FY25/results_announcement, PDF p11: "Treasury 1,039 1,056 (2)"
> [ev-8] WBC/FY25/results_announcement, PDF p11: "Net interest income increased 3% to $19,473 million."
> [ev-9] WBC/FY25/results_announcement, PDF p11: "Higher core net interest income, up 3% to $18,191 million."
> [ev-10] WBC/FY25/results_announcement, PDF p11: "Treasury and Markets income, down 2% to $1,282 million due to a stronger performance from Treasury in the prior year."

### other_operating_income — "Non-interest income"
*+144 $m | confidence 80/100*

Non-interest income increased $144 million (5%) to $2,991 million. This was driven by higher net fees ($1,732 million, up 4%) and total non-interest income components, including wealth management and trading income.
> [ev-33] WBC/FY25/results_announcement, PDF p9: "Non-interest income 2,991 2,847 5 1,567 1,424 10"
> [ev-42] WBC/FY25/results_announcement, PDF p53: "Net fees 1,732 1,672 4 887 845 5"
> [ev-43] WBC/FY25/results_announcement, PDF p53: "Total non-interest income 3,004 2,835 6 1,562 1,442 8"

### operating_expenses — "Operating expenses"
*-972 $m | confidence 80/100*

Total operating expenses increased $972 million (9%) to $11,916 million. Underlying expenses rose 6%, while the increase included a $273 million restructuring charge for 'Fit for Growth' initiatives in H2. Staff, technology, and occupancy costs contributed to the rise.
> [ev-17] WBC/FY25/results_announcement, PDF p18: "Total operating expenses (11,916) (10,944) 9 (6,218) (5,698) 9"
> [ev-18] WBC/FY25/results_announcement, PDF p18: "Full Year 2025 - Full Year 2024 Total operating expenses increased 9% to $11,916 million."
> [ev-19] WBC/FY25/results_announcement, PDF p18: "The increase included a restructuring charge of $273 million in the Second Half of 2025 to support targeted productivity initiatives under our Fit for Growth program. Excluding this charge, operating expenses increased by 6%"

### notable_items — "Fit for Growth restructuring expenses"
*-273 $m | confidence 80/100*

A $273 million restructuring charge was incurred in H2 FY25 under the 'Fit for Growth' program. This is reported separately from underlying operating expenses and contributes to the notable items reconciliation.
> [ev-16] WBC/FY25/results_announcement, PDF p18: "Fit for Growth restructuring expenses (273) - - (273) - -"
> [ev-19] WBC/FY25/results_announcement, PDF p18: "The increase included a restructuring charge of $273 million in the Second Half of 2025 to support targeted productivity initiatives under our Fit for Growth program. Excluding this charge, operating expenses increased by 6%"

### credit_impairment_charge — "Impairment (charges)/benefits"
*+113 $m | confidence 80/100*

Impairment charges decreased by $113 million (21%) to $424 million, providing a positive contribution to earnings. This reflects lower credit costs compared to the prior year.
> [ev-26] WBC/FY25/results_announcement, PDF p8: "Impairment (charges)/benefits (424) (537) (21) (174) (250) (30)"
> [ev-37] WBC/FY25/results_announcement, PDF p9: "Impairment (charges)/benefits (424) (537) (21) (174) (250) (30)"

### tax_and_other — "Income tax expense"
*+34 $m | confidence 80/100*

Tax expense decreased slightly by $34 million (1%) to $3,135 million, contributing positively to the bottom line movement relative to the prior year.
> [ev-39] WBC/FY25/results_announcement, PDF p9: "Income tax expense (3,135) (3,169) (1) (1,555) (1,580) (2)"

## Notable items
- Fit for Growth restructuring expenses

## Limitations
- The bridge reconciles the change in 'Net profit excluding Notable Items'. The statutory-to-cash reconciliation items (hedging/IFRS volatility) are excluded from the driver taxonomy as they explain the difference between statutory and cash within a period, not the year-on-year movement of cash earnings.
- Expenses are claimed on the underlying/notable split; the bank equally publishes the combined headline framing, so both claims are capped at 80.
- Failed check: drivers_reconcile (drivers -397.0 + residual +0.0 != delta -141.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T21:04:34+00:00
- seconds: 124.5
- cost_usd: 0.006
- tokens: 94151 in / 24099 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
