"""Movement, basis and sign normalisers (ticket 27, NAB/WBC movement round).

Two defects the WBC FY25 cases exposed:

- The impairment charge arrived re-signed. Westpac prints the line inside the
  P&L, where an expense is bracketed, so the shell reported -537 -> -424,
  delta +113 for a charge that FELL by $113m.
- The shell read "Return on average ordinary equity" when Westpac headlines
  ROTE ex Notable Items one line below. The registry already named the row.

These normalisers lived in author.py until ticket 33 wave 3 froze the open-loop
arm at the tag `pipeline-baseline-final`. They now live in validate.py beside
the checks that read their output, and the closed loop calls every one of them.
The tests that reached them through the deleted author shell now call them
directly or run through research_agent.build_attribution.
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
)
from bank_equity_researcher.validation.validate import (
    _settle_basis,
    check_drivers_reconcile,
    check_movement_basis,
    check_movement_variant,
    drop_off_unit_contributions,
    primary_basis,
    settle_charge_sign,
    settle_identity_scale,
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
            "benefit then charge",
            "the comparator being a benefit is equally real",
            IMPAIRMENT,
            {"from_value": -40.0, "to_value": 320.0, "delta": 360.0},
            (-40.0, 320.0, 360.0),
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
            "cash basis named in a CBA row",
            "CBA labels its own headline rows 'cash basis'",
            "roe",
            "row 'ROE - cash basis (%)', column FY25 -> column FY26",
            "cash",
            "Return on equity (cash basis)",
            False,
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
            "underscore in the citation",
            "the extractor's own label spelling reaches the citation as ex_notables",
            "roe",
            "row 'ROTE ex_notables', column FY24 -> column FY25",
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
# The ratio-identity scale normaliser (ticket 27, iteration 3)
#
# ROE and CTI derive their level-1 split from an identity. The growth rate
# enters that identity as a FRACTION, and a dollar movement enters it divided
# by average equity. An author that feeds a rate printed in per cent straight
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


def test_identity_scale_restates_the_cba_roe_split():
    """The same defect on the other side of zero, with a zero residual."""
    attribution = _identity(
        "roe", 10.2, 11.5,
        [("earnings_effect", 146.0, "ppt"), ("equity_effect", -16.0, "ppt")],
        residual=0.0,
    )
    assert settle_identity_scale(attribution, TAXONOMY["roe"]["method"]) is not None
    assert [d.contribution.value for d in attribution.drivers] == [1.46, -0.16]
    assert not check_drivers_reconcile(attribution)[1]


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


def test_identity_scale_is_silent_without_a_movement():
    attribution = _identity(
        "roe", 11.21, 10.97,
        [("earnings_effect", -23.76, "ppt")],
        residual=0.0,
    )
    attribution.movement = None
    assert settle_identity_scale(attribution, TAXONOMY["roe"]["method"]) is None


# ---------------------------------------------------------------------------
# Review round 2: the off-unit contribution drop
#
# A contribution is a share of THIS movement, so it is stated in the movement's
# own unit. The drop used to be reached only through the open-loop author, so
# these tests went through that shell. It is gone; the rule is not, and the
# closed loop calls it at research_agent.build_attribution. The end-to-end case
# lives in test_research_agent.py; this is the rule on its own.
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
# Review round 10: a registry that knows no basis settles none
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
