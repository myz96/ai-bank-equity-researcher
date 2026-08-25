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


@dataclass
class Usage:
    prompt_tokens: int = 0
    completion_tokens: int = 0
    cost_usd: float = 0.0
    calls: int = 0
    by_model: dict = field(default_factory=dict)

    def add(self, model: str, prompt: int, completion: int) -> None:
        pin, pout = PRICES.get(model, (0.0, 0.0))
        cost = prompt / 1e6 * pin + completion / 1e6 * pout
        self.prompt_tokens += prompt
        self.completion_tokens += completion
        self.cost_usd += cost
        self.calls += 1
        m = self.by_model.setdefault(model, {"prompt": 0, "completion": 0, "cost": 0.0, "calls": 0})
        m["prompt"] += prompt
        m["completion"] += completion
        m["cost"] += cost
        m["calls"] += 1


class LLM:
    def __init__(self) -> None:
        self.usage = Usage()

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

        last_error: Exception | None = None
        for attempt in range(retries):
            try:
                response = httpx.post(
                    API_URL,
                    headers={"Authorization": f"Bearer {openrouter_api_key()}"},
                    json=payload,
                    timeout=300,
                )
                if response.status_code == 400 and "reasoning" in payload:
                    payload.pop("reasoning")
                    continue
                if response.status_code == 429:
                    time.sleep(15 * (attempt + 1))
                    last_error = RuntimeError("429 Too Many Requests")
                    continue
                response.raise_for_status()
                data = response.json()
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
                time.sleep(2**attempt)
        raise RuntimeError(f"chat() failed for {model} after {retries} attempts: {last_error}")

    def chat_json(self, model: str, prompt: str, **kwargs):
        return parse_json_block(self.chat(model, prompt, **kwargs))


def parse_json_block(text: str):
    """Extract the first JSON object or array from a model reply."""
    fenced = re.search(r"```(?:json)?\s*(.+?)```", text, re.DOTALL)
    candidate = fenced.group(1) if fenced else text
    start = min((i for i in (candidate.find("{"), candidate.find("[")) if i >= 0), default=-1)
    if start == -1:
        raise ValueError(f"no JSON in reply: {text[:200]}")
    # strict=False tolerates literal newlines/control chars inside strings,
    # which vision models emit when reading multi-line chart labels.
    obj, _ = json.JSONDecoder(strict=False).raw_decode(candidate[start:])
    return obj
