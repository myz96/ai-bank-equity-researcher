# CBA — nim — FY21 vs FY20

**Movement (cash basis):** 207bps → 203bps (-4bps) | **Attribution confidence:** 90/100

CBA's Group NIM decreased by 4 basis points to 203 bps in FY21 (FY20: 207 bps). The decline was primarily driven by higher liquid assets (-4 bps) and lower asset pricing (-2 bps), reflecting competitive pressures and COVID-19 support measures. These were partially offset by favorable portfolio mix (+2 bps) and basis risk benefits (+3 bps). Funding costs also weighed on margin (-3 bps) due to the cash rate environment.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Higher Liquids | -4 bps | 95 | 2 () | ev-2, ev-7 |
| `asset_pricing` | Asset Pricing | -2 bps | 95 | 2 () | ev-2, ev-8 |
| `funding` | Deposit Pricing & Funding | -3 bps | 95 | 2 () | ev-2, ev-10 |
| `capital_replicating` | Capital & Other | -2 bps | 85 | 1 (single_source) | ev-2 |
| `mix` | Portfolio Mix | +2 bps | 85 | 1 (single_source) | ev-2 |
| `basis_risk` | Basis Risk (incl RP) | +3 bps | 85 | 1 (single_source) | ev-2 |
| `markets_treasury` | Treasury & Markets | +2 bps | 85 | 1 (single_source) | ev-2 |

### liquids — "Higher Liquids"
*-4 bps | confidence 95/100*

Increased lower-yielding non-lending interest-earning assets, including liquid assets, reduced margin by 4 bps. This is consistent across both the Profit Announcement and Results Presentation walks.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-7] CBA/FY21/profit_announcement, printed p12: "Liquid assets: Decreased margin by 4 basis points driven by increased lower yielding non-lending interest earning assets, including liquid assets."

### asset_pricing — "Asset Pricing"
*-2 bps | confidence 95/100*

Lower business lending margins (-1 bps) from repricing actions to support businesses during COVID-19, and lower consumer finance margins (-1 bps) from a reduction in interest-earning credit card balances.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-8] CBA/FY21/profit_announcement, printed p12: "Asset pricing: Decreased margin by 2 basis points driven by lower business lending margins (down 1 basis point) from repricing actions to support businesses during COVID-19, and lower consumer finance margins (down 1 basis point) from a reduction in the proportion of interest earning credit card balances."

### funding — "Deposit Pricing & Funding"
*-3 bps | confidence 95/100*

Decreased margin by 3 bps, reflecting lower earnings on transaction and savings deposits mainly due to decreases in the cash rate (-7 bps), partly offset by higher benefits from the replicating portfolio (+2 bps) and lower wholesale funding costs (+2 bps).
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-10] CBA/FY21/profit_announcement, printed p12: "Funding costs: Decreased margin by 3 basis points, reflecting lower earnings on transaction and savings deposits mainly due to decreases in the cash rate (down 7 basis points), partly offset by higher benefits from the replicating portfolio (up 2 basis points) and lower wholesale funding costs (up 2 basis points)."

### capital_replicating — "Capital & Other"
*-2 bps | confidence 85/100*

Included in the 'Capital & Other' category in the detailed walk. Likely reflects lower earnings on equity or capital management impacts in the low-rate environment.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"

### mix — "Portfolio Mix"
*+2 bps | confidence 85/100*

Favorable portfolio mix contributed +2 bps. This likely reflects the benefit from customers switching to at-call deposits from investment deposits, as noted in the half-year context, though the full-year narrative emphasizes unfavorable mix in some sections, the walk explicitly attributes +2 bps here.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"

### basis_risk — "Basis Risk (incl RP)"
*+3 bps | confidence 85/100*

Basis risk (including replicating portfolio) contributed +3 bps. This positive impact likely stems from the widening of bills/OIS spreads or favorable hedging outcomes in the falling rate environment.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"

### markets_treasury — "Treasury & Markets"
*+2 bps | confidence 85/100*

Markets and Treasury contribution added +2 bps to the margin.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"

## Source disagreements
- **NIM Level and Change Definition** (definitional): -4 bps change (207->203) — CBA/FY21/profit_announcement (ev-5, ev-6, ev-13, ev-14) vs +3 bps change (H2 FY20->H1 FY21) — CBA/FY21/profit_announcement (ev-3, ev-4)
  Preferred: -4 bps change (207->203). The task requires FY21 vs FY20 comparison. Evidence ev-3 and ev-4 describe the Half-Year comparison (prior half to current half), which is a different period. The FY21 vs FY20 comparison is consistently reported as a 4 bps decrease from 207 bps to 203 bps in ev-5, ev-6, ev-13, and ev-14.
- **Walk Granularity** (definitional): Simplified Walk: Higher Liquids (-4), Impact of lower rates (-6), Management actions/other (+6) — CBA/FY21/results_presentation (ev-1) vs Detailed Walk: Higher Liquids (-4), Asset Pricing (-2), Deposit Pricing & Funding (-3), Capital & Other (-2), Portfolio Mix (+2), Basis Risk (+3), Treasury & Markets (+2) — CBA/FY21/results_presentation (ev-2)
  Preferred: Detailed Walk. Per source hierarchy and method, the more granular walk (ev-2) provides specific canonical driver attributions that map better to the taxonomy. The simplified walk (ev-1) aggregates drivers into broader categories like 'Impact of lower rates' and 'Management actions/other', which are less precise for attribution.

## Limitations
- The 'Capital & Other' and 'Treasury & Markets' drivers are less explicitly detailed in the narrative text compared to Liquids, Asset Pricing, and Funding. Their values are taken directly from the detailed walk chart (ev-2).
- There is a discrepancy in the narrative description of 'Portfolio Mix' between the half-year context (favorable) and some full-year narrative snippets (unfavorable), but the walk explicitly assigns +2 bps to this driver for the FY21 vs FY20 movement.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-27T07:44:42+00:00
- seconds: 83.3
- cost_usd: 0.0019
- tokens: 32049 in / 7084 out
- orchestration: pipeline
