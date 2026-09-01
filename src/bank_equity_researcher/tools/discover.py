"""The agentic pocket (ADR-0004): document discovery for a bank with no
manifest. The model navigates the bank's website until it can name the result
documents for the requested periods. The loop, the tools, and the hand-off are
deterministic code; only the navigation choices are the model's.
"""

from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from urllib.parse import urljoin

import httpx

from ..config import MANIFEST_DIR
from ..llm import LLM
from ..validation.schema import DOC_TYPES
from . import corpus

DISCOVER_MODEL = "deepseek/deepseek-v4-pro-0813"
MAX_STEPS = 15
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)

PROMPT = """You are a document-discovery agent for banking equity research.
Today is {today}. Target: find {bank}'s results documents for periods
{periods}. For each period you must locate: the results announcement / results
book PDF (the detailed one with financial statements or MD&A) and the investor
presentation / discussion pack PDF.

You navigate the web one step at a time. Each turn, reply with JSON only:
- {{"action": "fetch", "url": "<absolute url>", "why": "<10 words>"}} to open a page
- {{"action": "done", "documents": [{{"period": "<e.g. 1H26>", "doc_type":
   "results_announcement|results_book|investor_presentation|investor_discussion_pack",
   "published": "<YYYY-MM-DD or null>", "url": "<direct PDF url>",
   "filename": "<BANK-PERIOD-doctype.pdf>"}}]}} when you have direct PDF URLs
- {{"action": "give_up", "reason": "..."}} if truly stuck

Rules: prefer the bank's own investor-relations pages. PDF links end in .pdf
or are labelled as PDFs. Do not invent URLs — only use links you have seen in
fetched pages. Australian banks with September year-end report half-years
(ended March) around May and full years around November.

History so far:
{history}"""


class _LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href = dict(attrs).get("href")
            self._text = []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data.strip())

    def handle_endtag(self, tag):
        if tag == "a" and self._href:
            self.links.append((self._href, " ".join(t for t in self._text if t)[:80]))
            self._href = None


def fetch_page(url: str) -> dict:
    response = httpx.get(url, headers={"User-Agent": USER_AGENT}, timeout=60, follow_redirects=True)
    content_type = response.headers.get("content-type", "")
    if "pdf" in content_type or url.lower().endswith(".pdf"):
        return {"url": url, "kind": "pdf", "bytes": len(response.content)}
    html = response.text
    parser = _LinkParser()
    try:
        parser.feed(html)
    except Exception:  # noqa: BLE001, S110 - a page that will not parse still yields its raw text below
        pass
    links = []
    seen = set()
    for href, text in parser.links:
        absolute = urljoin(str(response.url), href)
        if absolute in seen or absolute.startswith(("mailto:", "javascript:")):
            continue
        seen.add(absolute)
        if absolute.lower().endswith(".pdf") or any(
            k in (absolute + text).lower()
            for k in ("result", "investor", "shareholder", "presentation", "report", "announce", "half", "full-year")
        ):
            links.append(f"{absolute} | {text}")
    text_only = re.sub(r"<[^>]+>", " ", html)
    text_only = re.sub(r"\s+", " ", text_only)
    return {"url": url, "kind": "html", "text": text_only[:1200], "links": links[:80]}


def discover(bank: str, periods: list[str], seed_url: str, today: str) -> dict:
    """Run the discovery loop; write manifest/<bank>.json; return the manifest."""
    llm = LLM()
    history: list[str] = [f"Seed page available: {seed_url}"]
    for _ in range(MAX_STEPS):
        prompt = PROMPT.format(
            bank=bank, periods=", ".join(periods), today=today, history="\n\n".join(history[-8:])
        )
        reply = llm.chat_json(DISCOVER_MODEL, prompt, max_tokens=2000)
        action = reply.get("action")
        if action == "fetch":
            url = reply["url"]
            try:
                page = fetch_page(url)
            except Exception as exc:  # noqa: BLE001
                history.append(f"FETCH {url} FAILED: {exc}")
                continue
            if page["kind"] == "pdf":
                history.append(f"FETCHED {url}: this is a PDF ({page['bytes']} bytes).")
            else:
                history.append(
                    f"FETCHED {url}\nTEXT: {page['text']}\nLINKS:\n" + "\n".join(page["links"])
                )
        elif action == "done":
            # The prompt names the 4 doc types discovery TARGETS; the model may
            # answer with any term in the shared vocabulary. A value outside it
            # would silently lose slide-page numbering and the presentation
            # walk tolerance (the hand-built MQG manifest did exactly that), so
            # an unknown term fails here, loudly, before the manifest is
            # written.
            for d in reply.get("documents", []):
                if d.get("doc_type") not in DOC_TYPES:
                    raise RuntimeError(
                        f"discovery returned doc_type {d.get('doc_type')!r} for "
                        f"{d.get('filename')}, which is not in schema.DOC_TYPES; "
                        "map it to an existing term or extend the vocabulary "
                        "with its consumers checked"
                    )
            manifest = {
                "bank": bank.upper(),
                "notes": f"Discovered by the discovery agent ({DISCOVER_MODEL}) on {today}; "
                "URLs seen on the bank's own pages. scripts/fetch_corpus.py "
                "downloads and hashes them.",
                "documents": [
                    {
                        "period": d["period"],
                        "doc_type": d["doc_type"],
                        "published": d.get("published"),
                        "url": d["url"],
                        "filename": d["filename"],
                        "sha256": None,
                    }
                    for d in reply.get("documents", [])
                ],
            }
            path = MANIFEST_DIR / f"{bank.lower()}.json"
            path.write_text(json.dumps(manifest, indent=2) + "\n")
            # The corpus caches predate this manifest; a long-lived process
            # that discovers and then researches would read stale scope.
            corpus.load_documents.cache_clear()
            corpus._assert_distinct_stems.cache_clear()
            manifest["_usage"] = {
                "calls": llm.usage.calls,
                "cost_usd": round(llm.usage.cost_usd, 4),
                "tokens": f"{llm.usage.prompt_tokens} in / {llm.usage.completion_tokens} out",
            }
            return manifest
        elif action == "give_up":
            raise RuntimeError(f"discovery gave up: {reply.get('reason')}")
        else:
            history.append(f"Your reply was not a valid action: {str(reply)[:200]}")
    raise RuntimeError(f"discovery exceeded {MAX_STEPS} steps without finishing")
