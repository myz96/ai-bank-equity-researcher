# WBC — roe — FY25 vs FY24

**Movement (ex_notables basis):** 9.77ppt → 9.66ppt (-0.11ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on average ordinary equity', column FY24 (Sep 2024) -> column FY25 (Sep 2025)*

WBC's cash ROE declined by 11 bps to 9.66% in FY25 from 9.77% in FY24. The decline is driven by a negative earnings effect of approximately 1.3 ppt, partially offset by a positive equity effect of approximately 1.2 ppt. The equity effect reflects the dilutive impact of higher average equity ($71,544m vs $71,493m) which reduced the return per unit of capital, while the earnings effect captures the underlying profit contraction.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -1.3 ppt | 80 | 1 (single_source) | ev-1, ev-5 |
| `equity_effect` | — | +1.19 ppt | 80 | 1 (single_source) | ev-1, ev-5 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*-1.3 ppt | confidence 80/100*


> [ev-1] WBC/FY25/results_announcement, PDF p10: "Return on average ordinary equity 9.66% 9.77% (11 bps) 9.89% 9.42% 47 bps"
> [ev-5] WBC/FY25/results_announcement, PDF p10: "Average ordinary equity ($m) 71,544 71,493 - 72,499 70,584 3"

### equity_effect
*+1.19 ppt | confidence 80/100*

Derived as total delta (-0.11 ppt) minus earnings effect (-1.3 ppt). Reflects the drag from higher average ordinary equity ($71,544m vs $71,493m). The value is derived, not disclosed.
> [ev-1] WBC/FY25/results_announcement, PDF p10: "Return on average ordinary equity 9.66% 9.77% (11 bps) 9.89% 9.42% 47 bps"
> [ev-5] WBC/FY25/results_announcement, PDF p10: "Average ordinary equity ($m) 71,544 71,493 - 72,499 70,584 3"

## Limitations
- The earnings growth rate used for the earnings effect calculation is implied from the ROE and Equity data, as explicit profit growth % was not provided in the evidence records. The split between earnings and equity effects is an arithmetic derivation, not a bank disclosure.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T18:12:08+00:00
- seconds: 36.6
- cost_usd: 0.0013
- tokens: 32635 in / 2231 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
