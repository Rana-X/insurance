# Corgi take-home: SMB cyber insurance policy

A specimen cyber insurance policy for small and mid-sized businesses, a completed sample application, and a decision rationale. The insurer (Harborline Insurance Company) and the insured (Cedar Ridge Accounting Group, LLC) are fictional.

## Deliverables (`pdf/`)

| File | What it is |
|---|---|
| `Harborline_Cyber_Policy_Submission.pdf` | All three documents in one PDF, with bookmarks |
| `01_Harborline_Cyber_Protection_Policy.pdf` | Cover, policyholder notices, Declarations, incident guide, contents, policy form HIC-CY-100 (Sections I–VI), TRIA disclosure |
| `02_Sample_Application_Cedar_Ridge.pdf` | Completed application HIC-CY-APP for the sample insured, including the underwriting summary |
| `03_Decision_Rationale.pdf` | Why each key decision was made: structure, definitions, limits, coverages, exclusions, conditions, worked claim examples, trade-offs, references |

## Rebuilding

The PDFs are generated from the HTML/CSS in `src/` with WeasyPrint:

```bash
pip install weasyprint pypdf pymupdf
python3 build.py           # all documents plus the combined PDF
python3 build.py policy    # one document
python3 build.py --png     # also write page previews to build/
```

Fonts (Source Serif 4, Inter, IBM Plex Mono, Mrs Saint Delafield) are bundled in `fonts/` under the SIL Open Font License.
