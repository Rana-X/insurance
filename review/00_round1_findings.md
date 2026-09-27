# Round-1 review findings

First-pass review of the zip and the Claude Docs versions, September 27, 2026. This was the brief given to the research agents, so they could build on it rather than repeat it. Some points were later corrected (see README section 6).

Package: Harborline Cyber Protection Policy (fictional admitted insurer), sample insured Cedar Ridge Accounting Group (Denver CPA firm, 62 staff, $8.5M revenue), for a Corgi Insurance "Strategic Projects" take-home. Brief requires: declarations page, cover page, disclaimers, insuring agreements, definitions, coverage sections (data breach, BI, extortion), exclusions, conditions, clear plain language, reasonable assumptions (limits, deductibles, covered events), practical detail, 3+ cited external references, a sample filled-out application, a decision rationale (limits, inclusions/exclusions, definitions, trade-offs), a final formatted package, and "do not submit an AI output".

Files: policy.md (policy + declarations), application.txt, rationale.md, 04_references.txt (33 sources), Sources.csv, Claim_Ledger.json, Quality_Review.md, 00_submission_guide.txt.

Already found:
- Vouch "$7,078 median premium for $5-10M revenue" cannot be found anywhere; Vouch publishes an overall cyber median of $2,755 (2,034 clients). Used in rationale Summary and Market benchmark.
- Fraud gap: definition of fraudulent instruction item (3) requires an employee to transfer; Section III part 6 says reduced limit doesn't apply "when criminals send instructions directly to your bank" (implies coverage that doesn't exist).
- Exclusion IV.2.8 (unfair/deceptive trade practices) carve-back only for regulatory proceedings; class actions under I and Q usually plead UDAP/UCL.
- Late notice: 90-day post-period deadline plus prejudice-only rule undermines claims-made-and-reported; automatic ERP wording ambiguous.
- $25K incident response and $2,500 pre-incident help have no per-period cap (QR's $1,027,500 annual max assumes one).
- Claim-free reduction: compounding unclear; "claim-free" undefined.
- Item 5 "24/7 MDR would halve it" vs Item 7 "halve to $5,000".
- Item 6 mentions options ("higher limits available", "full-limit option") that don't exist in Part 2 or the application.
- Backup credit needs a restore test within 12 months before an incident; Cedar Ridge's test (June 12, 2026) lapses mid-term.
- Underwriter note: fixing a MEDIUM scan finding keeps claim-free eligibility; policy only requires fixing CRITICAL ones.
- Coverage A only "when you report to our hotline" vs 3 reporting channels; EDR "all devices" vs "laptops and servers".
- Application 7.5: ~27,300 Colorado residents is above CPA's 25,000 prong; possible GLBA entity exemption.
- Rationale: "Jaguar Land Rover's 2025 attack on its suppliers" misphrased; "Coalition reports privacy claims doubled in H1 2026" can't come from a March 2026 report; $280K invoice fraud, "5-minute response", $2,330-$4,048 premiums not in ledger; ~10 cited sources missing from the 33 (Chubb Neglected Software Exploit endorsement, Corvus, UK Insurance Act 2015, CISA #StopRansomware, FBI/IC3, NYDFS 500, HIPAA proposal, Colorado SB 26-189, Coalition Deepfake Response Endorsement Dec 2025, At-Bay "Post-Cyber Event Hardening"); BBR 5.0 date July 2025 vs 04/2025; $508K vs $422K both "average ransomware claim".
- Leftover process notes in the rationale (revision parentheticals, "12-hour" wait, old letters, "state this in the memo", "clarity criterion", "deep research report"), mixed I/we voice; rationale is 30 pages.
- Verified on the web 2026-09-27: CIRCIA final rule not yet published (Sept 2026 target); CA SB 690 passed Aug 28 2026, pen-register only, Governor deadline Sept 30, no pocket veto; Colorado SB 26-189 signed May 14 2026, effective Jan 1 2027. Corgi CORG-CY-0100 sells breach response, ransomware, BI, FTF, employee privacy, PCI, rogue-employee carveback as endorsements (search snippet); underwritten by Technology Risk Retention Group.

Network note: in this session, web search worked but direct page fetches were blocked for most insurer, court and regulator sites, so web evidence is search-result level.
