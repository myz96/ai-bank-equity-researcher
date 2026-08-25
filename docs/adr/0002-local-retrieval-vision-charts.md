# Local hybrid retrieval; vision models read charts

Page finding uses local dense embeddings (bge-small) unioned with BM25 — no LLM navigation and no section maps — and chart pages are rendered to images and read by a cheap vision model, validated by a deterministic sum check. Both choices were settled by prototype bake-offs on the CBA corpus (tickets 13 and 14), not by preference: local retrieval beat LLM navigation 10/10 vs 4–8/10 at zero cost, and vision reading scored 24/24 gold walk bars at $0.0006 while every text-layer arm failed the bar-label pairing.

## Consequences

- Retrieval is transparent and free, so the eval matrix can rerun page finding at no model cost.
- A future reader may expect RAG-with-an-agent or a TOC navigator here; the bake-off data is the reason it is absent. Revisit only if retrieval measurably misses evidence on another bank's documents.
- Presentation walks get a looser sum tolerance than Profit Announcement walks: CBA's own CET1 slide footnotes that its bars do not sum precisely.
