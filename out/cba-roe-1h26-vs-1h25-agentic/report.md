# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (ROE) (%) — Cash basis', column 31 Dec 24 -> column 31 Dec 25*

CBA's cash ROE rose 10 bpts to 13.8% in 1H26 from 13.7% in 1H25 (ev-1, ev-6, ev-13). The bank's own explanation is arithmetically simple: ROE "increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets" (ev-7). Cash NPAT from continuing operations rose $313m or 6% (6.1%) to $5,445m (ev-8, ev-14), driven by a 7% income increase, 5% underlying expense growth and a $1m LIE decrease. That earnings growth alone was worth roughly +0.84 ppt of ROE at constant equity; it was almost entirely absorbed by a $3,828m (5.2%) rise in net average equity, from $74,176m to $78,004m (ev-4), worth roughly -0.74 ppt. Statutory ROE (continuing) was flat at 13.8% (ev-2) because statutory NPAT grew only 5%/$270m (ev-12) — a modestly weaker basis. On a total-Group basis including discontinued operations, statutory ROE fell 10 bpts to 13.6%.

> [ev-1] CBA/1H26/profit_announcement, PDF p19: "Cash basis 13.8 13.4 13.7 40 bpts 10 bpts"
> [ev-2] CBA/1H26/profit_announcement, PDF p19: "Statutory basis 13.8 13.1 13.8 70 bpts –"
> [ev-4] CBA/1H26/profit_announcement, PDF p168: "Average net assets 78,004 77,020 74,176"
> [ev-6] CBA/1H26/profit_announcement, PDF p168: "ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-7] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-8] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million. The result was driven by a 7% increase in operating income, a 5% increase in operating expenses 2, and a $1 million decrease in loan impairment expense."
> [ev-12] CBA/1H26/profit_announcement, printed p2: "The Bank’s statutory net profit after tax (NPAT) from continuing operations for the half year ended 31 December 2025 increased $270 million or 5% on the prior comparative period to $5,412 million."
> [ev-13] CBA/1H26/results_presentation, printed p53: "ROE (cash) 13.8% +10bpts"
> [ev-14] CBA/1H26/results_presentation, printed p53: "Cash NPAT ($m) 5,445 +6.1%"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Higher cash NPAT | +0.84 ppt | 78 | 2 () | ev-1, ev-6, ev-8, ev-9, ev-10, ev-14, ev-21, ev-22 |
| `equity_effect` | Partly offset by higher net assets | -0.74 ppt | 74 | 1 (single_source) | ev-4, ev-7, ev-17, ev-18, ev-19 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect — "Higher cash NPAT"
*+0.84 ppt | confidence 78/100*

Derived, not disclosed: 13.7% x 6.1% cash NPAT growth. Cash NPAT rose $313m or 6% to $5,445m, driven by a 7% operating income increase, a 5% rise in underlying operating expenses and a $1m LIE decrease. NII +6% on AIEA +8% ($96bn) offset by NIM -4bpts; other operating income +8%.
> [ev-1] CBA/1H26/profit_announcement, PDF p19: "Cash basis 13.8 13.4 13.7 40 bpts 10 bpts"
> [ev-6] CBA/1H26/profit_announcement, PDF p168: "ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-8] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million. The result was driven by a 7% increase in operating income, a 5% increase in operating expenses 2, and a $1 million decrease in loan impairment expense."
> [ev-9] CBA/1H26/profit_announcement, printed p2: "Net Interest Income (NII) increased 6%, primarily driven by a $96 billion or 8% increase in Average Interest Earning Assets (AIEA), partly offset by a 4 basis point decrease in Net Interest Margin (NIM)."
> [ev-10] CBA/1H26/profit_announcement, printed p2: "Other operating income increased 8% with higher trading income from Markets including favourable derivative valuation adjustments, growth in equities volumes, higher insurance income"
> [ev-14] CBA/1H26/results_presentation, printed p53: "Cash NPAT ($m) 5,445 +6.1%"
> [ev-21] CBA/1H26/results_presentation, printed p8: "5,132 5,120 5,445 1H25 2H25 1H26"
> [ev-22] CBA/1H26/results_presentation, printed p8: "Cash NPAT up 6% – strong operational performance, disciplined growth, investment in the franchise"

### equity_effect — "Partly offset by higher net assets"
*-0.74 ppt | confidence 74/100*

Derived as residual (0.1 ppt total less +0.84 earnings effect), and includes the interaction term. The bank says higher cash NPAT was "partly offset by higher net assets" (net average equity $74,176m to $78,004m, +$3,828m). Growth came from retained profits ($42,578m to $45,019m); no shares were bought back in 1H26 and the DRP was satisfied by on-market purchase.
> [ev-4] CBA/1H26/profit_announcement, PDF p168: "Average net assets 78,004 77,020 74,176"
> [ev-7] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-17] CBA/1H26/profit_announcement, PDF p121: "Closing balance 45,019 43,974 42,578"
> [ev-18] CBA/1H26/profit_announcement, PDF p121: "On 13 August 2025, the Group announced a 12-month extension of the on-market share buy-back of up to $1 billion of CBA ordinary shares originally announced on 9 August 2023. No shares were bought back during the half year ended 31 December 2025."
> [ev-19] CBA/1H26/profit_announcement, PDF p121: "The DRP in respect of the final 2024/2025, interim 2024/2025 and final 2023/2024 dividends were satisfied in full through the on-market purchase and transfer of 3,802,106 shares at $168.60, 4,545,082 shares at $149.89, 5,335,505 shares at $141.50, respectively, to participating shareholders."

## Notable items
- Underlying operating expense growth of 5% excludes restructuring and notable items; 1H26 notables relate to provisions for settlement of legal proceedings in NZ, an additional goodwill payment from ASIC's Better Banking review, and domestic customer remediation (ev-8, ev-24). Statutory operating expenses grew 8.1% (ev-15 page context).
- Other operating income +8% included a milestone payment on the sale of CommInsure General Insurance and favourable derivative valuation adjustments (ev-10).

## Source disagreements
- **Cash vs statutory ROE movement** (definitional): cash +10 bpts (13.7% to 13.8%) vs statutory continuing operations nil (13.8% to 13.8%) vs statutory including discontinued -10 bpts (13.7% to 13.6%)
  Preferred: cash +10 bpts (13.7% to 13.8%). Cash NPAT grew 6%/$313m while statutory NPAT grew only 5%/$270m, so statutory ROE was flat on a continuing basis and fell 10bpts including discontinued operations. Cash is CBA's core reported measure and the headline row.
- **Cash NPAT growth rate precision** (rounding): 6% (profit announcement narrative) vs 6.1% (presentation KPI summary)
  Preferred: 6.1%. The results book rounds to 6%; the presentation prints 6.1%. Ratio of cited levels ($5,445m vs $5,132m) is 6.10%, so 6.1% is used in the derivation.

## Limitations
- Neither the profit announcement nor the presentation publishes an ROE walk or bridge chart for 1H26 vs 1H25. The earnings/equity split is my own arithmetic derivation from the ROE endpoints and the disclosed cash NPAT growth rate, framed on the bank's own qualitative statement (ev-7); it is not a disclosed decomposition, hence driver confidence is capped below chart level.
- The 10 bpt total is itself a rounded figure: computed precisely from cited levels, 5,445/78,004 = 6.98% vs 5,132/74,176 = 6.92% per half, so the true delta is near +0.12 ppt annualised. The derived contributions (+0.84 / -0.74) therefore carry rounding uncertainty of a few bpts.
- The bank calls the equity effect only 'partly offset by higher net assets' and does not quantify how much of the $3,828m equity increase came from retained earnings versus reserves; the DRP being satisfied on-market and no 1H26 buyback are cited as directional support only.
- ROE denominators on pages 19 and 168 are average net assets on a continuing operations basis; the cash ROE row is identical (13.8/13.4/13.7) whether or not discontinued operations are included, but the statutory row differs.

## Provenance
- combo: agentic
- models: agent=anthropic/claude-opus-5, vision=anthropic/claude-opus-5
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T19:26:30+00:00
- seconds: 119.4
- cost_usd: 0.53
- tokens: 266141 in / 8957 out
- orchestration: agent
- tool_calls: 19
- pages_read: 6
- charts_read: 0
- budget_exhausted: no
