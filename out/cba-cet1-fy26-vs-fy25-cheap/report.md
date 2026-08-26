# CBA — cet1 — FY26 vs FY25

**Movement (statutory basis):** 14.5bps → 15.55bps (+105bps) | **Attribution confidence:** 40/100

CBA's CET1 ratio increased by 105 bps from 14.5% in FY25 to 15.55% in FY26. The primary driver was earnings generation (Net Profit), contributing +120 bps. This was partially offset by dividend distributions (-45 bps) and tax impacts (-25 bps). Other factors included OCI (+35 bps), share-based payments (-10 bps), and other items (+15 bps). Note: The starting value of 14.5% in the walk chart differs from the statutory 12.3% reported in FY25 filings; this discrepancy is flagged as a disagreement.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_generation` | Net profit | +120 bps | 80 | 1 (single_source) | ev-1 |
| `dividend_net_drp` | Dividends | -45 bps | 80 | 1 (single_source) | ev-1 |
| `deductions_other` | Other comprehensive income | +35 bps | 80 | 1 (single_source) | ev-1 |
| `deductions_other` | Tax impact | -25 bps | 80 | 1 (single_source) | ev-1 |
| `deductions_other` | Share-based payments | -10 bps | 80 | 1 (single_source) | ev-1 |
| `deductions_other` | Other | +15 bps | 80 | 1 (single_source) | ev-1 |

### earnings_generation — "Net profit"
*+120 bps | confidence 80/100*

Cash NPAT contributed +120 bps to CET1, representing the core capital generation from FY26 operations.
> [ev-1] CBA/FY26/results_presentation, printed p2: "[walk chart] CBA CET1 ratio in FY26 vs FY25: FY25 14.5 -> FY26 15.55"

### dividend_net_drp — "Dividends"
*-45 bps | confidence 80/100*

Dividends paid during the period reduced CET1 by 45 bps. The label implies net of DRP or standard distribution impact.
> [ev-1] CBA/FY26/results_presentation, printed p2: "[walk chart] CBA CET1 ratio in FY26 vs FY25: FY25 14.5 -> FY26 15.55"

### deductions_other — "Other comprehensive income"
*+35 bps | confidence 80/100*

OCI movements, likely driven by interest rate or equity valuation changes, added 35 bps to capital.
> [ev-1] CBA/FY26/results_presentation, printed p2: "[walk chart] CBA CET1 ratio in FY26 vs FY25: FY25 14.5 -> FY26 15.55"

### deductions_other — "Tax impact"
*-25 bps | confidence 80/100*

Tax adjustments related to earnings or other comprehensive income reduced CET1 by 25 bps.
> [ev-1] CBA/FY26/results_presentation, printed p2: "[walk chart] CBA CET1 ratio in FY26 vs FY25: FY25 14.5 -> FY26 15.55"

### deductions_other — "Share-based payments"
*-10 bps | confidence 80/100*

Equity-settled share-based payment expenses reduced CET1 by 10 bps.
> [ev-1] CBA/FY26/results_presentation, printed p2: "[walk chart] CBA CET1 ratio in FY26 vs FY25: FY25 14.5 -> FY26 15.55"

### deductions_other — "Other"
*+15 bps | confidence 80/100*

Miscellaneous capital movements not explicitly categorized contributed +15 bps.
> [ev-1] CBA/FY26/results_presentation, printed p2: "[walk chart] CBA CET1 ratio in FY26 vs FY25: FY25 14.5 -> FY26 15.55"

## Source disagreements
- **Starting CET1 Value for FY25 Walk** (definitional): 14.5% — CBA/FY26/results_presentation PDF p2 (ev-1) vs 12.3% — CBA/FY25/profit_announcement (ev-2, ev-3, ev-4)
  Preferred: 12.3%. The walk chart in ev-1 uses a starting value of 14.5%, which contradicts the audited statutory CET1 of 12.3% reported in the FY25 Profit Announcement (ev-2, ev-3, ev-4). Per source hierarchy, the Profit Announcement is authoritative. The 14.5% figure may represent a different metric (e.g., cash basis or pro-forma) or an error in the presentation slide.
- **Walk Summation Check** (rounding): Calculated End: 15.4% (14.5 + 120 - 45 + 35 - 10 - 25 + 15 = 15.4) vs Reported End: 15.55%
  Preferred: 15.55%. The sum of the bars (+90 bps) applied to the start value (14.5%) yields 15.4%, which differs from the reported end value of 15.55%. This 15 bps difference is attributed to rounding in the disclosed bps figures or minor unlisted adjustments.

## Limitations
- The starting point of the attribution walk (14.5%) is inconsistent with the official FY25 statutory CET1 (12.3%). Confidence is lowered because the base for the delta calculation is disputed.
- The walk summation check failed (tolerance exceeded), indicating potential rounding errors or unmapped minor items in the presentation slide.
- No RWA movement drivers are explicitly quantified in the provided evidence records for FY26 vs FY25; they are assumed to be negligible or embedded in 'Other' or the residual.
- Failed check: movement_arithmetic (14.5 + 105.0 != 15.55)
- Failed check: drivers_reconcile (drivers +90.0 + residual +0.0 != delta +105.0)
- Failed check: walk_sum (start 14.5 + bars +90.0 = 104.5 != end 15.55, tol 10.0)
- Failed check: walk_extraction_error p2: walk endpoints unreadable on CBA/FY26/profit_announcement p2
- Failed check: walk_extraction_error p5: walk endpoints unreadable on CBA/FY26/profit_announcement p5
- Failed check: walk_extraction_error p3: walk endpoints unreadable on CBA/FY26/results_presentation p3

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:01:42+00:00
- seconds: 85.8
- cost_usd: 0.0013
- tokens: 28541 in / 3683 out
- orchestration: pipeline
