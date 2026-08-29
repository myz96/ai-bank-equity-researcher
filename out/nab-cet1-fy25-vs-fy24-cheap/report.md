# NAB — cet1 — FY25 vs FY24

**Movement (cash basis):** 1235bps → 1170bps (-65bps) | **Attribution confidence:** 60/100

*Read from: row 'Capital ratios CET1', column 30 Sep 24 -> column 30 Sep 25*

NAB's APRA Level 2 Group CET1 ratio declined by 65 bps to 11.70% in FY25 (from 12.35% in FY24). The decline was driven primarily by a 45 bps negative impact from increased credit RWA and a 61 bps negative impact from dividends net of DRP, partially offset by 82 bps of positive contribution from cash earnings generation.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_generation` | Cash earnings | +82 bps | 85 | 1 (single_source) | ev-2 |
| `dividend_net_drp` | Dividend | -61 bps | 85 | 1 (single_source) | ev-2 |
| `rwa.credit` | Credit RWA | -45 bps | 85 | 1 (single_source) | ev-2, ev-5 |
| `rwa` | Other RWA | +1 bps | 85 | 1 (single_source) | ev-2, ev-6 |
| `deductions_other` | Other | -8 bps | 85 | 1 (single_source) | ev-2, ev-7 |
| *residual (unexplained)* | — | -34 bps | — | — |

### earnings_generation — "Cash earnings"
*+82 bps | confidence 85/100*

Cash earnings generated an 82 bps increase in the CET1 ratio for the year ended September 2025.
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"

### dividend_net_drp — "Dividend"
*-61 bps | confidence 85/100*

Dividends paid during the period resulted in a 61 bps decrease in the CET1 ratio.
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"

### rwa.credit — "Credit RWA"
*-45 bps | confidence 85/100*

An increase in credit risk-weighted assets decreased the CET1 capital ratio by 45 bps.
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"
> [ev-5] NAB/FY25/results_book, printed p28: "an increase in credit RWA decreasing the CET1 capital ratio by 45 basis points"

### rwa — "Other RWA"
*+1 bps | confidence 85/100*

A decrease in other (non-credit) RWA increased the CET1 capital ratio by 1 bps.
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"
> [ev-6] NAB/FY25/results_book, printed p28: "a decrease in other (non-credit) RWA increasing the CET1 capital ratio by 1 basis point"

### deductions_other — "Other"
*-8 bps | confidence 85/100*

Other items, including capital deductions and reserves, decreased the CET1 capital ratio by 8 bps.
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"
> [ev-7] NAB/FY25/results_book, printed p28: "other items decreasing the CET1 capital ratio by 8 basis points"

## Source disagreements
- **Pro-forma adjustment** (definitional): 11.70% reported (ev-1) vs 11.81% pro-forma (ev-11)
  Preferred: 11.70%. The pro-forma ratio of 11.81% reflects the sale of MLC Life. This is a non-GAAP measure used for context; the statutory movement is based on the reported 11.70%.

## Limitations
- The provided evidence contains a half-on-half walk (Mar 25 -> Sep 25) rather than a full-year walk (Sep 24 -> Sep 25).
- The sum of the quantified drivers (-31 bps) does not reconcile with the total delta (-65 bps), leaving a residual of -34 bps.
- The bank narrative attributes the movement to specific factors but does not provide a full-year bridge table that sums to the delta, preventing precise attribution of the residual.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-29T18:08:53+00:00
- seconds: 45.1
- cost_usd: 0.0017
- tokens: 37782 in / 4716 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
