# Cyber insurance policy wordings for small and mid-sized businesses

A catalog of publicly posted cyber insurance policy wordings, specimen policies, coverage forms, endorsements,
summaries and applications aimed at small and medium-sized businesses. It includes a script that downloads every
document into `policies/`.

Research date: September 2026. The catalog was built from 15 parallel research passes, each covering one market
segment. The segments were US majors, US specialty (two groups), insurtechs, MGAs/wholesale, ISO/HSB standard forms,
US regional mutuals, industry programs, cyber built into BOP/package policies, UK/Lloyd's, Canada, Australia/NZ,
Europe, Asia/Middle East/Africa/Latin America, and a generic sweep.

## What's here

| File | Contents |
|---|---|
| [`CATALOG.md`](CATALOG.md) | Readable index grouped by region and carrier, with links to every document |
| `catalog/cyber_policies.csv` / `.json` | The full catalog: carrier, product, document type, form number, edition, market, URL |
| `catalog/gaps.json` | Carriers where no public wording was found, and carriers not yet searched |
| `catalog/raw/*.json` | The raw findings from each research segment, before de-duplication |
| `scripts/build_catalog.py` | Rebuilds the catalog, CSV and `CATALOG.md` from `catalog/raw/` |
| `scripts/download_policies.py` | Downloads the documents into `policies/<region>/<carrier>/` and writes a manifest with checksums |

### Current numbers

- **407** unique documents (**343** direct PDF/DOCX links) from 135 carrier or issuer names. Some names are regional entities of the same group.
- **169** core policy documents: wordings, specimens, coverage forms, endorsements and declarations. 91 of them are direct links to the latest edition found.
- The rest: 122 summaries/IPIDs/key-facts sheets, 66 applications and 50 product pages.
- By region: US 240, Europe 54, UK 33, Australia/NZ 30, Canada 23, Asia 23, other 4.

### Notable current SMB wordings found

**US**
- Crum & Forster Simple Cyber v6.0 (2025-09-04)
- Beazley Breach Response 5.0 (F00653 02/2025)
- Coalition Active Cyber Policy (2025–26 issued copies)
- At-Bay AB-CYB-001.2 (08/2023)
- Cowbell Prime 100
- Corvus Smart Cyber
- HSB Cyber Suite CSC (02-2025)
- Travelers CyberRisk CYB-16001
- Chubb Cyber ERM small business PF-48169
- Hiscox CyberClear admitted coverage part
- The Hartford CyberChoice Professional
- TMHCC NetGuard Plus NGP 1000
- DUAL Cyber (2023)
- Elpha Secure

**UK:** Hiscox CyberClear WD-PIP-UK-CCLEAR(5), Coalition UK specimen (2026), RSA, Aviva, Markel, HSB and AIG CyberEdge.

**Australia/NZ:** Emergence CEP-005.1 (2026), Delta AU 0824, CFC Cyber Proactive Response (2025), Chubb Cyber ERM 2.2 SME and QBE NZ CYB0625.

**Europe:** GDV AVB Cyber model conditions (Feb 2024), Hiscox, Allianz, AXA CH, HDI, Zurich CH, Markel, ERGO, Gothaer and R+V.

**India:** IRDAI-filed commercial cyber wordings from 10 insurers.

## Caveats

- **The PDFs are not downloaded yet.** The cloud session that built this catalog had a network policy that blocked
  every insurer website (HTTP 403 from the egress proxy). The catalog therefore contains URLs, and `policies/` is
  empty. Run the downloader from a machine or environment with normal internet access (see below).
- **Research is incomplete.** The session had a shared cap of 200 web searches across all agents, and it ran out
  after about 15 searches per segment. `catalog/gaps.json` lists 228 carriers or markets marked `not_searched`.
  Examples: The Hartford, CNA and Zurich NA forms; Markel, Berkley, AXA XL and Arch; most UK composites; France,
  Spain, Italy, the Nordics and Ireland; Singapore, Japan, the Middle East, Africa and Latin America. Another 49 were
  searched but had no public wording, usually because the carrier releases it only through brokers or portals.
- **Metadata comes from search snippets and hasn't been checked against the files.** Form numbers, edition dates and
  "latest" flags were inferred from titles, URLs and search snippets, not from the documents. Where an agent was
  unsure, the `notes` column says "verify".
- **Some entries are issued policies, not blank specimens.** They were posted publicly by the insured, for example a
  public agency, a council or a nonprofit. They show the real current wording but also contain that insured's
  details. The `notes` column says when a document is an issued policy.
- Wordings remain the copyright of the issuing insurers. This catalog only links to copies they or others have
  posted publicly.

## Downloading the documents

Requires Python 3.9+ and uses only the standard library:

```bash
python3 scripts/download_policies.py                        # every direct PDF/DOCX link
python3 scripts/download_policies.py --doc-type policy_wording --doc-type specimen_policy --doc-type coverage_form
python3 scripts/download_policies.py --region US --region UK
python3 scripts/download_policies.py --retry-failed         # retry only what failed last time
python3 scripts/download_policies.py --include-pages        # also save HTML product pages
```

Files are saved as `policies/<region>/<carrier>/<id>__<name>.pdf`. The `<id>` matches the `id` column in the
catalog. `catalog/download_manifest.json` records the HTTP status, final URL, byte size and SHA-256 of each file.
Re-runs skip files that already downloaded. A host blocked by the network is recorded as
`blocked_by_network_policy`, and an HTML page returned in place of a PDF as `ok_but_got_html`.

## Extending the research

Add a JSON file to `catalog/raw/` in the same format as the existing files, then run
`python3 scripts/build_catalog.py`. Entries are de-duplicated by URL (ignoring case, `www.` and tracking parameters),
and missing fields are filled in from duplicates. The `not_searched` rows in `catalog/gaps.json` are the to-do list
for the next pass.
