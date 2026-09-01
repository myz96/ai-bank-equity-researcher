"""Paths, model combos, and pricing. Model roles are configured here, never
hardcoded at the call sites."""

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
    "deepseek/deepseek-v4-pro-0813": (1.122, 3.366),
    "z-ai/glm-5.3": (1.40, 4.40),
    # Mid-tier reasoning candidates for the research loop; they price the
    # closed loop at cents per case. Catalogue prices read live 2026-08-31.
    "z-ai/glm-5.3-flash": (0.07, 0.25),
    "openai/gpt-5.6-luna": (0.20, 1.20),
    "deepseek/deepseek-v4-flash-0731": (0.14, 0.28),
    # Closed-loop research agent tiers (ADR-0005), from the OpenRouter
    # catalogue 2026-08-30. A tool loop reports its own cost per call, so
    # these are the fallback, not the primary accounting.
    "anthropic/claude-opus-5": (5.00, 25.00),
}


@dataclass(frozen=True)
class Combo:
    """A model-role assignment. The eval matrix iterates these."""

    name: str
    vision: str
    judges: tuple[str, str]
    # Which orchestration shell answers a case. "agent", the closed-loop
    # tool-use research agent (ADR-0005), is the only one left; the open-loop
    # "pipeline" shell is frozen at the tag `pipeline-baseline-final`. The
    # field stays as the seam runner_for reads.
    orchestration: str = "agent"
    # The tool-calling model that drives the research loop.
    agent: str = ""
    agent_max_tokens: int = 8000
    # Runaway protection only (ADR-0005 point 5): set generously enough that a
    # normal run never meets them. On exhaustion the loop asks for a submission
    # of what it has, with the shortfall declared; it never crashes.
    # The build round observed 40 BINDING on the two densest cases (45 and 54
    # calls wanted) — a rail that shapes a run violates ADR-0005 point 5, so
    # the default sits far above any observed need.
    max_tool_calls: int = 80
    cost_ceiling_usd: float = 2.0
    wall_clock_s: float = 1800.0


COMBOS: dict[str, Combo] = {
    # THE product combo (user decision, 2026-08-31): one model everywhere -
    # z-ai/glm-5.3-flash in the closed loop. Evidence: metric anchors 4/4 with
    # the project's best brier (0.011) at ~$0.03 a case; researcher questions
    # 11/15 coverage (tied with opus) and 7/20 fully-grounded facts (best of
    # every arm tested, frontier included); finds the audited Note 2.2 on p118
    # unaided. Trade accepted: 10-30 minutes a case. The opus/deepseek/qwen
    # comparisons live in evals/results/ and the design doc.
    "agentic": Combo(
        name="agentic",
        vision="qwen/qwen3.7-flash",
        judges=("deepseek/deepseek-v4-pro-0813", "qwen/qwen3.7-flash"),
        orchestration="agent",
        agent="z-ai/glm-5.3-flash",
        agent_max_tokens=16000,
        cost_ceiling_usd=1.0,
    ),
    # The evaluator speed option (user decision, 2026-09-01): the same closed
    # loop with deepseek-v4-flash driving it. Measured on the probe pair
    # (out/cba-impairment-fy26-vs-fy25-agentic-ds, out/ask-assess-whether-nab-*-agentic-ds):
    # 3.7-3.9 minutes and ~$0.01 a case, against agentic's 6-30 minutes.
    # The trade: movement numbers hold (they are tier-independent across the
    # bake-off), but the insight layer thins - the hard NAB question probe
    # scored 0/3 location coverage (evals/results/20260831-0916-agentic-ds-questions.md)
    # where glm-flash covered 11/15 across the question suite. Use this combo
    # to see the machine work quickly; use agentic for the answers that count.
    "fast": Combo(
        name="fast",
        vision="qwen/qwen3.7-flash",
        judges=("deepseek/deepseek-v4-pro-0813", "qwen/qwen3.7-flash"),
        orchestration="agent",
        agent="deepseek/deepseek-v4-flash-0731",
        agent_max_tokens=8000,
        cost_ceiling_usd=1.0,
    ),
}

# The default combo, named once: every CLI default and eval default reads it.
LIVE_COMBO = "agentic"


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
