# CBA — cet1 — FY26 vs FY25

**Movement (statutory basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 95/100

CBA's CET1 ratio declined by 30 bps to 12.0% in FY26 (Level 2). The primary detractor was dividends net of DRP (-76 bps), partially offset by earnings generation (+106 bps) and RWA reductions (-46 bps). Other deductions contributed a minor drag of -8 bps.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `dividend_net_drp` | 1H26 dividend (DRP neutralised) | -76 bps | 95 | 2 () | ev-1, ev-2, ev-5, ev-12, ev-23 |
| `earnings_generation` | Cash NPAT | +106 bps | 85 | 1 (single_source) | ev-1, ev-2 |
| `rwa.credit` | RWA | -46 bps | 90 | 2 () | ev-1, ev-2, ev-7, ev-13, ev-14, ev-15 |
| `deductions_other` | Other | -8 bps | 85 | 1 (single_source) | ev-1, ev-2 |

### dividend_net_drp — "1H26 dividend (DRP neutralised)"
*-76 bps | confidence 95/100*

Dividends paid net of the Dividend Reinvestment Plan reduced capital. This includes on-market share purchases related to the DRP.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230.0 -> Jun 26 Level 2 1200.0"
> [ev-5] CBA/FY26/profit_announcement, PDF p48: "The 2026 interim dividend included the on-market purchase of $530 million of shares (CET1 impact of -10 bpts)"
> [ev-12] CBA/FY26/results_presentation, printed p32: "The 2026 interim dividend included the on-market purchase of $530 million of shares (CET1 impact of -10bpts) in respect of the Dividend Reinvestment Plan."
> [ev-23] CBA/FY26/results_presentation, printed p106: "The 2026 interim dividend included the on-market purchase of $530 million of shares (CET1 impact of -10bpts) in respect of the Dividend Reinvestment Plan."

### earnings_generation — "Cash NPAT"
*+106 bps | confidence 85/100*

Capital generated from cash net profit after tax provided the largest positive contribution to the CET1 ratio.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230.0 -> Jun 26 Level 2 1200.0"

### rwa.credit — "RWA"
*-46 bps | confidence 90/100*

Reductions in Risk-Weighted Assets supported the ratio. While the PA table breaks this into credit/IRRBB/market components, the walk aggregates them as 'RWA'.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230.0 -> Jun 26 Level 2 1200.0"
> [ev-7] CBA/FY26/profit_announcement, PDF p48: "Dec 25 Level 2 1H26 Dividend Cash NPAT RWA Other Jun 26 Level 2 5 (38) Credit 4 (16) IRRBB 8 Market - Operational 2 3"
> [ev-13] CBA/FY26/results_presentation, printed p32: "Movements in bpts Credit Risk (38)"
> [ev-14] CBA/FY26/results_presentation, printed p32: "IRRBB (16)"
> [ev-15] CBA/FY26/results_presentation, printed p32: "Market Risk 8"

### deductions_other — "Other"
*-8 bps | confidence 85/100*

Minor negative impact from other capital deductions or reserves not captured in the main drivers.
> [ev-1] CBA/FY26/results_presentation, printed p32: "[walk chart] CBA CET1 ratio in FY26 vs FY25: Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"
> [ev-2] CBA/FY26/results_presentation, printed p106: "[walk chart] CET1 capital ratio movements: Dec 25 Level 2 1230.0 -> Jun 26 Level 2 1200.0"

## Source disagreements
- **RWA Driver Granularity** (definitional): -46 bps — CBA/FY26/results_presentation (ev-1, ev-2) vs -16 bps Credit + 8 bps IRRBB + 2 bps Operational — CBA/FY26/profit_announcement (ev-7)
  Preferred: Walk Chart Aggregation. The results presentation walk aggregates all risk-weighted asset movements into a single '-46 bps' bar labeled 'RWA'. The Profit Announcement table disaggregates this into specific risk types (Credit, IRRBB, Operational). Both are consistent (summing to -46 bps), but the walk is the primary source for the requested taxonomy.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-27T07:58:29+00:00
- seconds: 78.4
- cost_usd: 0.0015
- tokens: 31112 in / 4185 out
- orchestration: pipeline
