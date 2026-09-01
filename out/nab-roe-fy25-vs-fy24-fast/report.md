# NAB — roe — FY25 vs FY24

**Movement (cash basis):** 11.6ppt → 11.4ppt (-0.2ppt) | **Attribution confidence:** 80/100

*Read from: row 'Cash return on equity', column Year to Sep 24 column -> column Year to Sep 25 column*

NAB's Cash ROE fell 20 bps to 11.4% in FY25 from 11.6% in FY24 (results book p71, p10; investor presentation p6). Cash earnings were broadly flat, down 0.2% to $7,091m from $7,102m (results book p9; presentation p5), while total average equity attributable to owners rose 2.16% to $62,355m from $61,039m (results book p71). The 0.2 ppt decline splits into a small negative earnings effect (cash earnings fell slightly at constant equity) and a larger negative equity effect (average equity grew at roughly constant earnings). Statutory ROE fell 60 bps to 10.8% from 11.4% on the same comparison (results book p71), a wider decline reflecting the statutory basis.

> [ev-1] NAB/FY25/results_book, PDF p71: "Cash return on equity Earnings ($m) Cash earnings 7,091 7,102 3,508 3,583 Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314 Cash return on equity 11.4% 11.6% 11.0% 11.7%"
> [ev-3] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"
> [ev-4] NAB/FY25/investor_presentation, printed p6: "10.7% 11.7% 12.9% 11.6% 11.4% FY21 FY22 FY23 FY24 FY25"
> [ev-6] NAB/FY25/results_book, PDF p9: "Cash earnings 7,091 7,102 (0.2) 3,508 3,583 (2.1)"
> [ev-5] NAB/FY25/investor_presentation, printed p5: "7,102 7,091 FY24 FY25 10,823 10,965 FY24 FY25 Cash earnings1 ($m) Underlying profit ($m)"
> [ev-2] NAB/FY25/results_book, PDF p71: "Statutory return on equity 10.8% 11.4% 10.5% 11.1%"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Movement in cash earnings at constant equity | -0.018 ppt | 80 | 2 () | ev-6, ev-5, ev-11, ev-1 |
| `equity_effect` | Movement in average equity at constant earnings | -0.182 ppt | 75 | 1 (single_source) | ev-1, ev-9, ev-7, ev-10 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect — "Movement in cash earnings at constant equity"
*-0.018 ppt | confidence 80/100*

Derived, not disclosed: cash earnings fell 0.2% to $7,091m from $7,102m (ev-6, ev-5); at constant equity this lowers ROE by ~0.018 ppt. The decline reflects a higher credit impairment charge of $833m vs $728m (+14.4%) offsetting a 1.3% rise in underlying profit (ev-11, ev-6).
> [ev-6] NAB/FY25/results_book, PDF p9: "Cash earnings 7,091 7,102 (0.2) 3,508 3,583 (2.1)"
> [ev-5] NAB/FY25/investor_presentation, printed p5: "7,102 7,091 FY24 FY25 10,823 10,965 FY24 FY25 Cash earnings1 ($m) Underlying profit ($m)"
> [ev-11] NAB/FY25/results_book, PDF p5: "Credit impairment charge was $833 million, versus a FY24 charge of $728 million. The FY25 charge includes individually assessed charges of $964 million and a $131 million release from collective provisions."
> [ev-1] NAB/FY25/results_book, PDF p71: "Cash return on equity Earnings ($m) Cash earnings 7,091 7,102 3,508 3,583 Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314 Cash return on equity 11.4% 11.6% 11.0% 11.7%"

### equity_effect — "Movement in average equity at constant earnings"
*-0.182 ppt | confidence 75/100*

Derived as residual: total average equity rose 2.16% to $62,355m from $61,039m (ev-1), reducing ROE at roughly constant earnings. Equity growth reflects retained profits rising to $26,820m from $25,236m, outweighing a buyback-driven fall in contributed equity to $36,123m from $36,581m (ev-9, ev-7); DRP is satisfied by on-market purchase, issuing no new shares (ev-10).
> [ev-1] NAB/FY25/results_book, PDF p71: "Cash return on equity Earnings ($m) Cash earnings 7,091 7,102 3,508 3,583 Total average equity (attributable to owners of the Company) ($m) 62,355 61,039 63,375 61,314 Cash return on equity 11.4% 11.6% 11.0% 11.7%"
> [ev-9] NAB/FY25/results_book, printed p58: "Equity Contributed equity 36,123 36,119 36,581 Reserves (21) (56) (362) Retained profits 26,820 26,106 25,236 Total equity (attributable to owners of the Company) 62,922 62,169 61,455"
> [ev-7] NAB/FY25/results_book, PDF p29: "On 12 March 2025, the Group completed the on-market buyback that was announced on 15 August 2023 and subsequently increased on 2 May 2024 to $3 billion. Through this buy-back, the Group has bought back and cancelled 87,824,707 ordinary shares, including 16,572,039 ordinary shares ($0.6 billion or 0.15% of CET1 capital) in the September 2025 full year."
> [ev-10] NAB/FY25/results_book, PDF p31: "The Group periodically adjusts its DRP to reflect its capital position and outlook. There is no DRP discount for the 2025 final dividend. Eligible shareholders have the ability to participate in the DRP for the 2025 final dividend for up to 5 million NAB ordinary shares per participant. The Group expects to satisfy the DRP in full by an on-market purchase of ordinary shares."

## Source disagreements
- **ROE basis** (definitional): Cash ROE -0.2 ppt (11.4 vs 11.6) vs Statutory ROE -0.6 ppt (10.8 vs 11.4)
  Preferred: Cash ROE -0.2 ppt. The task's headline row is Cash ROE; statutory ROE is a different basis and shows a wider 60 bps decline.

## Limitations
- The earnings_effect and equity_effect are arithmetic derivations from the ROE endpoints and the cash earnings growth rate, not figures NAB discloses; the bank does not publish a ROE bridge for this comparison.
- The equity_effect is computed as the residual (total delta minus earnings_effect) and therefore also absorbs the interaction term between earnings and equity growth.
- The earnings growth rate (-0.2%) is read from the results book and investor presentation; the split is only as precise as that rate.

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-09-01T05:54:08+00:00
- seconds: 119.2
- cost_usd: 0.0099
- tokens: 314122 in / 8646 out
- orchestration: agent
- tool_calls: 32
- pages_read: 11
- charts_read: 0
- budget_exhausted: no
