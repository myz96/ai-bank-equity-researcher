"""Review round 5: the collapse-hygiene round.

Every test carries the repro that found the defect, as the reviewer executed
it. The measurement core normalised in this round, so what is left sits at the
edges of the collapse:

- The wave-1 cleanup deleted the named-driver caps for `comparison_leak` and
  `component_from_prior_half` and left `WHOLE_TABLE_FAILURES` excluding both
  names on the now-false ground that they cap in place. A repro'd wrong driver
  rode at 95 into the confidently-wrong population.
- The grace ladder classified a dead network by the ENGLISH of its message, so
  the timeout shape of a hotspot gap — the gap the ladder exists for — burned
  the five ordinary attempts instead.
- No call carried the case's own deadline, so one `chat_tools` call could hold
  ~9 minutes of grace sleeps after the budget was already spent.
- The while-loop conversion doubled the ordinary backoff and slept once more
  after the last attempt was gone.
"""

from __future__ import annotations

import inspect
import re
import time
from pathlib import Path

import httpx
import pytest

from bank_equity_researcher import cli
from bank_equity_researcher import llm as L
from bank_equity_researcher.config import COMBOS, runner_for
from bank_equity_researcher.evals import harness as E
from bank_equity_researcher.validation.schema import (
    Attribution,
    Contribution,
    DriverClaim,
    Movement,
)
from bank_equity_researcher.validation.validate import (
    CLAIM_CITATION_CAP,
    WHOLE_TABLE_FAILURES,
    cap_unreconciled_drivers,
)


def _attribution(unit="$m", movement=(5132.0, 5445.0, 313.0), drivers=()) -> Attribution:
    return Attribution(
        bank="CBA",
        metric="cash_earnings",
        period="1H26",
        comparator="1H25",
        basis="cash",
        movement=Movement(
            from_value=movement[0], to_value=movement[1], delta=movement[2], unit=unit
        ),
        drivers=[
            DriverClaim(
                canonical=canonical,
                contribution=Contribution(value=value, unit=unit),
                confidence=confidence,
                evidence=[],
            )
            for canonical, value, confidence in drivers
        ],
    )


# ---------------------------------------------------------------------------
# 1. The two named wrong-claim checks cap again
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "failure",
    [
        # Codex's executed repro: `comparison_leak` fired on a 95-confidence
        # driver, `cap_unreconciled_drivers` returned [] and the confidence
        # stayed at 95.
        (
            "comparison_leak (funding.deposits claims -3, which is the 'Deposits' bar of "
            "CBA/1H26/results_presentation p28, a walk for a different comparison; "
            "the task-comparison walk shows -5)"
        ),
        (
            "component_from_prior_half (credit_impairment_charge claims -1 $m, which is a "
            "delta against the PRIOR HALF's column and matches no 1H26 versus 1H25 delta "
            "in the evidence)"
        ),
    ],
)
def test_a_wrong_claim_check_that_lost_its_named_cap_caps_the_table(failure):
    """The cleanup regression, both halves of it.

    Ticket 33 wave 1 deleted `comparison_leak_cap_80` and
    `component_column_cap_80` because neither override fired on the 90 saved
    artifacts. Nothing replaced them, and `WHOLE_TABLE_FAILURES` still named
    both as absent BECAUSE they cap in place. A demonstrably wrong driver was
    therefore left at 95.
    """
    attribution = _attribution(drivers=[("credit_impairment_charge", -1.0, 95)])
    assert cap_unreconciled_drivers(attribution, [failure]) != []
    assert attribution.drivers[0].confidence == CLAIM_CITATION_CAP


def test_both_names_are_whole_table_failures():
    assert "comparison_leak" in WHOLE_TABLE_FAILURES
    assert "component_from_prior_half" in WHOLE_TABLE_FAILURES


def test_the_walk_names_stay_out_of_the_whole_table_set():
    """Round 3's decision is untouched: a broken chart read is capped by name."""
    assert "walk_sum" not in WHOLE_TABLE_FAILURES
    assert "walk_extraction_error" not in WHOLE_TABLE_FAILURES


# ---------------------------------------------------------------------------
# 3. The grace ladder classifies by exception TYPE
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "exc,grace",
    [
        # Fable's six executed shapes. The first two already passed on their
        # message; the next three are the hotspot gap the ladder exists for and
        # every one of them returned False.
        (httpx.ConnectError("[Errno 8] nodename nor servname provided, or not known"), True),
        (httpx.ConnectError("[Errno 61] Connection refused"), True),
        (httpx.ConnectTimeout("timed out"), True),
        (httpx.ConnectTimeout(""), True),
        (httpx.ConnectError("[Errno 60] Operation timed out"), True),
        # A read-phase timeout stays fail-fast: a stall mid-body is one stuck
        # provider route, and retrying on another route beats waiting.
        (httpx.ReadTimeout("timed out"), False),
        # The response-body budget is a read-phase abort as well.
        (L.ResponseDeadline("response abandoned after 320s and 12 bytes"), False),
        # A genuine request error never earns grace.
        (RuntimeError("HTTP 500: server exploded"), False),
        (RuntimeError("HTTP 429: slow down"), False),
    ],
)
def test_the_grace_ladder_reads_the_exception_type(exc, grace):
    assert L._network_error(exc) is grace


def test_a_wrapped_connection_failure_still_earns_grace():
    """A transport error the client re-raises inside another error is the same
    dead network. The chain is walked, so the wrapper cannot hide it."""
    try:
        try:
            raise httpx.ConnectError("[Errno 60] Operation timed out")
        except httpx.ConnectError as cause:
            raise RuntimeError("request failed") from cause
    except RuntimeError as exc:
        assert L._network_error(exc) is True


def test_a_plain_message_mark_still_earns_grace():
    """The message marks stay as the fallback for a shape httpx does not
    raise: the OSError a socket layer hands up unwrapped."""
    assert L._network_error(OSError(8, "nodename nor servname provided, or not known")) is True


# ---------------------------------------------------------------------------
# 4 + 7. The ladder is bounded by the case deadline and sleeps once per retry
# ---------------------------------------------------------------------------


def _sleepless(monkeypatch) -> list[float]:
    slept: list[float] = []
    monkeypatch.setattr(L.time, "sleep", slept.append)
    return slept


def test_five_server_errors_sleep_the_original_ladder_and_not_after_the_last(monkeypatch):
    """Finding 7's repro: the while-loop conversion slept [2, 4, 8, 16, 32] —
    62 seconds, 32 of them after no attempt remained. The loop before it slept
    [1, 2, 4, 8, 16], and the last of those was wasted too."""
    slept = _sleepless(monkeypatch)
    client = L.LLM()
    calls = {"n": 0}

    def broken_post(payload, deadline):
        calls["n"] += 1
        raise RuntimeError("HTTP 500: server exploded")

    monkeypatch.setattr(client, "_post", broken_post)
    with pytest.raises(RuntimeError):
        client.chat("m", "p")
    assert calls["n"] == 5
    assert slept == [1, 2, 4, 8]


def test_a_deadline_already_past_stops_the_call_before_it_posts(monkeypatch):
    """The case is over, so a new attempt is a call made after the budget."""
    slept = _sleepless(monkeypatch)
    client = L.LLM()
    calls = {"n": 0}

    def counting_post(payload, deadline):
        calls["n"] += 1
        return 200, b'{"choices":[{"message":{"content":"OK"}}],"usage":{}}'

    monkeypatch.setattr(client, "_post", counting_post)
    with pytest.raises(RuntimeError, match="deadline"):
        client.chat("m", "p", deadline_monotonic=time.monotonic() - 1)
    assert calls["n"] == 0
    assert slept == []


def test_a_grace_wait_that_would_outlive_the_case_is_not_taken(monkeypatch):
    """Finding 4's repro, in the shape that costs the most: one call could hold
    twelve 45-second grace waits, roughly nine minutes, after the case's own
    wall clock had already run out."""
    slept = _sleepless(monkeypatch)
    client = L.LLM()
    calls = {"n": 0}

    def dead_network(payload, deadline):
        calls["n"] += 1
        raise httpx.ConnectTimeout("timed out")

    monkeypatch.setattr(client, "_post", dead_network)
    with pytest.raises(RuntimeError, match="deadline"):
        # Ten seconds left, and one grace wait is 45.
        client.chat("m", "p", deadline_monotonic=time.monotonic() + 10)
    assert calls["n"] == 1
    assert slept == []


def test_the_request_budget_never_outlives_the_case(monkeypatch):
    """A single request may not be given more time than the case has left."""
    client = L.LLM()
    seen: list[float] = []

    def recording_post(payload, deadline):
        seen.append(deadline)
        return 200, b'{"choices":[{"message":{"content":"OK"}}],"usage":{}}'

    monkeypatch.setattr(client, "_post", recording_post)
    assert client.chat("m", "p", deadline_monotonic=time.monotonic() + 30) == "OK"
    assert seen and seen[0] <= 30


def test_a_call_with_no_deadline_keeps_the_full_ladder(monkeypatch):
    """The deadline is OPTIONAL: a caller that sets none is unchanged."""
    monkeypatch.setattr(L, "NETWORK_GRACE_SLEEP", 0)
    _sleepless(monkeypatch)
    client = L.LLM()
    calls = {"n": 0}

    def flaky_post(payload, deadline):
        calls["n"] += 1
        if calls["n"] <= 8:  # more failures than the 5 normal attempts
            raise httpx.ConnectTimeout("timed out")
        return 200, b'{"choices":[{"message":{"content":"OK"}}],"usage":{}}'

    monkeypatch.setattr(client, "_post", flaky_post)
    assert client.chat("m", "p") == "OK"


def test_chat_tools_carries_the_same_deadline_discipline(monkeypatch):
    """The tool loop is where the nine minutes were spent, so it needs the
    bound more than chat() does."""
    slept = _sleepless(monkeypatch)
    client = L.LLM()
    calls = {"n": 0}

    def dead_network(payload, deadline):
        calls["n"] += 1
        raise httpx.ConnectError("[Errno 61] Connection refused")

    monkeypatch.setattr(client, "_post", dead_network)
    with pytest.raises(RuntimeError, match="deadline"):
        client.chat_tools("m", [{"role": "user", "content": "p"}], [],
                          deadline_monotonic=time.monotonic() + 10)
    assert calls["n"] == 1
    assert slept == []


# ---------------------------------------------------------------------------
# 5. Every combo the CLI names can be reached
# ---------------------------------------------------------------------------


def test_every_combo_the_cli_help_names_can_actually_run():
    """Three `--combo` help strings read "agentic | agentic-glm |
    agentic-cheap" after the collapse left `COMBOS` holding one name, so a user
    who followed the help text got a KeyError from `runner_for`."""
    source = Path(cli.__file__).read_text()
    for name in re.findall(r"\bagentic-[a-z-]+\b", source):
        assert name in COMBOS, f"the CLI help advertises {name}, which runner_for rejects"


def test_the_unknown_combo_message_covers_every_retired_arm():
    """The old message explained the OPEN-LOOP freeze, which is the wrong
    story for `agentic-cheap`: that arm was a closed-loop combo retired
    separately, and a reader was sent looking for the wrong tag."""
    with pytest.raises(KeyError) as caught:
        runner_for("agentic-cheap")
    message = str(caught.value)
    assert "retired" in message
    assert "rescore" in message


def test_the_offline_actions_default_to_the_live_combo():
    """`run_judge_suite` and `rescore` both defaulted to `cheap`, a name
    `COMBOS` has not held since the collapse, so `run_judge_suite()` crashed on
    its own defaults."""
    assert inspect.signature(E.run_judge_suite).parameters["combo"].default == "agentic"
    assert inspect.signature(E.rescore).parameters["combo"].default == "agentic"


def test_the_judge_action_still_grades_a_retired_slug(tmp_path, monkeypatch):
    """The judge action reads SAVED artifacts and runs no shell, so it takes
    the combo as a slug selector exactly as rescore does. Reading
    `COMBOS[combo].judges` made a retired slug raise a bare KeyError and left
    the frozen `-cheap` baseline with no judge path at all."""
    monkeypatch.setattr(E, "RESULTS_DIR", tmp_path)
    monkeypatch.setattr(E, "load_gold", lambda suite, bank: [])
    card = E.run_judge_suite("dev", "cheap")
    assert card.exists()
    # The slug is the retired name; the judges are the live combo's.
    assert "combo cheap" in card.read_text()
    assert ", ".join(COMBOS["agentic"].judges) in card.read_text()
