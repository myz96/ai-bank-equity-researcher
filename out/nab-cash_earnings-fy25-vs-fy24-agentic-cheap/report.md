# NAB — cash_earnings — FY25 vs FY24

**Movement (cash basis):** 7102$m → 7091$m (-11$m) | **Attribution confidence:** 40/100

*Read from: row 'Cash earnings', column Year to Sep 24 $m -> column Year to Sep 25 $m*

NAB's cash earnings decreased by $11 million or 0.2% to $7,091 million in FY25 from $7,102 million in FY24. The decline was driven by higher credit impairment charges (+$105m), higher operating expenses (+$435m including $130m of payroll review and remediation costs), and higher income tax (+$27m), partially offset by higher net interest income (+$644m) and lower other operating income (-$67m). Statutory net profit fell $201 million to $6,759 million, reflecting non-cash items including $431 million of acquisition/integration/disposal costs ($295 million after tax), $49 million of amortisation of acquired intangibles ($36 million after tax), and $39 million of hedging gains ($28 million after tax). Underlying profit rose 1.3% to $10,965 million.

> [ev-11] NAB/FY25/results_book, PDF p9: "Cash earnings 7,091 7,102 (0.2)"
> [ev-14] NAB/FY25/results_book, printed p12: "Statutory net profit decreased by $201 million or 2.9%. Cash earnings decreased by $11 million or 0.2%."
> [ev-31] NAB/FY25/investor_presentation, printed p39: "Cash earnings 7,091 7,102 (11)"
> [ev-33] NAB/FY25/investor_presentation, printed p39: "Statutory net profit 6,759 6,960 (201)"
> [ev-5] NAB/FY25/results_book, PDF p9: "Underlying profit 10,965 10,823 1.3"

## Notable items
- Payroll review and remediation costs of $130 million ($101 million in personnel + $29 million in general expenses), all new in FY25
- Customer-related remediation charges of $102 million in net fees and commissions (FY24: $35 million)
- Fee reduction impact from business wind-downs and disposals of $66 million
- Acquisition, integration, disposal and closure costs of $431 million pre-tax ($295 million after tax) excluded from cash earnings
- Amortisation of acquired intangible assets of $49 million pre-tax ($36 million after tax) added back to cash earnings
- Hedging and fair value volatility of $39 million pre-tax ($28 million after tax) excluded from cash earnings

## Source disagreements
- **Statutory vs cash earnings movement** (definitional): statutory: -$201m vs cash: -$11m
  Preferred: cash: -$11m. The task asks for cash earnings movement. Statutory net profit moved -$201 million while cash earnings moved -$11 million. The $190 million difference reflects the year-on-year change in non-cash items: acquisitions/integration/disposals costs rose from $174m pre-tax in FY24 to $431m pre-tax in FY25 (+$257m adverse), hedging volatility improved from $13m pre-tax loss to $39m pre-tax gain (+$52m favourable), and amortisation worsened from $42m to $49m (+$7m adverse). These are statutory-to-cash reconciling items, not drivers of the cash earnings movement.

## Limitations
- No walk/bridge chart was found in either document decomposing the cash earnings movement into component bars; all driver values were computed as deltas between FY25 and FY24 period columns from the results table on page 9 of the results book, capping confidence at 80 for computed deltas.
- The investor presentation corroborates the headline cash earnings figure ($7,091m FY25 vs $7,102m FY24, -$11m) but does not provide a separate FY25 v FY24 bridge chart.
- The bank does not separately quantify volume vs margin contributions to NII in dollar terms for the full-year comparison; the volume/rate analysis table on page 64 provides a total NII movement of $646 million (volume $1,204m, rate -$558m) which differs slightly from the stated $644 million movement, likely due to rounding or basis differences.
- The $420 million productivity benefit is mentioned in narrative but not quantified as a separate line item in any table; it is embedded within the overall expense figures.
- Failed check: no_quantified_drivers

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-31T01:12:34+00:00
- seconds: 220.8
- cost_usd: 0.1238
- tokens: 2530110 in / 13350 out
- orchestration: agent
- tool_calls: 65
- pages_read: 28
- charts_read: 0
- budget_exhausted: no
