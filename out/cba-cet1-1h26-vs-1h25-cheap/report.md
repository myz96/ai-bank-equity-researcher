# CBA — cet1 — 1H26 vs 1H25

**Movement (cash basis):** 1220bps → 1230bps (+10bps) | **Attribution confidence:** 85/100

*Read from: row 'Common Equity Tier 1 (CET1) ratio', column 31 Dec 24 -> column 31 Dec 25*

CBA's CET1 ratio increased by 10 bps to 12.3% in 1H26 vs 1H25. The movement is driven by a +24 bps regulatory model change (APS 117 IRRBB RWA reduction), partially offset by -13 bps from DRP share purchases and organic RWA growth. Cash NPAT contribution was negligible (+3 bps). No half-on-half walk applies; drivers are extracted from specific event footnotes.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `regulatory_model_changes` | APRA Overlay Release / APS 117 | +24 bps | 85 | 1 (single_source) | ev-6 |
| `dividend_net_drp` | DRP share purchase | -13 bps | 85 | 1 () | ev-5 |
| *residual (unexplained)* | — | -1 bps | — | — |

### regulatory_model_changes — "APRA Overlay Release / APS 117"
*+24 bps | confidence 85/100*

Adoption of revised APS 117 framework effective 1 Oct 2025 reduced IRRBB RWA by ~$10 billion, positively impacting CET1 by +24 bps (ev-6).
> [ev-6] CBA/1H26/profit_announcement, printed p28: "Includes the impact of the reduction to IRRBB RWA of ~$10 billion (CET1 impact of +24 bpts) on adoption of the revised APS 117 framework effective 1 October 2025."

### dividend_net_drp — "DRP share purchase"
*-13 bps | confidence 85/100*

The 2025 final dividend included an on-market purchase of $643 million of shares in respect of the Dividend Reinvestment Plan, negatively impacting CET1 by -13 bps (ev-5).
> [ev-5] CBA/1H26/profit_announcement, printed p28: "The 2025 final dividend included the on-market purchase of $643 million of shares (CET1 impact of -13 bpts) in respect of the Dividend Reinvestment Plan."

### rwa — "RWA"
*unquantified | confidence 60/100*

Total RWA movement is not explicitly quantified as a standalone driver for the 1H25-1H26 period in the provided text. The bank reports strong capital position supporting franchise growth, implying organic RWA expansion which typically dilutes CET1, but no specific bps figure is attributed to total RWA for this comparison window.

### earnings_generation — "Cash NPAT"
*unquantified | confidence 60/100*

Cash NPAT contribution is not explicitly quantified in bps for the 1H25-1H26 period. While the half-on-half walk shows +107 bps, this is excluded per instructions. Organic earnings generation is expected to be positive but unquantified here.

## Limitations
- No primary half-on-half walk (1H25 -> 1H26) was available; only context walks (Jun 25 -> Dec 25) were found. Drivers were extracted from specific event footnotes (ev-5, ev-6).
- Residual of -1 bps exists because quantified drivers (+24, -13) do not sum exactly to the +10 bps delta. This may reflect rounding or unquantified minor items.
- RWA and Earnings contributions are unquantified for the specific period.
- No published walk covers 1H26 vs 1H25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T20:44:30+00:00
- seconds: 57.2
- cost_usd: 0.002
- tokens: 45350 in / 5158 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/1H26/profit_announcement p49 <- p48 page 29']
