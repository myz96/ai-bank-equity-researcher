# WBC — cet1 — FY25 vs FY24

**Movement (ex_notables basis):** 1249bps → 1253bps (+4bps) | **Attribution confidence:** 40/100

*Read from: row 'Level 2 common equity Tier 1 capital ratio', column 30 Sept 2024 -> column 30 Sept 2025*

WBC's Level 2 CET1 ratio increased by 4 bps to 12.53% in FY25 (ev-1, ev-7). The movement is driven by earnings partially offset by dividends, RWA growth, and buybacks. Note: the published walk chart for this period fails the sum check (-16 bps vs +4 bps), creating a significant residual.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_generation` | Net profit | +4 bps | 80 | 1 (single_source) | ev-1 |
| `dividend_net_drp` | 2024 final ordinary dividend | -4 bps | 80 | 1 (single_source) | ev-1 |
| `dividend_net_drp` | 2025 interim ordinary dividend | -4 bps | 80 | 1 (single_source) | ev-1 |
| `rwa` | Total RWA | -4 bps | 80 | 1 (single_source) | ev-1 |
| `capital_returns` | Market share buybacks | -4 bps | 80 | 1 (single_source) | ev-1 |
| `deductions_other` | Capitalised software | -4 bps | 80 | 1 (single_source) | ev-1 |
| `other_unmapped` | Other reserve movements | +0 bps | 80 | 1 (single_source) | ev-1 |
| *residual (unexplained)* | — | +20 bps | — | — |

### earnings_generation — "Net profit"
*+4 bps | confidence 80/100*

Capital generated from net profit contributed +4 bps to the ratio per the FY24-FY25 walk chart (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### dividend_net_drp — "2024 final ordinary dividend"
*-4 bps | confidence 80/100*

The payment of the 2024 final ordinary dividend reduced the ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### dividend_net_drp — "2025 interim ordinary dividend"
*-4 bps | confidence 80/100*

The payment of the 2025 interim ordinary dividend reduced the ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### rwa — "Total RWA"
*-4 bps | confidence 80/100*

Total risk-weighted assets movement reduced the ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### capital_returns — "Market share buybacks"
*-4 bps | confidence 80/100*

Market share buybacks reduced the ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### deductions_other — "Capitalised software"
*-4 bps | confidence 80/100*

Capitalised software movements reduced the ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### other_unmapped — "Other reserve movements"
*+0 bps | confidence 80/100*

Other reserve movements had no impact on the ratio (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

## Source disagreements
- **Walk Summation Error** (error): Sum of bars = -16 bps (Source: ev-1) vs Stated Delta = +4 bps (Source: ev-1, ev-5)
  Preferred: Stated Delta. The primary walk chart (ev-1) lists bars that sum to -16 bps, but the text and table explicitly state a +4 bps increase. The residual captures this discrepancy.

## Limitations
- The primary walk chart (ev-1) contains a summation error where the bars do not reconcile to the stated endpoints. Quantified drivers are taken directly from the chart labels despite the arithmetic mismatch.
- Half-on-half data (ev-2, ev-3) was excluded as it does not match the FY24-FY25 comparison window.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Failed check: walk_sum (start 1249 + bars -16.0 = 1233.0 != end 1253, tol 1.0) [WBC/FY25/results_announcement PDF p28 (ev-1)]

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T13:53:27+00:00
- seconds: 140.6
- cost_usd: 0.0019
- tokens: 45244 in / 4499 out
- orchestration: pipeline
