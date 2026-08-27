# CBA — impairment — FY21 vs FY20

**Movement (cash basis):** 2518$m → 554$m (-1964$m) | **Attribution confidence:** 40/100

CBA's loan impairment expense (LIE) decreased $1,964 million to $554 million in FY21 (cash basis), a 78% reduction from FY20 ($2,518 million). The loss rate fell 26 basis points to 7 bps on average gross loans and acceptances. This improvement was driven by significant provision write-backs as economic conditions and outlook improved, partially offset by forward-looking overlays added for ongoing COVID-19 uncertainty.

### collective.asset_quality — "Improvement in economic conditions and outlook"
*unquantified | confidence 75/100*

The primary driver of the LIE decrease is the reversal of provisions previously held due to pandemic-related risks. As economic conditions improved, collective provisions were released across Retail and Business Banking segments.
> [ev-4] CBA/FY21/profit_announcement, PDF p12: "Loan impairment expense decreased as a result of an improvement in economic conditions and outlook. The loan loss rate reduced to 7 basis points, down from 33 basis points in FY20."
> [ev-5] CBA/FY21/profit_announcement, PDF p12: "Our total impairment provisions decreased to $6,211m from $6,363m in FY20 reflecting the improved economic conditions and outlook, partly offset by additional overlays which reflect the ongoing economic uncertainty due to the continuing impact of COVID-19."
> [ev-13] CBA/FY21/profit_announcement, PDF p39: "A decrease in Retail Banking Services of $900 million or 87% to $134 million"
> [ev-14] CBA/FY21/profit_announcement, PDF p39: "A decrease in Business Banking of $551 million or 70% to $233 million"

### overlays_fla — "Additional overlays"
*unquantified | confidence 75/100*

Overlays increased or remained elevated to reflect ongoing economic uncertainty due to the continuing impact of COVID-19. This acted as a partial offset to the release of prior period provisions.
> [ev-5] CBA/FY21/profit_announcement, PDF p12: "Our total impairment provisions decreased to $6,211m from $6,363m in FY20 reflecting the improved economic conditions and outlook, partly offset by additional overlays which reflect the ongoing economic uncertainty due to the continuing impact of COVID-19."
> [ev-46] CBA/FY21/results_presentation, printed p32: "Overlays Jun 20 Dec 20 Jun 21 967 872 900"

### individual_provisions — "Individually assessed provisions"
*unquantified | confidence 75/100*

Individual provisions decreased significantly year-on-year, reflecting lower specific credit losses and recoveries compared to the heightened risk environment in FY20.
> [ev-27] CBA/FY21/profit_announcement, printed p26: "Consumer individually assessed provisions decreased by $51 million or 21% to $189 million."
> [ev-28] CBA/FY21/profit_announcement, printed p26: "Corporate individually assessed provisions decreased by $16 million or 2% to $711 million."

## Source disagreements
- **Statutory vs Cash Basis Impairment** (definitional): Statutory Loan Impairment Expense: $554m (FY21) / $2,518m (FY20) vs Cash Loan Impairment Expense: $554m (FY21) / $2,518m (FY20)
  Preferred: Cash. While the statutory and cash loan impairment expense figures are identical in this instance, the bank explicitly reports 'Loan impairment expense' on a cash basis in the segment results (ev-12, ev-13, ev-14). The statutory table (ev-3) also shows $554m/$2,518m. However, total impairment provisions differ between statutory and cash contexts if notable items are excluded. For the P&L charge line specifically, they align here.

## Limitations
- A precise quantitative bridge (walk) decomposing the -$1,964m movement into specific dollar amounts for each driver (volume, asset quality, overlays) is not provided in the evidence records. The attribution relies on narrative statements linking the decrease to 'improvement in economic conditions' and 'overlays'.
- Segment-level deltas are quantified (Retail -$900m, Business -$551m, NZ -$297m, IBM -$257m, Corp +$41m), but these sum to the total delta only if we assume no other minor segments exist or rounding differences are negligible. The sum of reported deltas (-900 - 551 - 297 - 257 + 41 = -1964) matches the total delta exactly.
- The specific dollar contribution of 'overlays' versus 'economic improvement' within the collective provision bucket is not explicitly separated in a numerical walk.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-27T07:50:04+00:00
- seconds: 97.3
- cost_usd: 0.0029
- tokens: 46056 in / 12038 out
- orchestration: pipeline
