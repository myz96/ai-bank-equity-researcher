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
        "retrieval_queries": [
            "cash earnings statutory net profit reconciliation non-cash items",
            "group performance summary net interest income operating expenses impairment",
            "operating income waterfall cash net profit after tax",
            "net profit after tax cash basis continuing operations movement prior year",
        ],
        "walk_markers": ["Statutory vs cash NPAT", "cash earnings bridge"],
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
        ],
        "walk_markers": [],
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
