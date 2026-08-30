# NAB — impairment — FY25 vs FY24

**Movement (cash basis):** 728$m → 833$m (+105$m) | **Attribution confidence:** 90/100

*Read from: row 'Total credit impairment charge', column FY24 -> column FY25*

NAB's credit impairment charge (CIC) increased by $105 million to $833 million in FY25 (vs $728 million in FY24). The increase was driven by a $328 million rise in individually assessed provisions, primarily in Corporate and Institutional Banking due to specific customer impairments and the non-recurrence of prior-year write-backs. This was partially offset by a $223 million decrease in collective provisions, which swung from a $92 million charge to a $131 million release.

> [ev-1] NAB/FY25/results_book, printed p24: "Total credit impairment charge 833 728 14.4"
> [ev-4] NAB/FY25/results_book, printed p24: "Credit impairment charge increased by $105 million or 14.4% to $833 million, driven by a higher level of individually assessed credit impairment charge primarily in Corporate and Institutional Banking. This was partially offset by a lower level of collective credit impairment charge."
> [ev-21] NAB/FY25/results_book, PDF p5: "Credit impairment charge was $833 million, versus a FY24 charge of $728 million."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `individual_provisions` | Individually assessed credit impairment charge | +328 $m | 85 | 1 (single_source) | ev-2 |
| `collective.asset_quality` | Collective credit impairment charge | -223 $m | 85 | 1 (single_source) | ev-3 |

### individual_provisions — "Individually assessed credit impairment charge"
*+328 $m | confidence 85/100*

Increased by $328 million to $964 million. Driven by higher charges in C&IB for a small number of customers and the non-recurrence of write-backs/recoveries seen in Sep 2024. Also saw modest increases in Business/Private Banking, NZ Banking, and unsecured retail portfolios.
> [ev-2] NAB/FY25/results_book, printed p24: "Individually assessed credit impairment charge increased by $328 million or 51.6% to $964 million mainly due to: an increased charge in Corporate and Institutional Banking for the impairment of a small number of customers combined with the non-recurrence of write-backs and recoveries for a small number of customers in the September 2024 full year, and a modest increase in charge across the Business and Private Banking and New Zealand Banking business lending portfolios and the unsecured retail portfolio in Personal Banking."

### collective.asset_quality — "Collective credit impairment charge"
*-223 $m | confidence 85/100*

Decreased by $223 million, swinging from a $92 million charge in FY24 to a $131 million write-back in FY25. Reflects improving asset quality and volume dynamics offsetting forward-looking adjustments.
> [ev-3] NAB/FY25/results_book, printed p24: "Collective credit impairment charge decreased by $223 million from a charge of $92 million to a write-back of $131 million."

## Source disagreements
- **Total CIC FY24 Level** (definitional): $728m (ev-1, ev-21) vs $741m (ev-18)
  Preferred: $728m. The results book summary table (ev-1) and narrative (ev-21) state $728m. A detailed roll-forward table (ev-18) shows $741m. The summary/narrative figures are prioritized as the headline reported metric.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T12:42:35+00:00
- seconds: 50.6
- cost_usd: 0.0022
- tokens: 39817 in / 7751 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
