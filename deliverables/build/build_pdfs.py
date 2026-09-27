"""Build HTML and PDF versions of the Harborline deliverables from Markdown.

Usage: python3 deliverables/build/build_pdfs.py
Needs: pip install markdown playwright; a Chromium binary (CHROME env var or the Playwright default path).
"""
import html
import os
import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
OUT_HTML = ROOT / "html"
OUT_PDF = ROOT / "pdf"
CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")

DOCS = [
    ("Harborline_Policy.md", "Harborline Cyber Protection Policy (Specimen)", "HIC-CY-100 (10/26) · Specimen"),
    ("Harborline_Application_Cedar_Ridge.md", "Cyber Protection Policy Application (Sample)", "HIC-CY-APP (10/26) · Sample"),
    ("Harborline_Decision_Rationale.md", "Decision Rationale", "Harborline Cyber Protection Policy"),
]

CSS = """
@page { size: Letter; margin: 0.8in 0.75in 0.85in 0.75in; }
html { font-family: "Source Serif 4", Georgia, "Times New Roman", serif; font-size: 10.5pt; color: #1b1b1b; }
body { line-height: 1.42; margin: 0; }
h1 { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 20pt; color: #0b3954; margin: 0 0 6pt; }
h2 { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 14pt; color: #0b3954; border-bottom: 1.5pt solid #0b3954;
     padding-bottom: 3pt; margin: 18pt 0 8pt; break-after: avoid; }
h3 { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 11.5pt; color: #0b3954; margin: 12pt 0 5pt; break-after: avoid; }
p, li { orphans: 3; widows: 3; }
p { margin: 0 0 6pt; }
ol, ul { margin: 0 0 6pt 18pt; padding: 0; }
li { margin: 0 0 3pt; }
table { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; font-size: 9pt; break-inside: auto; }
tr { break-inside: avoid; }
th, td { border: 0.6pt solid #9aa5b1; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #e8eef3; font-family: "Helvetica Neue", Arial, sans-serif; }
blockquote { margin: 6pt 0; padding: 6pt 10pt; border-left: 3pt solid #c0392b; background: #fbeeee; }
code { font-size: 9pt; }
.pagebreak { break-before: page; }
.footer-note { color: #555; font-size: 8.5pt; }
"""

MAJOR = re.compile(r"^## (Important notices|Policy declarations|Section I\.|Section II\.|Section III\.|Section IV\.|Section V\.|Back page|Part 1:|For underwriter use|1\. Who|Sources)")


def md_to_html(md_text: str) -> str:
    lines = md_text.splitlines()
    out = []
    first_h2 = True
    for line in lines:
        if line.startswith("## ") and MAJOR.match(line) and not first_h2:
            out.append('<div class="pagebreak"></div>')
        if line.startswith("## "):
            first_h2 = False
        out.append(line)
    return markdown.markdown("\n".join(out), extensions=["tables", "sane_lists"])


def build(md_name: str, title: str, footer: str) -> Path:
    src = ROOT / md_name
    body = md_to_html(src.read_text(encoding="utf-8"))
    OUT_HTML.mkdir(exist_ok=True)
    OUT_PDF.mkdir(exist_ok=True)
    page = f"""<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<style>{CSS}</style></head><body>{body}</body></html>"""
    html_path = OUT_HTML / (src.stem + ".html")
    html_path.write_text(page, encoding="utf-8")
    pdf_path = OUT_PDF / (src.stem + ".pdf")
    footer_tpl = (
        '<div style="font-size:7.5pt;width:100%;padding:0 0.75in;color:#666;display:flex;justify-content:space-between;">'
        f"<span>{html.escape(footer)}</span>"
        '<span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
    )
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        page_obj = browser.new_page()
        page_obj.goto(html_path.as_uri())
        page_obj.pdf(
            path=str(pdf_path), format="Letter", print_background=True, prefer_css_page_size=True,
            display_header_footer=True, header_template="<span></span>", footer_template=footer_tpl,
            margin={"top": "0.8in", "bottom": "0.85in", "left": "0.75in", "right": "0.75in"},
        )
        browser.close()
    return pdf_path


if __name__ == "__main__":
    for name, title, footer in DOCS:
        p = build(name, title, footer)
        print(p, p.stat().st_size, "bytes")
    sys.exit(0)
