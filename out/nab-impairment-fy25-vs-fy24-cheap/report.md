# NAB — impairment — FY25 vs FY24

**Movement (cash basis):** 728$m → 833$m (+105$m) | **Attribution confidence:** 90/100

*Read from: row 'Total credit impairment charge', column FY24 -> column FY25*

NAB's credit impairment charge (CIC) increased by $105 million (+14.4%) to $833 million in FY25 (vs $728 million in FY24). The increase was driven entirely by a $328 million rise in individually assessed provisions ($964m vs $636m), which was partially offset by a $223 million swing in collective provisions from a $92 million charge to a $131 million write-back. Net write-offs to GLAs rose 1 bps to 0.07%.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `individual_provisions` | Individually assessed credit impairment charge | +328 $m | 85 | 1 (single_source) | ev-3, ev-13, ev-14, ev-15 |
| `collective.asset_quality` | Collective credit impairment charge | -223 $m | 85 | 2 () | ev-4, ev-23 |

### individual_provisions — "Individually assessed credit impairment charge"
*+328 $m | confidence 85/100*

Individualy assessed charges rose $328 million to $964 million (ev-3). This reflects new and increased provisions of $1,061 million (ev-13), partially offset by write-backs of $178 million (ev-14) and recoveries of $50 million (ev-15).
> [ev-3] NAB/FY25/results_book, printed p24: "Individually assessed credit impairment charge increased by $328 million or 51.6% to $964 million"
> [ev-13] NAB/FY25/results_book, PDF p53: "Credit impairment charge New and increased provisions (net of collective provision releases)"
> [ev-14] NAB/FY25/results_book, PDF p53: "Credit impairment charge Write-backs of individually assessed provisions"
> [ev-15] NAB/FY25/results_book, PDF p53: "Credit impairment charge Recoveries of amounts previously written-off"

### collective.asset_quality — "Collective credit impairment charge"
*-223 $m | confidence 85/100*

Collective provisions swung from a $92 million charge to a $131 million write-back, a $223 million improvement (ev-4). The presentation notes 'no underlying collective provisioning charge' due to volume growth and asset quality improvements being offset by transfers to individual provisions (ev-23).
> [ev-4] NAB/FY25/results_book, printed p24: "Collective credit impairment charge decreased by $223 million from a charge of $92 million to a write-back of $131 million."
> [ev-23] NAB/FY25/investor_presentation, printed p26: "No underlying collective provisioning charge3 - volume growth and reducing impact from asset quality, offset by transfers to individual provisions"

## Source disagreements
- **Collective Provision Levels** (definitional): -$131m (Results Book ev-4) vs -$398m (Results Book Table ev-18)
  Preferred: -$131m. The Results Book narrative (ev-4) explicitly states the collective charge was a $131 million write-back, summing with the $964 million individual charge to match the total CIC of $833 million. The table in ev-18 appears to use a different classification or basis for 'Collective' that is inconsistent with the primary P&L attribution.

## Limitations
- Divisional breakdown of the CIC movement is not provided in the evidence records; only aggregate provision-type splits are available.
- The bank does not disclose specific drivers for the individual provision increase beyond 'new and increased provisions'.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-29T18:09:44+00:00
- seconds: 50.7
- cost_usd: 0.0018
- tokens: 34249 in / 5924 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
