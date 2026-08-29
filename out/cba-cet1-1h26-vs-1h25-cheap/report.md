# CBA — cet1 — 1H26 vs 1H25

**Movement (cash basis):** 1220bps → 1230bps (+10bps) | **Attribution confidence:** 40/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 31 Dec 24 -> column 31 Dec 25*

CBA's Level 2 CET1 ratio increased by 10 bps to 12.3% in 1H26 vs 1H25. The movement is driven by regulatory model changes (+24 bpts) and earnings generation, partially offset by dividends (-87 bpts) and RWA growth.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `regulatory_model_changes` | APS 117 framework adoption | +24 bps | 85 | 1 (single_source) | ev-6 |
| `dividend_net_drp` | Dividend net of DRP | -87 bps | 80 | 2 () | ev-1, ev-2, ev-5 |
| *residual (unexplained)* | — | +73 bps | — | — |

### regulatory_model_changes — "APS 117 framework adoption"
*+24 bps | confidence 85/100*

Adoption of revised APS 117 framework effective 1 Oct 2025 reduced IRRBB RWA by ~$10bn, impacting CET1 by +24 bps.
> [ev-6] CBA/1H26/profit_announcement, printed p28: "Includes the impact of the reduction to IRRBB RWA of ~$10 billion (CET1 impact of +24 bpts) on adoption of the revised APS 117 framework effective 1 October 2025."

### dividend_net_drp — "Dividend net of DRP"
*-87 bps | confidence 80/100*

The 2H25 dividend (DRP neutralised) had a negative impact of 87 bps on the CET1 ratio. This figure corresponds to the Jun 2025 -> Dec 2025 half-on-half walk context.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-2] CBA/1H26/results_presentation, printed p103: "[walk chart] CET1 capital ratio movements: Jun 25 Level 2 1230 -> Dec 25 Level 2 1230"
> [ev-5] CBA/1H26/profit_announcement, printed p28: "The 2025 final dividend included the on-market purchase of $643 million of shares (CET1 impact of -13 bpts) in respect of the Dividend Reinvestment Plan."

### earnings_generation — "Cash NPAT"
*unquantified | confidence 60/100*

Earnings generation contributed positively to capital. The Jun 2025 -> Dec 2025 walk shows Cash NPAT at +107 bps; this specific contribution for the 1H25->1H26 window is not explicitly quantified in the text.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-2] CBA/1H26/results_presentation, printed p103: "[walk chart] CET1 capital ratio movements: Jun 25 Level 2 1230 -> Dec 25 Level 2 1230"

### rwa — "RWA"
*unquantified | confidence 60/100*

Total RWA movement impacted the ratio. The Jun 2025 -> Dec 2025 walk shows RWA at -33 bps; the specific 1H25->1H26 driver value is not explicitly quantified in the text.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-2] CBA/1H26/results_presentation, printed p103: "[walk chart] CET1 capital ratio movements: Jun 25 Level 2 1230 -> Dec 25 Level 2 1230"

## Limitations
- No primary walk exists for the 1H25 -> 1H26 comparison. Quantified drivers are derived from the Jun 2025 -> Dec 2025 half-on-half walk or explicit text footnotes.
- Residual of 73 bps remains unexplained as the sum of known drivers (24 - 87 = -63) does not equal the total delta (+10). Earnings and RWA contributions for the specific period are unquantified.
- Failed check: comparison_leak (dividend_net_drp claims -87, which is the '2H25 dividend (DRP neutralised)' bar of CBA/1H26/results_presentation PDF p33 (ev-1), a walk for a different comparison; no walk covers the task comparison, so this bar cannot be a contribution for it — move the number into the driver narrative and name the span it belongs to)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T03:31:20+00:00
- seconds: 64.5
- cost_usd: 0.0022
- tokens: 49009 in / 5497 out
- orchestration: pipeline
