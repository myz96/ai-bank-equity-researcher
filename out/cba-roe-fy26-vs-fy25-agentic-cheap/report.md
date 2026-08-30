# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 1350ppt → 1400ppt (+50ppt) | **Attribution confidence:** 80/100

*Read from: row 'Cash basis ROE (%)', column 30 Jun 25 -> column 30 Jun 26*

CBA's return on equity (cash basis) increased 50 basis points to 14.0% in FY26 from 13.5% in FY25. The improvement was driven by a 7% rise in cash NPAT ($10,982m, up $730m or 7% on FY25's $10,253m), which lifted ROE at constant equity. This was partially offset by higher average net assets ($78,238m vs $75,710m), whose growth diluted the ROE impact. The bank stated: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."

> [ev-7] CBA/FY26/profit_announcement, printed p3: "Cash basis 14.0 13.5 50 bpts"
> [ev-8] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."
> [ev-9] CBA/FY26/profit_announcement, printed p3: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."
> [ev-11] CBA/FY26/asx_announcement, PDF p1: "return on equity rose to 14.0%"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | higher cash NPAT | +96 ppt | 80 | 1 (single_source) | ev-3, ev-4, ev-7, ev-8 |
| `equity_effect` | higher net assets | -46 ppt | 80 | 1 (single_source) | ev-2, ev-3, ev-9 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect — "higher cash NPAT"
*+96 ppt | confidence 80/100*

Derived: earnings_effect = prior-period ROE (13.5%) × earnings growth fraction (7.1%). Cash NPAT rose $730m or 7% to $10,982m from $10,253m (ev-8). At constant equity, this earnings growth lifts ROE by approximately 96ppt. The bank attributes the ROE improvement to 'higher cash NPAT' (ev-9).
> [ev-3] CBA/FY26/profit_announcement, PDF p147: "Net profit after tax – cash basis 10,982 10,253"
> [ev-4] CBA/FY26/profit_announcement, PDF p147: "ROE – cash basis (%) 14.0 13.5"
> [ev-7] CBA/FY26/profit_announcement, printed p3: "Cash basis 14.0 13.5 50 bpts"
> [ev-8] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."

### equity_effect — "higher net assets"
*-46 ppt | confidence 80/100*

Derived: equity_effect = total delta (50ppt) minus earnings_effect (96ppt) = -46ppt. Average net assets grew from $75,710m to $78,238m (+$2,528m or 3.3%), diluting ROE. The bank states higher cash NPAT was 'partly offset by higher net assets' (ev-9). Equity growth reflects retained earnings from $10,982m profit less $8,451m dividends (ev-3, ev-2 page 146), with no share buyback activity in FY26 (ev-page 91).
> [ev-2] CBA/FY26/profit_announcement, PDF p147: "Average net assets 78,238 75,710"
> [ev-3] CBA/FY26/profit_announcement, PDF p147: "Net profit after tax – cash basis 10,982 10,253"
> [ev-9] CBA/FY26/profit_announcement, printed p3: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."

## Limitations
- No walk/bridge chart for ROE decomposition exists in the results book or presentation; the earnings and equity effects are arithmetic derivations from KPI table endpoints, not bank-disclosed components.
- The bank does not separately quantify the earnings and equity contributions to the ROE movement; both values are computed using the identity: delta_ROE = ROE_FY25 × earnings_growth_rate + equity_effect.
- The EPS growth rate of 7% (ev-6) corroborates the NPAT growth rate but uses per-share figures rounded to one decimal place.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T14:11:12+00:00
- seconds: 126.0
- cost_usd: 0.0127
- tokens: 676375 in / 5180 out
- orchestration: agent
- tool_calls: 35
- pages_read: 17
- charts_read: 0
- budget_exhausted: no
