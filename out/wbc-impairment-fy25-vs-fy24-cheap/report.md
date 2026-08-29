# WBC — impairment — FY25 vs FY24

**Movement (ex_notables basis):** -537$m → -424$m (+113$m) | **Attribution confidence:** 40/100

*Read from: row 'Total impairment (charges)/benefits', column FY24 -> column FY25*

WBC's credit impairment charge improved by $113 million to $424 million in FY25 (5 bps of average loans), down from $537 million (7 bps) in FY24. The improvement was driven by a significant reduction in write-offs and higher recoveries, partially offset by increased forward-looking overlays.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `write_backs_recoveries` | Recoveries and Write-backs | +442 $m | 80 | 1 (single_source) | ev-5 |
| `overlays_fla` | Overlays | -108 $m | 80 | 1 (single_source) | ev-8 |
| `individual_provisions` | New IAPs | -408 $m | 80 | 1 (single_source) | ev-5 |
| `write_offs_direct` | Write-offs | +561 $m | 80 | 1 (single_source) | ev-4 |
| *residual (unexplained)* | — | -174 $m | — | — |

### write_backs_recoveries — "Recoveries and Write-backs"
*+442 $m | confidence 80/100*

Net benefit of $442m ($247m recoveries + $195m write-backs). This is a major positive driver compared to the prior year's lower recovery environment.
> [ev-5] WBC/FY25/results_announcement, PDF p21: "The IAP benefit of $34 million comprised: New IAPs of $408 million... Recoveries of $247 million... and Write-backs of $195 million..."

### collective.volume — "Portfolio Growth"
*unquantified | confidence 60/100*

The bank does not explicitly quantify portfolio growth as a separate provision driver in the provided text. It is implicitly included in the collective provision movement but cannot be isolated with certainty.

### overlays_fla — "Overlays"
*-108 $m | confidence 80/100*

Overlays increased by $108 million, representing a negative contribution to the P&L improvement. This reflects heightened forward-looking risk adjustments.
> [ev-8] WBC/FY25/investor_discussion_pack, printed p29: "Overlays increased $108m"

### individual_provisions — "New IAPs"
*-408 $m | confidence 80/100*

New individually assessed provisions were $408 million. While this is a cost, it is part of the net IAP benefit calculation which includes recoveries/write-backs.
> [ev-5] WBC/FY25/results_announcement, PDF p21: "The IAP benefit of $34 million comprised: New IAPs of $408 million... Recoveries of $247 million... and Write-backs of $195 million..."

### write_offs_direct — "Write-offs"
*+561 $m | confidence 80/100*

Write-offs were $561 million. The improvement in the total charge is significantly aided by a decrease in write-offs compared to FY24 levels (implied by the net CAP benefit context).
> [ev-4] WBC/FY25/results_announcement, PDF p21: "The CAP charge of $458 million comprised write-offs of $561 million which was partly offset by a benefit in other changes in CAP of $103 million."

## Source disagreements
- **Impairment Charge Rate** (definitional): 5 bps - ev-1/ev-3 vs 4 bps - ev-6
  Preferred: 5 bps. The results announcement (ev-1, ev-3) states 5 bps. The investor discussion pack (ev-6) states 4 bps. The results book is the primary source.

## Limitations
- The provided evidence lacks a full bridge of provision types (e.g., specific FY24 write-off and recovery values) required for a precise quantified reconciliation. The residual of -$174m captures unquantified drivers such as changes in Stage 3 IAP balances and other unmapped components.
- Divisional attribution is not available in the provided evidence records.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Failed check: drivers_reconcile (drivers +487.0 + residual -174.0 != delta +113.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T18:15:49+00:00
- seconds: 45.3
- cost_usd: 0.0016
- tokens: 35232 in / 4391 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['WBC/FY25/results_announcement p61 <- p2 page 61']
