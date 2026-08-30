# WBC — impairment — FY25 vs FY24

**Movement (ex_notables basis):** 537$m → 424$m (-113$m) | **Attribution confidence:** 80/100

*Read from: row 'Total impairment (charges)/benefits', column Total impairment FY24 -> column Total impairment FY25*

The credit impairment charge fell $113 million to $424 million (5 bps of average loans), down from $537 million (7 bps) in FY24. The reduction was primarily driven by higher write-backs and recoveries, partially offset by a higher Collective Provisioning (CAP) charge.

> [ev-1] WBC/FY25/results_announcement, PDF p21: "Total impairment (charges)/benefits"
> [ev-3] WBC/FY25/results_announcement, PDF p21: "The credit impairment charge of $424 million represented 5 basis points of average loans, down from 7 basis points in the prior year."
> [ev-4] WBC/FY25/results_announcement, PDF p21: "The lower impairment charge was mainly due to an increase in write-backs and recoveries partly offset by a higher CAP charge."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `write_backs_recoveries` | Write-backs and recoveries | +168 $m | 80 | 2 () | ev-7, ev-15 |
| `collective.asset_quality` | Collective provision charge | -281 $m | 80 | 1 (single_source) | ev-5, ev-6 |
| *residual (unexplained)* | — | +0 $m | — | — |

### write_backs_recoveries — "Write-backs and recoveries"
*+168 $m | confidence 80/100*

An increase in write-backs and recoveries reduced the charge. This included $247 million in recoveries and $195 million in write-backs against new IAPs of $408 million, resulting in a net IAP benefit of $34 million (ev-7). Higher Cards & Personal Loans recoveries were noted as a key driver (ev-15).
> [ev-7] WBC/FY25/results_announcement, PDF p21: "The IAP benefit of $34 million comprised: New IAPs of $408 million... Recoveries of $247 million... Write-backs of $195 million..."
> [ev-15] WBC/FY25/investor_discussion_pack, printed p49: "Higher Cards & Personal Loans recoveries"

### collective.asset_quality — "Collective provision charge"
*-281 $m | confidence 80/100*

A higher CAP charge increased the impairment expense. The CAP charge rose to $458 million, comprising $561 million in write-offs (largely in credit cards and personal loans) partly offset by a $103 million benefit in other changes in CAP (ev-5).
> [ev-5] WBC/FY25/results_announcement, PDF p21: "The CAP charge of $458 million comprised write-offs of $561 million which was partly offset by a benefit in other changes in CAP of $103 million."
> [ev-6] WBC/FY25/results_announcement, PDF p21: "Write-offs were largely within the credit card and personal loan portfolios."

## Limitations
- The bank's narrative attributes the movement to 'higher write-backs' and 'higher CAP charge'. The quantified bridge uses the specific components disclosed for these categories: Net IAP Benefit ($34m) and CAP Charge ($458m). The residual is zero because the sum of these two drivers (-$281m + $168m = -$113m) exactly matches the headline delta.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T16:38:43+00:00
- seconds: 40.1
- cost_usd: 0.0019
- tokens: 42669 in / 5124 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['WBC/FY25/results_announcement p61 <- p2 page 61']
