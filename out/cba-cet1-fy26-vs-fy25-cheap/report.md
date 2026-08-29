# CBA — cet1 — FY26 vs FY25

**Movement (cash basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 60/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 30 Jun 25 -> column 30 Jun 26*

CBA's Level 2 CET1 ratio decreased by 30 bps to 12.0% in FY26 (from 12.3% in FY25). The bank does not publish a full capital walk for this specific year-on-year comparison; the available presentation slides cover the half-on-half period (Dec 2025 to Jun 2026) and cannot be used as drivers for the FY26 vs FY25 movement.

### earnings_generation — "Cash NPAT"
*unquantified | confidence 60/100*

The bank states that strong capital position was maintained supporting franchise growth and dividends. No quantified earnings contribution is provided for the FY26 vs FY25 window.
> [ev-6] CBA/FY26/results_presentation, printed p32: "Strong capital position maintained, supporting franchise growth and dividends"

### dividend_net_drp — "Dividend"
*unquantified | confidence 60/100*

No quantified dividend impact is disclosed for the FY26 vs FY25 window. The presentation slide shows a -76 bpts impact from the 1H26 interim dividend (DRP neutralised), but this applies to the Dec 2025 -> Jun 2026 half-on-half period.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230.0 -> Jun 26 Level 2 1200.0"
> [ev-15] CBA/FY26/results_presentation, printed p32: "1H26 dividend (DRP neutralised) (8)"

### rwa — "RWA"
*unquantified | confidence 60/100*

No quantified RWA impact is disclosed for the FY26 vs FY25 window. The presentation slide shows a -46 bpts impact on CET1 from RWA movements, but this applies to the Dec 2025 -> Jun 2026 half-on-half period.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230.0 -> Jun 26 Level 2 1200.0"
> [ev-12] CBA/FY26/results_presentation, printed p32: "RWA 40"

### deductions_other — "Other"
*unquantified | confidence 60/100*

No quantified 'Other' impact is disclosed for the FY26 vs FY25 window. The presentation slide shows an -8 bpts impact, but this applies to the Dec 2025 -> Jun 2026 half-on-half period.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230.0 -> Jun 26 Level 2 1200.0"
> [ev-13] CBA/FY26/results_presentation, printed p32: "Other (76)"

## Source disagreements
- **Capital Walk Period Mismatch** (definitional): -30 bps stated change (FY25->FY26, ev-4) vs -46 bps total movement (Dec 25->Jun 26, ev-7)
  Preferred: -30 bps stated change (FY25->FY26, ev-4). The task requires the FY26 vs FY25 movement. The profit announcement explicitly states a 30 bps decrease for this period. The presentation slides provide a different walk for the half-on-half period (Dec 2025 to Jun 2026), which sums to -46 bps. These are distinct comparisons.

## Limitations
- The bank did not publish a capital walk for the FY26 vs FY25 comparison. All quantified driver bars in the results presentation (ev-1, ev-2) apply to the half-on-half period (Dec 2025 to Jun 2026) and were excluded from the driver table per instructions.
- Driver contributions are unquantified due to lack of period-matching evidence.
- Failed check: no_quantified_drivers
- No published walk covers FY26 vs FY25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T18:03:18+00:00
- seconds: 65.3
- cost_usd: 0.0019
- tokens: 46440 in / 3930 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY26/profit_announcement p49 <- p48 page 29']
