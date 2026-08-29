"""The canonical driver taxonomy (docs/design/driver-taxonomy.md, ticket 01).

Bank-agnostic. Per-bank verbatim label mappings live in registry/<bank>.json.
"""

from __future__ import annotations

TAXONOMY: dict[str, dict] = {
    "nim": {
        "name": "net interest margin",
        "unit": "bps",
        "method": "walk_extraction",
        "retrieval_queries": [
            "net interest margin movement walk driver contributions basis points",
            "net interest income average interest earning assets margin",
            "group margin walk deposits funding liquids replicating portfolio",
        ],
        "walk_markers": ["NIM Movement since", "Group margin", "Net interest margin movement", "margin movement", "Net interest margin -", "Net interest margin –"],
        "method_hint": (
            "Take the movement from the GROUP net interest margin row of the results book's "
            "KPI or performance-summary table, reading each task period's own column. A "
            "divisional or segment table repeats a margin row for ONE business unit at a "
            "different level: that is not the Group margin, so never let it supply the "
            "movement. The Group margin row carries no cash or statutory label; report it on "
            "the bank's primary basis and do not call it statutory. Build the driver table "
            "from the walk whose endpoints are the task's two balance dates; when the results "
            "book and a slide both publish that walk, the book's framing is primary and the "
            "slide corroborates. Claim every bar of the walk you adopt, zero bars included."
        ),
        "drivers": {
            "asset_pricing": "Lending margin / asset pricing / competition",
            "funding": "Funding costs (parent of deposits and wholesale)",
            "funding.deposits": "Deposit pricing and mix",
            "funding.wholesale": "Wholesale funding costs",
            "liquids": "Liquid assets and pooled facilities drag",
            "capital_replicating": "Capital, replicating portfolio and hedge earnings",
            "mix": "Asset and funding mix",
            "basis_risk": "Basis risk (bills/OIS spread)",
            "rate_timing": "Timing lag between cash-rate changes and customer repricing (Westpac splits this out)",
            "markets_treasury": "Markets and Treasury contribution",
            "other_unmapped": "Bars that fit no canonical concept",
        },
    },
    "cash_earnings": {
        "name": "cash earnings",
        "unit": "$m",
        "method": "bridge_extraction",
        # One query per bridge component (the P&L section titles every bank's
        # results book uses), so retrieval covers each component's own page
        # rather than only summary/reconciliation pages (ticket 25).
        "retrieval_queries": [
            "cash earnings statutory net profit reconciliation non-cash items",
            "total operating income operating performance net profit after tax cash basis",
            "net interest income increase average interest earning assets growth",
            "other operating income commissions lending fees trading income",
            "underlying operating expenses staff information technology restructuring notable items",
            "operating expenses waterfall inflation investment technology productivity",
            "loan impairment expense retail banking business banking new zealand movement",
            "income tax expense effective tax rate",
        ],
        # "Statutory vs cash NPAT" was removed as a walk marker (ticket 25):
        # it marks a two-column LEVELS reconciliation table, not a movement
        # bridge. The vision walk reader turned its comparator column into
        # "bars", and the inevitable walk_sum failure fatally capped
        # confidence. The reconciliation still reaches the author as
        # text/table evidence via the first retrieval query.
        "walk_markers": ["cash earnings bridge", "cash earnings walk"],
        "method_hint": (
            "Build the bridge from component MOVEMENTS in $m: net interest income, other "
            "operating income, UNDERLYING operating expenses (state notable/restructuring "
            "items separately, never inside the underlying number), credit impairment, and "
            "tax. When a table shows both periods' levels, compute the delta yourself and "
            "cite the table (e.g. expenses and tax are usually disclosed as levels for both "
            "periods). Claim tax_and_other as a quantified component from the tax expense "
            "movement, and claim the notable/restructuring items DELTA as its own "
            "notable_items component; declare a residual only for what genuinely remains. "
            "Say explicitly whether an expense figure is underlying or headline. "
            "NEVER claim statutory-to-cash reconciliation items (hedging/IFRS volatility, "
            "disposal gains and losses) as bridge drivers: they explain why statutory "
            "differs from cash in the SAME period, not why cash earnings moved year on "
            "year. When the reconciliation is in evidence, the headline MUST also give the "
            "statutory movement next to the cash movement and name the non-cash items that "
            "separate them."
        ),
        "drivers": {
            "nii": "Net interest income total (claim this when volume/margin are not separately quantified in dollars)",
            "nii.volume": "Net interest income: volume (AIEA growth)",
            "nii.margin": "Net interest income: margin (NIM movement)",
            "other_operating_income": "Fees, trading, insurance and other income",
            "operating_expenses": "Operating expenses (staff, technology, other)",
            "credit_impairment_charge": "Credit impairment charge movement",
            "tax_and_other": "Tax and minorities",
            "notable_items": "Notable / significant items",
            "divestments_acquisitions": "Business disposals, closures, migrations",
            "other_unmapped": "Unmapped components",
        },
    },
    "roe": {
        "name": "return on equity",
        "unit": "ppt",
        "method": "two_level_arithmetic",
        "retrieval_queries": [
            "return on equity cash basis average shareholders equity",
            "key performance indicators return on equity",
            "shareholders equity dividends buyback capital",
            # The level-1 derivation needs the earnings movement itself.
            "net profit after tax cash basis increase prior year",
        ],
        "extract_focus": (
            "also extract the cash profit levels for both periods and the profit growth "
            "rate, plus any average equity figures — the ROE numerator and denominator"
        ),
        "walk_markers": [],
        "method_hint": (
            "Quantify the movement from the KPI table, reading the row for the bank's headline "
            "ROE measure and the column of each task period (in ppt). Level 1 is an "
            "ARITHMETIC DERIVATION, not a disclosure hunt: with the ROE endpoints and the "
            "earnings growth rate in evidence, compute earnings_effect = prior-period ROE x "
            "earnings growth (the ppt lift at constant equity), and equity_effect = total "
            "delta minus earnings_effect (equity growth and the interaction term). Claim "
            "both as quantified contributions, citing the KPI-table and earnings-movement "
            "records, and say in each narrative that the value is derived, not disclosed. "
            "The earnings growth rate must come from an evidence record (the profit "
            "movement in $m or %); NEVER infer it from the ROE endpoints themselves and "
            "NEVER assume the equity effect is zero — if the earnings movement is missing, "
            "request it as evidence. Support equity_effect's direction with cited "
            "reasoning (retained earnings, buybacks, DRP treatment). Only leave the split "
            "unquantified when the ROE endpoints or the earnings movement are genuinely "
            "missing from evidence."
        ),
        "drivers": {
            "earnings_effect": "Movement in cash earnings at constant equity",
            "equity_effect": "Movement in average equity at constant earnings",
            "other_unmapped": "Interaction residual",
        },
    },
    "cet1": {
        "name": "CET1 ratio",
        "unit": "bps",
        "method": "walk_extraction",
        "retrieval_queries": [
            "CET1 capital ratio movement basis points dividend RWA",
            "capital adequacy ratios common equity tier 1",
            "risk weighted assets movement credit market operational IRRBB",
        ],
        "walk_markers": ["Movements in bpts", "capital ratio movement", "CET1 ratio movement"],
        "method_hint": (
            "Take the movement from the capital or KPI table, reading the APRA Level 2 (Group) "
            "CET1 ratio row and the column of each task period. The Level 1 ratio, the "
            "internationally comparable ratio and any pro-forma ratio are DIFFERENT measures: "
            "quote them as context or as a disagreement, never as the movement. Build the "
            "driver table from a walk whose endpoints are the task's two balance dates. Banks "
            "often publish only the half-on-half capital walk: when they do, do NOT restate its "
            "bars as this comparison's contributions. Quantify instead the drivers the text "
            "states in bpts for events INSIDE the comparison window — regulatory, model and "
            "accounting-standard changes, dividends net of DRP, buy-backs and divestments are "
            "usually footnoted with their own bpts impact — cite the footnote, and leave the "
            "rest unquantified with the half-on-half walk's numbers described in the narrative."
        ),
        "drivers": {
            "earnings_generation": "Capital generated from earnings",
            "dividend_net_drp": "Dividends net of DRP",
            "capital_returns": "Buybacks and capital returns",
            "rwa.credit": "Credit risk RWA movement",
            "rwa.market": "Traded market risk RWA",
            "rwa.operational": "Operational risk RWA",
            "rwa.irrbb": "IRRBB RWA (APS 117), volatile",
            "capital_floor": "Capital floor adjustment (APS 110)",
            "regulatory_model_changes": "Model and regulatory changes",
            "divestments_acquisitions": "Divestment and acquisition impacts",
            "deductions_other": "Capital deductions, reserves, other",
            "other_unmapped": "Unmapped bars",
        },
    },
    "impairment": {
        "name": "credit impairment charge",
        "unit": "$m",
        "method": "note_decomposition",
        "retrieval_queries": [
            "loan impairment expense collective individual provisions",
            "credit impairment charge forward looking adjustments overlays",
            "provisions for impairment asset quality",
        ],
        "walk_markers": [],
        "method_hint": (
            "Quantify the movement components in $m. The results book discloses the "
            "impairment line PER DIVISION for both periods (a table and/or bullets like "
            "'Retail +106 to 378'): when the bullets omit the delta, COMPUTE each "
            "division's delta from the two period columns and cite the table. Attribute "
            "each divisional delta to collective vs individually assessed provision "
            "drivers as the text states, sum them, and declare the small remainder (e.g. "
            "a corporate-centre division) as the residual — never force-fit. Decompose the "
            "P&L impairment CHARGE line itself: movements in provision BALANCES on the "
            "balance sheet are context for the narrative, never the quantified bridge (a "
            "provision-stock delta is not the period's charge). Always quote the loss "
            "rate in bps with the bank's denominator named."
        ),
        "drivers": {
            "individual_provisions": "Individually assessed / single-name provisions",
            "collective.volume": "Collective provisions: portfolio growth",
            "collective.asset_quality": "Collective provisions: risk migration",
            "overlays_fla": "Forward-looking adjustments and overlays",
            "write_backs_recoveries": "Write-backs and recoveries",
            "write_offs_direct": "Direct write-offs",
            "other_unmapped": "Unmapped components",
        },
    },
    "cti": {
        "name": "cost-to-income ratio",
        "unit": "ppt",
        "method": "two_level_arithmetic",
        "retrieval_queries": [
            "operating expenses to total operating income cost to income",
            "operating expenses staff technology investment productivity",
            "total operating income growth expense growth jaws",
        ],
        "walk_markers": [],
        "extract_focus": (
            "also extract the total operating income and total operating expense levels for "
            "every period column — the ratio's numerator and denominator"
        ),
        "method_hint": (
            "Take the ratio endpoints from the results book's KPI table, from the row for the "
            "bank's HEADLINE cost-to-income measure named in the bank vocabulary, reading each "
            "task period's own column. An 'underlying', 'ex-notable' or single-division version "
            "of the ratio is a DIFFERENT measure: report it beside the headline movement or as "
            "a disagreement, never as the movement itself. Level 1 is jaws: compute income "
            "growth and expense growth in per cent from the disclosed levels of both periods, "
            "say which grew faster, and name the jaws as positive or negative. Claim a ppt "
            "contribution only when the evidence supports the arithmetic; otherwise give the "
            "growth rates in the narrative and leave the ppt split unquantified."
        ),
        "drivers": {
            "income_growth": "Operating income growth (jaws numerator)",
            "expense_growth": "Operating expense growth (jaws denominator)",
            "notable_items": "Notable and restructuring items on either side",
            "other_unmapped": "Unmapped components",
        },
    },
}

METRIC_ALIASES = {
    "nim": "nim",
    "net interest margin": "nim",
    "cash earnings": "cash_earnings",
    "cash_earnings": "cash_earnings",
    "roe": "roe",
    "return on equity": "roe",
    "cet1": "cet1",
    "cet1 ratio": "cet1",
    "impairment": "impairment",
    "credit impairment charge": "impairment",
    "cti": "cti",
    "cost-to-income ratio": "cti",
    "cost to income": "cti",
}
