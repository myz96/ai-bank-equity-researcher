# 01 — Driver taxonomy and decomposition method per metric

Type: grilling
Status: resolved
Blocked by: 08, 11

## Question

For each of the six headline metrics (net interest margin, cash earnings, return on equity, CET1 ratio, credit impairment charge, cost-to-income ratio): what driver taxonomy does the agent use, and what decomposition method quantifies each driver's contribution to a movement? How is the taxonomy grounded in what banks actually disclose (NIM walks, earnings bridges, capital walks) while staying comparable across banks whose disclosures differ?

## Answer

Resolved with the user (grilling, 2026-08-25). Full artifact: [docs/design/driver-taxonomy.md](../../../docs/design/driver-taxonomy.md). Decision recorded as [ADR-0001](../../../docs/adr/0001-walk-first-layered-attribution.md).

- **One canonical cross-bank taxonomy per metric**, with per-bank verbatim label mappings; citations keep the bank's own words; `other_unmapped` catches poor fits (the unseen-bank path).
- **Walk-first layered method**: extract the published walk/bridge where one exists (NIM, cash earnings, CET1); decompose impairment from the notes; derive ROE and CTI arithmetically in two levels; include narrative drivers marked `unquantified`.
- **Deterministic validation in code** (user's addition): walk sums, NII = AIEA × NIM and other identities, cross-document agreement, basis and comparator consistency. Failures surface in output and lower confidence.
- **Reconciliation**: extracted walks must sum to the movement; derived decompositions carry an explicit residual, never force-fitted.
- **Notable items are a first-class category**; every figure is tagged with its basis (cash / statutory / ex-Notables); both headline movements shown when bases diverge materially.
- **Units**: bps (NIM, CET1, loss rate), $m/% (cash earnings, impairment), ppt (ROE, CTI); positive = metric up; parentheses for negatives.
