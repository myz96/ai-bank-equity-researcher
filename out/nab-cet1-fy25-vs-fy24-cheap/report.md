# NAB — cet1 — FY25 vs FY24

**Movement (cash basis):** 1235bps → 1170bps (-65bps) | **Attribution confidence:** 40/100

*Read from: row 'Capital ratios CET1', column 30 Sep 24 -> column 30 Sep 25*

NAB's Group CET1 ratio declined by 65 bps to 11.70% in FY25 (ev-14). The movement is driven primarily by a 45 bps decrease from Credit RWA growth and a net negative impact of 21 bps from cash earnings less dividends (ev-2, ev-4). These were partially offset by a 1 bps increase from non-credit RWA movements (ev-9). The bank notes the ratio remains above its operating target of >11.25% (ev-18).

> [ev-1] NAB/FY25/results_book, printed p28: "Capital ratios CET1 As at 30 Sep 25 11.70 31 Mar 25 12.01 30 Sep 24 12.35"
> [ev-14] NAB/FY25/results_book, printed p4: "Group CET1 ratio of 11.70%, down (65 bps) from September 2024."
> [ev-18] NAB/FY25/investor_presentation, printed p29: "Pro forma CET1 ratio of 11.81% reflects sale of 20% of MLC Life which completed on 31 October3, comfortably above operating target of >11.25%"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `rwa.credit` | Credit RWA | -45 bps | 80 | 1 (single_source) | ev-5, ev-6, ev-7, ev-8 |
| `earnings_generation` | Cash earnings | +82 bps | 80 | 1 (single_source) | ev-2 |
| `dividend_net_drp` | Dividend | -61 bps | 80 | 1 (single_source) | ev-2 |
| `rwa` | Other RWA | +1 bps | 80 | 1 (single_source) | ev-9 |
| `deductions_other` | Other | -8 bps | 80 | 1 (single_source) | ev-10 |
| *residual (unexplained)* | — | -29 bps | — | — |

### rwa.credit — "Credit RWA"
*-45 bps | confidence 80/100*

Credit RWA decreased the CET1 capital ratio by 45 basis points (ev-5). This was driven by volume growth (-27 bps) and asset quality deterioration (-5 bps), alongside model/methodology changes (-13 bps) (ev-6, ev-7, ev-8).
> [ev-5] NAB/FY25/results_book, printed p28: "an increase in credit RWA decreasing the CET1 capital ratio by 45 basis points"
> [ev-6] NAB/FY25/results_book, printed p28: "volume growth contributing to a decrease of 27 basis points"
> [ev-7] NAB/FY25/results_book, printed p28: "asset quality deterioration contributing to a decrease of 5 basis points"
> [ev-8] NAB/FY25/results_book, printed p28: "model and methodology changes contributing to a decrease of 13 basis points"

### earnings_generation — "Cash earnings"
*+82 bps | confidence 80/100*

Cash earnings contributed an increase of 82 basis points to the CET1 ratio (ev-2).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"

### dividend_net_drp — "Dividend"
*-61 bps | confidence 80/100*

The dividend payment resulted in a decrease of 61 basis points to the CET1 ratio (ev-2).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"

### rwa — "Other RWA"
*+1 bps | confidence 80/100*

Other (non-credit) RWA movements increased the CET1 capital ratio by 1 basis point (ev-9).
> [ev-9] NAB/FY25/results_book, printed p28: "a decrease in other (non-credit) RWA increasing the CET1 capital ratio by 1 basis point"

### deductions_other — "Other"
*-8 bps | confidence 80/100*

Other items decreased the CET1 capital ratio by 8 basis points (ev-10).
> [ev-10] NAB/FY25/results_book, printed p28: "other items decreasing the CET1 capital ratio by 8 basis points"

## Source disagreements
- **Walk Period Mismatch** (definitional): -31 bps (H2 FY25 walk) vs -65 bps (FY25 vs FY24)
  Preferred: -65 bps. The published capital walk (ev-2) covers the half-year ended March 2025 to September 2025 (H2 FY25), not the full year comparison requested. The H2 walk sums to -31 bps. The task requires the FY25 vs FY24 movement (-65 bps). The residual captures the unquantified drivers for the first half of FY25.

## Limitations
- The primary capital walk provided by NAB (ev-2) is for the half-year ended Sep 2025, not the full year FY25 vs FY24.
- The driver table quantifies only the H2 FY25 components explicitly stated in the results book.
- A residual of -29 bps exists because the sum of the H2 drivers (-116 bps) does not equal the full-year delta (-65 bps); this residual represents the unquantified net impact of the first half of FY25 (Oct 2024 - Mar 2025).
- Failed check: drivers_reconcile (drivers -31.0 + residual -29.0 != delta -65.0, tol 1.0)
- Capped at 80: rwa.credit -45 bps, earnings_generation +82 bps, dividend_net_drp -61 bps, rwa +1 bps, deductions_other -8 bps. drivers_reconcile failed, so the parts and the whole disagree. That proves one of these claims is wrong without saying which, so none of them may claim near-certainty.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T16:32:57+00:00
- seconds: 43.4
- cost_usd: 0.0021
- tokens: 44128 in / 6285 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
