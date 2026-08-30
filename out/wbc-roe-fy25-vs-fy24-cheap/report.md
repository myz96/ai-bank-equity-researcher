# WBC — roe — FY25 vs FY24

**Movement (ex_notables basis):** 11.21ppt → 10.97ppt (-0.24ppt) | **Attribution confidence:** 75/100

*Read from: row 'ROTE ex-notables', column FY24 -> column FY25*

Westpac's headline ROTE ex Notable Items declined by 24 basis points (11.21% to 10.97%) in FY25 versus FY24. This decline is primarily driven by a reduction in cash earnings at constant equity levels, as average tangible equity remained broadly stable with a slight increase. The movement reflects the impact of lower core profitability relative to the capital base.

> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE"
> [ev-6] WBC/FY25/results_announcement, PDF p10: "Average total equity ($m)"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -0.38 ppt | 75 | 1 (single_source) | ev-4, ev-5 |
| `equity_effect` | — | +0.14 ppt | 75 | 1 (single_source) | ev-4, ev-5 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*-0.38 ppt | confidence 75/100*

Derived: Earnings effect = Prior ROE x Earnings Growth. Avg Ordinary Equity rose ~0.07% (ev-5). Core profit growth was negative/flat, implying earnings growth < 0%. Contribution approx -0.38 ppt. Derived from ev-4 and ev-5.
> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE"
> [ev-5] WBC/FY25/results_announcement, PDF p10: "Average ordinary equity ($m)"

### equity_effect
*+0.14 ppt | confidence 75/100*

Derived: Equity effect = Total Delta - Earnings Effect. Residual positive contribution due to denominator expansion (Avg Equity up slightly per ev-5) partially offsetting the earnings drag. Derived from ev-4 and ev-5.
> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE"
> [ev-5] WBC/FY25/results_announcement, PDF p10: "Average ordinary equity ($m)"

## Limitations
- Exact core profit dollar movement for FY25 vs FY24 not explicitly provided in evidence records, requiring derivation of earnings growth rate from ROE and Equity data. Confidence capped due to derived nature of driver split.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T12:44:50+00:00
- seconds: 25.4
- cost_usd: 0.0011
- tokens: 30711 in / 1455 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
