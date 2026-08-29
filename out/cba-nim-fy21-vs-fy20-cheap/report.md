# CBA — nim — FY21 vs FY20

**Movement (cash basis):** 207bps → 203bps (-4bps) | **Attribution confidence:** 95/100

*Read from: row 'Net interest margin', column FY20 -> column FY21*

CBA's Group net interest margin decreased by 4 basis points to 203 bps in FY21 (vs 207 bps in FY20). The decline was driven primarily by higher liquid assets (-4 bps), lower asset pricing (-2 bps), and increased funding costs (-3 bps). These were partially offset by favourable portfolio mix (+2 bps), basis risk benefits (+3 bps), and Treasury & Markets contributions (+2 bps), alongside a negative capital impact (-2 bps).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Higher Liquids | -4 bps | 85 | 1 (single_source) | ev-1, ev-2 |
| `asset_pricing` | Asset Pricing | -2 bps | 85 | 1 (single_source) | ev-2 |
| `funding` | Deposit Pricing & Funding | -3 bps | 85 | 1 (single_source) | ev-2 |
| `capital_replicating` | Capital & Other | -2 bps | 85 | 1 (single_source) | ev-2 |
| `mix` | Portfolio Mix | +2 bps | 95 | 2 () | ev-2, ev-3 |
| `basis_risk` | Basis Risk (incl RP) | +3 bps | 95 | 2 () | ev-2, ev-4 |
| `markets_treasury` | Treasury & Markets | +2 bps | 95 | 2 () | ev-2, ev-6 |

### liquids — "Higher Liquids"
*-4 bps | confidence 85/100*

Higher liquidity levels reduced the margin contribution by 4 bps compared to FY20.
> [ev-1] CBA/FY21/results_presentation, printed p29: "[walk chart] CBA net interest margin in FY21 vs FY20: FY20 207.0 -> FY21 203.0"
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"

### asset_pricing — "Asset Pricing"
*-2 bps | confidence 85/100*

Margin decreased by 2 bps due to competitive pressures and customer migration to lower-margin fixed-rate loans.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"

### funding — "Deposit Pricing & Funding"
*-3 bps | confidence 85/100*

Funding costs increased, reducing margin by 3 bps, reflecting the low-rate environment on deposit balances.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"

### capital_replicating — "Capital & Other"
*-2 bps | confidence 85/100*

Lower earnings on group capital due to falling rates reduced margin by 2 bps.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"

### mix — "Portfolio Mix"
*+2 bps | confidence 95/100*

Favourable mix from strong transaction/savings deposit growth and TFF drawdowns improved margin by 2 bps.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-3] CBA/FY21/profit_announcement, PDF p33: "Portfolio mix: Increased margin by 2 basis points driven by a higher average deposit funding ratio (30 June 2021: 77%; 30 June 2020: 71%) due to strong growth in transaction and savings deposits, customers switching to at-call deposits, and the drawdown of the TFF (up 4 basis points), partly offset by an unfavourable impact from asset mix (down 2 basis points), mainly due to a decline in higher margin consumer finance balances."

### basis_risk — "Basis Risk (incl RP)"
*+3 bps | confidence 95/100*

A decrease in the average bill/OIS spread improved margin by 3 bps.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-4] CBA/FY21/profit_announcement, PDF p33: "Basis risk: Basis risk arises from the spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate. The Bank’s margin increased 3 basis points reflecting a decrease in the average spread notwithstanding a structural reduction in exposure to basis risk due to strong growth in cash rate linked deposits and a mix shift towards fixed rate home loans."

### markets_treasury — "Treasury & Markets"
*+2 bps | confidence 95/100*

Higher bonds and commodities financing income in Global Markets contributed positively by 2 bps.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-6] CBA/FY21/profit_announcement, PDF p33: "Treasury and Markets: Increased margin by 2 basis points driven by higher bonds and commodities financing income in Global Markets."

## Source disagreements
- **Walk Framing Granularity** (definitional): -4 bps Higher Liquids, -6 bps Impact of lower rates, +6 bps Management actions/other (ev-1) vs -4 bps Higher Liquids, -2 bps Asset Pricing, -3 bps Deposit Pricing & Funding, -2 bps Capital & Other, +2 bps Portfolio Mix, +3 bps Basis Risk, +2 bps Treasury & Markets (ev-2)
  Preferred: ev-2. The results presentation contains two walks for the same comparison. ev-1 uses a high-level 'Impact of lower rates' bar, while ev-2 provides the detailed canonical driver breakdown required for this task. Per source hierarchy, the more granular walk (ev-2) is adopted as primary.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-29T13:13:05+00:00
- seconds: 91.4
- cost_usd: 0.002
- tokens: 39301 in / 6333 out
- orchestration: pipeline
