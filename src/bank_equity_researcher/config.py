"""Paths, model combos, and pricing. Model roles are configured here, never
hardcoded in pipeline code (ticket 07)."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"
REGISTRY_DIR = REPO_ROOT / "registry"
MANIFEST_DIR = REPO_ROOT / "manifest"
OUT_DIR = REPO_ROOT / "out"

# USD per 1M tokens (input, output), from the OpenRouter catalogue 2026-08-25.
PRICES: dict[str, tuple[float, float]] = {
    "qwen/qwen3.7-flash": (0.03, 0.13),
    "deepseek/deepseek-v4-flash-0731": (0.14, 0.28),
    "deepseek/deepseek-v4-pro-0813": (1.122, 3.366),
    "z-ai/glm-5.3": (1.40, 4.40),
    "stealth/ox-alpha": (0.0, 0.0),
}


@dataclass(frozen=True)
class Combo:
    """A model-role assignment. The eval matrix iterates these."""

    name: str
    extract: str
    vision: str
    author: str
    # The author needs room to reason; glm-5.3 ignores the reasoning-off flag
    # (ticket 14), so its budget must cover reasoning + answer.
    author_max_tokens: int
    judges: tuple[str, str]


COMBOS: dict[str, Combo] = {
    "cheap": Combo(
        name="cheap",
        extract="qwen/qwen3.7-flash",
        vision="qwen/qwen3.7-flash",
        author="qwen/qwen3.7-flash",
        author_max_tokens=8000,
        judges=("deepseek/deepseek-v4-pro-0813", "qwen/qwen3.7-flash"),
    ),
    "normal": Combo(
        name="normal",
        extract="qwen/qwen3.7-flash",
        vision="qwen/qwen3.7-flash",
        author="z-ai/glm-5.3",
        # 24000 was not enough on the densest bridge prompt (CBA cash_earnings
        # FY26): glm-5.3 spent the whole budget reasoning and returned empty
        # content five times (bake-off, 2026-08-29).
        author_max_tokens=40000,
        judges=("deepseek/deepseek-v4-pro-0813", "qwen/qwen3.7-flash"),
    ),
}


def openrouter_api_key() -> str:
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        env_file = REPO_ROOT / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if line.startswith("OPENROUTER_API_KEY="):
                    key = line.split("=", 1)[1].strip()
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY not found in environment or .env")
    return key
