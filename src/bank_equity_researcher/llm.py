"""OpenRouter client: reasoning-aware, retrying, cost-tracked."""

from __future__ import annotations

import base64
import json
import re
import time
from dataclasses import dataclass, field

import httpx

from .config import PRICES, openrouter_api_key

API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Models that ignore `reasoning: {enabled: false}` and think regardless
# (observed for glm-5.3 in ticket 14). For these we leave reasoning on and
# rely on a large max_tokens; content arrives after the reasoning block.
ALWAYS_REASONS = {"z-ai/glm-5.3"}

# Absolute wall-clock budget for ONE request, body included.
#
# httpx's `timeout` bounds the gap between chunks, never the whole call, so a
# provider that drips a response body a few bytes at a time keeps the socket
# alive for ever. A dev-suite run stalled for 30 minutes on exactly that: the
# process sat in bytes_join assembling response.content while the API itself
# answered a fresh request in under two seconds. The deadline below is checked
# per chunk, so a slow route is abandoned and retried on another route.
#
# The budget scales with the output the caller asked for: a 4k-token
# extraction gets the floor, and a 24k-token reasoning author gets room to
# finish. Generous against a healthy route, decisive against a dead one.
DEADLINE_FLOOR_S = 120.0
DEADLINE_SECONDS_PER_TOKEN = 0.02
# A well-formed reply is a few hundred KB. Beyond this the body is a fault,
# not an answer, and reading it only wastes memory.
MAX_RESPONSE_BYTES = 8 * 1024 * 1024
# Per-chunk network timeouts, so a silent socket also fails fast.
CHUNK_TIMEOUT = httpx.Timeout(connect=20.0, read=45.0, write=45.0, pool=20.0)


# Providers that honour an explicit prompt-cache breakpoint. A tool loop
# re-sends its whole transcript every turn, so each turn is a prefix of the
# next; one breakpoint on the end of the transcript lets the provider keep that
# prefix and charge a fraction for it on the turn after. Measured on
# anthropic/claude-opus-5, 2026-08-30: 6232 prompt tokens cost $0.039 written
# and $0.0038 read back, an eleven-fold reduction. A provider not named here
# gets the transcript unchanged.
CACHE_BREAKPOINT_PREFIXES = ("anthropic/",)


class ResponseDeadline(RuntimeError):
    """The response body exceeded its wall-clock or size budget."""


def with_cache_breakpoint(messages: list[dict], model: str) -> list[dict]:
    """Mark the end of the transcript as cacheable, where the provider allows.

    The caller's list is never mutated: a breakpoint left on an old message
    would pin the cache to a prefix that is no longer the end of the
    transcript, and the next turn would pay to write a second copy.
    """
    if not messages or not model.startswith(CACHE_BREAKPOINT_PREFIXES):
        return messages
    last = messages[-1]
    content = last.get("content")
    if not isinstance(content, str) or not content:
        return messages
    marked = dict(last)
    marked["content"] = [
        {"type": "text", "text": content, "cache_control": {"type": "ephemeral"}}
    ]
    return [*messages[:-1], marked]


@dataclass
class Usage:
    prompt_tokens: int = 0
    completion_tokens: int = 0
    cost_usd: float = 0.0
    calls: int = 0
    json_retries: int = 0
    deadline_aborts: int = 0
    by_model: dict = field(default_factory=dict)

    def add(self, model: str, prompt: int, completion: int, cost_usd: float | None = None) -> None:
        """Book one call. `cost_usd` overrides the per-token table.

        A tool loop re-sends its whole transcript every turn, so what it really
        costs depends on provider-side prompt caching that a token table cannot
        see. When the provider reports the price of a call, that number is the
        truth and the table is only the fallback.
        """
        pin, pout = PRICES.get(model, (0.0, 0.0))
        cost = prompt / 1e6 * pin + completion / 1e6 * pout
        if isinstance(cost_usd, (int, float)) and not isinstance(cost_usd, bool):
            cost = float(cost_usd)
        self.prompt_tokens += prompt
        self.completion_tokens += completion
        self.cost_usd += cost
        self.calls += 1
        m = self.by_model.setdefault(model, {"prompt": 0, "completion": 0, "cost": 0.0, "calls": 0})
        m["prompt"] += prompt
        m["completion"] += completion
        m["cost"] += cost
        m["calls"] += 1


# A connection-level failure means the NETWORK is gone, not that the request
# is bad - the answer is to wait, not to fail. On mobile hotspots (2026-08-31,
# the sealed-exam run) gaps last minutes, and five quick retries (~31s) die
# inside every gap, so a 20-minute case restarts from scratch each time. The
# grace ladder waits out gaps: up to NETWORK_GRACE tries at
# NETWORK_GRACE_SLEEP seconds each (~9 minutes) that do NOT consume normal
# attempts. Genuine request errors keep failing fast. Infra-only: no prompt,
# scoring or answer-content change (post-freeze disclosure in the report).
NETWORK_GRACE = 12
NETWORK_GRACE_SLEEP = 45
_NETWORK_ERROR_MARKS = (
    "nodename", "errno 8", "temporary failure in name resolution",
    "connection refused", "connection reset", "no route to host",
    "network is unreachable",
)


def _network_error(exc: Exception) -> bool:
    text = str(exc).lower()
    return any(mark in text for mark in _NETWORK_ERROR_MARKS)


class LLM:
    def __init__(self) -> None:
        self.usage = Usage()

    def _post(self, payload: dict, deadline_s: float) -> tuple[int, bytes]:
        """One request, streamed, under an absolute wall-clock deadline.

        The body is read chunk by chunk so the elapsed time and the byte count
        are checked as it arrives. A route that never stops sending is aborted
        here instead of holding the whole run; the caller's retry loop then
        tries again, usually on a different provider.
        """
        started = time.monotonic()
        chunks: list[bytes] = []
        total = 0
        with httpx.Client(timeout=CHUNK_TIMEOUT) as client, client.stream(
            "POST",
            API_URL,
            headers={"Authorization": f"Bearer {openrouter_api_key()}"},
            json=payload,
        ) as response:
            for chunk in response.iter_bytes():
                chunks.append(chunk)
                total += len(chunk)
                elapsed = time.monotonic() - started
                if elapsed > deadline_s or total > MAX_RESPONSE_BYTES:
                    self.usage.deadline_aborts += 1
                    response.close()
                    raise ResponseDeadline(
                        f"response abandoned after {elapsed:.0f}s and {total} bytes "
                        f"(deadline {deadline_s:.0f}s, cap {MAX_RESPONSE_BYTES} bytes)"
                    )
            return response.status_code, b"".join(chunks)

    def chat(
        self,
        model: str,
        prompt: str,
        *,
        image_png: bytes | None = None,
        max_tokens: int = 4000,
        retries: int = 5,
    ) -> str:
        content: list | str
        if image_png is not None:
            b64 = base64.b64encode(image_png).decode()
            content = [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
            ]
        else:
            content = prompt
        payload: dict = {
            "model": model,
            "messages": [{"role": "user", "content": content}],
            "max_tokens": max_tokens,
            "temperature": 0,
        }
        if model not in ALWAYS_REASONS:
            payload["reasoning"] = {"enabled": False}

        deadline_s = max(DEADLINE_FLOOR_S, max_tokens * DEADLINE_SECONDS_PER_TOKEN)
        last_error: Exception | None = None
        attempt = 0
        grace = 0
        while attempt < retries:
            try:
                status, body = self._post(payload, deadline_s)
                if status == 400 and "reasoning" in payload:
                    payload.pop("reasoning")
                    continue
                if status == 429:
                    attempt += 1
                    time.sleep(15 * attempt)
                    last_error = RuntimeError("429 Too Many Requests")
                    continue
                if status >= 400:
                    raise RuntimeError(f"HTTP {status}: {body[:300]!r}")
                data = json.loads(body)
                if "choices" not in data:
                    raise RuntimeError(f"no choices: {str(data)[:300]}")
                usage = data.get("usage", {})
                self.usage.add(model, usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0))
                text = data["choices"][0]["message"]["content"]
                if not text:
                    raise RuntimeError("empty content (reasoning consumed the budget?)")
                return text
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                if _network_error(exc) and grace < NETWORK_GRACE:
                    # A dead network is waited out, never charged as an attempt.
                    grace += 1
                    time.sleep(NETWORK_GRACE_SLEEP)
                    continue
                attempt += 1
                time.sleep(2**attempt)
        raise RuntimeError(f"chat() failed for {model} after {retries} attempts: {last_error}")

    def chat_tools(
        self,
        model: str,
        messages: list[dict],
        tools: list[dict],
        *,
        max_tokens: int = 4000,
        retries: int = 5,
    ) -> dict:
        """One tool-calling turn, under chat()'s deadline and retry discipline.

        OpenRouter speaks the OpenAI tools schema, so a turn is an ordinary
        request that also carries `tools`. The return value is the assistant
        MESSAGE, because the caller needs both halves of it: the prose and the
        tool calls it asked for. A reply is empty only when it carries neither.
        """
        payload: dict = {
            "model": model,
            "messages": with_cache_breakpoint(messages, model),
            "tools": tools,
            "max_tokens": max_tokens,
            "temperature": 0,
            # Ask the provider to price the call itself; see Usage.add.
            "usage": {"include": True},
        }
        if model not in ALWAYS_REASONS:
            payload["reasoning"] = {"enabled": False}

        deadline_s = max(DEADLINE_FLOOR_S, max_tokens * DEADLINE_SECONDS_PER_TOKEN)
        last_error: Exception | None = None
        attempt = 0
        grace = 0
        while attempt < retries:
            try:
                status, body = self._post(payload, deadline_s)
                if status == 400 and "reasoning" in payload:
                    payload.pop("reasoning")
                    continue
                if status == 429:
                    attempt += 1
                    time.sleep(15 * attempt)
                    last_error = RuntimeError("429 Too Many Requests")
                    continue
                if status >= 400:
                    raise RuntimeError(f"HTTP {status}: {body[:300]!r}")
                data = json.loads(body)
                if "choices" not in data:
                    raise RuntimeError(f"no choices: {str(data)[:300]}")
                usage = data.get("usage", {})
                self.usage.add(
                    model,
                    usage.get("prompt_tokens", 0),
                    usage.get("completion_tokens", 0),
                    cost_usd=usage.get("cost"),
                )
                message = data["choices"][0]["message"]
                if not message.get("content") and not message.get("tool_calls"):
                    raise RuntimeError("empty reply: neither content nor a tool call")
                return message
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                if _network_error(exc) and grace < NETWORK_GRACE:
                    # A dead network is waited out, never charged as an attempt.
                    grace += 1
                    time.sleep(NETWORK_GRACE_SLEEP)
                    continue
                attempt += 1
                time.sleep(2**attempt)
        raise RuntimeError(
            f"chat_tools() failed for {model} after {retries} attempts: {last_error}"
        )

    def chat_json(self, model: str, prompt: str, *, json_retries: int = 2, **kwargs):
        """chat() plus a parse-failure retry, so every JSON caller inherits it.

        The cheap models occasionally return a TRUNCATED reply with
        finish_reason "stop" — the CBA FY25 Profit Announcement NIM chart came
        back as '```json\\n{\\n  "title": "NIM Movement' twice, and the author
        died twice on "Expecting ':' delimiter" (ticket 27). Re-issuing the
        whole request usually routes to a healthy provider, so the retry
        repeats the call rather than the parse, and asks for terminated JSON.
        """
        hint = "\n\nReply with COMPLETE terminated JSON only - no prose, no trailing text."
        error: Exception | None = None
        for attempt in range(json_retries + 1):
            text = self.chat(model, prompt if attempt == 0 else prompt + hint, **kwargs)
            try:
                return parse_json_block(text)
            except ValueError as exc:
                error = exc
                self.usage.json_retries += 1
        raise error if error else RuntimeError("chat_json failed without an error")


def parse_json_block(text: str):
    """Extract the first JSON object or array from a model reply."""
    fenced = re.search(r"```(?:json)?\s*(.+?)```", text, re.DOTALL)
    candidate = fenced.group(1) if fenced else text
    start = min((i for i in (candidate.find("{"), candidate.find("[")) if i >= 0), default=-1)
    if start == -1:
        raise ValueError(f"no JSON in reply: {text[:200]}")
    # strict=False tolerates literal newlines/control chars inside strings,
    # which vision models emit when reading multi-line chart labels.
    body = candidate[start:]
    try:
        obj, _ = json.JSONDecoder(strict=False).raw_decode(body)
    except json.JSONDecodeError:
        for repair in _REPAIRS:
            patched = repair(body)
            if patched == body:
                continue
            try:
                obj, _ = json.JSONDecoder(strict=False).raw_decode(patched)
                return obj
            except json.JSONDecodeError:
                continue
        raise _decode_error(body)
    return obj


# Both CBA CTI cases died on a dropped key colon. The model wrote
# '"narrative "Operating expenses grew 5.8%",' — the colon and the value's
# opening quote are missing, so the key swallowed the space. The pattern needs
# a bare identifier, whitespace, a closing quote and then a character that can
# never follow a string in valid JSON, which makes a false positive impossible.
_MISSING_KEY_COLON = re.compile(r'("[A-Za-z_][A-Za-z0-9_]*)\s+"(?=[^\s,:\]}])')
# The same slip with the value's quote intact: two strings side by side, which
# valid JSON never contains either.
_MISSING_COLON = re.compile(r'("[A-Za-z_][A-Za-z0-9_]*")(?=\s+["\[{tfn\-0-9])')

# Applied only after a strict parse has failed, and kept only if the patched
# text parses. A repair that does not parse is discarded, never guessed at.
_REPAIRS = (
    lambda body: _MISSING_KEY_COLON.sub(r'\1": "', body),
    lambda body: _MISSING_COLON.sub(r"\1: ", body),
)


def _decode_error(body: str) -> ValueError:
    """Re-run the failing decode to build a message that names the text.

    A bare "Expecting ':' delimiter: line 18 column 19" costs a whole rerun to
    diagnose; the window either side of the fault names the culprit at once.
    """
    try:
        json.JSONDecoder(strict=False).raw_decode(body)
    except json.JSONDecodeError as exc:
        window = body[max(0, exc.pos - 90): exc.pos + 90].replace("\n", "\\n")
        return ValueError(f"{exc.msg} at pos {exc.pos}; near: ...{window}...")
    return ValueError("JSON decode failed and then succeeded on retry")
