# CBA — cet1 — FY26 vs FY25

**Movement (cash basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 40/100

*Read from: row 'Common Equity Tier 1', column 30 Jun 25 -> column 30 Jun 26*

CBA's CET1 ratio declined by 30 bps to 12.0% in FY26 (Level 2). The bank did not publish a capital walk for the full-year period; published walks cover the half-on-half movement (Dec 25 to Jun 26) and are used here only as context. Quantified drivers for the full year are unavailable from the provided evidence.

> [ev-15] CBA/FY26/profit_announcement, PDF p48: "Common Equity Tier 1 (CET1) 12.0 12.3 12.3 (30)bpts (30)bpts"
> [ev-16] CBA/FY26/profit_announcement, PDF p48: "The Group’s CET1 Capital ratio was 12.0% as at 30 June 2026, a decrease of 30 basis points from 31 December 2025 and 30 June 2025."
> [ev-17] CBA/FY26/profit_announcement, PDF p120: "Common Equity Tier 1 12.0 12.3 12.3"
> [ev-23] CBA/FY26/results_presentation, printed p106: "Key capital ratios (%)1"

### earnings_generation — "Cash NPAT"
*unquantified | confidence 40/100*

The bank does not disclose the specific Cash NPAT contribution to the full-year CET1 movement. Context: the Dec 25 to Jun 26 walk shows +106 bps (ev-1).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CET1 ratio waterfall (Dec 25 Level 2 to Jun 26 Level 2): Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-8] CBA/FY26/results_presentation, printed p106: "[chart annotation] Cash NPAT: footnote 3"

### dividend_net_drp — "Dividend"
*unquantified | confidence 40/100*

The bank does not disclose the specific dividend impact on the full-year CET1 movement. Context: the Dec 25 to Jun 26 walk shows -76 bps (ev-1), including a -10 bps DRP buyback (ev-20).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CET1 ratio waterfall (Dec 25 Level 2 to Jun 26 Level 2): Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-7] CBA/FY26/results_presentation, printed p106: "[chart annotation] 1H26 dividend (DRP neutralised): footnote 2"
> [ev-20] CBA/FY26/results_presentation, printed p32: "The 2026 interim dividend included the on-market purchase of $530 million of shares (CET1 impact of -10bpts) in respect of the Dividend Reinvestment Plan."

### rwa — "RWA"
*unquantified | confidence 40/100*

The bank does not disclose the specific RWA contribution to the full-year CET1 movement. Context: the Dec 25 to Jun 26 walk shows -46 bps, driven by Credit Risk (-38 bps) and IRRBB (-16 bps) partially offset by Market Risk (+8 bps) (ev-1, ev-2, ev-3, ev-4).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CET1 ratio waterfall (Dec 25 Level 2 to Jun 26 Level 2): Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-9] CBA/FY26/results_presentation, printed p106: "[chart annotation] RWA: Credit Risk -38"
> [ev-10] CBA/FY26/results_presentation, printed p106: "[chart annotation] RWA: footnote 4"
> [ev-11] CBA/FY26/results_presentation, printed p106: "[chart annotation] RWA: IRRBB -16"
> [ev-12] CBA/FY26/results_presentation, printed p106: "[chart annotation] RWA: Market Risk +8"

### deductions_other — "Other"
*unquantified | confidence 40/100*

The bank does not disclose the specific 'Other' contribution to the full-year CET1 movement. Context: the Dec 25 to Jun 26 walk shows -8 bps (ev-1).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CET1 ratio waterfall (Dec 25 Level 2 to Jun 26 Level 2): Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-14] CBA/FY26/results_presentation, printed p106: "[chart annotation] Other: footnote 5"

## Limitations
- No capital walk was published for the FY25 to FY26 comparison; all available walks describe the half-on-half period (Dec 25 to Jun 26).
- Quantified driver contributions for the full year are not disclosed in the provided evidence records.
- Failed check: no_quantified_drivers
- No published walk covers FY26 vs FY25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T14:55:39+00:00
- seconds: 73.8
- cost_usd: 0.0023
- tokens: 57610 in / 4520 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY26/profit_announcement p49 <- p48 page 29']
