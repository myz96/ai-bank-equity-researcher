"""The package layering, pinned mechanically.

Two dependency cycles are broken and must stay broken: validation importing
tools (which dragged pymupdf into the contracts layer), and config importing
agent (which made configuration a routing participant).
"""

from __future__ import annotations

import ast
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src" / "bank_equity_researcher"


def _relative_imports(path: Path):
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.ImportFrom) and node.level and node.module:
            yield node.module


def test_validation_never_imports_tools():
    for path in (SRC / "validation").glob("*.py"):
        for module in _relative_imports(path):
            assert not module.startswith("tools"), (
                f"{path.name} imports {module}: validation must stay free of the "
                "pymupdf-backed tools layer"
            )


def test_config_never_imports_the_agent():
    for module in _relative_imports(SRC / "config.py"):
        assert not module.startswith("agent"), (
            f"config.py imports {module}: routing lives in agent/routing.py and "
            "config stays data only"
        )
