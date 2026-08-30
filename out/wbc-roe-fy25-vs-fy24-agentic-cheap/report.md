# WBC — roe — FY25 vs FY24

**Movement (ex_notables basis):** 11.21ppt → 10.97ppt (-0.24ppt) | **Attribution confidence:** 80/100

*Read from: row 'ROTE Shareholder value - excluding Notable Items', column Full Year Sept 2024 -> column Full Year Sept 2025*

ROTE ex Notable Items fell 24 bps to 10.97% in FY25 from 11.21% in FY24. The decline was driven primarily by a ~22 ppt earnings effect — net profit excluding Notable Items (adjusted for RSP dividends) declined 2% to $6,966m from $7,106m, reflecting higher operating expenses (up 9%, including a $273m restructuring charge) that more than offset higher net interest income (+3%) and lower impairment charges (5 bps vs 7 bps of avg loans). A small ~2 ppt equity effect arose as average tangible ordinary equity edged up 0.1% to $63,476m from $63,415m, partially diluting returns despite capital returns through on-market share buybacks and a 75% dividend payout ratio.

> [ev-1] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps)"
> [ev-5] WBC/FY25/investor_discussion_pack, printed p6: "11.0% ROTE ex Notable Items1 24bps to FY24"
> [ev-6] WBC/FY25/investor_discussion_pack, printed p20: "Excluding Notable Items: Net profit $7,113m $6,972m (2%)"
> [ev-7] WBC/FY25/investor_discussion_pack, printed p37: "11.0% Return on tangible equity ex Notable Items, down 24 bps"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Net profit excluding Notable Items movement | -0.216 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-4 |
| `equity_effect` | Average tangible ordinary equity movement | -0.024 ppt | 80 | 1 (single_source) | ev-1, ev-3, ev-8, ev-9, ev-10 |

### earnings_effect — "Net profit excluding Notable Items movement"
*-0.216 ppt | confidence 80/100*

Derived: prior-period ROE (10.97%) × earnings growth rate (-1.97%). Net profit excl Notable Items (adj RSP) fell $140m to $6,966m from $7,106m. Higher NII (+3% to $19,473m from loan growth, AIEA up 3%) and lower impairment charges ($424m vs $537m, 5bps vs 7bps) were more than offset by higher operating expenses (+9% to $11,916m, including $273m restructuring under Fit for Growth), per pages 8–9.
> [ev-1] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps)"
> [ev-2] WBC/FY25/results_announcement, PDF p9: "Net profit excluding Notable Items 6,972 7,113 (2)"
> [ev-4] WBC/FY25/results_announcement, PDF p58: "Net profit attributable to owners of WBC (adjusted for RSP dividends) excluding Notable Items 6,966 7,106"

### equity_effect — "Average tangible ordinary equity movement"
*-0.024 ppt | confidence 80/100*

Derived: total delta (-24 ppt) minus earnings effect (-21.6 ppt). Average tangible ordinary equity rose $61m to $63,476m from $63,415m (+0.1%), diluting ROE. Equity was supported by retained earnings but reduced by capital returns: on-market share buyback (2bps CET1 reduction, page 29) and DRP satisfied via market purchases (page 31). Dividend payout ratio ex Notable Items was 75.04%.
> [ev-1] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps)"
> [ev-3] WBC/FY25/results_announcement, PDF p58: "Average tangible ordinary equity 63,476 63,415"
> [ev-8] WBC/FY25/results_announcement, PDF p29: "Capital return: 2 basis points reduction due to the on market share buyback."
> [ev-9] WBC/FY25/results_announcement, PDF p31: "The Board has determined to satisfy the DRP for the 2025 final ordinary dividend by arranging for the purchase of shares in the market by a third party."
> [ev-10] WBC/FY25/results_announcement, PDF p10: "Average tangible ordinary equity ($m) 63,476 63,415"

## Limitations
- No dedicated ROTE walk/breakdown chart published by WBC; earnings and equity effects are arithmetic derivations, not disclosed components.
- The interaction term between earnings and equity movements is embedded in the equity_effect residual rather than separately quantified.
- No explicit bank disclosure of the ROTE decomposition rationale beyond the underlying earnings and equity drivers.
- Movement delta normalised from -24 to -0.24 (unit slip against the endpoints).
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Identity contributions restated from -24.00 to -0.2400 ppt: the identity closes on the movement delta at the ratio's own scale and not at the scale they were written on, and a contribution larger than the ratio itself cannot be a movement of that ratio. A growth rate enters a ratio identity as a fraction, and a dollar movement enters it divided by the identity's denominator.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T20:17:49+00:00
- seconds: 153.0
- cost_usd: 0.0579
- tokens: 1582645 in / 6812 out
- orchestration: agent
- tool_calls: 57
- pages_read: 30
- charts_read: 0
- budget_exhausted: no
