# 32 — Component bake-off round: parser, embeddings, vision-vs-text paths

Type: task
Status: open

## Question

Time-permitting robustness round (user, 2026-08-28): the current component choices are tested but not comprehensively compared — make each a measured decision rather than an assumption. Reuse the prototype-13/14 harnesses; every arm scores against existing gold.

1. **Extraction paths**: text-layer vs vision-rendered per page TYPE (clean tables, dense tables, era pages with text-layer artifacts like FY21's "47. 0", chart pages). Decides whether vision-for-tables earns its cost anywhere.
2. **Embedding models**: bge-small (current) vs a bigger local model (bge-m3 class) vs BM25-only, on the bake-off target set EXTENDED with NAB/WBC and longitudinal-case queries — CBA-shaped documents flattered the current choice.
3. **Parser**: pymupdf vs one alternative (pdfplumber or a vision-first read) on the known trap pages (decimal-space era pages, hidden-text slides, the chart page that breaks the vision reader).

Trigger earlier than "time permitting" if: a retrieval miss appears on NAB/WBC/longitudinal cases, or an extraction-stage regression traces to the text layer. Success = a table per component, and either a documented switch or a documented keep.
