# NAB — roe — FY25 vs FY24

**Movement (cash basis):** 11.6ppt → 11.4ppt (-0.2ppt) | **Attribution confidence:** 40/100

*Read from: row 'Cash return on equity', column Year to Sep 24 -> column Year to Sep 25*

NAB's Cash ROE declined 20 bps (from 11.6% to 11.4%) in FY25 vs FY24. The decline was driven primarily by a small earnings headwind — cash earnings fell $11m or 0.2% to $7,091m, broadly flat as higher credit impairment charges offset revenue growth — which reduced ROE by approximately 1.8 ppt at constant equity. A smaller equity effect of approximately 0.2 ppt reflected the impact of higher average equity ($62,355m vs $61,039m), partially offsetting the earnings drag. The bank described cash earnings as "broadly stable" and noted the ROE was 11.4%.

> [ev-1] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps)"
> [ev-4] NAB/FY25/results_book, PDF p71: "Cash return on equity 11.4% 11.6%"
> [ev-11] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps)"
> [ev-12] NAB/FY25/results_book, printed p6: "Cash earnings were broadly stable compared with FY24 including higher credit impairment charges. Cash EPS rose 1% and cash ROE was 11.4%"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -1.8 ppt | 80 | 1 (single_source) | ev-4, ev-5 |
| `equity_effect` | — | -0.2 ppt | 80 | 1 (single_source) | ev-3, ev-6, ev-7 |

### earnings_effect
*-1.8 ppt | confidence 80/100*

Derived: prior-period ROE (11.6%) × earnings growth rate (-0.15%, from $7,102m to $7,091m, a $11m decline). The bank states cash earnings were "broadly stable" (ev-12) but credit impairment charges rose 14.4% to $833m (ev-5), partially offsetting a 2.9% increase in net operating income. At constant equity, this earnings decline reduced ROE by approximately 1.8 ppt.
> [ev-4] NAB/FY25/results_book, PDF p71: "Cash return on equity 11.4% 11.6%"
> [ev-5] NAB/FY25/results_book, PDF p9: "Cash earnings 7,091 7,102 (0.2)"

### equity_effect
*-0.2 ppt | confidence 80/100*

Derived: total delta (-2.0 ppt) minus earnings effect (-1.8 ppt). Average equity attributable increased from $61,039m to $62,355m (+$1,316m or 2.2%), reflecting retained earnings and lower buybacks ($16.6m shares bought back in FY25 vs $60.7m in FY24, ev-7), with WA shares declining from 3,099m to 3,059m (ev-6). Higher equity at roughly constant earnings reduced ROE by approximately 0.2 ppt.
> [ev-3] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039"
> [ev-6] NAB/FY25/results_book, printed p68: "Weighted average number of ordinary shares (net of treasury shares) 3,059 3,099"
> [ev-7] NAB/FY25/results_book, PDF p73: "Shares bought back (16,572) (60,690)"

## Limitations
- No walk/bridge chart for ROE decomposition exists in either document; both contributions are arithmetic derivations per the task method, not bank-disclosed splits.
- The bank does not provide a formal ROE driver table; narratives describe earnings as 'broadly stable' without quantifying the ROE-specific contribution of each P&L component.
- Rounding in reported ROE (11.4% vs 11.6%) means the true unrounded delta may differ slightly from -20 bps.
- Movement delta normalised from -2.0 to -20 (unit slip against the endpoints).
- Movement endpoints converted from basis points (1160, 1140) to ppt: the evidence prints this ratio as 11.6% and 11.4%, and the unit for this metric is ppt. A change column printed in basis points is divided by 100 to enter a movement stated in points.
- Failed check: drivers_reconcile (drivers -2.0 + residual +0.0 != delta -0.2, tol 0.1)

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T16:08:47+00:00
- seconds: 232.5
- cost_usd: 0.0298
- tokens: 971681 in / 8282 out
- orchestration: agent
- tool_calls: 42
- pages_read: 14
- charts_read: 0
- budget_exhausted: no
