# CBA — cash_earnings — FY26 vs FY25

**Movement (cash basis):** 10252$m → 10982$m (+730$m) | **Attribution confidence:** 40/100

CBA's cash earnings (NPAT) increased $730 million (+7.1%) to $10,982 million in FY26. The growth was primarily driven by a $1,563 million increase in Net Interest Income (NII), supported by strong volume growth ($92 billion IEA increase). This was partially offset by higher operating expenses ($719 million underlying increase) and higher credit impairment charges ($62 million increase). Other operating income contributed positively with a $196 million increase.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `nii` | Net interest income | +1563 $m | 85 | 1 (single_source) | ev-27, ev-28 |
| `other_operating_income` | Other operating income | +196 $m | 85 | 1 (single_source) | ev-1, ev-2, ev-3, ev-4, ev-5, ev-6 |
| `operating_expenses` | Underlying operating expenses | -719 $m | 85 | 1 (single_source) | ev-7, ev-8, ev-9, ev-10, ev-11 |
| `credit_impairment_charge` | Loan impairment expense | -62 $m | 85 | 1 (single_source) | ev-13, ev-14, ev-15, ev-16, ev-17 |
| *residual (unexplained)* | — | -148 $m | — | — |

### nii — "Net interest income"
*+1563 $m | confidence 85/100*

NII increased $1,563 million (7%) to $25,586 million. Driven by an $92 billion (8%) increase in average interest earning assets, partly offset by a 3 bps decrease in NIM to 2.05%.
> [ev-27] CBA/FY26/profit_announcement, PDF p28: "Net interest income was $25,586 million, an increase of $1,563 million or 7% on the prior year."
> [ev-28] CBA/FY26/profit_announcement, PDF p28: "The result was driven by a $92 billion or 8% increase in average interest earning assets to $1,246 billion, partly offset by a 3 basis point decrease in net interest margin to 2.05%."

### other_operating_income — "Other operating income"
*+196 $m | confidence 85/100*

Other operating income increased $196 million (4%) to $4,638 million. Commissions rose $135 million; lending fees up $12 million; trading down $9 million; funds management up $12 million; other income up $46 million.
> [ev-1] CBA/FY26/profit_announcement, PDF p30: "Other operating income was $4,638 million, an increase of $196 million or 4% on the prior year."
> [ev-2] CBA/FY26/profit_announcement, PDF p30: "Commissions increased by $135 million or 6% to $2,234 million"
> [ev-3] CBA/FY26/profit_announcement, PDF p30: "Lending fees increased by $12 million or 1% to $924 million"
> [ev-4] CBA/FY26/profit_announcement, PDF p30: "Trading income decreased by $9 million or 1% to $1,190 million"
> [ev-5] CBA/FY26/profit_announcement, PDF p30: "Funds management income increased by $12 million or 10% to $134 million"
> [ev-6] CBA/FY26/profit_announcement, PDF p30: "Other income increased by $46 million or 42% to $156 million"

### operating_expenses — "Underlying operating expenses"
*-719 $m | confidence 85/100*

Underlying operating expenses increased $719 million (6%) to $13,585 million. Staff costs rose $288 million; IT services up $393 million; occupancy down $19 million; other expenses up $57 million.
> [ev-7] CBA/FY26/profit_announcement, PDF p31: "Underlying operating expenses were $13,585 million, an increase of $719 million or 6% on the prior year."
> [ev-8] CBA/FY26/profit_announcement, PDF p31: "Staff expenses increased by $288 million or 4% to $8,258 million"
> [ev-9] CBA/FY26/profit_announcement, PDF p31: "Occupancy and equipment expenses decreased by $19 million or 2% to $938 million"
> [ev-10] CBA/FY26/profit_announcement, PDF p31: "Information technology services expenses increased by $393 million or 16% to $2,782 million"
> [ev-11] CBA/FY26/profit_announcement, PDF p31: "Other expenses increased by $57 million or 4% to $1,607 million"

### credit_impairment_charge — "Loan impairment expense"
*-62 $m | confidence 85/100*

Loan impairment expense increased $62 million (9%) to $788 million. Increases in Retail Banking Services ($106m) and New Zealand ($11m) were partially offset by decreases in Business Banking ($45m) and IB&M ($16m).
> [ev-13] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."
> [ev-14] CBA/FY26/profit_announcement, PDF p34: "An increase in Retail Banking Services of $106 million to an expense of $378 million"
> [ev-15] CBA/FY26/profit_announcement, PDF p34: "An increase in New Zealand of $11 million to an expense of $66 million"
> [ev-16] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million"
> [ev-17] CBA/FY26/profit_announcement, PDF p34: "A decrease in Institutional Banking and Markets of $16 million to an expense of $33 million"

## Source disagreements
- **Residual / Tax** (definitional): Calculated Residual: -$148.0m vs Tax Movement: ~$100-$150m (implied)
  Preferred: Residual. The sum of quantified drivers (NII + OOI + OpEx + Impairment) is $730 million, which exactly matches the Cash NPAT delta. However, this implies that the tax impact and any other minor items net to zero or are included in the 'residual' bucket if we strictly follow the P&L waterfall. In reality, NPAT = Pre-tax Profit * (1-t). The pre-tax profit movement is $730m. If tax rate is ~30%, tax impact is ~$220m. The fact that the driver sum equals the NPAT delta suggests either the 'drivers' listed are post-tax or there is a significant unquantified tax benefit or the residual captures the tax effect. Given the instruction to claim tax_and_other as a quantified component from tax expense movement, and no explicit tax dollar movement is provided in the evidence records (only statutory/cash reconciliation non-cash items), I must report the residual. The exact match of pre-tax drivers to NPAT delta is unusual and likely indicates the 'drivers' represent the full P&L impact including tax effects implicitly or the residual captures the tax variance. Without explicit tax dollar figures, I cannot split it.

## Limitations
- No explicit tax expense dollar movement is provided in the evidence records to isolate 'tax_and_other'.
- The sum of the primary P&L drivers (NII, OOI, OpEx, Impairment) equals the total Cash NPAT delta ($730m), implying a residual of $0 for these specific line items relative to the bottom line, but this ignores the tax effect on the pre-tax profit change. A residual of -$148m was calculated based on the assumption that the provided drivers are pre-tax and the final NPAT includes tax, but without explicit tax data, this is an estimate.
- Notable/Restructuring items are excluded from underlying expenses but their delta is not explicitly quantified as a separate bridge driver in the text, though ev-44 shows FY26 level of $170m ex_notables. The FY25 level is not explicitly given in the same format to calculate the delta directly.
- Failed check: drivers_reconcile (drivers +978.0 + residual -148.0 != delta +730.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-27T07:56:25+00:00
- seconds: 136.5
- cost_usd: 0.0031
- tokens: 45157 in / 13117 out
- orchestration: pipeline
