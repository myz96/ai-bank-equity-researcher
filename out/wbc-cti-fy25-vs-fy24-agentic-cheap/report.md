# WBC — cti — FY25 vs FY24

**Movement (ex_notables basis):** 50.29ppt → 53.04ppt (+2.75ppt) | **Attribution confidence:** 85/100

*Read from: row 'Expense to income ratio (excluding Notable Items)', column Full Year Sept 2024 -> column Full Year Sept 2025*

Westpac’s expense to income ratio (excluding Notable Items) rose 275 basis points (2.75 percentage points) to 53.04% in FY25 from 50.29% in FY24. The deterioration was driven by operating expense growth of 9% (6% excluding the $273 million Fit for Growth restructuring charge) outpacing operating income growth of 3%. Expense growth was led by staff cost increases of $397 million (7% growth, driven by wage growth and UNITE investment), technology expenses up $146 million (13% growth, driven by UNITE program costs and higher software amortisation), and a $273 million restructuring charge. These increases were partially offset by productivity savings of $402 million and lower occupancy costs of $48 million (7% decrease). Income growth of 3% reflected net interest income growth of $557 million and non-interest income growth of $144 million (5%).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | Operating expense growth | +2.75 ppt | 90 | 2 () | ev-4, ev-9, ev-14, ev-15, ev-16 |
| `income_growth` | Operating income growth | -0.01 ppt | 80 | 2 () | ev-3, ev-6 |

### expense_growth — "Operating expense growth"
*+2.75 ppt | confidence 90/100*

Operating expenses increased 9% to $11,916 million from $10,944 million, driven by staff costs up 7% to $6,326 million due to wage growth and UNITE investment, technology expenses up 13% to $3,136 million due to UNITE program costs and higher software amortisation, and a $273 million Fit for Growth restructuring charge. Partially offset by productivity savings of $402 million and occupancy costs down 7% to $652 million.
> [ev-4] WBC/FY25/investor_discussion_pack, printed p27: "[walk chart] FY25 EXPENSES ($M): FY24 10944 -> FY25 11916"
> [ev-9] WBC/FY25/results_announcement, PDF p18: "Total operating expenses (11,916) (10,944) 9"
> [ev-14] WBC/FY25/results_announcement, PDF p18: "Technology expenses increased 13% to $3,136 million due to higher costs related to the UNITE program, an increase in software amortisation related to projects completed in prior years and higher software maintenance and licensing costs."
> [ev-15] WBC/FY25/results_announcement, PDF p18: "Occupancy expenses decreased by 7% to $652 million with further reductions in the Group's corporate and branch footprint."
> [ev-16] WBC/FY25/results_announcement, PDF p18: "Fit for Growth restructuring expenses to support targeted productivity initiatives were $273 million in the Second Half of 2025."

### income_growth — "Operating income growth"
*-0.01 ppt | confidence 80/100*

Net operating income excluding Notable Items increased 3% to $22,464 million from $21,763 million. Net interest income grew $557 million and non-interest income grew $144 million (5%). Income growth was insufficient to offset expense growth, contributing positively to the ratio increase.
> [ev-3] WBC/FY25/results_announcement, PDF p58: "Net operating income excluding Notable Items 22,464 21,763"
> [ev-6] WBC/FY25/investor_discussion_pack, printed p20: "Revenue $21.8bn $22.5bn 3%"

## Limitations
- The ppt split between income and expense growth drivers is approximated; the bank does not publish a formal bridge of the CTI ratio movement into ppt components.
- The expense growth driver includes the $273 million restructuring charge which is a one-time item; ex-restructuring expense growth was 6%.
- Income growth contribution to the ratio movement is small relative to expense growth; the dominant driver is expense growth.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T14:50:08+00:00
- seconds: 174.7
- cost_usd: 0.0462
- tokens: 1380889 in / 9632 out
- orchestration: agent
- tool_calls: 51
- pages_read: 20
- charts_read: 1
- budget_exhausted: no
