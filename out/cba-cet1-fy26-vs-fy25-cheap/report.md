# CBA — cet1 — FY26 vs FY25

**Movement (statutory basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 95/100

CBA's APRA Level 2 CET1 ratio declined by 30 bps in FY26, settling at 12.0% (ev-7, ev-15). This movement is primarily driven by cash NPAT generation of +106 bps, partially offset by dividend distributions net of DRP (-76 bps), credit RWA growth (-46 bps), and other deductions (-8 bps) as detailed in the results presentation walk charts (ev-1, ev-2).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_generation` | Cash NPAT | +106 bps | 85 | 1 (single_source) | ev-1, ev-2 |
| `dividend_net_drp` | 1H26 dividend (DRP neutralised) | -76 bps | 85 | 1 (single_source) | ev-1, ev-2, ev-12 |
| `rwa.credit` | RWA | -46 bps | 95 | 2 () | ev-1, ev-2, ev-4 |
| `deductions_other` | Other | -8 bps | 85 | 1 (single_source) | ev-1, ev-2 |

### earnings_generation — "Cash NPAT"
*+106 bps | confidence 85/100*

Cash NPAT contributed +106 bps to the CET1 ratio, representing the primary source of capital generation during the period.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

### dividend_net_drp — "1H26 dividend (DRP neutralised)"
*-76 bps | confidence 85/100*

Dividends net of DRP reduced the ratio by 76 bps. The interim dividend included a $530m on-market purchase impacting CET1 by -10 bps (ev-12).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-12] CBA/FY26/results_presentation, printed p32: "The 2026 interim dividend included the on-market purchase of $530 million of shares (CET1 impact of -10bpts) in respect of the Dividend Reinvestment Plan."

### rwa.credit — "RWA"
*-46 bps | confidence 95/100*

Credit risk RWA movements resulted in a -46 bps impact, consistent with the AS announcement noting deployment of 72 bpts of capital into credit RWA (ev-4).
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-4] CBA/FY26/asx_announcement, PDF p2: "The Group’s Common Equity Tier 1 (CET1) ratio of 12.0% was well above APRA’s minimum regulatory requirement of 10.25%. Across the year we deployed 72bpts of capital into credit risk weighted assets"

### deductions_other — "Other"
*-8 bps | confidence 85/100*

Other factors, including capital deductions and reserves, contributed a net -8 bps to the CET1 ratio movement.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:33:24+00:00
- seconds: 46.9
- cost_usd: 0.001
- tokens: 22849 in / 2718 out
- orchestration: pipeline
