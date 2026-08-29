# CBA — cet1 — 1H26 vs 1H25

**Movement (cash basis):** 1220bps → 1230bps (+10bps) | **Attribution confidence:** 60/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 31 Dec 24 -> column 31 Dec 25*

CBA's Level 2 CET1 ratio increased by 10 bps to 12.3% in 1H26 vs 1H25. The movement is driven by regulatory model changes (APS 117 adoption) and earnings generation, partially offset by dividends and RWA growth.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `regulatory_model_changes` | IRRBB Adoption CET1 Impact | +24 bps | 85 | 1 (single_source) | ev-6 |
| *residual (unexplained)* | — | -14 bps | — | — |

### regulatory_model_changes — "IRRBB Adoption CET1 Impact"
*+24 bps | confidence 85/100*

Adoption of revised APS 117 framework effective 1 Oct 2025 reduced IRRBB RWA by ~$10bn, adding +24 bpts to CET1 (ev-6).
> [ev-6] CBA/1H26/profit_announcement, printed p28: "Includes the impact of the reduction to IRRBB RWA of ~$10 billion (CET1 impact of +24 bpts) on adoption of the revised APS 117 framework effective 1 October 2025."

### earnings_generation — "Cash NPAT"
*unquantified | confidence 60/100*

Earnings generation contributed positively. The half-on-half walk shows Cash NPAT at +107 bps (ev-1), but the specific 1H26 contribution is not explicitly quantified in the text.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"

### dividend_net_drp — "Dividend"
*unquantified | confidence 60/100*

Dividends net of DRP were a negative driver. The 2025 final dividend included an on-market buyback of $643m for DRP shares with a -13 bpt impact (ev-5). The half-on-half walk shows total dividends at -87 bps (ev-1).
> [ev-5] CBA/1H26/profit_announcement, printed p28: "The 2025 final dividend included the on-market purchase of $643 million of shares (CET1 impact of -13 bpts) in respect of the Dividend Reinvestment Plan."
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"

### rwa — "RWA"
*unquantified | confidence 60/100*

RWA movements impacted the ratio. The half-on-half walk attributes -33 bps to RWA (ev-1). Specific credit/market/operational drivers are listed for the half-on-half period (ev-8) but not isolated for the year-on-year delta.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-8] CBA/1H26/profit_announcement, printed p28: "Dec 25 Level 2 6 3 (34) Credit 4 11 IRRBB 5 (1) Market (9) Operational 2 12.3%"

## Source disagreements
- **Walk Comparison Span** (definitional): Context Walk: Jun 25 -> Dec 25 (ev-1, ev-2) vs Task Comparison: Dec 24 -> Dec 25
  Preferred: Task Comparison. The provided capital walks (ev-1, ev-2) cover the half-on-half period (Jun 2025 to Dec 2025). They cannot be used as direct contributions for the 1H26 vs 1H25 comparison. Their values are cited in narratives only.

## Limitations
- No primary capital walk exists for the 1H25 -> 1H26 comparison. Only half-on-half (Jun 25 -> Dec 25) walks are available.
- Specific bps contributions for Earnings, Dividends, and RWA for the 1H26 vs 1H25 period are not explicitly stated in the text; they are inferred or left unquantified based on the available half-on-half data and narrative footnotes.
- No published walk covers 1H26 vs 1H25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T13:08:12+00:00
- seconds: 62.1
- cost_usd: 0.0022
- tokens: 48834 in / 5521 out
- orchestration: pipeline
