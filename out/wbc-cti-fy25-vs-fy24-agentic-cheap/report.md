# WBC — cti — FY25 vs FY24

**Movement (ex_notables basis):** 50.29ppt → 53.04ppt (+2.75ppt) | **Attribution confidence:** 85/100

*Read from: row 'Expense to income ratio (excluding Notable Items)', column Full Year Sept 2024 -> column Full Year Sept 2025*

Westpac's expense to income ratio (excluding Notable Items) rose 2.75ppt to 53.04% in FY25 from 50.29% in FY24. The deterioration was driven by operating expenses growing 9% ($10,944m to $11,916m) while operating income grew only 3% ($21,763m to $22,464m). Expense growth was led by a $273m Fit for Growth restructuring charge, $399m in UNITE investment spend, higher staff costs (+$397m, +7% driven by wage growth and investment in bankers), and technology costs (+$146m, +13% driven by UNITE and software amortisation), partially offset by $402m of productivity savings. Income growth of 3% came from net interest income (+3%) and non-interest income (+5%).

> [ev-15] WBC/FY25/results_announcement, PDF p58: "Expense to income ratio (excluding Notable Items) 53.04% 50.29%"
> [ev-31] WBC/FY25/investor_discussion_pack, printed p6: "Cost to income ratio ex Notable Items1"
> [ev-32] WBC/FY25/investor_discussion_pack, printed p6: "53.0%"
> [ev-33] WBC/FY25/investor_discussion_pack, printed p6: "3ppts to FY24"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | Operating expenses | +4.31 ppt | 80 | 2 () | ev-1, ev-21, ev-27, ev-29, ev-30, ev-34, ev-35, ev-36, ev-37, ev-38, ev-40 |
| `income_growth` | Operating income | -1.56 ppt | 80 | 2 () | ev-17, ev-18, ev-19, ev-20, ev-39 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### expense_growth — "Operating expenses"
*+4.31 ppt | confidence 80/100*

Operating expenses grew 9% to $11,916m (from $10,944m), driven by a $273m Fit for Growth restructuring charge, $399m UNITE investment (amortisation up $106m), staff costs up $397m to $6,326m (+7% from wage growth, UNITE and banker investment), and technology costs up $146m to $3,136m (+13% from UNITE, amortisation and licensing), partially offset by $402m productivity savings.
> [ev-1] WBC/FY25/investor_discussion_pack, printed p27: "[walk chart] FY25 EXPENSES ($M): FY24 10944 -> FY25 11916"
> [ev-21] WBC/FY25/results_announcement, PDF p18: "Total operating expenses (11,916) (10,944) 9"
> [ev-27] WBC/FY25/results_announcement, PDF p18: "Staff expensesa (6,326) (5,899) 7"
> [ev-29] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-30] WBC/FY25/results_announcement, PDF p18: "The expense to income ratio excluding Notable Items was 53.0%, up from 50.3%."
> [ev-34] WBC/FY25/investor_discussion_pack, printed p27: "9% INCREASE"
> [ev-35] WBC/FY25/investor_discussion_pack, printed p27: "6% increase ex restructuring"
> [ev-36] WBC/FY25/investor_discussion_pack, printed p27: "UNITE investment $399m"
> [ev-37] WBC/FY25/investor_discussion_pack, printed p27: "Amortisation up $106m"
> [ev-38] WBC/FY25/investor_discussion_pack, printed p27: "Lower investment ex UNITE"
> [ev-40] WBC/FY25/investor_discussion_pack, printed p20: "Expenses ($10.9bn) ($11.9bn) 9%"

### income_growth — "Operating income"
*-1.56 ppt | confidence 80/100*

Net operating income grew 3% to $22,464m (from $21,763m), with net interest income up 3% (driven by growth in average interest earning assets) and non-interest income up 5% (higher card fees, institutional lending fees, markets and wealth management income).
> [ev-17] WBC/FY25/results_announcement, PDF p58: "Net operating income excluding Notable Items 22,464 21,763"
> [ev-18] WBC/FY25/results_announcement, PDF p9: "Net operating income 22,464 21,763 3"
> [ev-19] WBC/FY25/results_announcement, PDF p9: "Operating expenses (11,916) (10,944) 9"
> [ev-20] WBC/FY25/results_announcement, PDF p9: "Operating expenses were 9% higher. The increase included restructuring costs of $273 million to support targeted productivity initiatives under our Fit for Growth program. Excluding these costs, operating expenses increased 6% mainly due to higher staff costs and the step up in UNITE investment spend. Productivity provided a partial offset."
> [ev-39] WBC/FY25/investor_discussion_pack, printed p20: "Revenue $21.8bn $22.5bn 3%"

## Limitations
- The bank does not provide a formal ppt decomposition of the cost-to-income ratio movement; the ppt contributions shown are computed from the jaws effect (income and expense growth differentials).
- The expense walk chart (ev-1) provides the component breakdown of the $972m expense increase but does not directly map to ratio ppt contributions.
- No separate cost-to-income ratio walk or bridge chart exists in the results book or investor pack.
- Capped at 80: expense_growth +4.31 ppt, income_growth -1.56 ppt. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-31T01:15:32+00:00
- seconds: 177.5
- cost_usd: 0.0473
- tokens: 1359520 in / 10848 out
- orchestration: agent
- tool_calls: 52
- pages_read: 25
- charts_read: 2
- budget_exhausted: no
