# WBC — impairment — FY25 vs FY24

**Movement (ex_notables basis):** 537$m → 424$m (-113$m) | **Attribution confidence:** 40/100

*Read from: row 'Total impairment (charges)/benefits', column Total impairment FY24 -> column Total impairment FY25*

The credit impairment charge fell $113 million to $424 million (5 bps of average loans), down from $537 million (7 bps) in FY24. The improvement was driven by higher write-backs and recoveries, partially offset by a larger collective provision charge.

> [ev-1] WBC/FY25/results_announcement, PDF p21: "Total impairment (charges)/benefits"
> [ev-2] WBC/FY25/results_announcement, PDF p21: "The credit impairment charge of $424 million represented 5 basis points of average loans, down from 7 basis points in the prior year."
> [ev-3] WBC/FY25/results_announcement, PDF p21: "The lower impairment charge was mainly due to an increase in write-backs and recoveries partly offset by a higher CAP charge."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `write_backs_recoveries` | Write-backs and recoveries | +194 $m | 80 | 2 () | ev-3, ev-6, ev-12 |
| `collective.asset_quality` | Collectively assessed provisions | -61 $m | 80 | 1 (single_source) | ev-3, ev-4, ev-5, ev-8 |
| `individual_provisions` | Individually assessed provisions | -174 $m | 80 | 1 (single_source) | ev-6, ev-7 |

### write_backs_recoveries — "Write-backs and recoveries"
*+194 $m | confidence 80/100*

Net write-backs and recoveries improved the charge by $194 million. This comprised $247 million in recoveries and $195 million in write-backs (ev-6). The bank attributes this to 'Higher Cards & Personal Loans recoveries' (ev-12).
> [ev-3] WBC/FY25/results_announcement, PDF p21: "The lower impairment charge was mainly due to an increase in write-backs and recoveries partly offset by a higher CAP charge."
> [ev-6] WBC/FY25/results_announcement, PDF p21: "The IAP benefit of $34 million comprised: New IAPs of $408 million... Recoveries of $247 million... Write-backs of $195 million..."
> [ev-12] WBC/FY25/investor_discussion_pack, printed p49: "Higher Cards & Personal Loans recoveries"

### collective.asset_quality — "Collectively assessed provisions"
*-61 $m | confidence 80/100*

The collective provision charge increased by $61 million ($397m to $458m) (ev-8). This included $561 million in write-offs, largely in credit cards and personal loans (ev-4, ev-5), partly offset by other changes in CAP benefits of $103 million (ev-4).
> [ev-3] WBC/FY25/results_announcement, PDF p21: "The lower impairment charge was mainly due to an increase in write-backs and recoveries partly offset by a higher CAP charge."
> [ev-4] WBC/FY25/results_announcement, PDF p21: "The CAP charge of $458 million comprised write-offs of $561 million which was partly offset by a benefit in other changes in CAP of $103 million."
> [ev-5] WBC/FY25/results_announcement, PDF p21: "Write-offs were largely within the credit card and personal loan portfolios."
> [ev-8] WBC/FY25/results_announcement, PDF p21: "Collectively assessed provisions (CAPs) Total CAPs"

### individual_provisions — "Individually assessed provisions"
*-174 $m | confidence 80/100*

The individually assessed provision benefit decreased by $174 million (a $140m benefit to a $34m benefit) (ev-7). This was due to new IAPs of $408 million, partially offset by recoveries and write-backs (ev-6).
> [ev-6] WBC/FY25/results_announcement, PDF p21: "The IAP benefit of $34 million comprised: New IAPs of $408 million... Recoveries of $247 million... Write-backs of $195 million..."
> [ev-7] WBC/FY25/results_announcement, PDF p21: "Individually assessed provisions (IAPs) Total IAPs, write-backs and recoveries"

## Limitations
- The movement is derived from the net change in provision categories rather than a direct walk chart. Confidence is capped at 80 as the arithmetic delta is computed by the analyst.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Failed check: drivers_reconcile (drivers -41.0 + residual +0.0 != delta -113.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T12:47:40+00:00
- seconds: 47.7
- cost_usd: 0.002
- tokens: 42148 in / 5881 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['WBC/FY25/results_announcement p61 <- p2 page 61']
