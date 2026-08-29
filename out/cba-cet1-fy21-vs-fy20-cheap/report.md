# CBA — cet1 — FY21 vs FY20

**Movement (cash basis):** 1160bps → 1310bps (+150bps) | **Attribution confidence:** 60/100

*Read from: row 'Common Equity Tier 1', column FY20 (Jun 20) -> column FY21 (Jun 21)*

CBA's APRA Level 2 CET1 ratio increased by 150 bps from 11.6% in FY20 to 13.1% in FY21. The bank did not publish a formal capital walk for this specific year-on-year comparison; the reported movement is derived from the endpoints. Quantified drivers are available only for the half-on-half period (Dec 20 to Jun 21) or as pro-forma adjustments.

### earnings_generation — "Organic Capital Generation"
*unquantified | confidence 80/100*

The bank describes 'strong organic capital generation' as the primary driver of the increase. A quantified figure of +97 bps is provided for Cash NPAT, but this belongs to the Dec 20-Jun 21 half-on-half walk (ev-1), not the full year comparison. No explicit bpts contribution for earnings is stated for the full year.
> [ev-1] CBA/FY21/results_presentation, printed p35: "[walk chart] CET1 of 13.1% – continued strong organic capital generation: Dec 20 Level 2¹ 1260 -> Jun 21 Level 2¹ 1310"
> [ev-4] CBA/FY21/profit_announcement, PDF p53: "The Group’s CET1 ratio (APRA) was 13.1% as at 30 June 2021, an increase of 50 basis points from 31 December 2020 and an increase of 150 basis points from 30 June 2020."
> [ev-17] CBA/FY21/results_presentation, printed p35: "CET1 of 13.1% - continued strong organic capital generation"

### dividend_net_drp — "Dividends paid"
*unquantified | confidence 60/100*


> [ev-2] CBA/FY21/results_presentation, printed p37: "[walk chart] CBA CET1 ratio in FY21 vs FY20: Jun 20 Level 2 1160 -> Jun 21 Level 2 Pro-forma 1215"

### capital_returns — "Off-market buy-back"
*unquantified | confidence 85/100*

An off-market buy-back occurred in FY21. The impact is stated as -133 bpts (ev-2). This bar appears in the pro-forma walk comparing Jun 20 to a pro-forma Jun 21 endpoint. It is excluded from the reported statutory CET1 of 13.1% (which excludes the buy-back impact per ev-16 context) and thus cannot be attributed to the reported movement.
> [ev-2] CBA/FY21/results_presentation, printed p37: "[walk chart] CBA CET1 ratio in FY21 vs FY20: Jun 20 Level 2 1160 -> Jun 21 Level 2 Pro-forma 1215"
> [ev-16] CBA/FY21/results_presentation, printed p13: "Pro-forma CET1 ratio calculated as Jun 21 CET1 ratio of 13.1% incorporating the impact of the off-market share buy-back (-133bpts)"

### rwa — "RWA"
*unquantified | confidence 60/100*

RWA movements contributed to the ratio change. A figure of +8 bps is provided for RWA in the Dec 20-Jun 21 walk (ev-1). No specific RWA bpts contribution is quantified for the full FY20-FY21 period in the provided evidence.
> [ev-1] CBA/FY21/results_presentation, printed p35: "[walk chart] CET1 of 13.1% – continued strong organic capital generation: Dec 20 Level 2¹ 1260 -> Jun 21 Level 2¹ 1310"

### regulatory_model_changes — "APRA Overlay Release"
*unquantified | confidence 60/100*

The release of the APRA overlay positively impacted capital. A figure of +17 bps is cited in the pro-forma walk (ev-2). As this walk uses a pro-forma endpoint, this specific bpts value is not confirmed as the exact contribution to the statutory reported movement.
> [ev-2] CBA/FY21/results_presentation, printed p37: "[walk chart] CBA CET1 ratio in FY21 vs FY20: Jun 20 Level 2 1160 -> Jun 21 Level 2 Pro-forma 1215"

### divestments_acquisitions — "Divestments"
*unquantified | confidence 60/100*

Divestments had a positive impact. A figure of +44 bps is cited in the pro-forma walk (ev-2). Like other bars in that walk, it is tied to a pro-forma endpoint and not explicitly broken out for the statutory movement.
> [ev-2] CBA/FY21/results_presentation, printed p37: "[walk chart] CBA CET1 ratio in FY21 vs FY20: Jun 20 Level 2 1160 -> Jun 21 Level 2 Pro-forma 1215"

## Source disagreements
- **Pro-forma vs Statutory Endpoint** (definitional): 12.15% (Pro-forma Jun 21, ev-2) vs 13.1% (Reported Jun 21, ev-4)
  Preferred: 13.1%. The task requires the movement against the reported statutory ratio. The walk on page 37 (ev-2) calculates a pro-forma ratio of 12.15% (or 1215 bps) which incorporates the buy-back. The reported ratio is 13.1%. Using the pro-forma walk's bars would attribute capital returns (buy-backs) to the statutory movement, which is incorrect.

## Limitations
- No formal capital walk was published for the FY20 to FY21 comparison. Only half-on-half (Dec 20-Jun 21) and pro-forma walks were provided.
- Quantified driver contributions (NPAT, Dividends, RWA, etc.) are only available for the half-on-half period or within the pro-forma context.
- The residual of 150 bps represents the total unattributed movement because no single document provides a reconciled breakdown of all drivers for the full year statutory movement.
- Failed check: no_quantified_drivers
- No published walk covers FY21 vs FY20: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-29T03:35:46+00:00
- seconds: 67.2
- cost_usd: 0.0022
- tokens: 47901 in / 5492 out
- orchestration: pipeline
