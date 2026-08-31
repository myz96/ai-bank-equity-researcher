# CBA — nim — FY25 vs FY24

**Movement (cash basis):** 199bps → 208bps (+9bps) | **Attribution confidence:** 90/100

*Read from: row 'Net interest margin (%)', column Full Year Ended 30 Jun 24 -> column Full Year Ended 30 Jun 25*

CBA's net interest margin (cash basis) increased 9 bps to 2.08% in FY25 from 1.99% in FY24, driven by +9 bps from capital, replicating portfolio and hedges, partially offset by −7 bps from funding costs (increased deposit price competition) and −1 bps from basis risk. Liquids & pooled facilities contributed +7 bps (a reduction in lower-yielding liquid assets (+5 bps) and institutional pooled lending facilities (+2 bps)), while asset pricing and portfolio mix were flat. Excluding the liquids/pooled facilities effect, underlying NIM improved only 2 bps.

> [ev-10] CBA/FY25/profit_announcement, printed p3: "Net interest margin (%) 2.08 1.99 9 bpts"
> [ev-22] CBA/FY25/profit_announcement, printed p12: "Net interest margin (%) 2.08 1.99 9bpts"
> [ev-23] CBA/FY25/profit_announcement, printed p12: "The Bank's net interest margin increased 9 basis points on the prior year to 2.08%. Excluding a 7 basis point increase in margin from a reduction in lower yielding liquid assets and institutional pooled facilities, which have a broadly neutral impact on net interest income, net interest margin increased 2 basis points."
> [ev-19] CBA/FY25/profit_announcement, PDF p9: "Excluding the mix effect of lower liquid assets and institutional pooled facilities, margins improved by 2bpts."
> [ev-20] CBA/FY25/profit_announcement, PDF p9: "The modest increase was primarily due to higher earnings on capital and replicating portfolio hedges, partly offset by the impact of increased competition on deposit pricing."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & Pooled Facilities | +7 bps | 85 | 1 (single_source) | ev-18, ev-23 |
| `asset_pricing` | Asset pricing | +0 bps | 80 | 1 (single_source) | ev-12 |
| `funding.deposits` | Funding costs | -7 bps | 85 | 1 (single_source) | ev-13 |
| `mix` | Portfolio mix | +0 bps | 80 | 1 (single_source) | ev-14 |
| `basis_risk` | Basis risk | -1 bps | 85 | 1 (single_source) | ev-15 |
| `capital_replicating` | Capital, Replicating and Other | +9 bps | 85 | 1 (single_source) | ev-16 |
| `markets_treasury` | Treasury and Markets | +1 bps | 85 | 1 (single_source) | ev-17 |

### liquids — "Liquids & Pooled Facilities"
*+7 bps | confidence 85/100*

Reduction in lower yielding liquid assets drove a +5 bps increase and institutional pooled lending facilities drove a +2 bps increase in margin respectively.
> [ev-18] CBA/FY25/profit_announcement, printed p12: "1 Reduction in lower yielding liquid assets and institutional pooled lending facilities drove a 5 basis point and 2 basis point increase in margin respectively."
> [ev-23] CBA/FY25/profit_announcement, printed p12: "The Bank's net interest margin increased 9 basis points on the prior year to 2.08%. Excluding a 7 basis point increase in margin from a reduction in lower yielding liquid assets and institutional pooled facilities, which have a broadly neutral impact on net interest income, net interest margin increased 2 basis points."

### asset_pricing — "Asset pricing"
*+0 bps | confidence 80/100*

The bank states asset pricing was flat for FY25 vs FY24, contributing 0 bps to the NIM movement.
> [ev-12] CBA/FY25/profit_announcement, printed p12: "Asset pricing: Flat."

### funding.deposits — "Funding costs"
*-7 bps | confidence 85/100*

Funding costs decreased margin by 7 bps driven by increased deposit price competition.
> [ev-13] CBA/FY25/profit_announcement, printed p12: "Funding costs: Decreased margin by 7 basis points driven by increased deposit price competition."

### mix — "Portfolio mix"
*+0 bps | confidence 80/100*

The bank states portfolio mix was flat for FY25 vs FY24, contributing 0 bps to the NIM movement.
> [ev-14] CBA/FY25/profit_announcement, PDF p29: "Portfolio mix: Flat."

### basis_risk — "Basis risk"
*-1 bps | confidence 85/100*

Basis risk decreased margin by 1 bps reflecting an increase in the average spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate.
> [ev-15] CBA/FY25/profit_announcement, PDF p29: "Basis risk: Basis risk arises from the spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate. The Bank's margin decreased 1 basis point reflecting an increase in the average spread."

### capital_replicating — "Capital, Replicating and Other"
*+9 bps | confidence 85/100*

Increased margin by 9 bps driven by the net impact of the replicating portfolio due to changes in portfolio rate and volume (+5 bps) and higher earnings on capital hedges (+4 bps).
> [ev-16] CBA/FY25/profit_announcement, PDF p29: "Capital, Replicating and Other: Increased margin by 9 basis points driven by the net impact of the replicating portfolio due to changes in portfolio rate and volume (up 5 basis points) and higher earnings on capital hedges (up 4 basis points)."

### markets_treasury — "Treasury and Markets"
*+1 bps | confidence 85/100*

Treasury and Markets increased margin by 1 bps.
> [ev-17] CBA/FY25/profit_announcement, PDF p29: "Treasury and Markets: Increased margin by 1 basis point."

## Limitations
- The walk chart is from the results book (profit_announcement p28), which is the primary source. The FY24 results_presentation does not cover the FY25 vs FY24 comparison and cannot corroborate this specific walk.
- The underlying NIM improvement of 2 bps (excl. liquids and pooled facilities) is stated by the bank but not decomposed into sub-drivers beyond what appears in the walk.
- Capped at 80: asset_pricing +0 bps, mix +0 bps. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY25/profit_announcement (e2e911ab4fed), CBA/FY24/profit_announcement (1ab9332c8371), CBA/FY24/results_presentation (168e3835d44c)
- generated: 2026-08-31T00:10:00+00:00
- seconds: 113.5
- cost_usd: 0.023
- tokens: 843366 in / 7248 out
- orchestration: agent
- tool_calls: 36
- pages_read: 10
- charts_read: 1
- budget_exhausted: no
