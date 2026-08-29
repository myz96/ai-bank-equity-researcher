# NAB — cet1 — FY25 vs FY24

**Movement (cash basis):** 1235bps → 1170bps (-65bps) | **Attribution confidence:** 60/100

*Read from: row 'Capital ratios CET1', column 30 Sep 24 -> column 30 Sep 25*

NAB's Group CET1 ratio declined by 65 bps to 11.70% in FY25 (ev-14). The primary driver was a 45 bps reduction from Credit RWA growth, partially offset by 82 bps of cash earnings generation and a 61 bps dividend outflow (ev-2). Other factors included model changes (-13 bps) and other items (-8 bps) (ev-2, ev-8, ev-10).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_generation` | Cash earnings | +82 bps | 85 | 1 (single_source) | ev-2 |
| `dividend_net_drp` | Dividend | -61 bps | 85 | 1 (single_source) | ev-2 |
| `rwa.credit` | Credit RWA | -45 bps | 85 | 1 (single_source) | ev-2, ev-5, ev-6, ev-7, ev-8 |
| `rwa` | Other RWA | +1 bps | 85 | 1 (single_source) | ev-2, ev-9 |
| `deductions_other` | Other | -8 bps | 85 | 1 (single_source) | ev-2, ev-10 |
| *residual (unexplained)* | — | -34 bps | — | — |

### earnings_generation — "Cash earnings"
*+82 bps | confidence 85/100*

Cash earnings generated an increase of 82 bps to the CET1 ratio for the full year (ev-2).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"

### dividend_net_drp — "Dividend"
*-61 bps | confidence 85/100*

The 2025 interim dividend resulted in a decrease of 61 bps to the CET1 ratio (ev-2).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"

### rwa.credit — "Credit RWA"
*-45 bps | confidence 85/100*

An increase in credit RWA decreased the CET1 capital ratio by 45 bps, driven by volume growth (-27 bps), asset quality deterioration (-5 bps), and model/methodology changes (-13 bps) (ev-5, ev-6, ev-7, ev-8).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"
> [ev-5] NAB/FY25/results_book, printed p28: "an increase in credit RWA decreasing the CET1 capital ratio by 45 basis points"
> [ev-6] NAB/FY25/results_book, printed p28: "volume growth contributing to a decrease of 27 basis points"
> [ev-7] NAB/FY25/results_book, printed p28: "asset quality deterioration contributing to a decrease of 5 basis points"
> [ev-8] NAB/FY25/results_book, printed p28: "model and methodology changes contributing to a decrease of 13 basis points"

### rwa — "Other RWA"
*+1 bps | confidence 85/100*

A decrease in other (non-credit) RWA increased the CET1 capital ratio by 1 bps (ev-2, ev-9).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"
> [ev-9] NAB/FY25/results_book, printed p28: "a decrease in other (non-credit) RWA increasing the CET1 capital ratio by 1 basis point"

### deductions_other — "Other"
*-8 bps | confidence 85/100*

Other items decreased the CET1 capital ratio by 8 bps (ev-2, ev-10).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"
> [ev-10] NAB/FY25/results_book, printed p28: "other items decreasing the CET1 capital ratio by 8 basis points"

## Limitations
- The bank only provides a half-on-half capital walk (Mar 25 -> Sep 25) with quantified drivers (ev-2). No published walk exists for the full-year FY24 -> FY25 comparison.
- The sum of the stated drivers (-31 bps) does not reconcile to the total movement (-65 bps), leaving a residual of -34 bps which is unquantified in the source text.
- Confidence is limited because the specific drivers contributing to the residual are not disclosed.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-29T21:01:31+00:00
- seconds: 48.6
- cost_usd: 0.002
- tokens: 42038 in / 5403 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
