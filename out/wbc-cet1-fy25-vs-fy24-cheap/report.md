# WBC — cet1 — FY25 vs FY24

**Movement (ex_notables basis):** 1249bps → 1253bps (+4bps) | **Attribution confidence:** 40/100

*Read from: row 'Level 2 common equity Tier 1 capital ratio', column Sep-24 -> column Sep-25*

WBC's APRA Level 2 CET1 ratio increased by 4 bps to 12.53% in FY25 (ev-7). The movement is driven primarily by a 126 bps headwind from higher Total RWA and a 17 bps hit from share buybacks, partially offset by 4 bps of earnings generation. Dividends also contributed -8 bps. The published walk contains an unexplained residual.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `rwa` | Higher Total RWA | -126 bps | 85 | 1 (single_source) | ev-1, ev-14 |
| `capital_returns` | On market share buybacks | -17 bps | 85 | 1 (single_source) | ev-1 |
| `earnings_generation` | Net profit | +4 bps | 85 | 1 (single_source) | ev-1 |
| `dividend_net_drp` | 2024 final ordinary dividend | -4 bps | 85 | 1 (single_source) | ev-1 |
| `dividend_net_drp` | 2025 interim ordinary dividend | -4 bps | 85 | 1 (single_source) | ev-1 |
| `deductions_other` | Lower capitalised software balances | -4 bps | 85 | 1 (single_source) | ev-1 |
| `deductions_other` | Other reserve movements | +0 bps | 85 | 1 (single_source) | ev-1 |
| *residual (unexplained)* | — | +151 bps | — | — |

### rwa — "Higher Total RWA"
*-126 bps | confidence 85/100*

Total RWA increased by $12.6 billion, mainly from higher IRRBB RWA (ev-14). This was the dominant negative driver.
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"
> [ev-14] WBC/FY25/results_announcement, PDF p28: "Total RWA increased by $12.6 billion mainly from higher Interest Rate Risk in the banking book (IRRBB) RWA."

### capital_returns — "On market share buybacks"
*-17 bps | confidence 85/100*

Capital returned via on-market buybacks reduced the ratio by 17 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### earnings_generation — "Net profit"
*+4 bps | confidence 85/100*

Earnings generated contributed +4 bps to the capital ratio (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### dividend_net_drp — "2024 final ordinary dividend"
*-4 bps | confidence 85/100*

Payment of the 2024 final ordinary dividend reduced the ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### dividend_net_drp — "2025 interim ordinary dividend"
*-4 bps | confidence 85/100*

Payment of the 2025 interim ordinary dividend reduced the ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### deductions_other — "Lower capitalised software balances"
*-4 bps | confidence 85/100*

Lower capitalised software balances reduced the ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### deductions_other — "Other reserve movements"
*+0 bps | confidence 85/100*

Other reserve movements had no impact (0 bps) on the ratio (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

## Source disagreements
- **Walk Summation Error** (error): Sum of bars: -151 bps (Source: ev-1) vs Stated Delta: +4 bps (Source: ev-12)
  Preferred: Stated Delta. The primary walk (ev-1) fails its own summation check (-151 bps vs +4 bps stated). The narrative confirms the drivers but the arithmetic is broken.

## Limitations
- The primary walk (ev-1) has a significant arithmetic error (sum -151 bps vs stated delta +4 bps).
- A large residual of 151 bps exists in the published walk which is not explained by any bar or narrative.
- Context walks (ev-2, ev-3) are for H2 only and cannot be used to resolve the FY24-FY25 discrepancy.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Failed check: walk_sum (start 1249 + bars -151.0 = 1098.0 != end 1253, tol 1.0) [WBC/FY25/results_announcement PDF p28 (ev-1)]

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T21:07:01+00:00
- seconds: 64.4
- cost_usd: 0.0021
- tokens: 51756 in / 4310 out
- orchestration: pipeline
- pages_extracted: 18
- reference_follow: ['WBC/FY25/investor_discussion_pack p125 <- p78 page 125 [added]']
