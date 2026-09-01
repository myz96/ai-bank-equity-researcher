"""Unit-typed tolerances (review round 1, items 1, 2 and 0).

Every numeric check in validate.py compared a gap against a constant that was
calibrated in BASIS POINTS, whatever unit the number was actually stated in.
A tolerance without its unit is not a tolerance:

- 1.0 is a rounding step in bps and five times the whole movement in ppt. The
  shipped CBA FY26 cost-to-income artifact carried drivers summing to 0.0 ppt
  against a -0.2 ppt movement and PASSED drivers_reconcile.
- walk_sum_tolerance returned the same bps-calibrated number for a ppt walk,
  so such a walk could never fail its own sum check.
- check_movement allowed 0.51 on a ppt movement, which is larger than most
  ratio movements the eval set contains.

The third case here is the weak-citation gate: a quantified claim whose cited
records neither print its value nor state it in words is the model's own
arithmetic, so it is capped like any computed delta.
"""

from __future__ import annotations

import pytest

from bank_equity_researcher.validation.schema import (
    Attribution,
    Contribution,
    DriverClaim,
    EvidenceRecord,
    Movement,
    NumberFact,
)
from bank_equity_researcher.validation.validate import (
    RATIO_TOL_PPT,
    WALK_SUM_TOL_PRESENTATION,
    cap_weakly_cited_claims,
    check_drivers_reconcile,
    check_movement,
    check_walk,
    reconcile_tolerance,
    walk_sum_tolerance,
)


def _attribution(unit: str, delta: float, contributions: list[float], **kw) -> Attribution:
    return Attribution(
        bank="CBA",
        metric=kw.pop("metric", "cti"),
        period="FY26",
        comparator="FY25",
        basis="cash",
        movement=Movement(
            from_value=kw.pop("from_value", 45.7),
            to_value=kw.pop("to_value", 45.5),
            delta=delta,
            unit=unit,
        ),
        drivers=[
            DriverClaim(
                canonical=f"d{i}",
                contribution=Contribution(value=v, unit=unit),
                confidence=85,
                evidence=["ev-1"],
            )
            for i, v in enumerate(contributions)
        ],
        **kw,
    )


# --------------------------------------------------------------------------
# Item 1: reconcile_tolerance is unit-typed
# --------------------------------------------------------------------------


def test_ppt_drivers_that_sum_to_zero_fail_a_ppt_movement():
    """The shipped cba-cti-fy26-vs-fy25-cheap artifact, replayed.

    Drivers of -0.12 and +0.12 ppt sum to 0.0 against a -0.2 ppt movement.
    Under the old flat 1.0 the whole movement was smaller than the tolerance,
    so the check could not see a bridge that explains nothing.
    """
    attribution = _attribution("ppt", -0.2, [-0.12, 0.12, 0.0])
    assert reconcile_tolerance(attribution) == RATIO_TOL_PPT
    passed, failed = check_drivers_reconcile(attribution)
    assert passed == []
    assert any(f.startswith("drivers_reconcile") for f in failed)


def test_ppt_drivers_that_do_reconcile_still_pass():
    attribution = _attribution("ppt", -0.2, [-0.15, -0.05])
    assert check_drivers_reconcile(attribution)[0] == ["drivers_reconcile"]


@pytest.mark.parametrize("unit,expected", [("bps", 1.0), ("ppt", RATIO_TOL_PPT), ("$m", 1.0)])
def test_reconcile_tolerance_follows_the_unit(unit, expected):
    assert reconcile_tolerance(_attribution(unit, 1.0, [1.0])) == expected


def test_presentation_lift_applies_to_bps_only():
    """A slide rounds a ratio to 0.1%, and the metric is stated in bps there.

    The lift is a quantity in basis points, so a ppt or $m answer never earns
    it: 10.0 ppt is a hundred times any ratio movement in the eval set.
    """
    slide = [
        EvidenceRecord(
            id="ev-1",
            doc_id="CBA/FY26/results_presentation",
            pdf_page=32,
            kind="walk_vision",
            quote="[walk chart] CET1",
        )
    ]
    bps = _attribution("bps", 1.0, [1.0], evidence_records=slide, metric="cet1")
    assert reconcile_tolerance(bps) == WALK_SUM_TOL_PRESENTATION
    ppt = _attribution("ppt", 1.0, [1.0], evidence_records=slide)
    assert reconcile_tolerance(ppt) == RATIO_TOL_PPT
    money = _attribution("$m", 1.0, [1.0], evidence_records=slide, metric="cash_earnings")
    assert reconcile_tolerance(money) == 1.0


# --------------------------------------------------------------------------
# Item 2: walk_sum_tolerance is unit-typed
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "doc_type,unit,expected",
    [
        ("profit_announcement", "bps", 1.0),
        ("results_presentation", "bps", WALK_SUM_TOL_PRESENTATION),
        ("profit_announcement", "ppt", RATIO_TOL_PPT),
        # The presentation lift is a bps quantity, so a ppt walk keeps the
        # ratio tolerance however the walk was published.
        ("results_presentation", "ppt", RATIO_TOL_PPT),
        ("profit_announcement", "$m", 1.0),
        ("results_presentation", "$m", 1.0),
    ],
)
def test_walk_sum_tolerance_follows_the_unit(doc_type, unit, expected):
    assert walk_sum_tolerance(doc_type, unit) == expected


def test_a_ppt_walk_can_fail_its_sum_check():
    """Bars summing 0.5 ppt away from the endpoint gap must fail.

    Under the bps-calibrated tolerance the same walk passed on a presentation
    (10.0) and on a results book (1.0), so a ppt walk had no sum check at all.
    """
    walk = {"start_bps": 45.7, "bars": [{"label": "a", "bps": 0.3}], "end_bps": 45.5}
    assert check_walk(walk, "results_presentation", "ppt")[1]
    assert check_walk(walk, "profit_announcement", "ppt")[1]
    # The same shape in basis points is inside the rounding of a slide.
    bps_walk = {"start_bps": 205.0, "bars": [{"label": "a", "bps": 3.0}], "end_bps": 202.0}
    assert check_walk(bps_walk, "results_presentation", "bps")[0] == ["walk_sum"]


def test_walk_sum_tolerance_keeps_its_bps_default():
    """check_walk's callers pass the metric unit; the default stays bps."""
    assert walk_sum_tolerance("profit_announcement") == 1.0
    assert walk_sum_tolerance("results_presentation") == WALK_SUM_TOL_PRESENTATION


# --------------------------------------------------------------------------
# check_movement's flat 0.51 (item 1, the author normaliser's share)
# --------------------------------------------------------------------------


def test_movement_arithmetic_is_unit_typed():
    """0.51 ppt is larger than most ratio movements the eval set contains."""
    wrong = Movement(from_value=45.7, to_value=45.5, delta=-0.5, unit="ppt")
    assert check_movement(wrong)[1]
    right = Movement(from_value=45.7, to_value=45.5, delta=-0.2, unit="ppt")
    assert check_movement(right)[0] == ["movement_arithmetic"]
    # Basis points keep the tolerance they were calibrated with.
    bps = Movement(from_value=205.0, to_value=202.0, delta=-3.0, unit="bps")
    assert check_movement(bps)[0] == ["movement_arithmetic"]


# --------------------------------------------------------------------------
# Item 0: the weak-citation cap, both shells
# --------------------------------------------------------------------------


def _cited(numbers: list[NumberFact], quote: str = "[walk chart] Loan impairment expense") -> list:
    return [
        EvidenceRecord(
            id="ev-1",
            doc_id="CBA/FY26/results_presentation",
            pdf_page=29,
            kind="walk_vision",
            quote=quote,
            numbers=numbers,
        )
    ]


def test_claim_whose_records_do_not_state_it_is_capped():
    """The shipped cba-impairment-fy26-vs-fy25-agentic-cheap artifact.

    +150 / -17 / -71 $m shipped at confidence 85 citing two chart reads whose
    numbers were 6.2, -5.6, 0.0, -8.5 and -1.4. The records resolved, so the
    evidence gate passed them; nothing asked whether they said 150.
    """
    attribution = _attribution(
        "$m", 62.0, [150.0, -17.0, -71.0],
        metric="impairment",
        evidence_records=_cited([NumberFact(label="Loan impairment", value=-8.5, unit="bps")]),
    )
    capped = cap_weakly_cited_claims(attribution)
    assert len(capped) == 3
    assert [d.confidence for d in attribution.drivers] == [80, 80, 80]
    assert all("computed_delta_cap_80" in d.checks_passed for d in attribution.drivers)
    assert any("150" in limitation for limitation in attribution.limitations)


def test_a_record_that_prints_the_number_keeps_the_confidence():
    attribution = _attribution(
        "$m", 62.0, [150.0],
        metric="impairment",
        evidence_records=_cited([NumberFact(label="Collective provision", value=150.0, unit="$m")]),
    )
    assert cap_weakly_cited_claims(attribution) == []
    assert attribution.drivers[0].confidence == 85


def test_a_quote_that_states_the_movement_in_words_keeps_the_confidence():
    """Prose evidence carries its number in the sentence, not in a NumberFact.

    The CBA FY26 NIM record "Decreased margin by 5 basis points" grounds a
    -5 bps claim exactly as well as an extracted bar does.
    """
    attribution = _attribution(
        "bps", -3.0, [-5.0],
        metric="nim",
        evidence_records=[
            EvidenceRecord(
                id="ev-1",
                doc_id="CBA/FY26/profit_announcement",
                pdf_page=12,
                quote="Asset pricing: Decreased margin by 5 basis points driven by home lending.",
            )
        ],
    )
    assert cap_weakly_cited_claims(attribution) == []
    assert attribution.drivers[0].confidence == 85


def test_a_period_tag_is_not_a_number():
    """"FY25" must not ground a claim of +25, nor "1H26" a claim of +26."""
    attribution = _attribution(
        "$m", 62.0, [25.0],
        metric="impairment",
        evidence_records=_cited([], quote="[walk chart] Impairment: FY25 72.6 -> FY26 78.8"),
    )
    assert len(cap_weakly_cited_claims(attribution)) == 1
    assert attribution.drivers[0].confidence == 80


def test_the_cap_never_raises_a_confidence():
    attribution = _attribution("$m", 62.0, [150.0], metric="impairment", evidence_records=_cited([]))
    attribution.drivers[0].confidence = 40
    assert cap_weakly_cited_claims(attribution) == []
    assert attribution.drivers[0].confidence == 40


def test_an_unquantified_driver_is_untouched():
    attribution = _attribution("$m", 62.0, [], metric="impairment", evidence_records=_cited([]))
    attribution.drivers.append(DriverClaim(canonical="narrative", confidence=90, evidence=["ev-1"]))
    assert cap_weakly_cited_claims(attribution) == []
    assert attribution.drivers[0].confidence == 90
