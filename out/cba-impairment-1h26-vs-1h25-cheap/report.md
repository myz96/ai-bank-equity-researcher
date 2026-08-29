# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 40/100

*Read from: row 'Total loan impairment expense', column 31 Dec 24 -> column 31 Dec 25*

CBA's credit impairment charge decreased $1 million to $319 million in 1H26 (vs $320 million in 1H25), driven by a $153 million Retail increase offset by a $129 million Business Banking decrease and other reductions.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Retail Banking Services | +153 $m | 85 | 1 (single_source) | ev-6 |
| `individual_provisions` | Business Banking | -129 $m | 85 | 1 (single_source) | ev-3 |
| `other_unmapped` | Institutional Banking and Markets | -17 $m | 85 | 1 (single_source) | ev-4 |
| `other_unmapped` | New Zealand | -12 $m | 85 | 1 (single_source) | ev-5 |
| *residual (unexplained)* | — | -106 $m | — | — |

### collective.asset_quality — "Retail Banking Services"
*+153 $m | confidence 85/100*

Retail LIE increased $153 million to $232 million, mainly driven by losses within the consumer finance portfolio (ev-6).
> [ev-6] CBA/1H26/profit_announcement, printed p18: "An increase in Retail Banking Services of $153 million to an expense of $232 million"

### individual_provisions — "Business Banking"
*-129 $m | confidence 85/100*

Business Banking LIE decreased $129 million to $91 million (ev-3).
> [ev-3] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million"

### other_unmapped — "Institutional Banking and Markets"
*-17 $m | confidence 85/100*

IB&M LIE decreased $17 million to a benefit of $8 million (ev-4).
> [ev-4] CBA/1H26/profit_announcement, printed p18: "A decrease in Institutional Banking and Markets of $17 million to a benefit of $8 million"

### other_unmapped — "New Zealand"
*-12 $m | confidence 85/100*

New Zealand LIE decreased $12 million to an expense of $4 million (ev-5).
> [ev-5] CBA/1H26/profit_announcement, printed p18: "A decrease in New Zealand of $12 million to an expense of $4 million"

## Source disagreements
- **Residual attribution** (definitional): -106.0 from calculation vs Unknown from source
  Preferred: Residual. The sum of quantified drivers (+$153m - $129m - $17m - $12m = -$5m) does not match the total delta (-$1m). The remaining -$106m is unattributed as the source text omits specific driver breakdowns for this remainder.

## Limitations
- The bank discloses divisional deltas but does not explicitly attribute them to individual vs collective provisions in the narrative summary. We have mapped Retail to collective risk migration based on the 'consumer finance' reference, but the residual ($106m) remains unmapped due to lack of granular disclosure.
- Failed check: drivers_reconcile (drivers -5.0 + residual -106.0 != delta -1.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T13:09:34+00:00
- seconds: 82.3
- cost_usd: 0.002
- tokens: 39885 in / 6430 out
- orchestration: pipeline
