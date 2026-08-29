# NAB — roe — FY25 vs FY24

**Movement (cash basis):** 11.6ppt → 11.4ppt (-0.2ppt) | **Attribution confidence:** 80/100

*Read from: row 'Cash return on equity', column FY24 -> column FY25*

NAB's Cash ROE declined by 20 bps to 11.4% in FY25 (ev-8). This decline is driven by a negative earnings effect of approximately 23 bps due to a slight decrease in cash earnings, partially offset by a positive equity effect of approximately 3 bps as average equity increased.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -0.23 ppt | 80 | 2 () | ev-4, ev-6, ev-8, ev-15 |
| `equity_effect` | — | +0.03 ppt | 80 | 1 (single_source) | ev-5, ev-6, ev-8 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*-0.23 ppt | confidence 80/100*

Derived: Prior ROE (11.6%) multiplied by earnings growth (-0.15%). Earnings fell $11m from $7,102m to $7,091m (ev-4, ev-15). Value is derived, not disclosed.
> [ev-4] NAB/FY25/results_book, PDF p71: "Cash earnings 7,091 7,102 3,508 3,583"
> [ev-6] NAB/FY25/results_book, PDF p71: "Cash return on equity 11.4% 11.6% 11.0% 11.7%"
> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"
> [ev-15] NAB/FY25/investor_presentation, printed p39: "Cash earnings 7,091 7,102 (11) 3,508 3,583 (75)"

### equity_effect
*+0.03 ppt | confidence 80/100*

Derived: Total delta minus earnings effect. Average equity rose from $61,039m to $62,355m (ev-5), increasing the denominator and mitigating the earnings decline. Value is derived, not disclosed.
> [ev-5] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314"
> [ev-6] NAB/FY25/results_book, PDF p71: "Cash return on equity 11.4% 11.6% 11.0% 11.7%"
> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"

## Source disagreements
- **Cash ROE FY25 value** (restatement): 11.4% - NAB/FY25/results_book (ev-6) vs 10.7% - NAB/FY25/investor_presentation (ev-9)
  Preferred: 11.4%. The results book (ev-6) is the primary source per hierarchy. The presentation (ev-9) likely contains a typo or uses a different basis not specified.

## Limitations
- Earnings and equity effects are derived using arithmetic decomposition, not disclosed by the bank.
- Disagreement exists between sources for FY25 Cash ROE; results book preferred.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-29T21:00:09+00:00
- seconds: 43.7
- cost_usd: 0.0016
- tokens: 33605 in / 4630 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['NAB/FY25/investor_presentation p39 <- p5 page 39', 'NAB/FY25/investor_presentation p10 <- p39 page 10 [added]']
