# CBA — nim — FY26 vs FY25

**Movement (cash basis):** 208bps → 205bps (-3bps) | **Attribution confidence:** 90/100

*Read from: row 'Net interest margin (%)', column 30 Jun 25 -> column 30 Jun 26*

CBA's net interest margin decreased 3 basis points to 2.05% in FY26 from 2.08% in FY25. Excluding the drag from growth in liquid assets (which had broadly neutral impacts on NII), the underlying margin was stable. The decline was driven primarily by competitive pressure on home lending and business/institutional lending pricing (−5 bps), partially offset by favourable portfolio mix from strong business lending and deposit growth (+2 bps) and higher replicating portfolio and capital hedge earnings (+5 bps). Liquids growth contributed −3 bps, while funding costs and basis risk were flat. Treasury & Markets reduced margin by 2 bps.

> [ev-13] CBA/FY26/profit_announcement, printed p3: "Net interest margin (%) 2.05 2.08 (3)bpts"
> [ev-14] CBA/FY26/profit_announcement, PDF p28: "Net interest margin (%) 2.05 2.08 (3)bpts"
> [ev-15] CBA/FY26/profit_announcement, PDF p28: "The Bank's net interest margin decreased by 3 basis points on the prior year to 2.05%. Excluding growth in liquid assets, which have broadly neutral impacts on net interest income, net interest margin was stable."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | — | -3 bps | 90 | 1 (corroborated_2_sources) | ev-14, ev-15 |
| `asset_pricing` | — | -5 bps | 90 | 1 (corroborated_2_sources) | ev-16 |
| `funding` | — | +0 bps | 80 | 1 (corroborated_2_sources) | ev-17 |
| `mix` | — | +2 bps | 90 | 1 (corroborated_2_sources) | ev-18 |
| `basis_risk` | — | +0 bps | 80 | 1 (single_source) | ev-19 |
| `capital_replicating` | — | +5 bps | 90 | 1 (cross_source_divergence_surfaced) | ev-20 |
| `markets_treasury` | — | -2 bps | 90 | 1 (corroborated_2_sources) | ev-21 |

### liquids
*-3 bps | confidence 90/100*

Growth in average liquid assets of $15 billion (9%) to $187 billion, including institutional repos, created a margin drag as low-yielding liquid balances grew faster than higher-yielding earning assets.
> [ev-14] CBA/FY26/profit_announcement, PDF p28: "Net interest margin (%) 2.05 2.08 (3)bpts"
> [ev-15] CBA/FY26/profit_announcement, PDF p28: "The Bank's net interest margin decreased by 3 basis points on the prior year to 2.05%. Excluding growth in liquid assets, which have broadly neutral impacts on net interest income, net interest margin was stable."

### asset_pricing
*-5 bps | confidence 90/100*

Home lending pricing fell 4 bps and business/institutional lending pricing fell 1 bps, primarily reflecting competitive pressure in the retail mortgage market.
> [ev-16] CBA/FY26/profit_announcement, PDF p28: "Asset pricing: Decreased margin by 5 basis points driven by home lending pricing (down 4 basis points) and business and institutional lending pricing (down 1 basis point), primarily reflecting the impact of competition."

### funding
*+0 bps | confidence 80/100*

Funding costs were flat year-on-year, with rising interest rates offset by unfavourable deposit mix shifts.
> [ev-17] CBA/FY26/profit_announcement, PDF p28: "Funding costs: Flat."

### mix
*+2 bps | confidence 90/100*

Favourable asset mix from strong growth in business lending ($27 billion, +10%) and favourable funding mix from strong deposit growth supported margin.
> [ev-18] CBA/FY26/profit_announcement, PDF p28: "Portfolio mix: Increased margin by 2 basis points driven by favourable asset mix from strong growth in business lending and favourable funding mix from strong growth in deposits."

### basis_risk
*+0 bps | confidence 80/100*

Basis risk (bills/OIS spread) was flat year-on-year.
> [ev-19] CBA/FY26/profit_announcement, PDF p28: "Basis risk: Flat."

### capital_replicating
*+5 bps | confidence 90/100*

Higher earnings on the replicating portfolio (up 4 bps from changes in portfolio rate and volume) and higher earnings on capital hedges (up 1 bps) drove margin improvement.
> [ev-20] CBA/FY26/profit_announcement, PDF p29: "Capital, Replicating and Other: Increased margin by 5 basis points driven by higher earnings on the replicating portfolio due to changes in portfolio rate and volume (up 4 basis points) and higher earnings on capital hedges (up 1 basis point)."

### markets_treasury
*-2 bps | confidence 90/100*

Lower risk management income in Treasury and growth in reverse sale and repurchase agreement balances reduced margin.
> [ev-21] CBA/FY26/profit_announcement, PDF p29: "Treasury and Markets: Decreased margin by 2 basis points due to lower risk management income in Treasury and growth in reverse sale and repurchase agreement balances."

## Source disagreements
- **capital_replicating contribution** (definitional): +1 — Capital, Treasury & Replicating (CBA/FY26/profit_announcement PDF p28 (ev-1)) vs +5 — Interest rate risk hedging (CBA/FY26/results_presentation PDF p60 (ev-4))
  Preferred: +5 (per the source hierarchy). The documents use different decompositions of the same movement.

## Limitations
- Capped at 80: funding +0 bps, basis_risk +0 bps. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.
- Failed check: walk_sum (start 208 + bars -7.0 = 201.0 != end 205, tol 0.1 %) [CBA/FY26/profit_announcement PDF p28 (ev-1)]

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T19:40:16+00:00
- seconds: 102.2
- cost_usd: 0.0083
- tokens: 509675 in / 6040 out
- orchestration: agent
- tool_calls: 27
- pages_read: 10
- charts_read: 2
- budget_exhausted: no
