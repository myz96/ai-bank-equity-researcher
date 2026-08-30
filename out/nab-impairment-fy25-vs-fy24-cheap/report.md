# NAB — impairment — FY25 vs FY24

**Movement (cash basis):** 728$m → 833$m (+105$m) | **Attribution confidence:** 90/100

*Read from: row 'Total credit impairment charge', column FY24 -> column FY25*

NAB's credit impairment charge (CIC) rose $105 million to $833 million in FY25 (vs $728 million in FY24). The increase was driven by a $328 million rise in individually assessed provisions ($964m vs $636m), reflecting new and increased provisions of $1,061 million against write-backs of $(178) million and recoveries of $(50) million. This was partially offset by a $223 million swing in collective provisions from a $92 million charge to a $131 million release, largely due to a $283 million release from forward-looking adjustments.

> [ev-1] NAB/FY25/results_book, printed p24: "Total credit impairment charge 833 728 14.4"
> [ev-4] NAB/FY25/results_book, printed p24: "Credit impairment charge increased by $105 million or 14.4% to $833 million"
> [ev-20] NAB/FY25/results_book, PDF p5: "Credit impairment charge was $833 million, versus a FY24 charge of $728 million."
> [ev-21] NAB/FY25/results_book, PDF p5: "The FY25 charge includes individually assessed charges of $964 million and a $131 million release from collective provisions."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `individual_provisions` | Individually assessed credit impairment charge | +328 $m | 85 | 1 (single_source) | ev-2, ev-15 |
| `collective.asset_quality` | Collective credit impairment charge | -223 $m | 85 | 1 (single_source) | ev-3, ev-22 |

### individual_provisions — "Individually assessed credit impairment charge"
*+328 $m | confidence 85/100*

The individually assessed charge increased by $328 million to $964 million (ev-2). This comprised new/increased provisions of $1,061 million, partially offset by write-backs of $(178) million and recoveries of $(50) million (ev-15).
> [ev-2] NAB/FY25/results_book, printed p24: "Individually assessed credit impairment charge increased by $328 million or 51.6% to $964 million"
> [ev-15] NAB/FY25/results_book, PDF p53: "Credit impairment charge New and increased provisions (net of collective provision releases) 1,061 968 606 455 Write-backs of individually assessed provisions (178) (132) (97) (81) Recoveries of amounts previously written-off (50) (95) (24) (26) Total charge to the income statement 833 741 485 348"

### collective.asset_quality — "Collective credit impairment charge"
*-223 $m | confidence 85/100*

Collective provisions swung from a $92 million charge to a $131 million release, a $223 million improvement (ev-3). The release included a $283 million benefit from forward-looking adjustments, offset by volume growth and asset quality deterioration (ev-22).
> [ev-3] NAB/FY25/results_book, printed p24: "Collective credit impairment charge decreased by $223 million from a charge of $92 million to a write-back of $131 million."
> [ev-22] NAB/FY25/results_book, PDF p5: "The $131 million release from collective provisions includes a $283 million release from forward-looking provisions, partially offset by the impact of volume growth in the B&PB business lending portfolio, combined with asset quality deterioration."

## Source disagreements
- **FY24 Individually Assessed Charge Level** (definitional): 636.0 (derived: ev-15) vs 728.0 (ev-23)
  Preferred: 636.0. Ev-2 states the FY25 charge is $964m with a delta of +$328m, implying an FY24 level of $636m. Ev-23 lists 'Individually assessed FY24' as $728m, which matches the Total CIC figure rather than the individual component. The derived value is consistent with the stated delta.

## Limitations
- Divisional breakdown of the CIC movement is not provided in the evidence records; attribution is limited to the Individual vs Collective split.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T16:34:00+00:00
- seconds: 63.3
- cost_usd: 0.0021
- tokens: 38726 in / 7155 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
