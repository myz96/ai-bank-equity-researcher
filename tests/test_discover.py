"""Discovery writes manifests other code trusts (review round 10).

The round-9 gate refuses a doc_type outside schema.DOC_TYPES before the
manifest is written; until this file, no test imported the module and the
gate shipped unexecuted.
"""

from __future__ import annotations

import re

import pytest

from bank_equity_researcher.tools import discover as D
from bank_equity_researcher.validation.schema import DOC_TYPES


class _ScriptedLLM:
    """Stands in for LLM(); replies with one scripted 'done' action."""

    def __init__(self, documents):
        self._documents = documents
        self.usage = type(
            "U", (), {"calls": 1, "cost_usd": 0.0, "prompt_tokens": 0, "completion_tokens": 0}
        )()

    def chat_json(self, model, prompt, max_tokens):
        return {"action": "done", "documents": self._documents}


def _doc(doc_type):
    return {
        "period": "FY26",
        "doc_type": doc_type,
        "published": None,
        "url": "https://example.com/x.pdf",
        "filename": f"ZZT-FY26-{doc_type}.pdf",
    }


def test_a_doc_type_outside_the_vocabulary_is_refused_before_the_write(monkeypatch, tmp_path):
    """The hand-built MQG manifest shipped "mda" and lost slide-page numbering
    and the presentation walk tolerance in silence (review round 7). The gate
    turns that into a loud failure with the manifest unwritten."""
    monkeypatch.setattr(D, "LLM", lambda: _ScriptedLLM([_doc("mda")]))
    monkeypatch.setattr(D, "MANIFEST_DIR", tmp_path)
    with pytest.raises(RuntimeError, match="not in schema.DOC_TYPES"):
        D.discover("ZZT", ["FY26"], "https://example.com", "2026-09-01")
    assert not (tmp_path / "zzt.json").exists()


def test_a_vocabulary_doc_type_is_written(monkeypatch, tmp_path):
    monkeypatch.setattr(D, "LLM", lambda: _ScriptedLLM([_doc("results_announcement")]))
    monkeypatch.setattr(D, "MANIFEST_DIR", tmp_path)
    manifest = D.discover("ZZT", ["FY26"], "https://example.com", "2026-09-01")
    assert (tmp_path / "zzt.json").exists()
    assert manifest["documents"][0]["doc_type"] == "results_announcement"


def test_the_prompt_enumerates_only_vocabulary_terms():
    """A rename in schema.DOC_TYPES must not strand the prompt's own list:
    every term the prompt offers the model has to pass the round-9 gate."""
    enumerated = re.search(r'"doc_type":\s*\n?\s*"([a-z_|]+)"', D.PROMPT)
    assert enumerated, "the prompt no longer enumerates doc_type terms"
    terms = set(enumerated.group(1).split("|"))
    assert terms, "empty doc_type enumeration in the prompt"
    assert terms <= DOC_TYPES
