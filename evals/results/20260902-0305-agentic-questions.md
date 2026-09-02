# Questions scorecard — combo agentic, 20260902-0305

## Run metadata

- run: 20260902-0305 (UTC)
- commit: 4b3f80c (working tree dirty)
- gold sha256 (evals/gold/*.json, first 16): acfb8172d297fa3b
- judges: deepseek/deepseek-v4-pro-0813, qwen/qwen3.7-flash

Two populations, reported apart. **Location coverage** measures the retriever: did the answer cite the pages that carry the answer? **Fully-grounded facts** measures citation discipline, not analysis quality: did the judges rule each gold fact both STATED by the answer and ENTAILED by its cited quotes, with EVERY load-bearing number present in those quotes? An answer whose analysis is right but whose quotes omit a number it used scores a fail here by design (measured 2026-08-31: frontier agents state nearly every gold fact and lose this column on quote completeness). A case PASSES only when coverage is 100%, NO fact failed, and the facts the judges could not settle stay inside 25% of the case. A flagged fact is neither a pass nor a fail; a failed fact is the answer getting it wrong, and no allowance covers that. Coverage alone is not correctness (ticket 29, finding 7).

| Case | Pass | Location coverage | Fully-grounded facts | Flagged | Missed locations | Conf | Cost |
|---|---|---|---|---|---|---|---|
| multi-bank nab-business-growth-quality | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | |
| multi-bank wbc-fy26-productivity-versus-investment | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | |
| multi-bank fy25-cross-bank-earnings-conversion | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | |
| multi-bank cba-fy25-fy26-earnings-engine-rotation | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | |
| multi-bank wbc-low-impairment-versus-provision-caution | ERROR: chat_tools() failed for z-ai/glm-5.3-flash after 5 attempts: | | | | | | |

## Judged facts

Judge cost: $0.0 over 0 calls (on top of the per-case answer cost).
