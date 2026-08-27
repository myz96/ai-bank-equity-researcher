# CBA — cet1 — 1H26 vs 1H25

**Movement (statutory basis):** 1530bps → 1510bps (-20bps) | **Attribution confidence:** 40/100

CBA's CET1 ratio declined by 20 bps in 1H26 to 15.1% (from 15.3% in 1H25). The decline is primarily driven by dividend distributions and RWA growth, partially offset by earnings generation. No period-matching walk chart was available for this specific comparison; the analysis relies on point-in-time data from the Profit Announcement and Presentation.

### dividend_net_drp — "Dividend"
*unquantified | confidence 60/100*

Dividends reduced CET1. While a specific 1H26 net DRP figure is not provided in the evidence, the 2H25 final dividend included a $643m share purchase impacting CET1 by -13 bps (ev-5). Full year or H1 specific net impact is not quantified in the provided records.
> [ev-5] CBA/1H26/profit_announcement, printed p28: "The 2025 final dividend included the on-market purchase of $643 million of shares (CET1 impact of -13 bpts) in respect of the Dividend Reinvestment Plan."

### rwa.credit — "RWA"
*unquantified | confidence 60/100*

RWA movements impacted CET1. The 2H25 period saw a -33 bps impact from RWA (ev-1), but no specific 1H26 RWA contribution is quantified in the provided evidence for the 1H25 vs 1H26 comparison.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] CET1 ratio movement Jun 25 to Dec 25: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"

### earnings_generation — "Cash NPAT"
*unquantified | confidence 60/100*

Earnings generated capital. Cash NPAT contributed +107 bps in 2H25 (ev-1). No specific 1H26 earnings contribution to the CET1 ratio movement is quantified in the provided evidence.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] CET1 ratio movement Jun 25 to Dec 25: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"

## Source disagreements
- **Period Mismatch of Walk Charts** (timing): -87 bps (ev-1, ev-2): 2H25 movement vs -20 bps (ev-10): 1H26 vs 1H25 movement
  Preferred: 1H26 vs 1H25 Movement. The provided walk charts (ev-1, ev-2) describe the movement from Jun 25 to Dec 25 (2H25). The task requires 1H26 vs 1H25. The only direct evidence for the requested period is the point-in-time CET1 ratios in ev-10.

## Limitations
- No walk chart specifically detailing the drivers for the 1H26 vs 1H25 CET1 movement was provided in the evidence records.
- Quantified driver contributions are unavailable for the 1H26 period; only 2H25 drivers are present in the walk charts.
- Attribution relies on point-in-time ratio changes without a corresponding driver breakdown for the specific half-year comparison.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-27T07:41:01+00:00
- seconds: 63.3
- cost_usd: 0.0016
- tokens: 34798 in / 3921 out
- orchestration: pipeline
