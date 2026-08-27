# CBA — cet1 — FY21 vs FY20

**Movement (statutory basis):** 1260bps → 1310bps (+50bps) | **Attribution confidence:** 100/100

CBA's CET1 ratio increased by 50 bps to 13.1% in FY21 (vs Dec 20). The primary driver was earnings generation (+97 bps), partially offset by dividends (-59 bps). RWA decreased slightly (+8 bps impact) and other adjustments contributed +4 bps.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_generation` | Cash NPAT | +97 bps | 100 | 2 () | ev-1, ev-5 |
| `dividend_net_drp` | 1H21 Dividend | -59 bps | 100 | 2 () | ev-1, ev-5 |
| `rwa.credit` | RWA | +8 bps | 100 | 2 () | ev-1, ev-5 |
| `deductions_other` | Other | +4 bps | 100 | 2 () | ev-1, ev-5 |

### earnings_generation — "Cash NPAT"
*+97 bps | confidence 100/100*

Capital generated from cash NPAT was the largest positive contributor, adding 97 bps to the CET1 ratio.
> [ev-1] CBA/FY21/results_presentation, printed p35: "[walk chart] CBA CET1 ratio in FY21 vs FY20: Dec 20 Level 2 1260 -> Jun 21 Level 2 1310"
> [ev-5] CBA/FY21/profit_announcement, PDF p53: "Key drivers of the change in CET1 for the 6 months ended 30 June 2021 were capital generated from earnings (+97 basis points, excluding net equity accounted profits from associates), lower total RWA (+8 basis points) and other regulatory adjustments (+4 basis points), partly offset by the 2021 interim dividend (-59 basis points)"

### dividend_net_drp — "1H21 Dividend"
*-59 bps | confidence 100/100*

The payment of the 2021 interim dividend reduced the CET1 ratio by 59 bps.
> [ev-1] CBA/FY21/results_presentation, printed p35: "[walk chart] CBA CET1 ratio in FY21 vs FY20: Dec 20 Level 2 1260 -> Jun 21 Level 2 1310"
> [ev-5] CBA/FY21/profit_announcement, PDF p53: "Key drivers of the change in CET1 for the 6 months ended 30 June 2021 were capital generated from earnings (+97 basis points, excluding net equity accounted profits from associates), lower total RWA (+8 basis points) and other regulatory adjustments (+4 basis points), partly offset by the 2021 interim dividend (-59 basis points)"

### rwa.credit — "RWA"
*+8 bps | confidence 100/100*

A decrease in total Risk-Weighted Assets contributed positively to the capital ratio by 8 bps.
> [ev-1] CBA/FY21/results_presentation, printed p35: "[walk chart] CBA CET1 ratio in FY21 vs FY20: Dec 20 Level 2 1260 -> Jun 21 Level 2 1310"
> [ev-5] CBA/FY21/profit_announcement, PDF p53: "Key drivers of the change in CET1 for the 6 months ended 30 June 2021 were capital generated from earnings (+97 basis points, excluding net equity accounted profits from associates), lower total RWA (+8 basis points) and other regulatory adjustments (+4 basis points), partly offset by the 2021 interim dividend (-59 basis points)"

### deductions_other — "Other"
*+4 bps | confidence 100/100*

Other regulatory adjustments provided a net positive contribution of 4 bps to the CET1 ratio.
> [ev-1] CBA/FY21/results_presentation, printed p35: "[walk chart] CBA CET1 ratio in FY21 vs FY20: Dec 20 Level 2 1260 -> Jun 21 Level 2 1310"
> [ev-5] CBA/FY21/profit_announcement, PDF p53: "Key drivers of the change in CET1 for the 6 months ended 30 June 2021 were capital generated from earnings (+97 basis points, excluding net equity accounted profits from associates), lower total RWA (+8 basis points) and other regulatory adjustments (+4 basis points), partly offset by the 2021 interim dividend (-59 basis points)"

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-27T07:48:26+00:00
- seconds: 78.9
- cost_usd: 0.0016
- tokens: 32482 in / 4769 out
- orchestration: pipeline
