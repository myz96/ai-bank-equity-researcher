# WBC — roe — FY25 vs FY24

**Movement (ex_notables basis):** 9.77ppt → 9.66ppt (-0.11ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on average ordinary equity', column FY24 (Sep 2024) -> column FY25 (Sep 2025)*

WBC's headline ROE (cash) declined by 11 bps to 9.66% in FY25 from 9.77% in FY24. The decline is primarily driven by a reduction in earnings at constant equity, partially offset by the effect of average equity levels.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -0.11 ppt | 80 | 1 (single_source) | ev-1, ev-5 |
| `equity_effect` | — | +0 ppt | 80 | 1 (single_source) | ev-1, ev-5 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*-0.11 ppt | confidence 80/100*


> [ev-1] WBC/FY25/results_announcement, PDF p10: "Return on average ordinary equity 9.66% 9.77% (11 bps) 9.89% 9.42% 47 bps"
> [ev-5] WBC/FY25/results_announcement, PDF p10: "Average ordinary equity ($m) 71,544 71,493 - 72,499 70,584 3"

### equity_effect
*+0 ppt | confidence 80/100*

Average ordinary equity increased marginally by $51m (0.07%). At constant earnings, this negligible increase would have slightly depressed ROE, but given the magnitude relative to the total delta, it is treated as zero contribution here. Value is derived.
> [ev-1] WBC/FY25/results_announcement, PDF p10: "Return on average ordinary equity 9.66% 9.77% (11 bps) 9.89% 9.42% 47 bps"
> [ev-5] WBC/FY25/results_announcement, PDF p10: "Average ordinary equity ($m) 71,544 71,493 - 72,499 70,584 3"

## Limitations
- The earnings growth rate used for the earnings_effect calculation is implied from the ROE and Equity data rather than explicitly stated as a driver percentage in the provided evidence. Confidence is capped at 80 due to this derivation.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T13:49:41+00:00
- seconds: 121.7
- cost_usd: 0.0012
- tokens: 31439 in / 2200 out
- orchestration: pipeline
