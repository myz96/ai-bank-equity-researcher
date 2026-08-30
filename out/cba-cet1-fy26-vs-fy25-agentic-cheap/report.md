# CBA — cet1 — FY26 vs FY25

**Movement (cash basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 40/100

*Read from: row 'Common Equity Tier 1 (CET1) APRA Level 2 Group', column 30 Jun 25 column -> column 30 Jun 26 column*

CBA's APRA Level 2 CET1 ratio fell 30 bps to 12.0% in FY26 from 12.3% in FY25. The decline reflects 72 bps of capital deployed into credit RWA (driven by strong volume growth in commercial portfolios and domestic residential mortgages), partially offset by earnings generation of $10.98 billion cash NPAT (up 7% on FY25's $10.25 billion). Full-year dividends of $8.45 billion (including $530 million DRP share purchase at -10 bps CET1 impact) absorbed capital. No buyback activity occurred in FY26. Divisional organic capital generation totalled $8.75 billion across Retail Banking Services (+81 bps), Business Banking (+54 bps), Institutional Banking & Markets (+17 bps) and ASB/New Zealand (+21 bps). The half-on-half CET1 walk (Dec 25→Jun 26) showed Cash NPAT +106 bps, Dividend -76 bps, RWA -46 bps and Other -8 bps, but no full-year walk is published.

> [ev-21] CBA/FY26/profit_announcement, PDF p48: "Common Equity Tier 1 (CET1) 12.0 12.3 12.3 (30)bpts (30)bpts"
> [ev-22] CBA/FY26/profit_announcement, PDF p48: "The Group's CET1 Capital ratio was 12.0% as at 30 June 2026, a decrease of 30 basis points from 31 December 2025 and 30 June 2025."
> [ev-36] CBA/FY26/results_presentation, printed p55: "10,252 10,982 FY25 FY26"
> [ev-37] CBA/FY26/results_presentation, printed p55: "12.3% 12.0% FY25 FY26"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `rwa.credit` | Credit Risk RWA | -72 bps | 80 | 1 (single_source) | ev-25 |

### rwa.credit — "Credit Risk RWA"
*-72 bps | confidence 80/100*

The bank states it deployed 72 bps of capital into credit RWA across the year, driven by strong volume growth particularly in commercial portfolios and domestic residential mortgages.
> [ev-25] CBA/FY26/profit_announcement, PDF p9: "Across the year we deployed 72bpts of capital into credit risk weighted assets with strong volume growth particularly in commercial portfolios and domestic residential mortgages."

### dividend_net_drp — "Dividend including DRP"
*unquantified | confidence 75/100*

Full-year dividends totalled $8,451 million (vs $8,116 million in FY25). The interim DRP included an on-market purchase of $530 million of shares with a CET1 impact of -10 bps. No buyback activity was undertaken during FY26.
> [ev-34] CBA/FY26/profit_announcement, PDF p146: "Total dividends ($M) 8,451 8,116"
> [ev-43] CBA/FY26/profit_announcement, PDF p48: "The 2026 interim dividend included the on-market purchase of $530 million of shares (CET1 impact of -10 bpts) in respect of the Dividend Reinvestment Plan."
> [ev-44] CBA/FY26/profit_announcement, PDF p48: "No buy-back activity was undertaken during FY26."

### earnings_generation — "Cash NPAT"
*unquantified | confidence 70/100*

Cash NPAT was $10,982 million (up 7% from $10,253 million in FY25). Divisional organic capital generation totalled $8,749 million: Retail Banking Services $4,145 million (+81 bps), Business Banking $2,716 million (+54 bps), IBM $831 million (+17 bps), and ASB $1,057 million (+21 bps).
> [ev-33] CBA/FY26/profit_announcement, PDF p145: "Net profit after tax – cash basis 10,982 10,253"
> [ev-27] CBA/FY26/profit_announcement, PDF p65: "Retail Banking Services generated $4,145 million of organic capital 1 for the Group in the current year. This contributed 81 basis points to the Group's CET1 ratio."
> [ev-28] CBA/FY26/profit_announcement, PDF p69: "Business Banking generated $2,716 million of organic capital 1 for the Group in the current year. This contributed 54 basis points to the Group's CET1 ratio."
> [ev-29] CBA/FY26/profit_announcement, PDF p73: "Institutional Banking and Markets generated $831 million of organic capital 2 for the Group in the current year. This impacted the Group's CET1 ratio by 17 basis points."
> [ev-32] CBA/FY26/profit_announcement, PDF p79: "This contributed 21 basis points to the Group's CET1 ratio."

### other_unmapped — "Other regulatory adjustments"
*unquantified | confidence 40/100*


> [ev-42] CBA/FY26/profit_announcement, PDF p48: "Other regulatory adjustments and movement in reserves"

## Limitations
- No full-year CET1 walk chart is published by CBA; only a half-on-half (Dec 25→Jun 26) walk is available, which cannot be used as driver contributions for the FY25→FY26 comparison per the walk preference rules.
- Earnings generation and dividend impacts are not quantified in basis points for the full year; only the half-on-half walk provides bps figures (+106 bps NPAT, -76 bps dividend).
- The residual between quantified drivers (credit RWA -72 bps, DRP -10 bps) and the total -30 bps movement is not explained by the bank for the full year.
- Divisional organic capital contributions (summing to 173 bps) net out intra-division RWA changes and do not map directly to CET1 walk components.
- Failed check: drivers_reconcile (drivers -72.0 + residual +0.0 != delta -30.0, tol 1.0)
- Failed check: walk_sum (start 1230 + bars -24.0 = 1206.0 != end 1200, tol 1.0 bps) [CBA/FY26/profit_announcement PDF p48 (ev-5)]
- Capped at 80: rwa.credit -72 bps. drivers_reconcile failed, so the parts and the whole disagree. That proves one of these claims is wrong without saying which, so none of them may claim near-certainty.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T19:52:26+00:00
- seconds: 279.9
- cost_usd: 0.1261
- tokens: 2704329 in / 14106 out
- orchestration: agent
- tool_calls: 69
- pages_read: 20
- charts_read: 3
- budget_exhausted: no
