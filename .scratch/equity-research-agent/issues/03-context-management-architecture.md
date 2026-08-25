# 03 — Context management architecture

Type: grilling
Status: resolved
Blocked by: 08, 13, 14

## Progress (grilling round 1, 2026-08-25)

Settled with the user:
- **Evidence records**: the orchestrator never sees raw PDF text at scale. A cheap-model extractor reads selected page ranges and emits typed records (document, printed+PDF page, verbatim quote/table, parsed numbers, units, basis tags). The reasoning model gets task + taxonomy + map branches + records only.
- **Caching**: start minimal — raw PDFs and extracted page text only. The evidence-record cache layer is deferred until eval cost demands it (user: leave out unnecessary complexity first).

Open, pending prototypes:
- Page-finding approach (section maps vs embeddings) → decided by ticket 13's bake-off.
- Chart reading (text layer vs vision model vs parse service) → decided by ticket 14's reliability test.

## Answer

Resolved with the user 2026-08-25, on prototype evidence (tickets 13 and 14):

1. **Page finding**: local hybrid retrieval — dense `BAAI/bge-small-en-v1.5` top-k unioned with BM25 — computed locally at zero model cost. No LLM navigation; no section maps. (Bake-off: dense 10/10, BM25 9/10, LLM navigation 4–8/10 and slower.)
2. **Evidence records**: the reasoning model reads only typed records (document, printed+PDF page, verbatim quote/table, parsed numbers, units, basis tags) extracted by the cheap model from retrieved pages. Never raw PDF text at scale.
3. **Chart pages**: render at 2x and read with vision `qwen3.7-flash` (24/24 gold bars, $0.0006); the deterministic sum check validates every extraction — tight tolerance for Profit Announcement walks, documented looser tolerance for presentation walks (CBA's own CET1 slide does not sum, per its rounding footnote).
4. **Caching**: minimal — raw PDFs, extracted page text, local embedding vectors. The evidence-record cache is deferred until eval cost demands it.
5. **Operational caveats**: `ox-alpha` is experiment-only (rate limits); `glm-5.3` requires a reasoning-aware client (ignores the reasoning-off flag) — flagged into ticket 07.

Recorded as [ADR-0002](../../../docs/adr/0002-local-retrieval-vision-charts.md).

## Question

How does a multi-hundred-page results pack become the small, correct slice the model reads? Decide: document indexing and navigation (table-of-contents maps vs retrieval), the extraction step and its output representation (for example compact evidence records), how chart-only evidence (walk charts as images) is read, what the orchestrator context holds at any time, and what is cached between runs.
