"""The tool-calling client and its cost accounting (ADR-0005).

Offline: nothing here opens a socket. What the tests pin down is the shape of a
tool turn, the prompt-cache breakpoint that makes a tool loop affordable, and
the rule that a provider's own price for a call beats the per-token table.
"""

from __future__ import annotations

import time

import httpx
import pytest

from bank_equity_researcher import llm as L
from bank_equity_researcher.llm import Usage, with_cache_breakpoint


def test_the_breakpoint_marks_only_the_end_of_the_transcript():
    messages = [
        {"role": "system", "content": "rules"},
        {"role": "user", "content": "the case"},
        {"role": "tool", "tool_call_id": "c1", "content": "a page"},
    ]
    marked = with_cache_breakpoint(messages, "anthropic/claude-opus-5")
    assert marked[0] == messages[0] and marked[1] == messages[1]
    assert marked[-1]["content"] == [
        {"type": "text", "text": "a page", "cache_control": {"type": "ephemeral"}}
    ]
    assert marked[-1]["tool_call_id"] == "c1"


def test_the_caller_s_transcript_is_never_mutated():
    """A breakpoint left on an old message pins the cache to the wrong prefix."""
    messages = [{"role": "user", "content": "the case"}]
    with_cache_breakpoint(messages, "anthropic/claude-opus-5")
    assert messages == [{"role": "user", "content": "the case"}]


def test_a_provider_without_breakpoints_gets_the_transcript_unchanged():
    messages = [{"role": "user", "content": "the case"}]
    assert with_cache_breakpoint(messages, "qwen/qwen3.7-flash") is messages


def test_an_assistant_turn_carrying_only_tool_calls_is_left_alone():
    messages = [{"role": "assistant", "content": "", "tool_calls": [{"id": "c1"}]}]
    assert with_cache_breakpoint(messages, "anthropic/claude-opus-5") is messages


def test_usage_prefers_the_price_the_provider_reported():
    usage = Usage()
    usage.add("anthropic/claude-opus-5", 1_000_000, 0, cost_usd=0.42)
    assert usage.cost_usd == 0.42
    assert usage.by_model["anthropic/claude-opus-5"]["cost"] == 0.42


def test_usage_falls_back_to_the_table_when_no_price_is_reported():
    usage = Usage()
    usage.add("anthropic/claude-opus-5", 1_000_000, 1_000_000)
    assert usage.cost_usd == 30.0


# ---------------------------------------------------------------------------
# The grace ladder classifies by exception TYPE
#
# The ladder classified a dead network by the ENGLISH of its message, so the
# timeout shape of a hotspot gap — the gap the ladder exists for — burned the
# five ordinary attempts instead.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "exc,grace",
    [
        # One shape per transport type. Both returned False before the fix: the
        # message carries no mark the old ladder knew, and an empty message
        # carries nothing at all.
        (httpx.ConnectTimeout(""), True),
        (httpx.ConnectError("[Errno 60] Operation timed out"), True),
        # A read-phase timeout stays fail-fast: a stall mid-body is one stuck
        # provider route, and retrying on another route beats waiting.
        (httpx.ReadTimeout("timed out"), False),
        # The response-body budget is a read-phase abort as well.
        (L.ResponseDeadline("response abandoned after 320s and 12 bytes"), False),
        # A genuine request error never earns grace.
        (RuntimeError("HTTP 500: server exploded"), False),
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
# The ladder is bounded by the case deadline and sleeps once per retry
#
# No call carried the case's own deadline, so one `chat_tools` call could hold
# ~9 minutes of grace sleeps after the budget was already spent.
# ---------------------------------------------------------------------------


def _sleepless(monkeypatch) -> list[float]:
    slept: list[float] = []
    monkeypatch.setattr(L.time, "sleep", slept.append)
    return slept


def test_five_server_errors_sleep_the_original_ladder_and_not_after_the_last(monkeypatch):
    """The while-loop conversion slept [2, 4, 8, 16, 32] — 62 seconds, 32 of
    them after no attempt remained. The loop before it slept [1, 2, 4, 8, 16],
    and the last of those was wasted too."""
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
    """The shape that costs the most: one call could hold twelve 45-second
    grace waits, roughly nine minutes, after the case's own wall clock had
    already run out."""
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
    """The deadline is OPTIONAL: a caller that sets none is unchanged, and a
    dead network is waited out through the grace ladder without consuming the
    five ordinary attempts."""
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


def test_the_usage_trace_books_request_time_and_sleeps(monkeypatch):
    """Where a slow case's time went is measured, not inferred: request wall
    time, the slowest call, retry counts, and ladder sleeps all book."""
    monkeypatch.setattr(L.time, "sleep", lambda s: None)
    client = L.LLM()
    calls = {"n": 0}

    def flaky_post(payload, deadline):
        calls["n"] += 1
        if calls["n"] == 1:
            raise RuntimeError("HTTP 500: server exploded")
        return 200, b'{"choices":[{"message":{"content":"OK"}}],"usage":{}}'

    monkeypatch.setattr(client, "_post", flaky_post)
    assert client.chat("m", "p") == "OK"
    assert client.usage.retry_attempts == 1
    assert client.usage.slept_s == 1
    assert client.usage.request_s >= 0
    assert client.usage.slowest_call_s >= 0


def test_an_empty_reply_reroutes_and_widens_the_budget(monkeypatch):
    """An empty reply is a MODEL-side failure the blind retry re-hit five
    times (the frozen exam lost 2 of 10 questions to one broken provider).
    The retry ignores the provider that served it and widens max_tokens —
    reasoning may have eaten the whole budget."""
    monkeypatch.setattr(L.time, "sleep", lambda s: None)
    client = L.LLM()
    seen: list[dict] = []

    def flaky_post(payload, deadline):
        seen.append({"provider": payload.get("provider"),
                     "max_tokens": payload["max_tokens"]})
        if len(seen) == 1:
            return 200, b'{"provider":"BadRoute","choices":[{"message":{"content":null}}],"usage":{}}'
        return 200, b'{"choices":[{"message":{"content":"OK","tool_calls":null}}],"usage":{}}'

    monkeypatch.setattr(client, "_post", flaky_post)
    message = client.chat_tools("m", [{"role": "user", "content": "p"}], [],
                                max_tokens=4000)
    assert message["content"] == "OK"
    assert seen[0]["provider"] is None
    assert seen[1]["provider"] == {"ignore": ["BadRoute"]}
    assert seen[1]["max_tokens"] == 6000
    assert client.usage.empty_replies == 1
