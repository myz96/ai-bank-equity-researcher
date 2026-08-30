# Questions scorecard — combo cheap, 20260830-2032

## Run metadata

- run: 20260830-2032 (UTC)
- commit: 5b4e890 (working tree dirty)
- gold sha256 (evals/gold/*.json, first 16): acfb8172d297fa3b
- judges: deepseek/deepseek-v4-pro-0813, qwen/qwen3.7-flash

Two populations, reported apart. **Location coverage** measures the retriever: did the answer cite the pages that carry the answer? **Fact accuracy** measures the answer: did the judges rule each gold fact both STATED by the answer and ENTAILED by its cited quotes? A case PASSES only when coverage is 100%, NO fact failed, and the facts the judges could not settle stay inside 25% of the case. A flagged fact is neither a pass nor a fail; a failed fact is the answer getting it wrong, and no allowance covers that. Coverage alone is not correctness (ticket 29, finding 7).

| Case | Pass | Location coverage | Fact accuracy | Flagged | Missed locations | Conf | Cost |
|---|---|---|---|---|---|---|---|
| multi-bank nab-business-growth-quality | ERROR: chat() failed for qwen/qwen3.7-flash after 5 attempts: HTTP  | | | | | | |
| multi-bank wbc-fy26-productivity-versus-investment | ERROR: chat() failed for qwen/qwen3.7-flash after 5 attempts: HTTP  | | | | | | |
| multi-bank fy25-cross-bank-earnings-conversion | ERROR: chat() failed for qwen/qwen3.7-flash after 5 attempts: HTTP  | | | | | | |
| multi-bank cba-fy25-fy26-earnings-engine-rotation | ERROR: chat() failed for qwen/qwen3.7-flash after 5 attempts: HTTP  | | | | | | |
| multi-bank wbc-low-impairment-versus-provision-caution | ERROR: chat() failed for qwen/qwen3.7-flash after 5 attempts: HTTP  | | | | | | |

## Judged facts

Judge cost: $0.0 over 0 calls (on top of the per-case answer cost).
