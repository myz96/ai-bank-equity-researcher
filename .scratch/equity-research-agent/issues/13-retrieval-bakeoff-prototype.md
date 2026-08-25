# 13 — Prototype: retrieval bake-off (section maps vs embeddings)

Type: prototype
Status: resolved
Blocked by: 15, 16

## Question

On the CBA corpus, which evidence-finding approach wins? Build both cheaply and compare:

- **(a) Section-map navigation**: one cheap-model pass per document builds a cached map (TOC, per-page headings, section summaries); a navigator model picks page ranges from the map.
- **(b) Embeddings retrieval**: chunk pages, embed with a local open-source embedding model (OpenRouter exposes no embeddings endpoint), retrieve top-k per query.

Fixed target set from ticket 08 (known evidence locations, FY26): NIM walk (PA printed p12), HoH walk (p13), NIM history appendix (p72), Group Performance Summary (p2), cash-vs-statutory reconciliation (App 6.3, p113), LIE section (p18), capital section (p28), expenses (p15), KPIs (pp4–5); presentation slides 23–27, 32, 60.

Score: hit rate (correct page inside the selected ranges / top-k), token cost, wall time, code complexity. Output: a comparison table the user reacts to before ticket 03 closes.

## Results (2026-08-25, prototypes/bakeoff.py)

Ten targets, gold pages located by marker search (not hardcoded). Hit = a gold page inside the arm's top-8 selection.

| Arm | Hits | Wall time | Model cost |
|---|---|---|---|
| dense embeddings, local `BAAI/bge-small-en-v1.5` | **10/10** | 114s first run (model load), seconds after | $0 |
| BM25 (rank-bm25, local) | 9/10 | instant | $0 |
| section map + `stealth/ox-alpha` navigator | 8/10 | 745s (free-tier 429 backoffs; one target lost to a rate-limit failure) | $0 |
| section map + `qwen/qwen3.7-flash` navigator | 4/10 | 19s | $0.0003 |

The only BM25 miss was the chart-heavy slide with almost no body text ("Group margin – 12 months"), which dense embeddings still caught. LLM navigation was slower, costlier, and less accurate than local retrieval on these well-structured documents.

**Recommendation:** retrieval = local hybrid (dense bge-small top-k unioned with BM25), no LLM in the page-finding loop. This contradicts the original section-map lean in ticket 03's grilling — the prototype settles it. User accepted 2026-08-25.
