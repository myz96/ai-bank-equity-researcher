# NAB — roe — FY25 vs FY24

**Movement (cash basis):** 11.6ppt → 11.4ppt (-0.2ppt) | **Attribution confidence:** 80/100

*Read from: row 'Cash return on equity', column FY24 -> column FY25*

NAB's Cash ROE declined by 20 bps to 11.4% in FY25 (ev-8). Earnings fell slightly (-$11m) while average equity rose ($1.3b), resulting in a negative earnings effect and a larger negative equity effect.

> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"
> [ev-4] NAB/FY25/results_book, PDF p71: "Cash earnings 7,091 7,102"
> [ev-5] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -0.02 ppt | 80 | 2 () | ev-4, ev-5, ev-8, ev-18 |
| `equity_effect` | — | -0.18 ppt | 80 | 2 () | ev-4, ev-5, ev-8, ev-18 |
| *residual (unexplained)* | — | -0 ppt | — | — |

### earnings_effect
*-0.02 ppt | confidence 80/100*

Derived: Prior ROE (11.6%) x Earnings Growth Rate (-0.15%). Earnings fell $11m from $7,102m to $7,091m (ev-4, ev-18).
> [ev-4] NAB/FY25/results_book, PDF p71: "Cash earnings 7,091 7,102"
> [ev-5] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039"
> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"
> [ev-18] NAB/FY25/investor_presentation, printed p39: "Cash earnings 7,091 7,102 (11) 3,508 3,583 (75)"

### equity_effect
*-0.18 ppt | confidence 80/100*

Derived: Total delta (-0.2 ppt) minus earnings effect (-0.02 ppt). Equity grew ~2.2% from $61,039m to $62,355m (ev-5), diluting the ratio despite stable earnings.
> [ev-4] NAB/FY25/results_book, PDF p71: "Cash earnings 7,091 7,102"
> [ev-5] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039"
> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"
> [ev-18] NAB/FY25/investor_presentation, printed p39: "Cash earnings 7,091 7,102 (11) 3,508 3,583 (75)"

## Limitations
- Drivers are derived via arithmetic identity (Level 1) rather than disclosed bridge tables.
- Interaction term is absorbed into the equity effect.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T23:40:04+00:00
- seconds: 30.9
- cost_usd: 0.0016
- tokens: 32927 in / 4394 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['NAB/FY25/investor_presentation p39 <- p5 page 39', 'NAB/FY25/investor_presentation p10 <- p39 page 10 [added]']
