"""The routing seams: every caller that answers a case or a question passes
through here (ADR-0005), so no caller can measure one shell while wearing
another's label. Routing lives beside the agent it routes to; config stays
data only (Codex architecture round 1: the lazy imports in config made it a
participant in a dependency cycle)."""

from __future__ import annotations

from ..config import COMBOS


def runner_for(combo_name: str):
    """The case runner (ADR-0005).

    Every caller that answers a case — the CLI and the eval harness — goes
    through this one function, or `evals run --combo agentic` silently measures
    one shell while wearing the other's label. The closed loop is the only
    shell left, and the function stays as the seam that keeps a caller honest.
    """
    _require_agent(combo_name)
    from .research_agent import run_agent_case

    return run_agent_case


def question_runner_for(combo_name: str):
    """The free-form question runner. The same rule as runner_for, over the
    other task: `ask` and `evals run --suite questions` reach the same closed
    loop. Every question caller passes (bank, question, combo, periods) and
    gets (output, out_dir), so none needs an adapter or a branch of its own."""
    _require_agent(combo_name)
    from .research_agent import run_agent_question

    return run_agent_question


def _require_agent(combo_name: str) -> None:
    """A combo that is not an agent combo has no shell to run.

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
