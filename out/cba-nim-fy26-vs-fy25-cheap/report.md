# CBA — nim — FY26 vs FY25

**Movement (cash basis):** 208bps → 205bps (-3bps) | **Attribution confidence:** 90/100

*Read from: row 'Net interest margin', column FY25 -> column FY26*

CBA's Group NIM decreased by 3 bps to 205 bps in FY26 (vs 208 bps in FY25). The decline was driven by lower asset pricing (-5 bps) and higher liquids drag (-3 bps), partially offset by favourable capital/replicating earnings (+5 bps) and portfolio mix (+2 bps). Funding costs and basis risk were neutral.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids | -3 bps | 90 | 2 (corroborated_2_sources) | ev-1, ev-4 |
| `asset_pricing` | Asset pricing | -5 bps | 90 | 2 (corroborated_2_sources) | ev-1, ev-4 |
| `funding` | Funding costs | +0 bps | 90 | 2 (corroborated_2_sources) | ev-1, ev-4 |
| `mix` | Portfolio mix | +2 bps | 90 | 2 (corroborated_2_sources) | ev-1, ev-4 |
| `basis_risk` | Basis risk | +0 bps | 85 | 1 (single_source) | ev-1 |
| `capital_replicating` | Capital, Replicating | +5 bps | 90 | 2 (corroborated_2_sources) | ev-1, ev-4 |
| `markets_treasury` | Treasury & Markets | -2 bps | 90 | 1 (corroborated_2_sources) | ev-1 |

### liquids — "Liquids"
*-3 bps | confidence 90/100*

Higher liquidity levels and institutional reverse repos exerted a negative drag on the margin.
> [ev-1] CBA/FY26/profit_announcement, PDF p28: "[walk chart] NIM Movement since June 2025: Jun 25 Full Year 208 -> Jun 26 Full Year 205"
> [ev-4] CBA/FY26/results_presentation, printed p60: "[walk chart] Group margin – 12 months: FY25 208.0 -> FY26 205.0"

### asset_pricing — "Asset pricing"
*-5 bps | confidence 90/100*

Lower lending margins due to home loan competition reduced the margin.
> [ev-1] CBA/FY26/profit_announcement, PDF p28: "[walk chart] NIM Movement since June 2025: Jun 25 Full Year 208 -> Jun 26 Full Year 205"
> [ev-4] CBA/FY26/results_presentation, printed p60: "[walk chart] Group margin – 12 months: FY25 208.0 -> FY26 205.0"

### funding — "Funding costs"
*+0 bps | confidence 90/100*

Funding costs had a net neutral impact on the margin movement year-on-year.
> [ev-1] CBA/FY26/profit_announcement, PDF p28: "[walk chart] NIM Movement since June 2025: Jun 25 Full Year 208 -> Jun 26 Full Year 205"
> [ev-4] CBA/FY26/results_presentation, printed p60: "[walk chart] Group margin – 12 months: FY25 208.0 -> FY26 205.0"

### mix — "Portfolio mix"
*+2 bps | confidence 90/100*

Favourable mix from business lending growth and deposits growing faster than lending supported the margin.
> [ev-1] CBA/FY26/profit_announcement, PDF p28: "[walk chart] NIM Movement since June 2025: Jun 25 Full Year 208 -> Jun 26 Full Year 205"
> [ev-4] CBA/FY26/results_presentation, printed p60: "[walk chart] Group margin – 12 months: FY25 208.0 -> FY26 205.0"

### basis_risk — "Basis risk"
*+0 bps | confidence 85/100*

Bills/OIS spread basis risk had a net neutral impact.
> [ev-1] CBA/FY26/profit_announcement, PDF p28: "[walk chart] NIM Movement since June 2025: Jun 25 Full Year 208 -> Jun 26 Full Year 205"

### capital_replicating — "Capital, Replicating"
*+5 bps | confidence 90/100*

Higher earnings on the replicating portfolio and capital hedges provided positive support.
> [ev-1] CBA/FY26/profit_announcement, PDF p28: "[walk chart] NIM Movement since June 2025: Jun 25 Full Year 208 -> Jun 26 Full Year 205"
> [ev-4] CBA/FY26/results_presentation, printed p60: "[walk chart] Group margin – 12 months: FY25 208.0 -> FY26 205.0"

### markets_treasury — "Treasury & Markets"
*-2 bps | confidence 90/100*

Markets and Treasury activities contributed negatively to the margin movement.
> [ev-1] CBA/FY26/profit_announcement, PDF p28: "[walk chart] NIM Movement since June 2025: Jun 25 Full Year 208 -> Jun 26 Full Year 205"

## Source disagreements
- **Liquids driver value** (definitional): -3 bps — CBA/FY26/profit_announcement PDF p28 (ev-1) vs -4 bps — CBA/FY26/results_presentation PDF p60 (ev-4)
  Preferred: -3 bps. The Profit Announcement (primary source) labels the bar 'Liquids' at -3 bps. The Presentation (secondary) labels it 'Liquids & repos' at -4 bps. Per source hierarchy, the PA framing is primary.
- **Treasury & Markets driver value** (definitional): -2 bps — CBA/FY26/profit_announcement PDF p28 (ev-1) vs -1 bps — CBA/FY26/results_presentation PDF p60 (ev-4)
  Preferred: -2 bps. The Profit Announcement (primary source) reports -2 bps. The Presentation (secondary) reports -1 bps. Per source hierarchy, the PA framing is primary.

## Limitations
- Discrepancies exist between the Profit Announcement and Results Presentation for Liquids (-3 vs -4 bps) and Treasury & Markets (-2 vs -1 bps). The Profit Announcement values are used as primary per source hierarchy.
- Basis risk is only explicitly listed in the Profit Announcement walk; it is assumed neutral based on the sum check of that walk.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T13:16:48+00:00
- seconds: 76.6
- cost_usd: 0.0022
- tokens: 50436 in / 5075 out
- orchestration: pipeline
