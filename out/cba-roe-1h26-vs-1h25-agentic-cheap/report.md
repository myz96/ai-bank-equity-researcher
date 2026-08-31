# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 75/100

*Read from: row 'ROE - "cash basis" (%) continuing operations', column 31 Dec 24 column -> column 31 Dec 25 column*

CBA's return on equity (cash basis) increased 10 basis points to 13.8% in 1H26 vs 13.7% in 1H25, a movement of +1.0 ppt. The increase was driven by higher cash NPAT of $5,445 million (+$313 million or 6% on 1H25's $5,132 million), which lifted ROE at constant equity. This was partly offset by higher average net assets of $78,004 million versus $74,176 million in 1H25, which diluted the ROE. The bank states: "Return on equity ("cash basis") increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets" (p.26).

> [ev-1] CBA/1H26/profit_announcement, PDF p168: "ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-2] CBA/1H26/profit_announcement, PDF p168: "Net profit after tax - "cash basis" 5,445 5,120 5,132"
> [ev-3] CBA/1H26/profit_announcement, PDF p168: "Net average equity 78,004 77,020 74,176"
> [ev-6] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax ("cash NPAT" or "cash profit") from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-7] CBA/1H26/profit_announcement, printed p2: "Return on equity ("cash basis") increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | higher cash NPAT | +0.836 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-6 |
| `equity_effect` | higher net assets | -0.736 ppt | 75 | 1 (single_source) | ev-3, ev-7, ev-8, ev-9, ev-10, ev-12 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect — "higher cash NPAT"
*+0.836 ppt | confidence 80/100*

Derived contribution: prior-period ROE of 13.7% multiplied by the earnings growth fraction of 6.1% ($313m/$5,132m). At constant equity, the 6% rise in cash NPAT from $5,132m to $5,445m would lift ROE by 83.6 ppt. The bank states cash NPAT increased $313 million or 6% on the prior comparative period (ev-6). This is a derived figure, not a disclosed decomposition.
> [ev-1] CBA/1H26/profit_announcement, PDF p168: "ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-2] CBA/1H26/profit_announcement, PDF p168: "Net profit after tax - "cash basis" 5,445 5,120 5,132"
> [ev-6] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax ("cash NPAT" or "cash profit") from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."

### equity_effect — "higher net assets"
*-0.736 ppt | confidence 75/100*

Derived contribution: total delta of 10 ppt minus earnings effect of 83.6 ppt equals -73.6 ppt. Average net assets rose from $74,176m to $78,004m (+$3,828m or +5.2%), diluting ROE. Equity growth came from retained earnings ($5,445m cash NPAT less $3,933m dividends = ~$1,512m retained half-on-half), partially offset by no buyback activity in 1H26 (ev-9) and DRP share issues at 14.8%-18.1% participation rates (ev-12). The bank states the increase was 'partly offset by higher net assets' (ev-7). This is a derived figure, not a disclosed decomposition.
> [ev-3] CBA/1H26/profit_announcement, PDF p168: "Net average equity 78,004 77,020 74,176"
> [ev-7] CBA/1H26/profit_announcement, printed p2: "Return on equity ("cash basis") increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-8] CBA/1H26/profit_announcement, printed p98: "Shareholders' equity attributable to equity holders of the Bank 77,232 78,776 75,264"
> [ev-9] CBA/1H26/profit_announcement, PDF p160: "No share buy-back activity was undertaken during 1H26 and 2H25."
> [ev-10] CBA/1H26/profit_announcement, PDF p160: "The Directors have determined a fully franked interim dividend of 235 cents per share amounting to $3,933 million."
> [ev-12] CBA/1H26/profit_announcement, PDF p160: "The DRP for the 2025 final, 2025 interim and 2024 final dividends were satisfied in full by the on-market purchase and transfer of shares, and had participation rates of 14.8%, 18.1% and 18.1% respectively."

## Limitations
- The earnings_effect and equity_effect are arithmetic derivations, not disclosed by the bank. CBA does not publish a formal ROE walk or bridge decomposition for the year-on-year comparison.
- No primary-period ROE walk chart was found in either document; the results presentation contains only peer-comparison charts without a driver breakdown.
- The equity effect narrative relies on end-of-period equity levels and dividend/buyback data rather than average equity movements, which introduces approximation error.
- Discontinued operations (CFS) are excluded from the continuing-operations ROE but appear in the including-discontinued-operations table (p.169); the two framings show slightly different statutory ROE values.
- Movement endpoints converted from basis points (1370, 1380) to ppt: the evidence prints this ratio as 13.7% and 13.8%, and the unit for this metric is ppt. A change column printed in basis points is divided by 100 to enter a movement stated in points.
- Identity contributions restated from +10.00 to +0.1000 ppt: the identity closes on the movement delta at the ratio's own scale and not at the scale they were written on, and a contribution larger than the ratio itself cannot be a movement of that ratio. A growth rate enters a ratio identity as a fraction, and a dollar movement enters it divided by the identity's denominator.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T23:53:23+00:00
- seconds: 88.5
- cost_usd: 0.0218
- tokens: 632278 in / 7786 out
- orchestration: agent
- tool_calls: 35
- pages_read: 13
- charts_read: 0
- budget_exhausted: no
