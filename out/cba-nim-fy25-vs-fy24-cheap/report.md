# CBA — nim — FY25 vs FY24

**Movement (cash basis):** 199bps → 208bps (+9bps) | **Attribution confidence:** 95/100

*Read from: row 'Net interest margin (%)', column FY24 -> column FY25*

CBA's Group net interest margin increased 9 basis points to 208 bps in FY25 (from 199 bps in FY24). On an underlying basis excluding a 7 bps benefit from reduced liquid assets and pooled facilities, the margin improved by 2 bps. The primary drivers of the total movement were higher earnings on capital and replicating portfolios (+9 bps) and lower funding costs (-7 bps), partially offset by adverse basis risk (-1 bps). Asset pricing and portfolio mix were flat.

> [ev-24] CBA/FY25/profit_announcement, PDF p9: "Net interest margin 2.08% 9bpts on FY24 (+2bpts underlying basis)"
> [ev-26] CBA/FY25/profit_announcement, PDF p100: "Net interest margin 2.08 1.99 2.08 2.08"
> [ev-43] CBA/FY25/profit_announcement, printed p12: "Net interest margin (%) 2.08 1.99 9bpts"
> [ev-44] CBA/FY25/profit_announcement, printed p12: "The Bank’s net interest margin increased 9 basis points on the prior year to 2.08%."
> [ev-45] CBA/FY25/profit_announcement, printed p12: "Excluding a 7 basis point increase in margin from a reduction in lower yielding liquid assets and institutional pooled facilities, which have a broadly neutral impact on net interest income, net interest margin increased 2 basis points."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & Pooled Facilities | +7 bps | 85 | 1 (single_source) | ev-1, ev-45, ev-48 |
| `asset_pricing` | Asset pricing | +0 bps | 85 | 1 (single_source) | ev-1, ev-46 |
| `funding` | Funding costs | -7 bps | 85 | 1 (single_source) | ev-1, ev-47 |
| `mix` | Portfolio mix | +0 bps | 85 | 1 (single_source) | ev-1, ev-46 |
| `basis_risk` | Basis risk | -1 bps | 85 | 1 (single_source) | ev-1, ev-49 |
| `capital_replicating` | Capital, Replicating and Other | +9 bps | 85 | 1 (single_source) | ev-1, ev-50 |
| `markets_treasury` | Treasury and Markets | +1 bps | 85 | 1 (single_source) | ev-1, ev-51 |

### liquids — "Liquids & Pooled Facilities"
*+7 bps | confidence 85/100*

A reduction in lower yielding liquid assets drove a 5 bps increase, while institutional pooled lending facilities contributed 2 bps. These items have a broadly neutral impact on net interest income.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-45] CBA/FY25/profit_announcement, printed p12: "Excluding a 7 basis point increase in margin from a reduction in lower yielding liquid assets and institutional pooled facilities, which have a broadly neutral impact on net interest income, net interest margin increased 2 basis points."
> [ev-48] CBA/FY25/profit_announcement, printed p12: "Reduction in lower yielding liquid assets and institutional pooled lending facilities drove a 5 basis point and 2 basis point increase in margin respectively."

### asset_pricing — "Asset pricing"
*+0 bps | confidence 85/100*

The bank reported asset pricing as flat for the period.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-46] CBA/FY25/profit_announcement, printed p12: "Asset pricing: Flat."

### funding — "Funding costs"
*-7 bps | confidence 85/100*

Decreased margin by 7 bps driven by increased deposit price competition.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-47] CBA/FY25/profit_announcement, printed p12: "Funding costs: Decreased margin by 7 basis points driven by increased deposit price competition."

### mix — "Portfolio mix"
*+0 bps | confidence 85/100*

The bank reported portfolio mix as flat for the period.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-46] CBA/FY25/profit_announcement, printed p12: "Asset pricing: Flat."

### basis_risk — "Basis risk"
*-1 bps | confidence 85/100*

Decreased margin by 1 bps reflecting an increase in the average spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-49] CBA/FY25/profit_announcement, PDF p29: "The Bank’s margin decreased 1 basis point reflecting an increase in the average spread."

### capital_replicating — "Capital, Replicating and Other"
*+9 bps | confidence 85/100*

Increased margin by 9 bps driven by the net impact of the replicating portfolio due to changes in portfolio rate and volume (up 5 bps) and higher earnings on capital hedges (up 4 bps).
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-50] CBA/FY25/profit_announcement, PDF p29: "Increased margin by 9 basis points driven by the net impact of the replicating portfolio due to changes in portfolio rate and volume (up 5 basis points) and higher earnings on capital hedges (up 4 basis points)."

### markets_treasury — "Treasury and Markets"
*+1 bps | confidence 85/100*

Increased margin by 1 bps.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-51] CBA/FY25/profit_announcement, PDF p29: "Treasury and Markets: Increased margin by 1 basis point."

## Source disagreements
- **NIM Movement Basis** (definitional): 9 bps increase (Primary cash basis, ev-44) vs -3 bps decrease (Cash basis segment table, ev-33)
  Preferred: 9 bps increase. The profit announcement narrative (ev-44) states a 9 bps increase on a primary cash basis. However, the text on page 64 (ev-33) describes a 3 bps decrease alongside NII growth figures that align with the statutory or different reporting scope. The walk chart (ev-1) confirms the 9 bps movement for the Group margin used in the headline.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY25/profit_announcement (e2e911ab4fed), CBA/FY24/profit_announcement (1ab9332c8371), CBA/FY24/results_presentation (168e3835d44c)
- generated: 2026-08-30T16:20:58+00:00
- seconds: 152.2
- cost_usd: 0.0036
- tokens: 80652 in / 9163 out
- orchestration: pipeline
- pages_extracted: 20
- reference_follow: ['CBA/FY24/profit_announcement p36 <- p29 page 20 [added]', 'CBA/FY25/profit_announcement p36 <- p29 page 20 [added]']
