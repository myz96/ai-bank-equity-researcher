# CBA — nim — FY25 vs FY24

**Movement (cash basis):** 199bps → 208bps (+9bps) | **Attribution confidence:** 95/100

*Read from: row 'Net interest margin', column FY24 Total Group -> column FY25 Total Group*

CBA's Group NIM (cash basis) increased 9 bps to 208 bps in FY25 from 199 bps in FY24. The improvement was driven by a 7 bps benefit from reduced liquid assets and pooled facilities drag, and a 9 bps contribution from capital and replicating portfolio earnings. These were partially offset by a 7 bps increase in funding costs and a 1 bps adverse impact from basis risk.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & Pooled Facilities | +7 bps | 85 | 1 (single_source) | ev-1, ev-5, ev-6, ev-22 |
| `asset_pricing` | Asset pricing | +0 bps | 85 | 1 (single_source) | ev-1 |
| `funding` | Funding costs | -7 bps | 85 | 1 (single_source) | ev-1 |
| `mix` | Portfolio mix | +0 bps | 85 | 1 (single_source) | ev-1 |
| `basis_risk` | Basis risk | -1 bps | 85 | 1 (single_source) | ev-1 |
| `capital_replicating` | Capital, Replicating and Other | +9 bps | 85 | 1 (single_source) | ev-1 |
| `markets_treasury` | Treasury and Markets | +1 bps | 85 | 1 (single_source) | ev-1 |

### liquids — "Liquids & Pooled Facilities"
*+7 bps | confidence 85/100*

A 7 bps positive contribution from the reduction in lower-yielding liquid assets and institutional pooled facilities.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-5] CBA/FY25/profit_announcement, PDF p9: "Net interest margin 2.08% 9bpts on FY24 (+2bpts underlying basis)"
> [ev-6] CBA/FY25/profit_announcement, PDF p9: "Excluding the mix effect of lower liquid assets and institutional pooled facilities, margins improved by 2bpts."
> [ev-22] CBA/FY25/profit_announcement, printed p12: "Excluding a 7 basis point increase in margin from a reduction in lower yielding liquid assets and institutional pooled facilities... net interest margin increased 2 basis points."

### asset_pricing — "Asset pricing"
*+0 bps | confidence 85/100*

No net contribution from asset pricing drivers in the primary walk.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

### funding — "Funding costs"
*-7 bps | confidence 85/100*

A 7 bps negative impact from higher funding costs, reflecting competition and mix shifts.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

### mix — "Portfolio mix"
*+0 bps | confidence 85/100*

No net contribution from portfolio mix in the primary walk.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

### basis_risk — "Basis risk"
*-1 bps | confidence 85/100*

A 1 bps negative impact from basis risk (bills/OIS spread).
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

### capital_replicating — "Capital, Replicating and Other"
*+9 bps | confidence 85/100*

A 9 bps positive contribution from capital, replicating portfolio, and other items.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

### markets_treasury — "Treasury and Markets"
*+1 bps | confidence 85/100*

A 1 bps positive contribution from Treasury and Markets.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

## Source disagreements
- **NIM Movement Magnitude** (definitional): 9 bps (Group Cash Basis, ev-5, ev-7, ev-20) vs -3 bps (Cash NPAT Segment, ev-13, ev-14) vs -4 bps (Cash NII Segment, ev-16, ev-17)
  Preferred: 9 bps (Group Cash Basis). The task requires the Group Net Interest Margin. The -3 bps and -4 bps figures refer to specific segments (likely Business Banking or similar cash-basis sub-metrics) within the Profit Announcement narrative, not the consolidated Group NIM reported in the KPI table.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY25/profit_announcement (e2e911ab4fed), CBA/FY24/profit_announcement (1ab9332c8371), CBA/FY24/results_presentation (168e3835d44c)
- generated: 2026-08-29T13:15:31+00:00
- seconds: 77.1
- cost_usd: 0.0023
- tokens: 54493 in / 5073 out
- orchestration: pipeline
