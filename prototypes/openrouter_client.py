"""Minimal OpenRouter client for the prototypes. Throwaway by design."""

from __future__ import annotations

import base64
import json
import os
import re
import time
from dataclasses import dataclass, field
from pathlib import Path

import httpx

REPO_ROOT = Path(__file__).resolve().parent.parent
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# USD per 1M tokens (input, output), from the live catalogue on 2026-08-25.
PRICES = {
    "stealth/ox-alpha": (0.0, 0.0),
    "qwen/qwen3.7-flash": (0.03, 0.13),
    "deepseek/deepseek-v4-flash-0731": (0.14, 0.28),
    "deepseek/deepseek-v4-flash-vision-exp": (0.44, 1.32),
    "deepseek/deepseek-v4-pro-0813": (1.122, 3.366),
    "z-ai/glm-5.3": (1.40, 4.40),
    "moonshotai/kimi-k3": (3.00, 15.00),
}


def load_api_key() -> str:
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        for line in (REPO_ROOT / ".env").read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                key = line.split("=", 1)[1].strip()
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY not found in env or .env")
    return key


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


USAGE = Usage()


def chat(model: str, prompt: str, *, image_png: bytes | None = None, max_tokens: int = 4000, retries: int = 5) -> str:
    content: list | str
    if image_png is not None:
        b64 = base64.b64encode(image_png).decode()
        content = [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
        ]
    else:
        content = prompt
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": content}],
        "max_tokens": max_tokens,
        "temperature": 0,
        # Reasoning eats the token budget and leaves content=None on hybrid
        # models; the prototypes want plain answers.
        "reasoning": {"enabled": False},
    }
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            response = httpx.post(
                API_URL,
                headers={"Authorization": f"Bearer {load_api_key()}"},
                json=payload,
                timeout=180,
            )
            if response.status_code == 400 and "reasoning" in payload:
                payload = {k: v for k, v in payload.items() if k != "reasoning"}
                continue
            if response.status_code == 429:
                time.sleep(15 * (attempt + 1))
                last_error = RuntimeError("429 Too Many Requests")
                continue
            response.raise_for_status()
            data = response.json()
            if "choices" not in data:
                raise RuntimeError(f"no choices: {data}")
            usage = data.get("usage", {})
            USAGE.add(model, usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0))
            text = data["choices"][0]["message"]["content"]
            if not text:
                raise RuntimeError("empty content (reasoning consumed the budget?)")
            return text
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(2**attempt)
    raise RuntimeError(f"chat() failed for {model} after {retries} attempts: {last_error}")


def parse_json_block(text: str):
    """Extract the first JSON object or array from a model reply."""
    fenced = re.search(r"```(?:json)?\s*(.+?)```", text, re.DOTALL)
    candidate = fenced.group(1) if fenced else text
    start = min((i for i in (candidate.find("{"), candidate.find("[")) if i >= 0), default=-1)
    if start == -1:
        raise ValueError(f"no JSON in reply: {text[:200]}")
    decoder = json.JSONDecoder()
    obj, _ = decoder.raw_decode(candidate[start:])
    return obj
