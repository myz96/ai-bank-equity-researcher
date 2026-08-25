"""Fetch corpus documents listed in a manifest into the gitignored data/ cache.

Usage:
    uv run python scripts/fetch_corpus.py --manifest manifest/cba.json [--record]

Behaviour:
    - Downloads each document to data/raw/<bank>/<period>/<filename>.
    - A file that exists and matches its recorded sha256 is skipped.
    - A checksum mismatch is an error, never silently overwritten.
    - --record writes newly computed checksums back into the manifest
      (trust-on-first-use pinning).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    tmp = dest.with_suffix(dest.suffix + ".part")
    with urllib.request.urlopen(request, timeout=120) as response, tmp.open("wb") as out:
        while block := response.read(1 << 20):
            out.write(block)
    head = tmp.open("rb").read(5)
    if not head.startswith(b"%PDF") and dest.suffix == ".pdf":
        tmp.unlink()
        raise RuntimeError(f"{url} did not return a PDF (starts with {head!r})")
    tmp.rename(dest)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--record", action="store_true", help="write computed sha256 values back to the manifest")
    args = parser.parse_args()

    manifest_path = args.manifest if args.manifest.is_absolute() else REPO_ROOT / args.manifest
    manifest = json.loads(manifest_path.read_text())
    bank = manifest["bank"]
    failures = 0
    updated = False

    for doc in manifest["documents"]:
        dest = REPO_ROOT / "data" / "raw" / bank / doc["period"] / doc["filename"]
        label = f"{bank}/{doc['period']}/{doc['filename']}"
        recorded = doc.get("sha256")

        if dest.exists():
            actual = sha256_of(dest)
            if recorded is None:
                print(f"EXISTS   {label} (no recorded checksum)")
            elif actual == recorded:
                print(f"OK       {label}")
                continue
            else:
                print(f"MISMATCH {label}: recorded {recorded[:12]}…, actual {actual[:12]}…", file=sys.stderr)
                failures += 1
                continue
        else:
            try:
                download(doc["url"], dest)
            except Exception as exc:  # noqa: BLE001 - report and continue to next doc
                print(f"FAILED   {label}: {exc}", file=sys.stderr)
                failures += 1
                continue
            actual = sha256_of(dest)
            size_mb = dest.stat().st_size / (1 << 20)
            print(f"FETCHED  {label} ({size_mb:.1f} MiB)")
            if recorded is not None and actual != recorded:
                print(f"MISMATCH {label}: recorded {recorded[:12]}…, actual {actual[:12]}…", file=sys.stderr)
                failures += 1
                continue

        if recorded is None and args.record:
            doc["sha256"] = actual
            updated = True

    if updated:
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
        print(f"Recorded checksums into {manifest_path.relative_to(REPO_ROOT)}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
