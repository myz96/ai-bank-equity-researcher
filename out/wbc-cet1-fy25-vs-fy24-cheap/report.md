# WBC — cet1 — FY25 vs FY24

**Movement (ex_notables basis):** 1249bps → 1253bps (+4bps) | **Attribution confidence:** 40/100

*Read from: row 'Level 2 common equity Tier 1 capital ratio', column 30 Sept 2024 -> column 30 Sept 2025*

WBC's Level 2 CET1 ratio increased by 4 bps to 12.53% in FY25 (ev-18). The movement was driven by net profit (+4 bps), largely offset by dividends (-8 bps total), higher Total RWA (-16 bps), and buybacks (-4 bps) (ev-1). A residual of +28 bps exists due to a walk summation failure in the primary source (ev-1), likely reflecting unquantified regulatory or model changes.

> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"
> [ev-13] WBC/FY25/results_announcement, PDF p6: "The CET1 capital ratio of 12.5% is above our target ratio of 11.25% in normal operating conditions."
> [ev-14] WBC/FY25/results_announcement, PDF p6: "The CET1 capital ratio increased 4 basis points as net profit was largely offset by the payment of dividends and increases in Risk Weighted Assets (RWA)."
> [ev-16] WBC/FY25/results_announcement, PDF p10: "Level 2 common equity Tier 1 capital ratio: - Australian Prudential Regulation Authority (APRA)"
> [ev-18] WBC/FY25/results_announcement, PDF p28: "The Level 2 CET1 capital ratio was 12.53% at 30 September 2025, 4 basis points higher than 30 September 2024."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_generation` | Net profit | +4 bps | 85 | 1 (single_source) | ev-1 |
| `dividend_net_drp` | 2024 final ordinary dividend | -4 bps | 85 | 1 (single_source) | ev-1 |
| `dividend_net_drp` | 2025 interim ordinary dividend | -4 bps | 85 | 1 (single_source) | ev-1 |
| `rwa` | Higher Total RWA | -16 bps | 85 | 1 (single_source) | ev-1, ev-20 |
| `capital_returns` | On market share buybacks | -4 bps | 85 | 1 (single_source) | ev-1 |
| *residual (unexplained)* | — | +28 bps | — | — |

### earnings_generation — "Net profit"
*+4 bps | confidence 85/100*

Net profit contributed +4 bps to the CET1 ratio movement from Sep 2024 to Sep 2025 (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### dividend_net_drp — "2024 final ordinary dividend"
*-4 bps | confidence 85/100*

The payment of the 2024 final ordinary dividend reduced the CET1 ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### dividend_net_drp — "2025 interim ordinary dividend"
*-4 bps | confidence 85/100*

The payment of the 2025 interim ordinary dividend reduced the CET1 ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### rwa — "Higher Total RWA"
*-16 bps | confidence 85/100*

Total RWA increased by $12.6 billion, mainly from higher IRRBB RWA, reducing the CET1 ratio by 16 bps (ev-1, ev-20).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"
> [ev-20] WBC/FY25/results_announcement, PDF p28: "Total RWA increased by $12.6 billion mainly from higher Interest Rate Risk in the banking book (IRRBB) RWA."

### capital_returns — "On market share buybacks"
*-4 bps | confidence 85/100*

On-market share buybacks reduced the CET1 ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

## Source disagreements
- **Walk Summation Failure** (error): Sum of bars: -24.0 bps (Source: ev-1) vs Actual Delta: +4.0 bps (Source: ev-16)
  Preferred: Actual Delta. The primary walk (ev-1) fails its own sum check (1249 + (-24) = 1225 != 1253). The delta is taken directly from the reported levels.

## Limitations
- The primary walk (ev-1) has a significant summation error (-24 bps vs +4 bps delta). A residual of +28 bps is declared.
- The residual likely captures unquantified drivers such as regulatory model changes or other reserve movements not explicitly broken out in the primary walk's bars.
- Half-on-half data (ev-2, ev-3) is excluded from the driver table as it does not match the FY24-FY25 comparison period.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Failed check: walk_sum (start 1249 + bars -24.0 = 1225.0 != end 1253, tol 1.0 bps) [WBC/FY25/results_announcement PDF p28 (ev-1)]

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T16:38:03+00:00
- seconds: 88.0
- cost_usd: 0.0029
- tokens: 71588 in / 5784 out
- orchestration: pipeline
- pages_extracted: 18
- reference_follow: ['WBC/FY25/investor_discussion_pack p125 <- p78 page 125 [added]']
