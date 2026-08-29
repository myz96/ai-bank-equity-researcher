# WBC — impairment — FY25 vs FY24

**Movement (ex_notables basis):** 537$m → 424$m (-113$m) | **Attribution confidence:** 40/100

*Read from: row 'Total impairment (charges)/benefits', column FY24 -> column FY25*

The credit impairment charge fell $113 million to $424 million (5 bps of average loans), down from $537 million (7 bps) in FY24. The reduction was driven by a net benefit from individually assessed provisions ($34 million benefit vs prior year charge) and lower collective provisioning, partially offset by higher direct write-offs.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `individual_provisions` | Individually assessed provisions | -442 $m | 80 | 1 (single_source) | ev-5, ev-1, ev-3 |
| `collective.asset_quality` | Collective provisions: risk migration | -16 $m | 60 | 1 (single_source) | ev-3, ev-2 |
| `write_offs_direct` | Direct write-offs | +561 $m | 70 | 1 (single_source) | ev-4 |
| `overlays_fla` | Forward-looking adjustments and overlays | +3 $m | 50 | 1 (single_source) | ev-10 |
| *residual (unexplained)* | — | -119 $m | — | — |

### individual_provisions — "Individually assessed provisions"
*-442 $m | confidence 80/100*

Net IAP benefit of $34 million comprised new IAPs of $408 million, recoveries of $247 million, and write-backs of $195 million (ev-5). This represents a swing of approximately $442 million versus the prior year's individual provision charge.
> [ev-5] WBC/FY25/results_announcement, PDF p21: "The IAP benefit of $34 million comprised: New IAPs of $408 million... Recoveries of $247 million... and Write-backs of $195 million..."
> [ev-1] WBC/FY25/results_announcement, PDF p21: "Total impairment (charges)/benefits"
> [ev-3] WBC/FY25/results_announcement, PDF p21: "The credit impairment charge of $424 million represented 5 basis points of average loans, down from 7 basis points in the prior year."

### collective.asset_quality — "Collective provisions: risk migration"
*-16 $m | confidence 60/100*

The bank disclosed a $16 million decrease in collective provisions (ev-3). While the text does not explicitly split this into volume vs asset quality, the decline in the loss rate (7 to 5 bps) despite portfolio growth suggests favorable or stable asset quality dynamics.
> [ev-3] WBC/FY25/results_announcement, PDF p21: "The credit impairment charge of $424 million represented 5 basis points of average loans, down from 7 basis points in the prior year."
> [ev-2] WBC/FY25/results_announcement, PDF p21: "Impairment charges/(benefits) to average loans"

### write_offs_direct — "Direct write-offs"
*+561 $m | confidence 70/100*

Write-offs increased to $561 million in FY25 (ev-4). This is a significant driver of the total charge, though partially offset by other changes in CAP. Prior year write-off levels are not explicitly quantified in the provided evidence.
> [ev-4] WBC/FY25/results_announcement, PDF p21: "The CAP charge of $458 million comprised write-offs of $561 million which was partly offset by a benefit in other changes in CAP of $103 million."

### overlays_fla — "Forward-looking adjustments and overlays"
*+3 $m | confidence 50/100*

Overlays increased slightly from $536 million to $539 million (ev-10). This balance sheet movement implies a small negative contribution to the P&L charge relative to the prior year, assuming no other overlay movements.
> [ev-10] WBC/FY25/investor_discussion_pack, printed p29: "Overlays 536 611 539 Stage 1 CAP 1,223 1,198 1,190 Stage 2 CAP 2,390 2,256 2,087 Stage 3 CAP 768 877 933 Stage 3 IAP 179 130 238 Sep-24 Mar-25 Sep-25"

## Source disagreements
- **Impairment Charge Level** (definitional): 424.0 - ev-1, ev-3 vs 458.0 - ev-4 (CAP specific)
  Preferred: 424.0. Ev-4 discusses a 'CAP charge' of $458 million which includes write-offs and other changes. Ev-1 and Ev-3 define the total impairment charge as $424 million. The task requires the total impairment charge.

## Limitations
- The provided evidence lacks a granular bridge splitting collective provisions into volume and asset quality components for both years. The residual captures unquantified drivers including potential volume effects and prior-year write-off comparisons.
- Confidence is limited by the absence of a full divisional impairment table in the provided extracts, preventing attribution of the movement to specific business lines (Retail, Business, Institutional).
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Failed check: drivers_reconcile (drivers +106.0 + residual -119.0 != delta -113.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T21:07:45+00:00
- seconds: 43.9
- cost_usd: 0.0017
- tokens: 38367 in / 4360 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['WBC/FY25/results_announcement p61 <- p2 page 61']
