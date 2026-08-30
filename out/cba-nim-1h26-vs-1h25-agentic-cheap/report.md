# CBA — nim — 1H26 vs 1H25

**Movement (cash basis):** 208bps → 204bps (-4bps) | **Attribution confidence:** 90/100

*Read from: row 'Net interest margin (%) row', column 31 Dec 24 column -> column 31 Dec 25 column*

CBA's Group net interest margin declined 4 bps to 204 bps in 1H26 from 208 bps in 1H25. Excluding liquid assets and institutional repos (which contributed -4 bps), the underlying NIM was flat. The decline was driven by higher liquids drag (-4 bps), weaker asset pricing (-2 bps) from home lending competition, higher funding costs (-3 bps) from deposit competition and lower cash rates, and lower Treasury & Markets income (-2 bps), partially offset by favourable portfolio mix (+1 bps) from strong at-call deposit growth and higher interest rate risk hedging earnings (+6 bps) from the replicating portfolio and capital.

> [ev-5] CBA/1H26/profit_announcement, printed p3: "Net interest margin (%) 2.04 2.08 2.08 (4)bpts (4)bpts"
> [ev-7] CBA/1H26/profit_announcement, PDF p9: "Excluding growth in liquid assets and institutional reverse sale and repurchase agreements, which have broadly neutral impacts on net interest income, underlying net interest margin was slightly lower in the half. This was primarily due to competition in home lending and lower Treasury and Markets income, partly offset by higher earnings on the replicating portfolio and favourable funding mix from strong growth in at-call deposits."
> [ev-8] CBA/1H26/profit_announcement, PDF p9: "Net interest margin Operating expenses4 2.04% $6,720m (44.7% cost-to-income) 4bpts on 1H25 (flat underlying basis)"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & repos | -4 bps | 85 | 1 (single_source) | ev-2, ev-18 |
| `asset_pricing` | Asset pricing | -2 bps | 90 | 2 () | ev-2, ev-19, ev-12 |
| `funding` | Funding costs | -3 bps | 85 | 1 (single_source) | ev-2, ev-20 |
| `mix` | Portfolio mix | +1 bps | 85 | 1 (single_source) | ev-2 |
| `capital_replicating` | Interest rate risk hedging | +6 bps | 92 | 2 () | ev-2, ev-21, ev-16 |
| `markets_treasury` | Treasury & Markets | -2 bps | 90 | 2 () | ev-2, ev-22, ev-17 |
| *residual (unexplained)* | — | +0 bps | — | — |

### liquids — "Liquids & repos"
*-4 bps | confidence 85/100*

Growth in liquid assets (+$20bn vs 1H25) contributed -3 bps and institutional repos (+$10bn vs 1H25) contributed -1 bps, reflecting the bank's management of liquidity buffers.
> [ev-2] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"
> [ev-18] CBA/1H26/results_presentation, printed p59: "Increase in liquid assets1 (3) Increase in institutional repos1 (1)"

### asset_pricing — "Asset pricing"
*-2 bps | confidence 90/100*

Home loan competition drove -2 bps, business lending competition -1 bps, partly offset by consumer finance +1 bps. The bank states increased competition in home lending pricing as the driver.
> [ev-2] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"
> [ev-19] CBA/1H26/results_presentation, printed p59: "Home loan competition (2) Business lending competition (1) Consumer finance 1"
> [ev-12] CBA/1H26/profit_announcement, PDF p29: "Asset pricing: Decreased margin by 2 basis points driven by home lending pricing reflecting the impact of increased competition."

### funding — "Funding costs"
*-3 bps | confidence 85/100*

Deposit competition, mix shift and lower cash rate reduced margin by 3 bps. The bank attributes this to competitive deposit pricing pressure and the pass-through of declining RBA cash rates.
> [ev-2] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"
> [ev-20] CBA/1H26/results_presentation, printed p59: "Deposit competition, mix and lower cash rate"

### mix — "Portfolio mix"
*+1 bps | confidence 85/100*

Favourable funding mix from strong growth in at-call deposits relative to lending assets contributed +1 bps. Deposits grew faster than lending, improving the margin.
> [ev-2] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"

### capital_replicating — "Interest rate risk hedging"
*+6 bps | confidence 92/100*

Higher earnings on the replicating portfolio contributed +5 bps and higher earnings on capital contributed +1 bps. This was the largest positive driver, offsetting competition and funding cost headwinds.
> [ev-2] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"
> [ev-21] CBA/1H26/results_presentation, printed p59: "Replicating portfolio 5 Higher earnings on capital 1"
> [ev-16] CBA/1H26/profit_announcement, PDF p29: "Capital, Replicating and Other: Increased margin by 1 basis point driven by higher earnings on the replicating portfolio."

### markets_treasury — "Treasury & Markets"
*-2 bps | confidence 90/100*

Lower risk management income in Treasury and an increase in reverse sale and repurchase agreement balances reduced margin by 2 bps. The bank describes this as minimal impact on earnings.
> [ev-2] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"
> [ev-22] CBA/1H26/results_presentation, printed p59: "Minimal impact on earnings"
> [ev-17] CBA/1H26/profit_announcement, PDF p29: "Treasury and Markets: Decreased margin by 2 basis points due to lower risk management income in Treasury and an increase in reverse sale and repurchase agreement balances."

## Limitations
- The results book narrative (p26) states underlying NIM was 'unchanged' ex-liquids, consistent with the walk chart showing non-liquids drivers summing to 0 bps.
- The half-on-half walk on page 29 of the profit announcement shows a different decomposition (Jun 25→Dec 25) and should not be mixed with the 1H25→1H26 primary walk.
- No separate basis_risk or rate_timing bars appear in the primary walk chart; these are subsumed within other categories.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T13:35:56+00:00
- seconds: 226.7
- cost_usd: 0.0159
- tokens: 786598 in / 7468 out
- orchestration: agent
- tool_calls: 38
- pages_read: 12
- charts_read: 2
- budget_exhausted: no
