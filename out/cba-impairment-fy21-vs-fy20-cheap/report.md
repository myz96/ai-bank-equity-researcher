# CBA — impairment — FY21 vs FY20

**Movement (cash basis):** 2518$m → 554$m (-1964$m) | **Attribution confidence:** 40/100

*Read from: row 'Total loan impairment expense', column FY20 (12 months ended Jun 2020) -> column FY21 (12 months ended Jun 2021)*

CBA's cash loan impairment expense fell $1,964m (-78%) to $554m in FY21 vs FY20, driven by improved economic conditions and outlook. The loss rate dropped 26bps to 7bps on average GLAAs.

### collective.asset_quality — "Improvement in economic conditions and outlook"
*unquantified | confidence 85/100*

The bank attributes the decrease primarily to an improvement in economic conditions and outlook, which reduced collective provisions across Retail and Business Banking segments significantly.
> [ev-3] CBA/FY21/profit_announcement, PDF p12: "Loan impairment expense decreased as a result of an improvement in economic conditions and outlook. The loan loss rate reduced to 7 basis points, down from 33 basis points in FY20."
> [ev-7] CBA/FY21/profit_announcement, PDF p39: "Loan impairment expense was $554 million, a decrease of $1,964 million or 78% on the prior year."
> [ev-8] CBA/FY21/profit_announcement, PDF p39: "A decrease in Retail Banking Services of $900 million or 87% to $134 million"
> [ev-9] CBA/FY21/profit_announcement, PDF p39: "A decrease in Business Banking of $551 million or 70% to $233 million"

### overlays_fla — "Forward-looking adjustments and overlays"
*unquantified | confidence 80/100*

Overlays partially offset the improvement. Total impairment provisions decreased only $152m ($6,363m to $6,211m) despite the large drop in expense, indicating overlays remained elevated due to ongoing COVID-19 uncertainty.
> [ev-4] CBA/FY21/profit_announcement, PDF p12: "Our total impairment provisions decreased to $6,211m from $6,363m in FY20 reflecting the improved economic conditions and outlook, partly offset by additional overlays which reflect the ongoing economic uncertainty due to the continuing impact of COVID-19."
> [ev-15] CBA/FY21/profit_announcement, printed p26: "Total provisions for impairment losses as at 30 June 2021 were $6,211 million, a decrease of $152 million or 2% on the prior year."
> [ev-34] CBA/FY21/results_presentation, printed p32: "Overlays Jun 20 Dec 20 Jun 21 967 872 900"

### individual_provisions — "Individually assessed provisions"
*unquantified | confidence 75/100*


> [ev-18] CBA/FY21/profit_announcement, printed p26: "Consumer individually assessed provisions decreased by $51 million or 21% to $189 million."
> [ev-19] CBA/FY21/profit_announcement, printed p26: "Corporate individually assessed provisions decreased by $16 million or 2% to $711 million."

## Source disagreements
- **Provision Balance vs Expense Movement** (definitional): Expense: -1964m (Cash) vs Provisions Balance: -152m (Statutory)
  Preferred: Expense movement for driver analysis. The task asks for credit impairment CHARGE (P&L). Evidence ev-7 shows a $1,964m decrease in expense. Evidence ev-15 shows a $152m decrease in provision balances. These are different metrics; the balance change includes write-offs and recoveries not in the charge.

## Limitations
- No primary walk chart provided to quantify specific driver contributions (volume vs quality vs overlays) in dollars.
- Driver contributions are qualitative based on narrative text attributing the decrease to 'economic conditions' and 'outlook'.
- Cannot separate volume growth impact from asset quality migration quantitatively without a detailed bridge table.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-28T12:09:02+00:00
- seconds: 67.4
- cost_usd: 0.0024
- tokens: 43537 in / 8330 out
- orchestration: pipeline
