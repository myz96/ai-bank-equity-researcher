# NAB — nim — FY25 vs FY24

**Movement (cash basis):** 171bps → 174bps (+3bps) | **Attribution confidence:** 40/100

*Read from: row 'Group net interest margin (%)', column Sep 24 column (FY24) -> column Sep 25 column (FY25)*

NAB's Group net interest margin rose 3 bps in FY25 to 1.74% from 1.71% in FY24 (results book KPI table). The bank attributes the increase to higher earnings on deposit and capital replicating portfolios (+9 bps), a lower mix of lower-yielding HQLA (+2 bps) and Markets & Treasury (+2 bps), partially offset by higher deposit costs including competitive pressures and deposit mix (-7 bps), higher wholesale funding costs (-2 bps) and a lower lending margin (-1 bp). These six stated drivers sum to +3 bps, matching the reported movement with no residual. The bank's published NIM walk chart covers the half-on-half (Mar 25→Sep 25, +8 bps) comparison, not the FY25-vs-FY24 comparison; the FY25-vs-FY24 decomposition is given in the results book narrative.

> [ev-15] NAB/FY25/results_book, PDF p17: "Group net interest margin (%) 1.74 1.71 3 bps 1.78 1.70 8 bps"
> [ev-16] NAB/FY25/results_book, PDF p17: "an increase of 9 basis points mainly driven by higher earnings on deposit and capital replicating portfolios,"
> [ev-17] NAB/FY25/results_book, PDF p17: "an increase of 2 basis points driven by a lower mix of lower yielding HQLA, and"
> [ev-18] NAB/FY25/results_book, PDF p17: "an increase of 2 basis points in Markets and Treasury."
> [ev-19] NAB/FY25/results_book, PDF p17: "a decrease of 7 basis points mainly driven by higher deposit costs including competitive pressures, combined with deposit mix impacts,"
> [ev-20] NAB/FY25/results_book, PDF p17: "a decrease of 2 basis points driven by higher wholesale funding costs, and"
> [ev-21] NAB/FY25/results_book, PDF p17: "a decrease of 1 basis point in lending margin primarily driven by competitive pressures impacting both the housing and business lending portfolios in Australia, partially offset by higher housing lending margin in New Zealand Banking, and favourable portfolio mix from stronger higher yielding business lending growth relative to housing lending."
> [ev-22] NAB/FY25/investor_presentation, printed p24: "Sep 25 1.78% M&T Liquid Assets Replicating Portfolios Deposits (0.01%) Funding Costs 0.01% Lending Margin 0.00% Mar 25 1.70% Sep 24 1.70% HoH increase 8bps"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `capital_replicating` | Replicating portfolios and other | +9 bps | 80 | 1 () | ev-16 |
| `liquids` | Liquid assets | +2 bps | 80 | 1 () | ev-17 |
| `markets_treasury` | Markets & Treasury (M&T) | +2 bps | 80 | 1 () | ev-18 |
| `funding.deposits` | Deposits | -7 bps | 80 | 1 () | ev-19 |
| `funding.wholesale` | Funding costs | -2 bps | 80 | 1 () | ev-20 |
| `asset_pricing` | Lending margin | -1 bps | 80 | 1 (corroborated_2_sources) | ev-21 |
| *residual (unexplained)* | — | +0 bps | — | — | — |

### capital_replicating — "Replicating portfolios and other"
*+9 bps | confidence 80/100*

The bank states an increase of 9 basis points mainly driven by higher earnings on deposit and capital replicating portfolios. This is the largest positive driver of the FY25 NIM increase.
> [ev-16] NAB/FY25/results_book, PDF p17: "an increase of 9 basis points mainly driven by higher earnings on deposit and capital replicating portfolios,"

### liquids — "Liquid assets"
*+2 bps | confidence 80/100*

The bank states an increase of 2 basis points driven by a lower mix of lower yielding HQLA (high-quality liquid assets).
> [ev-17] NAB/FY25/results_book, PDF p17: "an increase of 2 basis points driven by a lower mix of lower yielding HQLA, and"

### markets_treasury — "Markets & Treasury (M&T)"
*+2 bps | confidence 80/100*

The bank states an increase of 2 basis points in Markets and Treasury.
> [ev-18] NAB/FY25/results_book, PDF p17: "an increase of 2 basis points in Markets and Treasury."

### funding.deposits — "Deposits"
*-7 bps | confidence 80/100*

The bank states a decrease of 7 basis points mainly driven by higher deposit costs including competitive pressures, combined with deposit mix impacts. This is the largest offsetting driver.
> [ev-19] NAB/FY25/results_book, PDF p17: "a decrease of 7 basis points mainly driven by higher deposit costs including competitive pressures, combined with deposit mix impacts,"

### funding.wholesale — "Funding costs"
*-2 bps | confidence 80/100*

The bank states a decrease of 2 basis points driven by higher wholesale funding costs.
> [ev-20] NAB/FY25/results_book, PDF p17: "a decrease of 2 basis points driven by higher wholesale funding costs, and"

### asset_pricing — "Lending margin"
*-1 bps | confidence 80/100*

The bank states a decrease of 1 basis point in lending margin primarily driven by competitive pressures impacting both the housing and business lending portfolios in Australia, partially offset by higher housing lending margin in New Zealand Banking and favourable portfolio mix from stronger higher-yielding business lending growth relative to housing lending.
> [ev-21] NAB/FY25/results_book, PDF p17: "a decrease of 1 basis point in lending margin primarily driven by competitive pressures impacting both the housing and business lending portfolios in Australia, partially offset by higher housing lending margin in New Zealand Banking, and favourable portfolio mix from stronger higher yielding business lending growth relative to housing lending."

## Limitations
- The bank's published NIM walk chart (results book p17 and presentation p24) covers the half-on-half comparison (Mar 25→Sep 25, +8 bps), which is NOT the task comparison. The FY25-vs-FY24 decomposition is given only in the results book narrative text, not as a chart.
- The investor presentation does not publish a separate FY25-vs-FY24 Group NIM walk; its page 24 chart is the HoH walk (ev-22), which corroborates the NIM levels and HoH movement but not the YoY decomposition. The YoY decomposition therefore rests on a single document (results book), capping driver confidence at 85.
- The Group NIM row carries no cash or statutory label; it is reported on the bank's primary (cash) basis per the method.
- Failed check: comparison_leak (liquids claims +2, which is the 'Liquid assets' bar of NAB/FY25/results_book PDF p17 (ev-1), a walk for a different comparison; no walk covers the task comparison, so this bar cannot be a contribution for it — move the number into the driver narrative and name the span it belongs to)
- Failed check: comparison_leak (markets_treasury claims +2, which is the 'Markets & Treasury (M&T)' bar of NAB/FY25/results_book PDF p17 (ev-1), a walk for a different comparison; no walk covers the task comparison, so this bar cannot be a contribution for it — move the number into the driver narrative and name the span it belongs to)
- Failed check: walk_sum (start 170 + bars +60.0 = 230.0 != end 178, tol 0.1 %) [NAB/FY25/investor_presentation PDF p24 (ev-2)]
- Capped at 80: capital_replicating +9 bps, liquids +2 bps, markets_treasury +2 bps, funding.deposits -7 bps, funding.wholesale -2 bps, asset_pricing -1 bps. comparison_leak failed. That check condemns the whole quantified table: it proves one of these claims is wrong, or that the table was read from the wrong column, without saying which claim carries the fault. None of them may claim near-certainty.

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-09-01T18:11:52+00:00
- seconds: 101.4
- cost_usd: 0.0037
- tokens: 170811 in / 10626 out
- latency: 16 calls, 85s in requests (slowest 14s), 1 retries, 0 grace waits, 15s slept
- orchestration: agent
- tool_calls: 15
- pages_read: 3
- charts_read: 2
- budget_exhausted: no
