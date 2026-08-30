# NAB — roe — FY25 vs FY24

**Movement (cash basis):** 11.6ppt → 11.4ppt (-0.2ppt) | **Attribution confidence:** 75/100

*Read from: row 'Cash return on equity', column Year to Sep 24 -> column Year to Sep 25*

NAB's Cash ROE declined 20 bps (2.0 ppt) to 11.4% in FY25 from 11.6% in FY24. The decline was driven primarily by a modestly larger average equity base (equity effect of approximately −18 ppt), which more than offset a small positive contribution from cash earnings at constant equity (earnings effect of approximately +2 ppt). Cash earnings were broadly stable year-on-year ($7,091m vs $7,102m), declining by just $11m or 0.2%, while average attributable equity rose from $61,039m to $62,355m (+$1,316m or 2.2%), reflecting retained earnings and share count dynamics including on-market buybacks.

> [ev-5] NAB/FY25/results_book, PDF p71: "Cash return on equity 11.4% 11.6%"
> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps)"
> [ev-14] NAB/FY25/results_book, printed p6: "Cash earnings were broadly stable compared with FY24 including higher credit impairment charges. Cash EPS rose 1% and cash ROE was 11.4%."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Cash earnings movement | +0.018 ppt | 80 | 1 (single_source) | ev-5, ev-6, ev-11, ev-14 |
| `equity_effect` | Average equity movement | -0.182 ppt | 80 | 1 (single_source) | ev-5, ev-7, ev-13 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect — "Cash earnings movement"
*+0.018 ppt | confidence 80/100*

Derived: prior-period ROE (11.6%) × earnings growth rate (−0.15%). Cash earnings fell $11m to $7,091m from $7,102m, broadly stable per the bank's own description (ev-14). At constant equity, this tiny earnings decline would have reduced ROE by approximately 1.8 ppt. The value is derived, not disclosed.
> [ev-5] NAB/FY25/results_book, PDF p71: "Cash return on equity 11.4% 11.6%"
> [ev-6] NAB/FY25/results_book, PDF p71: "Cash earnings 7,091 7,102"
> [ev-11] NAB/FY25/results_book, printed p68: "Cash earnings(1) 7,091 7,102"
> [ev-14] NAB/FY25/results_book, printed p6: "Cash earnings were broadly stable compared with FY24 including higher credit impairment charges. Cash EPS rose 1% and cash ROE was 11.4%."

### equity_effect — "Average equity movement"
*-0.182 ppt | confidence 80/100*

Derived: total delta (−20 ppt) minus earnings effect (+1.8 ppt). Average attributable equity rose $1,316m to $62,355m from $61,039m (ev-7), a 2.2% increase driven by retained earnings partially offset by on-market share buybacks completed during FY25 (referenced on page 8 as a driver of CET1 ratio decline). The value is derived, not disclosed.
> [ev-5] NAB/FY25/results_book, PDF p71: "Cash return on equity 11.4% 11.6%"
> [ev-7] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039"
> [ev-13] NAB/FY25/results_book, printed p58: "Total equity (attributable to owners of the Company) 62,922 62,169 61,455"

## Limitations
- No walk/bridge chart for ROE movement was found in either document; the earnings and equity effects are arithmetic derivations, not bank-disclosed decompositions.
- The full-year CET1 capital movement bridge was not located; only the half-year bridge (Mar 25 to Sep 25) was available on page 30 of the results book.
- The equity effect direction is supported by the rise in average attributable equity from $61,039m to $62,355m, but the bank does not provide a formal decomposition of the ROE movement into earnings and equity components.
- Movement delta normalised from -2.0 to -0.2 (unit slip against the endpoints).
- Identity contributions restated from -16.40 to -0.1640 ppt: the identity closes on the movement delta at the ratio's own scale and not at the scale they were written on, and a contribution larger than the ratio itself cannot be a movement of that ratio. A growth rate enters a ratio identity as a fraction, and a dollar movement enters it divided by the identity's denominator.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T20:00:39+00:00
- seconds: 113.0
- cost_usd: 0.0441
- tokens: 1196506 in / 7701 out
- orchestration: agent
- tool_calls: 45
- pages_read: 10
- charts_read: 0
- budget_exhausted: no
