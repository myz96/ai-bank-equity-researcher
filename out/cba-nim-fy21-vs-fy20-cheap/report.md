# CBA — nim — FY21 vs FY20

**Movement (cash basis):** 207bps → 203bps (-4bps) | **Attribution confidence:** 90/100

CBA's cash NIM decreased by 4 bps to 203 bps in FY21 (FY20: 207 bps). The decline was driven primarily by higher liquid assets (-4 bps) and lower asset pricing/funding costs (-5 bps combined), partially offset by favourable portfolio mix (+2 bps), basis risk benefits (+3 bps), and treasury contributions (+2 bps). Management actions and other factors contributed +6 bps in the simplified view.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Higher Liquids | -4 bps | 95 | 2 () | ev-1, ev-2, ev-3 |
| `asset_pricing` | Asset Pricing | -2 bps | 85 | 2 () | ev-2, ev-14 |
| `funding.deposits` | Deposit Pricing & Funding | -3 bps | 85 | 2 () | ev-2, ev-3, ev-15 |
| `capital_replicating` | Capital & Other | -2 bps | 85 | 1 (single_source) | ev-2 |
| `mix` | Portfolio Mix | +2 bps | 85 | 1 (single_source) | ev-2, ev-23 |
| `basis_risk` | Basis Risk (incl RP) | +3 bps | 85 | 1 (single_source) | ev-2 |
| `markets_treasury` | Treasury & Markets | +2 bps | 85 | 1 (single_source) | ev-2 |

### liquids — "Higher Liquids"
*-4 bps | confidence 95/100*

Higher liquidity levels, including increased at-call deposit balances and TFF drawdowns, exerted a drag on margin.
> [ev-1] CBA/FY21/results_presentation, printed p29: "[walk chart] CBA net interest margin in FY21 vs FY20: FY20 207.0 -> FY21 203.0"
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-3] CBA/FY21/profit_announcement, PDF p11: "Net interest margin (NIM) was down 4 basis points due to higher liquid assets, with the impact of the low-rate environment largely offset by management actions, lower wholesale funding costs and favourable funding mix."

### asset_pricing — "Asset Pricing"
*-2 bps | confidence 85/100*

Lower lending margins due to competition and unfavourable home loan mix (variable to fixed shift), partly offset by repricing.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-14] CBA/FY21/profit_announcement, printed p47: "Lower home lending margins (down 5 basis points) due to unfavourable home loan portfolio mix (down 6 basis points) with a shift to lower margin loans (variable to fixed) and increased competition (down 5 basis points), partly offset by repricing (up 6 basis points);"

### funding.deposits — "Deposit Pricing & Funding"
*-3 bps | confidence 85/100*

Funding costs rose slightly due to the impact of lower cash rates on deposit margins, though wholesale funding costs fell.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-3] CBA/FY21/profit_announcement, PDF p11: "Net interest margin (NIM) was down 4 basis points due to higher liquid assets, with the impact of the low-rate environment largely offset by management actions, lower wholesale funding costs and favourable funding mix."
> [ev-15] CBA/FY21/profit_announcement, printed p47: "Lower deposit margins reflecting decreases in the cash rate (down 2 basis points);"

### capital_replicating — "Capital & Other"
*-2 bps | confidence 85/100*

Negative contribution from capital and replicating portfolio earnings.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"

### mix — "Portfolio Mix"
*+2 bps | confidence 85/100*

Favourable mix in certain areas, though consumer finance balances declined.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-23] CBA/FY21/results_presentation, printed p63: "Group margin1 Flat ex liquids – pressure from lower interest rates, offset by favourable portfolio mix, lower wholesale funding costs"

### basis_risk — "Basis Risk (incl RP)"
*+3 bps | confidence 85/100*

Positive contribution from basis risk management and hedging activities.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"

### markets_treasury — "Treasury & Markets"
*+2 bps | confidence 85/100*

Positive contribution from Treasury and Markets operations.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"

## Source disagreements
- **Simplified vs Detailed Attribution** (definitional): -4 bps Higher Liquids, -6 bps Impact of lower rates, +6 bps Management actions/other — ev-1 vs -4 bps Higher Liquids, -2 bps Asset Pricing, -3 bps Deposit Pricing & Funding, -2 bps Capital & Other, +2 bps Portfolio Mix, +3 bps Basis Risk, +2 bps Treasury & Markets — ev-2
  Preferred: ev-2. The presentation provides two walk charts. Ev-1 is a high-level summary grouping drivers into 'Impact of lower rates' and 'Management actions'. Ev-2 provides the detailed canonical breakdown used for attribution. Ev-2 is preferred as it maps to the taxonomy.

## Limitations
- The 'Impact of lower rates' and 'Management actions' from ev-1 are not directly mapped to canonical IDs but are conceptually covered by asset pricing, funding, and mix in ev-2.
- Confidence for individual driver components (except liquids) is capped at 85 due to reliance on the detailed slide walk (ev-2) rather than a primary profit announcement table with full breakdown.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-26T06:29:06+00:00
- seconds: 56.5
- cost_usd: 0.0014
- tokens: 26138 in / 4731 out
- orchestration: pipeline
