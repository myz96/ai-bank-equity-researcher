# CBA — nim — FY25 vs FY24

**Movement (cash basis):** 199bps → 208bps (+9bps) | **Attribution confidence:** 95/100

*Read from: row 'Net interest margin (%)', column FY24 -> column FY25*

CBA's Group net interest margin increased 9 basis points to 208 bps in FY25 (from 199 bps in FY24). The improvement was primarily driven by a 7 bps benefit from reduced liquid assets and pooled facilities, and a 9 bps positive contribution from capital and replicating portfolio earnings. These were partially offset by a 7 bps headwind from higher funding costs due to deposit price competition and a 1 bps negative impact from basis risk. Asset pricing and portfolio mix were flat.

> [ev-30] CBA/FY25/profit_announcement, PDF p9: "Net interest margin 2.08% 9bpts on FY24 (+2bpts underlying basis)"
> [ev-32] CBA/FY25/profit_announcement, PDF p100: "Net interest margin 2.08 1.99 2.08 2.08"
> [ev-49] CBA/FY25/profit_announcement, printed p12: "Net interest margin (%) 2.08 1.99 9bpts"
> [ev-50] CBA/FY25/profit_announcement, printed p12: "The Bank’s net interest margin increased 9 basis points on the prior year to 2.08%."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & Pooled Facilities | +7 bps | 85 | 1 (single_source) | ev-1, ev-51, ev-52 |
| `asset_pricing` | Asset pricing | +0 bps | 85 | 1 (single_source) | ev-1, ev-53 |
| `funding` | Funding costs | -7 bps | 85 | 1 (single_source) | ev-1, ev-54 |
| `mix` | Portfolio mix | +0 bps | 85 | 1 (single_source) | ev-1, ev-58 |
| `basis_risk` | Basis risk | -1 bps | 85 | 1 (single_source) | ev-1, ev-55 |
| `capital_replicating` | Capital, Replicating and Other | +9 bps | 85 | 1 (single_source) | ev-1, ev-56 |
| `markets_treasury` | Treasury and Markets | +1 bps | 85 | 1 (single_source) | ev-1, ev-57 |

### liquids — "Liquids & Pooled Facilities"
*+7 bps | confidence 85/100*

A reduction in lower yielding liquid assets contributed +5 bps, while a decrease in institutional pooled lending facilities added +2 bps to the margin (ev-52).
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-51] CBA/FY25/profit_announcement, printed p12: "Excluding a 7 basis point increase in margin from a reduction in lower yielding liquid assets and institutional pooled facilities, which have a broadly neutral impact on net interest income, net interest margin increased 2 basis points."
> [ev-52] CBA/FY25/profit_announcement, printed p12: "Reduction in lower yielding liquid assets and institutional pooled lending facilities drove a 5 basis point and 2 basis point increase in margin respectively."

### asset_pricing — "Asset pricing"
*+0 bps | confidence 85/100*

The bank reported asset pricing as flat for the period (ev-53).
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-53] CBA/FY25/profit_announcement, printed p12: "Asset pricing: Flat."

### funding — "Funding costs"
*-7 bps | confidence 85/100*

Margin decreased by 7 bps driven by increased deposit price competition (ev-54).
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-54] CBA/FY25/profit_announcement, printed p12: "Funding costs: Decreased margin by 7 basis points driven by increased deposit price competition."

### mix — "Portfolio mix"
*+0 bps | confidence 85/100*

The bank reported portfolio mix as flat for the period (ev-58).
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-58] CBA/FY25/profit_announcement, PDF p29: "Portfolio mix: Flat."

### basis_risk — "Basis risk"
*-1 bps | confidence 85/100*

Margin decreased by 1 bps reflecting an increase in the average spread between the 3-month bank bill swap rate and the 3-month overnight index swap rate (ev-55).
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-55] CBA/FY25/profit_announcement, PDF p29: "The Bank’s margin decreased 1 basis point reflecting an increase in the average spread."

### capital_replicating — "Capital, Replicating and Other"
*+9 bps | confidence 85/100*

Increased margin by 9 bps driven by the net impact of the replicating portfolio due to changes in portfolio rate and volume (+5 bps) and higher earnings on capital hedges (+4 bps) (ev-56).
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-56] CBA/FY25/profit_announcement, PDF p29: "Increased margin by 9 basis points driven by the net impact of the replicating portfolio due to changes in portfolio rate and volume (up 5 basis points) and higher earnings on capital hedges (up 4 basis points)."

### markets_treasury — "Treasury and Markets"
*+1 bps | confidence 85/100*

Increased margin by 1 bps (ev-57).
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-57] CBA/FY25/profit_announcement, PDF p29: "Treasury and Markets: Increased margin by 1 basis point."

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY25/profit_announcement (e2e911ab4fed), CBA/FY24/profit_announcement (1ab9332c8371), CBA/FY24/results_presentation (168e3835d44c)
- generated: 2026-08-30T14:48:57+00:00
- seconds: 155.4
- cost_usd: 0.0035
- tokens: 80498 in / 8412 out
- orchestration: pipeline
- pages_extracted: 20
- reference_follow: ['CBA/FY24/profit_announcement p36 <- p29 page 20 [added]', 'CBA/FY25/profit_announcement p36 <- p29 page 20 [added]']
