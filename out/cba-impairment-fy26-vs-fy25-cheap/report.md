# CBA — impairment — FY26 vs FY25

**Movement (statutory basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 40/100

CBA's Loan Impairment Expense (LIE) increased $62 million to $788 million in FY26 (FY25: $726 million), a 9% rise. The impairment rate rose 1 basis point to 8 bps of average GLAA. Growth was driven by Retail Banking (+$106m) and New Zealand (+$11m), partially offset by reductions in Business Banking (-$45m) and Institutional Banking (-$16m). Management attributed the increase to portfolio growth, cost-of-living pressures, and macroeconomic uncertainty.

### collective.volume
*unquantified | confidence 60/100*

Management cited 'portfolio growth' as a primary driver for the overall LIE increase (ev-1) and specifically for Corporate collective provisions which grew $172m (ev-11). This likely drove the RBS increase given its size.
> [ev-1] CBA/FY26/asx_announcement, PDF p2: "Loan impairment expense increased mainly reflecting portfolio growth, cost-of-living pressures and increased geopolitical risk and macroeconomic uncertainty."
> [ev-11] CBA/FY26/profit_announcement, PDF p44: "Corporate collective provisions increased $172 million or 7% to $2,797 million, mainly reflecting portfolio growth, increased geopolitical risk and macroeconomic uncertainty."

### overlays_fla
*unquantified | confidence 60/100*

Narrative attributes include 'cost-of-living pressures', 'geopolitical risk', and 'macroeconomic uncertainty' (ev-1). Consumer collective provisions decreased despite these headwinds due to 'rising house prices' and 'more targeted forward-looking adjustments' (ev-12), suggesting overlay management.
> [ev-1] CBA/FY26/asx_announcement, PDF p2: "Loan impairment expense increased mainly reflecting portfolio growth, cost-of-living pressures and increased geopolitical risk and macroeconomic uncertainty."
> [ev-12] CBA/FY26/profit_announcement, PDF p44: "Consumer collective provisions decreased $48 million or 2% to $2,888 million, reflecting rising house prices over the period and more targeted forward-looking adjustments for higher risk customer cohorts."

### write_backs_recoveries
*unquantified | confidence 60/100*

Corporate individually assessed provisions decreased $6m, explicitly 'driven by write-backs and write-offs' (ev-14). This activity contributed to the lower-than-expected corporate charge relative to the collective provision growth.
> [ev-14] CBA/FY26/profit_announcement, PDF p44: "Corporate individually assessed provisions decreased $6 million or 1% to $694 million, driven by write-backs and write-offs."

## Limitations
- No quantitative walk chart or bridge table is provided for FY26 vs FY25 LIE drivers. Contributions are inferred from segment-level P&L changes (ev-6 to ev-9) and narrative attributions (ev-1, ev-11-14).
- The sum of segment deltas ($106 + $11 - $45 - $16 = $56m) does not fully reconcile to the total delta ($62m), leaving a $6m unexplained residual potentially due to rounding or other segments.
- Specific attribution of the $62m movement to canonical taxonomy buckets (volume vs asset quality) is qualitative only.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:21:03+00:00
- seconds: 54.1
- cost_usd: 0.0014
- tokens: 24917 in / 5394 out
- orchestration: pipeline
