"""Author-stage normalisers (ticket 27, NAB/WBC movement round).

Two defects the WBC FY25 cases exposed:

- The impairment charge arrived re-signed. Westpac prints the line inside the
  P&L, where an expense is bracketed, so the author reported -537 -> -424,
  delta +113 for a charge that FELL by $113m.
- The author read "Return on average ordinary equity" when Westpac headlines
  ROTE ex Notable Items one line below. The registry already named the row; the
  prompt never showed it.
"""

from __future__ import annotations

import pytest

from bank_equity_researcher.author import AUTHOR_PROMPT, author_attribution, settle_charge_sign
from bank_equity_researcher.schema import Attribution, Movement
from bank_equity_researcher.taxonomy import TAXONOMY
from bank_equity_researcher.validate import check_movement_basis, check_movement_variant

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
    """The flag lives in the taxonomy, so author.py stays bank-agnostic."""
    assert IMPAIRMENT["sign_convention"] == "positive_charge"
    assert "sign_convention" not in CASH_EARNINGS


class _CapturingLLM:
    """Answers one fixed reply and keeps every prompt it was given."""

    def __init__(self):
        self.prompts: list[str] = []

    def chat_json(self, model, prompt, max_tokens=None):
        self.prompts.append(prompt)
        return {
            "movement": {"from_value": 11.21, "to_value": 10.97, "delta": -0.24, "unit": "ppt"},
            "movement_row": "ROTE",
            "movement_from_column": "Full Year Sept 2024",
            "movement_to_column": "Full Year Sept 2025",
            "basis": "ex_notables",
            "headline": "",
            "drivers": [],
            "attribution_confidence": 80,
            "limitations": [],
        }


def _author(headline_row):
    llm = _CapturingLLM()
    author_attribution(
        llm,
        "model",
        max_tokens=100,
        case={"bank": "WBC", "metric": "roe", "period": "FY25", "comparator": "FY24"},
        taxonomy=TAXONOMY["roe"],
        registry={"measures": {"core_profit": "net profit excluding Notable Items"}},
        evidence_records=[],
        walks=[],
        validation={},
        fetch_more=lambda query: [],
        headline_row=headline_row,
    )
    return llm.prompts[0]


def test_prompt_names_the_registry_headline_row():
    prompt = _author("ROTE (return on average tangible equity), also ex Notable Items")
    assert "HEADLINE ROW for return on equity at this bank" in prompt
    assert "ROTE (return on average tangible equity), also ex Notable Items" in prompt


def test_prompt_falls_back_when_the_registry_names_no_row():
    prompt = _author(None)
    assert "the registry records no row for this metric" in prompt


def test_prompt_template_still_carries_every_placeholder():
    """A missing format key would raise at author time, never in a unit test."""
    assert "{headline_row}" in AUTHOR_PROMPT


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
