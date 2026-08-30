# CBA — nim — FY26 vs FY25

**Movement (cash basis):** 208bps → 205bps (-3bps) | **Attribution confidence:** 90/100

*Read from: row 'Net interest margin (%)', column Full Year Ended 30 Jun 25 -> column Full Year Ended 30 Jun 26*

CBA's Group net interest margin (cash basis) decreased 3 bps to 205 bps (2.05%) in FY26 from 208 bps (2.08%) in FY25. Excluding liquids, NIM was stable. The decline was driven by asset pricing headwinds (-5 bps) from home loan and business/institutional lending competition, partially offset by capital/replicating portfolio gains (+5 bps) and favourable portfolio mix (+2 bps). Liquids drag was -3 bps, while funding costs and basis risk were flat. Treasury & Markets contributed -2 bps.

> [ev-4] CBA/FY26/profit_announcement, printed p3: "Net interest margin (%) 2.05 2.08 (3)bpts"
> [ev-5] CBA/FY26/profit_announcement, PDF p28: "The Bank's net interest margin decreased by 3 basis points on the prior year to 2.05%. Excluding growth in liquid assets, which have broadly neutral impacts on net interest income, net interest margin was stable."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids | -3 bps | 92 | 2 (corroborated_2_sources) | ev-5, ev-14 |
| `asset_pricing` | Asset pricing | -5 bps | 92 | 1 (corroborated_2_sources) | ev-6 |
| `funding` | Funding costs | +0 bps | 92 | 1 (corroborated_2_sources) | ev-7 |
| `mix` | Portfolio mix | +2 bps | 92 | 1 (corroborated_2_sources) | ev-8 |
| `basis_risk` | Basis risk | +0 bps | 85 | 1 (single_source) | ev-9 |
| `capital_replicating` | Capital, Replicating and Other | +5 bps | 92 | 1 (corroborated_2_sources) | ev-10 |
| `markets_treasury` | Treasury and Markets | -2 bps | 92 | 1 (corroborated_2_sources) | ev-11 |
| *residual (unexplained)* | — | +0 bps | — | — |

### liquids — "Liquids"
*-3 bps | confidence 92/100*

Growth in liquid assets of $15bn increased the drag by 3 bps. The bank notes liquids have broadly neutral impacts on NII, and excluding them NIM was stable.
> [ev-5] CBA/FY26/profit_announcement, PDF p28: "The Bank's net interest margin decreased by 3 basis points on the prior year to 2.05%. Excluding growth in liquid assets, which have broadly neutral impacts on net interest income, net interest margin was stable."
> [ev-14] CBA/FY26/results_presentation, printed p60: "1. +$15bn increase in average liquid assets and +$11bn increase in average institutional repos in FY26 vs FY25."

### asset_pricing — "Asset pricing"
*-5 bps | confidence 92/100*

Home lending pricing down 4 bps and business/institutional lending pricing down 1 bps, primarily reflecting competition.
> [ev-6] CBA/FY26/profit_announcement, PDF p28: "Asset pricing: Decreased margin by 5 basis points driven by home lending pricing (down 4 basis points) and business and institutional lending pricing (down 1 basis point), primarily reflecting the impact of competition."

### funding — "Funding costs"
*+0 bps | confidence 92/100*

Flat year-on-year. The bank does not disclose further sub-components.
> [ev-7] CBA/FY26/profit_announcement, PDF p28: "Funding costs: Flat."

### mix — "Portfolio mix"
*+2 bps | confidence 92/100*

Favourable asset mix from strong growth in business lending and favourable funding mix from strong deposit growth.
> [ev-8] CBA/FY26/profit_announcement, PDF p28: "Portfolio mix: Increased margin by 2 basis points driven by favourable asset mix from strong growth in business lending and favourable funding mix from strong growth in deposits."

### basis_risk — "Basis risk"
*+0 bps | confidence 85/100*

Flat. The bank does not disclose a numerical value beyond stating flat.
> [ev-9] CBA/FY26/profit_announcement, PDF p28: "Basis risk: Flat."

### capital_replicating — "Capital, Replicating and Other"
*+5 bps | confidence 92/100*

Higher earnings on the replicating portfolio from changes in portfolio rate and volume (up 4 bps) and higher earnings on capital hedges (up 1 bps).
> [ev-10] CBA/FY26/profit_announcement, PDF p29: "Capital, Replicating and Other: Increased margin by 5 basis points driven by higher earnings on the replicating portfolio due to changes in portfolio rate and volume (up 4 basis points) and higher earnings on capital hedges (up 1 basis point)."

### markets_treasury — "Treasury and Markets"
*-2 bps | confidence 92/100*

Lower risk management income in Treasury and growth in reverse sale and repurchase agreement balances.
> [ev-11] CBA/FY26/profit_announcement, PDF p29: "Treasury and Markets: Decreased margin by 2 basis points due to lower risk management income in Treasury and growth in reverse sale and repurchase agreement balances."

## Source disagreements
- **Liquids bar value** (rounding): -3 bps (profit_announcement p28) vs -4 bps (results_presentation p60)
  Preferred: -3 bps. The results book splits Liquids as -3 bps; the presentation combines Liquids & repos at -4 bps with sub-components of -3 (liquid assets) and -1 (institutional repos). The book's framing is primary.
- **Treasury & Markets bar value** (rounding): -2 bps (profit_announcement p28) vs -1 bps (results_presentation p60)
  Preferred: -2 bps. The results book reports -2 bps; the presentation reports -1 bps. Both are within rounding tolerance of the same underlying measure.

## Limitations
- The RBS divisional NIM (2.50% vs 2.51%, -1 bpt) is reported separately on cash basis and differs from the Group statutory-equivalent NIM (2.05% vs 2.08%, -3 bps); the Group-level walk decomposes the latter.
- The presentation slide chart uses slightly different bar values for Liquids (-4 vs -3) and Treasury & Markets (-1 vs -2) than the results book; only the book's values are used in the driver table.
- Funding costs and basis risk are reported as 'Flat' with no quantified sub-components disclosed by the bank.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T12:43:36+00:00
- seconds: 123.1
- cost_usd: 0.0112
- tokens: 502560 in / 7359 out
- orchestration: agent
- tool_calls: 26
- pages_read: 8
- charts_read: 2
- budget_exhausted: no
