# Questions scorecard — combo agentic-ds, 20260831-0916

## Run metadata

- run: 20260831-0916 (UTC)
- commit: 67b74fb (working tree dirty)
- gold sha256 (evals/gold/*.json, first 16): acfb8172d297fa3b
- judges: deepseek/deepseek-v4-pro-0813, qwen/qwen3.7-flash

Two populations, reported apart. **Location coverage** measures the retriever: did the answer cite the pages that carry the answer? **Fully-grounded facts** measures citation discipline, not analysis quality: did the judges rule each gold fact both STATED by the answer and ENTAILED by its cited quotes, with EVERY load-bearing number present in those quotes? An answer whose analysis is right but whose quotes omit a number it used scores a fail here by design (measured 2026-08-31: frontier agents state nearly every gold fact and lose this column on quote completeness). A case PASSES only when coverage is 100%, NO fact failed, and the facts the judges could not settle stay inside 25% of the case. A flagged fact is neither a pass nor a fail; a failed fact is the answer getting it wrong, and no allowance covers that. Coverage alone is not correctness (ticket 29, finding 7).

| Case | Pass | Location coverage | Fully-grounded facts | Flagged | Missed locations | Conf | Cost |
|---|---|---|---|---|---|---|---|
| nab-business-growth-quality | FAIL | 0/3 | 0/4 | 0 | NAB/FY25/investor-presentation p49; NAB/FY25/investor-presentation p50; NAB/FY25/investor-presentation p27 | 82 | $0.0159 |

## Judged facts

### nab-business-growth-quality
- **fail** — The printed 'Business and housing lending GLAs and deposits' chart shows business lending of $155.0bn at Sep-24 and $166.3bn at Sep-25, labelled 6.7% growth; the same page prints 'Revenue' of $8,358m in FY24 and $8,531m in FY25, up 2.1%, and 'Cash earnings' of $3,277m and $3,330m, up 1.6% (NAB/FY25/investor-presentation, PDF page 49).
  - stated=partial; entailed=not-entailed
- **fail** — The printed 'Net interest margin' bars are 3.11% in 1H24, 3.07% in 2H24, 3.01% in 1H25 and 3.02% in 2H25; 'Credit impairment charge and as a % of GLAs' prints $237m/0.18% in 1H25 and $292m/0.21% in 2H25 (NAB/FY25/investor-presentation, PDF page 49).
  - stated=partial; entailed=not-entailed
- **fail** — The printed 'Diversified Australian business lending growth (YoY)' chart shows Agri 3.5%, Health 5.9%, CRE 7.4%, Other 10.4%, NAB B&PB 7.3% and NAB Small business 9.2%, alongside the statement 'Broad based growth across most sectors including Trade, Manufacturing, Construction, Transport' (NAB/FY25/investor-presentation, PDF page 50).
  - stated=partial; entailed=not-entailed
- **fail** — The printed NPL chart rises from 2.66% at Sep-24 to 3.22% at Sep-25 and flags 'Includes 21bps relating to 2 large Agri customers'; the page also states, 'Excluding two large well secured Agri customers, underlying NPL ratio down 3bps to 3.01%' and 'Stable to improving NPL outcomes in 2H25 for most sectors' (NAB/FY25/investor-presentation, PDF page 27).
  - stated=absent; entailed=not-entailed

Judge cost: $0.0118 over 16 calls (on top of the per-case answer cost).
