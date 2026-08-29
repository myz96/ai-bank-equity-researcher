# CBA — nim — 1H26 vs 1H25

**Movement (cash basis):** 208bps → 204bps (-4bps) | **Attribution confidence:** 90/100

*Read from: row 'Net interest margin (%)', column 31 Dec 24 -> column 31 Dec 25*

CBA's Group net interest margin (cash basis) decreased 4 bps to 204 bps in 1H26 from 208 bps in 1H25. The decline was driven by lower asset pricing (-2 bps), higher funding costs (-3 bps), and negative treasury/markets contribution (-3 bps). These were partially offset by strong capital/replicating earnings (+6 bps) and favorable portfolio mix (+1 bps). Liquids drag was -3 bps.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids | -3 bps | 90 | 1 (corroborated_2_sources) | ev-1 |
| `asset_pricing` | Asset pricing | -2 bps | 90 | 1 (corroborated_2_sources) | ev-1 |
| `funding` | Funding costs | -3 bps | 90 | 1 (corroborated_2_sources) | ev-1 |
| `mix` | Portfolio mix | +1 bps | 90 | 1 (corroborated_2_sources) | ev-1 |
| `basis_risk` | Basis risk | +0 bps | 85 | 1 (single_source) | ev-1 |
| `capital_replicating` | Capital, Replicating & Other | +6 bps | 90 | 1 (corroborated_2_sources) | ev-1 |
| `markets_treasury` | Treasury & Markets | -3 bps | 90 | 1 (corroborated_2_sources) | ev-1 |

### liquids — "Liquids"
*-3 bps | confidence 90/100*

Negative impact from growth in liquid assets and institutional reverse sale and repurchase agreements.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"

### asset_pricing — "Asset pricing"
*-2 bps | confidence 90/100*

Lower home lending margins principally reflecting elevated competition.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"

### funding — "Funding costs"
*-3 bps | confidence 90/100*

Lower deposit margins mainly due to competition, mix shift to higher yielding savings deposits and the impact of declining interest rates.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"

### mix — "Portfolio mix"
*+1 bps | confidence 90/100*

Favourable portfolio mix primarily due to the benefit of strong growth in average deposits relative to assets.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"

### basis_risk — "Basis risk"
*+0 bps | confidence 85/100*

Flat contribution from basis risk (bills/OIS spread).
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"

### capital_replicating — "Capital, Replicating & Other"
*+6 bps | confidence 90/100*

Higher earnings on the replicating portfolio and equity hedge.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"

### markets_treasury — "Treasury & Markets"
*-3 bps | confidence 90/100*

Lower risk management income in Treasury and an increase in reverse sale and repurchase agreement balances.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"

## Source disagreements
- **Liquids Labeling** (definitional): -3 bps — CBA/1H26/profit_announcement PDF p28 (ev-1) vs -4 bps — CBA/1H26/results_presentation PDF p59 (ev-4)
  Preferred: -3 bps. The Profit Announcement (primary source) labels the bar 'Liquids' at -3 bps. The Results Presentation (slide) labels it 'Liquids & repos' at -4 bps. Per source hierarchy, the PA framing is primary.
- **Treasury & Markets Value** (definitional): -3 bps — CBA/1H26/profit_announcement PDF p28 (ev-1) vs -2 bps — CBA/1H26/results_presentation PDF p59 (ev-4)
  Preferred: -3 bps. The Profit Announcement (primary source) reports -3 bps for Treasury & Markets. The Results Presentation (slide) reports -2 bps. Per source hierarchy, the PA framing is primary.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T13:04:07+00:00
- seconds: 220.8
- cost_usd: 0.0025
- tokens: 52954 in / 7289 out
- orchestration: pipeline
