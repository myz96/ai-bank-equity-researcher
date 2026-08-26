# WBC — nim — FY25 vs FY24

**Movement (cash basis):** 195bps → 194bps (-1bps) | **Attribution confidence:** 95/100

WBC's Net Interest Margin (NIM) contracted by 1 basis point to 194 bps in FY25 compared to FY24. This decline was primarily driven by a 2 bps headwind from deposit pricing and mix, alongside 1 bps each from loan spread compression and wholesale funding costs. These negative pressures were partially offset by a 2 bps benefit from liquid assets and a 1 bps tailwind from capital/other items. Treasury & Markets contribution remained stable.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `funding.deposits` | Deposits | -2 bps | 85 | 1 (single_source) | ev-1, ev-15 |
| `asset_pricing` | Loans | -1 bps | 85 | 1 (single_source) | ev-1, ev-14 |
| `funding.wholesale` | WSF | -1 bps | 85 | 1 (single_source) | ev-1 |
| `liquids` | Liquid assets | +2 bps | 85 | 1 (single_source) | ev-1, ev-16 |
| `capital_replicating` | Capital & other | +1 bps | 85 | 1 (single_source) | ev-1 |
| `markets_treasury` | T&M | +0 bps | 85 | 1 (single_source) | ev-1, ev-13 |

### funding.deposits — "Deposits"
*-2 bps | confidence 85/100*

Deposit interest spreads decreased by 2 bps year-on-year, reflecting competitive pricing pressures or mix shifts within the deposit book.
> [ev-1] WBC/FY25/results_announcement, PDF p12: "[walk chart] Full Year 2025 - Full Year 2024 Net interest margin movement Excluding Notable Items: FY24 195.0 -> FY25 194.0"
> [ev-15] WBC/FY25/results_announcement, PDF p12: "Deposit interest spread: 2 basis points decrease"

### asset_pricing — "Loans"
*-1 bps | confidence 85/100*

Loan interest spreads narrowed by 1 bps, indicating margin compression on the lending side of the balance sheet.
> [ev-1] WBC/FY25/results_announcement, PDF p12: "[walk chart] Full Year 2025 - Full Year 2024 Net interest margin movement Excluding Notable Items: FY24 195.0 -> FY25 194.0"
> [ev-14] WBC/FY25/results_announcement, PDF p12: "Loan interest spread: 1 basis point narrower."

### funding.wholesale — "WSF"
*-1 bps | confidence 85/100*

Wholesale funding costs contributed a 1 bps headwind to NIM movement relative to the prior year.
> [ev-1] WBC/FY25/results_announcement, PDF p12: "[walk chart] Full Year 2025 - Full Year 2024 Net interest margin movement Excluding Notable Items: FY24 195.0 -> FY25 194.0"

### liquids — "Liquid assets"
*+2 bps | confidence 85/100*

Liquid assets provided a 2 bps positive contribution, likely due to favorable yield movements or mix changes in high-quality liquid assets.
> [ev-1] WBC/FY25/results_announcement, PDF p12: "[walk chart] Full Year 2025 - Full Year 2024 Net interest margin movement Excluding Notable Items: FY24 195.0 -> FY25 194.0"
> [ev-16] WBC/FY25/results_announcement, PDF p12: "Liquid Assets: 2 basis points increase"

### capital_replicating — "Capital & other"
*+1 bps | confidence 85/100*

Capital and other items contributed a net positive 1 bps to the margin movement.
> [ev-1] WBC/FY25/results_announcement, PDF p12: "[walk chart] Full Year 2025 - Full Year 2024 Net interest margin movement Excluding Notable Items: FY24 195.0 -> FY25 194.0"

### markets_treasury — "T&M"
*+0 bps | confidence 85/100*

Treasury & Markets contribution remained stable at 13 bps year-over-year, resulting in zero net impact on the margin movement.
> [ev-1] WBC/FY25/results_announcement, PDF p12: "[walk chart] Full Year 2025 - Full Year 2024 Net interest margin movement Excluding Notable Items: FY24 195.0 -> FY25 194.0"
> [ev-13] WBC/FY25/results_announcement, PDF p12: "Treasury and Markets contribution of 13 basis points, which was stable."

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-26T06:23:08+00:00
- seconds: 45.5
- cost_usd: 0.0008
- tokens: 14245 in / 3055 out
- orchestration: pipeline
