"""Movement, basis and sign normalisers (ticket 27).

Two defects the WBC FY25 cases exposed:

- The impairment charge arrived re-signed. Westpac prints the line inside the
  P&L, where an expense is bracketed, so the answer reported -537 -> -424,
  delta +113 for a charge that FELL by $113m.
- The answer read "Return on average ordinary equity" when Westpac headlines
  ROTE ex Notable Items one line below. The registry already named the row.

The normalisers live in validation/validate.py beside the checks that read
their output.
"""

from __future__ import annotations

import pytest

from bank_equity_researcher.taxonomy import TAXONOMY
from bank_equity_researcher.validation.schema import (
    Attribution,
    Contribution,
    DriverClaim,
    EvidenceRecord,
    Movement,
    NumberFact,
)
from bank_equity_researcher.validation.validate import (
    RATIO_LEVEL_CEILING,
    _settle_basis,
    check_drivers_reconcile,
    check_movement_basis,
    check_movement_variant,
    check_ratio_level,
    drop_off_unit_contributions,
    primary_basis,
    settle_charge_sign,
    settle_identity_scale,
    settle_ratio_scale,
)

IMPAIRMENT = TAXONOMY["impairment"]
CASH_EARNINGS = TAXONOMY["cash_earnings"]


@pytest.mark.parametrize(
    "name,why,taxonomy,movement,expected",
    [
        (
            "bracketed charge pair",
            "WBC FY25: (424) against (537) is a charge that fell by 113",
            IMPAIRMENT,
            {"from_value": -537.0, "to_value": -424.0, "delta": 113.0},
            (537.0, 424.0, -113.0),
        ),
        (
            "already positive",
            "CBA and NAB print the charge positive; nothing to re-sign",
            IMPAIRMENT,
            {"from_value": 726.0, "to_value": 788.0, "delta": 62.0},
            (726.0, 788.0, 62.0),
        ),
        (
            "charge then benefit",
            "a mixed pair is one charge and one benefit, so the signs are real",
            IMPAIRMENT,
            {"from_value": 320.0, "to_value": -40.0, "delta": -360.0},
            (320.0, -40.0, -360.0),
        ),
        (
            "metric with no charge convention",
            "cash earnings carries no sign_convention, so negatives stand",
            CASH_EARNINGS,
            {"from_value": -100.0, "to_value": -50.0, "delta": 50.0},
            (-100.0, -50.0, 50.0),
        ),
    ],
)
def test_settle_charge_sign(name, why, taxonomy, movement, expected):
    reply: dict = {}
    settled = settle_charge_sign(dict(movement), taxonomy, reply)
    assert (settled["from_value"], settled["to_value"], settled["delta"]) == expected, why
    re_signed = settled["from_value"] != movement["from_value"]
    assert bool(reply.get("limitations")) is re_signed, "a re-sign is always declared"


def test_impairment_carries_the_charge_convention():
    """The flag lives in the taxonomy, so the normalisers stay bank-agnostic."""
    assert IMPAIRMENT["sign_convention"] == "positive_charge"
    assert "sign_convention" not in CASH_EARNINGS


# ---------------------------------------------------------------------------
# The primary-basis check on the movement citation
# ---------------------------------------------------------------------------

CBA_LABEL = "Operating expenses to total operating income"
NAB_LABEL = "CTI - cost to income ratio"
WBC_ROE_LABEL = (
    "ROTE ex Notable Items (return on average tangible equity, excluding Notable Items) "
    "— printed under the 'Shareholder value - excluding Notable Items' block"
)


def _movement(metric, source, basis="cash"):
    return Attribution(
        bank="BANK",
        metric=metric,
        period="FY25",
        comparator="FY24",
        basis=basis,
        movement=Movement(from_value=46.5, to_value=47.3, delta=0.8, unit="ppt"),
        movement_source=source,
    )


@pytest.mark.parametrize(
    "name,why,metric,source,basis,label,fires",
    [
        (
            "statutory block at a cash bank",
            "NAB FY25 p15 prints the CTI row under both blocks; the statutory one is wrong",
            "cti",
            "row 'Cost to income ratio statutory Sep 25', column Sep 24 -> column Sep 25",
            "cash",
            NAB_LABEL,
            True,
        ),
        (
            "cash block at a cash bank",
            "the primary basis is never a variant",
            "cti",
            "row 'Cost to income ratio cash', column Sep 24 -> column Sep 25",
            "cash",
            NAB_LABEL,
            False,
        ),
        (
            "no basis word at all",
            "an unlabelled row takes the primary basis, so there is nothing to fail",
            "cti",
            "row 'Operating expenses to total operating income (%)', column FY25 -> column FY26",
            "cash",
            CBA_LABEL,
            False,
        ),
        (
            "ex-Notables row at a cash bank",
            "Westpac's basis is not CBA's; an ex-Notables row is a variant here",
            "cti",
            "row 'Cost to income ratio ex Notable Items', column FY25 -> column FY26",
            "cash",
            CBA_LABEL,
            True,
        ),
        (
            "ex-Notables row at an ex-Notables bank",
            "Westpac reports on that basis, so its own row is the headline row",
            "roe",
            "row 'ROTE ex Notable Items', column FY24 -> column FY25",
            "ex_notables",
            WBC_ROE_LABEL,
            False,
        ),
        (
            "statutory row at an ex-Notables bank",
            "the statutory ROTE sits one block above the headline row",
            "roe",
            "row 'ROTE, statutory basis', column FY24 -> column FY25",
            "ex_notables",
            WBC_ROE_LABEL,
            True,
        ),
        (
            "CET1 is skipped",
            "a regulatory capital ratio has no cash / statutory / ex-Notables basis",
            "cet1",
            "row 'CET1 capital ratio, statutory', column FY24 -> column FY25",
            "cash",
            None,
            False,
        ),
    ],
)
def test_check_movement_basis(name, why, metric, source, basis, label, fires):
    """The answer declares the bank's own basis; only the citation is on trial."""
    attribution = _movement(metric, source, basis=basis)
    passed, failed = check_movement_basis(attribution, basis, label)
    assert bool(failed) is fires, why
    assert bool(passed) is not fires or metric == "cet1"


@pytest.mark.parametrize(
    "name,why,declared,primary,label,fires",
    [
        (
            "statutory declared at an ex-Notables bank",
            "WBC FY25 cash earnings cited a row with no basis word and declared statutory",
            "statutory",
            "ex_notables",
            None,
            True,
        ),
        (
            "primary basis declared",
            "the ordinary case",
            "ex_notables",
            "ex_notables",
            None,
            False,
        ),
        (
            "non-primary basis the headline row itself names",
            "a metric whose headline row really is on another basis is exempt",
            "ex_notables",
            "cash",
            "Cost to income ratio ex Notable Items",
            False,
        ),
    ],
)
def test_check_movement_basis_reads_the_declared_basis(name, why, declared, primary, label, fires):
    attribution = _movement("cash_earnings", "row 'Net profit', column FY24 -> column FY25",
                            basis=declared)
    passed, failed = check_movement_basis(attribution, primary, label)
    assert bool(failed) is fires, why
    assert bool(passed) is not fires


def test_check_movement_basis_is_silent_without_a_registry_basis():
    """The cold path for an unseen bank whose registry is absent."""
    attribution = _movement("cti", "row 'Cost to income ratio statutory', column A -> column B")
    assert check_movement_basis(attribution, None, None) == ([], [])


# ---------------------------------------------------------------------------
# One spelling for a hyphenated variant word
# ---------------------------------------------------------------------------

WBC_CTI_LABEL = "Expense to income ratio, ex Notable Items (excluding Notable Items)"


@pytest.mark.parametrize(
    "name,why,metric,source,label,fires",
    [
        (
            "hyphen in the citation, space in the label",
            "the author wrote ROTE ex-notables; the registry spells it ex Notable Items",
            "roe",
            "row 'ROTE ex-notables', column FY24 -> column FY25",
            WBC_ROE_LABEL,
            False,
        ),
        (
            "hyphenated variant at a bank whose headline row is not that variant",
            "CBA's headline CTI row carries no ex-Notables wording, so the check still fires",
            "cti",
            "row 'Cost-to-income ratio ex-notable items', column FY25 -> column FY26",
            CBA_LABEL,
            True,
        ),
        (
            "underlying still fires",
            "the CBA 1H26 case that motivated the check must keep failing",
            "cti",
            "row 'Underlying operating expenses to underlying operating income', column A -> B",
            CBA_LABEL,
            True,
        ),
        (
            "Westpac's own cti row passes",
            "the headline expense-to-income row IS the ex-Notables one",
            "cti",
            "row 'Cost-to-income ratio (ex Notable Items)', column FY24 -> column FY25",
            WBC_CTI_LABEL,
            False,
        ),
    ],
)
def test_variant_words_ignore_hyphens(name, why, metric, source, label, fires):
    passed, failed = check_movement_variant(_movement(metric, source), label)
    assert bool(failed) is fires, why
    assert bool(passed) is not fires


# ---------------------------------------------------------------------------
# The ratio-identity scale normaliser (ticket 27)
#
# ROE and CTI derive their level-1 split from an identity. The growth rate
# enters that identity as a FRACTION, and a dollar movement enters it divided
# by average equity. An answer that feeds a rate printed in per cent straight
# in states the split 100 times too large: the WBC FY25 run split a -0.24 ppt
# movement into -23.76 and +0.56 ppt, and the CBA FY21 run split a +1.3 ppt
# movement into +146 and -16. Both movements were CORRECT and both shipped
# capped at 40 behind a failed drivers_reconcile.
#
# The normaliser must not become a way of making any failing bridge close, so
# each row below names the guard it exercises.
# ---------------------------------------------------------------------------


def _identity(metric, from_value, to_value, contributions, residual=None, unit="ppt"):
    return Attribution(
        bank="BANK",
        metric=metric,
        period="FY25",
        comparator="FY24",
        basis="cash",
        movement=Movement(
            from_value=from_value,
            to_value=to_value,
            delta=round(to_value - from_value, 2),
            unit=unit,
        ),
        drivers=[
            DriverClaim(
                canonical=canonical,
                contribution=Contribution(value=value, unit=contribution_unit),
                confidence=80,
                evidence=["ev-1"],
            )
            for canonical, value, contribution_unit in contributions
        ],
        residual=None if residual is None else Contribution(value=residual, unit=unit),
        evidence_records=[
            EvidenceRecord(
                id="ev-1",
                doc_id="BANK/FY25/results_announcement",
                pdf_page=9,
                quote="Return on equity 10.97 11.21",
            )
        ],
    )


def test_identity_scale_restates_the_wbc_roe_split():
    """The case that motivated the fix: a correct movement, a 100x split."""
    attribution = _identity(
        "roe", 11.21, 10.97,
        [("earnings_effect", -23.76, "ppt"), ("equity_effect", 0.56, "ppt")],
        residual=-0.04,
    )
    assert check_drivers_reconcile(attribution)[1], "the split must fail before the fix"
    note = settle_identity_scale(attribution, TAXONOMY["roe"]["method"])
    assert note is not None
    values = [d.contribution.value for d in attribution.drivers]
    assert values == [-0.2376, 0.0056]
    assert all("identity_scale_normalised" in d.checks_passed for d in attribution.drivers)
    assert check_drivers_reconcile(attribution)[0] == ["drivers_reconcile"]
    assert not check_drivers_reconcile(attribution)[1]
    assert note in attribution.limitations


def test_identity_scale_rescales_a_residual_written_on_the_same_scale():
    """The residual is part of the identity, so it moves with it — but only
    when the identity closes that way."""
    attribution = _identity(
        "roe", 10.2, 11.5,
        [("earnings_effect", 146.0, "ppt"), ("equity_effect", -20.0, "ppt")],
        residual=4.0,
    )
    assert settle_identity_scale(attribution, TAXONOMY["roe"]["method"]) is not None
    assert [d.contribution.value for d in attribution.drivers] == [1.46, -0.2]
    assert attribution.residual.value == 0.04


def test_identity_scale_leaves_a_split_that_is_already_on_scale():
    """The normaliser fires on the symptom, never on a passing answer."""
    attribution = _identity(
        "roe", 12.5, 13.0,
        [("earnings_effect", 0.94, "ppt"), ("equity_effect", -0.44, "ppt")],
        residual=0.0,
    )
    assert settle_identity_scale(attribution, TAXONOMY["roe"]["method"]) is None
    assert [d.contribution.value for d in attribution.drivers] == [0.94, -0.44]
    assert attribution.limitations == []


def test_identity_scale_does_not_rescue_a_wrong_split():
    """A split written on the RIGHT scale and simply wrong stays wrong.

    Without the guard, dividing any failing split by 100 would drive its sum to
    nearly zero and the loose ppt tolerance would then accept it, so every
    reconciliation failure on a ratio metric would disappear.
    """
    attribution = _identity(
        "roe", 11.21, 10.97,
        [("earnings_effect", -5.0, "ppt"), ("equity_effect", 1.0, "ppt")],
        residual=0.0,
    )
    assert settle_identity_scale(attribution, TAXONOMY["roe"]["method"]) is None
    assert [d.contribution.value for d in attribution.drivers] == [-5.0, 1.0]
    assert check_drivers_reconcile(attribution)[1], "the check keeps its teeth"


def test_identity_scale_ignores_a_bridge_metric():
    """Only a two-level ARITHMETIC identity is restated; a bridge's components
    are read from tables, so a 100x sum there is a reading error, not a scale."""
    attribution = _identity(
        "cash_earnings", 10000.0, 10200.0,
        [("nii", 40000.0, "$m"), ("operating_expenses", -20000.0, "$m")],
        residual=0.0,
        unit="$m",
    )
    assert settle_identity_scale(attribution, TAXONOMY["cash_earnings"]["method"]) is None
    assert [d.contribution.value for d in attribution.drivers] == [40000.0, -20000.0]


def test_identity_scale_ignores_a_split_stated_in_another_unit():
    """A contribution left in dollars is a different defect: converting it needs
    the identity's denominator, which this normaliser does not have."""
    attribution = _identity(
        "roe", 11.21, 10.97,
        [("earnings_effect", -442.0, "$m"), ("equity_effect", 0.56, "ppt")],
        residual=0.0,
    )
    assert settle_identity_scale(attribution, TAXONOMY["roe"]["method"]) is None


# ---------------------------------------------------------------------------
# The off-unit contribution drop
#
# A contribution is a share of THIS movement, so it is stated in the movement's
# own unit. research_agent.build_attribution calls the drop. The end-to-end
# case lives in test_research_agent.py; this is the rule on its own.
# ---------------------------------------------------------------------------


def test_a_contribution_in_another_unit_stops_being_a_contribution():
    drivers = [
        {"canonical": "nii", "contribution": {"value": 310, "unit": "$m"}, "confidence": 90},
        {"canonical": "mix", "contribution": {"value": -3, "unit": "bps"}, "confidence": 90},
    ]
    dropped = drop_off_unit_contributions(drivers, "$m")
    assert drivers[0]["contribution"] == {"value": 310, "unit": "$m"}
    assert drivers[1]["contribution"] is None
    assert len(dropped) == 1
    assert "not the movement's unit" in dropped[0]
    # Ticket 33 wave 1 deleted the hardcoded fall to 60: the drop fired on 0 of
    # the 90 saved artifacts, so the override cited no run. The drop stays.
    assert drivers[1]["confidence"] == 90


def test_a_unit_spelling_difference_is_not_an_off_unit_contribution():
    """"$M" and "$m" are one unit; the guard reads the canonical spelling."""
    drivers = [{"canonical": "nii", "contribution": {"value": 313, "unit": "$M"},
                "confidence": 90}]
    assert drop_off_unit_contributions(drivers, "$m") == []
    assert drivers[0]["contribution"] is not None


# ---------------------------------------------------------------------------
# A registry that knows no basis settles none
# ---------------------------------------------------------------------------


def test_a_measures_less_registry_settles_no_basis():
    """A skeleton registry must not rewrite the agent's declared basis.

    primary_basis defaulted to "cash" even for a registry with no measures
    block, so _settle_basis rewrote a declared "statutory" to "cash" and its
    limitation claimed "the registry names cash as the bank's headline basis"
    — a false claim. MQG (statutory NPAT, skeleton registry) hit exactly this.
    """
    assert primary_basis({}) is None
    assert primary_basis({"measures": {}}) is None
    reply: dict = {}
    assert _settle_basis("statutory", {}, [], reply) == "statutory"
    assert "limitations" not in reply


def test_a_registry_with_measures_still_normalises_an_unprinted_basis():
    registry = {"measures": {"core_profit": "cash earnings"}}
    reply: dict = {}
    assert _settle_basis("statutory", registry, [], reply) == "cash"
    assert any("Basis normalised" in x for x in reply["limitations"])


def test_no_declared_basis_and_no_registry_knowledge_says_as_reported():
    """An empty declaration used to fall to a hardcoded "cash".

    MQG reports statutory NPAT and its skeleton registry names no basis, so
    "cash" was invented knowledge shipped without a limitation. "as reported"
    states what is actually known: nothing was declared, nothing overrode it.
    """
    reply: dict = {}
    assert _settle_basis(None, {}, [], reply) == "as reported"
    assert _settle_basis("  ", {}, [], reply) == "as reported"
    assert "limitations" not in reply


def test_no_declared_basis_takes_the_registry_headline():
    reply: dict = {}
    cash_bank = {"measures": {"core_profit": "cash earnings"}}
    assert _settle_basis(None, cash_bank, [], reply) == "cash"
    wbc_like = {"measures": {"core_profit": "net profit excluding Notable Items"}}
    assert _settle_basis(None, wbc_like, [], reply) == "ex_notables"
    assert "limitations" not in reply


def test_a_measures_block_naming_no_basis_word_still_defaults_cash():
    """The surviving default: under a measures block every committed registry
    is an Australian major, where cash earnings is the headline convention."""
    assert primary_basis({"measures": {"core_profit": "profit"}}) == "cash"


# ---------------------------------------------------------------------------
# A ratio's LEVEL must be ratio-sized, and the corrector keys on the METRIC
#
# Nothing validated that a ratio's LEVEL is ratio-sized, so an ROE submitted as
# 1160 -> 1140 "ppt" passed movement arithmetic, reconciliation and the scale
# normaliser at once: 1160 + -20 = 1140 is self-consistent, the drivers
# reconciled at the same wrong scale, and settle_identity_scale needs a
# contribution larger than the level, which nothing was.
# ---------------------------------------------------------------------------


def _ratio(unit, movement, metric, records=(), drivers=()):
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
                confidence=85,
                evidence=[],
            )
            for canonical, value, driver_unit in drivers
        ],
        evidence_records=list(records),
    )


def _percent_record(quote, numbers):
    return EvidenceRecord(
        id="ev-1",
        doc_id="CBA/1H26/profit_announcement",
        pdf_page=34,
        kind="table",
        quote=quote,
        numbers=[NumberFact(label=label, value=value, unit=unit) for label, value, unit in numbers],
    )


ROE_RECORD_NUMBERS = [("ROE FY25", 11.4, "%"), ("ROE FY24", 11.6, "%")]
ROE_QUOTE = "Cash return on equity 11.4% 11.6% (20 bps)"


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


def test_the_ratio_level_check_keys_on_the_metric_unit():
    """The check read the model's own label, so a ppt metric submitted as
    "1160 bps" was never asked to be ratio-sized."""
    movement = Movement(from_value=1160.0, to_value=1140.0, delta=-20.0, unit="bps")
    assert check_ratio_level(movement, "ppt")[1] != []
    assert check_ratio_level(movement, "ppt")[1][0].startswith("movement_level_not_ratio_sized")
    # A metric whose own unit IS basis points keeps its basis-point levels.
    assert check_ratio_level(movement, "bps") == ([], [])


def test_the_ratio_corrector_settles_the_movement_unit():
    """The NAB FY25 ROE submission carried the metric's numbers in basis points
    AND the label "bps". The corrector divided the numbers by 100 and left the
    label, so the artifact shipped "11.6 -> 11.4, -0.2 bps" — the gold movement
    written in a unit 100x out.
    """
    attribution = _ratio(
        "bps", (1160.0, 1140.0, -20.0), "roe",
        records=[_percent_record(ROE_QUOTE, ROE_RECORD_NUMBERS)],
    )
    note = settle_ratio_scale(attribution, "ppt")
    assert note is not None
    assert (attribution.movement.from_value, attribution.movement.to_value) == (11.6, 11.4)
    assert attribution.movement.delta == -0.2
    assert attribution.movement.unit == "ppt"
    assert "bps" in note and "ppt" in note
    assert check_ratio_level(attribution.movement, "ppt")[1] == []


def test_the_ratio_corrector_does_not_reverse_the_percent_to_bps_lift():
    """CET1's taxonomy unit is bps. The model labels the movement "%", the lift
    multiplies the endpoints by 100, and `settle_ratio_scale` — keying on the
    model's own label rather than the METRIC's unit, which the taxonomy fixes —
    divided them straight back. No check then fires, and the artifact ships
    +0.1 % against a gold of +10 bps, carrying two limitations that contradict
    each other.
    """
    record = _percent_record(
        "Common Equity Tier 1 ratio 12.20% 12.30%",
        [("CET1 Sep 24", 12.20, "%"), ("CET1 Sep 25", 12.30, "%")],
    )
    attribution = _ratio("%", (1220.0, 1230.0, 10.0), "cet1", records=[record])
    assert settle_ratio_scale(attribution, "bps") is None
    assert (attribution.movement.from_value, attribution.movement.to_value) == (1220.0, 1230.0)
    assert attribution.movement.delta == 10.0


def test_the_ratio_corrector_stays_silent_without_percent_evidence():
    """A movement already in points cannot pass the test: no page prints an
    ROE of 0.116 per cent."""
    record = _percent_record("Return on equity 11.6%", [("ROE", 11.6, "%")])
    attribution = _ratio("ppt", (11.6, 11.4, -0.2), "roe", records=[record])
    assert settle_ratio_scale(attribution, "ppt") is None
    assert attribution.movement.from_value == 11.6


def test_a_money_metric_never_reaches_the_ratio_corrector():
    assert settle_ratio_scale(_ratio("$m", (5132.0, 5445.0, 313.0), "cash_earnings"), "$m") is None


# ---------------------------------------------------------------------------
# The reconciliation SUM is unit-typed, for contributions AND for the residual
# ---------------------------------------------------------------------------


def test_a_basis_point_bar_no_longer_reconciles_a_dollar_bridge():
    """The tolerance became unit-typed and the addition stayed unit-blind."""
    attribution = _ratio(
        "$m", (5132.0, 5445.0, 313.0), "cash_earnings",
        drivers=[("nii", 310.0, None), ("mix", 3.0, "bps")],
    )
    passed, failed = check_drivers_reconcile(attribution)
    assert passed == []
    assert any(f.startswith("drivers_unit_mismatch") for f in failed)
    assert any(f.startswith("drivers_reconcile") for f in failed)


def test_three_basis_points_do_not_close_a_dollar_bridge():
    """The unit-typed sum covered the CONTRIBUTIONS and left the RESIDUAL
    unfiltered, so `drivers_reconcile` PASSED beside its own
    `drivers_unit_mismatch` failure.
    """
    attribution = _ratio(
        "$m", (5132.0, 5445.0, 313.0), "cash_earnings",
        drivers=[("net_interest_income", 310.0, None)],
    )
    attribution.residual = Contribution(value=3.0, unit="bps")
    passed, failed = check_drivers_reconcile(attribution)
    assert "drivers_reconcile" not in passed
    assert any(f.startswith("drivers_reconcile") for f in failed)
    assert any(f.startswith("drivers_unit_mismatch") for f in failed)


def test_a_residual_in_the_movement_s_own_unit_still_closes_the_bridge():
    """The ordinary residual, and the arm of the filter every real bridge takes.

    A residual is admitted when its unit is EMPTY or the movement's own. The
    unit-typed sum was written for the off-unit case, so the case that closes
    every honest bridge needs its own pin: an admitted residual joins the sum
    and raises no `drivers_unit_mismatch`.
    """
    attribution = _ratio(
        "$m", (5132.0, 5445.0, 313.0), "cash_earnings",
        drivers=[("net_interest_income", 310.0, None)],
    )
    attribution.residual = Contribution(value=3.0, unit="$m")
    passed, failed = check_drivers_reconcile(attribution)
    assert "drivers_reconcile" in passed
    assert not any(f.startswith("drivers_unit_mismatch") for f in failed)


def test_a_bridge_with_nothing_quantified_reports_it_and_reconciles_nothing():
    """`no_quantified_drivers` is the name `finalise` reads to tell an honest
    partial answer from a broken one, so the check must emit it rather than
    pass an empty sum against the movement's delta."""
    attribution = _ratio("$m", (5132.0, 5445.0, 313.0), "cash_earnings", drivers=[])
    passed, failed = check_drivers_reconcile(attribution)
    assert passed == []
    assert "no_quantified_drivers" in failed
    assert not any(f.startswith("drivers_reconcile") for f in failed)


def test_a_residual_with_no_unit_still_closes_the_bridge():
    """An unlabelled residual makes no competing unit claim, so it is read in
    the movement's unit, exactly as the contribution filter reads it."""
    attribution = _ratio(
        "$m", (5132.0, 5445.0, 313.0), "cash_earnings",
        drivers=[("net_interest_income", 310.0, None)],
    )
    attribution.residual = Contribution(value=3.0, unit="")
    assert "drivers_reconcile" in check_drivers_reconcile(attribution)[0]


def test_a_bare_note_number_does_not_ground_a_movement():
    """"See Note 1" prints a 1 — a note number, not a quantity; it laundered
    a +1 ppt delta under the plain printed-check."""
    from bank_equity_researcher.validation.schema import (
        Attribution,
        EvidenceRecord,
        Movement,
    )
    from bank_equity_researcher.validation.validate import cap_ungrounded_movement

    a = Attribution(
        bank="B", metric="roe", period="FY26", comparator="FY25", basis="cash",
        movement=Movement(from_value=13.0, to_value=14.0, delta=1.0, unit="ppt"),
        headline_evidence=["ev-1"], attribution_confidence=95,
        evidence_records=[EvidenceRecord(id="ev-1", doc_id="d", pdf_page=1,
                                         quote="See Note 1 for dividends")],
    )
    assert cap_ungrounded_movement(a) is True
    assert a.attribution_confidence == 20


def test_a_movement_stated_in_words_is_not_capped():
    """"fell three basis points" states the movement; the digit-only scan
    called it ungrounded and capped it to 20."""
    from bank_equity_researcher.validation.schema import (
        Attribution,
        EvidenceRecord,
        Movement,
    )
    from bank_equity_researcher.validation.validate import cap_ungrounded_movement

    a = Attribution(
        bank="B", metric="nim", period="FY26", comparator="FY25", basis="cash",
        movement=Movement(from_value=208.0, to_value=205.0, delta=-3.0, unit="bps"),
        headline_evidence=["ev-1"], attribution_confidence=90,
        evidence_records=[EvidenceRecord(id="ev-1", doc_id="d", pdf_page=1,
                                         quote="the margin fell three basis points")],
    )
    assert cap_ungrounded_movement(a) is False
    assert a.attribution_confidence == 90


def test_grounding_runs_after_the_scale_repair():
    """The cap must read the REPAIRED endpoints: a percent-scale movement was
    capped as ungrounded and then repaired to the very values its quotes
    print, still capped. Moving the call back above the settle pair went
    green before this pin."""
    import inspect

    from bank_equity_researcher.agent import research_agent as RA

    src = inspect.getsource(RA.finalise)
    assert src.index("settle_ratio_scale(") < src.index("cap_ungrounded_movement(")
    assert src.index("settle_identity_scale(") < src.index("cap_ungrounded_movement(")
