# CBA — nim — FY21 vs FY20

**Movement (cash basis):** 207bps → 203bps (-4bps) | **Attribution confidence:** 95/100

*Read from: row 'Net interest margin (%)', column FY20 -> column FY21*

CBA's Group net interest margin decreased by 4 basis points to 203 bps in FY21 (from 207 bps in FY20). The decline was driven primarily by higher liquid assets (-4 bps) and lower asset pricing (-2 bps), partially offset by favourable portfolio mix (+2 bps) and basis risk dynamics (+3 bps).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Higher Liquids | -4 bps | 95 | 2 () | ev-1, ev-2, ev-17 |
| `asset_pricing` | Asset Pricing | -2 bps | 95 | 2 () | ev-2, ev-10 |
| `funding` | Deposit Pricing & Funding | -3 bps | 85 | 1 (single_source) | ev-2 |
| `capital_replicating` | Capital & Other | -2 bps | 95 | 2 () | ev-2, ev-5 |
| `mix` | Portfolio Mix | +2 bps | 95 | 2 () | ev-2, ev-3 |
| `basis_risk` | Basis Risk (incl RP) | +3 bps | 95 | 2 () | ev-2, ev-4 |
| `markets_treasury` | Treasury & Markets | +2 bps | 95 | 2 () | ev-2, ev-6 |

### liquids — "Higher Liquids"
*-4 bps | confidence 95/100*

Increased liquid asset balances exerted a drag on the margin.
> [ev-1] CBA/FY21/results_presentation, printed p29: "[walk chart] CBA net interest margin in FY21 vs FY20: FY20 207 -> FY21 203"
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-17] CBA/FY21/profit_announcement, PDF p11: "Net interest margin (NIM) was down 4 basis points due to higher liquid assets, with the impact of the low-rate environment largely offset by management actions, lower wholesale funding costs and favourable funding mix."

### asset_pricing — "Asset Pricing"
*-2 bps | confidence 95/100*

Margin declined due to home lending competition and customer switching to fixed rates.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-10] CBA/FY21/profit_announcement, PDF p33: "Asset pricing: Decreased margin by 2 basis points driven by home lending, reflecting the impact of customers switching to lower margin loans, particularly from variable rate to fixed rate loans (down 3 basis points) and increased competition (down 2 basis points), partly offset by repricing (up 3 basis points)."

### funding — "Deposit Pricing & Funding"
*-3 bps | confidence 85/100*

Funding costs increased as deposit margins compressed in the low-rate environment.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"

### capital_replicating — "Capital & Other"
*-2 bps | confidence 95/100*

Lower earnings on group capital due to falling interest rates, partly offset by NZ contribution.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-5] CBA/FY21/profit_announcement, PDF p33: "Capital and other: Decreased margin by 2 basis points driven by lower earnings on Group capital due to the falling interest rate environment (down 3 basis points), partly offset by increased contribution from New Zealand (up 1 basis point), reflecting lower wholesale funding costs and favourable portfolio mix, partly offset by the impact from RBNZ cash rate cuts."

### mix — "Portfolio Mix"
*+2 bps | confidence 95/100*

Favourable funding mix from TFF drawdown and at-call deposits, offset by unfavourable consumer finance mix.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-3] CBA/FY21/profit_announcement, PDF p33: "Portfolio mix: Increased margin by 2 basis points driven by a higher average deposit funding ratio (30 June 2021: 77%; 30 June 2020: 71%) due to strong growth in transaction and savings deposits, customers switching to at-call deposits, and the drawdown of the TFF (up 4 basis points), partly offset by an unfavourable impact from asset mix (down 2 basis points), mainly due to a decline in higher margin consumer finance balances."

### basis_risk — "Basis Risk (incl RP)"
*+3 bps | confidence 95/100*

Margin increased reflecting a decrease in the average bill/OIS spread.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-4] CBA/FY21/profit_announcement, PDF p33: "Basis risk: Basis risk arises from the spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate. The Bank’s margin increased 3 basis points reflecting a decrease in the average spread notwithstanding a structural reduction in exposure to basis risk due to strong growth in cash rate linked deposits and a mix shift towards fixed rate home loans."

### markets_treasury — "Treasury & Markets"
*+2 bps | confidence 95/100*

Higher bonds and commodities financing income in Global Markets.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-6] CBA/FY21/profit_announcement, PDF p33: "Treasury and Markets: Increased margin by 2 basis points driven by higher bonds and commodities financing income in Global Markets."

## Source disagreements
- **Walk Framing Granularity** (definitional): -4 bps Higher Liquids, -6 bps Impact of lower rates, +6 bps Management actions/other — CBA/FY21/results_presentation PDF p29 (ev-1) vs -4 bps Higher Liquids, -2 bps Asset Pricing, -3 bps Deposit Pricing & Funding, -2 bps Capital & Other, +2 bps Portfolio Mix, +3 bps Basis Risk, +2 bps Treasury & Markets — CBA/FY21/results_presentation PDF p63 (ev-2)
  Preferred: ev-2. The presentation contains two walks for the same period. The P63 walk (ev-2) provides the detailed canonical driver breakdown used in the primary attribution table, while the P29 walk (ev-1) aggregates drivers into broader categories.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-29T03:34:38+00:00
- seconds: 83.8
- cost_usd: 0.002
- tokens: 39129 in / 6316 out
- orchestration: pipeline
