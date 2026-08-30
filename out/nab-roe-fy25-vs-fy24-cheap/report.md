# NAB — roe — FY25 vs FY24

**Movement (cash basis):** 11.6ppt → 11.4ppt (-0.2ppt) | **Attribution confidence:** 80/100

*Read from: row 'Cash return on equity', column FY24 -> column FY25*

NAB's Cash ROE declined by 20 bps to 11.4% in FY25 (ev-6). Earnings fell slightly (-$11m) while average equity rose ($1.3bn), with the equity effect dominating the decline.

> [ev-6] NAB/FY25/results_book, PDF p71: "Cash return on equity 11.4% 11.6%"
> [ev-4] NAB/FY25/results_book, PDF p71: "Cash earnings 7,091 7,102"
> [ev-5] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -0.02 ppt | 80 | 2 () | ev-4, ev-5, ev-6, ev-23 |
| `equity_effect` | — | -0.18 ppt | 80 | 1 (single_source) | ev-5, ev-6 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*-0.02 ppt | confidence 80/100*

Derived: Prior ROE (11.6%) x earnings growth (-0.15%). Cash earnings fell $11m (ev-4, ev-23). Contribution is derived, not disclosed.
> [ev-4] NAB/FY25/results_book, PDF p71: "Cash earnings 7,091 7,102"
> [ev-5] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039"
> [ev-6] NAB/FY25/results_book, PDF p71: "Cash return on equity 11.4% 11.6%"
> [ev-23] NAB/FY25/investor_presentation, printed p39: "Cash earnings FY25 7,091 FY24 7,102 FY25 v FY24 (11) 2H25 3,508 1H25 3,583 2H25 v 1H25 (75)"

### equity_effect
*-0.18 ppt | confidence 80/100*

Derived: Total delta minus earnings effect. Average equity rose $1.3bn (ev-5). Higher denominator reduced ROE. Driven by retained earnings and buybacks.
> [ev-5] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039"
> [ev-6] NAB/FY25/results_book, PDF p71: "Cash return on equity 11.4% 11.6%"

## Source disagreements
- **Cash ROE Level** (definitional): 11.4% (Results Book) vs 10.7% (Investor Presentation)
  Preferred: 11.4%. The Results Book (ev-6) is the primary source per hierarchy. The IP figure (ev-15) likely uses a different equity basis or period definition.

## Limitations
- Drivers are arithmetic derivations, not bank-disclosed splits.
- IP table shows conflicting ROE level.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T12:40:27+00:00
- seconds: 43.9
- cost_usd: 0.0018
- tokens: 35580 in / 5851 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['NAB/FY25/investor_presentation p39 <- p5 page 39', 'NAB/FY25/investor_presentation p10 <- p39 page 10 [added]']
