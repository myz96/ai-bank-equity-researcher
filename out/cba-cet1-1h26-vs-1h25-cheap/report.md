# CBA — cet1 — 1H26 vs 1H25

**Movement (cash basis):** 1220bps → 1230bps (+10bps) | **Attribution confidence:** 75/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 31 Dec 24 -> column 31 Dec 25*

CBA's APRA Level 2 CET1 ratio increased by 10 bps to 12.3% in 1H26 (vs 12.2% in 1H25). The movement was driven by a +24 bps regulatory model change from revised APS 117 adoption, partially offset by -13 bps from on-market buybacks within the DRP and organic RWA growth. Cash NPAT contributed positively but was insufficient to fully offset these capital drains.

> [ev-8] CBA/1H26/profit_announcement, printed p28: "Summary Group Capital Adequacy Ratios Common Equity Tier 1 (CET1) 12.3 12.3 12.2 – 10 bpts"
> [ev-10] CBA/1H26/profit_announcement, printed p28: "Dec 25 vs Dec 24 % 10 bpts"
> [ev-12] CBA/1H26/profit_announcement, printed p28: "Includes the impact of the reduction to IRRBB RWA of ~$10 billion (CET1 impact of +24 bpts) on adoption of the revised APS 117 framework effective 1 October 2025."
> [ev-11] CBA/1H26/profit_announcement, printed p28: "The 2025 final dividend included the on-market purchase of $643 million of shares (CET1 impact of -13 bpts) in respect of the Dividend Reinvestment Plan."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `regulatory_model_changes` | APS 117 Adoption | +24 bps | 85 | 1 (single_source) | ev-12 |
| `capital_returns` | DRP Buyback | -13 bps | 85 | 1 (single_source) | ev-11 |
| *residual (unexplained)* | — | -1 bps | — | — |

### regulatory_model_changes — "APS 117 Adoption"
*+24 bps | confidence 85/100*

Adoption of the revised APS 117 framework effective 1 October 2025 reduced IRRBB RWA by ~$10 billion, providing a +24 bps CET1 impact (ev-12).
> [ev-12] CBA/1H26/profit_announcement, printed p28: "Includes the impact of the reduction to IRRBB RWA of ~$10 billion (CET1 impact of +24 bpts) on adoption of the revised APS 117 framework effective 1 October 2025."

### capital_returns — "DRP Buyback"
*-13 bps | confidence 85/100*

The 2025 final dividend included an on-market purchase of $643 million of shares in respect of the Dividend Reinvestment Plan, resulting in a -13 bps CET1 impact (ev-11).
> [ev-11] CBA/1H26/profit_announcement, printed p28: "The 2025 final dividend included the on-market purchase of $643 million of shares (CET1 impact of -13 bpts) in respect of the Dividend Reinvestment Plan."

### rwa — "RWA Growth"
*unquantified | confidence 60/100*

Total RWA grew from $496bn (Jun 25) to $505bn (Dec 25), exerting downward pressure on the ratio. The bank does not explicitly quantify the specific 1H26 vs 1H25 RWA contribution in bps for this comparison; the Jun-Dec walk shows -33 bps (ev-1).
> [ev-17] CBA/1H26/results_presentation, printed p105: "Total RWA: % of RWA:"
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital1: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"

### earnings_generation — "Cash NPAT"
*unquantified | confidence 60/100*

Cash NPAT generated capital. The Jun-Dec walk attributes +107 bps to Cash NPAT (ev-1). The specific 1H26 vs 1H25 contribution is not explicitly isolated in the provided text.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital1: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"

## Source disagreements
- **Walk Comparison Span** (definitional): Context Walk: Jun 25 -> Dec 25 (-10 bps net, ev-1) vs Task Comparison: Dec 24 -> Dec 25 (+10 bps net, ev-8)
  Preferred: Task Comparison. The available capital walk (ev-1) covers the half-on-half period (Jun 2025 to Dec 2025), not the required year-on-year period (Dec 2024 to Dec 2025). The task requires the latter.

## Limitations
- No explicit capital walk exists for the 1H25 (Dec 24) to 1H26 (Dec 25) comparison.
- Drivers like Cash NPAT and Total RWA are unquantified for the specific window; values from the Jun-Dec context walk are cited for narrative only.
- Residual of -1 bps remains after accounting for known regulatory and buyback impacts.
- No published walk covers 1H26 vs 1H25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T23:18:52+00:00
- seconds: 247.8
- cost_usd: 0.0021
- tokens: 47730 in / 5268 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/1H26/profit_announcement p49 <- p48 page 29']
