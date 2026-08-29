# CBA — cet1 — 1H26 vs 1H25

**Movement (cash basis):** 1260bps → 1230bps (-30bps) | **Attribution confidence:** 40/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 31 Dec 24 -> column 31 Dec 25*

CBA's Level 2 CET1 ratio declined by 30 bps to 12.3% in 1H26 vs 1H25. The bank published no capital walk for this specific period; the available half-on-half walk (Jun 25 -> Dec 25) is context only and cannot be attributed to the year-over-year movement.

### earnings_generation — "Cash NPAT"
*unquantified | confidence 60/100*

Unquantified for 1H26 vs 1H25. The Jun 25 -> Dec 25 walk shows +107 bps (ev-1). No text quantifies the YoY earnings impact.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital Movements in bpts: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-3] CBA/1H26/profit_announcement, printed p28: "Common Equity Tier 1 (CET1) 12.3 12.3 12.2 – 10 bpts"

### dividend_net_drp — "Dividend"
*unquantified | confidence 60/100*

Unquantified for 1H26 vs 1H25. The Jun 25 -> Dec 25 walk shows -87 bps (ev-1). No text quantifies the YoY dividend impact.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital Movements in bpts: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-3] CBA/1H26/profit_announcement, printed p28: "Common Equity Tier 1 (CET1) 12.3 12.3 12.2 – 10 bpts"

### rwa.credit — "RWA"
*unquantified | confidence 60/100*

Unquantified for 1H26 vs 1H25. The Jun 25 -> Dec 25 walk shows -33 bps (ev-1). No text quantifies the YoY RWA impact.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital Movements in bpts: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-3] CBA/1H26/profit_announcement, printed p28: "Common Equity Tier 1 (CET1) 12.3 12.3 12.2 – 10 bpts"

### deductions_other — "Other"
*unquantified | confidence 60/100*

Unquantified for 1H26 vs 1H25. The Jun 25 -> Dec 25 walk shows +9 bps (ev-1). No text quantifies the YoY other impact.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital Movements in bpts: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-3] CBA/1H26/profit_announcement, printed p28: "Common Equity Tier 1 (CET1) 12.3 12.3 12.2 – 10 bpts"

## Limitations
- The bank did not publish a capital walk for the 1H25 -> 1H26 comparison. Only the half-on-half (Jun 25 -> Dec 25) walk is available (ev-1, ev-2), which is explicitly excluded from driver attribution per instructions.
- Drivers are unquantified for the requested period; the residual equals the total delta.
- Failed check: no_quantified_drivers
- No published walk covers 1H26 vs 1H25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-28T12:40:47+00:00
- seconds: 206.8
- cost_usd: 0.0021
- tokens: 48139 in / 5146 out
- orchestration: pipeline
