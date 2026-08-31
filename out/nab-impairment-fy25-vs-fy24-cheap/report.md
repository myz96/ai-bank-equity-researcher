# NAB — impairment — FY25 vs FY24

**Movement (cash basis):** 728$m → 833$m (+105$m) | **Attribution confidence:** 85/100

*Read from: row 'Total credit impairment charge', column FY24 (Sep 2024) -> column FY25 (Sep 2025)*

NAB's credit impairment charge increased by $105 million to $833 million in FY25. The movement was driven by a $328 million increase in individually assessed provisions, primarily from Business lending and Australian unsecured retail portfolios. This was partially offset by a $223 million swing in collective provisions, which moved from a $92 million charge to a $131 million write-back due to forward-looking adjustments.

> [ev-1] NAB/FY25/results_book, printed p24: "Total credit impairment charge 833 728 14.4"
> [ev-2] NAB/FY25/results_book, printed p24: "Credit impairment charge increased by $105 million or 14.4% to $833 million"
> [ev-3] NAB/FY25/results_book, printed p24: "Individually assessed credit impairment charge increased by $328 million or 51.6% to $964 million"
> [ev-4] NAB/FY25/results_book, printed p24: "Collective credit impairment charge decreased by $223 million from a charge of $92 million to a write-back of $131 million."
> [ev-20] NAB/FY25/results_book, PDF p5: "Credit impairment charge was $833 million, versus a FY24 charge of $728 million."
> [ev-21] NAB/FY25/results_book, PDF p5: "The FY25 charge includes individually assessed charges of $964 million and a $131 million release from collective provisions."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `individual_provisions` | Individually assessed credit impairment charge | +328 $m | 85 | 1 (single_source) | ev-3, ev-22 |
| `overlays_fla` | Forward-looking provisions | -283 $m | 85 | 1 (single_source) | ev-23 |
| *residual (unexplained)* | — | +60 $m | — | — |

### individual_provisions — "Individually assessed credit impairment charge"
*+328 $m | confidence 85/100*

Individualy assessed charges rose $328 million to $964 million. The bank states these primarily relate to customers in the Group’s business lending portfolio and, to a lesser extent, the Australian unsecured retail portfolio (ev-3, ev-22).
> [ev-3] NAB/FY25/results_book, printed p24: "Individually assessed credit impairment charge increased by $328 million or 51.6% to $964 million"
> [ev-22] NAB/FY25/results_book, PDF p5: "Individually assessed charges primarily relate to customers in the Group’s business lending portfolio and, to a lesser extent, the Australian unsecured retail portfolio."

### overlays_fla — "Forward-looking provisions"
*-283 $m | confidence 85/100*

The $131 million collective write-back includes a $283 million release from forward-looking provisions (ev-23). This is part of the collective driver narrative.
> [ev-23] NAB/FY25/results_book, PDF p5: "The $131 million release from collective provisions includes a $283 million release from forward-looking provisions, partially offset by the impact of volume growth in the B&PB business lending portfolio, combined with asset quality deterioration."

### collective.volume — "Collective volume growth"
*unquantified | confidence 60/100*

The collective write-back was partially offset by the impact of volume growth in the B&PB business lending portfolio (ev-23). No specific quantified value for this sub-component is provided in the evidence.
> [ev-23] NAB/FY25/results_book, PDF p5: "The $131 million release from collective provisions includes a $283 million release from forward-looking provisions, partially offset by the impact of volume growth in the B&PB business lending portfolio, combined with asset quality deterioration."

### collective.asset_quality — "Collective asset quality"
*unquantified | confidence 60/100*

The collective write-back was also partially offset by asset quality deterioration (ev-23). No specific quantified value for this sub-component is provided in the evidence.
> [ev-23] NAB/FY25/results_book, PDF p5: "The $131 million release from collective provisions includes a $283 million release from forward-looking provisions, partially offset by the impact of volume growth in the B&PB business lending portfolio, combined with asset quality deterioration."

## Source disagreements
- **Total CIC Level** (definitional): 833 (ev-1, ev-2, ev-20) vs 741 (ev-15)
  Preferred: 833. The results book headline table (ev-1) and text (ev-2, ev-20) state the total charge is $833 million. A detailed breakdown table (ev-15) sums to $741 million. The headline figure is preferred per source hierarchy.
- **Individually Assessed Charge FY24** (rounding): 728 (ev-3 delta implies 964-328=636? No, ev-3 says 964 level. ev-24 says 728) vs 636 (implied by ev-3 delta 328 on 964 level) vs 728 (ev-24)
  Preferred: 636. Ev-3 states the FY25 level is 964 and the delta is +328, implying an FY24 level of 636. Ev-24 lists FY24 as 728. There is a discrepancy. However, ev-15 shows 'New and increased provisions' at 968 for FY24. The most consistent interpretation of the *charge* line items in ev-3 suggests the FY24 base was ~636. But ev-24 explicitly lists 'Individually assessed credit impairment FY24' as 728. Given the explicit table in ev-24, I will use 728 as the stated FY24 level, but note the delta in ev-3 might be net of something else or there is a rounding/disagreement. Actually, looking at ev-15, 'New and increased provisions' is 968. Writebacks are -132. Recoveries -95. Net = 741. This matches the total in ev-15. Ev-3 says Indiv Charge is 964. Collective is -131. Sum = 833. This matches ev-1. So Ev-3's delta of 328 implies FY24 Indiv Charge was 636. Ev-24 says FY24 Indiv Charge was 728. This is a disagreement. I will stick to the explicit levels in ev-24 for the 'from_value' if needed, but the driver contribution is based on the delta stated in ev-3. Wait, the task asks to attribute the movement. The movement is 105. The drivers sum to 328 (Indiv) - 223 (Coll) = 105. This works perfectly. The underlying FY24 levels in ev-24 (728/ -398) don't sum to the FY24 total in ev-1 (728). 728-398 = 330 != 728. Ev-24 seems to have different definitions or errors. I will rely on the deltas in ev-3 and ev-4 which sum correctly to the total delta in ev-2.

## Limitations
- The residual of $60 million represents unmapped components or rounding differences between the headline total and the sum of the primary drivers (Indiv + Coll).
- Sub-components of the collective provision driver (volume vs asset quality) are not quantified separately in the provided evidence.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T23:41:55+00:00
- seconds: 45.2
- cost_usd: 0.0021
- tokens: 37892 in / 7379 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
