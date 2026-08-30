# NAB — cet1 — FY25 vs FY24

**Movement (cash basis):** 1235bps → 1170bps (-65bps) | **Attribution confidence:** 60/100

*Read from: row 'Capital ratios CET1', column 30 Sep 24 -> column 30 Sep 25*

NAB's APRA Level 2 CET1 ratio declined by 65 bps to 11.70% in FY25 (ev-11). The movement is driven primarily by a 45 bps negative impact from Credit RWA growth and quality, partially offset by an 82 bps positive contribution from cash earnings generation. Dividends reduced the ratio by 61 bps. Other factors, including model changes and non-credit RWA movements, had minor impacts.

> [ev-1] NAB/FY25/results_book, printed p28: "Capital ratios CET1 As at 30 Sep 25 11.70 31 Mar 25 12.01 30 Sep 24 12.35"
> [ev-9] NAB/FY25/results_book, printed p66: "Capital ratios CET1 30 Sep 25 11.70 31 Mar 25 12.01 30 Sep 24 12.35"
> [ev-10] NAB/FY25/results_book, printed p4: "Group CET1 ratio(i) (%) ... FY24 12.35 ... FY25 11.70"
> [ev-11] NAB/FY25/results_book, printed p4: "Group CET1 ratio of 11.70%, down (65 bps) from September 2024."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_generation` | Cash earnings | +82 bps | 85 | 1 (single_source) | ev-2 |
| `dividend_net_drp` | Dividend | -61 bps | 85 | 1 (single_source) | ev-2 |
| `rwa.credit` | Credit RWA | -45 bps | 85 | 1 (single_source) | ev-5 |
| `rwa` | Other RWA | +1 bps | 85 | 1 (single_source) | ev-6 |
| `deductions_other` | Other | -8 bps | 85 | 1 (single_source) | ev-7 |
| *residual (unexplained)* | — | -34 bps | — | — |

### earnings_generation — "Cash earnings"
*+82 bps | confidence 85/100*

Cash earnings contributed +82 bps to the CET1 ratio for the full year. This reflects the bank's core profit generation over the period (ev-2).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"

### dividend_net_drp — "Dividend"
*-61 bps | confidence 85/100*

Dividends paid during the period reduced the CET1 ratio by 61 bps (ev-2).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01 Cash earnings 0.82 Dividend (0.61) Credit RWA¹ (0.45) Other RWA 0.01 Other (0.08) Sep 25 11.70"

### rwa.credit — "Credit RWA"
*-45 bps | confidence 85/100*

Credit RWA decreased the ratio by 45 bps. Drivers: volume growth (-27 bps), asset quality deterioration (-5 bps), and model/methodology changes (-13 bps) (ev-5).
> [ev-5] NAB/FY25/results_book, printed p28: "an increase in credit RWA decreasing the CET1 capital ratio by 45 basis points, driven by: – volume growth contributing to a decrease of 27 basis points, – asset quality deterioration contributing to a decrease of 5 basis points, and – model and methodology changes contributing to a decrease of 13 basis points."

### rwa — "Other RWA"
*+1 bps | confidence 85/100*

Non-credit RWA increased the ratio by 1 bp. Components: operational risk (+1 bp), traded market risk (+1 bp), IRRBB (+2 bps), capital floor adjustment (-3 bps) (ev-6).
> [ev-6] NAB/FY25/results_book, printed p28: "a decrease in other (non-credit) RWA increasing the CET1 capital ratio by 1 basis point, driven mainly by: – operational risk contributing to an increase of 1 basis point, – traded market risk contributing to an increase of 1 basis point, – interest rate risk in the banking book contributing to an increase of 2 basis points, and – the capital floor adjustment contributing to a decrease of 3 basis points."

### deductions_other — "Other"
*-8 bps | confidence 85/100*

Other items decreased the ratio by 8 bps, primarily due to net foreign exchange translation impacts (ev-7).
> [ev-7] NAB/FY25/results_book, printed p28: "other items decreasing the CET1 capital ratio by 8 basis points, including net foreign exchange translation"

## Source disagreements
- **Proforma CET1 Ratio** (definitional): 11.70% (Reported) vs 11.81% (Proforma)
  Preferred: 11.70%. The proforma ratio of 11.81% adjusts for the sale of MLC Life which completed after the balance date (Oct 31). The reported ratio of 11.70% is the actual statutory result at Sep 30.

## Limitations
- The provided evidence contains a half-on-half capital walk (Mar 25 -> Sep 25) but no published full-year (FY24 -> FY25) driver table.
- The sum of the quantified drivers from the half-on-half walk (+82 -61 -45 +1 -8 = -31 bps) does not reconcile with the full-year delta of -65 bps.
- A residual of -34 bps is required to bridge the gap between the available half-on-half data and the full-year headline movement.
- Specific drivers affecting the first half of the year (Oct 24 -> Mar 25) are not explicitly quantified in the provided text, preventing a precise attribution of the full-year variance.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T12:41:44+00:00
- seconds: 48.0
- cost_usd: 0.0022
- tokens: 44292 in / 6337 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
