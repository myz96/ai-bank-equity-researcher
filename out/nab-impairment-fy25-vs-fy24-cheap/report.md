# NAB — impairment — FY25 vs FY24

**Movement (cash basis):** 728$m → 833$m (+105$m) | **Attribution confidence:** 90/100

*Read from: row 'Total credit impairment charge', column FY24 -> column FY25*

NAB's credit impairment charge (CIC) increased by $105 million to $833 million in FY25 (vs $728 million in FY24). The increase was driven by a $328 million rise in individually assessed provisions, partially offset by a $223 million swing in collective provisions from a $92 million charge to a $131 million write-back.

> [ev-1] NAB/FY25/results_book, printed p24: "Total credit impairment charge 833 728 14.4"
> [ev-4] NAB/FY25/results_book, printed p24: "Credit impairment charge increased by $105 million or 14.4% to $833 million"
> [ev-23] NAB/FY25/results_book, PDF p5: "Credit impairment charge was $833 million, versus a FY24 charge of $728 million."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `individual_provisions` | Individually assessed credit impairment charge | +328 $m | 85 | 1 (single_source) | ev-2, ev-15, ev-16, ev-17 |
| `collective.asset_quality` | Collective credit impairment charge | -223 $m | 90 | 2 () | ev-3, ev-29, ev-30, ev-39 |

### individual_provisions — "Individually assessed credit impairment charge"
*+328 $m | confidence 85/100*

Increased by $328 million to $964 million. Driven by new and increased provisions of $1,061 million (FY24: $968 million), partially offset by larger write-backs ($178m vs $132m) and recoveries ($50m vs $95m).
> [ev-2] NAB/FY25/results_book, printed p24: "Individually assessed credit impairment charge increased by $328 million or 51.6% to $964 million"
> [ev-15] NAB/FY25/results_book, PDF p53: "Credit impairment charge New and increased provisions (net of collective provision releases) 1,061 968 606 455"
> [ev-16] NAB/FY25/results_book, PDF p53: "Credit impairment charge Write-backs of individually assessed provisions (178) (132) (97) (81)"
> [ev-17] NAB/FY25/results_book, PDF p53: "Credit impairment charge Recoveries of amounts previously written-off (50) (95) (24) (26)"

### collective.asset_quality — "Collective credit impairment charge"
*-223 $m | confidence 90/100*

Swung from a $92 million charge to a $131 million write-back (-$223 million total). Reflects a net release from forward-looking adjustments (FLAs) of $89 million and no underlying collective provisioning charge.
> [ev-3] NAB/FY25/results_book, printed p24: "Collective credit impairment charge decreased by $223 million from a charge of $92 million to a write-back of $131 million."
> [ev-29] NAB/FY25/investor_presentation, printed p26: "Underlying CP charge/(write-back) ($m)"
> [ev-30] NAB/FY25/investor_presentation, printed p26: "Forward looking provisions ($m)"
> [ev-39] NAB/FY25/investor_presentation, printed p86: "Net release of FLAs mainly relating to Retail Trade, Construction and Commercial Property"

## Source disagreements
- **Total CIC Level** (definitional): 833 - results_book vs 348 - investor_presentation
  Preferred: 833 - results_book. The investor presentation table reports an 'underlying' or 'statutory' metric excluding specific items, while the results book KPI and narrative report the statutory cash earnings impact of $833 million.

## Limitations
- The divisional breakdown of the CIC movement is not explicitly quantified in the provided evidence records, so the driver attribution relies on the aggregate Individual vs Collective split.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T19:01:17+00:00
- seconds: 57.7
- cost_usd: 0.0019
- tokens: 37728 in / 6236 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
