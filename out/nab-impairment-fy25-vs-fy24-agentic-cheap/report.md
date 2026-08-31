# NAB — impairment — FY25 vs FY24

**Movement (cash basis):** 728$m → 833$m (+105$m) | **Attribution confidence:** 85/100

*Read from: row 'Total credit impairment charge', column Year to Sep 24 $m -> column Year to Sep 25 $m*

NAB’s credit impairment charge (CIC) rose $105 million (+14.4%) to $833 million in FY25 from $728 million in FY24. The increase was driven by a $328 million rise in individually assessed charges (from $636m to $964m), primarily in Corporate & Institutional Banking (+$153m to $146m charge) and Business & Private Banking (+$6m to $529m), partially offset by a $223 million swing in collective provisions from a $92m charge to a $131m write-back, driven by a $283m release of forward-looking provisions.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `individual_provisions` | — | +328 $m | 80 | 1 (single_source) | ev-2, ev-3, ev-6, ev-7, ev-8, ev-9 |
| `overlays_fla` | — | -223 $m | 80 | 1 (single_source) | ev-2, ev-4, ev-5 |
| `other_unmapped` | — | +0 $m | 80 | 1 (single_source) | ev-6, ev-7, ev-8, ev-9 |

### individual_provisions
*+328 $m | confidence 80/100*

Individually assessed charges rose $328 million (51.6%) to $964 million (FY24: $636 million). This was driven by higher charges in Corporate & Institutional Banking for impairments of a small number of larger customers plus non-recurrence of prior-year write-backs/recoveries, and modest increases across B&PB business lending, NZ Banking, and unsecured retail portfolios.
> [ev-2] NAB/FY25/results_book, PDF p5: "The FY25 charge includes individually assessed charges of $964 million and a $131 million release from collective provisions."
> [ev-3] NAB/FY25/results_book, printed p24: "Total individually assessed credit impairment charge 964 636 51.6"
> [ev-6] NAB/FY25/results_book, printed p38: "Credit impairment (charge) / write-back (146) 7 large"
> [ev-7] NAB/FY25/results_book, printed p34: "Credit impairment charge (529) (523) 1.1"
> [ev-8] NAB/FY25/results_book, printed p36: "Credit impairment charge (255) (288) (11.5)"
> [ev-9] NAB/FY25/results_book, printed p42: "Credit impairment (charge) / write-back (25) (129) (80.6)"

### overlays_fla
*-223 $m | confidence 80/100*

Collective provisions swung from a $92 million charge in FY24 to a $131 million write-back in FY25 ($223 million improvement). The FY25 write-back was driven by a net release of forward-looking provisions including a $283 million release from target sector FLAs (including $215 million from Agri FLA), partially offset by volume growth and asset quality deterioration in B&PB business lending and Australian mortgage portfolios.
> [ev-2] NAB/FY25/results_book, PDF p5: "The FY25 charge includes individually assessed charges of $964 million and a $131 million release from collective provisions."
> [ev-4] NAB/FY25/results_book, printed p24: "Collective credit impairment (write-back) / charge (131) 92 large"
> [ev-5] NAB/FY25/results_book, printed p24: "Total credit impairment charge 833 728 14.4"

### other_unmapped
*+0 $m | confidence 80/100*

Corporate Functions & Other showed a credit impairment write-down of $83 million (from $205m write-back in FY24 to $122m in FY25), reflecting lower net releases of forward-looking provisions and non-repeat of methodology refinement impacts. New Zealand Banking improved $104 million (from $129m charge to $25m charge) due to forward-looking provision write-backs including Agri FLA release, partially offset by lending growth and higher individually assessed charges for a small number of business customers.
> [ev-6] NAB/FY25/results_book, printed p38: "Credit impairment (charge) / write-back (146) 7 large"
> [ev-7] NAB/FY25/results_book, printed p34: "Credit impairment charge (529) (523) 1.1"
> [ev-8] NAB/FY25/results_book, printed p36: "Credit impairment charge (255) (288) (11.5)"
> [ev-9] NAB/FY25/results_book, printed p42: "Credit impairment (charge) / write-back (25) (129) (80.6)"

## Limitations
- No primary-period walk chart found in the investor presentation; the provision-type bridge is built from results book tables (page 26) which state the movement components directly.
- Divisional deltas sum to $105m (C&IB +153, B&PB +6, PB -33, NZ -104, Corp Func +83), matching the total movement, but the bank does not publish a single consolidated divisional CIC table with both periods side-by-side; figures were extracted from separate divisional pages.
- The bank's prose attributes the individually assessed increase to 'a small number of customers' in C&IB and NZ Banking and 'modest increase' in B&PB and unsecured retail, but does not provide granular sub-component dollar breakdowns within individually assessed charges beyond the new/increased, write-backs, and recoveries split on page 26.
- Write-offs are embedded in the individually assessed charge but not separately quantified in the FY24-FY25 comparison narrative; page 53 shows write-offs of $600m in FY25 vs $512m in FY24 as part of the ECL rollforward, but these are balance-sheet movements, not the P&L charge drivers.
- Research stopped early: the tool-call budget (80 calls) was reached, so the evidence behind this answer is less complete than a full run's.
- Capped at 80: individual_provisions +328 $m, overlays_fla -223 $m. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-31T00:31:41+00:00
- seconds: 212.5
- cost_usd: 0.1307
- tokens: 3339785 in / 9792 out
- orchestration: agent
- tool_calls: 80
- pages_read: 57
- charts_read: 0
- budget_exhausted: the tool-call budget (80 calls)
