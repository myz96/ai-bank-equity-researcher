# NAB — roe — FY25 vs FY24

**Movement (cash basis):** 1160ppt → 1140ppt (-20ppt) | **Attribution confidence:** 75/100

*Read from: row 'Cash return on equity row', column Year to Sep 24 column -> column Year to Sep 25 column*

NAB's cash ROE declined 20 ppt from 11.6% in FY24 to 11.4% in FY25. The decline was driven primarily by an equity effect of approximately 18 ppt, reflecting a 2.2% increase in average equity attributable to owners ($61,039m to $62,355m) from retained earnings accumulation and capital base expansion, partially offset by share buybacks of $0.6 billion. The earnings effect contributed approximately 2 ppt of decline, as cash earnings were broadly stable at $7,091m versus $7,102m in FY24 (down 0.2%), with higher credit impairment charges largely offsetting underlying profit growth.

> [ev-1] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps)"
> [ev-2] NAB/FY25/results_book, PDF p71: "Cash earnings 7,091 7,102"
> [ev-3] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039"
> [ev-5] NAB/FY25/results_book, PDF p9: "Cash earnings 7,091 7,102 (0.2)"
> [ev-10] NAB/FY25/results_book, printed p6: "Cash earnings were broadly stable compared with FY24 including higher credit impairment charges. Cash EPS rose 1% and cash ROE was 11.4%."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | earnings effect | -1.8 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-3, ev-5, ev-10 |
| `equity_effect` | equity effect | -18.2 ppt | 80 | 1 (single_source) | ev-3, ev-8, ev-9, ev-11 |

### earnings_effect — "earnings effect"
*-1.8 ppt | confidence 80/100*

Derived: prior-period ROE (11.6%) multiplied by the cash earnings growth rate of -0.15% (($7,091m − $7,102m) / $7,102m). Cash earnings were broadly stable year-on-year, down $11 million or 0.2%, as higher net operating income (+$577m, 2.9%) was offset by higher operating expenses (+$435m, 4.6%) and higher credit impairment charges (+$105m, 14.4%). Higher credit impairment charges included a $7m large item in FY25 versus a $73m large item in FY24.
> [ev-1] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps)"
> [ev-2] NAB/FY25/results_book, PDF p71: "Cash earnings 7,091 7,102"
> [ev-3] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039"
> [ev-5] NAB/FY25/results_book, PDF p9: "Cash earnings 7,091 7,102 (0.2)"
> [ev-10] NAB/FY25/results_book, printed p6: "Cash earnings were broadly stable compared with FY24 including higher credit impairment charges. Cash EPS rose 1% and cash ROE was 11.4%."

### equity_effect — "equity effect"
*-18.2 ppt | confidence 80/100*

Derived: total delta (−20 ppt) minus earnings effect (−1.8 ppt). Average equity attributable to owners rose 2.2% from $61,039m to $62,355m, driven by retained profits increasing $1,584m to $26,820m (page 60), partially offset by share buybacks of 16,572k shares ($0.6 billion) reducing contributed equity by $458m (pages 60, 73). The weighted average number of ordinary shares fell from 3,099m to 3,059m (page 69).
> [ev-3] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039"
> [ev-8] NAB/FY25/results_book, PDF p69: "Weighted average number of ordinary shares (net of treasury shares) 3,059 3,099"
> [ev-9] NAB/FY25/results_book, PDF p73: "Shares bought back (16,572) (60,690)"
> [ev-11] NAB/FY25/results_book, printed p4: "the impact of $0.6 billion of shares bought back in FY25 (-15 bps)"

## Limitations
- No walk chart or bridge table for Cash ROE movement exists in NAB's disclosure; the earnings and equity effects are arithmetic derivations, not bank-stated components.
- The bank does not provide a formal decomposition of the ROE movement into earnings and equity drivers.
- The interaction term between earnings and equity movements is embedded in the equity_effect residual.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T14:30:12+00:00
- seconds: 176.4
- cost_usd: 0.038
- tokens: 1229227 in / 7208 out
- orchestration: agent
- tool_calls: 48
- pages_read: 19
- charts_read: 0
- budget_exhausted: no
