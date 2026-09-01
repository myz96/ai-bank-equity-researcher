# NAB — nim — 1H26 vs 1H25

**Movement (cash basis):** 170bps → 181bps (+11bps) | **Attribution confidence:** 40/100

*Read from: row 'Group net interest margin (%)', column Mar 25 column -> column Mar 26 column*

NAB's Group net interest margin rose 11 bps in 1H26 (Mar 26) to 1.81% from 1.70% in 1H25 (Mar 25), per the results book KPI table (ev-9). The investor presentation corroborates the levels (1.81% Mar 26, 1.70% Mar 25; ev-16/18). The bank's year-on-year decomposition (results book p26) attributes the +11 bps to: +4 bps M&T, +3 bps lower mix of lower-yielding HQLA, +6 bps higher earnings on deposit and capital replicating portfolios, +1 bp lower short-term wholesale funding costs, +1 bp lower deposit costs and deposit mix, offset by -4 bps lending margin (ev-11/12/13/14/10). These sum to +11 bps with zero residual. The bank's published walk charts (results book p26 and presentation p25) are the half-on-half (Sep 25→Mar 26) walk, a different comparison, and are reported as context only.

> [ev-9] NAB/1H26/results_book, printed p22: "Group net interest margin (%) 1.81 1.78 1.70 3 bps 11 bps"
> [ev-16] NAB/1H26/investor_presentation, printed p25: "1.81%"
> [ev-17] NAB/1H26/investor_presentation, printed p25: "1.78%"
> [ev-18] NAB/1H26/investor_presentation, printed p25: "1.70%"
> [ev-11] NAB/1H26/results_book, printed p22: "The Group's net interest margin increased by 11 basis points. Excluding an increase of 4 basis points in M&T and 3 basis points from a lower mix of lower yielding HQLA, the margin increased by 4 basis points due to:"
> [ev-12] NAB/1H26/results_book, printed p22: "an increase of 6 basis points primarily driven by higher earnings on deposit and capital replicating portfolios,"
> [ev-13] NAB/1H26/results_book, printed p22: "an increase of 1 basis point driven by lower short-term wholesale funding costs, and"
> [ev-14] NAB/1H26/results_book, printed p22: "an increase of 1 basis point mainly driven by lower deposit costs, combined with deposit mix benefits, partially offset by competitive pressures impacting deposits in New Zealand Banking."
> [ev-10] NAB/1H26/results_book, printed p22: "These increases were partially offset by a decrease of 4 basis points in lending margin primarily driven by competitive pressures impacting both the business and housing lending portfolios, as well as timing differences between movements in interest rates and pricing changes in home lending in Australia (-1 basis point)."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `asset_pricing` | Lending margin | -4 bps | 85 | 1 () | ev-10 |
| `capital_replicating` | Deposit and capital replicating portfolios | +6 bps | 85 | 1 () | ev-12 |
| `markets_treasury` | M&T | +4 bps | 85 | 1 () | ev-11 |
| `liquids` | Lower HQLA mix | +3 bps | 85 | 1 () | ev-11 |
| `funding.wholesale` | Lower short-term wholesale funding costs | +1 bps | 85 | 1 () | ev-13 |
| `funding.deposits` | Lower deposit costs and deposit mix | +1 bps | 85 | 1 () | ev-14 |
| *residual (unexplained)* | — | +0 bps | — | — |

### asset_pricing — "Lending margin"
*-4 bps | confidence 85/100*

Decrease of 4 bps in lending margin, primarily driven by competitive pressures impacting both the business and housing lending portfolios, as well as timing differences between interest-rate movements and pricing changes in home lending in Australia (-1 bp).
> [ev-10] NAB/1H26/results_book, printed p22: "These increases were partially offset by a decrease of 4 basis points in lending margin primarily driven by competitive pressures impacting both the business and housing lending portfolios, as well as timing differences between movements in interest rates and pricing changes in home lending in Australia (-1 basis point)."

### capital_replicating — "Deposit and capital replicating portfolios"
*+6 bps | confidence 85/100*

Increase of 6 bps primarily driven by higher earnings on deposit and capital replicating portfolios.
> [ev-12] NAB/1H26/results_book, printed p22: "an increase of 6 basis points primarily driven by higher earnings on deposit and capital replicating portfolios,"

### markets_treasury — "M&T"
*+4 bps | confidence 85/100*

Increase of 4 bps in Markets and Treasury (M&T), excluded from the underlying 4 bps increase.
> [ev-11] NAB/1H26/results_book, printed p22: "The Group's net interest margin increased by 11 basis points. Excluding an increase of 4 basis points in M&T and 3 basis points from a lower mix of lower yielding HQLA, the margin increased by 4 basis points due to:"

### liquids — "Lower HQLA mix"
*+3 bps | confidence 85/100*

Increase of 3 bps from a lower mix of lower-yielding high-quality liquid assets (HQLA), excluded from the underlying 4 bps increase.
> [ev-11] NAB/1H26/results_book, printed p22: "The Group's net interest margin increased by 11 basis points. Excluding an increase of 4 basis points in M&T and 3 basis points from a lower mix of lower yielding HQLA, the margin increased by 4 basis points due to:"

### funding.wholesale — "Lower short-term wholesale funding costs"
*+1 bps | confidence 85/100*

Increase of 1 bp driven by lower short-term wholesale funding costs.
> [ev-13] NAB/1H26/results_book, printed p22: "an increase of 1 basis point driven by lower short-term wholesale funding costs, and"

### funding.deposits — "Lower deposit costs and deposit mix"
*+1 bps | confidence 85/100*

Increase of 1 bp mainly driven by lower deposit costs, combined with deposit mix benefits, partially offset by competitive pressures impacting deposits in New Zealand Banking.
> [ev-14] NAB/1H26/results_book, printed p22: "an increase of 1 basis point mainly driven by lower deposit costs, combined with deposit mix benefits, partially offset by competitive pressures impacting deposits in New Zealand Banking."

## Limitations
- No year-on-year (Mar 25→Mar 26) walk chart exists in either document. Both published walk charts (results book p26 and investor presentation p25) are the half-on-half (Sep 25→Mar 26) walk: Lending margin -4, Funding costs 0, Deposits +1, Replicating portfolios +3, Liquid assets +1, M&T +2, total +3 bps (ev-1, ev-2, ev-15). These HoH bars are a different comparison and were NOT used as year-on-year contributions; the year-on-year driver table is built from the bank's narrative decomposition on results book p26.
- The year-on-year driver decomposition appears in only one document (results book p26), so each driver is capped at confidence 85 per the single-source rule.
- The investor presentation p25 chart was read by the chart tool as 'primary' (Mar 25→Mar 26) but its title and text ('Net interest margin (HoH)', 'HoH increase 3bps') confirm it is the half-on-half walk; its bars sum to +3 bps (1.78→1.81), not the +11 bps year-on-year movement.
- Failed check: walk_sum (start 170 + bars +3.0 = 173.0 != end 181, tol 0.1 %) [NAB/1H26/investor_presentation PDF p25 (ev-2)]

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: NAB/1H26/results_book (4b4984ec002d), NAB/1H26/investor_presentation (520f2a59967e)
- generated: 2026-09-01T07:37:32+00:00
- seconds: 875.1
- cost_usd: 0.0054
- tokens: 179500 in / 9434 out
- orchestration: agent
- tool_calls: 17
- pages_read: 4
- charts_read: 2
- budget_exhausted: no
