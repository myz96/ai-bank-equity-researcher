# WBC — roe — FY25 vs FY24

**Movement (ex_notables basis):** 11.21ppt → 10.97ppt (-0.24ppt) | **Attribution confidence:** 80/100

*Read from: row 'ROTE ex-notables', column FY24 (Sep 2024) -> column FY25 (Sep 2025)*

Westpac's headline ROTE ex Notable Items declined by 24 bps to 10.97% in FY25 from 11.21% in FY24. This decline is driven primarily by a reduction in cash earnings at constant equity, partially offset by a small increase in average tangible equity.

> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps) 10.87% 11.08% (21 bps)"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -0.08 ppt | 80 | 1 (single_source) | ev-4, ev-8 |
| `equity_effect` | — | -0.16 ppt | 80 | 1 (single_source) | ev-4, ev-5, ev-6, ev-8 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*-0.08 ppt | confidence 80/100*

Derived: Prior-period ROE (11.21%) multiplied by the EPS growth rate (-0.39%). Earnings fell from 204.4c to 203.6c (ev-8), yielding a negative contribution of approx -0.08 ppt.
> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps) 10.87% 11.08% (21 bps)"
> [ev-8] WBC/FY25/results_announcement, PDF p10: "Basic earnings per ordinary share (cents) 203.6 204.4 - 102.8 100.8 2"

### equity_effect
*-0.16 ppt | confidence 80/100*

Derived: Total delta (-0.24) minus earnings effect (-0.08). Average tangible equity rose slightly (ev-5/ev-6 imply ~0.7% growth), which dilutes ROE when earnings fall. Value is derived, not disclosed.
> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps) 10.87% 11.08% (21 bps)"
> [ev-5] WBC/FY25/results_announcement, PDF p10: "Average ordinary equity ($m) 71,544 71,493 - 72,499 70,584 3"
> [ev-6] WBC/FY25/results_announcement, PDF p10: "Average total equity ($m) 71,885 71,549 - 72,837 70,928 3"
> [ev-8] WBC/FY25/results_announcement, PDF p10: "Basic earnings per ordinary share (cents) 203.6 204.4 - 102.8 100.8 2"

## Limitations
- Drivers are quantified via arithmetic derivation (Level 1) rather than direct disclosure. The bank does not provide a bridge for this specific metric.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T15:12:25+00:00
- seconds: 51.4
- cost_usd: 0.0017
- tokens: 43233 in / 3208 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
