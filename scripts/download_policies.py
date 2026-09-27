#!/usr/bin/env python3
"""Download every document listed in catalog/cyber_policies.json into policies/.

Files land in policies/<region>/<carrier>/<id>__<original-name>. A manifest recording the
status, HTTP code, size and SHA-256 of every attempt is written to
catalog/download_manifest.json, so a re-run skips files that already downloaded.

Standard library only. Examples:
  python3 scripts/download_policies.py                       # all direct documents
  python3 scripts/download_policies.py --region US --region UK
  python3 scripts/download_policies.py --doc-type policy_wording --doc-type specimen_policy
  python3 scripts/download_policies.py --include-pages       # also save HTML product pages
  python3 scripts/download_policies.py --retry-failed        # retry only failures from last run
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog" / "cyber_policies.json"
MANIFEST = ROOT / "catalog" / "download_manifest.json"
OUT_DIR = ROOT / "policies"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
MAGIC = {b"%PDF": "pdf", b"PK\x03\x04": "docx", b"\xd0\xcf\x11\xe0": "doc"}


def slug(text: str, limit: int = 60) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", text or "unknown").strip("-.")[:limit] or "unknown"


def safe_url(url: str) -> str:
    """Percent-encode spaces and other unsafe characters without double-encoding."""
    p = urlsplit(url)
    return urlunsplit((p.scheme, p.netloc, quote(unquote(p.path), safe="/:@!$&'()*+,;=-._~"), p.query, p.fragment))


def sniff(head: bytes, content_type: str) -> str:
    for magic, kind in MAGIC.items():
        if head.startswith(magic):
            return kind
    if "html" in content_type or head.lstrip()[:15].lower().startswith((b"<!doctype", b"<html")):
        return "html"
    return "bin"


def dest_for(entry: dict, kind: str) -> Path:
    name = Path(unquote(urlsplit(entry["url"]).path)).stem or "document"
    return OUT_DIR / slug(entry.get("region") or "Other") / slug(entry.get("carrier") or "Unknown") / f"{entry['id']}__{slug(name, 80)}.{kind}"


def fetch(entry: dict, timeout: int, retries: int) -> dict:
    record = {"id": entry["id"], "url": entry["url"], "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    request = urllib.request.Request(safe_url(entry["url"]), headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as resp:
                body = resp.read()
                content_type = resp.headers.get("Content-Type", "").lower()
                kind = sniff(body[:512], content_type)
                expected = entry.get("file_type") or "html"
                path = dest_for(entry, kind)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(body)
                status = "ok" if kind == expected or (expected == "html" and kind == "html") else f"ok_but_got_{kind}"
                record.update(
                    status=status, http_status=resp.status, final_url=resp.geturl(), content_type=content_type,
                    bytes=len(body), sha256=hashlib.sha256(body).hexdigest(), path=str(path.relative_to(ROOT)),
                )
                return record
        except urllib.error.HTTPError as exc:
            record.update(status="http_error", http_status=exc.code, error=str(exc))
            if exc.code in (400, 401, 403, 404, 410):
                return record
        except Exception as exc:  # noqa: BLE001 - record every failure and keep going
            record.update(status="error", error=f"{type(exc).__name__}: {exc}")
            if "Tunnel connection failed: 403" in str(exc):
                record["status"] = "blocked_by_network_policy"
                return record
        time.sleep(2 ** attempt)
    return record


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--region", action="append", help="only these regions (repeatable)")
    ap.add_argument("--doc-type", action="append", help="only these doc types (repeatable)")
    ap.add_argument("--include-pages", action="store_true", help="also save non-document product pages")
    ap.add_argument("--retry-failed", action="store_true", help="only retry entries that failed last run")
    ap.add_argument("--force", action="store_true", help="re-download files that already succeeded")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument("--retries", type=int, default=3)
    args = ap.parse_args()

    entries = json.loads(CATALOG.read_text())["entries"]
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}

    todo = []
    for e in entries:
        if not args.include_pages and not e.get("is_direct_document"):
            continue
        if args.region and e.get("region") not in args.region:
            continue
        if args.doc_type and e.get("doc_type") not in args.doc_type:
            continue
        prev = manifest.get(e["id"], {})
        done = str(prev.get("status", "")).startswith("ok") and (ROOT / prev.get("path", "")).exists()
        if done and not args.force:
            continue
        if args.retry_failed and (not prev or done):
            continue
        todo.append(e)

    print(f"{len(todo)} documents to fetch ({len(entries)} in catalog)")
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(fetch, e, args.timeout, args.retries): e for e in todo}
        for n, fut in enumerate(as_completed(futures), 1):
            rec = fut.result()
            manifest[rec["id"]] = rec
            print(f"[{n}/{len(todo)}] {rec['status']:<16} {rec.get('http_status', '')!s:<4} {rec['url']}", flush=True)
            if n % 25 == 0:
                MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    statuses: dict[str, int] = {}
    for rec in manifest.values():
        statuses[rec["status"]] = statuses.get(rec["status"], 0) + 1
    print("manifest totals:", statuses)


if __name__ == "__main__":
    main()
