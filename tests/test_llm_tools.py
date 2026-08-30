"""The tool-calling client and its cost accounting (ADR-0005).

Offline: nothing here opens a socket. What the tests pin down is the shape of a
tool turn, the prompt-cache breakpoint that makes a tool loop affordable, and
the rule that a provider's own price for a call beats the per-token table.
"""

from __future__ import annotations

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
