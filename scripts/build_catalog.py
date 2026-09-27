#!/usr/bin/env python3
"""Merge the per-segment research files in catalog/raw/ into one deduplicated catalog.

Outputs:
  catalog/cyber_policies.json   full catalog (list of entries + metadata)
  catalog/cyber_policies.csv    same data, spreadsheet friendly
  catalog/gaps.json             carriers/products where no public wording was found
  CATALOG.md                    human-readable index grouped by region and carrier
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import parse_qsl, unquote, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "catalog" / "raw"
OUT_JSON = ROOT / "catalog" / "cyber_policies.json"
OUT_CSV = ROOT / "catalog" / "cyber_policies.csv"
OUT_GAPS = ROOT / "catalog" / "gaps.json"
OUT_MD = ROOT / "CATALOG.md"

FIELDS = [
    "id", "carrier", "product", "doc_type", "form_number", "edition_date",
    "region", "country", "target_market", "file_type", "is_direct_document",
    "is_latest_known", "title", "url", "notes", "segments",
]
DOC_TYPE_ORDER = {
    "policy_wording": 0, "specimen_policy": 1, "coverage_form": 2, "endorsement": 3,
    "declarations": 4, "summary": 5, "application": 6, "product_page": 7,
}
REGION_ALIASES = {
    "us": "US", "usa": "US", "united states": "US",
    "uk": "UK", "gb": "UK", "united kingdom": "UK", "lloyd's": "UK",
    "canada": "Canada", "ca": "Canada",
    "australia/nz": "Australia/NZ", "australia": "Australia/NZ", "au": "Australia/NZ",
    "nz": "Australia/NZ", "new zealand": "Australia/NZ",
    "europe": "Europe", "eu": "Europe",
    "asia": "Asia", "middle east": "Middle East", "africa": "Africa",
    "latin america": "Latin America", "latam": "Latin America",
}
TRACKING_PARAMS = re.compile(r"^(utm_|gclid|fbclid|mc_|_hs)", re.I)


def norm_url(url: str) -> str:
    """Canonical form used only for de-duplication."""
    parts = urlsplit(url.strip())
    query = urlencode([(k, v) for k, v in parse_qsl(parts.query) if not TRACKING_PARAMS.match(k)])
    path = unquote(parts.path).rstrip("/")
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    return urlunsplit(("https", host, path.lower(), query, ""))


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (text or "unknown").lower()).strip("-")[:60] or "unknown"


def infer_file_type(url: str, given: str | None) -> str:
    path = urlsplit(url).path.lower()
    for ext in ("pdf", "docx", "doc"):
        if path.endswith("." + ext):
            return ext
    return (given or "html").lower()


def norm_region(region: str | None) -> str:
    if not region:
        return "Other"
    return REGION_ALIASES.get(region.strip().lower(), region.strip())


def clean(value):
    if isinstance(value, str):
        value = value.strip()
        return value or None
    return value


def load_raw() -> tuple[list[dict], list[dict]]:
    entries, gaps = [], []
    for path in sorted(RAW_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            print(f"!! skipping {path.name}: {exc}", file=sys.stderr)
            continue
        segment = data.get("segment") or path.stem
        for entry in data.get("entries", []):
            entry["segments"] = [segment]
            entries.append(entry)
        for gap in data.get("gaps", []) or []:
            gap["segment"] = segment
            gaps.append(gap)
    return entries, gaps


def merge(entries: list[dict]) -> list[dict]:
    by_url: dict[str, dict] = {}
    for raw in entries:
        url = clean(raw.get("url"))
        if not url or not re.match(r"^https?://", url, re.I):
            continue
        entry = {k: clean(raw.get(k)) for k in FIELDS if k not in ("id", "segments")}
        entry["url"] = url
        entry["segments"] = raw["segments"]
        entry["region"] = norm_region(entry.get("region"))
        entry["file_type"] = infer_file_type(url, entry.get("file_type"))
        if entry.get("is_direct_document") is None:
            entry["is_direct_document"] = entry["file_type"] in ("pdf", "docx", "doc")
        key = norm_url(url)
        if key not in by_url:
            by_url[key] = entry
            continue
        kept = by_url[key]
        for field, value in entry.items():
            if field == "segments":
                kept["segments"] = sorted(set(kept["segments"]) | set(value))
            elif kept.get(field) in (None, "") and value not in (None, ""):
                kept[field] = value
            elif field == "notes" and value and value not in (kept.get("notes") or ""):
                kept["notes"] = f"{kept['notes']} | {value}"
    merged = list(by_url.values())
    for entry in merged:
        entry["id"] = f"{slug(entry.get('carrier'))[:30]}-{hashlib.sha1(norm_url(entry['url']).encode()).hexdigest()[:8]}"
    merged.sort(key=lambda e: (
        e["region"], (e.get("carrier") or "").lower(), (e.get("product") or "").lower(),
        DOC_TYPE_ORDER.get(e.get("doc_type") or "", 9), e["url"],
    ))
    return merged


def merge_gaps(gaps: list[dict], covered: set[str]) -> list[dict]:
    seen, out = set(), []
    for gap in gaps:
        carrier = clean(gap.get("carrier"))
        if not carrier:
            continue
        key = (carrier.lower(), (clean(gap.get("product")) or "").lower())
        if key in seen:
            continue
        seen.add(key)
        gap = {k: clean(v) for k, v in gap.items()}
        gap["carrier_has_other_documents"] = carrier.lower() in covered
        out.append(gap)
    out.sort(key=lambda g: (g["carrier"].lower(), (g.get("product") or "").lower()))
    return out


def write_csv(entries: list[dict]) -> None:
    with OUT_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        for entry in entries:
            row = dict(entry)
            row["segments"] = ";".join(entry["segments"])
            writer.writerow({k: row.get(k) for k in FIELDS})


def md_cell(value) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def write_markdown(entries: list[dict], gaps: list[dict], stats: dict) -> None:
    lines = [
        "# Cyber insurance policy catalog: SMB/SME wordings",
        "",
        f"Generated {stats['generated']} by `scripts/build_catalog.py` from {stats['segments']} research segments.",
        "",
        f"- **{stats['total']}** unique documents from **{stats['carriers']}** carriers/issuers",
        f"- **{stats['direct']}** direct document links (PDF/DOCX), {stats['total'] - stats['direct']} product pages only",
        "- By type: " + ", ".join(f"{k} {v}" for k, v in stats["by_type"].most_common()),
        "- By region: " + ", ".join(f"{k} {v}" for k, v in stats["by_region"].most_common()),
        "",
        "To download the files, run `python3 scripts/download_policies.py` (see README.md).",
        "",
    ]
    grouped: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for entry in entries:
        grouped[entry["region"]][entry.get("carrier") or "Unknown"].append(entry)
    for region in sorted(grouped):
        lines += [f"## {region}", ""]
        for carrier in sorted(grouped[region], key=str.lower):
            lines += [f"### {carrier}", "", "| Product | Type | Form / edition | Market | Document |", "|---|---|---|---|---|"]
            for e in grouped[region][carrier]:
                form = " ".join(x for x in (e.get("form_number"), e.get("edition_date") and f"({e['edition_date']})") if x)
                label = (e.get("file_type") or "link").upper() if e.get("is_direct_document") else "page"
                lines.append(
                    f"| {md_cell(e.get('product'))} | {md_cell(e.get('doc_type'))} | {md_cell(form)} "
                    f"| {md_cell(e.get('target_market'))} | [{label}]({e['url'].replace(' ', '%20')}) |"
                )
            lines.append("")
    if gaps:
        lines += ["## Gaps: no public wording found", "", "| Carrier | Product | Note |", "|---|---|---|"]
        for g in gaps:
            lines.append(f"| {md_cell(g.get('carrier'))} | {md_cell(g.get('product'))} | {md_cell(g.get('note'))} |")
        lines.append("")
    OUT_MD.write_text("\n".join(lines))


def main() -> None:
    raw_entries, raw_gaps = load_raw()
    entries = merge(raw_entries)
    carriers = {(e.get("carrier") or "").lower() for e in entries}
    gaps = merge_gaps(raw_gaps, carriers)
    stats = {
        "generated": date.today().isoformat(),
        "segments": len(list(RAW_DIR.glob("*.json"))),
        "raw": len(raw_entries),
        "total": len(entries),
        "carriers": len(carriers),
        "direct": sum(1 for e in entries if e.get("is_direct_document")),
        "by_type": Counter(e.get("doc_type") or "unknown" for e in entries),
        "by_region": Counter(e["region"] for e in entries),
    }
    OUT_JSON.write_text(json.dumps({
        "generated": stats["generated"],
        "description": "Publicly posted cyber insurance policy wordings, specimen forms and related documents for small and medium-sized businesses.",
        "count": stats["total"],
        "entries": entries,
    }, indent=2, ensure_ascii=False) + "\n")
    OUT_GAPS.write_text(json.dumps(gaps, indent=2, ensure_ascii=False) + "\n")
    write_csv(entries)
    write_markdown(entries, gaps, stats)
    print(f"raw entries: {stats['raw']}  unique: {stats['total']}  direct docs: {stats['direct']}  carriers: {stats['carriers']}  gaps: {len(gaps)}")
    print("by type:", dict(stats["by_type"]))
    print("by region:", dict(stats["by_region"]))


if __name__ == "__main__":
    main()
