# NAB — roe — FY25 vs FY24

**Movement (cash basis):** 11.6ppt → 11.4ppt (-0.2ppt) | **Attribution confidence:** 80/100

*Read from: row 'Cash return on equity', column FY24 -> column FY25*

NAB's Cash ROE declined by 20 bps to 11.4% in FY25 (ev-3). Earnings fell $11m to $7,091m while average equity rose $1.3bn to $62.4bn (ev-2). The earnings effect is a negative contribution of approximately 20 bps, and the equity effect is approximately zero.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -20 ppt | 80 | 2 () | ev-2, ev-3, ev-10 |
| `equity_effect` | — | +19.8 ppt | 80 | 1 (single_source) | ev-2 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*-20 ppt | confidence 80/100*

Derived: prior-period ROE (11.6%) multiplied by earnings growth (-0.15%). Earnings fell $11m to $7,091m from $7,102m (ev-2, ev-10). This represents a quantified contribution derived from KPI-table endpoints.
> [ev-2] NAB/FY25/results_book, PDF p71: "Cash return on equity Earnings ($m) Cash earnings 7,091 7,102 3,508 3,583 Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314 Cash return on equity 11.4% 11.6% 11.0% 11.7%"
> [ev-3] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"
> [ev-10] NAB/FY25/investor_presentation, printed p39: "Cash earnings 7,091 7,102 (11) 3,508 3,583 (75)"

### equity_effect
*+19.8 ppt | confidence 80/100*

Residual: total delta (-20.0) minus earnings effect (-20.0). Equity grew ~2.1%, offsetting the earnings decline. Derived value.
> [ev-2] NAB/FY25/results_book, PDF p71: "Cash return on equity Earnings ($m) Cash earnings 7,091 7,102 3,508 3,583 Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314 Cash return on equity 11.4% 11.6% 11.0% 11.7%"

## Source disagreements
- **ROE Value Source** (definitional): 11.4% — NAB/FY25/results_book (ev-2) vs 10.7% — NAB/FY25/investor_presentation (ev-6)
  Preferred: 11.4%. The results book (ev-2) is the primary source per hierarchy. The investor presentation (ev-6) likely uses a different basis or restatement.

## Limitations
- Earnings effect is derived, not disclosed as a standalone driver.
- Equity effect is a residual.
- Disagreement exists between results book and investor presentation for FY25 ROE.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-29T18:07:33+00:00
- seconds: 38.9
- cost_usd: 0.0019
- tokens: 39793 in / 5361 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['NAB/FY25/investor_presentation p39 <- p5 page 39', 'NAB/FY25/investor_presentation p10 <- p39 page 10 [added]']
