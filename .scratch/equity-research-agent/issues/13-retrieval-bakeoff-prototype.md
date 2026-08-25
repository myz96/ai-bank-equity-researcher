# 13 — Prototype: retrieval bake-off (section maps vs embeddings)

Type: prototype
Status: open
Blocked by: 15, 16

## Question

On the CBA corpus, which evidence-finding approach wins? Build both cheaply and compare:

- **(a) Section-map navigation**: one cheap-model pass per document builds a cached map (TOC, per-page headings, section summaries); a navigator model picks page ranges from the map.
- **(b) Embeddings retrieval**: chunk pages, embed with a local open-source embedding model (OpenRouter exposes no embeddings endpoint), retrieve top-k per query.

Fixed target set from ticket 08 (known evidence locations, FY26): NIM walk (PA printed p12), HoH walk (p13), NIM history appendix (p72), Group Performance Summary (p2), cash-vs-statutory reconciliation (App 6.3, p113), LIE section (p18), capital section (p28), expenses (p15), KPIs (pp4–5); presentation slides 23–27, 32, 60.

Score: hit rate (correct page inside the selected ranges / top-k), token cost, wall time, code complexity. Output: a comparison table the user reacts to before ticket 03 closes.
