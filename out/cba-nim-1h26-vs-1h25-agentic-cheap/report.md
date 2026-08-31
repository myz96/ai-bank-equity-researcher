# CBA — nim — 1H26 vs 1H25

**Movement (cash basis):** 208bps → 204bps (-4bps) | **Attribution confidence:** 85/100

*Read from: row 'Net interest margin (%)', column 31 Dec 24 -> column 31 Dec 25*

CBA's net interest margin decreased 4 basis points to 2.04% in 1H26 from 2.08% in 1H25. The decline was driven by growth in liquid assets and institutional repos (-4 bps), asset pricing pressure from home loan and business lending competition (-2 bps), and higher funding costs (-3 bps), partially offset by a favourable portfolio mix from strong at-call deposit growth (+1 bps), higher earnings from the replicating portfolio and equity hedges (+6 bps), and lower Treasury & Markets income (-2 bps). Excluding liquid assets and institutional reverse sale/repurchase agreements, underlying NIM was flat.

> [ev-13] CBA/1H26/profit_announcement, printed p3: "Net interest margin (%) 2.04 2.08 2.08 (4)bpts (4)bpts"
> [ev-2] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"
> [ev-11] CBA/1H26/profit_announcement, printed p2: "Net Interest Income (NII) increased 6%, primarily driven by a $96 billion or 8% increase in Average Interest Earning Assets (AIEA), partly offset by a 4 basis point decrease in Net Interest Margin (NIM). Excluding the impact of liquid assets and institutional reverse sale and repurchase agreements, the underlying NIM was unchanged."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & repos | -4 bps | 85 | 1 (single_source) | ev-2 |
| `asset_pricing` | Asset pricing | -2 bps | 85 | 1 (single_source) | ev-2 |
| `funding` | Funding costs | -3 bps | 85 | 1 (single_source) | ev-2 |
| `mix` | Portfolio mix | +1 bps | 85 | 1 (single_source) | ev-2 |
| `capital_replicating` | Interest rate risk hedging | +6 bps | 85 | 1 (single_source) | ev-2 |
| `markets_treasury` | Treasury & Markets | -2 bps | 85 | 1 (single_source) | ev-2 |

### liquids — "Liquids & repos"
*-4 bps | confidence 85/100*

Growth in liquid assets (-3 bps) and institutional repos (-1 bps) dragged on margin, with a $20 billion increase in average liquid assets and a $10 billion increase in average institutional repos in 1H26 versus 1H25.
> [ev-2] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"

### asset_pricing — "Asset pricing"
*-2 bps | confidence 85/100*

Home loan pricing pressure (-2 bps) from increased competition, partially offset by business lending competition (-1 bps) and consumer finance (+1 bps).
> [ev-2] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"

### funding — "Funding costs"
*-3 bps | confidence 85/100*

Deposit competition, mix and lower cash rate contributed to higher funding costs, reducing margin by 3 basis points year-on-year.
> [ev-2] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"

### mix — "Portfolio mix"
*+1 bps | confidence 85/100*

Favourable funding mix from strong growth in at-call deposits increased margin by 1 basis point.
> [ev-2] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"

### capital_replicating — "Interest rate risk hedging"
*+6 bps | confidence 85/100*

Higher earnings from the replicating portfolio (+5 bps) and higher earnings on capital (+1 bps) drove a 6 basis point improvement in margin.
> [ev-2] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"

### markets_treasury — "Treasury & Markets"
*-2 bps | confidence 85/100*

Lower risk management income in Treasury and an increase in reverse sale and repurchase agreement balances reduced margin by 2 basis points.
> [ev-2] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"

## Limitations
- The profit announcement provides a sequential-half NIM walk (Jun 25 to Dec 25) with different driver values; the 12-month walk comes only from the results presentation slide deck, not the results book.
- The bank states that underlying NIM (excluding liquids and institutional reverse sale/repurchase agreements) was unchanged, which qualifies the headline -4 bpt movement.
- Funding costs sub-components (deposit pricing vs wholesale) are not separately quantified in the 12-month walk.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T23:49:27+00:00
- seconds: 163.1
- cost_usd: 0.0102
- tokens: 507975 in / 7226 out
- orchestration: agent
- tool_calls: 27
- pages_read: 10
- charts_read: 3
- budget_exhausted: no
