# CBA — cet1 — 1H26 vs 1H25

**Movement (cash basis):** 1220bps → 1230bps (+10bps) | **Attribution confidence:** 60/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 31 Dec 24 -> column 31 Dec 25*

CBA's CET1 ratio increased by 10 bps to 12.3% in 1H26 vs 1H25. The bank did not publish a capital walk for this specific year-on-year comparison; the published half-on-half walk (Jun 25 -> Dec 25) shows offsetting drivers including +107 bps from earnings and -87 bps from dividends. Year-on-year movement is derived from endpoint levels.

### earnings_generation — "Cash NPAT"
*unquantified | confidence 60/100*

The bank does not quantify the year-on-year earnings contribution to CET1. The half-on-half walk (ev-1, ev-2) reports Cash NPAT at +107 bps for Jun 25 -> Dec 25.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-2] CBA/1H26/results_presentation, printed p103: "[walk chart] CET1 capital ratio movements: Jun 25 Level 2 1230 -> Dec 25 Level 2 1230"

### dividend_net_drp — "Dividend"
*unquantified | confidence 60/100*

The bank does not quantify the year-on-year dividend impact. The half-on-half walk (ev-1, ev-2) reports 2H25 dividend (DRP neutralised) at -87 bps for Jun 25 -> Dec 25.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-2] CBA/1H26/results_presentation, printed p103: "[walk chart] CET1 capital ratio movements: Jun 25 Level 2 1230 -> Dec 25 Level 2 1230"

### rwa — "RWA"
*unquantified | confidence 60/100*

The bank does not quantify the year-on-year RWA impact. The half-on-half walk (ev-1, ev-2) reports RWA at -33 bps for Jun 25 -> Dec 25.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-2] CBA/1H26/results_presentation, printed p103: "[walk chart] CET1 capital ratio movements: Jun 25 Level 2 1230 -> Dec 25 Level 2 1230"

## Limitations
- No capital walk was published for the 1H25 -> 1H26 comparison. Drivers are unquantified for this period.
- Movement delta calculated from endpoint levels (12.2% to 12.3%).
- Half-on-half walk bars (ev-1, ev-2) are context only and not attributed to 1H25->1H26.
- Failed check: no_quantified_drivers
- No published walk covers 1H26 vs 1H25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T17:48:42+00:00
- seconds: 60.6
- cost_usd: 0.0021
- tokens: 49880 in / 4731 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/1H26/profit_announcement p49 <- p48 page 29']
