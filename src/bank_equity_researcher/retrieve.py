"""Local hybrid page retrieval: BM25 unioned with dense bge-small (ADR-0002)."""

from __future__ import annotations

import re
from functools import lru_cache

import numpy as np

from .config import DATA_DIR
from .corpus import Document

_ENCODER = None


def _encoder():
    global _ENCODER
    if _ENCODER is None:
        from sentence_transformers import SentenceTransformer

        _ENCODER = SentenceTransformer("BAAI/bge-small-en-v1.5")
    return _ENCODER


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


@lru_cache(maxsize=64)
def _doc_index(doc_path: str):
    """Build (bm25, embeddings) for a document; embeddings cached on disk."""
    from rank_bm25 import BM25Okapi

    doc = _DOCS[doc_path]
    texts = doc.page_texts()
    bm25 = BM25Okapi([_tokenize(t) or ["empty"] for t in texts])

    emb_cache = DATA_DIR / "cache" / "emb" / (doc.path.stem + ".npy")
    if emb_cache.exists():
        embeddings = np.load(emb_cache)
    else:
        embeddings = _encoder().encode(
            [t[:2000] for t in texts], normalize_embeddings=True, show_progress_bar=False
        )
        emb_cache.parent.mkdir(parents=True, exist_ok=True)
        np.save(emb_cache, embeddings)
    return bm25, embeddings, len(texts)


_DOCS: dict[str, Document] = {}


def retrieve(doc: Document, query: str, top_k: int = 6) -> list[tuple[int, float]]:
    """Return (1-based page, score): union of BM25 top-k and dense top-k.
    Score = reciprocal-rank fusion, so downstream page caps keep the most
    relevant pages instead of the lowest-numbered ones."""
    _DOCS[str(doc.path)] = doc
    bm25, embeddings, n_pages = _doc_index(str(doc.path))

    scores = bm25.get_scores(_tokenize(query))
    bm25_top = sorted(range(n_pages), key=lambda i: -scores[i])[:top_k]

    q = _encoder().encode([query], normalize_embeddings=True)
    sims = (embeddings @ q.T).ravel()
    dense_top = np.argsort(-sims)[:top_k].tolist()

    fused: dict[int, float] = {}
    for rank, i in enumerate(bm25_top):
        fused[i + 1] = fused.get(i + 1, 0.0) + 1.0 / (rank + 1)
    for rank, i in enumerate(dense_top):
        fused[i + 1] = fused.get(i + 1, 0.0) + 1.0 / (rank + 1)
    return sorted(fused.items(), key=lambda kv: -kv[1])
