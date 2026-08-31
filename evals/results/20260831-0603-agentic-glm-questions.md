# Questions scorecard — combo agentic-glm, 20260831-0603

## Run metadata

- run: 20260831-0603 (UTC)
- commit: 4fd0379 (working tree dirty)
- gold sha256 (evals/gold/*.json, first 16): acfb8172d297fa3b
- judges: deepseek/deepseek-v4-pro-0813, qwen/qwen3.7-flash

Two populations, reported apart. **Location coverage** measures the retriever: did the answer cite the pages that carry the answer? **Fully-grounded facts** measures citation discipline, not analysis quality: did the judges rule each gold fact both STATED by the answer and ENTAILED by its cited quotes, with EVERY load-bearing number present in those quotes? An answer whose analysis is right but whose quotes omit a number it used scores a fail here by design (measured 2026-08-31: frontier agents state nearly every gold fact and lose this column on quote completeness). A case PASSES only when coverage is 100%, NO fact failed, and the facts the judges could not settle stay inside 25% of the case. A flagged fact is neither a pass nor a fail; a failed fact is the answer getting it wrong, and no allowance covers that. Coverage alone is not correctness (ticket 29, finding 7).

| Case | Pass | Location coverage | Fully-grounded facts | Flagged | Missed locations | Conf | Cost |
|---|---|---|---|---|---|---|---|
| nab-business-growth-quality | FAIL | 3/3 | 1/4 | 2 | — | 88 | $0.0293 |
| wbc-fy26-productivity-versus-investment | FAIL | 3/3 | 1/5 | 3 | — | 78 | $0.0501 |
| fy25-cross-bank-earnings-conversion | FAIL | 1/3 | 0/3 | 1 | NAB/FY25/investor-presentation p5; WBC/FY25/presentation-and-IDP p20 | 85 | $0.0322 |
| multi-bank cba-fy25-fy26-earnings-engine-rotation | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | |
| wbc-low-impairment-versus-provision-caution | FAIL | 0/3 | 0/4 | 0 | WBC/FY25/presentation-and-IDP p20; WBC/FY25/presentation-and-IDP p29; WBC/FY25/presentation-and-IDP p54 | 20 | $0.0352 |

## Judged facts

### nab-business-growth-quality
- **flagged_for_human** — The printed 'Business and housing lending GLAs and deposits' chart shows business lending of $155.0bn at Sep-24 and $166.3bn at Sep-25, labelled 6.7% growth; the same page prints 'Revenue' of $8,358m in FY24 and $8,531m in FY25, up 2.1%, and 'Cash earnings' of $3,277m and $3,330m, up 1.6% (NAB/FY25/investor-presentation, PDF page 49).
  - judges disagree — stated: judges answered ['partial', 'stated']
- **fail** — The printed 'Net interest margin' bars are 3.11% in 1H24, 3.07% in 2H24, 3.01% in 1H25 and 3.02% in 2H25; 'Credit impairment charge and as a % of GLAs' prints $237m/0.18% in 1H25 and $292m/0.21% in 2H25 (NAB/FY25/investor-presentation, PDF page 49).
  - stated=partial; entailed=not-entailed
- **pass** — The printed 'Diversified Australian business lending growth (YoY)' chart shows Agri 3.5%, Health 5.9%, CRE 7.4%, Other 10.4%, NAB B&PB 7.3% and NAB Small business 9.2%, alongside the statement 'Broad based growth across most sectors including Trade, Manufacturing, Construction, Transport' (NAB/FY25/investor-presentation, PDF page 50).
  - the answer states the fact and the cited quotes entail it
- **flagged_for_human** — The printed NPL chart rises from 2.66% at Sep-24 to 3.22% at Sep-25 and flags 'Includes 21bps relating to 2 large Agri customers'; the page also states, 'Excluding two large well secured Agri customers, underlying NPL ratio down 3bps to 3.01%' and 'Stable to improving NPL outcomes in 2H25 for most sectors' (NAB/FY25/investor-presentation, PDF page 27).
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']

### wbc-fy26-productivity-versus-investment
- **flagged_for_human** — The printed 'FY25 expenses ($m)' bridge moves from $10,944m in FY24 to $11,916m in FY25, a 9% increase, with Staff costs +$397m, Technology +$146m, Volume and other +$199m, Productivity ($402m), Investments +$359m and Restructuring charge +$273m; it labels the increase 6% excluding restructuring (WBC/FY25/presentation-and-IDP, PDF page 27).
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']
- **flagged_for_human** — Under 'Key considerations for FY26' the page prints 'EBA increase 3% to 4% and investment in bankers', 'Increase in UNITE spend' and 'Fit for Growth benefits to contribute to targeted productivity of >$500m in FY26' (WBC/FY25/presentation-and-IDP, PDF page 27).
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']
- **fail** — The printed 'Investment spend' chart rises from $1,756m in FY24 to $1,918m in FY25, up 9%; the table shows 'Total expensed' rising from 56% to 60% and 'Amortisation expense ($m)' from $889m to $995m (WBC/FY25/presentation-and-IDP, PDF page 26).
  - stated=stated; entailed=not-entailed
- **pass** — The FY26 considerations print 'Investment spend ~$2bn' and 'Increase in UNITE spend to $850m - $950m, ~75% expensed' (WBC/FY25/presentation-and-IDP, PDF page 26).
  - the answer states the fact and the cited quotes entail it
- **flagged_for_human** — The UNITE page states 'Plan extends into FY29', 'Expect to invest $850 - $950 million in FY26', 'c.40% of total investment spend FY27 - FY28', 'Lower spend in FY29' and 'c.75% of spend to be expensed' (WBC/FY25/presentation-and-IDP, PDF page 14).
  - judges disagree — entailed: judges answered ['entailed', 'not-entailed']

### fy25-cross-bank-earnings-conversion
- **flagged_for_human** — CBA's printed cash-basis 'Group Performance Summary' shows total operating income of $28,465m versus $27,174m, up 5%; operating expenses of $12,996m versus $12,218m, up 6%; operating performance of $15,469m versus $14,956m, up 3%; loan impairment expense of $726m versus $802m, down 9%; and continuing-operations cash NPAT of $10,252m versus $9,836m, up 4% (CBA/FY25/profit-announcement, PDF page 16).
  - judges disagree — stated: judges answered ['partial', 'stated']
- **fail** — NAB's printed 'Financial results' charts show underlying profit of $10,965m versus $10,823m, up 1.3%; cash earnings of $7,091m versus $7,102m, down 0.2%; and statutory profit of $6,759m versus $6,960m, down 2.9% (NAB/FY25/investor-presentation, PDF page 5).
  - stated=stated; entailed=not-entailed
- **fail** — Westpac's printed 'FY25 financial performance' table shows net profit excluding Notable Items of $6,972m versus $7,113m, down 2%; revenue of $22.5bn versus $21.8bn, up 3%; expenses of $11.9bn versus $10.9bn, up 9%; expenses excluding restructuring of $11.6bn versus $10.9bn, up 6%; pre-provision profit of $10.5bn versus $10.8bn, down 3%; and impairment charges to average loans of 5bps versus 7bps (WBC/FY25/presentation-and-IDP, PDF page 20).
  - stated=stated; entailed=not-entailed

### wbc-low-impairment-versus-provision-caution
- **fail** — The printed FY25 financial-performance table shows 'Impairment charges to average loans annualised' of 5bps in FY25 versus 7bps in FY24 (WBC/FY25/presentation-and-IDP, PDF page 20).
  - stated=stated; entailed=not-entailed (no quote was cited to entail it)
- **fail** — The impairment-provisions page states 'Impairment charges remain low, 4bps of average loans', 'CAP to credit RWA of 1.25%, down 1bps', 'Overlays increased $108m', '2.5ppt increase in downside scenario weight' and 'IAP decreased $72m due to a single name write-off' (WBC/FY25/presentation-and-IDP, PDF page 29).
  - stated=partial; entailed=not-entailed (no quote was cited to entail it)
- **fail** — The printed provision stack totals $5,096m at Sep-24, $5,072m at Mar-25 and $4,987m at Sep-25; the Sep-25 components are Overlays $238m, Stage 1 CAP $933m, Stage 2 CAP $2,087m, Stage 3 CAP $1,190m and Stage 3 IAP $539m (WBC/FY25/presentation-and-IDP, PDF page 54).
  - stated=partial; entailed=not-entailed (no quote was cited to entail it)
- **fail** — The printed 'Expected credit loss (ECL) ($m)' chart shows reported probability-weighted ECL of $4,987m, 100% base case ECL of $3,040m and 100% downside ECL of $7,152m, with the statement '$1.9bn in provisions above the base case ECL' (WBC/FY25/presentation-and-IDP, PDF page 54).
  - stated=stated; entailed=not-entailed (no quote was cited to entail it)

Judge cost: $0.0532 over 57 calls (on top of the per-case answer cost).
