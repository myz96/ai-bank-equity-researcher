# CBA — cet1 — FY26 vs FY25

**Movement (statutory basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 60/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 30 Jun 25 -> column 30 Jun 26*

CBA's statutory CET1 ratio declined by 30 bps to 12.0% in FY26 from 12.3% in FY25. The bank did not publish a full-year capital walk for this period; the published half-on-half walk shows earnings (+106 bps) and RWA (-46 bps) as primary drivers.

### earnings_generation — "Cash NPAT"
*unquantified | confidence 60/100*

Unquantified for FY26 vs FY25. The published half-on-half walk (Dec 25 -> Jun 26) attributes +106 bps to Cash NPAT (ev-1, ev-2). No specific full-year driver value is provided.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

### dividend_net_drp — "1H26 dividend (DRP neutralised)"
*unquantified | confidence 60/100*

Unquantified for FY26 vs FY25. The published half-on-half walk (Dec 25 -> Jun 26) attributes -76 bps to dividends (ev-1, ev-2). A -10 bps impact from DRP buybacks is noted (ev-9), but total FY26 dividend impact is not explicitly stated.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-9] CBA/FY26/results_presentation, printed p32: "The 2026 interim dividend included the on-market purchase of $530 million of shares (CET1 impact of -10bpts) in respect of the Dividend Reinvestment Plan."

### rwa.credit — "RWA"
*unquantified | confidence 60/100*

Unquantified for FY26 vs FY25. The published half-on-half walk (Dec 25 -> Jun 26) attributes -46 bps to RWA (ev-1, ev-2). Credit risk movement within that period was -38 bps (ev-8).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-8] CBA/FY26/results_presentation, printed p32: "Movements in bpts Credit Risk4 (38) IRRBB (16) Market Risk 8 Operational Risk - 3"

### deductions_other — "Other"
*unquantified | confidence 60/100*

Unquantified for FY26 vs FY25. The published half-on-half walk (Dec 25 -> Jun 26) attributes -8 bps to Other items (ev-1, ev-2).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

## Limitations
- The bank only published a capital walk for the half ended Dec 2025 (context comparison). No full-year (FY25 vs FY26) capital walk or driver breakdown was available in the source documents.
- Failed check: no_quantified_drivers
- No published walk covers FY26 vs FY25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-28T12:17:39+00:00
- seconds: 65.1
- cost_usd: 0.0018
- tokens: 42415 in / 3740 out
- orchestration: pipeline
