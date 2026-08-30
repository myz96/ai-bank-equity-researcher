# NAB — impairment — FY25 vs FY24

**Movement (cash basis):** 728$m → 833$m (+105$m) | **Attribution confidence:** 90/100

*Read from: row 'Total credit impairment charge', column FY24 -> column FY25*

NAB's credit impairment charge (CIC) increased by $105 million (+14.4%) to $833 million in FY25 (vs $728 million in FY24). The increase was driven by a $328 million rise in individually assessed provisions, partially offset by a $223 million swing in collective provisions from a $92 million charge to a $131 million write-back.

> [ev-1] NAB/FY25/results_book, printed p24: "Total credit impairment charge 833 728 14.4"
> [ev-2] NAB/FY25/results_book, printed p24: "Credit impairment charge increased by $105 million or 14.4% to $833 million"
> [ev-3] NAB/FY25/results_book, printed p24: "Individually assessed credit impairment charge increased by $328 million or 51.6% to $964 million"
> [ev-4] NAB/FY25/results_book, printed p24: "Collective credit impairment charge decreased by $223 million from a charge of $92 million to a write-back of $131 million."
> [ev-28] NAB/FY25/results_book, PDF p5: "Credit impairment charge was $833 million, versus a FY24 charge of $728 million."
> [ev-29] NAB/FY25/results_book, PDF p5: "The FY25 charge includes individually assessed charges of $964 million and a $131 million release from collective provisions."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `individual_provisions` | Individually assessed credit impairment charge | +328 $m | 85 | 1 (single_source) | ev-3, ev-21, ev-22 |
| `collective.asset_quality` | Collective credit impairment charge | -223 $m | 90 | 2 () | ev-4, ev-37 |

### individual_provisions — "Individually assessed credit impairment charge"
*+328 $m | confidence 85/100*

The bank states the individually assessed charge increased by $328 million or 51.6% to $964 million (ev-3). This reflects new and increased provisions for single-name credits, which were partially offset by write-backs of $178 million and recoveries of $50 million (ev-21, ev-22).
> [ev-3] NAB/FY25/results_book, printed p24: "Individually assessed credit impairment charge increased by $328 million or 51.6% to $964 million"
> [ev-21] NAB/FY25/results_book, PDF p53: "Credit impairment charge Write-backs of individually assessed provisions"
> [ev-22] NAB/FY25/results_book, PDF p53: "Credit impairment charge Recoveries of amounts previously written-off"

### collective.asset_quality — "Collective credit impairment charge"
*-223 $m | confidence 90/100*

The collective charge swung by $223 million, moving from a $92 million charge in FY24 to a $131 million write-back in FY25 (ev-4). This release is attributed to improved asset quality and forward-looking adjustments, including an $89 million net release from forward-looking provisions (ev-37).
> [ev-4] NAB/FY25/results_book, printed p24: "Collective credit impairment charge decreased by $223 million from a charge of $92 million to a write-back of $131 million."
> [ev-37] NAB/FY25/investor_presentation, printed p85: "Net $89m release from forward-looking provisions"

## Source disagreements
- **Total CIC Level** (definitional): 833 - ev-1/ev-28 vs 741 - ev-19
  Preferred: 833. The results book summary table (ev-1) and narrative (ev-28) state the total CIC is $833 million. A detailed breakdown table (ev-19) lists a 'Total charge to the income statement' of $741 million. The $833 million figure is consistent with the sum of the individually assessed ($964m) and collective (-$131m) components disclosed in the primary narrative (ev-29), making it the correct headline measure.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T15:02:08+00:00
- seconds: 63.4
- cost_usd: 0.0022
- tokens: 39481 in / 7530 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
