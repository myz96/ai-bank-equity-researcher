# WBC — nim — 1H26 vs 1H25

**Movement (ex_notables basis):** 192bps → 189bps (-3bps) | **Attribution confidence:** 40/100

*Read from: row 'NIM (Excluding Notable Items, %)', column March 2025 column -> column March 2026 column*

Westpac's Group net interest margin (NIM, Excluding Notable Items) fell 3 basis points to 1.89% in 1H26 from 1.92% in 1H25 (results book KPI table, ev-19). The bank's own walk (results book p13, ev-1) attributes the -3bps to: Loans -2bps, Deposits -1bp, Timing difference -1bp, Liquid assets +5bps, Wholesale funding 0bps, Capital & other -3bps, and Treasury & Markets -1bp. NIM comprised Core NIM of 1.78% (down 2bps) plus a Treasury & Markets contribution of 11bps (down 1bp) (ev-22, ev-23, ev-24). The investor pack corroborates the levels (1H25 1.92%, 1H26 1.89%, ev-32) but its walk is the half-on-half (2H25→1H26) comparison, so the results book walk is the primary framing for this task.

> [ev-19] WBC/1H26/results_announcement, printed p6: "NIM (Excluding Notable Items, %) NIM 1.89% 1.95% 1.92% (6 bps) (3 bps)"
> [ev-1] WBC/1H26/results_announcement, PDF p13: "[walk chart] Net interest margin movement Excluding Notable Items First Half 2026 – First Half 2025: 1H25 192 -> 1H26 189"
> [ev-22] WBC/1H26/results_announcement, PDF p13: "NIM decreased by 3 basis points to 1.89%. NIM comprised:"
> [ev-23] WBC/1H26/results_announcement, PDF p13: "Core NIM of 1.78%, down 2 basis points, with key drivers described below; and"
> [ev-24] WBC/1H26/results_announcement, PDF p13: "Treasury and Markets contribution of 11 basis points, which was down 1 basis point due to lower Treasury income."
> [ev-32] WBC/1H26/investor_discussion_pack, printed p24: "1.92 1.95 (2bps) - 2bps - 1.89 (3bps) (1bps) (2bps) 1H25 2H25 Timing Difference Loans Deposits Liquid assets Capital & Other Wholesale funding Treasury & Markets 1H26 NET INTEREST MARGIN (%)"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `asset_pricing` | Loans | -2 bps | 90 | 1 (single_source) | ev-1, ev-14 |
| `funding.deposits` | Deposits | -1 bps | 90 | 1 (single_source) | ev-1, ev-15 |
| `rate_timing` | Timing difference | -1 bps | 90 | 1 (single_source) | ev-1, ev-16 |
| `liquids` | Liquid assets | +5 bps | 90 | 1 (single_source) | ev-1, ev-17 |
| `funding.wholesale` | WSF | +0 bps | 90 | 1 (single_source) | ev-1 |
| `capital_replicating` | Capital & other | -3 bps | 90 | 1 (single_source) | ev-1, ev-18 |
| `markets_treasury` | T&M | -1 bps | 90 | 1 (single_source) | ev-1, ev-24 |
| *residual (unexplained)* | — | +0 bps | — | — | — |

### asset_pricing — "Loans"
*-2 bps | confidence 90/100*

Loan interest spread narrowed 2bps: higher spreads in New Zealand were more than offset by tighter spreads in Australia due to competition (ev-14).
> [ev-1] WBC/1H26/results_announcement, PDF p13: "[walk chart] Net interest margin movement Excluding Notable Items First Half 2026 – First Half 2025: 1H25 192 -> 1H26 189"
> [ev-14] WBC/1H26/results_announcement, PDF p13: "Loan interest spread: 2 basis point decrease. Higher spreads in New Zealand were more than offset by tighter spreads in Australia due to competition;"

### funding.deposits — "Deposits"
*-1 bps | confidence 90/100*

Deposit interest spread fell 1bp, driven by a higher proportion of customers qualifying for the savings bonus rate and narrower spreads on term deposits; favourable deposit mix and repricing the base rate of the consumer behavioural product provided a benefit (ev-15).
> [ev-1] WBC/1H26/results_announcement, PDF p13: "[walk chart] Net interest margin movement Excluding Notable Items First Half 2026 – First Half 2025: 1H25 192 -> 1H26 189"
> [ev-15] WBC/1H26/results_announcement, PDF p13: "Deposit interest spread: 1 basis point decrease driven by a higher proportion of customers qualifying for the savings bonus rate and narrower spreads on term deposits. Favourable deposit mix and repricing the base rate of the consumer behavioural product provided a benefit;"

### rate_timing — "Timing difference"
*-1 bps | confidence 90/100*

Timing difference decreased 1bp due to the timing differences of interest rate changes (the delay between the RBA cash-rate change and customer repricing) (ev-16).
> [ev-1] WBC/1H26/results_announcement, PDF p13: "[walk chart] Net interest margin movement Excluding Notable Items First Half 2026 – First Half 2025: 1H25 192 -> 1H26 189"
> [ev-16] WBC/1H26/results_announcement, PDF p13: "Timing difference1: 1 basis point decrease due to the timing differences of interest rate changes;"

### liquids — "Liquid assets"
*+5 bps | confidence 90/100*

Liquid assets added 5bps as trading assets reduced, average liquid assets rose by less than average lending assets and spreads narrowed (ev-17).
> [ev-1] WBC/1H26/results_announcement, PDF p13: "[walk chart] Net interest margin movement Excluding Notable Items First Half 2026 – First Half 2025: 1H25 192 -> 1H26 189"
> [ev-17] WBC/1H26/results_announcement, PDF p13: "Liquid assets: 5 basis point increase as trading assets reduced, average liquid assets rose by less than average lending assets and spreads narrowed; and"

### funding.wholesale — "WSF"
*+0 bps | confidence 90/100*

Wholesale funding costs (WSF) contributed 0bps to the NIM movement in the bank's walk (ev-1).
> [ev-1] WBC/1H26/results_announcement, PDF p13: "[walk chart] Net interest margin movement Excluding Notable Items First Half 2026 – First Half 2025: 1H25 192 -> 1H26 189"

### capital_replicating — "Capital & other"
*-3 bps | confidence 90/100*

Capital and other decreased 3bps due to a remediation provision in the current period and the non-repeat of items in the prior corresponding period (ev-18).
> [ev-1] WBC/1H26/results_announcement, PDF p13: "[walk chart] Net interest margin movement Excluding Notable Items First Half 2026 – First Half 2025: 1H25 192 -> 1H26 189"
> [ev-18] WBC/1H26/results_announcement, PDF p13: "Capital and other: 3 basis point decrease due to a remediation provision in the current period and the non repeat of items in the prior corresponding period."

### markets_treasury — "T&M"
*-1 bps | confidence 90/100*

Treasury & Markets contribution of 11bps was down 1bp due to lower Treasury income (ev-24).
> [ev-1] WBC/1H26/results_announcement, PDF p13: "[walk chart] Net interest margin movement Excluding Notable Items First Half 2026 – First Half 2025: 1H25 192 -> 1H26 189"
> [ev-24] WBC/1H26/results_announcement, PDF p13: "Treasury and Markets contribution of 11 basis points, which was down 1 basis point due to lower Treasury income."

## Limitations
- The investor discussion pack's NIM walk (p24) is the half-on-half 2H25→1H26 comparison, not the task's 1H25→1H26 comparison; its bars were therefore not used as driver contributions. It corroborates only the NIM levels (1H25 1.92%, 1H26 1.89%).
- The task-comparison walk exists only in the results book (p13), which is the primary framing adopted; no second document publishes the same 1H25→1H26 walk for independent corroboration of each bar.
- The bank's walk bars sum to -3bps, matching the stated NIM movement, so no residual is reported.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Failed check: movement_from_variant (the row you read is a 'excluding notable' variant: row 'NIM (Excluding Notable Items, %)', column March 2025 column -> column March 2026 column. Read the headline measure instead, and report the variant as context or as a disagreement)

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: WBC/1H26/results_announcement (5d0e7d301d0e), WBC/1H26/investor_discussion_pack (7af34e986c7f)
- generated: 2026-09-01T18:13:13+00:00
- seconds: 81.1
- cost_usd: 0.004
- tokens: 187247 in / 9709 out
- latency: 17 calls, 80s in requests (slowest 10s), 0 retries, 0 grace waits, 0s slept
- orchestration: agent
- tool_calls: 18
- pages_read: 4
- charts_read: 2
- budget_exhausted: no
