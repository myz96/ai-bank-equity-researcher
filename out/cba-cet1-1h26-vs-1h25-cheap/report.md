# CBA — cet1 — 1H26 vs 1H25

**Movement (cash basis):** 1220bps → 1230bps (+10bps) | **Attribution confidence:** 60/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 31 Dec 24 -> column 31 Dec 25*

CBA's CET1 ratio increased by 10 bps to 12.3% in 1H26 vs 1H25. The movement is driven by a +24 bps regulatory model change (APS 117) and organic earnings generation, partially offset by dividends and RWA growth. No half-on-half walk covers this period; the bank's published Jun-Dec walk shows -87 bps dividend and +107 bps NPAT.

> [ev-17] CBA/1H26/profit_announcement, printed p28: "Summary Group Capital Adequacy Ratios ... Common Equity Tier 1 (CET1) ... 31 Dec 25: 12.3% ... 30 Jun 25: 12.3% ... 31 Dec 24: 12.2%"
> [ev-22] CBA/1H26/profit_announcement, PDF p157: "Common Equity Tier 1 12.3 12.3 12.2"
> [ev-41] CBA/1H26/results_presentation, printed p103: "Level 2 CET1 capital ratio of 12.3%"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `regulatory_model_changes` | APRA Overlay Release / APS 117 | +24 bps | 85 | 2 () | ev-20, ev-24 |
| *residual (unexplained)* | — | -14 bps | — | — |

### regulatory_model_changes — "APRA Overlay Release / APS 117"
*+24 bps | confidence 85/100*

Adoption of revised APS 117 framework effective 1 Oct 2025 reduced IRRBB RWA by ~$10bn, impacting CET1 by +24 bps (ev-20). This is the primary positive driver for the 1H26 vs 1H25 delta.
> [ev-20] CBA/1H26/profit_announcement, printed p28: "Includes the impact of the reduction to IRRBB RWA of ~$10 billion (CET1 impact of +24 bpts) on adoption of the revised APS 117 framework effective 1 October 2025."
> [ev-24] CBA/1H26/results_presentation, printed p105: "CET1 impact Net Impact"

### earnings_generation — "Cash NPAT"
*unquantified | confidence 60/100*

Organic earnings generation contributed positively. The bank's published Jun-Dec walk (context only) shows Cash NPAT at +107 bps (ev-1). For the 1H26 vs 1H25 period, the specific contribution is not explicitly quantified in the text, but implied as part of the net movement alongside the regulatory change.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital1 Strong capital position supporting franchise growth and dividends: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-9] CBA/1H26/results_presentation, printed p103: "[walk chart] CET1 capital ratio movements: Jun 25 Level 2 1230 -> Dec 25 Level 2 1230"

### dividend_net_drp — "Dividends"
*unquantified | confidence 60/100*

Dividends reduced CET1. The Jun-Dec walk shows -87 bps for '2H25 dividend (DRP neutralised)' (ev-1). The 1H26 final dividend included a $643m on-market purchase impacting CET1 by -13 bps (ev-19). The total 1H26 vs 1H25 impact is not separately quantified from the interim dividend.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital1 Strong capital position supporting franchise growth and dividends: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-19] CBA/1H26/profit_announcement, printed p28: "The 2025 final dividend included the on-market purchase of $643 million of shares (CET1 impact of -13 bpts) in respect of the Dividend Reinvestment Plan."

### rwa — "RWA"
*unquantified | confidence 60/100*

RWA movements were negative in the Jun-Dec context (-33 bps, ev-1), driven by Credit Risk (-34 bps, ev-4) and Operational Risk (-9 bps, ev-5), partially offset by IRRBB (+11 bps, ev-7). The specific 1H26 vs 1H25 RWA contribution is not isolated.
> [ev-1] CBA/1H26/results_presentation, printed p33: "[walk chart] Capital1 Strong capital position supporting franchise growth and dividends: Jun 25 Level 2 1230 -> Dec 25 Level 2 1220"
> [ev-4] CBA/1H26/results_presentation, printed p33: "[chart annotation] RWA: Credit Risk⁴ -34"
> [ev-5] CBA/1H26/results_presentation, printed p33: "[chart annotation] RWA: Operational Risk -9"
> [ev-7] CBA/1H26/results_presentation, printed p33: "[chart annotation] RWA: IRRBB +11"

## Source disagreements
- **Walk Period Mismatch** (timing): Context Walk: Jun 25 -> Dec 25 (ev-1) vs Task Comparison: Dec 24 -> Dec 25
  Preferred: Task Comparison. The bank provides a capital walk for the half-on-half period (Jun 2025 to Dec 2025) but does not provide a direct walk for the year-on-year period (Dec 2024 to Dec 2025). The drivers listed in the context walk cannot be directly attributed to the task comparison.

## Limitations
- No direct capital walk provided for 1H25 -> 1H26. Drivers are inferred or taken from the Jun-Dec context walk.
- Residual of -14 bps exists after accounting for the known +24 bps regulatory change and the implied net of other factors.
- Specific contributions of NPAT and Dividends for the 1H25->1H26 window are not explicitly stated, only for the Jun-Dec window.
- No published walk covers 1H26 vs 1H25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T16:51:02+00:00
- seconds: 93.5
- cost_usd: 0.0029
- tokens: 65139 in / 7202 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/1H26/profit_announcement p49 <- p48 page 29']
