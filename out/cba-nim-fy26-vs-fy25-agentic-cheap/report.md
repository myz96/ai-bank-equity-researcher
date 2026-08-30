# CBA — nim — FY26 vs FY25

**Movement (cash basis):** 208bps → 205bps (-3bps) | **Attribution confidence:** 85/100

*Read from: row 'Net interest margin (%)', column Full Year Ended 30 Jun 25 -> column Full Year Ended 30 Jun 26*

CBA's Group net interest margin (cash basis) declined 3 bps to 205 bps (2.05%) in FY26 from 208 bps (2.08%) in FY25. Excluding growth in liquid assets and institutional repos, which had broadly neutral impacts on NII, underlying margins were stable. The decline was driven by lower asset pricing (-5 bps from home lending and business/institutional lending competition), partially offset by higher capital and replicating portfolio earnings (+5 bps) and favourable portfolio mix (+2 bps from business lending and deposit growth). Liquids drag was -3 bps, while funding costs and basis risk were flat. Treasury & Markets contributed -2 bps from lower risk management income and repo balance growth.

> [ev-1] CBA/FY26/profit_announcement, printed p5: "Net interest margin (%) 2.50 2.51 (1)bpt"
> [ev-4] CBA/FY26/profit_announcement, PDF p28: "Net interest margin (%) 2.05 2.08 (3)bpts"
> [ev-15] CBA/FY26/profit_announcement, printed p3: "Net interest margin (%) 2.05 2.08 (3)bpts"
> [ev-16] CBA/FY26/profit_announcement, PDF p9: "Margins were broadly stable excluding growth in liquid assets and institutional reverse sale and repurchase agreements, which have broadly neutral impacts on net interest income."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | — | -3 bps | 85 | 1 (corroborated_2_sources) | ev-2 |
| `asset_pricing` | — | -5 bps | 90 | 1 (corroborated_2_sources) | ev-5 |
| `funding` | — | +0 bps | 85 | 1 (corroborated_2_sources) | ev-6 |
| `mix` | — | +2 bps | 90 | 1 (corroborated_2_sources) | ev-7 |
| `basis_risk` | — | +0 bps | 85 | 1 (single_source) | ev-8 |
| `capital_replicating` | — | +5 bps | 90 | 1 (cross_source_divergence_surfaced) | ev-9 |
| `markets_treasury` | — | -2 bps | 90 | 1 (corroborated_2_sources) | ev-10 |

### liquids
*-3 bps | confidence 85/100*

Liquids and repos increased by $26 billion ($15bn liquid assets + $11bn institutional repos) year-on-year, creating a -3 bps margin drag with broadly neutral impact on net interest income.
> [ev-2] CBA/FY26/profit_announcement, PDF p28: "[walk chart] NIM Movement since June 2025: Jun 25 Full Year 208 -> Jun 26 Full Year 205"

### asset_pricing
*-5 bps | confidence 90/100*

Home lending pricing down 4 bps and business and institutional lending pricing down 1 bps, primarily reflecting the impact of competition.
> [ev-5] CBA/FY26/profit_announcement, PDF p28: "Asset pricing: Decreased margin by 5 basis points driven by home lending pricing (down 4 basis points) and business and institutional lending pricing (down 1 basis point), primarily reflecting the impact of competition."

### funding
*+0 bps | confidence 85/100*

Funding costs were flat year-on-year, with rising interest rates partly offset by unfavourable deposit mix.
> [ev-6] CBA/FY26/profit_announcement, PDF p28: "Funding costs: Flat."

### mix
*+2 bps | confidence 90/100*

Favourable asset mix from strong growth in business lending and favourable funding mix from strong growth in deposits.
> [ev-7] CBA/FY26/profit_announcement, PDF p28: "Portfolio mix: Increased margin by 2 basis points driven by favourable asset mix from strong growth in business lending and favourable funding mix from strong growth in deposits."

### basis_risk
*+0 bps | confidence 85/100*

Basis risk (bills/OIS spread) was flat year-on-year.
> [ev-8] CBA/FY26/profit_announcement, PDF p28: "Basis risk: Flat."

### capital_replicating
*+5 bps | confidence 90/100*

Higher earnings on the replicating portfolio due to changes in portfolio rate and volume (up 4 bps) and higher earnings on capital hedges (up 1 bps).
> [ev-9] CBA/FY26/profit_announcement, PDF p29: "Capital, Replicating and Other: Increased margin by 5 basis points driven by higher earnings on the replicating portfolio due to changes in portfolio rate and volume (up 4 basis points) and higher earnings on capital hedges (up 1 basis point)."

### markets_treasury
*-2 bps | confidence 90/100*

Lower risk management income in Treasury and growth in reverse sale and repurchase agreement balances.
> [ev-10] CBA/FY26/profit_announcement, PDF p29: "Treasury and Markets: Decreased margin by 2 basis points due to lower risk management income in Treasury and growth in reverse sale and repurchase agreement balances."

## Source disagreements
- **capital_replicating contribution** (definitional): +1 — Capital, Replicating and Other (CBA/FY26/profit_announcement PDF p28 (ev-2)) vs +5 — Interest rate risk hedging (CBA/FY26/results_presentation PDF p60 (ev-3))
  Preferred: +5 (per the source hierarchy). The documents use different decompositions of the same movement.

## Limitations
- The results book walk chart (p28) fails its own sum check: bars sum to -7 bps vs actual -3 bps movement, with the Capital, Replicating and Other bar showing +1 bps in the chart but +5 bps in the accompanying text. Driver values used are from the text narrative which is internally consistent and sums correctly to -3 bps.
- The presentation slide chart (p60) passes its sum check but uses different labels (combining liquids+repos, splitting hedging separately) and slightly different values. Results book text is primary per source hierarchy.
- No statutory-basis NIM is separately disclosed; the bank reports only cash-basis NIM.
- Failed check: walk_sum (start 208 + bars -7.0 = 201.0 != end 205, tol 1.0) [CBA/FY26/profit_announcement PDF p28 (ev-2)]

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T14:05:58+00:00
- seconds: 172.5
- cost_usd: 0.0315
- tokens: 815784 in / 8269 out
- orchestration: agent
- tool_calls: 36
- pages_read: 9
- charts_read: 2
- budget_exhausted: no
