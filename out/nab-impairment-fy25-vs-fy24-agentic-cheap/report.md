# NAB — impairment — FY25 vs FY24

**Movement (cash basis):** 728$m → 833$m (+105$m) | **Attribution confidence:** 85/100

*Read from: row 'Total credit impairment charge', column Year to Sep 24 $m -> column Year to Sep 25 $m*

NAB's credit impairment charge (CIC) rose $105 million or 14.4% to $833 million in FY25 from $728 million in FY24, lifting the annualised loss rate on gross loans and acceptances by 1 basis point to 0.11%. The increase was driven by a $328 million rise in individually assessed charges (to $964 million, up 51.6%), primarily from Corporate & Institutional Banking where impairments for a small number of larger customers plus non-recurrence of prior-year write-backs and recoveries pushed the divisional charge from a $7 million write-back to $146 million (+$153 million). This was partially offset by a $223 million swing in collective provisions from a $92 million charge to a $131 million write-back, driven by a $283 million release from forward-looking provisions including a $215 million release from target sector FLAs, partially offset by volume growth and asset quality deterioration in Business & Private Banking business lending.

> [ev-6] NAB/FY25/results_book, printed p24: "Total credit impairment charge 833 728 14.4"
> [ev-29] NAB/FY25/results_book, printed p24: "Individually assessed credit impairment charge increased by $328 million or 51.6% to $964 million"
> [ev-27] NAB/FY25/results_book, printed p24: "Collective credit impairment charge decreased by $223 million from a charge of $92 million to a write-back of $131 million."
> [ev-12] NAB/FY25/results_book, printed p24: "Credit impairment charge to GLAs - annualised 0.11 0.10 1 bp"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `individual_provisions` | Individually assessed credit impairment charge | +328 $m | 85 | 1 (single_source) | ev-7, ev-9, ev-10, ev-11, ev-29, ev-30, ev-31 |
| `collective.asset_quality` | Collective credit impairment (write-back) / charge | -223 $m | 85 | 1 (single_source) | ev-8, ev-27, ev-28, ev-40 |

### individual_provisions — "Individually assessed credit impairment charge"
*+328 $m | confidence 85/100*

Individually assessed charges rose $328 million (51.6%) to $964 million. New and increased provisions jumped $329 million to $1,192 million (up 38.1%), driven by impairments for a small number of larger customers in C&IB and modest increases across B&PB business lending, NZ Banking business lending, and unsecured retail. Write-backs grew $46 million to $178 million (non-recurrence of prior-year recoveries/write-backs in C&IB). Recoveries fell $45 million to $50 million.
> [ev-7] NAB/FY25/results_book, printed p24: "Total individually assessed credit impairment charge 964 636 51.6"
> [ev-9] NAB/FY25/results_book, printed p24: "Individually assessed credit impairment charge New and increased 1,192 863 38.1"
> [ev-10] NAB/FY25/results_book, printed p24: "Write-backs (178) (132) 34.8"
> [ev-11] NAB/FY25/results_book, printed p24: "Recoveries of amounts previously written off (50) (95) (47.4)"
> [ev-29] NAB/FY25/results_book, printed p24: "Individually assessed credit impairment charge increased by $328 million or 51.6% to $964 million"
> [ev-30] NAB/FY25/results_book, PDF p41: "Credit impairment charge up $153m"
> [ev-31] NAB/FY25/results_book, PDF p41: "The increase was due to higher individually assessed provision charges reflecting impairments for a small number of larger customers in addition to the non-recurrence of recoveries and write-backs from the prior year, partially offset by collective provision write-backs."

### collective.asset_quality — "Collective credit impairment (write-back) / charge"
*-223 $m | confidence 85/100*

Collective provisions swung $223 million from a $92 million charge to a $131 million write-back. The $131 million write-back was driven by a net release of forward-looking provisions ($283 million decrease including $215 million from target sector FLAs) combined with release of provisions held for customers transferring to individually assessed. Partially offset by volume growth in B&PB business lending and asset quality deterioration across Australian lending.
> [ev-8] NAB/FY25/results_book, printed p24: "Collective credit impairment (write-back) / charge (131) 92 large"
> [ev-27] NAB/FY25/results_book, printed p24: "Collective credit impairment charge decreased by $223 million from a charge of $92 million to a write-back of $131 million."
> [ev-28] NAB/FY25/results_book, printed p24: "The write-back for the September 2025 full year of $131 million was driven by a net release of forward-looking provisions, combined with the release of provisions held for customers that transferred to individually assessed during the September 2025 full year. This was partially offset by the impact of volume growth in the Business and Private Banking business lending portfolio, combined with deterioration in asset quality across the Australian lending portfolio."
> [ev-40] NAB/FY25/results_book, PDF p27: "a decrease of $283 million in forward-looking provisions, including a $215 million release from target sector forward-looking adjustments (FLAs)"

### other_unmapped — "Corporate Functions and Other"
*unquantified | confidence 80/100*

Corporate Functions and Other reported a credit impairment write-back of $122 million (FY24: $205 million), a decrease of $83 million. The lower write-back was due to reduced net releases of forward-looking provisions and non-repeat of methodology refinement impacts. This is an enabling unit, not a revenue-generating division.
> [ev-17] NAB/FY25/results_book, PDF p45: "Credit impairment write-back 122 205 (40.5)"
> [ev-38] NAB/FY25/results_book, PDF p45: "Credit impairment write-back down $83m, 40.5%"
> [ev-39] NAB/FY25/results_book, PDF p45: "The decrease was due to a lower level of net releases of the forward-looking provisions and the non-repeat of the impact of methodology refinements."

## Limitations
- The provision-type bridge from page 53 (new/increased + write-backs + recoveries) sums to $741 million for FY24, which differs by $13 million from the $728 million reported on page 26; this discrepancy is noted but not resolved in the available documents.
- The collective driver narrative does not provide a precise numerical split between volume growth, asset quality deterioration, and forward-looking provision releases within the $223 million swing beyond the $283 million FLA release figure.
- No primary-period walk chart was found in either document; the driver table is built from the results book KPI table and divisional tables rather than a single reconciled bridge.
- The investor presentation corroborates the $833 million / $728 million levels and the individually assessed / collective split but does not publish a separate FY25 v FY24 movement bridge.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T14:39:14+00:00
- seconds: 204.0
- cost_usd: 0.0989
- tokens: 2715381 in / 11798 out
- orchestration: agent
- tool_calls: 72
- pages_read: 27
- charts_read: 0
- budget_exhausted: no
