"""Corpus access: manifests, cached page text, page rendering."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

import pymupdf

from .config import DATA_DIR, MANIFEST_DIR


class Document:
    def __init__(self, bank: str, meta: dict) -> None:
        self.bank = bank
        self.period: str = meta["period"]
        self.doc_type: str = meta["doc_type"]
        self.filename: str = meta["filename"]
        self.sha256: str | None = meta.get("sha256")
        self.path = DATA_DIR / "raw" / bank / self.period / self.filename

    @property
    def doc_id(self) -> str:
        return f"{self.bank}/{self.period}/{self.doc_type}"

    def page_texts(self) -> list[str]:
        cache = DATA_DIR / "cache" / "pages" / (Path(self.filename).stem + ".json")
        if cache.exists():
            return json.loads(cache.read_text())
        pdf = pymupdf.open(self.path)
        texts = [page.get_text() for page in pdf]
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(texts))
        return texts

    def render_page(self, page_no: int, zoom: float = 2.0) -> bytes:
        """page_no is 1-based PDF page number."""
        pdf = pymupdf.open(self.path)
        return pdf[page_no - 1].get_pixmap(matrix=pymupdf.Matrix(zoom, zoom)).tobytes("png")


@lru_cache(maxsize=None)
def load_documents(bank: str) -> list[Document]:
    manifest_path = MANIFEST_DIR / f"{bank.lower()}.json"
    if not manifest_path.exists():
        return []
    manifest = json.loads(manifest_path.read_text())
    docs = [Document(manifest["bank"], meta) for meta in manifest["documents"]]
    return [d for d in docs if d.path.exists() and d.path.suffix == ".pdf"]


def documents_for_period(bank: str, *periods: str) -> list[Document]:
    return [d for d in load_documents(bank) if d.period in periods]
