# NAB — cet1 — FY25 vs FY24

**Movement (cash basis):** 1235bps → 1170bps (-65bps) | **Attribution confidence:** 40/100

*Read from: row 'Capital ratios CET1', column 30 Sep 24 -> column 30 Sep 25*

NAB's APRA Level 2 Group CET1 ratio declined by 65 bps to 11.70% in FY25 (ev-14). The movement is driven primarily by a 45 bps decrease from credit RWA growth and a net negative impact of 21 bps from cash earnings less dividends (ev-4). These were partially offset by a 1 bps increase from other non-credit RWA reductions (ev-9) and an 8 bps decrease from other items (ev-10). Model changes contributed a further 13 bps decrease (ev-8). A pro-forma adjustment for the MLC Life sale would have resulted in a 11.81% ratio (ev-15).

> [ev-1] NAB/FY25/results_book, printed p28: "Capital ratios CET1 As at 30 Sep 25 11.70 31 Mar 25 12.01 30 Sep 24 12.35"
> [ev-14] NAB/FY25/results_book, printed p4: "Group CET1 ratio of 11.70%, down (65 bps) from September 2024."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `rwa.credit` | Credit RWA | -45 bps | 80 | 1 (single_source) | ev-5, ev-6, ev-7, ev-8 |
| `earnings_generation` | Cash earnings | +82 bps | 80 | 1 (single_source) | ev-2 |
| `dividend_net_drp` | Dividend | -61 bps | 80 | 1 (single_source) | ev-2, ev-4 |
| `rwa` | Other RWA | +1 bps | 80 | 1 (single_source) | ev-9 |
| `deductions_other` | Other | -8 bps | 80 | 1 (single_source) | ev-10 |
| *residual (unexplained)* | — | -29 bps | — | — |

### rwa.credit — "Credit RWA"
*-45 bps | confidence 80/100*

Credit RWA decreased the CET1 capital ratio by 45 basis points (ev-5). This was composed of volume growth contributing a 27 bps decrease (ev-6), asset quality deterioration contributing a 5 bps decrease (ev-7), and model/methodology changes contributing a 13 bps decrease (ev-8).
> [ev-5] NAB/FY25/results_book, printed p28: "an increase in credit RWA decreasing the CET1 capital ratio by 45 basis points"
> [ev-6] NAB/FY25/results_book, printed p28: "volume growth contributing to a decrease of 27 basis points"
> [ev-7] NAB/FY25/results_book, printed p28: "asset quality deterioration contributing to a decrease of 5 basis points"
> [ev-8] NAB/FY25/results_book, printed p28: "model and methodology changes contributing to a decrease of 13 basis points"

### earnings_generation — "Cash earnings"
*+82 bps | confidence 80/100*

Cash earnings generated an 82 bps increase to the CET1 ratio (ev-2). This figure represents the gross earnings contribution before dividend deductions.
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"

### dividend_net_drp — "Dividend"
*-61 bps | confidence 80/100*

The 2025 interim dividend reduced the CET1 ratio by 61 bps (ev-2). Combined with earnings, this resulted in a net positive capital generation of 21 bps (ev-4).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"
> [ev-4] NAB/FY25/results_book, printed p28: "cash earnings less the 2025 interim dividend resulting in an increase of 21 basis points."

### rwa — "Other RWA"
*+1 bps | confidence 80/100*

A decrease in other (non-credit) RWA increased the CET1 capital ratio by 1 basis point (ev-9).
> [ev-9] NAB/FY25/results_book, printed p28: "a decrease in other (non-credit) RWA increasing the CET1 capital ratio by 1 basis point"

### deductions_other — "Other"
*-8 bps | confidence 80/100*

Other items decreased the CET1 capital ratio by 8 basis points (ev-10).
> [ev-10] NAB/FY25/results_book, printed p28: "other items decreasing the CET1 capital ratio by 8 basis points"

## Source disagreements
- **Pro-forma vs Reported Ratio** (definitional): 11.70% - ev-1 vs 11.81% - ev-15
  Preferred: 11.70%. The reported statutory ratio is 11.70%. The 11.81% figure is a pro-forma measure reflecting the sale of the remaining 20% stake in MLC Life, which completed after the period end.

## Limitations
- The bank's published half-on-half walk (ev-2) sums to -31 bps, whereas the full-year delta is -65 bps. The narrative drivers provided (ev-5 through ev-10) sum to -36 bps, leaving a residual of -29 bps unexplained by specific quantified bars in the text. This suggests either unquantified drivers or that the narrative sub-components do not fully reconcile to the headline annual movement.
- Failed check: drivers_reconcile (drivers -31.0 + residual -29.0 != delta -65.0, tol 1.0)
- Capped at 80: rwa.credit -45 bps, earnings_generation +82 bps, dividend_net_drp -61 bps, rwa +1 bps, deductions_other -8 bps. drivers_reconcile failed, so the parts and the whole disagree. That proves one of these claims is wrong without saying which, so none of them may claim near-certainty.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T23:41:10+00:00
- seconds: 39.3
- cost_usd: 0.002
- tokens: 41170 in / 5740 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
