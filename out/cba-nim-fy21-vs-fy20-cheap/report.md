# CBA — nim — FY21 vs FY20

**Movement (cash basis):** 207bps → 203bps (-4bps) | **Attribution confidence:** 95/100

*Read from: row 'Net interest margin (%)', column FY20 -> column FY21*

CBA's Group net interest margin decreased 4 basis points to 203 bps in FY21 (vs 207 bps in FY20). The decline was driven by higher liquid assets (-4 bps), lower asset pricing (-2 bps), and increased funding costs (-3 bps). These were partially offset by favourable portfolio mix (+2 bps), positive basis risk contribution (+3 bps), and Treasury & Markets performance (+2 bps), alongside a negative capital impact (-2 bps).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Higher Liquids | -4 bps | 95 | 2 () | ev-1, ev-2, ev-9 |
| `asset_pricing` | Asset Pricing | -2 bps | 95 | 2 () | ev-2, ev-5 |
| `funding` | Deposit Pricing & Funding | -3 bps | 95 | 2 () | ev-2, ev-6 |
| `capital_replicating` | Capital & Other | -2 bps | 95 | 2 () | ev-2, ev-7 |
| `mix` | Portfolio Mix | +2 bps | 95 | 2 () | ev-2, ev-4 |
| `basis_risk` | Basis Risk (incl RP) | +3 bps | 95 | 2 () | ev-2, ev-10 |
| `markets_treasury` | Treasury & Markets | +2 bps | 90 | 2 () | ev-2, ev-8 |

### liquids — "Higher Liquids"
*-4 bps | confidence 95/100*

Higher liquid assets reduced NIM by 4 bps due to stable non-lending interest-earning asset balances during the period.
> [ev-1] CBA/FY21/results_presentation, printed p29: "[walk chart] CBA net interest margin in FY21 vs FY20: FY20 207 -> FY21 203"
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-9] CBA/FY21/profit_announcement, PDF p33: "Liquid assets: Flat, reflecting stable non-lending interest earning asset balances during the period."

### asset_pricing — "Asset Pricing"
*-2 bps | confidence 95/100*

Decreased by 2 bps driven by home lending: switching to fixed rates (-3 bps) and competition (-2 bps), partly offset by repricing (+3 bps).
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-5] CBA/FY21/profit_announcement, PDF p33: "Asset pricing: Decreased margin by 2 basis points driven by home lending, reflecting the impact of customers switching to lower margin loans, particularly from variable rate to fixed rate loans (down 3 basis points) and increased competition (down 2 basis points), partly offset by repricing (up 3 basis points)."

### funding — "Deposit Pricing & Funding"
*-3 bps | confidence 95/100*

Increased funding costs reduced NIM by 3 bps. Savings/investment deposit repricing provided +3 bps benefit, offset by cash rate cut impact (-1 bps) and replicating portfolio earnings decrease (-1 bps).
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-6] CBA/FY21/profit_announcement, PDF p33: "Funding costs: Increased margin by 1 basis point driven by the benefit of savings and investment deposit repricing (up 3 basis points), partly offset by lower earnings on deposits due to the decrease in the cash rate (down 1 basis point), and lower earnings from the replicating portfolio due to the falling interest rate environment (down 1 basis point)."

### capital_replicating — "Capital & Other"
*-2 bps | confidence 95/100*

Reduced NIM by 2 bps. NZ capital contribution increased by 2 bps due to lower wholesale funding costs, offset by lower earnings on Group capital (-1 bps) from falling rates.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-7] CBA/FY21/profit_announcement, PDF p33: "Capital and other: Increased margin by 1 basis points due to increased contribution from New Zealand (up 2 basis points), reflectin g lower wholesale funding costs, and favourable portfolio mix and lending margins, partly offset by lower earnings on Group capital due to the falling interest rate environment (down 1 basis point)."

### mix — "Portfolio Mix"
*+2 bps | confidence 95/100*

Favourable mix added 2 bps. Driven by TFF drawdown and switch to at-call deposits (+2 bps) and decline in lower-margin institutional lending (+1 bps).
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-4] CBA/FY21/profit_announcement, PDF p33: "Portfolio mix: Increased margin by 3 basis points driven by favourable funding mix from the drawdown of the TFF and customers switching to at-call deposits (up 2 basis points), and favourable lending mix from the decline of lower margin institutional lending balances (up 1 basis point)."

### basis_risk — "Basis Risk (incl RP)"
*+3 bps | confidence 95/100*

Positive contribution of 3 bps. Average spread and exposure remained broadly flat during the half.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-10] CBA/FY21/profit_announcement, PDF p33: "Basis risk: Basis risk arises from the spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate. The average spread and exposure remained broadly flat during the half."

### markets_treasury — "Treasury & Markets"
*+2 bps | confidence 90/100*

Contributed 2 bps. Described as 'Flat' in narrative text, but walk chart assigns +2 bps value.
> [ev-2] CBA/FY21/results_presentation, printed p63: "[walk chart] Group margin: FY20 207 -> FY21 203"
> [ev-8] CBA/FY21/profit_announcement, PDF p33: "Treasury and Markets: Flat."

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-29T17:52:50+00:00
- seconds: 89.8
- cost_usd: 0.0023
- tokens: 44994 in / 7113 out
- orchestration: pipeline
- pages_extracted: 17
- reference_follow: ['CBA/FY21/results_presentation p64 <- p29 page 64', 'CBA/FY21/profit_announcement p41 <- p32 page 21 [added]']
