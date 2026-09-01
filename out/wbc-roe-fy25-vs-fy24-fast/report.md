# WBC — roe — FY25 vs FY24

**Movement (ex_notables basis):** 11.21ppt → 10.97ppt (-0.24ppt) | **Attribution confidence:** 80/100

*Read from: row 'ROTE (return on average tangible equity) ex Notable Items', column Full Year Sept 2024 column -> column Full Year Sept 2025 column*

WBC's headline ROE measure, ROTE ex Notable Items, fell 24 bps to 10.97% in FY25 from 11.21% in FY24 (delta -0.24 ppt). The movement is driven almost entirely by lower earnings: net profit ex Notable Items (RSP-adjusted) fell about 2% to $6,966m from $7,106m, which at constant equity lowers ROE by roughly 0.22 ppt. Average tangible ordinary equity rose only slightly (to $63,476m from $63,415m), contributing a small negative equity effect of about 0.02 ppt. The bank's FY24-FY25 earnings walk shows the fall driven by higher expenses (UNITE costs, salaries and wages, restructuring charge) partly offset by productivity initiatives, with net interest income up on loan growth. Both contributions are arithmetic derivations, not disclosed figures.

> [ev-1] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps) 10.87% 11.08% (21 bps)"
> [ev-3] WBC/FY25/results_announcement, PDF p58: "Net profit attributable to owners of WBC (adjusted for RSP dividends) excluding Notable Items 6,966 7,106 3,511 3,454"
> [ev-2] WBC/FY25/results_announcement, PDF p10: "Average tangible ordinary equity ($m) 63,476 63,415 - 64,429 62,519 3"
> [ev-9] WBC/FY25/investor_discussion_pack, printed p6: "11.0% ROTE ex Notable Items1 24bps to FY24"
> [ev-10] WBC/FY25/investor_discussion_pack, printed p20: "Excluding Notable Items: Net profit $7,113m $6,972m (2%)"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Movement in cash earnings at constant equity | -0.221 ppt | 80 | 2 () | ev-3, ev-1, ev-5, ev-6, ev-7, ev-8, ev-11 |
| `equity_effect` | Movement in average equity at constant earnings | -0.019 ppt | 75 | 1 (single_source) | ev-2, ev-1 |
| *residual (unexplained)* | — | +0 ppt | — | — | — |

### earnings_effect — "Movement in cash earnings at constant equity"
*-0.221 ppt | confidence 80/100*

Derived, not disclosed: prior-period ROTE (11.21%) x earnings growth (-1.97%, from $7,106m to $6,966m ex Notable Items, RSP-adjusted) = -0.221 ppt. The bank's FY24-FY25 walk shows expenses -$972m (higher UNITE costs, salaries and wages, restructuring charge, partly offset by productivity initiatives), net interest income +$557m (AIEA up 3% on loan growth, Core NIM down 1bp), non-interest income +$144m, impairment +$113m, tax & NCI +$17m.
> [ev-3] WBC/FY25/results_announcement, PDF p58: "Net profit attributable to owners of WBC (adjusted for RSP dividends) excluding Notable Items 6,966 7,106 3,511 3,454"
> [ev-1] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps) 10.87% 11.08% (21 bps)"
> [ev-5] WBC/FY25/investor_discussion_pack, printed p40: "[walk chart] Net profit FY24 – FY25 ($m): FY24 7113 -> FY25 6972"
> [ev-6] WBC/FY25/investor_discussion_pack, printed p40: "[chart annotation] Net interest income: AIEA up 3% due to loan growth, Core NIM down 1bp, Treasury & Markets NIM flat +557"
> [ev-7] WBC/FY25/investor_discussion_pack, printed p40: "[chart annotation] Non interest income: Higher card fees, Institutional lending fees, markets and net wealth income +144"
> [ev-8] WBC/FY25/investor_discussion_pack, printed p40: "[chart annotation] Expenses: Higher UNITE costs, salaries and wages and restructuring charge, partly offset by productivity initiatives -972"
> [ev-11] WBC/FY25/investor_discussion_pack, printed p40: "Higher UNITE costs, salaries and wages and restructuring charge, partly offset by productivity initiatives"

### equity_effect — "Movement in average equity at constant earnings"
*-0.019 ppt | confidence 75/100*

Derived, not disclosed: total delta (-0.24 ppt) minus earnings_effect (-0.221 ppt) = -0.019 ppt. Average tangible ordinary equity rose slightly to $63,476m from $63,415m (+$61m, +0.1%), so at constant earnings the small equity growth marginally lowers ROE. Direction supported by the modest equity increase; the bank does not disclose a separate equity attribution.
> [ev-2] WBC/FY25/results_announcement, PDF p10: "Average tangible ordinary equity ($m) 63,476 63,415 - 64,429 62,519 3"
> [ev-1] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps) 10.87% 11.08% (21 bps)"

## Notable items
- ROTE ex Notable Items is the headline row; statutory ROTE (10.89% FY25, 11.01% FY24, -12bps) and both Return on average ordinary equity rows are named variants

## Source disagreements
- **Net profit ex Notable Items level** (definitional): results announcement: $6,966m FY25 / $7,106m FY24 (RSP-adjusted) vs investor pack: $6,972m FY25 / $7,113m FY24
  Preferred: results announcement (RSP-adjusted, matches ROTE numerator). The results announcement page 58 reports net profit ex Notable Items adjusted for restricted share dividends ($6,966m/$7,106m), which is the numerator used in ROTE. The investor pack page 20/42 reports the unadjusted figure ($6,972m/$7,113m). Both show ~2% decline; the RSP-adjusted figure is used for the ROE attribution.

## Limitations
- The earnings_effect and equity_effect contributions are arithmetic derivations per the task method, not figures the bank discloses; the bank provides no explicit ROE walk chart for the FY24-FY25 comparison.
- The bank's FY24-FY25 net profit walk (investor pack p40) is the earnings decomposition used to explain the earnings_effect; it is a primary-comparison chart but decomposes profit, not ROE directly.
- The equity_effect is small and its direction is inferred from the modest rise in average tangible ordinary equity; the bank does not disclose a separate equity attribution or buyback/DRP detail for this measure.
- The investor pack reports net profit ex Notable Items unadjusted for RSP dividends ($6,972m/$7,113m) while the results announcement uses the RSP-adjusted figure ($6,966m/$7,106m); the RSP-adjusted figure is used as it matches the ROTE numerator.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-09-01T17:54:44+00:00
- seconds: 67.3
- cost_usd: 0.0037
- tokens: 171453 in / 9581 out
- latency: 14 calls, 67s in requests (slowest 14s), 0 retries, 0 grace waits, 0s slept
- orchestration: agent
- tool_calls: 22
- pages_read: 8
- charts_read: 1
- budget_exhausted: no
