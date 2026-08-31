# CBA — cet1 — FY26 vs FY25

**Movement (cash basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 40/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 31 Dec 25 -> column 30 Jun 26*

CBA's CET1 ratio declined by 30 bps to 12.0% in FY26 from 12.3% in FY25. The bank does not publish a capital walk for this specific period; the published half-on-half walk shows organic earnings (+106 bps) offset by dividends (-76 bps) and RWA movements (-46 bps).

> [ev-14] CBA/FY26/profit_announcement, PDF p48: "Common Equity Tier 1 (CET1) 12.0 12.3 12.3 (30)bpts (30)bpts"
> [ev-15] CBA/FY26/profit_announcement, PDF p48: "The Group’s CET1 Capital ratio was 12.0% as at 30 June 2026, a decrease of 30 basis points from 31 December 2025 and 30 June 2025."
> [ev-16] CBA/FY26/profit_announcement, PDF p120: "Common Equity Tier 1 12.0 12.3 12.3"

### earnings_generation — "Cash NPAT"
*unquantified | confidence 40/100*

The bank does not quantify the FY26 vs FY25 contribution. The half-on-half walk (Dec 25 -> Jun 26) reports Cash NPAT at +106 bps (ev-1, ev-6).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CET1 ratio walk: Dec 25 Level 2 to Jun 26 Level 2: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-6] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

### dividend_net_drp — "1H26 dividend (DRP neutralised)"
*unquantified | confidence 40/100*

The bank does not quantify the FY26 vs FY25 contribution. The half-on-half walk (Dec 25 -> Jun 26) reports the interim dividend impact at -76 bps (ev-1, ev-6).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CET1 ratio walk: Dec 25 Level 2 to Jun 26 Level 2: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-6] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

### rwa — "RWA"
*unquantified | confidence 40/100*

The bank does not quantify the FY26 vs FY25 contribution. The half-on-half walk (Dec 25 -> Jun 26) reports total RWA movement at -46 bps (ev-1, ev-6).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CET1 ratio walk: Dec 25 Level 2 to Jun 26 Level 2: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-6] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

### deductions_other — "Other"
*unquantified | confidence 40/100*

The bank does not quantify the FY26 vs FY25 contribution. The half-on-half walk (Dec 25 -> Jun 26) reports Other impacts at -8 bps (ev-1, ev-6).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CET1 ratio walk: Dec 25 Level 2 to Jun 26 Level 2: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-6] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

## Limitations
- No capital walk is published for the FY25 -> FY26 comparison. All driver values are borrowed from the Dec 25 -> Jun 26 half-on-half walk and cannot be attributed to the task period.
- Failed check: no_quantified_drivers
- No published walk covers FY26 vs FY25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-31T00:49:52+00:00
- seconds: 52.1
- cost_usd: 0.0022
- tokens: 56861 in / 4102 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY26/profit_announcement p49 <- p48 page 29']
