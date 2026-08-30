# NAB — roe — FY25 vs FY24

**Movement (cash basis):** 11.6ppt → 11.4ppt (-0.2ppt) | **Attribution confidence:** 80/100

*Read from: row 'Cash return on equity', column FY24 -> column FY25*

NAB's Cash ROE declined by 20 bps to 11.4% in FY25 (ev-8). Earnings fell slightly (-$11m) while average equity rose ($1.3bn), resulting in a negative earnings effect and a larger negative equity effect.

> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"
> [ev-4] NAB/FY25/results_book, PDF p71: "Cash earnings 7,091 7,102 3,508 3,583"
> [ev-5] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -0.02 ppt | 80 | 2 () | ev-8, ev-15 |
| `equity_effect` | — | -0.18 ppt | 80 | 1 (single_source) | ev-8, ev-5 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*-0.02 ppt | confidence 80/100*

Derived: Prior ROE (11.6%) x Earnings Growth (-0.15%). Earnings fell $11m (ev-15). Contribution is derived, not disclosed.
> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"
> [ev-15] NAB/FY25/investor_presentation, printed p39: "Cash earnings 7,091 7,102 (11) 3,508 3,583 (75)"

### equity_effect
*-0.18 ppt | confidence 80/100*

Derived: Delta minus earnings effect. Equity rose $1.3bn (ev-5). Higher denominator reduced ROE. Contribution is derived, not disclosed.
> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"
> [ev-5] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314"

## Source disagreements
- **Cash ROE Level** (restatement): 11.4% - ev-8 (Results Book) vs 10.7% - ev-11 (Investor Presentation)
  Preferred: 11.4%. The Results Book (ev-8) is the primary source per hierarchy. The IP (ev-11) likely uses a different basis or contains a typo.

## Limitations
- Drivers are mathematically derived from KPI levels, not disclosed by the bank.
- IP data (ev-11) conflicts with Results Book; Results Book preferred.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T18:59:10+00:00
- seconds: 36.7
- cost_usd: 0.0017
- tokens: 34298 in / 5149 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['NAB/FY25/investor_presentation p39 <- p5 page 39', 'NAB/FY25/investor_presentation p10 <- p39 page 10 [added]']
