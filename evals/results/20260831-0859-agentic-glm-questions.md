# Questions scorecard — combo agentic-glm, 20260831-0859

## Run metadata

- run: 20260831-0859 (UTC)
- commit: e81d8ed (working tree dirty)
- gold sha256 (evals/gold/*.json, first 16): acfb8172d297fa3b
- judges: deepseek/deepseek-v4-pro-0813, qwen/qwen3.7-flash

Two populations, reported apart. **Location coverage** measures the retriever: did the answer cite the pages that carry the answer? **Fully-grounded facts** measures citation discipline, not analysis quality: did the judges rule each gold fact both STATED by the answer and ENTAILED by its cited quotes, with EVERY load-bearing number present in those quotes? An answer whose analysis is right but whose quotes omit a number it used scores a fail here by design (measured 2026-08-31: frontier agents state nearly every gold fact and lose this column on quote completeness). A case PASSES only when coverage is 100%, NO fact failed, and the facts the judges could not settle stay inside 25% of the case. A flagged fact is neither a pass nor a fail; a failed fact is the answer getting it wrong, and no allowance covers that. Coverage alone is not correctness (ticket 29, finding 7).

| Case | Pass | Location coverage | Fully-grounded facts | Flagged | Missed locations | Conf | Cost |
|---|---|---|---|---|---|---|---|
| multi-bank nab-business-growth-quality | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | |
| wbc-fy26-productivity-versus-investment | FAIL | 3/3 | 2/5 | 3 | — | 80 | $0.0161 |
| fy25-cross-bank-earnings-conversion | FAIL | 3/3 | 2/3 | 0 | — | 90 | $0.0144 |
| cba-fy25-fy26-earnings-engine-rotation | FAIL | 2/3 | 1/4 | 0 | CBA/FY26/results-presentation p54 | 88 | $0.0782 |
| multi-bank wbc-low-impairment-versus-provision-caution | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | |

## Judged facts

### wbc-fy26-productivity-versus-investment
- **pass** — The printed 'FY25 expenses ($m)' bridge moves from $10,944m in FY24 to $11,916m in FY25, a 9% increase, with Staff costs +$397m, Technology +$146m, Volume and other +$199m, Productivity ($402m), Investments +$359m and Restructuring charge +$273m; it labels the increase 6% excluding restructuring (WBC/FY25/presentation-and-IDP, PDF page 27).
  - the answer states the fact and the cited quotes entail it
- **flagged_for_human** — Under 'Key considerations for FY26' the page prints 'EBA increase 3% to 4% and investment in bankers', 'Increase in UNITE spend' and 'Fit for Growth benefits to contribute to targeted productivity of >$500m in FY26' (WBC/FY25/presentation-and-IDP, PDF page 27).
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']
- **flagged_for_human** — The printed 'Investment spend' chart rises from $1,756m in FY24 to $1,918m in FY25, up 9%; the table shows 'Total expensed' rising from 56% to 60% and 'Amortisation expense ($m)' from $889m to $995m (WBC/FY25/presentation-and-IDP, PDF page 26).
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']
- **flagged_for_human** — The FY26 considerations print 'Investment spend ~$2bn' and 'Increase in UNITE spend to $850m - $950m, ~75% expensed' (WBC/FY25/presentation-and-IDP, PDF page 26).
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']
- **pass** — The UNITE page states 'Plan extends into FY29', 'Expect to invest $850 - $950 million in FY26', 'c.40% of total investment spend FY27 - FY28', 'Lower spend in FY29' and 'c.75% of spend to be expensed' (WBC/FY25/presentation-and-IDP, PDF page 14).
  - the answer states the fact and the cited quotes entail it

### fy25-cross-bank-earnings-conversion
- **fail** — CBA's printed cash-basis 'Group Performance Summary' shows total operating income of $28,465m versus $27,174m, up 5%; operating expenses of $12,996m versus $12,218m, up 6%; operating performance of $15,469m versus $14,956m, up 3%; loan impairment expense of $726m versus $802m, down 9%; and continuing-operations cash NPAT of $10,252m versus $9,836m, up 4% (CBA/FY25/profit-announcement, PDF page 16).
  - stated=stated; entailed=not-entailed
- **pass** — NAB's printed 'Financial results' charts show underlying profit of $10,965m versus $10,823m, up 1.3%; cash earnings of $7,091m versus $7,102m, down 0.2%; and statutory profit of $6,759m versus $6,960m, down 2.9% (NAB/FY25/investor-presentation, PDF page 5).
  - the answer states the fact and the cited quotes entail it
- **pass** — Westpac's printed 'FY25 financial performance' table shows net profit excluding Notable Items of $6,972m versus $7,113m, down 2%; revenue of $22.5bn versus $21.8bn, up 3%; expenses of $11.9bn versus $10.9bn, up 9%; expenses excluding restructuring of $11.6bn versus $10.9bn, up 6%; pre-provision profit of $10.5bn versus $10.8bn, down 3%; and impairment charges to average loans of 5bps versus 7bps (WBC/FY25/presentation-and-IDP, PDF page 20).
  - the answer states the fact and the cited quotes entail it

### cba-fy25-fy26-earnings-engine-rotation
- **pass** — The FY25 review states, 'Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $416 million or 4% on the prior year to $10,252 million. The result was driven by a 3% increase in operating performance with a 5% increase in operating income and a 6% increase in operating expenses, as well as a $76 million decrease in loan impairment expense' (CBA/FY25/profit-announcement, PDF page 26).
  - the answer states the fact and the cited quotes entail it
- **fail** — The FY25 review also states, 'Net Interest Income (NII) increased 5%, primarily driven by a 9 basis point increase in Net Interest Margin (NIM) and a $9 billion increase in Average Interest Earning Assets (AIEA).' It adds that excluding liquid assets and institutional pooled facilities, growth was driven by a 5% increase in AIEA and a 2 basis point increase in NIM (CBA/FY25/profit-announcement, PDF page 26).
  - stated=partial; entailed=not-entailed
- **fail** — The printed FY26 key outcomes show Cash NPAT of $10,982m, up 7.1%; operating income of $30,224m, up 6.2%; operating expenses of $13,755m, up 5.8%; cost to income of 45.5%, down 20bps; NIM of 2.05%, down 3bps; and LIE to GLAA of 8bps, up 1bp (CBA/FY26/results-presentation, PDF page 54).
  - stated=stated; entailed=not-entailed
- **fail** — The printed FY26 'Group margin - 12 months' bridge moves from 208bps in FY25 to 205bps in FY26 and is captioned 'Lower margin largely due to growth in liquids and repos - competition offset by hedge earnings'; the bridge prints Liquids & repos (4bps), Asset pricing (5bps), Funding costs nil, Portfolio mix +2bps, Interest rate risk hedging +5bps and Treasury & Markets (1bp) (CBA/FY26/results-presentation, PDF page 60).
  - stated=partial; entailed=not-entailed

Judge cost: $0.0478 over 48 calls (on top of the per-case answer cost).
