# Questions scorecard — combo agentic, 20260830-1347

## Run metadata

- run: 20260830-1347 (UTC)
- commit: 95447d6 (working tree dirty)
- gold sha256 (evals/gold/*.json, first 16): acfb8172d297fa3b
- judges: deepseek/deepseek-v4-pro-0813, qwen/qwen3.7-flash

Two populations, reported apart. **Location coverage** measures the retriever: did the answer cite the pages that carry the answer? **Fact accuracy** measures the answer: did the judges rule each gold fact both STATED by the answer and ENTAILED by its cited quotes? A case PASSES only when coverage is 100% and fact accuracy is at least 75%. Coverage alone is not correctness (ticket 29, finding 7).

| Case | Pass | Location coverage | Fact accuracy | Flagged | Missed locations | Conf | Cost |
|---|---|---|---|---|---|---|---|
| nab-business-growth-quality | FAIL | 3/3 | 0/4 | 2 | — | 83 | $0.7431 |

## Judged facts

### nab-business-growth-quality
- **fail** — The printed 'Business and housing lending GLAs and deposits' chart shows business lending of $155.0bn at Sep-24 and $166.3bn at Sep-25, labelled 6.7% growth; the same page prints 'Revenue' of $8,358m in FY24 and $8,531m in FY25, up 2.1%, and 'Cash earnings' of $3,277m and $3,330m, up 1.6% (NAB/FY25/investor-presentation, PDF page 49).
  - stated=partial; entailed=not-entailed
- **flagged_for_human** — The printed 'Net interest margin' bars are 3.11% in 1H24, 3.07% in 2H24, 3.01% in 1H25 and 3.02% in 2H25; 'Credit impairment charge and as a % of GLAs' prints $237m/0.18% in 1H25 and $292m/0.21% in 2H25 (NAB/FY25/investor-presentation, PDF page 49).
  - judges disagree — stated: judges answered ['partial', 'stated']
- **flagged_for_human** — The printed 'Diversified Australian business lending growth (YoY)' chart shows Agri 3.5%, Health 5.9%, CRE 7.4%, Other 10.4%, NAB B&PB 7.3% and NAB Small business 9.2%, alongside the statement 'Broad based growth across most sectors including Trade, Manufacturing, Construction, Transport' (NAB/FY25/investor-presentation, PDF page 50).
  - judges disagree — stated: judges answered ['partial', 'stated']; entailed: judges answered ['entailed', 'not-entailed']
- **fail** — The printed NPL chart rises from 2.66% at Sep-24 to 3.22% at Sep-25 and flags 'Includes 21bps relating to 2 large Agri customers'; the page also states, 'Excluding two large well secured Agri customers, underlying NPL ratio down 3bps to 3.01%' and 'Stable to improving NPL outcomes in 2H25 for most sectors' (NAB/FY25/investor-presentation, PDF page 27).
  - stated=stated; entailed=not-entailed

Judge cost: $0.0166 over 16 calls (on top of the per-case answer cost).
