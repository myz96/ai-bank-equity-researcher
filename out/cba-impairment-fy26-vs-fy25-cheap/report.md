# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 80/100

*Read from: row 'Loan impairment expense', column FY25 -> column FY26*

CBA's loan impairment expense increased $62 million to $788 million in FY26 (ev-19). The loss rate rose 1 basis point to 8 bps on average GLAA (ev-22), driven by a $150 million increase in collective provisions offset by a $17 million reduction in individual net provisions.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Net collective provision funding | +150 $m | 90 | 2 () | ev-4, ev-27 |
| `individual_provisions` | Net new and increased individual provisioning | -17 $m | 85 | 1 (single_source) | ev-5, ev-6 |
| *residual (unexplained)* | — | -71 $m | — | — |

### collective.asset_quality — "Net collective provision funding"
*+150 $m | confidence 90/100*

Collective provisions increased $150 million ($606m vs $456m) due to risk migration and macro uncertainty (ev-4, ev-27).
> [ev-4] CBA/FY26/profit_announcement, PDF p118: "Net collective provision funding 606 456 388 218"
> [ev-27] CBA/FY26/results_presentation, printed p29: "Impairment expense higher reflecting portfolio growth and increased global macroeconomic uncertainty"

### individual_provisions — "Net new and increased individual provisioning"
*-17 $m | confidence 85/100*

Net individual provisions decreased $17 million ($422m vs $439m) as write-backs accelerated (ev-5, ev-6).
> [ev-5] CBA/FY26/profit_announcement, PDF p118: "Net new and increased individual provisioning 422 439 177 245"
> [ev-6] CBA/FY26/profit_announcement, PDF p118: "Write-back of individually assessed provisions (240) (169) (96) (144)"

## Source disagreements
- **Loss Rate Definition** (definitional): 8 bps (ev-22) vs 102 bps (ev-26)
  Preferred: 8 bps. The Profit Announcement (ev-22) defines the headline ratio as annualised LIE / average GLAA. The Presentation (ev-26) uses a different denominator or calculation method.

## Limitations
- No primary walk chart provided; drivers derived from table deltas.
- Residual of -$71m exists because divisional P&L changes do not sum to the group total delta.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T03:43:13+00:00
- seconds: 67.8
- cost_usd: 0.0017
- tokens: 32553 in / 5753 out
- orchestration: pipeline
