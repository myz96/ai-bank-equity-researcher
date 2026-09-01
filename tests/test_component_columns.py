"""The component-column check (ticket 27): rule 10's discipline one level down.

A bridge answer can carry the right movement and still read its components out
of the wrong table columns. The fixtures mirror the CBA 1H26 GPS table shape —
three period columns — with neutral values.
"""

from __future__ import annotations

from bank_equity_researcher.validation.schema import (
    Attribution,
    Contribution,
    DriverClaim,
    EvidenceRecord,
    Movement,
    NumberFact,
)
from bank_equity_researcher.validation.validate import (
    check_component_columns,
    half_label,
)

CALENDAR = {"fy_end": "30 June", "halves": {"1H": "ends 31 December", "2H": "ends 30 June"}}
PERIOD_DATE, COMPARATOR_DATE, PRIOR_HALF_DATE = (12, 2025), (12, 2024), (6, 2025)

# row -> (31 Dec 25, 30 Jun 25, 31 Dec 24)
ROWS = {
    "Total operating income": (15000, 14400, 14100),
    "Underlying operating expenses": (6700, 6500, 6400),
    "Total operating expenses": (6900, 6600, 6400),
    "Loan impairment expense": (320, 400, 321),
    "Corporate tax expense": (2400, 2200, 2300),
    "Net interest income": (12700, 12100, 11900),
}
COLUMNS = ("31 Dec 25", "30 Jun 25", "31 Dec 24")


def _records() -> list[EvidenceRecord]:
    return [
        EvidenceRecord(
            id=f"ev-{i}",
            doc_id="BANK/1H26/profit_announcement",
            pdf_page=1,
            kind="table",
            quote=row,
            numbers=[
                NumberFact(label=f"{row} {column}", value=float(value), unit="$m")
                for column, value in zip(COLUMNS, values)
            ],
        )
        for i, (row, values) in enumerate(ROWS.items(), 1)
    ]


def _attribution(claims: list[tuple[str, float]]) -> Attribution:
    return Attribution(
        bank="BANK",
        metric="cash_earnings",
        period="1H26",
        comparator="1H25",
        basis="cash",
        movement=Movement(from_value=5100, to_value=5400, delta=300, unit="$m"),
        drivers=[
            DriverClaim(
                canonical=canonical,
                contribution=Contribution(value=value, unit="$m"),
                confidence=80,
            )
            for canonical, value in claims
        ],
        evidence_records=_records(),
    )


def _run(claims):
    return check_component_columns(
        _attribution(claims),
        PERIOD_DATE,
        COMPARATOR_DATE,
        PRIOR_HALF_DATE,
        half_label(PRIOR_HALF_DATE, CALENDAR),
    )


def test_comparator_column_deltas_pass():
    passed, failed = _run(
        [
            ("nii", 800),  # 12700 - 11900
            ("operating_expenses", -500),  # 6900 - 6400, signed as a cost
            ("credit_impairment_charge", 1),  # 320 vs 321
            ("tax_and_other", -100),  # 2400 - 2300
        ]
    )
    assert not failed
    assert passed == ["components_from_comparator_column"]


def test_half_on_half_component_fires():
    _, failed = _run([("nii", 600)])  # 12700 - 12100: the prior-half column
    assert len(failed) == 1
    assert "component_from_prior_half" in failed[0]
    assert "nii" in failed[0]


def test_prior_half_level_as_delta_fires():
    _, failed = _run([("credit_impairment_charge", -400)])  # the 30 Jun 25 LEVEL
    assert len(failed) == 1
    assert "credit_impairment_charge" in failed[0]


def test_nearby_pcp_delta_of_another_row_does_not_rescue():
    # 320 - 400 = -80 is the impairment half-on-half delta; the tax PCP delta
    # (100) sits within LEAK_TOL's $10m of it, but component deltas are exact,
    # so the loose movement tolerance must not hide the claim.
    _, failed = _run([("credit_impairment_charge", 80)])
    assert len(failed) == 1


def test_small_claims_and_missing_groups_stay_silent():
    # Below tolerance: the check cannot tell the pools apart.
    passed, failed = _run([("credit_impairment_charge", 1)])
    assert not failed
    # No prior-half column in evidence -> silent, never a guess.
    attribution = _attribution([("nii", 600)])
    for record in attribution.evidence_records:
        record.numbers = [n for n in record.numbers if "Jun" not in n.label]
    passed, failed = check_component_columns(
        attribution, PERIOD_DATE, COMPARATOR_DATE, PRIOR_HALF_DATE,
        half_label(PRIOR_HALF_DATE, CALENDAR),
    )
    assert not failed and not passed
