"""Local hybrid page retrieval: BM25 unioned with dense bge-small (ADR-0002).

Retrieval is POOLED across the task's whole corpus: one BM25 index over every
in-scope page (so idf is computed once and scores compare across documents)
and one pooled dense ranking. Per-document rank fusion looked comparable but
was not — every document's own top page scored 2.0, ties broke lexically on
doc_id, and the one relevant document in a thirteen-document scope fell out
of the global top eight (executed repro, Sol review round 3).
"""

from __future__ import annotations

import re
from functools import lru_cache

import numpy as np

from ..config import DATA_DIR
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
def _doc_embeddings(doc_path: str):
    """Dense page embeddings for one document, cached on disk by file stem."""
    doc = _DOCS[doc_path]
    texts = doc.page_texts()
    emb_cache = DATA_DIR / "cache" / "emb" / (doc.path.stem + ".npy")
    if emb_cache.exists():
        embeddings = np.load(emb_cache)
        # A stale cache (the PDF replaced with a different page count) would
        # shift every later document's rows against the wrong pages in the
        # pooled matrix (executed repro: B/p1's vector answered as A/p3).
        if embeddings.shape[0] == len(texts):
            return embeddings
    embeddings = _encoder().encode(
        [t[:2000] for t in texts], normalize_embeddings=True, show_progress_bar=False
    )
    emb_cache.parent.mkdir(parents=True, exist_ok=True)
    np.save(emb_cache, embeddings)
    return embeddings


@lru_cache(maxsize=8)
def _pool_index(doc_paths: tuple[str, ...]):
    """One BM25 index and one embedding matrix over a whole corpus scope."""
    from rank_bm25 import BM25Okapi

    pages: list[tuple[str, int]] = []
    tokens: list[list[str]] = []
    embeddings = []
    for path in doc_paths:
        doc = _DOCS[path]
        texts = doc.page_texts()
        embeddings.append(_doc_embeddings(path))
        for i, text in enumerate(texts):
            pages.append((path, i + 1))
            tokens.append(_tokenize(text) or ["empty"])
    return BM25Okapi(tokens), np.vstack(embeddings), pages


_DOCS: dict[str, Document] = {}


def retrieve_pool(
    docs: list[Document], query: str, top_k: int = 8
) -> list[tuple[Document, int, float]]:
    """Return (document, 1-based page, score) over the pooled scope: the union
    of the pooled BM25 top-k and the pooled dense top-k, reciprocal-rank
    fused. Scores compare across documents because the ranks are global."""
    for doc in docs:
        _DOCS[str(doc.path)] = doc
    bm25, embeddings, pages = _pool_index(tuple(str(doc.path) for doc in docs))

    scores = bm25.get_scores(_tokenize(query))
    bm25_top = sorted(range(len(pages)), key=lambda i: -scores[i])[:top_k]

    q = _encoder().encode([query], normalize_embeddings=True)
    sims = (embeddings @ q.T).ravel()
    dense_top = np.argsort(-sims)[:top_k].tolist()

    fused: dict[int, float] = {}
    for rank, i in enumerate(bm25_top):
        fused[i] = fused.get(i, 0.0) + 1.0 / (rank + 1)
    for rank, i in enumerate(dense_top):
        fused[i] = fused.get(i, 0.0) + 1.0 / (rank + 1)
    ranked = sorted(fused.items(), key=lambda kv: -kv[1])
    return [(_DOCS[pages[i][0]], pages[i][1], score) for i, score in ranked]
