# NAB — roe — FY25 vs FY24

**Movement (cash basis):** 11.6ppt → 11.4ppt (-0.2ppt) | **Attribution confidence:** 80/100

*Read from: row 'Cash return on equity', column FY24 -> column FY25*

NAB's Cash ROE declined by 20 bps to 11.4% in FY25 (ev-8). Earnings fell slightly (-$11m) while average equity rose ($1.3bn), with the equity effect dominating the decline.

> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"
> [ev-4] NAB/FY25/results_book, PDF p71: "Cash earnings 7,091 7,102 3,508 3,583"
> [ev-5] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -0.02 ppt | 80 | 2 () | ev-8, ev-17 |
| `equity_effect` | — | -0.18 ppt | 80 | 1 (single_source) | ev-8, ev-5 |
| *residual (unexplained)* | — | -0 ppt | — | — |

### earnings_effect
*-0.02 ppt | confidence 80/100*

Derived: Prior ROE (11.6%) x earnings growth rate (-0.15%). Earnings fell $11m (ev-17). Contribution is derived, not disclosed.
> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"
> [ev-17] NAB/FY25/investor_presentation, printed p39: "Cash earnings 7,091 7,102 (11) 3,508 3,583 (75)"

### equity_effect
*-0.18 ppt | confidence 80/100*

Derived: Total delta (-0.2 ppt) minus earnings effect (-0.02 ppt). Equity grew ~2.2% (ev-5), diluting returns. Contribution is derived, not disclosed.
> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"
> [ev-5] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314"

## Source disagreements
- **Cash ROE Level** (definitional): 11.4% (Results Book ev-8) vs 10.7% (Investor Presentation ev-11)
  Preferred: 11.4%. The Results Book (ev-8) is the primary source per hierarchy. The IP (ev-11) likely uses a different denominator or basis.

## Limitations
- Drivers are mathematically derived from KPI endpoints and profit/equity movements, not explicitly stated by the bank as a bridge.
- Interaction term is absorbed into the equity effect.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T16:31:29+00:00
- seconds: 54.0
- cost_usd: 0.0018
- tokens: 34879 in / 5462 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['NAB/FY25/investor_presentation p39 <- p5 page 39', 'NAB/FY25/investor_presentation p10 <- p39 page 10 [added]']
