# WBC — impairment — FY25 vs FY24

**Movement (ex_notables basis):** 537$m → 424$m (-113$m) | **Attribution confidence:** 40/100

*Read from: row 'Total impairment (charges)/benefits', column FY24 (Sep 2024) -> column FY25 (Sep 2025)*

The credit impairment charge fell $113 million to $424 million (5 bps of average loans), down from $537 million (7 bps) in FY24. The improvement was driven by a $174 million swing in write-backs and recoveries, partially offset by a $61 million increase in the collectively assessed provision charge.

> [ev-1] WBC/FY25/results_announcement, PDF p21: "Total impairment (charges)/benefits (424) (537) (21) (174) (250) (30)"
> [ev-2] WBC/FY25/results_announcement, PDF p21: "The credit impairment charge of $424 million represented 5 basis points of average loans, down from 7 basis points in the prior year."
> [ev-3] WBC/FY25/results_announcement, PDF p21: "The lower impairment charge was mainly due to an increase in write-backs and recoveries partly offset by a higher CAP charge."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `write_backs_recoveries` | Write-backs and recoveries | +174 $m | 80 | 2 () | ev-3, ev-6, ev-7, ev-12 |
| `collective.asset_quality` | Collectively assessed provisions | -61 $m | 80 | 1 (single_source) | ev-3, ev-4, ev-5, ev-8 |

### write_backs_recoveries — "Write-backs and recoveries"
*+174 $m | confidence 80/100*


> [ev-3] WBC/FY25/results_announcement, PDF p21: "The lower impairment charge was mainly due to an increase in write-backs and recoveries partly offset by a higher CAP charge."
> [ev-6] WBC/FY25/results_announcement, PDF p21: "The IAP benefit of $34 million comprised: New IAPs of $408 million... Recoveries of $247 million... Write-backs of $195 million..."
> [ev-7] WBC/FY25/results_announcement, PDF p21: "Individually assessed provisions (IAPs) New IAPs (408) (423)... Write-backs 195 93... Recoveries 247 190... Total IAPs, write-backs and recoveries 34 (140)"
> [ev-12] WBC/FY25/investor_discussion_pack, printed p49: "Higher Cards & Personal Loans recoveries"

### collective.asset_quality — "Collectively assessed provisions"
*-61 $m | confidence 80/100*

CAP charge increased $61 million ($458m FY25 vs $397m FY24). Write-offs rose $75m ($561m vs $486m) in cards/personal loans, partly offset by a $14m rise in other changes/benefits ($103m vs $89m).
> [ev-3] WBC/FY25/results_announcement, PDF p21: "The lower impairment charge was mainly due to an increase in write-backs and recoveries partly offset by a higher CAP charge."
> [ev-4] WBC/FY25/results_announcement, PDF p21: "The CAP charge of $458 million comprised write-offs of $561 million which was partly offset by a benefit in other changes in CAP of $103 million."
> [ev-5] WBC/FY25/results_announcement, PDF p21: "Write-offs were largely within the credit card and personal loan portfolios."
> [ev-8] WBC/FY25/results_announcement, PDF p21: "Collectively assessed provisions (CAPs) Write-offs (561) (486)... Other changes in CAPs 103 89... Total CAPs (458) (397)"

## Limitations
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Capped at 80: write_backs_recoveries +174 $m, collective.asset_quality -61 $m. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.
- Failed check: drivers_reconcile (drivers +113.0 + residual +0.0 != delta -113.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-31T00:56:01+00:00
- seconds: 38.0
- cost_usd: 0.002
- tokens: 42887 in / 5225 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['WBC/FY25/results_announcement p61 <- p2 page 61']
