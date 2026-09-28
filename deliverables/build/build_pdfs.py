"""Build HTML and PDF versions of the cyber policy deliverables, plus the submission package.

Usage: python3 deliverables/build/build_pdfs.py
Needs: pip install markdown playwright pypdf; a Chromium binary (CHROME env var or the Playwright default path).
"""
import html
import os
import re
import shutil
import sys
from pathlib import Path

import markdown
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
OUT_HTML = ROOT / "html"
OUT_PDF = ROOT / "pdf"
PKG = ROOT / "package" / "Corgi_Cyber_Policy_Package"
CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")

DOCS = [
    # source, title, footer, package name
    ("Submission_Guide.md", "Submission Guide", "Cyber Protection Policy · Submission Guide", "00_Submission_Guide.pdf"),
    ("Cyber_Protection_Policy.md", "Cyber Protection Policy (Specimen)", "Corgi Insurance Company, Inc. · CORG-CY-0200 (10/26) · Specimen", "01_Cyber_Protection_Policy_Specimen.pdf"),
    ("Sample_Application_Cedar_Ridge.md", "Cyber Protection Policy Application (Sample)", "CORG-CY-0202 (10/26) · Sample", "02_Sample_Application_Cedar_Ridge.pdf"),
    ("Decision_Rationale.md", "Decision Rationale", "Cyber Protection Policy · Decision Rationale", "03_Decision_Rationale.pdf"),
]

CSS = """
@page { size: Letter; margin: 0.8in 0.75in 0.85in 0.75in; }
html { font-family: "Source Serif 4", Georgia, "Times New Roman", serif; font-size: 10.5pt; color: #1b1b1b; }
body { line-height: 1.42; margin: 0; }
h1 { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 20pt; color: #0b3954; margin: 0 0 8pt; }
h2 { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 14pt; color: #0b3954; border-bottom: 1.5pt solid #0b3954;
     padding-bottom: 3pt; margin: 18pt 0 8pt; break-after: avoid; }
h3 { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 11.5pt; color: #0b3954; margin: 12pt 0 5pt; break-after: avoid; }
h4 { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 10.5pt; color: #0b3954; margin: 10pt 0 4pt; break-after: avoid; }
p, li { orphans: 3; widows: 3; }
p { margin: 0 0 6pt; }
ol, ul { margin: 0 0 6pt 18pt; padding: 0; }
li { margin: 0 0 3pt; }
table { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; font-size: 9pt; }
table.keep { break-inside: avoid; }
tr { break-inside: avoid; }
th, td { border: 0.6pt solid #9aa5b1; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #e8eef3; font-family: "Helvetica Neue", Arial, sans-serif; }
blockquote { margin: 6pt 0; padding: 6pt 10pt; border-left: 3pt solid #c0392b; background: #fbeeee; }
a { color: #0b5394; text-decoration: none; word-break: break-all; }
.pagebreak { break-before: page; }
.cover { text-align: center; padding-top: 0.5in; }
.cover-insurer { font-family: "Helvetica Neue", Arial, sans-serif; font-weight: bold; letter-spacing: 2pt; color: #0b3954; font-size: 12pt; margin-bottom: 22pt; }
.cover h1 { font-size: 30pt; margin: 0 0 6pt; }
.cover-sub { font-size: 13pt; margin: 0 0 4pt; }
.cover-form { font-size: 9.5pt; color: #555; margin: 0 0 26pt; }
.cover-notice { border: 1.2pt solid #0b3954; padding: 8pt 14pt 4pt; text-align: left; margin: 0 0.25in 16pt; }
.cover-report { margin: 0 0.25in 18pt; }
table.cover-contents { width: 55%; margin: 0 auto 26pt; font-size: 10.5pt; }
table.cover-contents td { border: none; border-bottom: 0.5pt dotted #9aa5b1; text-align: left; padding: 3pt 2pt; }
.cover-witness { font-size: 9pt; text-align: left; margin: 0 0.25in 4pt; }
table.cover-sign { width: 90%; margin: 0 auto; }
table.cover-sign td { border: none; text-align: center; padding-top: 26pt; font-size: 9.5pt; }
"""

# Light diagonal watermark on every page of the specimen policy.
SPECIMEN_CSS = """
body::before { content: "SPECIMEN"; position: fixed; top: 40%; left: 0; right: 0; text-align: center;
  font: bold 110pt "Helvetica Neue", Arial, sans-serif; color: rgba(11, 57, 84, 0.05);
  transform: rotate(-35deg); z-index: -1; }
"""

MAJOR = re.compile(
    r"^## (Important Notices|Declarations|Section I\.|Section II\.|Section III\.|Section IV\.|Section V\.|"
    r"Part 1:|For underwriter use|Sources)"
)
LIST_ITEM = re.compile(r"^(- |\d+\. )")
URL = re.compile(r"(?<![<(\"])(https?://[^\s<>|)]+)")


def preprocess(md_text: str) -> str:
    out = []
    first_h2 = True
    for line in md_text.splitlines():
        # A list must follow a blank line, or Markdown runs it into the paragraph above.
        if LIST_ITEM.match(line) and out and out[-1].strip() and not LIST_ITEM.match(out[-1]) \
                and not out[-1].startswith("|") and not out[-1].startswith("    "):
            out.append("")
        if line.startswith("## ") and MAJOR.match(line) and not first_h2:
            out.append('<div class="pagebreak"></div>')
            out.append("")
        if line.startswith("## "):
            first_h2 = False
        # Bare URLs become autolinks, which also protects underscores from emphasis.
        line = URL.sub(lambda m: "<" + m.group(1).rstrip(".,;") + ">" + m.group(1)[len(m.group(1).rstrip(".,;")):], line)
        out.append(line)
    return "\n".join(out)


def postprocess(body: str) -> str:
    # Keep short tables on one page.
    def mark(m):
        rows = m.group(0).count("<tr>")
        return m.group(0).replace("<table>", '<table class="keep">', 1) if rows <= 8 else m.group(0)
    return re.sub(r"<table>.*?</table>", mark, body, flags=re.S)


GUIDE_CSS = "html { font-size: 9.6pt; } table { font-size: 8.4pt; margin: 2pt 0 6pt; } h1 { font-size: 17pt; } h3 { margin: 7pt 0 3pt; } li, p { margin-bottom: 2pt; }"


def build(md_name: str, title: str, footer: str, fill: dict | None = None) -> Path:
    src = ROOT / md_name
    text = src.read_text(encoding="utf-8")
    for k, v in (fill or {}).items():
        text = text.replace("{" + k + "}", str(v))
    body = postprocess(markdown.markdown(preprocess(text), extensions=["tables", "sane_lists"]))
    extra_css = GUIDE_CSS if md_name.startswith("Submission_Guide") else ""
    if md_name == "Cyber_Protection_Policy.md":
        extra_css = SPECIMEN_CSS
    OUT_HTML.mkdir(exist_ok=True)
    OUT_PDF.mkdir(exist_ok=True)
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<style>{CSS}{extra_css}</style></head><body>{body}</body></html>"""
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
        kwargs = dict(
            path=str(pdf_path), format="Letter", print_background=True, prefer_css_page_size=True,
            display_header_footer=True, header_template="<span></span>", footer_template=footer_tpl,
            margin={"top": "0.8in", "bottom": "0.85in", "left": "0.75in", "right": "0.75in"},
        )
        try:
            page_obj.pdf(outline=True, tagged=True, **kwargs)
        except TypeError:
            page_obj.pdf(**kwargs)
        browser.close()
    return pdf_path


def package(built):
    send = PKG / "1_Send_to_Corgi"
    private = PKG / "2_Keep_Private_Working_Files"
    if PKG.exists():
        shutil.rmtree(PKG)
    send.mkdir(parents=True)
    private.mkdir(parents=True)
    writer = PdfWriter()
    for (src, title, _footer, pkg_name), pdf in zip(DOCS, built):
        shutil.copy(pdf, send / pkg_name)
        start = len(writer.pages)
        reader = PdfReader(str(pdf))
        for p in reader.pages:
            writer.add_page(p)
        parent = writer.add_outline_item(title, start)

        def copy_outline(items, parent_item, depth):
            last = None
            for item in items:
                if isinstance(item, list):
                    if last is not None and depth < 2:
                        copy_outline(item, last, depth + 1)
                    continue
                try:
                    last = writer.add_outline_item(item.title, start + reader.get_destination_page_number(item), parent=parent_item)
                except Exception:
                    last = None

        # Chromium nests everything under the H1; skip that level so sections sit directly under the document.
        top = reader.outline
        if len(top) >= 2 and not isinstance(top[0], list) and isinstance(top[1], list):
            top = top[1]
        copy_outline(top, parent, 0)
    writer.add_metadata({"/Title": "Cyber Protection Policy: Complete Submission"})
    with open(send / "Complete_Submission.pdf", "wb") as f:
        writer.write(f)
    for name in ["Cyber_Protection_Policy.md", "Sample_Application_Cedar_Ridge.md", "Decision_Rationale.md"]:
        shutil.copy(ROOT / name, private / ("source_" + name))
    for extra in (ROOT / "validation").glob("*.md"):
        shutil.copy(extra, private / extra.name)
    (PKG / "READ_ME_FIRST.txt").write_text((ROOT / "build" / "READ_ME_FIRST.txt").read_text(encoding="utf-8"), encoding="utf-8")
    zip_base = ROOT / "Corgi_Cyber_Policy_Package"
    shutil.make_archive(str(zip_base), "zip", root_dir=PKG.parent, base_dir=PKG.name)
    # A send-only zip: nothing from the private folder may leave the machine by accident.
    send_base = ROOT / "Send_to_Corgi"
    shutil.make_archive(str(send_base), "zip", root_dir=PKG, base_dir="1_Send_to_Corgi")
    return zip_base.with_suffix(".zip")


if __name__ == "__main__":
    built = {}
    for name, title, footer, _pkg in DOCS[1:]:
        built[name] = build(name, title, footer)
    counts = {k: len(PdfReader(str(v)).pages) for k, v in built.items()}
    fill = {"POLICY_PAGES": counts["Cyber_Protection_Policy.md"], "APP_PAGES": counts["Sample_Application_Cedar_Ridge.md"],
            "RAT_PAGES": counts["Decision_Rationale.md"]}
    g = DOCS[0]
    built[g[0]] = build(g[0], g[1], g[2], fill)
    built = [built[d[0]] for d in DOCS]
    for p in built:
        print(p, len(PdfReader(str(p)).pages), "pages")
    z = package(built)
    print(z, z.stat().st_size, "bytes")
    sys.exit(0)
