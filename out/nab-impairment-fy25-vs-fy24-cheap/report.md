# NAB — impairment — FY25 vs FY24

**Movement (cash basis):** 728$m → 833$m (+105$m) | **Attribution confidence:** 90/100

*Read from: row 'Total credit impairment charge', column FY24 -> column FY25*

NAB's credit impairment charge (CIC) rose $105 million to $833 million in FY25 (vs $728 million in FY24). The increase was driven by a $328 million rise in individually assessed provisions ($964m vs $636m), partially offset by a $223 million swing in collective provisions from a $92 million charge to a $131 million write-back.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `individual_provisions` | Individually assessed credit impairment charge | +328 $m | 90 | 2 () | ev-2, ev-22, ev-36, ev-47 |
| `collective.asset_quality` | Collective credit impairment charge | -223 $m | 90 | 2 () | ev-3, ev-22, ev-28 |

### individual_provisions — "Individually assessed credit impairment charge"
*+328 $m | confidence 90/100*

Individualy assessed charges increased $328 million to $964 million (ev-2). This reflects higher specific provisioning on business lending, including customers in C&IB and BNZ (ev-36, ev-47).
> [ev-2] NAB/FY25/results_book, printed p24: "Individually assessed credit impairment charge increased by $328 million or 51.6% to $964 million"
> [ev-22] NAB/FY25/results_book, PDF p5: "The FY25 charge includes individually assessed charges of $964 million and a $131 million release from collective provisions."
> [ev-36] NAB/FY25/investor_presentation, printed p28: "IAP of $1.2bn, $0.2bn higher than Mar 25 reflecting higher business lending impairments including a small number of customers in both C&IB and NZ Banking"
> [ev-47] NAB/FY25/investor_presentation, printed p85: "$243m increase in 2H25 mainly related to a small number of customers in both C&IB and BNZ, combined with B&PB business lending"

### collective.asset_quality — "Collective credit impairment charge"
*-223 $m | confidence 90/100*

Collective provisions swung from a $92 million charge to a $131 million write-back, a $223 million improvement (ev-3). The bank notes no underlying collective provisioning charge, with volume growth and reducing asset quality impact offset by transfers to individual provisions (ev-28).
> [ev-3] NAB/FY25/results_book, printed p24: "Collective credit impairment charge decreased by $223 million from a charge of $92 million to a write-back of $131 million."
> [ev-22] NAB/FY25/results_book, PDF p5: "The FY25 charge includes individually assessed charges of $964 million and a $131 million release from collective provisions."
> [ev-28] NAB/FY25/investor_presentation, printed p26: "No underlying collective provisioning charge3 - volume growth and reducing impact from asset quality, offset by transfers to individual provisions"

## Source disagreements
- **Investor Presentation CIC Definition** (definitional): 833 (Results Book) vs -89 (Investor Presentation)
  Preferred: 833. The Investor Presentation table (ev-24) lists 'Credit impairment charge (CIC)' as -89m for FY25, which contradicts the Results Book headline of 833m. The IP figure likely represents a net release or excludes specific components included in the statutory/cash P&L line item reported in the Results Book. We follow the Results Book as the primary source.

## Limitations
- Divisional breakdowns are not explicitly quantified in the provided evidence records for the full year comparison, so the narrative relies on aggregate provision type splits and high-level commentary on business lending drivers.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-29T21:02:29+00:00
- seconds: 58.0
- cost_usd: 0.0023
- tokens: 40147 in / 8180 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
