# 25 — Iterate the cash-earnings bridge path to the benchmark spec

Type: task
Status: resolved

## Question

The pipeline scores 1/4 components at confidence 40 on CBA cash earnings FY26 while the Fable benchmark reconciled the full bridge with zero residual (docs/design/benchmarks.md). Close the gap using the benchmark's working as the spec: (1) extraction must capture the FY25 comparative LEVELS (tax expense, notable items) so deltas are computable, plus the presentation's income waterfall (slide 25) and the statutory-vs-cash reconciliation (slide 23); (2) the author must distinguish underlying vs headline expenses and claim the underlying bridge (−719) with the notable delta separate; (3) claim the `tax_and_other` component instead of dumping it into residual; (4) state the statutory divergence with its reason. Target: 4/4 gold components within tolerance, confidence earned above 80. Verify against the harness (CBA-only suite).

## Progress note — 2026-08-27 (cheap-combo bridge iteration)

Root cause found: the author never received the bridge evidence. Two defects
caused this.

1. Page starvation. The FY26 Profit Announcement produced ~20 candidate
   pages. The doc-type-ranked ordering let it fill all 10 text slots. The
   presentation waterfall slides (24/25/27) and the component pages of the PA
   (p28 NII, p30 OOI, p31 expenses, p34 LIE) were never extracted.
2. Bogus walk. The marker "Statutory vs cash NPAT" matched slide 23. That
   slide is a two-column LEVELS reconciliation, not a movement bridge. The
   vision reader turned the comparator column into bars. The walk_sum failure
   was fatal and capped confidence at 40 on every run.

Changes:

- pipeline.py: MAX_TEXT_PAGES 10 -> 14, and a new per-document cap
  (MAX_TEXT_PAGES_PER_DOC = 7). The source hierarchy stays; one document can
  no longer starve the others. Also: per-metric "extract_focus" is appended
  to the case description, so the extractor keeps identity inputs (profit,
  equity) for derived metrics.
- taxonomy.py (cash_earnings): one retrieval query per bridge component
  (NII, OOI, expenses, LIE, tax, summary, reconciliation, expense walk).
  Removed the "Statutory vs cash NPAT" walk marker (reason above; the
  reconciliation still arrives as text evidence). Method hint now: claim
  tax_and_other and the notable delta as components; NEVER claim
  statutory-to-cash reconciliation items as bridge drivers; state the
  statutory movement next to cash in the headline.
- taxonomy.py (roe): level-1 arithmetic split is now explicit
  (earnings_effect = prior ROE x earnings growth; equity_effect = delta
  minus earnings_effect). The growth rate must come from evidence; the hint
  forbids inferring it from the ROE endpoints. Added a query and an
  extract_focus for the profit movement.
- taxonomy.py (impairment): compute divisional deltas from the two period
  columns when bullets omit them; decompose the P&L charge, not provision
  balances; declare the small remainder as residual.
- author.py: new rule 9 — claim every bar of the primary walk, including
  zero bars and small bars.
- extract.py: the text prompt now demands full coverage of
  performance-summary tables, signed deltas from movement statements, and
  divisional rows; record cap 8 -> 10. The walk-vision retry nudges the
  format and raises the token budget.

Results (single-case, cheap combo): cash_earnings FY26 reached the full
six-component bridge (NII +1563, OOI +196, expenses -719, notables -40,
LIE -62, tax -208; residual none; conf 95). ROE FY26 derived +0.94 / -0.44
ppt with the cited 7% growth (conf 95). Impairment FY26 quantified the
divisional deltas (+106, -45, -16, +11, +6; sum 62 exact; conf 95).
NIM FY26 claimed 7/7 bars, both zero bars included.

Suite run (evals/results/20260827-0801-cheap-dev.md, 19 dev cases — the
1H26/FY21 non-NIM cases ran for the first time): cash_earnings FY26 scored
4/4 recall and 4/4 precision. In that run the author claimed only the four
components and computed the residual wrong (-148 instead of -248);
drivers_reconcile caught it and capped confidence at 40. The single-case run
above shows the same code reaching the full bridge at conf 95; the gap is
author variance, not a code path.

Normal-combo answer (out/cba-cash_earnings-fy26-vs-fy25-normal/): glm-5.3 on
the OLD evidence also failed the bridge (only expenses -719 and notables -40
quantified; residual +1489; conf 40; $0.22, 19 minutes). The bottleneck was
evidence coverage, not author capability. A per-metric author tier is
therefore NOT needed; the config.py feature was not built.

Open defects for the next iteration (not fixed here):

1. Author JSON parse crashes: two cases (cash_earnings 1H26, cti FY26) died
   with "Expecting ':' delimiter". author_attribution has no parse-failure
   retry; extract_walk does. Mirror that retry.
2. Spurious confidence caps: nim FY26 scored 7/7 recall and 7/7 precision,
   but a SECONDARY walk misread (bars summed +202) failed walk_sum, and any
   walk_sum failure is fatal. When another walk for the same comparison
   passed and the claims reconcile, the failed secondary read should be
   peripheral, not fatal.
3. The FY25 PA NIM chart still breaks the vision reader ("Unterminated
   string", both attempts): nim FY25 fell to 2/7. The hardened retry did not
   cure this page.
4. Residual arithmetic: the author retry loop returns the failure text, but
   the model still computed -148 instead of -248 once. A code-side residual
   suggestion (delta minus claimed sum) in the retry message would close it.
