# WBC — cet1 — FY25 vs FY24

**Movement (ex_notables basis):** 1249bps → 1253bps (+4bps) | **Attribution confidence:** 40/100

*Read from: row 'Level 2 common equity Tier 1 capital ratio', column As at 30 Sept 2024 -> column As at 30 Sept 2025*

WBC's Level 2 CET1 ratio increased by 4 bps to 12.53% in FY25 (ev-24). The movement was driven by earnings generation (+4 bps), partially offset by dividends (-8 bps total), higher Total RWA (-4 bps), and on-market share buybacks (-4 bps) (ev-1). Other reserve movements contributed +4 bps, while lower capitalised software balances reduced the ratio by 4 bps (ev-1).

> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249.0 -> 30 Sept 2025 1253.0"
> [ev-18] WBC/FY25/results_announcement, PDF p6: "The CET1 capital ratio of 12.5% is above our target ratio of 11.25% in normal operating conditions."
> [ev-19] WBC/FY25/results_announcement, PDF p6: "The CET1 capital ratio increased 4 basis points as net profit was largely offset by the payment of dividends and increases in Risk Weighted Assets (RWA)."
> [ev-24] WBC/FY25/results_announcement, PDF p28: "The Level 2 CET1 capital ratio was 12.53% at 30 September 2025, 4 basis points higher than 30 September 2024."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_generation` | Net profit | +4 bps | 85 | 1 (single_source) | ev-1 |
| `dividend_net_drp` | Dividends | -8 bps | 80 | 1 (single_source) | ev-1 |
| `rwa` | Higher Total RWA | -4 bps | 85 | 1 (single_source) | ev-1, ev-26 |
| `capital_returns` | On market share buybacks | -4 bps | 85 | 1 (single_source) | ev-1 |
| `deductions_other` | Other reserve movements | +4 bps | 85 | 1 (single_source) | ev-1 |
| `deductions_other` | Lower capitalised software balances | -4 bps | 85 | 1 (single_source) | ev-1 |
| *residual (unexplained)* | — | +16 bps | — | — |

### earnings_generation — "Net profit"
*+4 bps | confidence 85/100*

Capital generated from net profit contributed +4 bps to the CET1 ratio for the full year ended September 2025 compared to September 2024 (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249.0 -> 30 Sept 2025 1253.0"

### dividend_net_drp — "Dividends"
*-8 bps | confidence 80/100*

The payment of the 2024 final ordinary dividend (-4 bps) and the 2025 interim ordinary dividend (-4 bps) reduced the CET1 ratio by a combined 8 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249.0 -> 30 Sept 2025 1253.0"

### rwa — "Higher Total RWA"
*-4 bps | confidence 85/100*

Total Risk Weighted Assets increased by $12.6 billion, primarily due to higher Interest Rate Risk in the Banking Book (IRRBB) RWA, resulting in a -4 bps impact on the CET1 ratio (ev-1, ev-26).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249.0 -> 30 Sept 2025 1253.0"
> [ev-26] WBC/FY25/results_announcement, PDF p28: "Total RWA increased by $12.6 billion mainly from higher Interest Rate Risk in the banking book (IRRBB) RWA."

### capital_returns — "On market share buybacks"
*-4 bps | confidence 85/100*

On-market share buybacks during the period reduced the CET1 ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249.0 -> 30 Sept 2025 1253.0"

### deductions_other — "Other reserve movements"
*+4 bps | confidence 85/100*

Movements in other reserves contributed positively to the CET1 ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249.0 -> 30 Sept 2025 1253.0"

### deductions_other — "Lower capitalised software balances"
*-4 bps | confidence 85/100*

Lower capitalised software balances resulted in a negative contribution of 4 bps to the CET1 ratio (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249.0 -> 30 Sept 2025 1253.0"

## Source disagreements
- **Walk Summation** (error): Sum of bars: -12.0 bps (Source: WBC/FY25/results_announcement PDF p28) vs Stated Delta: +4.0 bps (Source: WBC/FY25/results_announcement PDF p28)
  Preferred: Stated Delta. The published walk chart (ev-1) lists individual bar values that sum to -12.0 bps, which contradicts the stated delta of +4.0 bps and the endpoint levels (1249 -> 1253). This indicates a likely typographical error in the printed bar values within the source document.

## Limitations
- The primary walk chart (ev-1) contains an internal summation error where the listed driver contributions do not reconcile with the reported delta or endpoints.
- A residual of +16.0 bps is required to bridge the gap between the sum of the stated drivers (-12.0 bps) and the actual movement (+4.0 bps).
- Confidence is capped because the specific drivers accounting for the +16.0 bps residual are not explicitly quantified in the provided evidence records for this comparison span.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Capped at 80: dividend_net_drp -8 bps. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.
- Failed check: walk_sum (start 1249.0 + bars -12.0 = 1237.0 != end 1253.0, tol 1.0 bps) [WBC/FY25/results_announcement PDF p28 (ev-1)]

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T15:06:42+00:00
- seconds: 125.4
- cost_usd: 0.003
- tokens: 73111 in / 6287 out
- orchestration: pipeline
- pages_extracted: 18
- reference_follow: ['WBC/FY25/investor_discussion_pack p125 <- p78 page 125 [added]']
