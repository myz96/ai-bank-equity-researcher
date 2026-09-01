# NAB — nim — 1H26 vs 1H25

**Movement (cash basis):** 170bps → 181bps (+11bps) | **Attribution confidence:** 40/100

*Read from: row 'Group net interest margin (%)', column Mar 25 column -> column Mar 26 column*

NAB's Group net interest margin rose 11 bps in 1H26 (Mar 26) to 1.81% from 1.70% in 1H25 (Mar 25), per the results book KPI table (ev-15). The investor presentation corroborates the levels, showing Mar 25 1.70% and Mar 26 1.81% (ev-24, ev-22). The bank's stated decomposition of the +11 bps: +4 bps M&T, +3 bps lower mix of lower-yielding HQLA, +6 bps higher earnings on deposit and capital replicating portfolios, +1 bp lower short-term wholesale funding costs, +1 bp lower deposit costs with deposit mix benefits, offset by -4 bps lending margin (ev-17 to ev-20, ev-16). These sum to +11 bps with no residual. The published walk charts (results book p26 and presentation p25) are the half-on-half (Sep 25 → Mar 26) movement, +3 bps, which is context, not the task comparison.

> [ev-15] NAB/1H26/results_book, printed p22: "Group net interest margin (%) 1.81 1.78 1.70 3 bps 11 bps"
> [ev-24] NAB/1H26/investor_presentation, printed p25: "1.70%"
> [ev-22] NAB/1H26/investor_presentation, printed p25: "1.81%"
> [ev-17] NAB/1H26/results_book, printed p22: "The Group's net interest margin increased by 11 basis points. Excluding an increase of 4 basis points in M&T and 3 basis points from a lower mix of lower yielding HQLA, the margin increased by 4 basis points due to:"
> [ev-18] NAB/1H26/results_book, printed p22: "an increase of 6 basis points primarily driven by higher earnings on deposit and capital replicating portfolios,"
> [ev-19] NAB/1H26/results_book, printed p22: "an increase of 1 basis point driven by lower short-term wholesale funding costs, and"
> [ev-20] NAB/1H26/results_book, printed p22: "an increase of 1 basis point mainly driven by lower deposit costs, combined with deposit mix benefits, partially offset by competitive pressures impacting deposits in New Zealand Banking."
> [ev-16] NAB/1H26/results_book, printed p22: "These increases were partially offset by a decrease of 4 basis points in lending margin primarily driven by competitive pressures impacting both the business and housing lending portfolios, as well as timing differences between movements in interest rates and pricing changes in home lending in Australia (-1 basis point)."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `markets_treasury` | M&T | +4 bps | 85 | 1 () | ev-17 |
| `liquids` | Lower mix of lower yielding HQLA | +3 bps | 85 | 1 () | ev-17 |
| `capital_replicating` | Deposit and capital replicating portfolios | +6 bps | 85 | 1 () | ev-18 |
| `funding.wholesale` | Lower short-term wholesale funding costs | +1 bps | 85 | 1 () | ev-19 |
| `funding.deposits` | Lower deposit costs and deposit mix benefits | +1 bps | 85 | 1 () | ev-20 |
| `asset_pricing` | Lending margin | -4 bps | 85 | 1 () | ev-16 |
| *residual (unexplained)* | — | +0 bps | — | — | — |

### markets_treasury — "M&T"
*+4 bps | confidence 85/100*

The bank states an increase of 4 basis points in M&T, excluded from the underlying margin. The presentation's HoH walk corroborates M&T as a positive contributor (+2 bps Sep 25→Mar 26, context).
> [ev-17] NAB/1H26/results_book, printed p22: "The Group's net interest margin increased by 11 basis points. Excluding an increase of 4 basis points in M&T and 3 basis points from a lower mix of lower yielding HQLA, the margin increased by 4 basis points due to:"

### liquids — "Lower mix of lower yielding HQLA"
*+3 bps | confidence 85/100*

The bank states 3 basis points from a lower mix of lower yielding HQLA (high-quality liquid assets), excluded from the underlying margin. The HoH walk corroborates Liquid Assets +1 bp (context).
> [ev-17] NAB/1H26/results_book, printed p22: "The Group's net interest margin increased by 11 basis points. Excluding an increase of 4 basis points in M&T and 3 basis points from a lower mix of lower yielding HQLA, the margin increased by 4 basis points due to:"

### capital_replicating — "Deposit and capital replicating portfolios"
*+6 bps | confidence 85/100*

The bank states an increase of 6 basis points primarily driven by higher earnings on deposit and capital replicating portfolios. The HoH walk corroborates Replicating Portfolios +3 bps (context).
> [ev-18] NAB/1H26/results_book, printed p22: "an increase of 6 basis points primarily driven by higher earnings on deposit and capital replicating portfolios,"

### funding.wholesale — "Lower short-term wholesale funding costs"
*+1 bps | confidence 85/100*

The bank states an increase of 1 basis point driven by lower short-term wholesale funding costs. The HoH walk corroborates Funding Costs flat (0.00) for the half-on-half (context).
> [ev-19] NAB/1H26/results_book, printed p22: "an increase of 1 basis point driven by lower short-term wholesale funding costs, and"

### funding.deposits — "Lower deposit costs and deposit mix benefits"
*+1 bps | confidence 85/100*

The bank states an increase of 1 basis point mainly driven by lower deposit costs, combined with deposit mix benefits, partially offset by competitive pressures impacting deposits in New Zealand Banking. The HoH walk corroborates Deposits +1 bp (context).
> [ev-20] NAB/1H26/results_book, printed p22: "an increase of 1 basis point mainly driven by lower deposit costs, combined with deposit mix benefits, partially offset by competitive pressures impacting deposits in New Zealand Banking."

### asset_pricing — "Lending margin"
*-4 bps | confidence 85/100*

The bank states a decrease of 4 basis points in lending margin primarily driven by competitive pressures impacting both the business and housing lending portfolios, as well as timing differences between movements in interest rates and pricing changes in home lending in Australia (-1 basis point). The HoH walk corroborates Lending Margin -4 bps (context).
> [ev-16] NAB/1H26/results_book, printed p22: "These increases were partially offset by a decrease of 4 basis points in lending margin primarily driven by competitive pressures impacting both the business and housing lending portfolios, as well as timing differences between movements in interest rates and pricing changes in home lending in Australia (-1 basis point)."

## Notable items
- NIM ex M&T
- NIM ex M&T and Liquid Assets

## Limitations
- The published walk charts (results book p26 and investor presentation p25) both describe the HALF-ON-HALF movement (Sep 25 → Mar 26, +3 bps), which is context, not the task comparison (Mar 25 → Mar 26, +11 bps). No primary walk chart exists for the task comparison, so the driver table is built from the bank's stated narrative decomposition of the +11 bps in the results book (ev-17 to ev-20, ev-16), which sums to +11 bps with no residual.
- The investor presentation p25 chart is labelled 'Net interest margin (HoH)' and its bars (Lending Margin -4, Funding Costs 0, Deposits +1, Replicating Portfolios +3, Liquid Assets +1, M&T +2) sum to +3 bps matching Sep 25→Mar 26; the read_chart tool's 'primary' classification with start 170 failed its walk-sum check, confirming it is the HoH walk, not the task comparison.
- The +11 bps movement is corroborated across two documents (results book states +11 bps; presentation shows 1.70%→1.81%), but the driver decomposition appears only in the results book narrative, so each driver is capped at 85 confidence.
- The bank reports a variant 'NIM ex M&T' and 'NIM ex M&T and Liquid Assets'; the underlying margin (ex M&T and HQLA mix) increased 4 bps, per the narrative.
- Failed check: walk_sum (start 170 + bars +3.0 = 173.0 != end 181, tol 0.1 %) [NAB/1H26/investor_presentation PDF p25 (ev-2)]

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: NAB/1H26/results_book (4b4984ec002d), NAB/1H26/investor_presentation (520f2a59967e)
- generated: 2026-09-01T18:10:11+00:00
- seconds: 91.6
- cost_usd: 0.0038
- tokens: 158992 in / 12323 out
- latency: 15 calls, 91s in requests (slowest 17s), 0 retries, 0 grace waits, 0s slept
- orchestration: agent
- tool_calls: 16
- pages_read: 4
- charts_read: 2
- budget_exhausted: no
