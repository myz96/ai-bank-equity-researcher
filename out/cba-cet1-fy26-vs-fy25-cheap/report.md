# CBA — cet1 — FY26 vs FY25

**Movement (cash basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 60/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 31 Dec 25 -> column 30 Jun 26*

CBA's Level 2 CET1 ratio decreased by 30 bps to 12.0% in FY26 from 12.3% in FY25. The bank did not publish a full-year capital walk for this period; the published walk covers the half-on-half movement (Dec 2025 to Jun 2026). Quantified drivers are derived from text footnotes and RWA breakdowns.

### dividend_net_drp — "1H26 dividend (DRP neutralised)"
*unquantified | confidence 60/100*

The bank states the interim dividend included a $530m on-market purchase of shares with a CET1 impact of -10 bps (ev-8, ev-14). The full-year DRP-neutralized dividend impact is not explicitly quantified in the provided text.
> [ev-8] CBA/FY26/results_presentation, printed p32: "The 2026 interim dividend included the on-market purchase of $530 million of shares (CET1 impact of -10bpts) in respect of the Dividend Reinvestment Plan."
> [ev-14] CBA/FY26/results_presentation, printed p106: "The 2026 interim dividend included the on-market purchase of $530 million of shares (CET1 impact of -10bpts) in respect of the Dividend Reinvestment Plan."

### rwa.credit — "Credit Risk"
*unquantified | confidence 60/100*


> [ev-9] CBA/FY26/results_presentation, printed p32: "Movements in bpts Credit Risk4 (38) IRRBB (16) Market Risk 8 Operational Risk - 3 Underlying movement Jun 26 vs Jun 25"

### rwa.irrbb — "IRRBB"
*unquantified | confidence 60/100*

IRRBB RWA movement is stated as -16 bps in the Jun 2025 vs Jun 2026 comparison (ev-9). This is a year-on-year metric, not a contribution to the FY26 vs FY25 flow.
> [ev-9] CBA/FY26/results_presentation, printed p32: "Movements in bpts Credit Risk4 (38) IRRBB (16) Market Risk 8 Operational Risk - 3 Underlying movement Jun 26 vs Jun 25"

### earnings_generation — "Cash NPAT"
*unquantified | confidence 60/100*

Cash NPAT contributed +106 bpts in the context-only Dec 2025 -> Jun 2026 walk (ev-1, ev-2). No specific FY26 vs FY25 earnings contribution is quantified in the text.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

## Source disagreements
- **Capital Walk Period** (definitional): Context: Dec 2025 -> Jun 2026 (ev-1, ev-2) vs Task: FY25 -> FY26
  Preferred: Task Comparison. The bank only provides a capital walk for the half-on-half period (Dec 2025 to Jun 2026). The task requires the full-year movement (Jun 2025 to Jun 2026). The provided walk bars cannot be attributed to the task period.

## Limitations
- No full-year (FY25 to FY26) capital walk was published in the evidence.
- Quantified drivers are limited to specific footnote impacts (-10 bps for buyback) or year-on-year comparisons (-38 bps credit, -16 bps IRRBB) which do not sum to the FY26 vs FY25 delta.
- Residual of -30 bps remains unexplained due to lack of full-year driver data.
- Failed check: no_quantified_drivers
- No published walk covers FY26 vs FY25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T03:42:05+00:00
- seconds: 72.8
- cost_usd: 0.0019
- tokens: 45055 in / 4483 out
- orchestration: pipeline
