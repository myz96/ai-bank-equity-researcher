# 20 — Defect: author prefers slide framing over the Profit Announcement

Type: task
Status: open

## Question

In the corroborated CBA FY26 NIM run, the author preferred slide 60's framing (liquids −4, IRR hedging split out) over the Profit Announcement walk (liquids −3, capital/replicating combined) and justified it as "per the hierarchy" — backwards. The source hierarchy ranks PA tables above presentation slides. Fix: the author prompt must state that when two walks of the same movement conflict, the PA walk's framing is the primary attribution and the slide framing is corroboration/annotation; consider a deterministic preferred-walk selection (doc_type ranking) passed to the author rather than left to prose.

Update 2026-08-26: prompt rule 8 (walk preference) plus book-first walk ordering did NOT bind the cheap author — it again adopted the slide framing and said so. Remaining candidates: (a) deterministic primary-walk injection (the pipeline names the primary walk and the author must use its framing), (b) the normal-tier author. The per-stage evals arbitrate; defect stays open.

Benchmark lesson (Fable baseline, 2026-08-26): the ceiling behaviour is neither picking — it is RECONCILING: the frontier agent showed PA "T&M −2" = slide "T&M ex-repos −1" + "repos −1" and presented one merged, internally consistent decomposition with the relationship stated. Revised target: primary framing = results book (hierarchy), with slide bars arithmetically reconciled into it where the mapping is exact; a disagreement entry only when reconciliation fails.
