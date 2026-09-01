# CBA — cet1 — FY26 vs FY25

**Movement (cash basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 40/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 30 Jun 25 column -> column 30 Jun 26 column*

CBA's APRA Level 2 (Group) CET1 ratio fell 30 bpts to 12.0% at 30 June 2026 from 12.3% at 30 June 2025 (results book p48; corroborated on presentation p55 and p106). The bank publishes only a half-on-half capital walk (Dec 25 → Jun 26: Cash NPAT +106, 1H26 dividend -76, RWA -46, Other -8 bpts), not a full-year walk, so the FY26-vs-FY25 drivers are only partially quantified. Within the FY26 window the bank states: New Zealand organic capital contributed +20 bpts, and the 1H26 dividend DRP on-market purchase of $530m had a -10 bpts CET1 impact. The remaining -40 bpts is driven by RWA growth and other regulatory adjustments, which the bank does not quantify in bpts for the full-year comparison.

> [ev-11] CBA/FY26/profit_announcement, PDF p48: "Common Equity Tier 1 (CET1) 12.0 12.3 12.3 (30)bpts (30)bpts"
> [ev-12] CBA/FY26/profit_announcement, PDF p48: "The Group's CET1 Capital ratio was 12.0% as at 30 June 2026, a decrease of 30 basis points from 31 December 2025 and 30 June 2025."
> [ev-17] CBA/FY26/results_presentation, printed p55: "12.3% 12.0%"
> [ev-18] CBA/FY26/results_presentation, printed p55: "(30bpts)"
> [ev-26] CBA/FY26/results_presentation, printed p106: "CET1 capital ratio 12.3 12.3 12.0"
> [ev-16] CBA/FY26/profit_announcement, PDF p76: "This contributed 20 basis points to the Group's CET1 ratio."
> [ev-13] CBA/FY26/profit_announcement, PDF p48: "The 2026 interim dividend included the on-market purchase of $530 million of shares (CET1 impact of -10 bpts) in respect of the Dividend Reinvestment Plan."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_generation` | New Zealand organic capital | +20 bps | 85 | 1 (corroborated_2_sources) | ev-16 |
| `dividend_net_drp` | 1H26 dividend DRP | -10 bps | 85 | 1 (corroborated_2_sources) | ev-13 |
| *residual (unexplained)* | — | -40 bps | — | — | — |

### earnings_generation — "New Zealand organic capital"
*+20 bps | confidence 85/100*

New Zealand generated AUD1,021 million of organic capital for the Group in the current year, contributing 20 basis points to the Group's CET1 ratio. Organic capital is cash NPAT less the capital equivalent of the change in regulatory RWA, excluding dividends.
> [ev-16] CBA/FY26/profit_announcement, PDF p76: "This contributed 20 basis points to the Group's CET1 ratio."

### dividend_net_drp — "1H26 dividend DRP"
*-10 bps | confidence 85/100*

The 2026 interim dividend included the on-market purchase of $530 million of shares (CET1 impact of -10 bpts) in respect of the Dividend Reinvestment Plan. FY26 dividend was $5.05 per share (final $2.70), payout ratio 77% of cash NPAT.
> [ev-13] CBA/FY26/profit_announcement, PDF p48: "The 2026 interim dividend included the on-market purchase of $530 million of shares (CET1 impact of -10 bpts) in respect of the Dividend Reinvestment Plan."

### rwa — "RWA"
*unquantified | confidence 60/100*

The bank does not quantify the full-year RWA impact in bpts. The half-on-half walk (Dec 25 → Jun 26) shows RWA -46 bpts (Credit -38, IRRBB -16, Market +8, Operational 0). Full-year RWA levels rose $26.3bn to $522.4bn (Jun 25: $496.1bn); IRRBB RWA rose from $40bn to $42bn (APS 117 +$12bn, underlying -$10bn).
> [ev-19] CBA/FY26/profit_announcement, PDF p122: "Total risk weighted assets 522,407 505,310 496,145"
> [ev-20] CBA/FY26/profit_announcement, PDF p122: "Total RWA for Credit Risk Exposures 422,703 409,119 398,928"
> [ev-21] CBA/FY26/profit_announcement, PDF p122: "Traded market risk 7,004 9,971 9,752"
> [ev-22] CBA/FY26/profit_announcement, PDF p122: "Interest rate risk in the banking book 41,659 35,179 39,841"
> [ev-23] CBA/FY26/profit_announcement, PDF p122: "Operational risk 51,041 51,041 47,624"
> [ev-24] CBA/FY26/results_presentation, printed p32: "40 42 12 (10) Jun 25 APS 117 Underlying movement Jun 26 IRRBB RWA ($bn) Jun 26 vs Jun 25"

### deductions_other — "Other"
*unquantified | confidence 60/100*

The bank does not quantify the full-year 'Other' impact in bpts. The half-on-half walk (Dec 25 → Jun 26) shows Other -8 bpts, including intangibles, FX impact on Credit RWA, equity accounted profits/losses, movements in reserves and other regulatory adjustments.
> [ev-1] CBA/FY26/profit_announcement, PDF p48: "[walk chart] Capital – CET1 (APRA) (bps): Dec 25 Level 2 1230 -> Jun 26 Level 2 1200"

## Source disagreements
- **Level 1 vs Level 2 CET1 ratio** (definitional): Level 2 CET1 12.0% Jun 26 vs Level 1 CET1 12.1% Jun 26
  Preferred: Level 2 (Group) CET1 ratio 12.0%. The task's headline measure is the APRA Level 2 (Group) CET1 ratio. The Level 1 ratio (12.1% at Jun 26) and International ratio (18.3%) are different measures, quoted as context only.
- **Half-on-half vs full-year capital walk** (timing): Dec 25→Jun 26 walk: Cash NPAT +106, 1H26 div -76, RWA -46, Other -8 vs FY26 vs FY25 movement -30 bpts
  Preferred: Full-year movement -30 bpts. The bank publishes only the half-on-half (Dec 25→Jun 26) capital walk. Its bars are NOT the FY26-vs-FY25 contributions and are described in the narrative as context only.

## Limitations
- The bank publishes only a half-on-half (Dec 25 → Jun 26) capital walk; no full-year (Jun 25 → Jun 26) walk exists. Per method, the half-on-half bars are not restated as this comparison's contributions.
- Only two drivers are quantified in bpts for events inside the FY26 window: NZ organic capital (+20 bpts) and the 1H26 dividend DRP (-10 bpts). The RWA and Other drivers are unquantified for the full-year comparison; their half-on-half values are described in the narrative.
- The residual of -40 bpts reflects the gap between the -30 bpts movement and the +10 bpts of quantified drivers; it is not a bank-stated figure.
- The IRRBB RWA full-year movement (40→42 $bn) is stated in $bn, not bpts, so it cannot be converted to a bpts contribution without the bank's own conversion.
- Movement endpoints converted from percent (12.3, 12.0) to bps: the unit for this metric is bps.
- Failed check: walk_sum (start 1230 + bars -24.0 = 1206.0 != end 1200, tol 1.0 bps) [CBA/FY26/profit_announcement PDF p48 (ev-1)]
- Failed check: walk_sum (start 1230 + bars -24.0 = 1206.0 != end 1200, tol 1.0 $bn) [CBA/FY26/results_presentation PDF p32 (ev-6)]

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-09-01T17:36:05+00:00
- seconds: 159.6
- cost_usd: 0.0118
- tokens: 758072 in / 20229 out
- latency: 31 calls, 158s in requests (slowest 18s), 0 retries, 0 grace waits, 0s slept
- orchestration: agent
- tool_calls: 44
- pages_read: 18
- charts_read: 2
- budget_exhausted: no
