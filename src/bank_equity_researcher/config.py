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
    "deepseek/deepseek-v4-pro-0813": (1.122, 3.366),
    "z-ai/glm-5.3": (1.40, 4.40),
    # Mid-tier reasoning candidates for the research loop (user, 2026-08-31):
    # opus is too expensive to run often; these price the closed loop at
    # cents per case. Catalogue prices read live 2026-08-31.
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
    extract: str
    vision: str
    author: str
    # The author needs room to reason; glm-5.3 ignores the reasoning-off flag
    # (ticket 14), so its budget must cover reasoning + answer.
    author_max_tokens: int
    judges: tuple[str, str]
    # Which orchestration shell answers a case. "agent", the closed-loop
    # tool-use research agent (ADR-0005), is the only one left: ticket 33 wave
    # 3 froze the open-loop "pipeline" shell at the tag
    # `pipeline-baseline-final`. The field stays as the seam runner_for reads.
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
    # The closed-loop research agent (ADR-0005). The default combo runs the
    # strongest reliably tool-calling model in the OpenRouter catalogue:
    # anthropic/claude-opus-5 is the newest and the top of the Opus line
    # (published 2026-07-24, above claude-sonnet-5 and claude-fable-5), and a
    # live probe confirmed it emits a well-formed tool call, reads the result
    # and calls the next tool.
    "agentic": Combo(
        name="agentic",
        # The agent reads charts through the same vision tool the pipeline
        # uses; extract/author stay filled so the combo answers every caller.
        extract="anthropic/claude-opus-5",
        vision="anthropic/claude-opus-5",
        author="anthropic/claude-opus-5",
        author_max_tokens=16000,
        judges=("deepseek/deepseek-v4-pro-0813", "qwen/qwen3.7-flash"),
        orchestration="agent",
        agent="anthropic/claude-opus-5",
        agent_max_tokens=8000,
        # The densest anchor case cost $1.57; a $2 ceiling was close enough to
        # shape behaviour. $5 is a pure runaway-catch.
        cost_ceiling_usd=5.0,
    ),
    # Mid-tier reasoner in the closed loop (user candidate 2026-08-31): a
    # reasoning model at 1/70th the opus price. If it holds the agentic
    # quality bar it becomes the default's price point.
    # Speed candidate for iteration loops (user, 2026-08-31): deepseek's
    # flash tier is priced near qwen but reasons less per token than
    # glm-5.3-flash, so a case should finish in minutes, not tens of minutes.
    # Probe first; it earns a place only if it holds the p118 bar.
    "agentic-ds": Combo(
        name="agentic-ds",
        extract="qwen/qwen3.7-flash",
        vision="qwen/qwen3.7-flash",
        author="deepseek/deepseek-v4-flash-0731",
        author_max_tokens=16000,
        judges=("deepseek/deepseek-v4-pro-0813", "qwen/qwen3.7-flash"),
        orchestration="agent",
        agent="deepseek/deepseek-v4-flash-0731",
        agent_max_tokens=16000,
        cost_ceiling_usd=1.0,
    ),
    "agentic-glm": Combo(
        name="agentic-glm",
        extract="qwen/qwen3.7-flash",
        vision="qwen/qwen3.7-flash",
        author="z-ai/glm-5.3-flash",
        author_max_tokens=16000,
        judges=("deepseek/deepseek-v4-pro-0813", "qwen/qwen3.7-flash"),
        orchestration="agent",
        agent="z-ai/glm-5.3-flash",
        agent_max_tokens=16000,
        cost_ceiling_usd=1.0,
    ),
    # A comparison arm, never the product (ADR-0005 point 4): it measures what
    # the model tier buys INSIDE a closed loop. qwen3.7-flash is the cheapest
    # model in the catalogue that tool-called reliably on the live probe;
    # z-ai/glm-5.3 is the documented fallback if it stops doing so.
    "agentic-cheap": Combo(
        name="agentic-cheap",
        extract="qwen/qwen3.7-flash",
        vision="qwen/qwen3.7-flash",
        author="qwen/qwen3.7-flash",
        author_max_tokens=8000,
        judges=("deepseek/deepseek-v4-pro-0813", "qwen/qwen3.7-flash"),
        orchestration="agent",
        agent="qwen/qwen3.7-flash",
        agent_max_tokens=8000,
        cost_ceiling_usd=0.50,
    ),
}


def runner_for(combo_name: str):
    """The case runner (ADR-0005).

    Every caller that answers a case — the CLI and the eval harness — goes
    through this one function, or `evals run --combo agentic` silently measures
    one shell while wearing the other's label (Codex architecture critique
    2026-08-30, finding 1). The open-loop shell used to be the other branch
    here; ticket 33 wave 3 froze it at the tag `pipeline-baseline-final` and
    deleted it, so the closed loop is the only shell. The function stays
    because it is the seam that kept the two honest, and every caller already
    goes through it. The import is lazy so config stays free of shell
    dependencies.
    """
    _require_agent(combo_name)
    from .research_agent import run_agent_case

    return run_agent_case


def question_runner_for(combo_name: str):
    """The free-form question runner. The same rule as runner_for, over the
    other task: `ask` and `evals run --suite questions` reach the same closed
    loop. Both runners take (bank, question, combo, periods) and return
    (output, out_dir), so no caller needs an adapter or a branch of its own."""
    _require_agent(combo_name)
    from .research_agent import run_agent_question

    return run_agent_question


def _require_agent(combo_name: str) -> None:
    """A combo that is not an agent combo has no shell to run since wave 3.

    Saved artifacts from the deleted arm stay readable and `evals rescore`
    still scores them by slug, so this refuses only a fresh RUN.
    """
    combo = COMBOS.get(combo_name)
    if combo is None:
        raise KeyError(
            f"unknown combo: {combo_name} (known: {', '.join(sorted(COMBOS))}). "
            "The open-loop combos 'cheap' and 'normal' were frozen at the git tag "
            "pipeline-baseline-final and removed from main."
        )
    if combo.orchestration != "agent":
        raise ValueError(f"combo {combo_name} names no orchestration shell")


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
