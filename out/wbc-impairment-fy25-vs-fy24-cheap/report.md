# WBC — impairment — FY25 vs FY24

**Movement (ex_notables basis):** -537$m → -424$m (+113$m) | **Attribution confidence:** 40/100

*Read from: row 'Total impairment (charges)/benefits', column FY24 -> column FY25*

WBC's credit impairment charge improved by $113m to $424m in FY25 (ev-1). The loss rate fell from 7bps to 5bps of average loans (ev-2). This improvement was driven by lower write-offs and higher recoveries, partially offset by increased overlays.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `write_backs_recoveries` | Write-backs & recoveries | +120 $m | 85 | 1 (single_source) | ev-10, ev-12 |
| `write_offs_direct` | Write-offs direct | +76 $m | 80 | 1 (single_source) | ev-11 |
| `overlays_fla` | Overlays | -108 $m | 85 | 1 (single_source) | ev-16, ev-13 |
| `individual_provisions` | Individually assessed provisions | +72 $m | 85 | 1 (single_source) | ev-15, ev-9 |
| *residual (unexplained)* | — | -70 $m | — | — |

### write_backs_recoveries — "Write-backs & recoveries"
*+120 $m | confidence 85/100*

Net benefits increased by $120m, moving from a ($147m) benefit in FY24 to a ($27m) benefit in FY25 (ev-10). Higher Cards & Personal Loans recoveries contributed (ev-12).
> [ev-10] WBC/FY25/investor_discussion_pack, printed p49: "Impairment charges ($m) Write-backs & recoveries 2H24 (147) 1H25 (76) 2H25 (27)"
> [ev-12] WBC/FY25/investor_discussion_pack, printed p49: "Higher Cards & Personal Loans recoveries"

### write_offs_direct — "Write-offs direct"
*+76 $m | confidence 80/100*

Direct write-offs decreased by $76m, falling from $250m in FY24 to $174m in FY25 (ev-11). Note: FY25 H2 write-offs are not explicitly quantified in the provided table.
> [ev-11] WBC/FY25/investor_discussion_pack, printed p49: "Impairment charges ($m) Write-offs direct 2H24 250 1H25 174 2H25 N/A"

### overlays_fla — "Overlays"
*-108 $m | confidence 85/100*

Overlays increased by $108m in FY25 compared to FY24 (ev-16), representing a drag on the P&L improvement. This is partly offset by improvements in economics (ev-13).
> [ev-16] WBC/FY25/investor_discussion_pack, printed p29: "Overlays increased $108m"
> [ev-13] WBC/FY25/investor_discussion_pack, printed p49: "Improvement in economics, partly offset by overlays"

### individual_provisions — "Individually assessed provisions"
*+72 $m | confidence 85/100*

IAP charges decreased by $72m due to a single name write-off in the prior year impacting comparability (ev-15). New IAPs remained relatively stable at ~$280m (ev-9).
> [ev-15] WBC/FY25/investor_discussion_pack, printed p29: "IAP decreased $72m due to a single name write-off"
> [ev-9] WBC/FY25/investor_discussion_pack, printed p49: "Impairment charges ($m) New IAPs 2H24 275 1H25 279 2H25 282"

## Source disagreements
- **Impairment Charge Rate Definition** (definitional): 5 bps (ev-2, ev-3) vs 4 bps (ev-14)
  Preferred: 5 bps. The results announcement (ev-2, ev-3) states the charge was 5bps of average loans. The investor discussion pack (ev-14) mentions 4bps, likely excluding specific items or using a different denominator. We prioritize the results announcement for the headline metric.

## Limitations
- The sum of identified drivers (+120 + 76 - 108 + 72 = +160) does not fully reconcile with the total delta (+113), leaving a residual of -$70m. This residual may include unmapped components like collective volume/quality shifts or timing differences not explicitly broken out in the provided evidence.
- H2 FY25 write-offs are marked N/A in ev-11, preventing a precise full-year attribution for that component based solely on the quarterly table.
- Confidence is capped due to the unreconciled residual and reliance on stated movements rather than a full walk chart.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Failed check: drivers_reconcile (drivers +160.0 + residual -70.0 != delta +113.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T13:54:12+00:00
- seconds: 44.6
- cost_usd: 0.0018
- tokens: 36431 in / 5494 out
- orchestration: pipeline
