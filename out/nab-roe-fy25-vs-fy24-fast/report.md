# NAB — roe — FY25 vs FY24

**Movement (cash basis):** 11.6ppt → 11.4ppt (-0.2ppt) | **Attribution confidence:** 85/100

*Read from: row 'Cash return on equity', column Sep 24 column -> column Sep 25 column*

NAB's Cash ROE fell 20 bps to 11.4% in FY25 from 11.6% in FY24 (results book p10 states "(20 bps)"; p71 prints 11.4% vs 11.6%; presentation p6 corroborates). Cash earnings were broadly flat, down $11m or 0.2% to $7,091m (p14, p5), while total average equity attributable to owners rose 2.2% to $62,355m from $61,039m (p71). The movement splits arithmetically into a small negative earnings effect (~-0.02 ppt) and a larger negative equity effect (~-0.18 ppt), the latter reflecting equity growing faster than flat earnings despite the completed on-market buyback. Statutory ROE fell more sharply, 60 bps to 10.8% (p71), a definitional difference from the cash basis.

> [ev-1] NAB/FY25/results_book, PDF p71: "Cash return on equity Earnings ($m) Cash earnings 7,091 7,102 3,508 3,583 Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314 Cash return on equity 11.4% 11.6% 11.0% 11.7%"
> [ev-3] NAB/FY25/investor_presentation, printed p6: "Cash return on equity Basic cash EPS (cents) Dividend per share and payout ratio (cents) 10.7% 11.7% 12.9% 11.6% 11.4% FY21 FY22 FY23 FY24 FY25"
> [ev-4] NAB/FY25/results_book, printed p12: "Cash earnings decreased by $11 million or 0.2%."
> [ev-6] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"
> [ev-8] NAB/FY25/investor_presentation, printed p5: "Financial results 5 7,102 7,091 FY24 FY25 10,823 10,965 FY24 FY25 Cash earnings1 ($m) Underlying profit ($m) 6,960 6,759 FY24 FY25 Statutory profit ($m) (1) Refer to page 39 for definition of cash earnings and reconciliation to statutory net profit 1.3% (0.2%) (2.9%)"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Cash earnings movement at constant equity | -0.02 ppt | 80 | 2 () | ev-1, ev-4, ev-8 |
| `equity_effect` | Average equity movement at constant earnings | -0.18 ppt | 80 | 2 () | ev-1, ev-5, ev-7 |
| `other_unmapped` | Interaction residual | +0 ppt | 80 | 1 (single_source) | ev-1 |
| *residual (unexplained)* | — | +0 ppt | — | — | — |

### earnings_effect — "Cash earnings movement at constant equity"
*-0.02 ppt | confidence 80/100*

Derived, not disclosed: cash earnings fell $11m or 0.2% to $7,091m (p14, p5). At constant equity, prior-period ROE of 11.6% times the -0.2% earnings growth (fraction -0.002) gives about -0.02 ppt. The bank attributes the flat earnings to higher net interest income (+$644m) offset by higher expenses, lower other income and a higher credit impairment charge (p14).
> [ev-1] NAB/FY25/results_book, PDF p71: "Cash return on equity Earnings ($m) Cash earnings 7,091 7,102 3,508 3,583 Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314 Cash return on equity 11.4% 11.6% 11.0% 11.7%"
> [ev-4] NAB/FY25/results_book, printed p12: "Cash earnings decreased by $11 million or 0.2%."
> [ev-8] NAB/FY25/investor_presentation, printed p5: "Financial results 5 7,102 7,091 FY24 FY25 10,823 10,965 FY24 FY25 Cash earnings1 ($m) Underlying profit ($m) 6,960 6,759 FY24 FY25 Statutory profit ($m) (1) Refer to page 39 for definition of cash earnings and reconciliation to statutory net profit 1.3% (0.2%) (2.9%)"

### equity_effect — "Average equity movement at constant earnings"
*-0.18 ppt | confidence 80/100*

Derived, not disclosed: total delta (-0.2 ppt) minus earnings effect (-0.02 ppt) = about -0.18 ppt. Average equity attributable to owners rose 2.2% to $62,355m from $61,039m (p71), growing faster than flat earnings. Despite the completed $3bn on-market buyback (p29), equity still rose; the DRP for the 2H25 dividend is to be neutralised (p7).
> [ev-1] NAB/FY25/results_book, PDF p71: "Cash return on equity Earnings ($m) Cash earnings 7,091 7,102 3,508 3,583 Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314 Cash return on equity 11.4% 11.6% 11.0% 11.7%"
> [ev-5] NAB/FY25/results_book, PDF p29: "On 12 March 2025, the Group completed the on-market buyback that was announced on 15 August 2023 and subsequently increased on 2 May 2024 to $3 billion. Through this buy-back, the Group has bought back and cancelled 87,824,707 ordinary shares, including 16,572,039 ordinary shares ($0.6 billion or 0.15% of CET1 capital) in the September 2025 full year."
> [ev-7] NAB/FY25/investor_presentation, printed p7: "DRP for 2H25 dividend to be neutralised"

### other_unmapped — "Interaction residual"
*+0 ppt | confidence 80/100*

The two derived effects sum to the total delta (-0.02 + -0.18 = -0.20 ppt), so the interaction residual is zero. The equity effect as computed already absorbs the interaction term per the method.
> [ev-1] NAB/FY25/results_book, PDF p71: "Cash return on equity Earnings ($m) Cash earnings 7,091 7,102 3,508 3,583 Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314 Cash return on equity 11.4% 11.6% 11.0% 11.7%"

## Notable items
- Statutory ROE fell 60 bps to 10.8% vs Cash ROE -20 bps

## Source disagreements
- **Statutory vs Cash ROE movement** (definitional): Statutory ROE -60 bps (10.8% vs 11.4%) vs Cash ROE -20 bps (11.4% vs 11.6%)
  Preferred: Cash ROE -20 bps. The bank's headline ROE measure is Cash ROE (11.4% vs 11.6%, -20 bps). Statutory ROE fell 60 bps to 10.8% from 11.4% (p71), a larger decline driven by the difference between cash and statutory earnings (statutory net profit fell $201m or 2.9% vs cash earnings down $11m or 0.2%).

## Limitations
- The bank does not publish a walk/bridge decomposition of the Cash ROE movement; the earnings and equity effects are arithmetic derivations from the ROE endpoints and the bank-stated earnings growth rate, not disclosed figures.
- The equity effect is derived as the residual (total delta minus earnings effect) and therefore absorbs the interaction term; its direction is supported by the 2.2% rise in average equity attributable to owners (p71) and the DRP neutralisation (p7), but the bank does not quantify the equity contribution itself.
- No primary ROE walk chart exists in either document; the driver split rests on the arithmetic identity rather than a bank-published bridge.

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-09-01T17:45:12+00:00
- seconds: 90.4
- cost_usd: 0.0058
- tokens: 325984 in / 13175 out
- latency: 19 calls, 90s in requests (slowest 20s), 0 retries, 0 grace waits, 0s slept
- orchestration: agent
- tool_calls: 27
- pages_read: 8
- charts_read: 0
- budget_exhausted: no
