1. **High — [validate.py:840](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:840), [evals.py:531](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/evals.py:531): Driver and residual units are ignored during reconciliation and scoring.**  
   Failure scenario: a `-5 bps` contribution inside a `-$5m` movement is summed as `-5`, passes `drivers_reconcile`, and can score correct against a `-$5m` gold slot because only the value is compared; the agent strips this at [research_agent.py:1159](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:1159), but the pipeline does not.  
   Suggested fix: reject or unquantify every contribution/residual whose normalized unit differs from the movement unit, and have the scorer verify claim units independently.

2. **High — [evals.py:406](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/evals.py:406): Small opposite-sign money values can score as matching despite the stated “sign flip never matches” rule.**  
   Failure scenario: gold `+$5m` versus answer `-$5m` returns true because the $10m absolute tolerance suppresses the sign check and the absolute difference is exactly $10m.  
   Suggested fix: reject opposite non-zero signs before applying any absolute or relative tolerance.

3. **High — [schema.py:141](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/schema.py:141), [research_agent.py:1667](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:1667): The question evidence gate strips unsupported key facts but leaves unsupported numbers in the primary answer prose.**  
   Failure scenario: `answer="NIM was 9.9%"`, `key_facts=[]`, and no evidence produces a saved report that still states `9.9%`; only confidence is capped to 20.  
   Suggested fix: gate quantified sentences in `answer` itself, or deterministically render the answer solely from surviving key facts and supported narrative.

4. **High — [corpus.py:30](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/corpus.py:30), [retrieve.py:38](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/retrieve.py:38): Page-text and embedding caches are keyed only by filename stem, allowing documents to reuse another case’s cached contents.**  
   Failure scenario: `CBA/FY26/results.pdf` populates `results.json` and `results.npy`; subsequently reading `NAB/FY25/results.pdf` silently returns or ranks CBA’s pages, potentially with mismatched page counts.  
   Suggested fix: key caches by bank, period, document type, and SHA-256—or by a hash of the absolute path and content hash.

5. **High — [pipeline.py:318](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/pipeline.py:318), [pipeline.py:368](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/pipeline.py:368): Evidence fetched during the first author attempt is lost when output validation triggers the second attempt.**  
   Failure scenario: the author requests a new page, uses its records, but fails reconciliation; the retry receives the original outer `records`, while the fetched page is now in `candidates` and therefore cannot be fetched again.  
   Suggested fix: make `fetch_more` append to the shared evidence collection, or carry the first attribution’s expanded `evidence_records` into subsequent author attempts.

6. **High — [research_agent.py:1607](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:1607), [extract.py:360](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/extract.py:360): Question-mode chart reads default to `$m`, while extracted walk records always label bars as `bps`.**  
   Failure scenario: “What drove CBA’s FY26 NIM?” followed by `read_chart` without an explicit unit instructs vision to read the NIM chart in dollars, while the resulting evidence record labels the same values as basis points, yielding wrong scaling or contradictory evidence.  
   Suggested fix: require a unit in question-mode chart calls or infer it from the question/metric, and store the supplied unit rather than hard-coding `"bps"`.

7. **High — [validate.py:754](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:754): Driver reconciliation tolerance ignores the metric unit and becomes 10 for any submitted presentation walk.**  
   Failure scenario: a CTI movement of `+1ppt` with drivers totaling `+10ppt` passes because an otherwise unrelated cited presentation chart makes the allowed error 10; even without a presentation, the default 1ppt tolerance is ten times the scorer’s 0.1ppt tolerance.  
   Suggested fix: use unit-specific tolerances and grant presentation rounding slack only when the load-bearing, task-comparison walk supplies those contributions.

8. **High — [research_agent.py:1440](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:1440): Tool calls appearing after an accepted `submit` in the same assistant turn are still executed and can mutate the finalized result.**  
   Failure scenario: a response calls `submit` and then `read_chart`; the submission is accepted, but the later chart can add a walk failure that caps the already-submitted attribution at 40, while also incurring post-completion cost.  
   Suggested fix: make submission turns atomic—either reject mixed submit/research batches or stop dispatching non-submit calls once a submission is accepted.

9. **Medium — [ask.py:153](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/ask.py:153), [ask.py:169](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/ask.py:169): Open-loop question retrieval can spend its entire page budget on one period and silently omit the comparison period.**  
   Failure scenario: two documents for the first manifest-ordered period each contribute six pages, filling `MAX_ASK_PAGES=12` before any page from the other period is considered; a FY26-versus-FY25 question is then authored from only one side. The “primary” period also follows manifest order, not the caller’s requested period order.  
   Suggested fix: preserve requested period order and allocate minimum/per-period page quotas before ranking the remaining slots globally.

10. **Medium — [research_agent.py:1385](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/research_agent.py:1385), [llm.py:227](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/llm.py:227): Tool, cost, and wall-clock budgets are checked only between turns, not before each dispatched call or retry.**  
    Failure scenario: at 79/80 calls, one model turn can issue several `read_chart` calls and all execute; one chart’s nested JSON and HTTP retries can also run beyond the remaining wall-clock budget before control returns to the loop.  
    Suggested fix: check remaining tool/cost/time budget before every call in a batch and pass an absolute remaining deadline into all LLM retries and retry sleeps.

11. **Medium — [evals.py:230](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/evals.py:230): The 75% question pass threshold treats a definitively failed fact the same as the intended one flagged fact.**  
    Failure scenario: with four gold facts, three passes and one unanimous `FAIL` produce accuracy `0.75`; full location coverage therefore marks the entire case `PASS`, despite the comment saying the allowance is for a flagged or judge-split item.  
    Suggested fix: pass only when `failed == 0`, coverage is complete, and the permitted number of facts are specifically `flagged`.

12. **Medium — [validate.py:223](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/validate.py:223), [author.py:424](/Users/michaelzhao/swe/ai-bank-equity-researcher/src/bank_equity_researcher/author.py:424): The universal 0.51 movement-arithmetic tolerance silently accepts materially wrong ratio deltas.**  
    Failure scenario: a CTI movement `45.0ppt → 46.0ppt` reported with delta `+1.5ppt` differs by `0.5ppt`, but neither the author normalizer nor `check_movement` corrects or fails it; the scorer’s 0.1ppt tolerance then scores the movement wrong.  
    Suggested fix: use the shared unit-typed tolerance—0.1ppt for ratios, 0.5bps for bps, and the appropriate money rule—for both normalization and validation.
tokens used
217,424
