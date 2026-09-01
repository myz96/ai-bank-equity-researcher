# WBC — nim — FY25 vs FY24

**Movement (ex_notables basis):** 195bps → 194bps (-1bps) | **Attribution confidence:** 40/100

*Read from: row 'NIM (Excluding Notable Items, %)', column Full Year Sept 2024 -> column Full Year Sept 2025*

Westpac's Group net interest margin (NIM, Excluding Notable Items) fell 1 basis point in FY25 to 1.94%, from 1.95% in FY24. The movement comprised a 1bp contraction in Core NIM to 1.81% (from 1.82%) while the Treasury & Markets contribution was stable at 13 basis points. The results book's walk attributes the 1bp decline to: Loans -1bp, Deposits -2bps, Liquid assets +2bps, Wholesale funding -1bp, Capital & other +1bp, and Treasury & Markets 0. The investor discussion pack corroborates the levels (NIM 1.95% to 1.94%, Core NIM 1.82% to 1.81%, T&M 0.13% to 0.13%).

> [ev-1] WBC/FY25/results_announcement, PDF p12: "[walk chart] Net interest margin movement - Full Year 2025 - Full Year 2024: FY24 195 -> FY25 194"
> [ev-2] WBC/FY25/results_announcement, PDF p11: "NIM (Excluding Notable Items, %) NIM 1.94% 1.95% (1 bps) 1.95% 1.92% 3 bps Core NIM 1.81% 1.82% (1 bps) 1.82% 1.80% 2 bps"
> [ev-3] WBC/FY25/results_announcement, PDF p12: "NIM decreased 1 basis point to 1.94%."
> [ev-9] WBC/FY25/results_announcement, PDF p12: "Treasury and Markets contribution of 13 basis points, which was stable."
> [ev-10] WBC/FY25/investor_discussion_pack, printed p46: "Composition of NIM (%) FY24 FY25 1H25 2H25 Core NIM 1.82 1.81 1.80 1.82 Treasury & Markets 0.13 0.13 0.12 0.13 NIM 1.95 1.94 1.92 1.95"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `asset_pricing` | Loans | -1 bps | 92 | 1 (single_source) | ev-1, ev-4 |
| `funding.deposits` | Deposits | -2 bps | 92 | 1 (single_source) | ev-1, ev-5 |
| `liquids` | Liquid assets | +2 bps | 92 | 1 (single_source) | ev-1, ev-6 |
| `funding.wholesale` | WSF (Wholesale funding) | -1 bps | 92 | 1 (single_source) | ev-1, ev-7 |
| `capital_replicating` | Capital & other | +1 bps | 92 | 1 (single_source) | ev-1, ev-8 |
| `markets_treasury` | T&M (Treasury & Markets) | +0 bps | 92 | 1 (single_source) | ev-1, ev-9 |
| *residual (unexplained)* | — | +0 bps | — | — |

### asset_pricing — "Loans"
*-1 bps | confidence 92/100*

Loan interest spread 1bp narrower. Higher spreads in New Zealand mortgages driven by fixed rate repricing was more than offset by tighter spreads in Australia due to competition and the sale of the auto finance portfolio.
> [ev-1] WBC/FY25/results_announcement, PDF p12: "[walk chart] Net interest margin movement - Full Year 2025 - Full Year 2024: FY24 195 -> FY25 194"
> [ev-4] WBC/FY25/results_announcement, PDF p12: "Loan interest spread: 1 basis point narrower."

### funding.deposits — "Deposits"
*-2 bps | confidence 92/100*

Deposit interest spread 2bps decrease with a mix shift towards lower spread savings products, margin compression in term deposits and the impact from lower interest rates. Earnings on hedged deposits were higher.
> [ev-1] WBC/FY25/results_announcement, PDF p12: "[walk chart] Net interest margin movement - Full Year 2025 - Full Year 2024: FY24 195 -> FY25 194"
> [ev-5] WBC/FY25/results_announcement, PDF p12: "Deposit interest spread: 2 basis points decrease with a mix shift towards lower spread savings products, margin compression in term deposits and the impact from lower interest rates."

### liquids — "Liquid assets"
*+2 bps | confidence 92/100*

Liquid Assets 2bps increase as average liquid assets rose by less than average lending assets.
> [ev-1] WBC/FY25/results_announcement, PDF p12: "[walk chart] Net interest margin movement - Full Year 2025 - Full Year 2024: FY24 195 -> FY25 194"
> [ev-6] WBC/FY25/results_announcement, PDF p12: "Liquid Assets: 2 basis points increase as average liquid assets rose by less than average lending assets;"

### funding.wholesale — "WSF (Wholesale funding)"
*-1 bps | confidence 92/100*

Wholesale funding 1bp decrease from the impact of higher funding costs, with the final Term Funding Facility (TFF) draw downs maturing in the prior year.
> [ev-1] WBC/FY25/results_announcement, PDF p12: "[walk chart] Net interest margin movement - Full Year 2025 - Full Year 2024: FY24 195 -> FY25 194"
> [ev-7] WBC/FY25/results_announcement, PDF p12: "Wholesale funding: 1 basis point decrease from the impact of higher funding costs, with the final Term Funding Facility (TFF) draw downs maturing in the prior year;"

### capital_replicating — "Capital & other"
*+1 bps | confidence 92/100*

Capital and Other 1bp increase primarily from higher earnings on hedged capital balances.
> [ev-1] WBC/FY25/results_announcement, PDF p12: "[walk chart] Net interest margin movement - Full Year 2025 - Full Year 2024: FY24 195 -> FY25 194"
> [ev-8] WBC/FY25/results_announcement, PDF p12: "Capital and Other: 1 basis point increase primarily from higher earnings on hedged capital balances."

### markets_treasury — "T&M (Treasury & Markets)"
*+0 bps | confidence 92/100*

Treasury & Markets contribution of 13 basis points, which was stable (no change to NIM).
> [ev-1] WBC/FY25/results_announcement, PDF p12: "[walk chart] Net interest margin movement - Full Year 2025 - Full Year 2024: FY24 195 -> FY25 194"
> [ev-9] WBC/FY25/results_announcement, PDF p12: "Treasury and Markets contribution of 13 basis points, which was stable."

## Limitations
- The investor discussion pack's NIM walk (page 24) covers the half-on-half comparison (Mar 2025 to Sep 2025), not the FY24-to-FY25 task comparison, so its bars were not used as driver contributions; the results announcement page 12 walk is the primary framing and passed its sum check.
- The pack page 24 walk is context only; its sub-driver annotations (e.g. NZ mortgages 1bp, auto finance -1bp, consumer savings reprice 3bps) belong to the half-on-half period and were not used.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Failed check: movement_from_variant (the row you read is a 'excluding notable' variant: row 'NIM (Excluding Notable Items, %)', column Full Year Sept 2024 -> column Full Year Sept 2025. Read the headline measure instead, and report the variant as context or as a disagreement)

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-09-01T08:00:28+00:00
- seconds: 923.9
- cost_usd: 0.0078
- tokens: 141452 in / 7576 out
- orchestration: agent
- tool_calls: 16
- pages_read: 4
- charts_read: 2
- budget_exhausted: no
