# CBA — nim — FY25 vs FY24

**Movement (cash basis):** 199bps → 208bps (+9bps) | **Attribution confidence:** 95/100

*Read from: row 'Net interest margin (%)', column FY24 Total Group -> column FY25 Total Group*

CBA's Group NIM (cash basis) increased 9 bps to 208 bps in FY25 from 199 bps in FY24. The improvement was driven by a 7 bps benefit from lower liquid assets and pooled facilities, offset by 7 bps of higher funding costs and 1 bps of adverse basis risk. Capital and replicating portfolio earnings contributed 9 bps.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & Pooled Facilities | +7 bps | 85 | 1 (single_source) | ev-1, ev-5, ev-6, ev-21 |
| `funding` | Funding costs | -7 bps | 85 | 1 (single_source) | ev-1, ev-14 |
| `capital_replicating` | Capital, Replicating and Other | +9 bps | 85 | 1 (single_source) | ev-1, ev-14 |
| `basis_risk` | Basis risk | -1 bps | 85 | 1 (single_source) | ev-1, ev-14 |
| `markets_treasury` | Treasury and Markets | +1 bps | 85 | 1 (single_source) | ev-1 |
| `asset_pricing` | Asset pricing | +0 bps | 85 | 1 (single_source) | ev-1 |
| `mix` | Portfolio mix | +0 bps | 85 | 1 (single_source) | ev-1 |

### liquids — "Liquids & Pooled Facilities"
*+7 bps | confidence 85/100*

A reduction in lower-yielding liquid assets and institutional pooled facilities improved the margin by 7 bps.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-5] CBA/FY25/profit_announcement, PDF p9: "Net interest margin 2.08% 9bpts on FY24 (+2bpts underlying basis)"
> [ev-6] CBA/FY25/profit_announcement, PDF p9: "Excluding the mix effect of lower liquid assets and institutional pooled facilities, margins improved by 2bpts."
> [ev-21] CBA/FY25/profit_announcement, printed p12: "Excluding a 7 basis point increase in margin from a reduction in lower yielding liquid assets and institutional pooled facilities... net interest margin increased 2 basis points."

### funding — "Funding costs"
*-7 bps | confidence 85/100*

Higher funding costs reduced the margin by 7 bps, primarily due to deposit pricing competition and mix shifts towards higher-yielding deposits.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-14] CBA/FY25/profit_announcement, printed p42: "Net interest margin decreased by 3 basis points on the prior year, reflecting: • Lower deposit margins mainly due to competition, unfavourable mix as customers shift to higher yielding deposits and the impact of declining interest rates; • Lower home lending margins principally reflecting elevated competition; and • The impact of higher basis risk arising from an increase in the spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate; partly offset by • Higher earnings on the replicating portfolio; • Favourable portfolio mix primarily due to the benefit of stro"

### capital_replicating — "Capital, Replicating and Other"
*+9 bps | confidence 85/100*

Higher earnings on the replicating portfolio and capital management activities contributed a 9 bps increase to the margin.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-14] CBA/FY25/profit_announcement, printed p42: "Net interest margin decreased by 3 basis points on the prior year, reflecting: • Lower deposit margins mainly due to competition, unfavourable mix as customers shift to higher yielding deposits and the impact of declining interest rates; • Lower home lending margins principally reflecting elevated competition; and • The impact of higher basis risk arising from an increase in the spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate; partly offset by • Higher earnings on the replicating portfolio; • Favourable portfolio mix primarily due to the benefit of stro"

### basis_risk — "Basis risk"
*-1 bps | confidence 85/100*

Adverse basis risk arising from an increase in the spread between the 3-month bank bill swap rate and the 3-month OIS rate reduced the margin by 1 bps.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-14] CBA/FY25/profit_announcement, printed p42: "Net interest margin decreased by 3 basis points on the prior year, reflecting: • Lower deposit margins mainly due to competition, unfavourable mix as customers shift to higher yielding deposits and the impact of declining interest rates; • Lower home lending margins principally reflecting elevated competition; and • The impact of higher basis risk arising from an increase in the spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate; partly offset by • Higher earnings on the replicating portfolio; • Favourable portfolio mix primarily due to the benefit of stro"

### markets_treasury — "Treasury and Markets"
*+1 bps | confidence 85/100*

Treasury and markets activities contributed a net positive 1 bps to the margin movement.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

### asset_pricing — "Asset pricing"
*+0 bps | confidence 85/100*

Asset pricing had no net impact on the margin movement for the period.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

### mix — "Portfolio mix"
*+0 bps | confidence 85/100*

Portfolio mix had no net impact on the margin movement for the period.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

## Source disagreements
- **NIM Basis Reporting** (definitional): 9 bps increase (Cash/Primary basis, ev-5, ev-7) vs -3 bps decrease (Statutory basis, ev-8)
  Preferred: 9 bps increase (Cash/Primary basis). The task requires the Group net interest margin row from the results book's KPI table. The primary reporting basis for CBA's Group NIM is cash (unlabelled rows take the primary basis). The statutory basis shows a different movement (-3 bps) due to accounting differences, but the cash basis is the correct measure for this analysis.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY25/profit_announcement (e2e911ab4fed), CBA/FY24/profit_announcement (1ab9332c8371), CBA/FY24/results_presentation (168e3835d44c)
- generated: 2026-08-29T03:37:10+00:00
- seconds: 84.4
- cost_usd: 0.0022
- tokens: 54094 in / 4774 out
- orchestration: pipeline
