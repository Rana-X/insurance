# 02: Insurtech and startup cyber products, a competitive profile and Harborline benchmark

Prepared 2026-09-27 for the Harborline Cyber Protection Policy (fictional admitted insurer; SMBs with $1M–$50M revenue), a Corgi "Strategic Projects" take-home. This builds on `round1_findings.md` and does not repeat those items.

## How to read this file

**Method.** I read the Harborline context first: the Declarations Items 1–12, Section I, and the relevant Section III and V clauses in `policy.md`, plus the rationale tables. I then looked up each player in the 407-row catalog (`/home/user/insurance/catalog/cyber_policies.csv`) and ran 22 web searches, the full budget.

**Network limits.** I could not open any insurer document directly. Every curl and WebFetch attempt failed with CONNECT 403 or EGRESS_BLOCKED, including at-bay.com, coalitioninc.com, help.coalitioninc.com, cowbell.insure, corvusinsurance.com, corgi.insure, vouch.us, embroker.com, businesswire.com, assets.ctfassets.net, acwajpia.com, elphasecure.com, portal.bigimd.com and home.sayatalabs.com. The proxy log also shows blocks for astroa.org, mwvhomelessalliance.org, alloantibody.org, beazley.com and tmhcc.com. As a result, every web finding below is at **search-snippet level**. No policy wording was re-read this round.

**Evidence codes** (used in every table):

| Code | Meaning |
| --- | --- |
| **S1** | Search snippet taken from the company's own page or press release (coalitioninc.com, at-bay.com, cowbell.insure, corvusinsurance.com, PR Newswire or Business Wire releases) |
| **S2** | Search snippet from trade press (Insurance Business, The Insurer, IA Magazine, SiliconANGLE, insurance-canada.ca, Reinsurance News, Help Net Security, FF News, TechCrunch) |
| **S3** | Search snippet from an aggregator or secondary blog (quotesweep, agentinsured.eu, Medium, insurerbrain, ryskly, market-overview blogs). Low reliability. |
| **C** | The candidate's own reading of a primary document, as recorded in `rationale.md` or `Claim_Ledger.json`. I could not re-open it, so it is **not independently verified**. |
| **K** | A note in the local catalog (`cyber_policies.csv` / `CATALOG.md`) |
| **n/f** | Not found in this round |

All search dates are 2026-09-27. Where a source date appears in a URL or snippet, it is given.

---

## 0. Headline findings

1. **Corgi launched an admitted carrier on Aug 26, 2026**: Corgi Insurance Company, Inc., aimed at main-street small businesses (dry cleaners, salons, restaurants, professional offices, retail) (S1/S2). The rationale still presents Corgi as a startup-only, liability-first RRG writer, and it uses "admitted insurer" as a Harborline differentiator. For a Corgi take-home that framing is out of date and should be fixed. It is also an opening: Harborline reads naturally as the cyber form such a carrier would file.
2. **Coalition's Active Cyber Policy (ACP) is written on surplus lines paper in the US** ("all non-admitted new business and renewal quotes" from Apr 15, 2025; S1). The 2026 Enhanced Business Recovery endorsements are sold as add-ons to the ACP (S1). Yet the rationale labels Coalition "admitted" and then borrows ACP-only features. Harborline needs to say which Coalition form it means each time.
3. **Harborline is behind the market in four places:**
   - vendor (dependent) system failure is optional, while Coalition's ACP base form covers non-IT providers' *security or systems* failures;
   - system-failure BI carries a $250K sublimit, against Coalition's full limit (C);
   - there is no deepfake reputational-response cover, which Coalition has offered globally since Dec 2025;
   - breach response sits inside the aggregate, with only $25K / 72 hours outside it, whereas Beazley BBR's breach-response services and Coalition's Breach Response Separate Limits endorsement are outside-limit structures (K/C).
4. **Harborline is genuinely ahead in five places:**
   - a *firm* 50% BI advance, where Coalition's Cashflow Lifeline is expressly "discretionary" (confirmed, S1);
   - contractual service standards;
   - a modern war exclusion with an attribution process;
   - employee privacy, rogue employee and paper records all in the core;
   - a combined $2,500 pre-incident budget.
5. **Of the 13 claims tested:** 5 confirmed (b, e, k, l, m), 1 partly contradicted (i: Corgi regulatory defense appears to be included, not sold by endorsement), 7 unverifiable this round (a, c, d, f, g, h, j). Three of the unverifiable ones carry a framing risk:
   - (a) is a universal negative;
   - (c) "electronic means" arguably already covers phone and VoIP deepfakes;
   - (j) the Vouch figures come from one insured's certificate, not from Vouch's product maximums.

---

## 1. Player profiles

### 1.1 Coalition (MGA/insurer; Active Insurance model)

| Field | Finding | Evidence | Source (date) |
| --- | --- | --- | --- |
| Segment / revenue | ACP covers insureds up to $5B revenue; limits up to $15M | K | help.coalitioninc.com/hc/en-us/articles/33998071846811-Active-Cyber-Policy-FAQ (FAQ, 2025-04-15 per catalog; rationale cites "updated June 20, 2025") |
| Paper | ACP: "Beginning April 15, 2025, all non-admitted new business and renewal quotes in the US will be issued on this new form" (surplus lines). Coalition also writes admitted paper, but the admitted form's current name and features were not found this round. The issued policy Harborline benchmarked is called "Coalition Cyber Policy 3.0, issued Nov 2025" in the ledger (C) but "Active Cyber Policy (surplus lines)" in the catalog (K). **Unresolved; matters for claim (k) and the "admitted" row.** | S1, C, K | businesswire.com/news/home/20250409047735/en/Coalition-Launches-New-Active-Cyber-Policy (2025-04-09); coalitioninc.com/announcements/coalition-launches-new-active-cyber-policy |
| Structure | 11 coverages formerly sold by endorsement moved into the base form as insuring agreements | S1 | same (2025-04-09) |
| Canada | ACP launched in Canada, March 2026 | S2 | insurance-canada.ca/2026/03/11/coalition-launch-active-cyber-policy/ |
| AI | ACP gives affirmative coverage for "AI-related security events, including … deepfake-enabled FTF and AI-caused security failures". There is also a separately announced "Affirmative AI Endorsement" (date not captured). | S1 | coalitioninc.com/announcements/coalition-adds-new-affirmative-ai-endorsement-to-cyber-policies; coalitioninc.com/ai-coverage |
| Dependent BI | ACP: "expanded contingent business interruption: coverage for business interruption loss when a **non-IT provider** experiences a **security or systems failure**." The issued policy requires a written contract for hosted services (C). | S1 (search summary of the Apr 2025 release), C | businesswire 2025-04-09 |
| Deepfake Response Endorsement | Added globally, **Dec 2025**. Covers deepfake-forensics analysis with a written report, legal work to take the deepfake down from platforms, and crisis-PR support. Scenarios: a fake CEO video with inflammatory remarks; an employee likeness used to move a share price. Available in US, UK, Canada (incl. Quebec), Australia, Germany, Denmark, Sweden, France. | S1, S2 | coalitioninc.com/announcements/coalition-adds-deepfake-response-endorsement; siliconangle.com/2025/12/09/…; fintech.global/2025/12/18/… |
| Enhanced Business Recovery (EBR) | Four BI endorsements for ACP policies, US and Canada (excl. Quebec): **Key Customer Coverage** (protects revenue tied to the biggest customers); **Rapid Review** (one neutral forensic accountant, "same set of numbers"); **Cashflow Lifeline** ("an early, **discretionary** cash advance to qualifying small businesses … while the full BI loss is measured"); and a **reduced waiting period for top-tier MDR** users. Announced at Activate, April 2026; IA Magazine headline "Coalition Releases…" dated 2026-08-17. No % or $ amount found for the Lifeline. | S1, S2 | coalitioninc.com/announcements/coalition-unveils-enhanced-business-recovery-endorsements; coalitioninc.com/blog/cyber-insurance/introducing-enhanced-business-recovery (ledger: 2026-04-30); insurance-canada.ca/2026/04/16/…; iamagazine.com/2026/08/17/… |
| IR services / retention | "$0 retention … for insureds that use Coalition's in-house Incident Response services" (security and forensics). Canada has a separate $0-retention announcement. | S1, S2 | coalitioninc.com/announcements/coalition-eliminates-out-of-pocket-security-and-forensics-costs-for-policyholders-facing-a-cyber-claim; insurancebusinessmag.com/us/news/cyber/coalition-eliminates-outofpocket-costs-for-security-forensics-services-241017.aspx (older, likely 2023) |
| Response time | "average response time of **under five minutes**" (Coalition Incident Response) | S1 | same, plus coalitioninc.com/incident-response |
| Breach response outside limits | Available through the "Breach Response Separate Limits Endorsement" (help article); the issued policy has 72 hours of breach response outside limits (C) | K, C | help.coalitioninc.com/hc/en-us/articles/7665647884443-… |
| Pre-claim assistance | Coalition "offers pre-claims assistance"; the rationale's **$1,010** is from one issued policy (C) | S1 (search summary), C | coalitioninc.com/claims-experience / report-a-claim (the snippet does not name the page) |
| Vanishing retention | Exists (Coalition blog "How Vanishing Retention Rewards Security-Conscious Policyholders"); terms not captured | S1 (title only) | coalitioninc.com/blog/cyber-insurance/how-vanishing-retention-rewards-security-conscious-policyholders |
| Policy mechanics per the issued policy | 70% hammer; ERP 100/150/200%; invoice loss at net cost; $50K proof of loss; 25% betterment; legacy war wording; system failure core at full limit; 8-hour wait; 180-day restoration; $250K FTF; $1M/$2,500 on the SMB policy reviewed | C | mwvhomelessalliance.org/wp-content/uploads/2026/02/8._Cyber-Policy.pdf (blocked) |
| Coalition Control / MDR | Control is the security platform bundled with the policy, not a policy form (K). No Coalition MDR product details captured this round. | K / n/f | help.coalitioninc.com/hc/en-us/articles/7687332367259-Coalition-Control-Overview |
| Loss data | 2026 Claims Report (FY2025 data, published 2026-03-05): initial ransom demands +47% YoY; a record 86% refused to pay; $21.8M of stolen funds recovered, average recovery $202K; 100,000+ policyholders. Older IR release: 45% of reported events handled without a claim; 84% of social-engineering funds clawed back. | S1 | coalitioninc.com/announcements/2026-cyber-claims-report; coalitioninc.com/claims-report/2026 |

### 1.2 At-Bay (InsurSec MGA/insurer)

| Field | Finding | Evidence | Source (date) |
| --- | --- | --- | --- |
| Form | AB-CYB-001.2 (08/2023), 36 pages; the older AB-CYB-POL-COV (05/2022) is superseded | K | at-bay.com/wp-content/uploads/2023/06/Cyber-Insurance-Policy-Form.pdf |
| Paper | Surplus lines per the rationale; not verified | C | — |
| Limits / retention (SMB example) | $1M aggregate, $2,500 retention, $1M dependent BI, 8-hour system-failure wait on the ASTRO issued policy | C | astroa.org/…/Corrected_Stamped_Policy… (blocked) |
| MDR / "InsurSec packages" (Oct 2, 2025) | Two "industry-first" solutions with **zero retentions on ransomware and financial fraud** for qualifying package buyers. Policies placed by At-Bay that adopt **Stance MDR for Email** can raise financial fraud sublimits to **up to $1M**. Stance MDR for Email = Stance Fraud Defense plus AI-powered cloud email security. | S1, S2 | businesswire.com/news/home/20251002591457/en/…; reinsurancene.ws/at-bay-reveals-new-cyber-insurance-solutions-for-ransomware-and-financial-fraud/; at-bay.com/packages/; at-bay.com/mdr/ |
| Post-Cyber Event Hardening (Mar 2026) | A **post-claim service**, not an insuring agreement: "up to **100 hours** of hands-on security remediation" for eligible policyholders after a claim. Covers assessment of remaining gaps, technical hardening and "betterment" playbooks. Rationale for launch: firms hit once are 2x as likely to be hit again within two years. | S2 | ffnews.com/newsarticle/at-bay-launches-post-cyber-event-hardening-service-…; job-boards.greenhouse.io/atbayjobs/jobs/7710066003 |
| Form mechanics | ERP 75%/125% (1 and 2 years); 80% hammer; 180-day restoration from when the disruption begins; sum of retentions capped at the largest; fraud limited to "email or other electronic communication"; forensic accounting inside BI loss; "External Computer Systems" in the computer-system definition; legacy war wording | C | at-bay.com form (blocked this round) |
| Invoice manipulation | Add-on | C | at-bay.com/articles/invoice-manipulation-cyber-insurance/ |
| Rationale's "flat renewal after ransomware" | Not seen in any snippet | n/f | — |
| Loss data (2026 InsurSec Report, Apr 2026) | Average claim severity at an all-time high of **$221K**; ransomware severity **$508K** (+16%); financial fraud is 30% of claims, with the average stolen amount $285K (+16%); **small businesses saw +56% FTF incidents**; remote access was the entry point in 87% of ransomware claims; VPN in 73% of ransomware claims with a known vector; SonicWall in about 1 in 3 ransomware claims. The rationale's band figures ($180K average claim and $422K ransomware under $25M revenue) come from the provided PDF (C). | S1, S2 | at-bay.com/articles/insursec-report-2026-key-findings-cyber-risk/; helpnetsecurity.com/2026/04/23/cyber-insurance-claims-report/; insurancebusinessmag.com/us/news/cyber/one-ransomware-crew-now-drives-half-of-all-cyber-claims-atbay-573139.aspx |

### 1.3 Corvus (Smart Cyber; owned by Travelers)

| Field | Finding | Evidence | Source (date) |
| --- | --- | --- | --- |
| Ownership | Travelers acquired the Corvus MGU. Travelers Cyber Risk Services were added to all Travelers cyber policies in 2025. | S1 | corvusinsurance.com/pressroom/travelers-cyber-risk-services; investor.travelers.com/…/2025/Travelers-Announces-Enhanced-Services-for-Cyber-Liability-Customers |
| Segment / limits | Limits doubled to $10M; revenue ceiling $5B; bigger appetite below $30M revenue, focused on the sub-$10M segment. Date not in the snippet; likely 2023. | S2 | insurtechinsights.com/corvus-expands-its-small-business-cyber-offering-whilst-doubling-underwriting-offer/; cyberinsurer.com/… |
| BI | Covered "until the date of full system restoration", with no dollar retention (undated explainer) | S1 | corvusinsurance.com/news-and-insights/cyber-coverage-explained-business-interruption/ |
| Contingent BI | **6-hour waiting period**, no dollar retention; the rationale says full-limit CBI is available (C) | S1, C | corvusinsurance.com/news-and-insights/cyber-coverage-explained-contingent-business-interruption-cyber |
| Form | "Corvus Smart Cyber Policy Form" (edition not shown; there is also a Scribd copy) | K | corvusinsurance.com/hubfs/Corvus%20Smart%20Cyber%20Policy%20Form.pdf |
| Paper, hammer, ERP, fraud | n/f | — | — |

### 1.4 Cowbell (Prime family; Cowbell Factors)

| Field | Finding | Evidence | Source (date) |
| --- | --- | --- | --- |
| Prime 100 / Prime 100 Pro | **Admitted**, standalone, businesses up to **$100M** revenue. Social engineering added April 2020. Coverages include security-breach expense, data restoration, loss of income, PR, breach liability, FTF and website media. "Reputation" means PR fees to restore reputation, not lost profit. | S1 | cowbell.insure/prime-100-standalone-admitted-cyber-insurance/; cowbell.insure/news-events/pr/cowbell-adds-social-engineering-coverage-to-its-cyber-insurance-program/ |
| Prime 100 form | Specimen "PRIME 100 PRO 100 11 22" (11/2022, © 2024) | K | home.sayatalabs.com/cnc-wb/get_resource/carriers/SAMPLE_POLICY_FORM/COWBELL |
| Prime 100 exclusions (per rationale) | Excludes system failure and voluntary shutdown; conditions social engineering on a documented verification procedure | C | cowbell.insure/wp-content/uploads/pdfs/CB-Prime100-Overview.pdf (blocked) |
| Prime 250 | **Admitted**, standalone, up to **$250M** revenue. **Includes BI from system failure.** | S1 | cowbell.insure/prime-250/ |
| Prime Plus | Excess, follows form over Cowbell or third-party primary; 8 bundled proactive services (pen test, training, MDR/EDR, risk assessment…) | S3 | ryskly.com/product/cowbell-cyber-inc-cowbell-prime-plus-usa |
| Prime One (2026) | US launch; **non-admitted**; $250M–$1B revenue; up to **$10M**; **affirmative AI and quantum-computing** coverage | S1 | cowbell.insure/news-events/pr/prime-one-us-emerging-ai-quantum-risks/; prnewswire.com/…-302748534.html |
| Capacity | $15M-limits program with Obsidian and Benchmark (date not captured) | S2 | theinsurer.com/cyber-risk/news/cowbell-cyber-launches-15mn-limits-program-with-obsidian-and-benchmark/ |
| Cowbell Factors | Continuously updated risk ratings and peer benchmarking, used in pricing | S1 | cowbell.insure (search summary) |

### 1.5 Resilience

| Field | Finding | Evidence | Source |
| --- | --- | --- | --- |
| Segment | Serves the mid-market and enterprise with cyber-risk quantification. No SMB product, form, limits or pricing found. | S3 | quotesweep.com/blog/best-cyber-insurance-small-business |
| Relevance to Harborline | Low: sits above Harborline's $1M–$50M band | — | — |

### 1.6 Vouch

| Field | Finding | Evidence | Source (date) |
| --- | --- | --- | --- |
| Segment | Startups and tech. Cyber covers breach response, BI from system outages, ransomware, liability, regulatory fines and phishing/BEC fraud, "subject to sublimits". | S1 | vouch.us/blog/cyber-insurance (2026); vouch.us/insurance101/cyber-insurance |
| Terms used by the rationale | $62,500 ransomware sublimit; $25K dependent BI; 90-day restoration; 8-hour wait; $10K retention; system failure as a purchased option; surplus lines. **Source: one insured's certificate/declarations** (Alloantibody Exchange), not a Vouch product sheet. | C | alloantibody.org/files/Alloantibody_Exchange_-_Certificate_of_Insurance_Cyber.pdf (blocked) |
| Corix | Vouch reportedly launched Corix, a broker-facing MGA, in Jan 2025 | S3 | market-statistics snippet (security.org / heimdal); low reliability |
| Pricing | Overall cyber median premium **$2,755** across 2,034 clients (round 1). The $7,078 figure for $5–10M revenue is still unsourced (round 1). | round 1 | — |

### 1.7 Embroker

| Field | Finding | Evidence | Source |
| --- | --- | --- | --- |
| Segment / product | Startup-focused digital broker/MGA; "10-minute binding" per an aggregator. No cyber form, carrier, limits or features found. | S3 | quotesweep.com/blog/best-cyber-insurance-small-business; embroker.com/blog/cyber-insurance-requirements-for-smbs-usa-2025 |

### 1.8 Corgi (the prospective employer)

| Field | Finding | Evidence | Source (date) |
| --- | --- | --- | --- |
| Company | Founded 2024 in SF (YC) by Nico Laqua and Emily Yuan; regulatory approval July 2025; reported $4B valuation on its third raise in 8 weeks (TechCrunch, 2026-07-23) | S2 | techcrunch.com/2026/07/23/insurance-startup-corgi-reportedly-raised-more-money-at-4b-…; ycombinator.com/companies/corgi-insurance |
| Paper (tech/startup book) | **Technology Risk Retention Group (TRRG)**, an Arizona-chartered RRG. One aggregator says TRRG has no AM Best rating. | S2 / S3 | insurancebusinessmag.com/…-587646.aspx; quotesweep.com/insurtech/corgi |
| **Paper (new, main-street)** | **Corgi Insurance Company, Inc.**, an admitted carrier, **announced 2026-08-26**. Guaranty-fund protection for eligible policies. Target classes include condo associations, small apartments, restaurants, dry cleaners, technology companies, professional/administrative offices, retail, salons and repair shops, self-storage, wholesalers. Whether cyber is on the admitted paper yet: **n/f**. | S1, S2 | prnewswire.com/news-releases/corgi-insurance-launches-admitted-insurance-carrier-302860246.html; theinsurer.com/ti/news/corgi-launches-admitted-commercial-lines-carrier-2026-08-26/; insurancebusinessmag.com/us/news/breaking-news/corgi-built-its-name-insuring-ai-startups--its-new-carrier-targets-dry-cleaners-salons-and-more-587646.aspx |
| Cyber form | **CORG-CY-0100**. Endorsements: Breach Response / Event Management; Ransomware / Cyber Extortion; Business Interruption; Funds Transfer Fraud; Employee Privacy; PCI Liability; Rogue Employee Carveback. The same snippet says Corgi cyber "includes data breaches, ransomware, breach response, and **regulatory defense**". | S1 (search summary of corgi.insure) | corgi.insure/cyber-liability |
| Retention / media | $10K retention; media sold as a separate policy | C only | — |
| AI liability (May 2026) | "AI Insurance Coverage" launched 2026-05-04/05. Integrates with existing **Tech E&O** policies; modular, tailored to how the company uses AI; covers algorithmic bias, autonomous decisions, AI-generated errors. | S1, S2 | prnewswire.com/news-releases/corgi-launches-ai-insurance-coverage-to-protect-businesses-when-ai-goes-wrong-302762029.html; artificiallawyer.com/2026/05/05/…; fintech.global/2026/05/06/… |
| Analyst inference (flagged) | Under the federal Liability Risk Retention Act, RRGs may write only *liability* insurance. That plausibly explains why the TRRG cyber base is liability-first, with first-party pieces (breach response, ransomware, BI, FTF) as endorsements. It also explains why an admitted carrier matters for first-party cyber for main-street SMBs. **Counsel should confirm before this goes in the memo.** | inference | — |

### 1.9 Boost Insurance and Measured Insurance

The one combined search returned nothing specific on either company's cyber product: no form, limits, paper, pricing or dates. They are **not profiled**. Neither appears in the catalog.

### 1.10 Elpha Secure and Cysurance (security-bundled SMB)

| Player | Finding | Evidence | Source |
| --- | --- | --- | --- |
| Elpha Secure | MGA that embeds its own security software (Elphaware) in every policy. The sample policy defines "Cybersecurity Risk Controls" (Elphaware or third-party software confirmed in the application); paper described only as "AM Best A-rated". Feb 2026: ES Mail launch and **cybercrime limit expanded to $500K**. AXIS partnership (2024) and SentinelOne partnership (late 2025). ES-1000 package with Sterling (date not captured). | K, S3 | elphasecure.com/docasset/documents/Sample-Policy.pdf; insurerbrain.com/wiki/Elpha_Secure; sterlingrisk.com/elpha-secure-and-sterling-new-age-cyber-launch-es-1000-… |
| Cysurance | A cyber **warranty** combined with an insurance program (Protect360 through an Amwins program). "Certified solutions" give SMBs automatic warranty protection and discounted cyber policies with "no application or underwriting required". The public PDFs are warranty terms, not insurance wordings. | K, S1 | protect360.cysurance.com; cysurance.com/services/ |

### 1.11 AI-risk insurers (for Harborline's AI clause and AI-agent definition)

| Player | Finding | Evidence | Source |
| --- | --- | --- | --- |
| Armilla | Lloyd's coverholder; affirmative AI liability launched April 2025 (Chaucer among the backers); up to $25M per organization | S3 | medium.com/@purdyhouse/…; agentinsured.eu/tools/carrier-comparison/ |
| AIUC | $15M seed in July 2025 (led by Nat Friedman / NFDG). Publishes the **AIUC-1** standard. First AIUC-1-backed policy (ElevenLabs), Feb 2026. | S3 | agentinsured.eu; agentmarketcap.ai/blog/2026/04/15/… |
| Testudo | MGA launched Jan 2026; capacity of $9.25M per insured with Atrium and QBE; claims generative-AI litigation +137% YoY (its own data) | S3 | same set |
| Munich Re aiSure | Operating since 2018. A **performance guarantee** that pays if a model misses a contractually defined accuracy threshold; reportedly up to $15M through Mosaic. | S3 | agentinsured.eu/articles/munich-re-aisure-ai-performance-insurance-europe |
| Relm | n/f this round | — | — |
| Takeaway | These are standalone AI-liability or AI-performance covers for AI builders and deployers. They are not SMB cyber. Harborline's "AI is not excluded" clause and AI-agent definition sit at a different layer, which is fine, but the rationale should not imply cyber is where AI performance risk belongs. | — | — |

### 1.12 Beazley BBR 5.0 (incumbent reference point)

| Field | Finding | Evidence | Source (date) |
| --- | --- | --- | --- |
| Timing | Summary document BZCBR184_04/25 (April 2025). Applies to accounts **incepting on or after July 1, 2025**. This reconciles the rationale's "July 2025" and "04/25" (round 1 flagged the mismatch): the document is dated April and the effective date is July. | S1, C | beazley.com/globalassets/full-spectrum-cyber/bbr-5.0-enhancements-and-clarifications.pdf |
| Paper | Full Spectrum Cyber is written admitted (Beazley Insurance Company) and surplus (Beazley Excess and Surplus / Lloyd's). myBeazley small-business application covers revenue under $35M. | K | catalog notes; beazley_breach_response_new_business_application_revenues_below_35ml_0.pdf |
| Specimen | F00653 02/2025 (form number from a snippet, not checked against the file) | K | portal.bigimd.com/…/Beazley_SpecimenPolicyForm.pdf |
| Confirmed this round | **Computer Bricking Loss** insuring agreement; **System Failure** added as a cause of loss for Data Recovery Costs | S1 | BBR 5.0 enhancements PDF (search summary) |
| Candidate-read only | Hammer 60%→70%; reputation loss; proof of loss for all first-party loss; invoice manipulation without delivery-first; cryptojacking including cloud charges; voluntary shutdown; no out-of-band requirement for fraud | C | same PDF (C13 in the ledger) |
| Breach response structure | BBR breach-response services measured in notified individuals ("up to 5 million affected individuals", on an older factsheet) | K | beazley.com/…/beazley-bbr-coverage-factsheet-us.pdf |
| War | Beazley War and Cyber War Exclusion (E15626): physical-force war, "major detrimental impact", bystander carve-back, no attribution mechanism | C, K | lmalloyds.com/…/Beazley-War-and-Cyber-War-Exclusion-1.pdf |

---

## 2. Public pricing and loss data (2025–2026)

| Metric | Value | Evidence | Source |
| --- | --- | --- | --- |
| At-Bay average claim severity (all insureds, 2025 claims) | $221K (all-time high) | S1/S2 | At-Bay 2026 InsurSec Report coverage |
| At-Bay average ransomware severity | $508K (+16%) | S1/S2 | same |
| At-Bay financial fraud | 30% of claims; average stolen amount $285K (+16%); small businesses +56% FTF incidents | S1/S2 | same |
| At-Bay under-$25M band | $180K average claim; $422K ransomware | C | provided PDF |
| Coalition ransom demands | +47% YoY; 86% refused to pay | S1 | Coalition 2026 Claims Report |
| Coalition fund recovery | $21.8M recovered; $202K average recovery | S1 | same |
| Vouch cyber median premium | $2,755 (2,034 clients) | round 1 | — |
| Harborline illustrative premium | $5,508 for $1M / $7,500 retention, $8.5M-revenue CPA firm | policy.md | — |
| Premium data from other players | None published by Coalition, At-Bay, Cowbell, Corgi or Embroker in any result this round | n/f | — |

**Implication.** Harborline's $5,508 is about 2x Vouch's overall median. That median mixes startup sizes and cannot be compared like-for-like. With no public band-level premium data, the rationale should call the price "illustrative" and drop any "sits between X and Y" positioning that relies on unsourced figures ($2,330–$4,048; $7,078).

---

## 3. Feature matrix

**Key:**
- **Harborline position:** ▲ ahead of the named peers · ● market-standard · ▼ behind · ? cannot tell.
- Cell codes are the evidence codes from the top of the file.
- "Coalition" means the surplus-lines ACP unless a cell says "issued policy".
- The Embroker/Resilience column is dropped because nothing product-level was found for either.

| # | Feature | Harborline | Coalition | At-Bay | Corvus | Cowbell (Prime 100 unless noted) | Vouch | Corgi (CORG-CY-0100) | Beazley BBR 5.0 | Position |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Target band | $1–50M revenue, 10–250 staff | Up to $5B (K) | SMB–mid; reports split at $25M (C) | Appetite <$30M, up to $5B (S2) | ≤$100M; P250 ≤$250M; Prime One $250M–1B (S1) | Startups (S1) | VC-backed startups; admitted main-street carrier from Aug 2026 (S1) | SME; myBeazley <$35M (K) | ● |
| 2 | Paper | Admitted (fictional) | ACP surplus (S1); admitted form n/f | Surplus (C) | Travelers (S1); basis n/f | Admitted (S1); Prime One non-admitted | Surplus (C) | RRG (S2); admitted Corgi Ins. Co. (S1) | Admitted and surplus (K) | ● No longer a differentiator (Cowbell, Beazley, Corgi) |
| 3 | Structure | Core A–O plus options P–S, one form | Integrated; 11 endorsements folded into base (S1) | Base plus endorsements (C) | n/f | Standalone package (S1) | Modular (C) | Liability base plus 7 first-party/extension endorsements (S1) | Integrated, endorsements built in (K) | ● |
| 4 | Aggregate limit (SMB) | $1M | $1M on reviewed SMB policy (C); to $15M (K) | $1M (C) | to $10M (S2) | n/f; $15M program (S2) | n/f | n/f | n/f | ● |
| 5 | Retention | $10K by band, $7.5K with MFA+EDR, $5K with MDR | $2,500 (C); $0 with Coalition IR (S1) | $2,500 (C); $0 ransomware and fraud in MDR packages (S1) | $0 dollar retention on BI/CBI (S1) | n/f | $10K (C) | $10K (C) | n/f | ▼ vs At-Bay/Coalition $0 paths; ● otherwise |
| 6 | Breach response inside/outside limit | Inside $1M aggregate (B) | Separate-limits endorsement (K); 72h outside on issued policy (C) | n/f | n/f | Inside (S1 list) | n/f | Endorsement (S1) | Services by notified individuals (K) | ▼ |
| 7 | IR services outside limit, $0 retention | 72h, up to $25K, $0 | $0 retention with Coalition IR, cap n/f (S1) | n/f | n/f | n/f | n/f | n/f | n/f | ● |
| 8 | Pre-claim / pre-incident help | $2,500 outside limit | Offered (S1); $1,010 (C) | n/f | Travelers Cyber Risk Services (S1) | Prime Plus services (S3) | n/f | n/f | n/f | ▲ if $1,010 is right |
| 9 | Ransomware limit | Full; 20% coinsurance without verified backups | Full (C) | Full (C) | n/f | n/f | $62,500 sublimit on one insured (C) | Endorsement (S1) | n/f | ● (coinsurance is a mild ▼) |
| 10 | BI: security failure | Full limit | Full (C) | Full (C) | Until full restoration (S1) | Loss of income (S1) | Yes (S1) | Endorsement (S1) | Yes | ● |
| 11 | BI: own system failure | Core, $250K sublimit | Core, full limit (C) | Added coverage (C) | n/f | P100 excludes (C); P250 includes (S1) | Purchased option (C) | n/f | Data recovery only (S1); BI n/f | ▼ vs Coalition, ▲ vs P100/Vouch |
| 12 | Dependent BI: security failure | $500K, unnamed providers | Hosted systems with written contract (C) | $1M "External Computer Systems" (C) | CBI, full-limit option (C) | n/f | $25K (C) | n/f | Yes (K) | ▼ vs At-Bay/Corvus; ▲ vs Vouch |
| 13 | Dependent BI: system failure | Optional P | **In ACP base for non-IT providers (S1)** | n/f | n/f | n/f | n/f | n/f | n/f | ▼ |
| 14 | Non-IT vendors | Any provider under written or electronic terms (security only in core) | Yes, security or systems failure (S1) | "Distinct coverage line" (C) | n/f | n/f | n/f | n/f | n/f | ● for security, ▼ for system failure |
| 15 | BI waiting period | 8h; 4h with 24/7 MDR | 8h (C); reduced with top-tier MDR (S1, 2026) | 8h (C) | CBI 6h (S1) | n/f | 8h (C) | n/f | n/f | ● (MDR cut = Coalition 2026) |
| 16 | Restoration period | 180 days | 180 (C) | 180 (C) | Until full restoration (S1, undated) | n/f | 90 (C) | n/f | n/f | ● |
| 17 | SE/FTF limit | $250K shared ($100K if unverified); $500K or $1M option | $250K (C) | $250K (C); up to $1M with **email** MDR (S1) | n/f | SE since 2020, verification required (S1/C) | Low sublimit (C) | Endorsement (S1) | n/f | ● |
| 18 | Faster-reporting fraud retention | $2,500 if reported within 72h | Same idea in ACP (C) | n/f | n/f | n/f | n/f | n/f | n/f | ● |
| 19 | Invoice manipulation | Core, shared limit, net cost | Core, net cost (C) | Add-on (C) | n/f | n/f | n/f | n/f | Yes, no delivery-first (C) | ● |
| 20 | Fraud channels | Any means incl. phone, letter, deepfake (but an employee must transfer) | "Electronic means" plus deepfakes (C); deepfake FTF affirmative (S1) | Email/electronic (C) | n/f | n/f | n/f | n/f | n/f | ? (see claim c) |
| 21 | Bricking | $100K core | Base (C) | n/f | n/f | n/f | n/f | n/f | Insuring agreement (S1) | ● |
| 22 | Reputational harm | $100K lost profit, 14-day wait, 90 days | Base (C) | n/f | n/f | PR costs only (S1) | n/f | n/f | Yes (C) | ● |
| 23 | Deepfake reputational response | None; declined in rationale | **Endorsement, Dec 2025, global (S1)** | n/f | n/f | n/f | n/f | n/f | n/f | ▼ |
| 24 | Cryptojacking / telecom | $50K | Base (C) | n/f | n/f | n/f | n/f | n/f | Incl. cloud charges (C) | ● |
| 25 | Betterment / post-incident hardening | $25K security-improvement costs incl. first-year subscriptions | 25% betterment (C) | Up to 100 hours hands-on remediation service (S2) | n/f | n/f | n/f | n/f | n/f | ● to ▲ |
| 26 | Key customer | Optional S, 90 days | EBR endorsement 2026 (S1) | n/f | n/f | n/f | n/f | n/f | n/f | ● |
| 27 | BI cash advance | **Firm 50% within 10 business days, ≤$250K**, after coverage is confirmed | **Discretionary** Cashflow Lifeline (S1) | n/f | n/f | n/f | n/f | n/f | n/f | ▲ |
| 28 | Single forensic accountant / proof-of-loss $ | Option plus $50K for any first-party loss | Rapid Review (S1); $50K proof of loss (C) | Inside BI loss (C) | n/f | n/f | n/f | n/f | Proof of loss for all first-party (C) | ● |
| 29 | Affirmative AI | Base clause plus AI-agent definition | ACP base plus endorsement (S1) | Not in 2023 form (C) | n/f | Prime One AI and quantum (S1) | n/f | AI cover on Tech E&O, May 2026 (S1) | n/f | ● (the agent definition is ▲, unverified) |
| 30 | Hammer | 70% | 70% (C) | 80% (C) | n/f | n/f | n/f | n/f | 70% (C) | ● (less generous than At-Bay) |
| 31 | ERP | Auto 60 days; 12 months at 75%, 24 months at 125% | 100/150/200% (C) | 75%/125% (C) | n/f | n/f | n/f | n/f | n/f | ● (matches At-Bay) |
| 32 | War wording | Modern; attribution; insurer burden; help continues | Legacy (C) | Legacy (C) | n/f | n/f | n/f | n/f | Modern, no attribution (C) | ▲ |
| 33 | Vanishing / claim-free retention | −25% a year to $2,500, conditional | Vanishing retention (S1 title) | n/f | n/f | n/f | n/f | n/f | n/f | ● |
| 34 | Security-linked terms | Credits table (retention, wait, coinsurance, fraud limit) | MDR wait cut (S1); $0 with IR (S1) | Zero-retention packages; $1M fraud with email MDR (S1) | n/f | Cowbell Factors rating (S1) | n/f | n/f | n/f | ● concept; ? presentation (claim a) |
| 35 | Cancellation refund | Pro rata | Short-rate (C, not in ledger) | n/f | n/f | n/f | n/f | n/f | n/f | ? |
| 36 | Response / service standards | Contractual: 1h contact, 30-day decision, 15-day pay plus interest | Marketing: <5 min average (S1) | n/f | n/f | n/f | n/f | n/f | n/f | ▲ |
| 37 | Unlimited reinstatements | No (declined) | Yes (C) | n/f | n/f | n/f | n/f | n/f | n/f | ▼ (declined deliberately) |

**Tally for Harborline across the 37 rows:**

- **▲ ahead (6):** firm BI advance; contractual service standards; war wording; pre-incident budget (conditional on the $1,010 figure); employee privacy, rogue employee and paper records in the core (rationale; not a matrix row); AI-agent definition (unverified).
- **▼ behind (7):** outside-limit breach response; dependent system failure; system-failure sublimit; deepfake reputational response; $0-retention paths; dependent BI limit vs At-Bay and Corvus; unlimited reinstatements.
- **● market-standard:** everything else.

---

## 4. Tests of the rationale's competitor claims

| # | Claim in rationale.md | Verdict | Evidence and reasoning | Suggested fix |
|---|---|---|---|---|
| (a) | Declarations have "two additions no competitor has: a plain-English coverage column and a security credits table" | **Unverifiable**. A universal negative that cannot be proven; also overstated. | Only three issued declarations were reviewed (At-Bay ASTRO, Coalition issued policy, Vouch certificate), and none could be re-opened. Competitors already turn security into visible terms: At-Bay zero-retention and $1M-fraud packages (S1), Coalition's MDR waiting-period cut (S1), Cowbell Factors (S1), Elpha's software-linked terms (K). The *format* may be new; the *concept* is not. | "None of the declarations pages we reviewed show…". Drop "no competitor has". |
| (b) | Firm 50% BI advance vs Coalition's discretionary Cashflow Lifeline | **Confirmed** (S1) | Coalition: "an early, **discretionary** cash advance to qualifying small businesses." Nuance: Harborline's advance sits in Section V.7 "Our service standards", starts only "once we confirm that Coverage D, E or P applies", and is 50% of *our* reasonable estimate. That is firm in amount and timing but still gated on the insurer's judgment. Coalition's EBR endorsements attach to the surplus-lines ACP. | Keep. Move the advance out of "service standards" (where clauses 1–3 say "aim to") into Section III.4 so it reads as coverage. |
| (c) | "Both competitors limit fraud to electronic channels; ours adds phone calls and letters" | **Unverifiable this round** (wordings blocked); **at risk** | The ledger records At-Bay "email or other electronic communication" and Coalition "electronic means, including deepfakes" (C). But a phone or VoIP call, video call or deepfake voice is arguably "electronic", and Coalition markets affirmative deepfake-FTF cover (S1). So the practical gap is probably letters only. Harborline's own definition still requires an **employee** to transfer (round 1). Separately, and not verified this round: fraudulent-instruction wordings in crime and older BBR-style forms commonly list "written … or telephone instructions". Check BBR 5.0 (F00653) before claiming anything market-wide. | "At-Bay and Coalition define the channel as electronic; ours names phone, video and paper channels expressly, removing any argument." |
| (d) | Coalition charges short-rate refunds | **Unverifiable** | Not in Claim Ledger C11 (the Coalition issued-policy entry), and no snippet surfaced it. Source blocked. | Re-check against the issued policy's cancellation clause or drop it. Pro rata stands on its own merits. |
| (e) | Coalition "advertises a 5-minute average response" | **Confirmed**, with wording nuance (S1) | Coalition: "average response time of **under five minutes**" (Coalition Incident Response; release likely about 2023). | "advertises an average response of under five minutes". |
| (f) | Coalition pre-claim assistance $1,010 | **Existence confirmed** (S1); **amount unverifiable** (C) | Coalition "offers pre-claims assistance". $1,010 is one issued policy's figure (odd enough that it may be a schedule artefact). | "($1,010 on the 2025–26 issued policy we reviewed)"; do not present it as Coalition's standard. |
| (g) | At-Bay ERP 75%/125%, hammer 80%, 180-day restoration | **Unverifiable this round**; not contradicted (C) | at-bay.com was blocked. The candidate's ledger C12 records a direct text read of AB-CYB-001.2 (08/2023). Note the form is from 2023; the ASTRO issued policy is 2025. | Keep; cite the form edition "(AB-CYB-001.2, 08/2023)". |
| (h) | Coalition ERP 100/150/200%, hammer 70% | **Unverifiable this round** (C) | Ledger C11 says this comes from the issued policy. Open question: is that policy the admitted form or the ACP? See §5.1. | Name the Coalition form each time. |
| (i) | Corgi sells employee privacy, PCI, rogue-employee carveback and regulatory defense by endorsement; media as a separate policy; $10K retention | **Partly confirmed, partly contradicted**, rest unverifiable | Confirmed (S1): Employee Privacy, PCI Liability and Rogue Employee Carveback endorsements, plus breach response, ransomware, BI and FTF by endorsement. **Regulatory defense** is *not* in the endorsement list, and the same snippet says Corgi cyber "includes … regulatory defense", so "by endorsement" looks wrong. Media as a separate policy and the $10K retention: n/f. | Rationale I-J row and benchmark table: change Corgi regulatory defense to "included". Keep the other three. |
| (j) | Vouch $62,500 ransomware sublimit, $25K dependent BI, 90-day restoration, 8-hour wait | **Unverifiable** (source blocked); **framing risk** | The figures come from one insured's certificate (Alloantibody Exchange). They show what *that buyer* purchased, not Vouch's product terms or maximums. | "On one Vouch-insured's 2025–26 declarations…". Don't generalize to "Vouch's sublimit". |
| (k) | "Coalition's newest base form covers non-IT vendors" | **Confirmed** (S1), with two caveats | The ACP release: contingent BI "when a non-IT provider experiences a security **or systems failure**." Caveats: (1) the "newest base form" is the **April 2025 surplus-lines ACP**; (2) it covers *system* failures at non-IT providers in the base, which Harborline makes optional (P). Citing it to justify Harborline's broadening hides that Harborline is narrower. | "Coalition's Active Cyber Policy (surplus lines, April 2025) covers non-IT providers' security and system failures in its base. We match security failures in the core and sell system failures as Option P." |
| (l) | "At-Bay's 2026 Post-Cyber Event Hardening" | **Confirmed** (S2): launched March 2026 | A **service** giving up to 100 hours of hands-on remediation after a claim, not a dollar coverage. Harborline's G ($25K, including first-year subscriptions) is a different mechanism inspired by it. Also missing from the 33 sources (round 1). | "Inspired by At-Bay's Post-Cyber Event Hardening service (Mar 2026: up to 100 hours of remediation)". Add to the sources. |
| (m) | Coalition Deepfake Response Endorsement, Dec 2025 | **Confirmed** (S1/S2; SiliconANGLE 2025-12-09) | Covers forensics report, legal takedown and crisis PR; available in 8 countries. Harborline's N needs a security failure or privacy event, so a deepfake smear with no breach is **uncovered**. | Keep "declined", but name it as a gap in the benchmark table and say what would trigger adding it. Add to the sources. |

**Score:** 5 confirmed (b, e, k, l, m) · 1 partly contradicted (i) · 7 unverifiable (a, c, d, f, g, h, j). None of (a)–(m) is contradicted outright. The biggest *framing* problems are in (a), (c), (j) and (k).

---

## 5. Other competitor-framing problems in rationale.md (not in the a–m list)

1. **"Admitted insurer | Coalition (admitted) vs. At-Bay and Vouch (surplus lines)"** (Declarations table). Coalition's ACP, the form behind "Coalition's newest base form", affirmative AI in the base, and the 2026 EBR endorsements, is **non-admitted** in the US (S1). Pick one of these:
   - Coalition's admitted form (and confirm it has those features), or
   - "Coalition's surplus-lines ACP".

   Also note that Cowbell Prime 100/250 (S1), Beazley (K) and, since Aug 2026, Corgi (S1) all offer admitted paper. "Admitted" is table stakes, not an edge.
2. **Corgi's positioning is outdated.** The Summary ("Corgi's liability-first, modular form suits startups…") and the Structure row predate Corgi Insurance Company, Inc. (admitted, main-street SMB, Aug 26, 2026). For a Corgi take-home, add one sentence: *"Corgi's new admitted carrier targets exactly this segment; Harborline is designed as the cyber form it could file."*
3. **The fraud-limit option is tied to the wrong control.** Harborline raises Coverage H to $1M with **24/7 endpoint MDR**. At-Bay's $1M is tied to **Stance MDR for Email** (S1), the control that actually stops BEC. Either tie Option R to email security or verified callback, or explain the choice.
4. **"Cowbell's Prime 100 excludes it [system failure]"** may be accurate for Prime 100 (C), but Cowbell's admitted **Prime 250 includes system-failure BI** (S1). Say "Prime 100" every time, and don't generalize to "Cowbell".
5. **"Zero retention and flat renewal after ransomware (At-Bay)"** (declined table). Zero retention is confirmed; "flat renewal" was not seen in any source (n/f).
6. **BBR 5.0 date.** Use "BBR 5.0 (summary BZCBR184_04/25; effective for policies incepting on or after July 1, 2025)". This fixes the round-1 inconsistency.
7. **Corvus.** The rationale cites Corvus only for full-limit CBI. The Corvus explainers also show a **6-hour** CBI wait and **no dollar retention** on BI/CBI (S1, undated). Both are tighter than Harborline's 8 hours. Mention them or check the dates.
8. **At-Bay severity figures.** $508K is At-Bay's *all-insured* ransomware average and $422K is the under-$25M band (C). Label each; round 1 flagged the pair as conflicting. At-Bay's all-insured average claim is $221K (S1/S2), against the rationale's $180K under-$25M figure. Keep the band label.

---

## 6. Key gaps against the market, and recommended edits (in priority order)

| Priority | Gap / issue | Market reference | Recommended change |
|---|---|---|---|
| 1 | Coalition admitted/surplus conflation and outdated Corgi framing | Coalition ACP surplus (S1); Corgi admitted carrier (S1) | Fix the Declarations-table "Admitted" row, the Summary and the benchmark table. Add the Corgi admitted-carrier sentence. |
| 2 | Dependent (vendor) system failure is optional | Coalition ACP base covers non-IT providers' system failures (S1) | Keep P optional (a defensible accumulation choice), but state openly that Harborline is **narrower** than Coalition here. Or add a small core sublimit (e.g., the same $250K as own-system failure) with a 12-hour wait. |
| 3 | System-failure BI sublimit of $250K | Coalition full limit (C) | State it as a deliberate trade-off (already in the "Where we are narrower" line). Show pricing intent for "higher limits available" or delete that phrase (round 1). |
| 4 | No deepfake reputational response | Coalition, Dec 2025 (S1) | Add an optional "Deepfake Response" sublimit (forensics, takedown, PR; e.g., $25K) or list it clearly as not covered in the benchmark table. |
| 5 | Breach response inside the aggregate | BBR notified-individual services (K); Coalition separate-limits endorsement (K) | Offer an optional "breach response outside limits" (a separate $ limit), or note the trade-off. |
| 6 | Dependent BI $500K vs At-Bay $1M / Corvus full limit; Corvus CBI 6-hour wait | C / S1 | Already has a full-limit option. Put its existence on Item 6 with a price flag. |
| 7 | Claims (a), (c), (j) overstated | — | Reword as in §4. |
| 8 | Missing sources | At-Bay Post-Cyber Event Hardening (S2), Coalition Deepfake Response (S1), Coalition EBR announcement (S1), At-Bay packages (S1), Coalition ACP launch (S1) | Add them to 04_references / Sources.csv with the URLs in §7. |

---

## 7. Source list (all retrieved via search on 2026-09-27; none opened directly)

**Coalition**
- Coalition Launches New Active Cyber Policy (2025-04-09): https://www.businesswire.com/news/home/20250409047735/en/Coalition-Launches-New-Active-Cyber-Policy ; https://www.coalitioninc.com/announcements/coalition-launches-new-active-cyber-policy (S1)
- Coalition ACP in Canada (2026-03-11): https://insurance-canada.ca/2026/03/11/coalition-launch-active-cyber-policy/ (S2)
- Affirmative AI Endorsement: https://www.coalitioninc.com/announcements/coalition-adds-new-affirmative-ai-endorsement-to-cyber-policies ; https://www.coalitioninc.com/ai-coverage (S1)
- Deepfake Response Endorsement (Dec 2025): https://www.coalitioninc.com/announcements/coalition-adds-deepfake-response-endorsement ; https://siliconangle.com/2025/12/09/coalition-expands-cyber-insurance-cover-deepfake-driven-reputation-attacks/ ; https://fintech.global/2025/12/18/coalition-adds-deepfake-cover-to-cyber-insurance/ (S1/S2)
- Enhanced Business Recovery (Apr 2026; release reported Aug 2026): https://www.coalitioninc.com/announcements/coalition-unveils-enhanced-business-recovery-endorsements ; https://www.coalitioninc.com/blog/cyber-insurance/introducing-enhanced-business-recovery ; https://insurance-canada.ca/2026/04/16/coalition-enhanced-business-recovery-endorsements/ ; https://www.iamagazine.com/2026/08/17/coalition-releases-enhanced-business-recovery-endorsements/ ; https://www.reinsurancene.ws/coalition-introduces-enhanced-business-recovery-endorsements-for-cyber-incidents/ (S1/S2)
- $0 retention with Coalition IR; "under five minutes": https://www.coalitioninc.com/announcements/coalition-eliminates-out-of-pocket-security-and-forensics-costs-for-policyholders-facing-a-cyber-claim ; https://www.insurancebusinessmag.com/us/news/cyber/coalition-eliminates-outofpocket-costs-for-security-forensics-services-241017.aspx ; https://www.coalitioninc.com/incident-response (S1/S2)
- Vanishing retention blog: https://www.coalitioninc.com/blog/cyber-insurance/how-vanishing-retention-rewards-security-conscious-policyholders (S1, title only)
- 2026 Cyber Claims Report (2026-03-05): https://www.coalitioninc.com/announcements/2026-cyber-claims-report ; https://www.coalitioninc.com/claims-report/2026 (S1)
- Catalog: ACP FAQ https://help.coalitioninc.com/hc/en-us/articles/33998071846811-Active-Cyber-Policy-FAQ ; Breach Response Separate Limits https://help.coalitioninc.com/hc/en-us/articles/7665647884443 ; Control https://help.coalitioninc.com/hc/en-us/articles/7687332367259-Coalition-Control-Overview (K)

**At-Bay**
- InsurSec packages / Stance MDR for Email (2025-10-02): https://www.businesswire.com/news/home/20251002591457/en/ ; https://www.reinsurancene.ws/at-bay-reveals-new-cyber-insurance-solutions-for-ransomware-and-financial-fraud/ ; https://www.at-bay.com/packages/ ; https://www.at-bay.com/mdr/ (S1/S2)
- Post-Cyber Event Hardening (Mar 2026): https://ffnews.com/newsarticle/at-bay-launches-post-cyber-event-hardening-service-targeting-unresolved-vulnerabilities-that-drive-repeat-claims/ ; https://job-boards.greenhouse.io/atbayjobs/jobs/7710066003 (S2)
- 2026 InsurSec Report (Apr 2026): https://www.at-bay.com/articles/insursec-report-2026-key-findings-cyber-risk/ ; https://www.helpnetsecurity.com/2026/04/23/cyber-insurance-claims-report/ ; https://www.insurancebusinessmag.com/us/news/cyber/one-ransomware-crew-now-drives-half-of-all-cyber-claims-atbay-573139.aspx (S1/S2)
- Form AB-CYB-001.2 (08/2023): https://www.at-bay.com/wp-content/uploads/2023/06/Cyber-Insurance-Policy-Form.pdf (K; blocked)

**Corvus / Travelers**
- https://www.corvusinsurance.com/smart-cyber-and-cyber-excess ; https://www.corvusinsurance.com/pressroom/travelers-cyber-risk-services ; https://investor.travelers.com/newsroom/press-releases/news-details/2025/Travelers-Announces-Enhanced-Services-for-Cyber-Liability-Customers/default.aspx ; https://corvusinsurance.com/news-and-insights/cyber-coverage-explained-contingent-business-interruption-cyber ; https://www.corvusinsurance.com/news-and-insights/cyber-coverage-explained-business-interruption/ ; https://www.insurtechinsights.com/corvus-expands-its-small-business-cyber-offering-whilst-doubling-underwriting-offer/ ; form https://www.corvusinsurance.com/hubfs/Corvus%20Smart%20Cyber%20Policy%20Form.pdf (K)

**Cowbell**
- https://cowbell.insure/prime-100-standalone-admitted-cyber-insurance/ ; https://cowbell.insure/prime-250/ ; https://cowbell.insure/news-events/pr/prime-one-us-emerging-ai-quantum-risks/ ; https://www.prnewswire.com/news-releases/cowbell-launches-prime-one-in-the-us-introducing-cyber-coverage-for-emerging-ai-and-quantum-risks-302748534.html ; https://cowbell.insure/news-events/pr/cowbell-adds-social-engineering-coverage-to-its-cyber-insurance-program/ ; https://www.theinsurer.com/cyber-risk/news/cowbell-cyber-launches-15mn-limits-program-with-obsidian-and-benchmark/ ; https://ryskly.com/product/cowbell-cyber-inc-cowbell-prime-plus-usa (S3) ; specimen https://home.sayatalabs.com/cnc-wb/get_resource/carriers/SAMPLE_POLICY_FORM/COWBELL (K)

**Corgi**
- https://www.corgi.insure/cyber-liability (S1 via search) ; https://www.quotesweep.com/insurtech/corgi (S3)
- AI coverage (2026-05-04): https://www.prnewswire.com/news-releases/corgi-launches-ai-insurance-coverage-to-protect-businesses-when-ai-goes-wrong-302762029.html ; https://www.artificiallawyer.com/2026/05/05/corgi-launches-ai-liability-insurance/ ; https://fintech.global/2026/05/06/corgi-launches-ai-insurance-product-to-cover-emerging-risks/
- Admitted carrier (2026-08-26): https://www.prnewswire.com/news-releases/corgi-insurance-launches-admitted-insurance-carrier-302860246.html ; https://www.theinsurer.com/ti/news/corgi-launches-admitted-commercial-lines-carrier-2026-08-26/ ; https://www.insurancebusinessmag.com/us/news/breaking-news/corgi-built-its-name-insuring-ai-startups--its-new-carrier-targets-dry-cleaners-salons-and-more-587646.aspx ; https://www.reinsurancene.ws/ai-financial-infrastructure-firm-corgi-launches-admitted-insurance-carrier/
- Funding (2026-07-23): https://techcrunch.com/2026/07/23/insurance-startup-corgi-reportedly-raised-more-money-at-4b-its-third-round-in-eight-weeks/

**Vouch, Embroker, Resilience**
- https://www.vouch.us/blog/cyber-insurance ; https://www.vouch.us/insurance101/cyber-insurance (S1) ; https://www.quotesweep.com/blog/best-cyber-insurance-small-business (S3) ; https://www.embroker.com/blog/cyber-insurance-requirements-for-smbs-usa-2025

**Elpha Secure, Cysurance**
- https://elphasecure.com/docasset/documents/Sample-Policy.pdf (K) ; https://www.insurerbrain.com/wiki/Elpha_Secure (S3) ; https://www.cysurance.com/services/ ; https://www.protect360.cysurance.com/ (K)

**AI-risk insurers** (all S3)
- https://medium.com/@purdyhouse/the-first-ai-liability-insurance-product-has-25-million-in-coverage-five-exist-worldwide-575a2903b17b ; https://agentinsured.eu/tools/carrier-comparison/ ; https://agentinsured.eu/articles/munich-re-aisure-ai-performance-insurance-europe ; https://agentmarketcap.ai/blog/2026/04/15/ai-agent-error-insurance-lloyds-aig-beazley-hallucination-liability ; https://aicoverageguide.com/comparison.html

**Beazley**
- BBR 5.0 enhancements (BZCBR184_04/25): https://www.beazley.com/globalassets/full-spectrum-cyber/bbr-5.0-enhancements-and-clarifications.pdf (S1 via search) ; specimen (F00653 02/2025, per catalog) https://portal.bigimd.com/files/Membership%20Benefits/Cyber%20Liability%20Insurance/Beazley_SpecimenPolicyForm.pdf (K)

---

## 8. Not verified this round (for a follow-up with network access)

1. Open the Coalition issued policy (mwvhomelessalliance.org) and settle: is it ACP or admitted "Cyber Policy 3.0"? Check the cancellation basis (short-rate?), ERP percentages, hammer, $1,010 pre-claim, and the fraud-channel wording.
2. Open At-Bay AB-CYB-001.2 and check ERP, hammer, restoration and the fraud-channel wording.
3. Open the Vouch certificate and confirm which figures are that insured's purchased sublimits.
4. Open BBR 5.0 specimen F00653: check the fraudulent-instruction channels (written or telephone?), the hammer, and whether system-failure BI (not just data recovery) is in the base.
5. Corgi: retention, media placement, and whether cyber is (or will be) written on the new admitted paper.
6. Find product-level data for Boost, Measured, Relm, Embroker and Resilience (nothing found this round).
