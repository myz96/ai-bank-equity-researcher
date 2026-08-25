# 03 — Context management architecture

Type: grilling
Status: open
Blocked by: 08, 13, 14

## Progress (grilling round 1, 2026-08-25)

Settled with the user:
- **Evidence records**: the orchestrator never sees raw PDF text at scale. A cheap-model extractor reads selected page ranges and emits typed records (document, printed+PDF page, verbatim quote/table, parsed numbers, units, basis tags). The reasoning model gets task + taxonomy + map branches + records only.
- **Caching**: start minimal — raw PDFs and extracted page text only. The evidence-record cache layer is deferred until eval cost demands it (user: leave out unnecessary complexity first).

Open, pending prototypes:
- Page-finding approach (section maps vs embeddings) → decided by ticket 13's bake-off.
- Chart reading (text layer vs vision model vs parse service) → decided by ticket 14's reliability test.

## Question

How does a multi-hundred-page results pack become the small, correct slice the model reads? Decide: document indexing and navigation (table-of-contents maps vs retrieval), the extraction step and its output representation (for example compact evidence records), how chart-only evidence (walk charts as images) is read, what the orchestrator context holds at any time, and what is cached between runs.
