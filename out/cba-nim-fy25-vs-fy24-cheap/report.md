# CBA — nim — FY25 vs FY24

**Movement (cash basis):** 199bps → 208bps (+9bps) | **Attribution confidence:** 95/100

*Read from: row 'Net interest margin', column FY24 Total Group -> column FY25 Total Group*

CBA's Group NIM (cash basis) increased 9 bps to 208 bps in FY25 vs FY24. The improvement was driven by a 7 bps benefit from reduced liquid assets and pooled facilities drag, offset by 7 bps of higher funding costs due to deposit competition. Capital/replicating portfolio earnings contributed 9 bps.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & Pooled Facilities | +7 bps | 85 | 1 (single_source) | ev-1, ev-5, ev-6, ev-20 |
| `funding` | Funding costs | -7 bps | 85 | 1 (single_source) | ev-1, ev-21 |
| `capital_replicating` | Capital, Replicating and Other | +9 bps | 85 | 1 (single_source) | ev-1 |
| `asset_pricing` | Asset pricing | +0 bps | 85 | 1 (single_source) | ev-1 |
| `mix` | Portfolio mix | +0 bps | 85 | 1 (single_source) | ev-1 |
| `basis_risk` | Basis risk | -1 bps | 85 | 1 (single_source) | ev-1 |
| `markets_treasury` | Treasury and Markets | +1 bps | 85 | 1 (single_source) | ev-1 |

### liquids — "Liquids & Pooled Facilities"
*+7 bps | confidence 85/100*

Reduction in lower-yielding liquid assets and institutional pooled facilities improved margin by 7 bps.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-5] CBA/FY25/profit_announcement, PDF p9: "Net interest margin 2.08% 9bpts on FY24 (+2bpts underlying basis)"
> [ev-6] CBA/FY25/profit_announcement, PDF p9: "Excluding the mix effect of lower liquid assets and institutional pooled facilities, margins improved by 2bpts."
> [ev-20] CBA/FY25/profit_announcement, printed p12: "Excluding a 7 basis point increase in margin from a reduction in lower yielding liquid assets and institutional pooled facilities... net interest margin increased 2 basis points."

### funding — "Funding costs"
*-7 bps | confidence 85/100*

Increased deposit price competition drove down margins by 7 bps.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-21] CBA/FY25/profit_announcement, printed p12: "Funding costs: Decreased margin by 7 basis points driven by increased deposit price competition."

### capital_replicating — "Capital, Replicating and Other"
*+9 bps | confidence 85/100*

Higher earnings on the replicating portfolio contributed positively to margin.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

### asset_pricing — "Asset pricing"
*+0 bps | confidence 85/100*

No net impact from asset pricing changes this period.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

### mix — "Portfolio mix"
*+0 bps | confidence 85/100*

No net impact from portfolio mix changes this period.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

### basis_risk — "Basis risk"
*-1 bps | confidence 85/100*

Unfavourable movement in the bill/OIS spread reduced margin by 1 bps.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

### markets_treasury — "Treasury and Markets"
*+1 bps | confidence 85/100*

Treasury and markets activities contributed a positive 1 bps.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

## Source disagreements
- **Cash vs Statutory NIM Movement** (definitional): 9 bps increase (Primary Cash Basis) vs -3 bps decrease (Statutory Basis)
  Preferred: 9 bps increase (Primary Cash Basis). The bank reports two distinct NIM measures. The primary cash-basis NIM (Group) increased 9 bps (ev-1, ev-5). The statutory NIM decreased 3 bps (ev-13). As per instructions, the primary basis is used for the main analysis.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY25/profit_announcement (e2e911ab4fed), CBA/FY24/profit_announcement (1ab9332c8371), CBA/FY24/results_presentation (168e3835d44c)
- generated: 2026-08-28T12:29:25+00:00
- seconds: 195.2
- cost_usd: 0.0022
- tokens: 53890 in / 4527 out
- orchestration: pipeline
