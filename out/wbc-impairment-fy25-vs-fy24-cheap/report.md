# WBC — impairment — FY25 vs FY24

**Movement (ex_notables basis):** 537$m → 424$m (-113$m) | **Attribution confidence:** 60/100

*Read from: row 'Total impairment (charges)/benefits', column Total impairment FY24 -> column Total impairment FY25*

The credit impairment charge fell $113 million to $424 million (5 bps of average loans), down from $537 million (7 bps) in FY24. The reduction was driven by a significant increase in write-backs and recoveries, partially offset by higher collective assessed provisions (CAP).

> [ev-1] WBC/FY25/results_announcement, PDF p21: "Total impairment (charges)/benefits"
> [ev-2] WBC/FY25/results_announcement, PDF p21: "The credit impairment charge of $424 million represented 5 basis points of average loans, down from 7 basis points in the prior year."
> [ev-3] WBC/FY25/results_announcement, PDF p21: "The lower impairment charge was mainly due to an increase in write-backs and recoveries partly offset by a higher CAP charge."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `write_backs_recoveries` | Write-backs and recoveries | -281 $m | 60 | 1 (single_source) | ev-3, ev-5 |
| `collective.asset_quality` | Collectively assessed provisions (CAP) | +61 $m | 80 | 1 (single_source) | ev-7, ev-4 |
| `individual_provisions` | Individually assessed provisions (IAP) | +174 $m | 80 | 1 (single_source) | ev-6, ev-5 |
| *residual (unexplained)* | — | -67 $m | — | — |

### write_backs_recoveries — "Write-backs and recoveries"
*-281 $m | confidence 60/100*

Bank states the lower charge was 'mainly due to an increase in write-backs and recoveries' (ev-3). In FY25, IAP recoveries were $247m and write-backs $195m (ev-5). Combined with CAP recoveries implied by the net benefit, this driver reduced the charge significantly compared to FY24.
> [ev-3] WBC/FY25/results_announcement, PDF p21: "The lower impairment charge was mainly due to an increase in write-backs and recoveries partly offset by a higher CAP charge."
> [ev-5] WBC/FY25/results_announcement, PDF p21: "The IAP benefit of $34 million comprised: New IAPs of $408 million... Recoveries of $247 million... Write-backs of $195 million..."

### collective.asset_quality — "Collectively assessed provisions (CAP)"
*+61 $m | confidence 80/100*

CAP charges increased from $397m in FY24 to $458m in FY25 (ev-7). This $61m rise in expense was partly offset by other changes in CAP benefits of $103m against write-offs of $561m (ev-4).
> [ev-7] WBC/FY25/results_announcement, PDF p21: "Collectively assessed provisions (CAPs) Total CAPs"
> [ev-4] WBC/FY25/results_announcement, PDF p21: "The CAP charge of $458 million comprised write-offs of $561 million which was partly offset by a benefit in other changes in CAP of $103 million."

### individual_provisions — "Individually assessed provisions (IAP)"
*+174 $m | confidence 80/100*

IAP moved from a net benefit of $140m in FY24 to a net benefit of $34m in FY25 (ev-6). This represents a $174m increase in the net charge (or decrease in benefit), driven by new IAPs of $408m offset by recoveries and write-backs (ev-5).
> [ev-6] WBC/FY25/results_announcement, PDF p21: "Individually assessed provisions (IAPs) Total IAPs, write-backs and recoveries"
> [ev-5] WBC/FY25/results_announcement, PDF p21: "The IAP benefit of $34 million comprised: New IAPs of $408 million... Recoveries of $247 million... Write-backs of $195 million..."

## Limitations
- The bank's narrative attributes the movement mainly to write-backs/recoveries and CAP, but does not provide a quantified bridge for the total impairment charge delta. The residual of -$67m likely reflects unquantified movements in collective volume or overlays not explicitly broken out in the provided text.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T19:06:04+00:00
- seconds: 36.7
- cost_usd: 0.0018
- tokens: 41056 in / 4637 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['WBC/FY25/results_announcement p61 <- p2 page 61']
