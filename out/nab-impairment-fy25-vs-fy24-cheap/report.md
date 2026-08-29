# NAB — impairment — FY25 vs FY24

**Movement (cash basis):** 728$m → 833$m (+105$m) | **Attribution confidence:** 90/100

*Read from: row 'Total credit impairment charge', column FY24 -> column FY25*

NAB's credit impairment charge (CIC) increased by $105 million to $833 million in FY25. The rise was driven entirely by a $328 million increase in individually assessed provisions ($964m vs $636m), partially offset by a $223 million swing in collective provisions from a $92 million charge to a $131 million write-back.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `individual_provisions` | Individually assessed credit impairment charge | +328 $m | 85 | 1 (single_source) | ev-3, ev-14, ev-15 |
| `collective.asset_quality` | Collective credit impairment charge | -223 $m | 85 | 2 () | ev-4, ev-23 |

### individual_provisions — "Individually assessed credit impairment charge"
*+328 $m | confidence 85/100*

Individually assessed charges rose $328 million to $964 million (ev-3). This reflects increased specific provisions on single-name exposures, partially offset by write-backs and recoveries which totaled $228 million (ev-14, ev-15).
> [ev-3] NAB/FY25/results_book, printed p24: "Individually assessed credit impairment charge increased by $328 million or 51.6% to $964 million"
> [ev-14] NAB/FY25/results_book, PDF p53: "Write-backs of individually assessed provisions"
> [ev-15] NAB/FY25/results_book, PDF p53: "Recoveries of amounts previously written-off"

### collective.asset_quality — "Collective credit impairment charge"
*-223 $m | confidence 85/100*

Collective provisions swung from a $92 million charge to a $131 million write-back (-$223 million delta, ev-4). The results book notes 'no underlying collective provisioning charge' (ev-23), attributing the movement to reducing impact from asset quality and volume growth offsets.
> [ev-4] NAB/FY25/results_book, printed p24: "Collective credit impairment charge decreased by $223 million from a charge of $92 million to a write-back of $131 million."
> [ev-23] NAB/FY25/investor_presentation, printed p26: "No underlying collective provisioning charge3 - volume growth and reducing impact from asset quality, offset by transfers to individual provisions"

## Source disagreements
- **FY24 Collective Provision Level** (definitional): $92 million (ev-4 text) vs -$398 million (ev-18 table)
  Preferred: $92 million. The narrative text (ev-4) explicitly states the FY24 collective charge was $92 million, consistent with the total CIC of $728m minus individual provisions of $636m. The table in ev-18 appears to contain a labeling error or different scope for the 'Collective' row.

## Limitations
- The bank does not provide a granular bridge separating collective volume from collective risk migration; the driver is attributed to collective asset quality based on the 'no underlying CP' statement.
- Forward-looking adjustments are netted within the collective line in the primary disclosure.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-29T13:42:50+00:00
- seconds: 159.2
- cost_usd: 0.0018
- tokens: 33732 in / 6044 out
- orchestration: pipeline
