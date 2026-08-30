# CBA — cet1 — FY26 vs FY25

**Movement (cash basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 40/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 30 Jun 25 -> column 30 Jun 26*

CBA's Level 2 CET1 ratio decreased by 30 bps to 12.0% in FY26 from 12.3% in FY25. The bank did not publish a full-year capital walk for this period; the published half-on-half walk shows earnings (+106 bps) and RWA (-46 bps) as primary drivers. For the full year, the net impact is unquantified due to missing H2 data.

> [ev-14] CBA/FY26/profit_announcement, PDF p48: "Common Equity Tier 1 (CET1) 12.0 12.3 12.3 (30)bpts (30)bpts"
> [ev-15] CBA/FY26/profit_announcement, PDF p48: "The Group’s CET1 Capital ratio was 12.0% as at 30 June 2026, a decrease of 30 basis points from 31 December 2025 and 30 June 2025."
> [ev-17] CBA/FY26/profit_announcement, PDF p120: "Common Equity Tier 1 12.0 12.3 12.3"
> [ev-23] CBA/FY26/results_presentation, printed p106: "Key capital ratios (%)1"

### earnings_generation — "Cash NPAT"
*unquantified | confidence 60/100*

The bank states 'Capital generated from earnings' was a key driver (ev-16). However, the only quantified figure is +106 bps for the first half (ev-1), which does not cover the full FY26 period.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-16] CBA/FY26/profit_announcement, PDF p48: "Key drivers of the change in CET1 for the 6 months ended 30 June 2026 were: • Capital generated from earnings; partly offset by • Payment of the 1H26 dividend; • Higher Credit Risk and IRRBB RWA, partly offset by lower Traded Market Risk RWA; and • Other regulatory adjustments and movement in reserves."

### dividend_net_drp — "Dividend"
*unquantified | confidence 60/100*

The bank cites 'Payment of the 1H26 dividend' as a driver (ev-16). The quantified impact of -76 bps applies only to the first half (ev-1). The second half dividend impact is not disclosed.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-16] CBA/FY26/profit_announcement, PDF p48: "Key drivers of the change in CET1 for the 6 months ended 30 June 2026 were: • Capital generated from earnings; partly offset by • Payment of the 1H26 dividend; • Higher Credit Risk and IRRBB RWA, partly offset by lower Traded Market Risk RWA; and • Other regulatory adjustments and movement in reserves."

### rwa — "RWA"
*unquantified | confidence 60/100*

The bank notes 'Higher Credit Risk and IRRBB RWA' offset by 'lower Traded Market Risk RWA' (ev-16). Quantified sub-components (-38, -16, +8 bps) are provided only for the first half (ev-19).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-16] CBA/FY26/profit_announcement, PDF p48: "Key drivers of the change in CET1 for the 6 months ended 30 June 2026 were: • Capital generated from earnings; partly offset by • Payment of the 1H26 dividend; • Higher Credit Risk and IRRBB RWA, partly offset by lower Traded Market Risk RWA; and • Other regulatory adjustments and movement in reserves."
> [ev-19] CBA/FY26/results_presentation, printed p32: "Movements in bpts"

### deductions_other — "Other"
*unquantified | confidence 60/100*

The bank lists 'Other regulatory adjustments and movement in reserves' (ev-16). A quantified impact of -8 bps is reported for the first half only (ev-1).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-16] CBA/FY26/profit_announcement, PDF p48: "Key drivers of the change in CET1 for the 6 months ended 30 June 2026 were: • Capital generated from earnings; partly offset by • Payment of the 1H26 dividend; • Higher Credit Risk and IRRBB RWA, partly offset by lower Traded Market Risk RWA; and • Other regulatory adjustments and movement in reserves."

## Source disagreements
- **Period Mismatch** (timing): -30 bps (FY25 vs FY26, ev-14) vs -30 bps (Dec 25 vs Jun 26, ev-1)
  Preferred: FY25 vs FY26. The bank's published capital walk covers Dec 2025 to Jun 2026. While the delta matches the FY25-FY26 change numerically, the drivers inside the walk apply only to the H1 period.

## Limitations
- No full-year capital walk is published for FY26 vs FY25.
- All quantified driver contributions (-76, +106, -46, -8 bps) relate to the half ended Dec 2025 -> Jun 2026.
- Second half movements are unquantified.
- Failed check: no_quantified_drivers
- No published walk covers FY26 vs FY25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T12:36:09+00:00
- seconds: 64.5
- cost_usd: 0.0023
- tokens: 57184 in / 4467 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY26/profit_announcement p49 <- p48 page 29']
