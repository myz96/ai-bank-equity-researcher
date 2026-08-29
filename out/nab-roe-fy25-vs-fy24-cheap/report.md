# NAB — roe — FY25 vs FY24

**Movement (cash basis):** 11.6ppt → 11.4ppt (-0.2ppt) | **Attribution confidence:** 75/100

*Read from: row 'Cash return on equity', column FY24 -> column FY25*

NAB's Cash ROE declined by 20 bps to 11.4% in FY25 (ev-3). Earnings fell slightly (-$11m) while average equity rose (+$1.3bn), with the equity effect dominating the decline.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Earnings effect | -0.18 ppt | 75 | 1 (single_source) | ev-2, ev-3 |
| `equity_effect` | Equity effect | -0.02 ppt | 75 | 1 (single_source) | ev-2, ev-3 |

### earnings_effect — "Earnings effect"
*-0.18 ppt | confidence 75/100*

Derived: Prior ROE (11.6%) x earnings growth (-0.15%). Cited ev-2 for earnings/equity levels. Value is derived, not disclosed.
> [ev-2] NAB/FY25/results_book, PDF p71: "Cash return on equity Earnings ($m) Cash earnings 7,091 7,102 3,508 3,583 Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314 Cash return on equity 11.4% 11.6% 11.0% 11.7%"
> [ev-3] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"

### equity_effect — "Equity effect"
*-0.02 ppt | confidence 75/100*

Residual: Delta (-0.2) minus earnings effect (-0.18). Driven by higher average equity ($62.4bn vs $61.0bn) diluting returns. Cited ev-2.
> [ev-2] NAB/FY25/results_book, PDF p71: "Cash return on equity Earnings ($m) Cash earnings 7,091 7,102 3,508 3,583 Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314 Cash return on equity 11.4% 11.6% 11.0% 11.7%"
> [ev-3] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"

## Source disagreements
- **Cash ROE FY25 value** (restatement): 11.4% - ev-2/ev-3 (Results Book) vs 10.7% - ev-4 (Investor Presentation)
  Preferred: 11.4%. The Results Book (ev-2) and its summary table (ev-3) are higher hierarchy than the Investor Presentation slide (ev-4). The slide likely contains a typo or uses a different basis.

## Limitations
- Earnings growth rate inferred from absolute profit change rather than stated percentage.
- Drivers are arithmetic derivations; bank does not explicitly split ROE movement into these components.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-29T13:34:03+00:00
- seconds: 111.8
- cost_usd: 0.0013
- tokens: 29584 in / 2882 out
- orchestration: pipeline
