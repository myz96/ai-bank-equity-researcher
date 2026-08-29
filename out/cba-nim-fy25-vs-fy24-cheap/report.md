# CBA — nim — FY25 vs FY24

**Movement (cash basis):** 199bps → 208bps (+9bps) | **Attribution confidence:** 95/100

*Read from: row 'Net interest margin (%)', column FY24 -> column FY25*

CBA's Group NIM increased 9 bps to 208 bps in FY25 (vs 199 bps in FY24). The primary driver was Capital & Replicating (+9 bps), offset by Funding costs (-7 bps) and Basis risk (-1 bps). Liquids & Pooled Facilities contributed +7 bps, while Asset pricing and Portfolio mix were flat. Excluding the 7 bps liquidity benefit, underlying NIM improved only 2 bps.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & Pooled Facilities | +7 bps | 85 | 1 (single_source) | ev-1, ev-26, ev-29 |
| `asset_pricing` | Asset pricing | +0 bps | 85 | 1 (single_source) | ev-1, ev-27 |
| `funding` | Funding costs | -7 bps | 85 | 1 (single_source) | ev-1, ev-28 |
| `mix` | Portfolio mix | +0 bps | 85 | 1 (single_source) | ev-1, ev-33 |
| `basis_risk` | Basis risk | -1 bps | 85 | 1 (single_source) | ev-1, ev-30 |
| `capital_replicating` | Capital, Replicating and Other | +9 bps | 85 | 1 (single_source) | ev-1, ev-31 |
| `markets_treasury` | Treasury and Markets | +1 bps | 85 | 1 (single_source) | ev-1, ev-32 |

### liquids — "Liquids & Pooled Facilities"
*+7 bps | confidence 85/100*

A reduction in lower yielding liquid assets (+5 bps) and institutional pooled lending facilities (+2 bps) drove this increase. These items have a broadly neutral impact on net interest income but improve the margin ratio.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-26] CBA/FY25/profit_announcement, printed p12: "Excluding a 7 basis point increase in margin from a reduction in lower yielding liquid assets and institutional pooled facilities, which have a broadly neutral impact on net interest income, net interest margin increased 2 basis points."
> [ev-29] CBA/FY25/profit_announcement, printed p12: "Reduction in lower yielding liquid assets and institutional pooled lending facilities drove a 5 basis point and 2 basis point increase in margin respectively."

### asset_pricing — "Asset pricing"
*+0 bps | confidence 85/100*

The bank reported asset pricing as 'Flat' for the period, with no net contribution to the margin movement.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-27] CBA/FY25/profit_announcement, printed p12: "Asset pricing: Flat."

### funding — "Funding costs"
*-7 bps | confidence 85/100*

Decreased margin by 7 bps driven by increased deposit price competition.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-28] CBA/FY25/profit_announcement, printed p12: "Funding costs: Decreased margin by 7 basis points driven by increased deposit price competition."

### mix — "Portfolio mix"
*+0 bps | confidence 85/100*

The bank reported portfolio mix as 'Flat' for the period, with no net contribution to the margin movement.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-33] CBA/FY25/profit_announcement, PDF p29: "Portfolio mix: Flat."

### basis_risk — "Basis risk"
*-1 bps | confidence 85/100*

Margin decreased by 1 bps reflecting an increase in the average spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-30] CBA/FY25/profit_announcement, PDF p29: "The Bank’s margin decreased 1 basis point reflecting an increase in the average spread."

### capital_replicating — "Capital, Replicating and Other"
*+9 bps | confidence 85/100*

Increased margin by 9 bps driven by the net impact of the replicating portfolio due to changes in portfolio rate and volume (+5 bps) and higher earnings on capital hedges (+4 bps).
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-31] CBA/FY25/profit_announcement, PDF p29: "Increased margin by 9 basis points driven by the net impact of the replicating portfolio due to changes in portfolio rate and volume (up 5 basis points) and higher earnings on capital hedges (up 4 basis points)."

### markets_treasury — "Treasury and Markets"
*+1 bps | confidence 85/100*

Increased margin by 1 bps.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-32] CBA/FY25/profit_announcement, PDF p29: "Treasury and Markets: Increased margin by 1 basis point."

## Source disagreements
- **NIM Movement Magnitude** (definitional): 9 bps (ev-5, ev-7, ev-24) vs -3 bps (ev-14)
  Preferred: 9 bps. ev-14 reports a -3 bps change based on Cash NIM (2.50% in FY25 vs 2.53% in FY24 per ev-8). However, the task requires the Group headline measure, which is the Primary basis (2.08% in FY25 vs 1.99% in FY24 per ev-7/ev-24), resulting in a +9 bps movement. The cash basis is a segmental or alternative reporting line, not the Group headline.

## Limitations
- The analysis uses the Group Net Interest Margin on the primary (non-statutory) basis, consistent with the bank's KPI table.
- Cash basis NIM movements are excluded from the primary attribution as they represent a different reporting basis.
- Half-on-half movements (Dec 2024 to Jun 2025) are excluded from the driver attribution as they do not match the FY24-FY25 comparison span.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY25/profit_announcement (e2e911ab4fed), CBA/FY24/profit_announcement (1ab9332c8371), CBA/FY24/results_presentation (168e3835d44c)
- generated: 2026-08-29T20:50:31+00:00
- seconds: 93.4
- cost_usd: 0.003
- tokens: 67254 in / 7634 out
- orchestration: pipeline
- pages_extracted: 20
- reference_follow: ['CBA/FY24/profit_announcement p36 <- p29 page 20 [added]', 'CBA/FY25/profit_announcement p36 <- p29 page 20 [added]']
