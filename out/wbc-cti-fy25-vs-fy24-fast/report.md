# WBC — cti — FY25 vs FY24

**Movement (ex_notables basis):** 50.29ppt → 53.04ppt (+2.75ppt) | **Attribution confidence:** 80/100

*Read from: row 'Expense to income ratio (excluding Notable Items)', column Full Year Sept 2024 -> column Full Year Sept 2025*

Westpac's cost-to-income ratio (Expense to income ratio ex Notable Items) rose 2.75 ppt in FY25, from 50.29% in FY24 to 53.04% in FY25 (results book p58; investor pack p6 shows 53.0%, up 3ppts). The rise reflects negative jaws: operating expenses grew 9% to $11,916m while net operating income excluding Notable Items grew only 3.2% to $22,464m, so expense growth outran income growth and pushed the ratio up. The bank's FY25 expenses bridge decomposes the +$972m expense rise into staff costs, technology, volume and other, investments and a restructuring charge, partly offset by productivity savings. Notable Items on operating expenses were nil in both years, so they contributed nothing to the ratio.

> [ev-1] WBC/FY25/results_announcement, PDF p58: "Expense to income ratio (excluding Notable Items) 53.04% 50.29% 54.21% 51.83%"
> [ev-10] WBC/FY25/investor_discussion_pack, printed p6: "53.0% Cost to income ratio ex Notable Items1 3ppts to FY24"
> [ev-3] WBC/FY25/results_announcement, PDF p58: "Net operating income excluding Notable Items 22,464 21,763 11,471 10,993"
> [ev-4] WBC/FY25/results_announcement, PDF p18: "Total operating expenses (11,916) (10,944) 9 (6,218) (5,698) 9"
> [ev-11] WBC/FY25/investor_discussion_pack, printed p27: "[walk chart] FY25 EXPENSES ($M): FY24 10944 -> FY25 11916"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `notable_items` | Notable Items | +0 ppt | 80 | 1 (single_source) | ev-25 |
| *residual (unexplained)* | — | +2.75 ppt | — | — | — |

### expense_growth — "Operating expenses (jaws denominator)"
*unquantified | confidence 90/100*

Operating expenses grew 9% to $11,916m from $10,944m, faster than income, raising the ratio. The bank's FY25 expenses bridge splits the +$972m into staff costs +$397m, technology +$146m, volume and other +$199m, investments +$359m and restructuring charge +$273m, partly offset by productivity -$402m. Driven by UNITE investment, wage growth, higher software amortisation and the Fit for Growth restructuring charge; occupancy fell 7%.
> [ev-4] WBC/FY25/results_announcement, PDF p18: "Total operating expenses (11,916) (10,944) 9 (6,218) (5,698) 9"
> [ev-6] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million. The increase included a restructuring charge of $273 million in the Second Half of 2025 to support targeted productivity initiatives under our Fit for Growth program. Excluding this charge, operating expenses increased by 6% due to the ramp up in UNITE investment, wage growth and higher software amortisation."
> [ev-11] WBC/FY25/investor_discussion_pack, printed p27: "[walk chart] FY25 EXPENSES ($M): FY24 10944 -> FY25 11916"
> [ev-23] WBC/FY25/investor_discussion_pack, printed p27: "9% INCREASE"
> [ev-24] WBC/FY25/investor_discussion_pack, printed p27: "6% increase ex restructuring"
> [ev-22] WBC/FY25/investor_discussion_pack, printed p27: "UNITE investment $399m Amortisation up $106m Lower investment ex UNITE"
> [ev-7] WBC/FY25/results_announcement, PDF p18: "Staff expenses1 increased by 7% to $6,326 million mainly due to wage growth, UNITE and the investment in bankers."
> [ev-8] WBC/FY25/results_announcement, PDF p18: "Technology expenses increased 13% to $3,136 million due to higher costs related to the UNITE program, an increase in software amortisation related to projects completed in prior years and higher software maintenance and licensing costs."
> [ev-9] WBC/FY25/results_announcement, PDF p18: "Occupancy expenses decreased by 7% to $652 million with further reductions in the Group's corporate and branch footprint."

### income_growth — "Operating income growth (jaws numerator)"
*unquantified | confidence 80/100*

Net operating income excluding Notable Items grew 3.2% to $22,464m from $21,763m, slower than expenses, so income growth did not offset the expense rise. Net interest income +3% to $19,473m and non-interest income +5% to $2,991m. Revenue rose 3% to $22.5bn per the investor pack.
> [ev-3] WBC/FY25/results_announcement, PDF p58: "Net operating income excluding Notable Items 22,464 21,763 11,471 10,993"
> [ev-26] WBC/FY25/results_announcement, PDF p11: "Net interest income increased 3% to $19,473 million."
> [ev-27] WBC/FY25/results_announcement, PDF p16: "Non-interest income increased by 5% to $2,991 million."
> [ev-21] WBC/FY25/investor_discussion_pack, printed p20: "Revenue $21.8bn $22.5bn 3% Expenses ($10.9bn) ($11.9bn) 9% Expenses excluding restructuring charge ($10.9bn) ($11.6bn) 6%"

### notable_items — "Notable Items"
*+0 ppt | confidence 80/100*

Notable Items on operating expenses were nil in both FY25 and FY24, so notable items contributed nothing to the ratio movement; the ratio is reported ex Notable Items.
> [ev-25] WBC/FY25/results_announcement, PDF p58: "Less: Notable Items (operating expenses) - - - -"

## Limitations
- The bank does not publish a ppt decomposition of the cost-to-income ratio movement into income vs expense contributions; the FY25 expenses bridge (investor pack p27) is a $m bridge of the expense level, not a ppt bridge of the ratio. Accordingly the income_growth and expense_growth contributions are left unquantified in ppt and the full +2.75 ppt movement is reported as residual.
- The jaws growth rates (income +3.2%, expenses +8.9%) are computed by subtracting the disclosed FY25 and FY24 levels, so they are capped at 80 confidence.
- The investor pack p48 expenses bridge and p40 net profit bridge describe the half-on-half (2H25 vs 2H24) comparison, a different question from this task, and were not used for the driver table.
- Capped at 80: notable_items +0 ppt. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-09-01T17:56:49+00:00
- seconds: 125.1
- cost_usd: 0.0096
- tokens: 618352 in / 16404 out
- latency: 28 calls, 124s in requests (slowest 18s), 0 retries, 0 grace waits, 0s slept
- orchestration: agent
- tool_calls: 43
- pages_read: 19
- charts_read: 1
- budget_exhausted: no
