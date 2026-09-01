"""Review round 2: the deterministic layer.

Each test below carries the repro that found the defect. Two of them are
fixes of round-1 fixes, so they are written as the reviewer executed them:

- `_quote_numbers` read a PREFIX of any number with a glued unit ("$10,982m"
  came back as 10), so the citation cap certified a neighbouring driver with a
  small round value and capped the driver whose number the record printed.
- The citation cap compared magnitudes and never units, so the `0.0 $m` cell of
  a dollar row grounded a `+0.0 ppt` claim at confidence 90.
- A failed check lowered `attribution_confidence` alone. The calibration
  metrics read PER-DRIVER confidence, so every failed check was invisible to
  them, and the suite's one confidently-wrong claim sat at 85 under an answer
  that declared 40.
- Nothing validated that a ratio's LEVEL is ratio-sized, so an ROE submitted as
  1160 -> 1140 "ppt" passed movement arithmetic, reconciliation and the scale
  normaliser at once.
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
    CLAIM_CITATION_CAP,
    RATIO_LEVEL_CEILING,
    _quote_numbers,
    cap_unreconciled_drivers,
    cap_weakly_cited_claims,
    check_drivers_reconcile,
    check_ratio_level,
    convert_unit,
    movement_arithmetic_tolerance,
    normalize_unit,
    quote_prints,
    quote_states,
    reconcile_tolerance,
    settle_ratio_scale,
)


def _record(record_id: str, quote: str, numbers: list[tuple] = ()) -> EvidenceRecord:
    return EvidenceRecord(
        id=record_id,
        doc_id="CBA/1H26/profit_announcement",
        pdf_page=34,
        kind="table",
        quote=quote,
        numbers=[NumberFact(label=label, value=value, unit=unit) for label, value, unit in numbers],
    )


def _attribution(unit="$m", movement=(5132.0, 5445.0, 313.0), drivers=(), records=(),
                 residual=None, metric="cash_earnings") -> Attribution:
    return Attribution(
        bank="CBA",
        metric=metric,
        period="1H26",
        comparator="1H25",
        basis="cash",
        movement=Movement(
            from_value=movement[0], to_value=movement[1], delta=movement[2], unit=unit
        ),
        drivers=[
            DriverClaim(
                canonical=canonical,
                contribution=Contribution(value=value, unit=driver_unit or unit),
                confidence=confidence,
                evidence=list(evidence),
            )
            for canonical, value, confidence, evidence, driver_unit in drivers
        ],
        residual=None if residual is None else Contribution(value=residual, unit=unit),
        evidence_records=list(records),
    )


# ---------------------------------------------------------------------------
# 1. The glued-unit number (fix of a round-1 fix)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "quote,expected",
    [
        # The reviewer's own repro, verbatim. Before the fix these returned
        # [10.0], [], and [2.0].
        ("cash NPAT of $10,982m", [(10982.0, "$m")]),
        ("fell 5bps", [(5.0, "bps")]),
        ("$2.5bn buyback", [(2.5, "$bn")]),
        # Real quotes from the shipped set: 8% of them glue a digit to a letter.
        ("(-3bps)", [(3.0, "bps")]),
        ("(CET1 impact of -13bpts)", [(13.0, "bps")]),
        # A bank spells the money unit out as often as it glues it.
        ("a decrease of $1 million on the prior comparative period.", [(1.0, "$m")]),
        ("increased by 3% to $1,002.9 billion", [(3.0, "%"), (1002.9, "$bn")]),
        # A word that merely starts with a unit letter is not a unit. Round 3
        # then taught the pool the SPELLED-OUT ratio units, so this number now
        # carries the unit the sentence names rather than none: without it the
        # conversion table read a unitless 3, and any unit the model attached
        # to it was accepted.
        ("The margin fell 3 basis points", [(3.0, "bps")]),
        ("12 months at 31 December 2025", [(12.0, ""), (31.0, "")]),
    ],
)
def test_a_number_keeps_its_glued_unit_and_its_digits(quote, expected):
    """The trailing lookahead failed on a glued unit, so the engine backtracked
    and the pool took a PREFIX of the number."""
    assert _quote_numbers(quote) == expected


def test_a_bare_year_is_not_a_magnitude():
    """A period TAG was already excluded; a sentence spells the year out."""
    assert (2025.0, "") not in _quote_numbers("at 31 December 2025 the ratio was 12.2%")


def test_the_citation_cap_is_not_inverted_by_a_digit_prefix():
    """One record, both directions of the defect at once.

    The quote prints 10,982. Before the fix the driver claiming +10982 was
    CAPPED (the pool held 10, not 10982) and a neighbour claiming +10 was
    certified at 95 by that same prefix.
    """
    quote = "Cash net profit after tax was $10,982m, up 7% on the prior year."
    assert quote_states(quote, 10982, "$m") is True
    assert quote_states(quote, 10, "$m") is False


# ---------------------------------------------------------------------------
# 2. A fatal check reaches the drivers
# ---------------------------------------------------------------------------


def test_a_bridge_that_does_not_close_caps_every_quantified_driver():
    """The live confidently-wrong claim.

    CBA 1H26 cash earnings failed drivers_reconcile, the answer declared 40,
    and `credit_impairment_charge -1.0` shipped at 85 against a gold of +1.
    A bridge that does not close proves one contribution is wrong without
    saying which, so none of them may claim near-certainty.
    """
    attribution = _attribution(
        drivers=[
            ("nii", 761.0, 85, ["ev-1"], None),
            ("credit_impairment_charge", -1.0, 85, ["ev-1"], None),
        ]
    )
    capped = cap_unreconciled_drivers(
        attribution, ["drivers_reconcile (drivers +760.0 + residual +0.0 != delta +313.0, tol 1.0)"]
    )
    assert len(capped) == 2
    assert [d.confidence for d in attribution.drivers] == [CLAIM_CITATION_CAP, CLAIM_CITATION_CAP]
    assert any("unreconciled_bridge_cap_80" in d.checks_passed for d in attribution.drivers)


def test_an_unrelated_failed_check_leaves_the_drivers_alone():
    """The cap names the failures that condemn the WHOLE table, not every one."""
    attribution = _attribution(drivers=[("nii", 313.0, 90, ["ev-1"], None)])
    assert cap_unreconciled_drivers(attribution, ["movement_from_variant (…)"]) == []
    assert attribution.drivers[0].confidence == 90


def test_a_driver_already_at_or_below_the_cap_is_left_alone():
    attribution = _attribution(drivers=[("nii", 313.0, 60, ["ev-1"], None)])
    cap_unreconciled_drivers(attribution, ["drivers_reconcile (…)"])
    assert attribution.drivers[0].confidence == 60


# ---------------------------------------------------------------------------
# 3. The citation cap binds the unit
# ---------------------------------------------------------------------------


def test_a_dollar_cell_does_not_ground_a_percentage_point_claim():
    """The shipped CBA 1H26 cost-to-income record, exactly as it was saved.

    `notable_items +0.0 ppt` kept confidence 90 because a cited record carried
    a NumberFact of `0.0 $m`. A zero in another unit grounds nothing, and a
    zero-valued claim is the easiest of all to ground by accident.
    """
    record = _record(
        "ev-16",
        "Restructuring and notable items",
        [("Notable items 31 Dec 25", -170.0, "$m"),
         ("Notable items 30 Jun 25", -130.0, "$m"),
         ("Notable items 31 Dec 24", 0.0, "$m")],
    )
    attribution = _attribution(
        unit="ppt",
        movement=(45.7, 45.5, -0.2),
        metric="cti",
        drivers=[("notable_items", 0.0, 90, ["ev-16"], None)],
        records=[record],
    )
    assert cap_weakly_cited_claims(attribution) == ["notable_items +0 ppt"]
    assert attribution.drivers[0].confidence == CLAIM_CITATION_CAP


def test_basis_points_ground_the_same_movement_in_points():
    """A -20 bps fact grounds -0.2 ppt, and never -20 ppt."""
    record = _record("ev-1", "Cash return on equity 11.4% 11.6% (20 bps)",
                     [("ROE change", -20.0, "bps")])
    grounded = _attribution(
        unit="ppt", movement=(11.6, 11.4, -0.2), metric="roe",
        drivers=[("earnings", -0.2, 95, ["ev-1"], None)], records=[record],
    )
    assert cap_weakly_cited_claims(grounded) == []
    at_the_wrong_scale = _attribution(
        unit="ppt", movement=(11.6, 11.4, -0.2), metric="roe",
        drivers=[("earnings", -20.0, 95, ["ev-1"], None)], records=[record],
    )
    assert at_the_wrong_scale.drivers[0].canonical in cap_weakly_cited_claims(
        at_the_wrong_scale
    )[0]


def test_a_number_with_no_unit_grounds_nothing():
    """Absent unit is no evidence either way, in either direction."""
    assert convert_unit(5.0, "", "$m") is None
    assert convert_unit(5.0, "$m", "") is None
    assert convert_unit(5.0, "bps", "$m") is None
    assert convert_unit(2.5, "$bn", "$m") == 2500.0


def test_a_bare_number_needs_the_quote_to_name_its_unit_family():
    """A table row prints its unit in the table header, not in the row."""
    assert quote_states("Loan impairment expense was $319 million.", 319, "$m") is True
    assert quote_states("Cost to income ratio 45.7 45.9", 45.7, "$m") is False


# ---------------------------------------------------------------------------
# 4. A ratio's level must be ratio-sized
# ---------------------------------------------------------------------------


def test_a_ratio_level_in_basis_points_fails_the_check():
    """The NAB FY25 ROE submission: the RIGHT row, read at the wrong scale.

    1160 + -20 = 1140 is self-consistent, so movement arithmetic passed; the
    drivers reconciled at the same wrong scale; and settle_identity_scale needs
    a contribution larger than the level, which nothing was.
    """
    failed = check_ratio_level(Movement(from_value=1160.0, to_value=1140.0, delta=-20.0, unit="ppt"))[1]
    assert failed and failed[0].startswith("movement_level_not_ratio_sized")


def test_the_largest_real_ratio_in_the_saved_set_passes():
    """Westpac's FY25 cost-to-income ratio of 53.04 is the largest legitimate
    level the eval corpus holds; the ceiling sits 3.8x above it."""
    assert check_ratio_level(
        Movement(from_value=53.04, to_value=51.8, delta=-1.24, unit="ppt")
    )[1] == []
    assert RATIO_LEVEL_CEILING == 200.0


def test_a_money_movement_is_never_asked_to_be_ratio_sized():
    assert check_ratio_level(
        Movement(from_value=5132.0, to_value=5445.0, delta=313.0, unit="$m")
    ) == ([], [])


def test_the_ratio_corrector_restates_endpoints_the_evidence_prints_as_percent():
    """The mirror of the percent-to-bps lift, and self-evidencing the same way."""
    record = _record("ev-1", "Cash return on equity 11.4% 11.6% (20 bps)",
                     [("ROE FY25", 11.4, "%"), ("ROE FY24", 11.6, "%")])
    attribution = _attribution(
        unit="ppt", movement=(1160.0, 1140.0, -20.0), metric="roe", records=[record],
    )
    # Round 3: the gate is the METRIC's unit, which the taxonomy fixes, and
    # never the movement's unit, which the model writes.
    note = settle_ratio_scale(attribution, "ppt")
    assert note is not None
    assert (attribution.movement.from_value, attribution.movement.to_value) == (11.6, 11.4)
    assert attribution.movement.delta == -0.2
    assert check_ratio_level(attribution.movement)[1] == []


def test_the_ratio_corrector_stays_silent_without_percent_evidence():
    """A movement already in points cannot pass the test: no page prints an
    ROE of 0.116 per cent."""
    record = _record("ev-1", "Return on equity 11.6%", [("ROE", 11.6, "%")])
    attribution = _attribution(
        unit="ppt", movement=(11.6, 11.4, -0.2), metric="roe", records=[record]
    )
    assert settle_ratio_scale(attribution, "ppt") is None
    assert attribution.movement.from_value == 11.6


# ---------------------------------------------------------------------------
# 6. The reconciliation SUM is unit-typed, not only its tolerance
# ---------------------------------------------------------------------------


def test_a_basis_point_bar_no_longer_reconciles_a_dollar_bridge():
    """Round 1 made the tolerance unit-typed and left the addition unit-blind."""
    attribution = _attribution(
        drivers=[("nii", 310.0, 85, ["ev-1"], None), ("mix", 3.0, 85, ["ev-1"], "bps")]
    )
    passed, failed = check_drivers_reconcile(attribution)
    assert passed == []
    assert any(f.startswith("drivers_unit_mismatch") for f in failed)
    assert any(f.startswith("drivers_reconcile") for f in failed)


# ---------------------------------------------------------------------------
# 7. One spelling per unit, everywhere a tolerance is keyed
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "raw,canonical",
    [("PPT", "ppt"), ("ppts", "ppt"), ("bpts", "bps"), (" $ m", "$m"), ("$bn", "$bn"),
     ("$b", "$bn"), ("cents", "cents"), ("ratio", "ratio"), (None, "")],
)
def test_unit_spellings_canonicalise(raw, canonical):
    assert normalize_unit(raw) == canonical


def test_an_uppercase_unit_gets_its_own_tolerance():
    """`unit="PPT"` took the default 1.0, so drivers totalling +0.6 passed a
    -0.2 movement despite a 0.8 ppt gap."""
    attribution = _attribution(unit="PPT", movement=(45.7, 45.5, -0.2), metric="cti")
    assert reconcile_tolerance(attribution) == 0.1
    assert movement_arithmetic_tolerance("PPT") == 0.1


# ---------------------------------------------------------------------------
# 8. A submitted NumberFact must be printed by the quote it sits under
# ---------------------------------------------------------------------------


def test_a_fact_the_quote_does_not_print_is_not_evidence():
    quote = "Operating expenses increased 9% to $11,916 million."
    assert quote_prints(quote, 11916, "$m") is True
    assert quote_prints(quote, 9, "%") is True
    assert quote_prints(quote, 150, "$m") is False
