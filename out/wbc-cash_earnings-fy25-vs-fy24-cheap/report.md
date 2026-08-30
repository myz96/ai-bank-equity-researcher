# WBC — cash_earnings — FY25 vs FY24

**Movement (ex_notables basis):** 7113$m → 6972$m (-141$m) | **Attribution confidence:** 40/100

*Read from: row 'Net profit excluding Notable Items', column Full Year Sept 2024 -> column Full Year Sept 2025*

Westpac's cash earnings (net profit excluding Notable Items) declined $141 million (-2%) to $6,972 million in FY25, compared to $7,113 million in FY24. The decline was driven by a $972 million increase in operating expenses and a $128 million reduction in pre-provision profit, partially offset by a $113 million improvement in credit impairment charges and stable tax expense.

> [ev-41] WBC/FY25/results_announcement, PDF p9: "Net profit excluding Notable Items 6,972 7,113 (2) 3,515 3,457 2"
> [ev-59] WBC/FY25/investor_discussion_pack, printed p42: "Statutory net profit 6,990 6,916 3,317 3,599 Hedging items (123) (56) (140) 84 Net profit excluding Notable Items 7,113 6,972 3,457 3,515"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `nii` | Net interest income | +557 $m | 80 | 1 (single_source) | ev-1, ev-2, ev-10 |
| `other_operating_income` | Non-interest income | +157 $m | 80 | 1 (single_source) | ev-33, ev-42, ev-43, ev-44 |
| `operating_expenses` | Operating expenses | -972 $m | 80 | 1 (single_source) | ev-12, ev-13, ev-14, ev-15, ev-16, ev-17 |
| `credit_impairment_charge` | Impairment (charges)/benefits | +113 $m | 80 | 1 (single_source) | ev-25 |
| `tax_and_other` | Income tax expense | +24 $m | 80 | 1 (single_source) | ev-39 |
| *residual (unexplained)* | — | -32 $m | — | — |

### nii — "Net interest income"
*+557 $m | confidence 80/100*

NII increased $557 million (+3%) to $19,473 million (ev-1). Core NII rose $583 million (+3%) to $18,191 million (ev-2), while Treasury & Markets income fell $17 million (-2%) to $1,282 million (ev-10).
> [ev-1] WBC/FY25/results_announcement, PDF p11: "Net interest income 19,473 18,916 3"
> [ev-2] WBC/FY25/results_announcement, PDF p11: "Core net interest income 18,191 17,608 3"
> [ev-10] WBC/FY25/results_announcement, PDF p11: "Treasury and Markets income, down 2% to $1,282 million due to a stronger performance from Treasury in the prior year."

### other_operating_income — "Non-interest income"
*+157 $m | confidence 80/100*

Non-interest income increased $157 million (+5%) to $2,991 million (ev-33). Net fees rose $60 million (+4%) to $1,732 million (ev-42), net wealth management rose $35 million (+8%) to $476 million (ev-43), and trading income rose $13 million (+2%) to $717 million (ev-44).
> [ev-33] WBC/FY25/results_announcement, PDF p9: "Non-interest income 2,991 2,847 5 1,567 1,424 10"
> [ev-42] WBC/FY25/results_announcement, PDF p53: "Net fees 1,732 1,672 4 887 845 5"
> [ev-43] WBC/FY25/results_announcement, PDF p53: "Net wealth management 476 441 8 242 234 3"
> [ev-44] WBC/FY25/results_announcement, PDF p53: "Trading 717 704 2 419 298 41"

### operating_expenses — "Operating expenses"
*-972 $m | confidence 80/100*

Total operating expenses increased $972 million (+9%) to $11,916 million (ev-17). Staff expenses rose $427 million (+7%) to $6,326 million (ev-12), technology expenses rose $372 million (+13%) to $3,136 million (ev-14), occupancy expenses fell $48 million (-7%) to $652 million (ev-13), other expenses fell $52 million (-3%) to $1,529 million (ev-15), and Fit for Growth restructuring costs were $273 million (ev-16).
> [ev-12] WBC/FY25/results_announcement, PDF p18: "Staff expensesa (6,326) (5,899) 7 (3,211) (3,115) 3"
> [ev-13] WBC/FY25/results_announcement, PDF p18: "Occupancy expenses (652) (700) (7) (334) (318) 5"
> [ev-14] WBC/FY25/results_announcement, PDF p18: "Technology expenses (3,136) (2,764) 13 (1,656) (1,480) 12"
> [ev-15] WBC/FY25/results_announcement, PDF p18: "Other expensesa (1,529) (1,581) (3) (744) (785) (5)"
> [ev-16] WBC/FY25/results_announcement, PDF p18: "Fit for Growth restructuring expenses (273) - - (273) - -"
> [ev-17] WBC/FY25/results_announcement, PDF p18: "Total operating expenses (11,916) (10,944) 9 (6,218) (5,698) 9"

### credit_impairment_charge — "Impairment (charges)/benefits"
*+113 $m | confidence 80/100*

Impairment charges decreased $113 million (-21%) to $424 million (ev-25). Lower charges contributed positively to earnings growth.
> [ev-25] WBC/FY25/results_announcement, PDF p8: "Impairment (charges)/benefits (424) (537) (21) (174) (250) (30)"

### tax_and_other — "Income tax expense"
*+24 $m | confidence 80/100*

Tax expense decreased $34 million (-1%) to $3,135 million (ev-39). This decrease provided a positive contribution to net profit.
> [ev-39] WBC/FY25/results_announcement, PDF p9: "Income tax expense (3,135) (3,169) (1) (1,555) (1,580) (2)"

## Notable items
- Hedging items reduced statutory profit by $56 million in FY25 (FY24: $123 million reduction).

## Limitations
- The sum of the quantified drivers ($779 million) does not fully reconcile with the total movement (-$141 million), leaving a residual of -$32 million. This residual likely represents minor rounding differences or unallocated components within the reported line items.
- Capped at 80: nii +557 $m, other_operating_income +157 $m, operating_expenses -972 $m, credit_impairment_charge +113 $m, tax_and_other +24 $m. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.
- Failed check: drivers_reconcile (drivers -121.0 + residual -32.0 != delta -141.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T15:03:48+00:00
- seconds: 100.2
- cost_usd: 0.0048
- tokens: 74954 in / 19921 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
