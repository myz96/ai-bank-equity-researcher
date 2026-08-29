# CBA — nim — 1H26 vs 1H25

**Movement (cash basis):** 208bps → 204bps (-4bps) | **Attribution confidence:** 95/100

*Read from: row 'Net interest margin (%)', column 31 Dec 24 -> column 31 Dec 25*

CBA's Group net interest margin (cash basis) decreased by 4 bps to 204 bps in 1H26 from 208 bps in 1H25. The decline was driven by lower asset pricing (-2 bps), higher funding costs (-3 bps), and a negative Treasury & Markets contribution (-3 bps). These were partially offset by strong capital/replicating portfolio earnings (+6 bps) and favourable portfolio mix (+1 bps). Liquids contributed -3 bps, while basis risk was flat.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids | -3 bps | 95 | 1 (corroborated_2_sources) | ev-1, ev-22 |
| `asset_pricing` | Asset pricing | -2 bps | 95 | 1 (corroborated_2_sources) | ev-1, ev-23 |
| `funding` | Funding costs | -3 bps | 95 | 1 (corroborated_2_sources) | ev-1, ev-24 |
| `mix` | Portfolio mix | +1 bps | 95 | 1 (corroborated_2_sources) | ev-1, ev-25 |
| `basis_risk` | Basis risk | +0 bps | 85 | 1 (single_source) | ev-1, ev-26 |
| `capital_replicating` | Capital, Replicating and Other | +6 bps | 95 | 1 (corroborated_2_sources) | ev-1, ev-27 |
| `markets_treasury` | Treasury & Markets | -3 bps | 95 | 1 (corroborated_2_sources) | ev-1, ev-35 |

### liquids — "Liquids"
*-3 bps | confidence 95/100*

Decreased margin by 3 bps due to growth in liquid assets and institutional reverse sale and repurchase agreements. The bank notes these have broadly neutral impacts on net interest income but drag on the margin ratio.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"
> [ev-22] CBA/1H26/profit_announcement, printed p12: "Excluding growth in liquid assets, which have broadly neutral impacts on net interest income, net interest margin decreased by 1 basis point."

### asset_pricing — "Asset pricing"
*-2 bps | confidence 95/100*

Decreased margin by 2 bps driven by home lending pricing (down 2 bps) and business lending pricing (down 1 bps) reflecting elevated competition, partly offset by higher consumer finance margins (up 1 bps).
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"
> [ev-23] CBA/1H26/profit_announcement, printed p12: "Asset pricing: Decreased margin by 2 basis points driven by home lending pricing (down 2 basis points) and business lending pricing (down 1 basis point) reflecting the impact of elevated competition, partly offset by higher consumer finance margins (up 1 basis point)."

### funding — "Funding costs"
*-3 bps | confidence 95/100*

Decreased margin by 3 bps driven by declining interest rates, unfavourable deposit mix, and increased deposit price competition.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"
> [ev-24] CBA/1H26/profit_announcement, printed p12: "Funding costs: Decreased margin by 3 basis points driven by declining interest rates, unfavourable deposit mix and increased deposit price competition."

### mix — "Portfolio mix"
*+1 bps | confidence 95/100*

Increased margin by 1 bps driven by favourable funding mix from strong growth in at-call deposits relative to assets.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"
> [ev-25] CBA/1H26/profit_announcement, printed p12: "Portfolio mix: Increased margin by 1 basis point driven by favourable funding mix from strong growth in at-call deposits."

### basis_risk — "Basis risk"
*+0 bps | confidence 85/100*

Flat. No material impact on net interest margin compared to the prior comparative period.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"
> [ev-26] CBA/1H26/profit_announcement, printed p12: "Basis risk: Flat."

### capital_replicating — "Capital, Replicating and Other"
*+6 bps | confidence 95/100*

Increased margin by 6 bps driven by the impact of the replicating portfolio due to changes in portfolio rate and volume (up 5 bps) and higher earnings on capital hedges (up 1 bps).
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"
> [ev-27] CBA/1H26/profit_announcement, printed p12: "Capital, Replicating and Other: Increased margin by 6 basis points driven by the impact of the replicating portfolio due to changes in portfolio rate and volume (up 5 basis points) and higher earnings on capital hedges (up 1 basis point)."

### markets_treasury — "Treasury & Markets"
*-3 bps | confidence 95/100*

Decreased margin by 3 bps. This reflects lower risk management income in Treasury and an increase in reverse sale and repurchase agreement balances.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"
> [ev-35] CBA/1H26/profit_announcement, PDF p29: "Treasury and Markets: Decreased margin by 2 basis points due to lower risk management income in Treasury and an increase in reverse sale and repurchase agreement balances."

## Source disagreements
- **Treasury & Markets Contribution Value** (definitional): -3 bps — CBA/1H26/profit_announcement PDF p28 (ev-1) vs -2 bps — CBA/1H26/results_presentation PDF p59 (ev-4)
  Preferred: -3 bps. The Profit Announcement (primary source per hierarchy) states a -3 bps impact. The Results Presentation slide shows -2 bps. We adopt the primary source value.

## Limitations
- The Treasury & Markets driver value differs between the Profit Announcement (-3 bps) and the Results Presentation (-2 bps). The Profit Announcement is preferred as the primary source.
- The 'Liquids' driver includes both liquid assets and institutional repos. The narrative combines these into a single bar as presented in the primary walk.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T17:43:10+00:00
- seconds: 237.9
- cost_usd: 0.0027
- tokens: 56238 in / 7497 out
- orchestration: pipeline
- pages_extracted: 19
- reference_follow: ['CBA/1H26/profit_announcement p36 <- p29 page 20 [added]']
