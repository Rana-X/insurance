#!/usr/bin/env python3
"""Build the take-home PDFs from the HTML sources in src/.

  python3 build.py            # build all documents plus the combined submission PDF
  python3 build.py policy     # build a single document
  python3 build.py --png      # also render PNG page previews into build/ for review
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from pypdf import PdfWriter
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "pdf"
PREVIEW = ROOT / "build"

LOGO = (
    '<svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">'
    '<rect width="32" height="32" rx="6" fill="#0e6b73"/>'
    '<path d="M16 5.5 L20 14.5 H12 Z" fill="#ffffff"/>'
    '<rect x="14.4" y="14.5" width="3.2" height="5.5" fill="#ffffff"/>'
    '<path d="M5 22.5 Q8.5 19.5 12 22.5 T19 22.5 T26 22.5" stroke="#ffffff" stroke-width="1.9" fill="none"/>'
    '<path d="M5 26.5 Q8.5 23.5 12 26.5 T19 26.5 T26 26.5" stroke="#ffffff" stroke-width="1.9" fill="none" opacity="0.65"/>'
    "</svg>"
)

DOCS = {
    "policy": {
        "title": "Harborline Cyber Protection Policy (Specimen)",
        "css": ["base.css", "policy.css"],
        "parts": ["policy_01_front.html", "policy_02_toc.html", "policy_03_form.html", "policy_03b_form.html", "policy_04_back.html"],
        "pdf": "01_Harborline_Cyber_Protection_Policy.pdf",
    },
    "application": {
        "title": "Harborline Cyber Protection Policy Application (Completed Sample)",
        "css": ["base.css", "application.css"],
        "parts": ["application.html"],
        "pdf": "02_Sample_Application_Cedar_Ridge.pdf",
    },
    "rationale": {
        "title": "Decision Rationale: Harborline Cyber Protection Policy",
        "css": ["base.css", "rationale.css"],
        "parts": ["rationale.html"],
        "pdf": "03_Decision_Rationale.pdf",
    },
}
COMBINED = "Harborline_Cyber_Policy_Submission.pdf"


def build(name: str, png: bool) -> Path:
    doc = DOCS[name]
    body = "\n".join((SRC / p).read_text() for p in doc["parts"] if (SRC / p).exists())
    body = body.replace("{{LOGO}}", LOGO)
    body = (body.replace("{{YES}}", '<span class="yn"><span class="cb on"></span>Yes <span class="cb"></span>No</span>')
                .replace("{{NO}}", '<span class="yn"><span class="cb"></span>Yes <span class="cb on"></span>No</span>')
                .replace("{{X}}", '<span class="cb on"></span>')
                .replace("{{O}}", '<span class="cb"></span>'))
    # keep lead-in lines ("... means:", "... made:") on the same page as the list that follows
    body = re.sub(r'<p class="([^"]*)"((?:(?!</p>).)*?:)</p>', lambda m: f'<p class="{m.group(1)} lead"{m.group(2)}</p>', body, flags=re.S)
    body = re.sub(r'<p>((?:(?!</p>).)*?:)</p>', r'<p class="lead">\1</p>', body, flags=re.S)
    links = "\n".join(f'<link rel="stylesheet" href="{c}">' for c in doc["css"])
    html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{doc["title"]}</title>{links}</head><body>{body}</body></html>'
    OUT.mkdir(exist_ok=True)
    target = OUT / doc["pdf"]
    HTML(string=html, base_url=str(SRC) + "/").write_pdf(target, pdf_variant=None)
    print(f"built {target.relative_to(ROOT)}")
    if png:
        import pymupdf as fitz

        PREVIEW.mkdir(exist_ok=True)
        for old in PREVIEW.glob(f"{name}-*.png"):
            old.unlink()
        with fitz.open(target) as pdf:
            for i, page in enumerate(pdf, 1):
                page.get_pixmap(dpi=100).save(PREVIEW / f"{name}-{i:02d}.png")
            print(f"  {len(pdf)} pages, previews in build/")
    return target


def combine(paths: list[Path]) -> None:
    writer = PdfWriter()
    labels = {"policy": "Policy (with Declarations)", "application": "Sample Application", "rationale": "Decision Rationale"}
    for name, path in zip(DOCS, paths):
        writer.append(str(path), outline_item=labels[name])
    writer.add_metadata({"/Title": "Harborline Cyber Protection Policy: Specimen Policy, Sample Application and Decision Rationale"})
    with open(OUT / COMBINED, "wb") as fh:
        writer.write(fh)
    print(f"built pdf/{COMBINED}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    png = "--png" in sys.argv
    names = args or list(DOCS)
    built = [build(n, png) for n in names]
    if not args:
        combine(built)
