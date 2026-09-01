"""The package layering, pinned mechanically.

Two dependency cycles are broken and must stay broken: validation importing
tools (which dragged pymupdf into the contracts layer), and config importing
agent (which made configuration a routing participant).
"""

from __future__ import annotations

import ast
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src" / "bank_equity_researcher"


PACKAGE = "bank_equity_researcher"


def _imported_subpackages(path: Path):
    """Every subpackage this file imports, however the import is spelt.

    A relative import ("from ..tools import corpus") and an absolute one
    ("from bank_equity_researcher.tools import corpus") reach the same module,
    so a walker that reads only relative imports pins nothing: the absolute
    spelling walks straight past it. Plain `import` statements count too.
    """
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.ImportFrom):
            if node.level and node.module:
                yield node.module
            elif node.level or node.module == PACKAGE:
                # `from .. import tools` carries no module, and `from
                # bank_equity_researcher import tools` carries only the
                # package root: in both, the NAMES are the modules (the
                # walker's two bypasses, Sol architecture round 4).
                for alias in node.names:
                    yield alias.name
            elif node.module:
                yield _strip_package(node.module)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                yield _strip_package(alias.name)


def _strip_package(module: str) -> str:
    """An absolute name reduced to the part the layering rules talk about."""
    return module[len(PACKAGE) + 1:] if module.startswith(f"{PACKAGE}.") else module


def test_validation_never_imports_tools():
    for path in (SRC / "validation").glob("*.py"):
        for module in _imported_subpackages(path):
            assert not module.startswith("tools"), (
                f"{path.name} imports {module}: validation must stay free of the "
                "pymupdf-backed tools layer"
            )


def test_config_never_imports_the_agent():
    for module in _imported_subpackages(SRC / "config.py"):
        assert not module.startswith("agent"), (
            f"config.py imports {module}: routing lives in agent/routing.py and "
            "config stays data only"
        )


def test_the_walker_reads_every_import_spelling(tmp_path):
    """The layering pins are only as good as the walker: each spelling below
    must surface `tools`, or a cycle could return through the blind one."""
    spellings = [
        "from ..tools.corpus import DOC_TYPES",
        "from .. import tools",
        "from bank_equity_researcher import tools",
        "from bank_equity_researcher.tools import corpus",
        "import bank_equity_researcher.tools.corpus",
    ]
    for src in spellings:
        f = tmp_path / "probe.py"
        f.write_text(src)
        found = list(_imported_subpackages(f))
        assert any(m == "tools" or m.startswith("tools") for m in found), (src, found)

