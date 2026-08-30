# WBC — roe — FY25 vs FY24

**Movement (ex_notables basis):** 11.21ppt → 10.97ppt (-0.24ppt) | **Attribution confidence:** 80/100

*Read from: row 'ROTE ex-notables', column FY24 -> column FY25*

Westpac's headline ROTE (ex-Notable Items) declined by 24 bps to 10.97% in FY25 from 11.21% in FY24. This decline is driven primarily by a negative earnings effect (-26 bps), reflecting a fall in core profit despite stable equity levels. The movement is partially offset by a small positive equity effect (+2 bps).

> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps) 10.87% 11.08% (21 bps)"
> [ev-8] WBC/FY25/results_announcement, PDF p10: "Basic earnings per ordinary share (cents) 203.6 204.4 - 102.8 100.8 2"
> [ev-5] WBC/FY25/results_announcement, PDF p10: "Average ordinary equity ($m) 71,544 71,493 - 72,499 70,584 3"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -0.26 ppt | 80 | 1 (single_source) | ev-4, ev-8 |
| `equity_effect` | — | +0.02 ppt | 80 | 1 (single_source) | ev-4, ev-5, ev-8 |

### earnings_effect
*-0.26 ppt | confidence 80/100*

Derived: Prior-period ROE (11.21%) multiplied by the EPS growth rate (-0.39%). Core EPS fell from 204.4c to 203.6c (ev-8), reducing the numerator at constant equity.
> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps) 10.87% 11.08% (21 bps)"
> [ev-8] WBC/FY25/results_announcement, PDF p10: "Basic earnings per ordinary share (cents) 203.6 204.4 - 102.8 100.8 2"

### equity_effect
*+0.02 ppt | confidence 80/100*

Derived: Total delta (-24 bps) minus earnings effect (-26 bps). Average ordinary equity rose slightly from $71,493m to $71,544m (ev-5), providing a small denominator benefit that mitigated the earnings decline.
> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps) 10.87% 11.08% (21 bps)"
> [ev-5] WBC/FY25/results_announcement, PDF p10: "Average ordinary equity ($m) 71,544 71,493 - 72,499 70,584 3"
> [ev-8] WBC/FY25/results_announcement, PDF p10: "Basic earnings per ordinary share (cents) 203.6 204.4 - 102.8 100.8 2"

## Limitations
- Earnings and equity effects are derived via arithmetic identity rather than disclosed bridge tables.
- Confidence capped at 80 due to reliance on computed deltas rather than explicit bank-stated driver values.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T16:36:08+00:00
- seconds: 39.8
- cost_usd: 0.0019
- tokens: 43931 in / 4426 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
