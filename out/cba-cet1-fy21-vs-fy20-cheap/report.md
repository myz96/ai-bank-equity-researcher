# CBA — cet1 — FY21 vs FY20

**Movement (cash basis):** 1160bps → 1310bps (+150bps) | **Attribution confidence:** 40/100

*Read from: row 'Common Equity Tier 1 capital ratio', column FY20 (Jun 20) -> column FY21 (Jun 21)*

CBA's APRA Level 2 CET1 ratio increased by 150 bps from 11.6% in FY20 to 13.1% in FY21. The bank did not publish a formal capital walk for the full year; however, it disclosed specific regulatory and divestment impacts (+17 bps overlay release, +44 bps divestments) and an off-market buyback (-133 bps). The remaining movement is attributed to organic capital generation, which includes cash NPAT and RWA reductions.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `regulatory_model_changes` | APRA Overlay Release | +17 bps | 85 | 1 (single_source) | ev-2 |
| `divestments_acquisitions` | Divestments | +44 bps | 85 | 1 (single_source) | ev-2, ev-23, ev-25 |
| `capital_returns` | Off-market buy-back | -133 bps | 85 | 1 (single_source) | ev-2, ev-16 |
| *residual (unexplained)* | — | +172 bps | — | — |

### regulatory_model_changes — "APRA Overlay Release"
*+17 bps | confidence 85/100*

The bank explicitly quantified the impact of the APRA overlay release as +17 bps on the CET1 ratio during the period (ev-2).
> [ev-2] CBA/FY21/results_presentation, printed p37: "[walk chart] CBA CET1 ratio in FY21 vs FY20: Jun 20 Level 2 1160 -> Jun 21 Level 2 Pro-forma 1215"

### divestments_acquisitions — "Divestments"
*+44 bps | confidence 85/100*

The bank quantified the expected CET1 uplift from divestments (CFS and CIGI) as +44 bps (ev-2). This aligns with the sum of expected uplifts for Colonial First State (30-40 bps) and CommInsure General Insurance (9 bps) (ev-23, ev-25).
> [ev-2] CBA/FY21/results_presentation, printed p37: "[walk chart] CBA CET1 ratio in FY21 vs FY20: Jun 20 Level 2 1160 -> Jun 21 Level 2 Pro-forma 1215"
> [ev-23] CBA/FY21/results_presentation, printed p35: "Expected CET1 uplift from the previously announced divestments of Colonial First State (Level 2: 30-40bpts, Level 1: 25-35bpts) and CommInsure General Insurance (Level 2: 9bpts, Level 1: 6bpts)."
> [ev-25] CBA/FY21/results_presentation, printed p37: "Expected CET1 uplift from the previously announced divestments of Colonial First State (30-40bpts) and CommInsure General Insurance (9bpts)."

### capital_returns — "Off-market buy-back"
*-133 bps | confidence 85/100*

The bank disclosed an off-market share buyback that reduced the CET1 ratio by 133 bps (ev-2, ev-16).
> [ev-2] CBA/FY21/results_presentation, printed p37: "[walk chart] CBA CET1 ratio in FY21 vs FY20: Jun 20 Level 2 1160 -> Jun 21 Level 2 Pro-forma 1215"
> [ev-16] CBA/FY21/results_presentation, printed p13: "Pro-forma CET1 ratio calculated as Jun 21 CET1 ratio of 13.1% incorporating the impact of the off-market share buy-back (-133bpts)"

### earnings_generation — "Organic Capital Generation"
*unquantified | confidence 60/100*

No explicit full-year organic figure is provided. However, the half-on-half walk shows Cash NPAT at +97 bps and RWA at +8 bps (ev-1). The residual movement after accounting for known items suggests strong organic generation.
> [ev-1] CBA/FY21/results_presentation, printed p35: "[walk chart] CET1 of 13.1% – continued strong organic capital generation: Dec 20 Level 2¹ 1260 -> Jun 21 Level 2¹ 1310"

### dividend_net_drp — "Dividends paid"
*unquantified | confidence 60/100*

The half-on-half dividend was -59 bps (ev-1). The full-year dividend impact is not explicitly broken out in a full-year walk, but total dividends are implied in the organic/residual calculation.
> [ev-1] CBA/FY21/results_presentation, printed p35: "[walk chart] CET1 of 13.1% – continued strong organic capital generation: Dec 20 Level 2¹ 1260 -> Jun 21 Level 2¹ 1310"

## Limitations
- The bank did not publish a formal capital walk for the full year FY20 to FY21. The driver table relies on discrete disclosures (overlay, divestments, buyback) and a residual calculation.
- The 'Organic' and 'Dividend' drivers are unquantified for the full year because the only available walk (ev-1) covers the half-on-half period (Dec 20 to Jun 21), not the full year.
- The residual of +172 bps captures the net effect of earnings, RWA movements, and dividends for the full year, which cannot be further decomposed with high confidence from the provided evidence.
- Failed check: drivers_reconcile (drivers -72.0 + residual +172.0 != delta +150.0, tol 10.0)
- Failed check: comparison_leak (regulatory_model_changes claims +17, which is the 'APRA Overlay Release' bar of CBA/FY21/results_presentation PDF p37 (ev-2), a walk for a different comparison; no walk covers the task comparison, so this bar cannot be a contribution for it — move the number into the driver narrative and name the span it belongs to)
- Failed check: comparison_leak (divestments_acquisitions claims +44, which is the 'Divestments' bar of CBA/FY21/results_presentation PDF p37 (ev-2), a walk for a different comparison; no walk covers the task comparison, so this bar cannot be a contribution for it — move the number into the driver narrative and name the span it belongs to)
- Failed check: comparison_leak (capital_returns claims -133, which is the 'Off-market buy-back' bar of CBA/FY21/results_presentation PDF p37 (ev-2), a walk for a different comparison; no walk covers the task comparison, so this bar cannot be a contribution for it — move the number into the driver narrative and name the span it belongs to)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-29T17:54:04+00:00
- seconds: 74.1
- cost_usd: 0.0024
- tokens: 52271 in / 6597 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY21/profit_announcement p54 <- p53 page 32', 'CBA/FY21/profit_announcement p55 <- p54 page 33']
