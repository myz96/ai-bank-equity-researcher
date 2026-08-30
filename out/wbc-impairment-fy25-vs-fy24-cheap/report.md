# WBC — impairment — FY25 vs FY24

**Movement (ex_notables basis):** 537$m → 424$m (-113$m) | **Attribution confidence:** 60/100

*Read from: row 'Total impairment (charges)/benefits', column FY24 (Sep 2024) -> column FY25 (Sep 2025)*

The credit impairment charge fell $113 million to $424 million (5 bps of average loans), down from $537 million (7 bps) in FY24. The improvement was driven by a $174 million increase in write-backs and recoveries, partially offset by a $61 million rise in collectively assessed provisions.

> [ev-1] WBC/FY25/results_announcement, PDF p21: "Total impairment (charges)/benefits (424) (537) (21) (174) (250) (30)"
> [ev-2] WBC/FY25/results_announcement, PDF p21: "The credit impairment charge of $424 million represented 5 basis points of average loans, down from 7 basis points in the prior year."
> [ev-3] WBC/FY25/results_announcement, PDF p21: "The lower impairment charge was mainly due to an increase in write-backs and recoveries partly offset by a higher CAP charge."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `write_backs_recoveries` | Write-backs and recoveries | +174 $m | 80 | 2 () | ev-3, ev-6, ev-16 |
| `collective.asset_quality` | Collectively assessed provisions | -61 $m | 80 | 1 (single_source) | ev-3, ev-4, ev-5, ev-8 |
| `individual_provisions` | Individually assessed provisions | +174 $m | 80 | 1 (single_source) | ev-6, ev-7 |
| *residual (unexplained)* | — | -400 $m | — | — |

### write_backs_recoveries — "Write-backs and recoveries"
*+174 $m | confidence 80/100*

An increase in write-backs and recoveries of $174 million drove the improvement. This included higher Cards & Personal Loans recoveries (ev-16). New IAPs were $408m, with recoveries of $247m and write-backs of $195m (ev-6).
> [ev-3] WBC/FY25/results_announcement, PDF p21: "The lower impairment charge was mainly due to an increase in write-backs and recoveries partly offset by a higher CAP charge."
> [ev-6] WBC/FY25/results_announcement, PDF p21: "The IAP benefit of $34 million comprised: New IAPs of $408 million... Recoveries of $247 million... Write-backs of $195 million..."
> [ev-16] WBC/FY25/investor_discussion_pack, printed p49: "Higher Cards & Personal Loans recoveries"

### collective.asset_quality — "Collectively assessed provisions"
*-61 $m | confidence 80/100*

Higher CAP charges of $61 million ($458m vs $397m) offset some gains. This comprised write-offs of $561m partly offset by other changes in CAP of $103m (ev-4). Write-offs were largely in credit cards and personal loans (ev-5).
> [ev-3] WBC/FY25/results_announcement, PDF p21: "The lower impairment charge was mainly due to an increase in write-backs and recoveries partly offset by a higher CAP charge."
> [ev-4] WBC/FY25/results_announcement, PDF p21: "The CAP charge of $458 million comprised write-offs of $561 million which was partly offset by a benefit in other changes in CAP of $103 million."
> [ev-5] WBC/FY25/results_announcement, PDF p21: "Write-offs were largely within the credit card and personal loan portfolios."
> [ev-8] WBC/FY25/results_announcement, PDF p21: "Collectively assessed provisions (CAPs) Total CAPs (458) (397) 15 (255) (203) 26"

### individual_provisions — "Individually assessed provisions"
*+174 $m | confidence 80/100*

IAPs swung from a net benefit of $140m in FY24 to a net charge of $34m in FY25, a $174m negative contribution. This included new IAPs of $408m, recoveries of $247m, and write-backs of $195m (ev-6).
> [ev-6] WBC/FY25/results_announcement, PDF p21: "The IAP benefit of $34 million comprised: New IAPs of $408 million... Recoveries of $247 million... Write-backs of $195 million..."
> [ev-7] WBC/FY25/results_announcement, PDF p21: "Individually assessed provisions (IAPs) Total IAPs, write-backs and recoveries 34 (140) large 81 (47) large"

## Limitations
- The bank's narrative attributes the movement mainly to write-backs/recoveries and CAP charges. However, the sum of these two drivers (-61 + 174 = +113) only accounts for half the total delta (-113). The remaining -$174 swing in IAPs is explicitly quantified in the evidence (ev-6, ev-7) but not highlighted in the summary text, leading to a large residual if strictly following the prose attribution.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T15:07:37+00:00
- seconds: 54.8
- cost_usd: 0.002
- tokens: 43276 in / 5440 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['WBC/FY25/results_announcement p61 <- p2 page 61']
