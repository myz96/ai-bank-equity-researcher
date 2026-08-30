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
            # Phrased for the NII section's TABLE page (the row levels and the
            # stated PCP movement), not the continuation page of its prose: the
            # old growth-phrased query ranked the continuation page first and
            # the 1H26 author never saw the stated PCP movement (ticket 27).
            "net interest income cash basis net interest margin average interest earning assets table",
            "other operating income commissions lending fees trading income",
            "underlying operating expenses staff information technology restructuring notable items",
            "operating expenses waterfall inflation investment technology productivity",
            "loan impairment expense retail banking business banking new zealand movement",
            "income tax expense effective tax rate",
        ],
        # The bridge components live in P&L tables whose rows a literal-minded
        # extractor drops as background ("cash earnings" names none of them).
        "extract_focus": (
            "also extract every P&L line of the group performance and section tables for "
            "EVERY period column - net interest income, other operating income, total "
            "operating income, operating expenses (underlying, notable items and total), "
            "loan impairment expense, tax expense and profit - these are the bridge "
            "components"
        ),
        # Canonical component -> normalised label words that identify it in
        # extracted evidence. Drives the completeness nudge in the author
        # retry: a component these words find quantified in evidence must not
        # stay unclaimed. Words, never values.
        "component_labels": {
            "nii": ("netinterestincome",),
            "other_operating_income": ("otheroperatingincome",),
            "operating_expenses": ("operatingexpenses",),
            "credit_impairment_charge": ("loanimpairmentexpense", "creditimpairment"),
        },
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
            "tax. CLAIM EVERY COMPONENT the evidence quantifies — at minimum NII, other "
            "operating income, underlying operating expenses and loan impairment; leaving "
            "a disclosed component unclaimed is a recall failure, not caution. COLUMN "
            "DISCIPLINE per component: prefer the movement the bank STATES 'on the prior "
            "comparative period'; when you compute a delta yourself from a table, "
            "subtract that component's value in the comparator's column from its value "
            "in the period's column — the SAME rule as the movement, so a delta against "
            "the middle (prior-half) column, or a prior-half level, is never a "
            "contribution. A near-zero movement between the task's two columns is still "
            "the movement, however large the swing against the prior half looks. SIGN: a "
            "contribution is the effect on cash earnings — an INCREASE in expenses, "
            "impairment or tax is a NEGATIVE contribution even where the bank prints the "
            "change as a positive number. Claim tax_and_other as a quantified component "
            "from the tax expense movement, and claim the notable/restructuring items "
            "DELTA as its own notable_items component; declare a residual only for what "
            "genuinely remains. Say explicitly whether an expense figure is underlying or "
            "headline. NEVER claim statutory-to-cash reconciliation items (hedging/IFRS "
            "volatility, disposal gains and losses) as bridge drivers: they explain why "
            "statutory differs from cash in the SAME period, not why cash earnings moved "
            "year on year. When the reconciliation is in evidence, the headline MUST also "
            "give the statutory movement next to the cash movement and name the non-cash "
            "items that separate them. OPEN WITH THE BANK'S OWN SUMMARY of the result "
            "before the component list: total operating income with its growth rate, "
            "operating performance (income less operating expenses, before impairment) "
            "with its growth rate, and the period's statutory profit beside its cash "
            "profit — each as the bank prints it, from evidence, whichever document "
            "carries it."
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
            "delta minus earnings_effect (equity growth and the interaction term). SCALE: "
            "the growth rate enters this identity as a FRACTION, so a fall of 2.1 per cent "
            "is -0.021 and never -2.1, and a profit movement in dollars enters divided by "
            "average equity. Both contributions are therefore SMALLER than the ROE "
            "endpoints themselves; a contribution bigger than the ratio is a scale error, "
            "not a driver. Claim "
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
            "rwa": "Total risk-weighted assets movement (parent of rwa.credit, rwa.market, rwa.operational, rwa.irrbb; claim this for an undecomposed total-RWA bar)",
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
        # A charge is stated as a POSITIVE number, whatever sign the table
        # prints. Banks put the impairment line inside the P&L, where every
        # expense is bracketed: Westpac prints "Impairment (charges)/benefits
        # (424) | (537)" and CBA's FY21 group summary prints "(554) | (2,518)".
        # Both are charges. author.py reads this flag.
        "sign_convention": "positive_charge",
        "method_hint": (
            "SIGN: state the charge as a POSITIVE number in both endpoints, so a FALLING "
            "charge gives a NEGATIVE delta. A results table often prints the impairment line "
            "inside the P&L, where expenses are bracketed — a row reading 'Impairment "
            "(charges)/benefits (424) (537)' is a charge of 424 against a charge of 537, and "
            "the bank's own prose beside it says 'the credit impairment charge of $424 "
            "million'. Take the bracketed figures as charge magnitudes; never carry the "
            "bracket into from_value and to_value. "
            "Quantify the movement components in $m. PROVISION TYPE FIRST: when the "
            "impairment note splits the CHARGE into its provision types for both periods "
            "— net collective provisioning, new and increased individually assessed "
            "provisioning, write-backs and recoveries — build the quantified bridge from "
            "those rows, because they are the canonical drivers and they sum to the "
            "movement. A DIVISION is not a provision type. ALSO NAME WHERE THE MOVEMENT "
            "AROSE: the results book discloses the impairment EXPENSE per DIVISION for "
            "both periods — the bank's own segments, retail, business, institutional, the "
            "offshore bank and the corporate centre — in a table and/or bullets like "
            "'Retail +106 to 378'. That divisional table is the where-layer, and a "
            "provision BALANCE split by portfolio is not a substitute for it. State EVERY "
            "division's movement — the delta AND both period levels — inside the NARRATIVE "
            "of the driver it belongs to, and cite the divisional table there; when the "
            "bullets omit the delta, COMPUTE each division's delta from the two period "
            "columns. When the note publishes no provision-type split, build the bridge "
            "from the divisional deltas instead: attribute "
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
            # Phrased for the GROUP KPI / performance-summary page, not for the
            # ratio label alone (ticket 27, NAB FY25). Every divisional table
            # repeats the row "Cost to income ratio", so a label-only query
            # ranked three NAB divisional pages above the Group KPI page and
            # the author took a division's 34.0% for the Group's 47.3%. Naming
            # the section title as well as both common label forms puts the KPI
            # page first for CBA, NAB and WBC alike.
            "key performance indicators group performance cost to income ratio "
            "operating expenses to total operating income",
            "operating expenses staff technology investment productivity",
            "total operating income growth expense growth jaws",
        ],
        "walk_markers": [],
        "extract_focus": (
            "also extract the total operating income and total operating expense levels for "
            "every period column — the ratio's numerator and denominator"
        ),
        "method_hint": (
            "Take the ratio endpoints from the GROUP KPI table of the results book, from the "
            "row for the bank's HEADLINE cost-to-income measure named in the bank vocabulary, "
            "reading each task period's own column. A divisional or segment table repeats the "
            "SAME row label for ONE business unit at a different level: that is not the Group "
            "ratio, so never let it supply the movement — a divisional ratio is often ten or "
            "more points away from the Group's. When the KPI table prints one BLOCK per basis "
            "(a statutory block and a cash block, each with its own 'Cost to income ratio' "
            "row), take the block for the bank's primary basis and quote the other block as "
            "context. An 'underlying', 'ex-notable' or single-division version "
            "of the ratio is a DIFFERENT measure: report it beside the headline movement or as "
            "a disagreement, never as the movement itself. Level 1 is jaws: compute income "
            "growth and expense growth in per cent from the disclosed levels of both periods, "
            "say which grew faster, and name the jaws as positive or negative. SIGN: a "
            "contribution is the effect on the RATIO, so the quantified contributions plus the "
            "residual must sum to the movement delta. Expense growth that outruns income "
            "growth RAISES the ratio, which is a POSITIVE contribution to a rising ratio; "
            "income growth that outruns expenses LOWERS it. Check the sum against the delta "
            "before you answer: two negative contributions can never explain a ratio that "
            "rose. Claim a ppt "
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
