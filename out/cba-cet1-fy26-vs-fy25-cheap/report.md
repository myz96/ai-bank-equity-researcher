# CBA — cet1 — FY26 vs FY25

**Movement (cash basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 40/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 30 Jun 25 -> column 30 Jun 26*

CBA's Level 2 CET1 ratio decreased by 30 bps to 12.0% in FY26 from 12.3% in FY25. The bank did not publish a full capital walk for this specific year-on-year comparison; the published walk covers the half-on-half period (Dec 2025 to Jun 2026). Consequently, while the total movement is known, the specific driver contributions for the full year are unquantified in the provided evidence.

### dividend_net_drp — "1H26 dividend (DRP neutralised)"
*unquantified | confidence 40/100*

The bank states a 76 bps negative impact from dividends net of DRP, but this figure is explicitly part of the Dec 2025 to Jun 2026 half-on-half walk (ev-1, ev-2), not the FY25-FY26 comparison.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

### earnings_generation — "Cash NPAT"
*unquantified | confidence 40/100*

The bank reports a 106 bps positive contribution from Cash NPAT, but this is also restricted to the Dec 2025 to Jun 2026 half-on-half walk (ev-1, ev-2) and cannot be attributed to the full year movement.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

### rwa — "RWA"
*unquantified | confidence 40/100*

A 46 bps negative impact from RWA is noted, but this belongs to the Dec 2025 to Jun 2026 half-on-half walk (ev-1, ev-2), not the FY25-FY26 comparison.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

### deductions_other — "Other"
*unquantified | confidence 40/100*

An 8 bps negative impact from Other items is reported, but this is part of the Dec 2025 to Jun 2026 half-on-half walk (ev-1, ev-2), not the FY25-FY26 comparison.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

## Source disagreements
- **Walk Comparison Span** (definitional): -30 bps: stated vs FY25 (ev-3, ev-4) vs -8 bps: Dec 2025 -> Jun 2026 (ev-7)
  Preferred: -30 bps. The task requires the FY25 to FY26 movement (-30 bps). The detailed driver breakdowns provided in the presentation (ev-1, ev-2, ev-7) cover the half-on-half period (Dec 2025 to Jun 2026), which is a different comparison.

## Limitations
- The bank did not publish a capital walk for the FY25 to FY26 comparison. All available driver quantifications (ev-1, ev-2) apply to the Dec 2025 to Jun 2026 half-on-half period.
- Driver contributions for the full year are therefore unquantified based on the provided evidence.
- Failed check: no_quantified_drivers
- No published walk covers FY26 vs FY25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T20:55:33+00:00
- seconds: 58.5
- cost_usd: 0.0021
- tokens: 50398 in / 4532 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY26/profit_announcement p49 <- p48 page 29']
