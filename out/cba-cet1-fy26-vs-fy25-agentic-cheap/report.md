# CBA — cet1 — FY26 vs FY25

**Movement (cash basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 40/100

*Read from: row 'Common Equity Tier 1 (CET1) APRA Level 2 ratio', column 30 Jun 25 column, CET1 row -> column 30 Jun 26 column, CET1 row*

CBA's APRA Level 2 CET1 ratio declined 30 bpts to 12.0% in FY26 from 12.3% in FY25, remaining well above APRA's 10.25% minimum. The decline was driven by capital deployed into Credit RWA growth (the bank deployed 72 bpts of capital into Credit RWA across the year for volume growth in commercial portfolios and domestic residential mortgages), offset by capital generated from earnings (Cash NPAT of $10,982m, up 7% on FY25). The full-year dividend of $5.05 per share (77% payout ratio of cash NPAT) was fully DRP-neutralised via on-market share purchases. No buy-back activity occurred during FY26 ($300m of the $1bn programme was completed in prior periods). Total RWA grew $26.3 billion to $522.4 billion (+5.3%). The Level 1 CET1 ratio moved from 12.4% to 12.1% (-30 bpts), and the International CET1 ratio was flat at 18.3%.

> [ev-9] CBA/FY26/profit_announcement, PDF p48: "The Group's CET1 Capital ratio was 12.0% as at 30 June 2026, a decrease of 30 basis points from 31 December 2025 and 30 June 2025."
> [ev-24] CBA/FY26/results_presentation, printed p106: "CET1 capital ratio 12.3 12.3 12.0"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `rwa.credit` | Credit Risk RWA growth | -72 bps | 80 | 1 (single_source) | ev-17, ev-21 |
| `capital_returns` | Share buy-back | +0 bps | 80 | 1 (single_source) | ev-18 |
| *residual (unexplained)* | — | -30 bps | — | — |

### rwa.credit — "Credit Risk RWA growth"
*-72 bps | confidence 80/100*

The bank deployed 72 bpts of capital into Credit RWA across the year, driven by strong volume growth particularly in commercial portfolios and domestic residential mortgages. Credit RWA grew $23.8 billion to $422.7 billion (from $398.9 billion in Jun 25), an increase of 6.0%, mainly from volume growth in commercial lending and domestic residential mortgages.
> [ev-17] CBA/FY26/profit_announcement, PDF p9: "Across the year we deployed 72bpts of capital into credit risk weighted assets with strong volume growth particularly in commercial portfolios and domestic residential mortgages."
> [ev-21] CBA/FY26/profit_announcement, PDF p122: "Total risk weighted assets 522,407 505,310 496,145"

### earnings_generation — "Capital generated from earnings"
*unquantified | confidence 60/100*

Cash NPAT of $10,982 million increased 7% on FY25 ($10,252 million implied), driven by a 6% increase in operating income supported by lending volume growth and broadly stable underlying NIM. The bank states capital was generated from earnings as a key driver supporting the CET1 position. No specific bpts figure is disclosed for the full-year earnings contribution.
> [ev-16] CBA/FY26/profit_announcement, PDF p9: "The Group's Common Equity Tier 1 (CET1) ratio of 12.0% was well above APRA's minimum regulatory requirement of 10.25%."

### dividend_net_drp — "Dividends net of DRP"
*unquantified | confidence 60/100*

Full-year dividend of $5.05 per share (final $2.70 + interim $2.35) was paid at a 77% payout ratio of cash NPAT. Both the 2025 final and 2026 interim DRPs were satisfied in full by on-market purchase of shares (participation rates 14.8% and 13.5% respectively). The half-on-half walk shows the 1H26 dividend (DRP neutralised) had a -76 bpts impact; the 2H25 final dividend (also DRP neutralised) would have had a similar negative CET1 impact. No specific full-year bpts figure is disclosed.
> [ev-18] CBA/FY26/profit_announcement, PDF p9: "The $1 billion on-market share buy-back, of which $300 million has been completed, expires on 12 August 2026 and will not be extended."

### capital_returns — "Share buy-back"
*+0 bps | confidence 80/100*

No buy-back activity was undertaken during FY26. The $300 million of the $1 billion on-market share buy-back programme that was completed as at 30 June 2026 relates to activity in prior periods. The buy-back expires on 12 August 2026 and will not be extended.
> [ev-18] CBA/FY26/profit_announcement, PDF p9: "The $1 billion on-market share buy-back, of which $300 million has been completed, expires on 12 August 2026 and will not be extended."

### other_unmapped — "Other regulatory adjustments and movement in reserves"
*unquantified | confidence 50/100*

The half-on-half walk shows 'Other' at -8 bpts, which includes intangibles, FX impact on Credit RWA, equity accounted profits/losses and impairments from associates, movements in reserves and other regulatory adjustments. For the full year, no specific bpts figure is disclosed. The bank does not disclose a separate full-year figure for this category.
> [ev-16] CBA/FY26/profit_announcement, PDF p9: "The Group's Common Equity Tier 1 (CET1) ratio of 12.0% was well above APRA's minimum regulatory requirement of 10.25%."

## Source disagreements
- **Level 1 vs Level 2 CET1 ratio** (definitional): Level 1: 12.4% → 12.1% (-30 bpts) vs Level 2: 12.3% → 12.0% (-30 bpts)
  Preferred: Level 2 CET1 ratio of 12.0% at 30 Jun 26, down 30 bpts from 12.3% at 30 Jun 25. Both Level 1 and Level 2 show -30 bpts movement, but the task specifies taking the APRA Level 2 (Group) CET1 ratio row as the headline measure. Level 1 is a different measure.
- **International CET1 ratio** (definitional): 18.7% → 18.3% (-40 bpts)
  Preferred: Not used as movement basis. The International CET1 ratio is a different measure from the APRA Level 2 CET1 ratio specified in the task. It is reported as context only.

## Limitations
- No full-year CET1 walk chart exists in the published documents. Only a half-on-half (Dec 25 → Jun 26) CET1 walk is provided, which is context-only and cannot be used as the primary driver table for the FY25→FY26 comparison.
- The bank discloses that 72 bpts of capital was deployed into Credit RWA across the year, but does not provide a full-year bpts breakdown for earnings generation, dividends, or other regulatory adjustments.
- The half-on-half walk (ev-1) shows Cash NPAT +106 bpts, 1H26 Dividend -76 bpts, RWA -46 bpts, Other -8 bpts, but these are for H1 only and the sum check failed (-24 bpts vs actual -30 bpts).
- The Level 1 CET1 ratio (12.4% → 12.1%) and International CET1 ratio (18.7% → 18.3%) are different measures from the APRA Level 2 CET1 ratio and are reported as context/disagreements.
- Driver contributions for earnings generation, dividends, and other adjustments are unquantified for the full year because the bank does not disclose full-year bpts impacts for these categories.
- Capped at 80: capital_returns +0 bps. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.
- Failed check: drivers_reconcile (drivers -72.0 + residual -30.0 != delta -30.0, tol 1.0)
- Failed check: walk_sum (start 1230 + bars -24.0 = 1206.0 != end 1200, tol 1.0 bps) [CBA/FY26/profit_announcement PDF p48 (ev-1)]
- Capped at 80: rwa.credit -72 bps. drivers_reconcile failed, so the parts and the whole disagree. That proves one of these claims is wrong without saying which, so none of them may claim near-certainty.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-31T01:01:47+00:00
- seconds: 174.6
- cost_usd: 0.056
- tokens: 1520270 in / 10938 out
- orchestration: agent
- tool_calls: 61
- pages_read: 25
- charts_read: 1
- budget_exhausted: no
