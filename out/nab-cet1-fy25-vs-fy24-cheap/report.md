# NAB — cet1 — FY25 vs FY24

**Movement (cash basis):** 1235bps → 1170bps (-65bps) | **Attribution confidence:** 60/100

*Read from: row 'Capital ratios CET1', column 30 Sep 24 -> column 30 Sep 25*

NAB's APRA CET1 ratio declined by 65 bps to 11.70% in FY25 (ev-1, ev-12). The movement is driven primarily by credit RWA growth and dividend payments, partially offset by cash earnings generation.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `rwa.credit` | Credit RWA | -45 bps | 85 | 1 (single_source) | ev-2, ev-5, ev-6, ev-7, ev-8 |
| `dividend_net_drp` | Dividend | -61 bps | 85 | 1 (single_source) | ev-2 |
| `earnings_generation` | Cash earnings | +82 bps | 85 | 1 (single_source) | ev-2 |
| `other_unmapped` | Other items | -8 bps | 85 | 1 (single_source) | ev-2, ev-10 |
| `rwa` | Other RWA | +1 bps | 85 | 1 (single_source) | ev-2, ev-9 |
| *residual (unexplained)* | — | -34 bps | — | — |

### rwa.credit — "Credit RWA"
*-45 bps | confidence 85/100*

Credit RWA increased, decreasing the CET1 ratio by 45 bps. This includes volume growth (-27 bps), asset quality deterioration (-5 bps), and model/methodology changes (-13 bps) (ev-2, ev-5, ev-6, ev-7, ev-8).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01, Cash earnings 0.82, Dividend (0.61), Credit RWA¹ (0.45), Other RWA 0.01, Other (0.08), Sep 25 11.70"
> [ev-5] NAB/FY25/results_book, printed p28: "an increase in credit RWA decreasing the CET1 capital ratio by 45 basis points"
> [ev-6] NAB/FY25/results_book, printed p28: "volume growth contributing to a decrease of 27 basis points"
> [ev-7] NAB/FY25/results_book, printed p28: "asset quality deterioration contributing to a decrease of 5 basis points"
> [ev-8] NAB/FY25/results_book, printed p28: "model and methodology changes contributing to a decrease of 13 basis points"

### dividend_net_drp — "Dividend"
*-61 bps | confidence 85/100*

Dividends paid during the period decreased the CET1 ratio by 61 bps (ev-2).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01, Cash earnings 0.82, Dividend (0.61), Credit RWA¹ (0.45), Other RWA 0.01, Other (0.08), Sep 25 11.70"

### earnings_generation — "Cash earnings"
*+82 bps | confidence 85/100*

Cash earnings generated capital, increasing the CET1 ratio by 82 bps (ev-2).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01, Cash earnings 0.82, Dividend (0.61), Credit RWA¹ (0.45), Other RWA 0.01, Other (0.08), Sep 25 11.70"

### other_unmapped — "Other items"
*-8 bps | confidence 85/100*

Other items decreased the CET1 ratio by 8 bps (ev-2, ev-10).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01, Cash earnings 0.82, Dividend (0.61), Credit RWA¹ (0.45), Other RWA 0.01, Other (0.08), Sep 25 11.70"
> [ev-10] NAB/FY25/results_book, printed p28: "other items decreasing the CET1 capital ratio by 8 basis points"

### rwa — "Other RWA"
*+1 bps | confidence 85/100*

Decrease in other (non-credit) RWA increased the CET1 ratio by 1 bps (ev-2, ev-9).
> [ev-2] NAB/FY25/results_book, printed p28: "Movements in CET1 capital ratio (%) Mar 25 12.01, Cash earnings 0.82, Dividend (0.61), Credit RWA¹ (0.45), Other RWA 0.01, Other (0.08), Sep 25 11.70"
> [ev-9] NAB/FY25/results_book, printed p28: "a decrease in other (non-credit) RWA increasing the CET1 capital ratio by 1 basis point"

## Source disagreements
- **Pro-forma adjustment** (definitional): 11.70% reported (ev-1) vs 11.81% pro-forma (ev-14)
  Preferred: 11.70%. The pro-forma ratio of 11.81% reflects the sale of MLC Life which completed after the balance date (Oct 31, 2025). The task requires the reported statutory movement.

## Limitations
- The bank's published capital walk (ev-2) covers the half-on-half period (Mar 25 to Sep 25), not the full year (Sep 24 to Sep 25).
- The sum of the drivers from the half-on-half walk (-131 bps) does not reconcile with the full-year delta (-65 bps).
- Full-year specific drivers for dividends and earnings are not explicitly quantified in the provided text; the half-on-half values are used as proxies but may differ due to H1 impacts.
- A residual of -34 bts remains unexplained, likely due to H1 movements or differences in the composition of 'Other' items between periods.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-29T13:40:10+00:00
- seconds: 214.5
- cost_usd: 0.0018
- tokens: 37586 in / 5160 out
- orchestration: pipeline
