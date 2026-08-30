# CBA — cet1 — FY26 vs FY25

**Movement (cash basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 40/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 31 Dec 2025 -> column 30 Jun 2026*

CBA's CET1 ratio declined by 30 bps to 12.0% in FY26 from 12.3% in FY25. The bank does not publish a full capital walk for the FY25-FY26 period; only the half-on-half (Dec 25-Jun 26) walk is available. Consequently, specific driver contributions for the full year are unquantified.

> [ev-12] CBA/FY26/profit_announcement, PDF p48: "Common Equity Tier 1 (CET1) | 12.0 | 12.3 | 12.3"
> [ev-13] CBA/FY26/profit_announcement, PDF p48: "The Group’s CET1 Capital ratio was 12.0% as at 30 June 2026, a decrease of 30 basis points from 31 December 2025 and 30 June 2025."
> [ev-14] CBA/FY26/profit_announcement, PDF p120: "Common Equity Tier 1 12.0 12.3 12.3"

### earnings_generation — "Cash NPAT"
*unquantified | confidence 40/100*

The bank does not quantify the earnings contribution to the FY25-FY26 movement. For context, the Dec 25-Jun 26 walk shows Cash NPAT contributing +106 bps (ev-1).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CET1 ratio walk from Dec 25 Level 2 to Jun 26 Level 2: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-7] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

### dividend_net_drp — "Dividends net of DRP"
*unquantified | confidence 40/100*

The bank does not quantify the dividend impact on the FY25-FY26 movement. For context, the Dec 25-Jun 26 walk shows dividends net of DRP contributing -76 bps (ev-1).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CET1 ratio walk from Dec 25 Level 2 to Jun 26 Level 2: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-7] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

### rwa — "RWA"
*unquantified | confidence 40/100*

The bank does not quantify the RWA impact on the FY25-FY26 movement. For context, the Dec 25-Jun 26 walk shows RWA contributing -46 bps (ev-1).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CET1 ratio walk from Dec 25 Level 2 to Jun 26 Level 2: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-7] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

### deductions_other — "Other"
*unquantified | confidence 40/100*

The bank does not quantify the 'Other' impact on the FY25-FY26 movement. For context, the Dec 25-Jun 26 walk shows Other contributing -8 bps (ev-1).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CET1 ratio walk from Dec 25 Level 2 to Jun 26 Level 2: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-7] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

## Limitations
- No capital walk published for the FY25-FY26 comparison; only the half-on-half (Dec 25-Jun 26) walk is available.
- Driver contributions for the task period are unquantified and cannot be derived from the available evidence.
- Failed check: no_quantified_drivers
- No published walk covers FY26 vs FY25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T18:54:07+00:00
- seconds: 54.9
- cost_usd: 0.0024
- tokens: 59368 in / 4723 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY26/profit_announcement p49 <- p48 page 29']
