# Driver taxonomy and decomposition method

Resolution of wayfinder ticket [01 — Driver taxonomy and decomposition](../../.scratch/equity-research-agent/issues/01-driver-taxonomy-and-decomposition.md).
Grounded in [research/11-decomposition-conventions.md](../../.scratch/equity-research-agent/research/11-decomposition-conventions.md) (verbatim walk labels, cited).

## Method: walk-first, layered, deterministically validated

Every attribution is built from four layers:

1. **Walk extraction** (primary quantified layer). If the bank publishes a walk/bridge for the metric, extract it and map each bar to a canonical driver. The bank's verbatim label is always preserved in the citation.
2. **Arithmetic derivation.** For metrics without a published walk (ROE, CTI), derive contributions from disclosed line items using the identities below. Derived contributions carry an explicit **residual** — never force-fit.
3. **Narrative supplement.** Drivers described in commentary but not quantified are included, marked `unquantified`. The agent also flags where management framing and the numbers diverge (e.g. a "broadly revenue neutral" liquids bar inflating headline NIM movement).
4. **Deterministic validation** (code, not model). Checks run on every extraction:
   - Walk sum: Σ bar contributions = reported movement (tolerance: rounding, e.g. 1bp).
   - Identities: NII ≈ AIEA × NIM; CTI = operating expenses / operating income; ROE ≈ cash NPAT / average equity; loss rate ≈ impairment charge / average gross loans (annualised for halves); CET1 = CET1 capital / RWA.
   - Cross-document agreement: a figure quoted from one document must match its appearance in a second document when one exists (profit announcement vs presentation vs Excel pack).
   - Basis consistency: every figure is tagged cash / statutory / ex-Notables, and reconciliation items must sum to the cash-statutory gap.
   - Comparator consistency: the prior-period value quoted must match that period's own report.

   A failed check is surfaced in the output and lowers confidence; it is never silently dropped.

Basis rule (all metrics): the attribution states its basis. When cash and statutory diverge materially, both headline movements are shown before attribution. For Westpac, "net profit excluding Notable Items" is treated as the cash-comparable basis, and the output says so.

Units and signs: bps for NIM, CET1, loss rates; $m and % for cash earnings and impairment; percentage points (ppt) for ROE and CTI. Positive contribution = metric increased. Negatives render in parentheses.

## 1. NIM (bps) — extract published walk

Canonical drivers, with per-bank verbatim labels:

| Canonical | NAB | Westpac | CBA | ANZ |
|---|---|---|---|---|
| `asset_pricing` | "Lending Margin" | "Loans" | "Asset pricing" | "Assets pricing" |
| `funding.deposits` | "Deposits" | "Deposits" | (inside "Funding costs") | "Deposits pricing" |
| `funding.wholesale` | "Funding Costs" | "Wholesale funding" | (inside "Funding costs") | "Wholesale funding" |
| `liquids` | "Liquid Assets" | "Liquid assets" | "Liquids & Pooled Facilities" | "Group Centre liquids" |
| `capital_replicating` | "Replicating Portfolios" | "Capital & Other" | "Capital, Replicating and Other" | "Capital and replicating portfolio" |
| `mix` | (inside other bars) | (inside other bars) | "Portfolio mix" | "Assets and funding mix" |
| `basis_risk` | — | — | "Basis risk" | — |
| `rate_timing` | (in lending margin narrative) | "Timing difference" (from 1H26) | — | (in assets pricing narrative) |
| `markets_treasury` | "M&T" | "Treasury & Markets" | "Treasury and Markets" | "Markets activities" |
| `other_unmapped` | catch-all for bars that fit no concept above | | | |

Mapping rules:
- A coarse bank bar may map to a **parent** concept: CBA's "Funding costs" maps to `funding` (parent of `deposits`/`wholesale`), not to either child.
- Bar sub-annotations (NAB's "Aust HL −1bp"; Westpac's "Consumer savings reprice 3bps") are captured as child contributions when legible.
- "Ex-volatile" NIM variants are **not** interchangeable across banks (NAB ex-M&T ≠ Westpac Core NIM ≠ ANZ excl. Markets ≠ CBA excl. liquids). The agent names the variant it quotes.

## 2. Cash earnings ($m, %) — extract published bridge

| Canonical | Notes |
|---|---|
| `nii.volume` | AIEA growth |
| `nii.margin` | NIM movement |
| `other_operating_income` | fees, trading, insurance |
| `operating_expenses` | children: `staff`, `technology_investment`, `volume_related`, `productivity` (negative bar), `depreciation_amortisation`, `remediation_restructuring`, `other` |
| `credit_impairment_charge` | sign flows into earnings |
| `tax_and_other` | effective tax rate, minorities |
| `notable_items` | first-class, always separated; per-bank label preserved ("Notable Items" WBC, "significant items" ANZ, "notable" CBA/NAB) |
| `divestments_acquisitions` | e.g. business closures, migrations |
| `residual` | unexplained remainder, reported explicitly |

Bank measure mapping: NAB "cash earnings", ANZ "cash profit", CBA "cash NPAT", Westpac "net profit excluding Notable Items" (cash-comparable, flagged). Pre-provision subtotal names differ per bank and are mapped, not compared raw.

## 3. CET1 ratio (bps) — extract published capital walk

| Canonical | Notes |
|---|---|
| `earnings_generation` | cash earnings / organic capital generation |
| `dividend_net_drp` | dividends net of DRP |
| `capital_returns` | buybacks, capital returns |
| `rwa.credit` | children: `volume`, `asset_quality`, `models_methodology`, `fx` |
| `rwa.market` | traded market risk |
| `rwa.operational` | APS 115 |
| `rwa.irrbb` | APS 117; volatile, always its own bar |
| `capital_floor` | APS 110 72.5% floor adjustment |
| `regulatory_model_changes` | standard changes, overlays, IRB enhancements |
| `divestments_acquisitions` | completion impacts |
| `deductions_other` | capital deductions, reserves |
| `residual` | |

Level 2 (group) ratios are the headline; Level 1 is noted when disclosed.

## 4. Credit impairment charge ($m + loss rate bps) — decompose from notes

| Canonical | Notes |
|---|---|
| `individual_provisions` | new IAPs, single-name exposures |
| `collective.volume` | portfolio growth |
| `collective.asset_quality` | risk migration, transfers to IP |
| `overlays_fla` | forward-looking adjustments, economic scenarios |
| `write_backs_recoveries` | negative charge items |
| `write_offs_direct` | |
| `residual` | |

Loss rate is always computed and quoted with the bank's own denominator named (GLAs / GLAAs / average loans / average gross loans and advances). P&L line label mapped per bank (CIC / impairment charges / LIE / credit impairment (charge)/release).

## 5. ROE (ppt) — two-level arithmetic derivation

- **Level 1**: `earnings_effect` (Δ cash earnings at constant equity) vs `equity_effect` (Δ average equity at constant earnings), computed arithmetically; interaction term goes to `residual`.
- **Level 2**: `earnings_effect` reuses the cash-earnings bridge (§2). `equity_effect` decomposes into `retained_earnings`, `dividends`, `buybacks`, `capital_raisings`, `reserves_other`, sourced from the capital walk (§3) and the statement of changes in equity.
- Variant rule: the agent uses the bank's headline variant (CBA/NAB cash ROE; Westpac ROTE; ANZ ROE + ROTE) and names it. Cross-bank comparisons only on matching variants.

## 6. Cost-to-income ratio (ppt) — two-level arithmetic derivation

- **Level 1**: jaws — `income_growth` vs `expense_growth`; the CTI movement is derived from the two growth rates (deterministic identity).
- **Level 2**: income side reuses `nii.volume` / `nii.margin` / `other_operating_income`; expense side uses the expense-bridge children from §2.
- `notable_items` separated on both sides; ex-Notables CTI quoted when the bank quotes it.

## Unseen-bank rule

The canonical layer is fixed; only the label mappings are per-bank. For a bank outside the registry, the agent maps walk labels to canonical concepts by meaning, puts poor fits in `other_unmapped` rather than forcing them, and lowers confidence accordingly.
