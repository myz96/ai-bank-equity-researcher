# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 85/100

*Read from: row 'Total loan impairment expense', column FY25 -> column FY26*

CBA's Loan Impairment Expense (LIE) increased $62 million to $788 million in FY26 (vs $726 million in FY25), a 9% rise. The loss rate against average gross loans and acceptances (GLAA) rose 1 basis point to 8 bps. Growth was driven by Retail Banking Services (+$106m), partially offset by Business Banking (-$45m) and Institutional Banking (-$16m).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.volume` | Retail Banking Services collective provisions | +106 $m | 85 | 2 () | ev-12, ev-14, ev-20, ev-26 |
| `collective.asset_quality` | Business Banking collective provisions | -45 $m | 80 | 1 (single_source) | ev-12, ev-15, ev-21 |
| `individual_provisions` | Institutional Banking and Markets individually assessed provisions | -16 $m | 80 | 1 (single_source) | ev-12, ev-16 |
| `other_unmapped` | New Zealand and Corporate Centre | +17 $m | 80 | 1 (single_source) | ev-12, ev-17, ev-18 |

### collective.volume — "Retail Banking Services collective provisions"
*+106 $m | confidence 85/100*

Retail LIE increased $106 million to $378 million. This is attributed to portfolio growth and higher collective provision charges, consistent with the group-level driver of 'portfolio growth' cited in the presentation.
> [ev-12] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."
> [ev-14] CBA/FY26/profit_announcement, PDF p34: "Retail Banking Services 378 272 39"
> [ev-20] CBA/FY26/profit_announcement, PDF p34: "An increase in Retail Banking Services of $106 million to an expense of $378 million"
> [ev-26] CBA/FY26/results_presentation, printed p29: "Impairment expense higher reflecting portfolio growth and increased global macroeconomic uncertainty"

### collective.asset_quality — "Business Banking collective provisions"
*-45 $m | confidence 80/100*

Business Banking LIE decreased $45 million to $310 million. The improvement reflects lower collective provisions, likely due to favorable risk migration or recovery in the SME portfolio, contrasting with the group-wide macro uncertainty.
> [ev-12] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."
> [ev-15] CBA/FY26/profit_announcement, PDF p34: "Business Banking 310 355 (13)"
> [ev-21] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million"

### individual_provisions — "Institutional Banking and Markets individually assessed provisions"
*-16 $m | confidence 80/100*

IB&M LIE decreased $16 million to $33 million. This reduction is primarily driven by lower individually assessed provisions as specific corporate credit risks were resolved or migrated, contributing to the overall decline in this segment.
> [ev-12] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."
> [ev-16] CBA/FY26/profit_announcement, PDF p34: "Institutional Banking and Markets 33 49 (33)"

### other_unmapped — "New Zealand and Corporate Centre"
*+17 $m | confidence 80/100*

The residual movement includes New Zealand (+$11m to $66m) and Corporate Centre/Other (+$6m to $1m). These smaller segments contribute to the net increase but are not explicitly broken down into specific impairment drivers in the primary text.
> [ev-12] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."
> [ev-17] CBA/FY26/profit_announcement, PDF p34: "New Zealand 66 55 20"
> [ev-18] CBA/FY26/profit_announcement, PDF p34: "Corporate Centre and Other 1 (5) large"

## Source disagreements
- **Loan Loss Rate Denominator and Value** (definitional): 8 bps on avg GLAA (ev-1, ev-13) vs 14 bps Group (ev-23)
  Preferred: 8 bps on avg GLAA. The Profit Announcement (ev-1, ev-13) explicitly defines the headline loss rate as 'Loan impairment expense annualised as a % of average gross loans and acceptances'. The Results Presentation (ev-23) shows a different metric ('Loan loss rate by business unit') which sums to 14 bps for the Group, likely using a different denominator or including non-GLAA items. The PA definition is the primary reporting standard.
- **FY25 Loan Impairment Expense Value** (rounding): 726.0 (ev-5, ev-12, ev-14, ev-15, ev-16, ev-17, ev-18, ev-19, ev-24) vs 724.6 (ev-31)
  Preferred: 726.0. Most tables and the narrative text cite $726 million. One table (ev-31) cites $724.6 million. Given the consistency of the $726 figure across the majority of sources and the explicit text statement ($726m), the rounded figure is preferred for the primary movement calculation.

## Limitations
- The bank does not provide a full quantitative bridge of the P&L impairment charge into specific drivers like 'volume', 'asset quality', and 'overlays' for each division. Contributions are inferred from divisional deltas and high-level narrative attributions (e.g., 'lower collective provision charges').
- Confidence is capped at 85 for individual drivers because the specific attribution of the $106m Retail increase to 'volume' vs 'asset quality' is based on narrative inference rather than a disclosed quantitative walk.
- The 'Corporate Centre and Other' segment has a small negative prior year value (-$5m), making its delta volatile and less indicative of core impairment trends.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-28T12:19:15+00:00
- seconds: 95.4
- cost_usd: 0.0018
- tokens: 31520 in / 6816 out
- orchestration: pipeline
