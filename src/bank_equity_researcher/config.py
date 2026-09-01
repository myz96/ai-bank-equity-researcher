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
    # THE product combo (user decision, 2026-08-31, iteration close): one
    # model everywhere - z-ai/glm-5.3-flash in the closed loop. Evidence:
    # metric anchors 4/4 with the project's best brier (0.011) at ~$0.03 a
    # case; researcher questions 11/15 coverage (tied with opus) and 7/20
    # fully-grounded facts (best of every arm tested, frontier included);
    # finds the audited Note 2.2 on p118 unaided. Trade accepted: 10-30
    # minutes a case. Opus/deepseek/qwen comparisons live in
    # evals/results/ and the design doc; their combos were retired with
    # the collapse (git history has them).
    "agentic": Combo(
        name="agentic",
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

    Saved artifacts from a retired arm stay readable, and `evals rescore` and
    `evals judge` still read them by slug, so this refuses only a fresh RUN.
    """
    combo = COMBOS.get(combo_name)
    if combo is None:
        raise KeyError(
            f"unknown combo: {combo_name} (known: {', '.join(sorted(COMBOS))}). "
            "Every other combo is retired and lives in git history: the open-loop "
            "'cheap' and 'normal' at the tag pipeline-baseline-final, and the "
            "closed-loop arms retired with the collapse. Their saved artifacts stay "
            "readable — `evals rescore` and `evals judge` take a retired name as a "
            "slug and run no shell."
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
