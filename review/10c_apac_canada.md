# 10c. Ideas from Asia-Pacific and Canadian small-business cyber policies, adapted for Harborline

Prepared September 27, 2026. Scope: Australian, New Zealand, Asian and Canadian SME cyber products, 2023–2026, assessed for Harborline (US admitted, Colorado law, US businesses with $1M–$50M revenue; sample insured Cedar Ridge Accounting Group).

## How to read this report

**Evidence levels** (used on every row):

| Tag | Meaning |
| --- | --- |
| **[O]** | Opened and read at source. **None this session.** Every insurer, regulator and trade-press domain tried (emergenceinsurance.com, centrewest.com.au, psychology.org.au, chubb.com, qbe.com, deltainsurance.com.au, godigit.com, bizcover.com.au, mips.com.au, bflcanada.ca, cfc.com, coalitioninc.com, insurancebusinessmag.com, insurance-canada.ca) returned an egress block. None was retried. |
| **[SS]** | Search-result snippet or search-engine summary. Paraphrased, never quoted as clause text. 20 of 20 WebSearch calls used. |
| **[CAT]** | Note in `/home/user/insurance/catalog/cyber_policies.csv` / `CATALOG.md` (form codes, editions and URLs come from there). |
| **[BK]** | My background knowledge. Verify before quoting. |
| **[PKG]** | Harborline package or the earlier review reports (reports 00–09 in this folder). |

**Rules I followed:**
- No carrier clause text is reproduced. All carrier features are paraphrased from snippets or catalog notes.
- Every block of clause wording is labeled **Harborline draft**. The drafts are there to show the mechanism. Rewrite them in your own words before they go into the submission.
- Anything already on the planned fix list in `README.md` is labeled **Planned (T-ID)** and is not re-proposed as new. Where an idea builds on a planned fix, I say what it adds.

---

## 1. Bottom line

Harborline already has most of what makes the best APAC and Canadian SME forms stand out: nil-retention first response outside the limit, suspected-incident response, bundled pre-incident help, a betterment-style fund, affirmative AI cover, key-customer and one-accountant BI mechanics, and written claims-service standards. So the transferable ideas are mostly *structural refinements*, not new coverages.

**The six worth doing:**

| # | Idea | Where it comes from | Verdict |
| --- | --- | --- | --- |
| 1 | **Verified-framework tier.** An independent attestation to a recognized baseline earns a premium credit, access to higher limits and a short-form renewal. It never becomes a coverage condition | Singapore Cyber Essentials mark (insurer discounts); Australian Essential Eight ML1/ML2 renewal questions | **ADAPT**, using CIS Controls v8.1 IG1, NIST CSF 2.0 profiles or the FTC Safeguards Rule WISP as the US reference |
| 2 | **External early warning = reasonable suspicion.** A notice from the FBI, CISA, your bank, your IT provider or our own monitoring is always enough to trigger investigation cover, even if nothing is found | Japanese SME cyber (Tokio Marine: investigation costs covered after an alert from police, a public body or a security firm, even where nothing happened) | **ADAPT** (adds to planned T2-1f/W-09 and W-25) |
| 3 | **Yearly cap on retentions.** After one retention is paid in a policy period, later incidents that period carry no dollar retention | CFC Cyber Proactive Response (2025): option to pay only one deductible per policy term | **ADAPT** |
| 4 | **No retention on panel forensics and breach coach if reported within 72 hours** | Coalition Active Cyber Policy Canada (March 2026): $0 retention with Coalition Incident Response. Emergence reportedly removed the excess for turnover under A$25M | **ADAPT** (scoped narrowly) |
| 5 | **Ransom-payment reporting support.** If we pay for you, we give you the facts a government report needs within 12 hours, and we pay the cost of filing | Australia's Cyber Security Act 2024: 72-hour ransomware payment report, with the clock starting when you learn someone (e.g., an insurer) paid for you | **ADAPT** (adds to planned T2-19) |
| 6 | **Contractual services schedule plus an "IT provider" clarifier** | CFC (prevention services written into the wording), Delta AU, Emergence cyberSuite, Chubb Canada Cyber Stack, Japan's お助け隊 bundle; Emergence CEP-005/005.1 IT-contractor cover | **ADAPT** (both) |

**Also recommended:**
- **ADOPT:** make foreign privacy regulators (Canada's OPC, Québec's CAI, others) explicit in "regulatory proceeding".
- **ADAPT:** examples and notes, CFC-style, in a companion guide.
- **OPTIONAL:** goodwill payments to affected clients (Japan), one reinstatement (Emergence/CFC), goods-diversion fraud (Emergence), an MSP-embedded micro tier (Japan).
- **SKIP:** full-limit system failure (Emergence 005.1) and widespread-event endorsement (Chubb AU E13), because they conflict with deliberate, review-supported design choices.

**Do not copy** (section 5): Australian PDS/TMD and s.54 mechanics, ASD/CERT-In/PDPC reporting clocks, Essential Eight references, Québec's Civil Code art. 2503 defense-outside-limits rule, Law 25 penalty language, French-first contract rules, and India's IRDAI UIN and "sachet" formats.

---

## 2. Feature inventory: 18 features

Status column: **Has** = Harborline already has it; **Partly** = has the substance but not this mechanism; **No** = absent; **Planned** = on the review fix list.

| # | Feature | Carrier / source; form, edition, date | What it does | Why it's good for SMBs | Evidence (URL, date, level) | Harborline status | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | Nil-retention first response with its own limit | CFC Cyber Proactive Response (CPR), launched Apr 2025; CFC nil-deductible IR article Aug 2024. Coalition ACP Canada, Mar 10, 2026 ($0 retention using Coalition IR). Chubb Cyber ERM 2.2 (AU): "Emergency Incident Response Expenses" in the first 48 hours after discovery; IR manager contact within 1 hour | Initial incident response is paid from dollar one, from a separate limit | Removes the "can I afford to call?" hesitation, and early calls cut severity | cfc.com/en-us/knowledge/resources/articles/2024/08/cyber-coverage-highlights-nil-deductible-and-separate-limit-for-incident-response/ (Aug 2024) [SS]; coalitioninc.com/en-ca/announcements/coalition-brings-active-cyber-policy-to-canada (Mar 2026) [SS]; chubb.com/au-en/business/cyber-services-overview.html (n.d.) [SS]. Whether Chubb waives the retention on the 48-hour costs was **not confirmed** | **Has.** Coverage A: 72 hours, $25K, outside the aggregate, $0 retention. Per-period cap **Planned (T2-8)** | Keep. No new clause |
| F2 | Panel-response retention waiver (beyond first response) | Coalition ACP Canada: $0 retention on forensics and IR when the insured uses Coalition IR (Mar 2026). Emergence CEP-005 (2024) or CEP-005.1 (Feb 2026): trade press reports the excess was removed for insureds with turnover under A$25M (which covers it applies to, and which edition, **not confirmed**) | No retention on the investigation and legal-coach work when the carrier's own or panel team runs it | Steers insureds to the fastest, cheapest response, and removes the biggest out-of-pocket surprise in a breach-only claim | insurance-canada.ca/2026/03/11/coalition-launch-active-cyber-policy/ (Mar 11, 2026) [SS]; insurancebusinessmag.com/au/news/cyber/emergence-insurance-revamps-cyber-policy-478685.aspx (date not shown) [SS] | **No** (B carries $7,500) | **ADAPT** (§3.4) |
| F3 | One deductible per policy period | CFC CPR (Apr 2025): offered at nil deductible with unlimited reinstatements, or, for a lower premium, one deductible per policy term however many events | Caps what the insured pays out of pocket in a year | SMBs hit once are more likely to be hit again soon (At-Bay: 2x within two years [PKG 02]). A second retention in one year is what hurts cash flow | cfc.com/en-us/knowledge/news/2025/04/cfc-reinvents-cyber-insurance-with-launch-of-new-product/ (Apr 2025) [SS]; insurancejournal.com/news/national/2025/04/02/818156.htm (Apr 2, 2025) [SS] | **No.** Has one retention per incident (III.1.3) | **ADAPT** (§3.3) |
| F4 | Each-incident limit / reinstatement | Emergence CEP-005.1 (Feb 2026): policy aggregate replaced with an Each Incident Limit. CFC CPR (Apr 2025): unlimited reinstatements | A second, unrelated event gets a fresh limit | Protects a small firm whose first event used the whole limit | emergenceinsurance.com/wp-content/uploads/sites/6/2026/02/Emergence_Cyber-Event-Protection_Summary-of-Key-Changes_CEP005-to-CEP005.1_02.26.pdf (Feb 2026) [SS]; CFC as F3 [SS] | **No.** Unlimited reinstatements deliberately declined for aggregation risk (rationale L261 [PKG]) | **OPTIONAL** (§4.2) |
| F5 | Suspicion trigger via **external alert**, paid even if nothing is found | Tokio Marine & Nichido サイバーリスク保険 (Japan). Covers investigation costs for a *possible* attack (サイバー攻撃の"おそれ"). Where the investigation followed a notice from a security operations firm, the police or a public body, costs are paid even if the result is "nothing happened". Also pays recovery and recurrence-prevention costs | Makes the external alert itself the trigger | SMBs usually learn of compromise from outsiders (FBI, bank, MSP). They should never have to argue that their suspicion was "reasonable" | tokiomarine-nichido.co.jp/hojin/baiseki/cyber/hosho02.html (n.d.) [SS]; chuokai.or.jp/archive/insu/pdf/privacy/tokiomarine-nichido_pamphlet_2025.pdf (2025) [SS] | **Partly.** A covers "suspected"; the B/trigger fix is **Planned (T2-1f/W-09)**; precautionary shutdown **Planned (W-25)** | **ADAPT** (§3.2): the "external alert is always enough" rule is new |
| F6 | Prevention services written into the policy | CFC CPR (Apr 2025): described as the first insurer to *contractually* provide attack-prevention services (24/7 monitoring, access to its security team) inside the wording. Emergence CEP-005 via cyberSuite: 1-hour analyst consult, templates (e.g., IR plan), 24/7 external scanning. Delta Insurance AU (wording Delta_AU_CYB_0824, Aug 2024): baseline security assessment, targeted ransomware assessment and surveillance, IR plan preparation. Chubb Canada Cyber Stack (sheet 11/05/2025): loss-mitigation services free for the first full year, value "up to $28,000", select services for ≤100 employees. Northbridge Canada: CyberScout services automatically included. QBE QCyberPrepare: secure "cyber saferoom" for out-of-band IR comms | Turns marketing services into a defined deliverable | SMBs lack security staff. A named service list tells them what they get and when | cfc.com (Apr 2025) [SS]; insurance-edge.net/2025/04/03/cfc-claims-two-world-firsts-lets-get-into-it/ (Apr 3, 2025) [SS]; Emergence (Feb 2026) [SS]; deltainsurance.com.au/products/cyber-liability-insurance (n.d.) [SS] + [CAT]; chubb.com/content/dam/chubb-sites/chubb-com/ca-en/business-insurance/cyber-enterprise-risk-management-cyber-erm/documents/pdf/chubb_chubbcyberstack_stackingupyourdigitaldefense_sheet_110525-ca-en.pdf (Nov 2025) [CAT][SS]; cyberscout.com press release (n.d.) [SS]; qbe.com/newsroom/news/how-qbes-global-cyber-proposition-is-constantly-evolving-to-support-brokers-and-customers (n.d.) [SS] | **Partly.** Pre-issue scan; $2,500 pre-incident help; claim-free reduction references "critical issues we report" but nothing defines the service or "critical issue" (undefined-term finding, review 4.1) | **ADAPT** (§3.6) |
| F7 | Government-framework-linked terms | **Australia:** renewals increasingly ask about ASD Essential Eight alignment at ML1; ML2 reportedly unlocks higher limits or better price (vendor blogs, 2026; no insurer-specific credit found). **Singapore:** CSA Cyber Essentials mark holders are eligible for discounted cyber insurance rates from named insurers (Blackpanda, Delta Underwriting, Protos Labs, QBE Singapore). The mark is valid 2 years; CSA co-funds up to 70% of a CISO-as-a-Service engagement; marks expanded in 2025–26 to cloud, AI and OT. **India:** CERT-In's 15 Elemental Cyber Defence Controls for MSMEs | A recognized, externally checked baseline replaces pages of questions and earns better terms | One credential, reused across insurers and clients; a clear path to better pricing | csa.gov.sg/our-programmes/support-for-enterprises/sg-cyber-safe-programme/cybersecurity-certification-for-organisations/cyber-essentials/certification-for-the-cyber-essentials-mark/ (n.d.) [SS]; securitypulse.ai/resources/cyber-essentials-certification-singapore/ (2026) [SS]; 4it.com.au/cybersecurity/cyber-insurance-australian-sme-2026/ (2026) [SS, vendor, low]; cyberpulse.com.au/2026/02/25/cyber-insurance-in-australia/ (Feb 25, 2026) [SS, low]; practiceguides.chambers.com/practice-guides/cybersecurity-2026/india/ (2026) [SS] | **Partly.** Item 7 credits are control-by-control; the application already maps to NIST CSF 2.0 and CIS v8.1 [PKG] | **ADAPT** (§3.1, §4) |
| F8 | Ransomware-payment reporting built around the insurer paying | **Australia**, Cyber Security Act 2024, Part 3 (in force May 30, 2025): businesses with ≥A$3M turnover must report a ransomware payment to ASD within 72 hours of paying *or of becoming aware that a payment was made*, including by a third party such as an insurer. Civil penalty 60 penalty units. **No AU wording clause reflecting it was found** | Puts the reporting duty on the insured even when the insurer pays | Insureds can't meet a clock they don't know has started | minterellison.com/articles/mandatory-ransomware-payment-reporting-obligations-in-force (2025) [SS]; twobirds.com/en/insights/2024/australia/australias-first-standalone-cyber-security-law-the-cyber-security-act-2024 (2024) [SS]; coalitioninc.com/blog/cyber-insurance/australia-ransomware-reporting-laws (n.d.) [SS] | **Partly.** III.3.5: 24-hour report to FBI/CISA "of making it"; legal reports need no consent. "Report before payment" **Planned (T2-19)** | **ADAPT** (§3.5) |
| F9 | IT-contractor and data-processor events | Emergence CEP-005 (2024; CEP-005.1 Feb 2026): BI from a cyber event at the insured's **IT contractor's** business; system-failure BI; response costs when a cyber event affects IT contractors or data processors; AI-caused cyber events covered | Names the MSP as a source of loss rather than leaving it to general definitions | Most SMBs outsource IT (Cedar Ridge uses Front Range IT Partners [PKG]). MSP compromise and MSP error are common paths | insurancebusinessmag.com/au/news/cyber/emergence-updates-cyber-policy-wording-for-australian-smes-565467.aspx (Feb 2026) [SS]; emergenceinsurance.com/emergence-strengthens-cyber-event-protection-with-cep-005-1-upgrade/ (Feb 2026) [SS] | **Partly.** Covered in substance through E, "privacy event … while a dependent provider holds it", "security failure" and "system failure", but nowhere in terms an insured would recognize. "Outside IT provider is not an executive" **Planned (W-34)** | **ADAPT** (§3.7): clarifier only |
| F10 | Plain-language, annotated wording | CFC: interactive wording with commentary and worked examples for each clause (Apr 2025). Emergence: combined "Important Information" (PDS-style) and wording document; flagship SME policy for micro to mid-market (CEP-005.1, Feb 2026) | Explains how clauses respond, outside the operative text | SMB buyers without brokers or counsel understand what they bought | cfc.com/en-us/knowledge/resources/articles/2025/04/interactive-cyber-policy-wording/ (Apr 2025) [SS]; Emergence CEP-005.1 [CAT] | **Partly.** "How to read this policy"; but the cover promises "plain-English notes" that don't exist (review 4.1 cross-reference failure) [PKG] | **ADAPT** (§3.8) |
| F11 | Push-payment theft; physical goods theft option | Emergence CEP-005: criminal financial loss includes push-payment theft. CEP-005.1: optional cover extended to theft of physical goods | Covers authorized-push-payment fraud; option for goods diverted by fake orders | APP fraud is the top SMB fraud loss; goods diversion hits distributors | Emergence (Feb 2026) [SS] | **Has** push-payment (Coverage H, fraudulent instruction; path fixes **Planned (T2-1, T2-1a)**). Goods: **No** | APP: keep. Goods: **OPTIONAL** (§4.3) |
| F12 | Goodwill / apology payments to affected people | MS&AD (Mitsui Sumitomo) Cyber Protector: pays condolence money or gifts (見舞金・見舞品), reported at ¥50,000 per corporate victim or ¥1,000 per individual. Sompo Japan: pays condolence payments and "trust recovery" (信頼回復) costs | Funds small gestures that keep customers after a breach | Cheaper than losing clients; complements reputational harm cover | ms-ins.com/business/indemnity/pd-protector/ (n.d.) [SS; the snippet's attribution between that page and aspicjapan.org is uncertain]; sompo-japan-cyber.jp/coverage/ (n.d.) [SS] | **No.** B pays PR and monitoring; N pays lost profit | **OPTIONAL** (§4.1) |
| F13 | Government-certified SME bundle with simple insurance | Japan, METI/IPA サイバーセキュリティお助け隊サービス: certified private providers bundle 24/7 monitoring, a help desk, on-site dispatch and simple cyber insurance. Reported at ≤¥10,000/month (network type) or ≤¥2,000 per device/month | Security service and insurance sold as one low-cost product | Reaches micro-firms that never buy standalone cyber | meti.go.jp/policy/netsecurity/otasuketai.html (n.d.) [SS]; ipa.go.jp/security/otasuketai-pr/ (n.d.) [SS] | **No** | **OPTIONAL** as distribution, not form (§4.4) |
| F14 | Betterment as a named insuring agreement | Travelers Canada CyberRisk (highlight sheet Jan 17, 2023): pays to improve systems after a breach where recommended to remove the vulnerability | Pays upgrades, not just like-for-like | Stops the same attack recurring | travelerscanada.ca/iw-documents/canada/CyberRisk-Coverage-Highlight-Sheet_230117.pdf (Jan 2023) [CAT][SS] | **Has.** Coverage G ($25K, incident-team-recommended, 90 days). Clock fix **Planned (T2-18)** | Keep |
| F15 | Privacy-regulator coverage for Canadian regimes | Canadian forms respond to PIPEDA (OPC; "real risk of significant harm" notices) and Québec Law 25 (CAI; administrative monetary penalties up to C$10M or 2% of worldwide turnover; penal fines up to C$25M or 4%) | Defense of foreign privacy regulators' investigations | US SMBs with Canadian clients or staff face these regulators too | gowlingwlg.com/en/insights-resources/articles/2022/law-25-the-cost-of-a-privacy-breach-just-went-up (2022) [SS]; mccarthy.ca/…/navigating-the-legislative-landscape-on-data-breaches-2026-data-breach-insights-part-3 (2026) [SS] | **Unclear.** "Regulatory proceeding" names "federal, state or local government agency", which reads as US-only | **ADOPT** (§3.9) |
| F16 | Full-limit system failure and non-IT contingent BI | Emergence CEP-005.1 (Feb 2026): optional non-IT contingent BI and system failure raised from A$100,000 to full limit | Removes the systemic-risk sublimit | Simple for buyers | Emergence key-changes PDF (Feb 2026) [SS] | Deliberate $250K system-failure sublimit (review #8 supports it); P optional | **SKIP.** Conflicts with review-supported design and **Planned (T2-3)** |
| F17 | Widespread-event endorsement | Chubb Cyber ERM 2.2 E13 (AU): separate limit, retention and coinsurance for widespread events; ERM 2.2 splits "limited impact" and "widespread" events | Ring-fences systemic loss | Protects carrier solvency more than the SMB | chubb.com …/erm-v2-2-e13-widespread-event-endorsement.pdf [CAT]; Chubb v2 vs 2.2 factsheet [SS] | Decision already scoped in **Planned (T2-3)** | **SKIP** (not new) |
| F18 | Sublimit transparency / one-page coverage summary | Emergence CEP coverage summary published alongside the wording [CAT]; QBE NZ QCyberProtect 2025 coverage sheet [CAT]; Emergence 005.1 moving sublimits to full limit [SS] | Shows every limit on one page | Buyers see what's capped | CATALOG.md rows for Emergence and QBE NZ [CAT] | Item 6 exists; per-incident vs per-period **Planned (T2-1e)** | Not new: fold into T2-1e |

Also checked; nothing standout for the Harborline form:
- **Zurich Australia** (paper for Cowbell's "Prime One" SME cyber, turnover to A$100M, limits to A$5M) [SS].
- **Allianz Australia** (capacity partner of Coalition, whose ACP launched in Australia) [SS].
- **QBE NZ** QCyberProtect CYB0625 (06/2025): the coverage sheet lists IT and non-IT BI, reputational loss, PCI and bricking [SS/CAT], all already in Harborline.
- **Intact and Aviva Canada** (cyber sold as package add-ons; Aviva offers "Privacy Expense only" and "Business Disruption Expense only" options) [CAT].
- **Indian** commercial wordings (e.g., Go Digit UIN IRDAN158CP0011V01202122; SBI, Tata AIG, HDFC ERGO) [CAT]: none opened; no distinctive SME feature surfaced in snippets.
- **Hong Kong:** the only catalogued wording is Beazley InfoSec HK (03/2019), outside the 2023–26 window.
- **Malaysia:** only regulatory changes surfaced.

---

## 3. ADOPT / ADAPT items: Harborline draft clauses

Each item says where the text goes and what it touches in the current form or the planned fixes.

### 3.1 Verified-framework tier (F7): ADAPT

**Idea.** Singapore ties insurer discounts to a government-recognized SME certification. Australia uses Essential Eight maturity as a renewal gate and a price lever.

The US has **no government certification for SMB cyber hygiene**:
- CISA Cyber Essentials is a guide and toolkit, not a mark.
- The FCC's **"U.S. Cyber Trust Mark"** is an IoT *product* label. Don't let the name suggest it is an analogue of Singapore's organizational Cyber Trust mark [BK].

So Harborline should name **a short list of attestable US baselines** (section 4) and reward an independent attestation. It should not make any framework a condition of coverage. That keeps the form's "security affects price, not coverage" principle (IV.1).

**What it adds over today's Item 7:**
- (a) one credential instead of control-by-control evidence;
- (b) eligibility benefits (limits and options) rather than only price;
- (c) a mid-term way to earn the credit, following Singapore's "certify, then get the discount" path.

**Harborline draft: Declarations, Item 7, new row**

| Security control | Verified? | What you earned |
| --- | --- | --- |
| **Verified framework**: an independent assessment in the last 12 months shows you meet one of the baselines listed in Section III, part 1.9 | No | Not earned. It would give a [x]% premium credit, let you buy the $2M or $3M limit and Coverage R without a supplemental application, and let you renew on our short-form application |

**Harborline draft: Section III, part 1, new item 9**

> **9. Verified framework credit.**
> 1. You earn this credit if you give us a **framework assessment** dated within the 12 months before the **policy period** starts. We may also accept one dated during the **policy period**.
> 2. A **framework assessment** means a written report, by an assessor independent of the systems it assesses, showing that you meet one of these baselines: (a) CIS Controls v8.1, Implementation Group 1; (b) a NIST Cybersecurity Framework 2.0 organizational profile that meets the target outcomes listed in Item 7; or (c) another baseline listed in Item 7. Your IT provider may prepare the report if it attaches the evidence we list in Item 7.
> 3. This is a pricing credit only. If you later fall short of the baseline, your coverage does not change, and we do not take the credit back during the **policy period**.
> 4. If you earn the credit during the **policy period**, we will refund the unused part of the credit, pro rata, from the date we accept your assessment.
> 5. If the assessment was wrong because of an honest mistake, Section V, part 3 applies. We may adjust the premium, never the coverage.
> 6. This credit is combined with the other premium credits in Item 7 under the stacking rule in Item 7. It does not change your **retention**.

**Where:** Item 7 (new row), III.1 (new item 9), and a new definition of **framework assessment** in Section II. Add an optional "Framework assessment" upload to the application (Part 4 or 6).

**Conflicts and dependencies:**
- **Planned (T2-16)** stacking rule: write that rule first. This credit should not stack beyond a stated maximum.
- **Review #11:** the market treats MFA/EDR as bind prerequisites. This tier sits *above* them, so it strengthens the "credits for going beyond the minimum" story.
- **III.1.5 / Planned (W-21):** this credit, unlike control credits, is not lost mid-term. Say so to avoid inconsistency.
- **V.3.4 scan estoppel / Planned (T2-7):** an attestation is part of the **application**, so the honest-mistake rule applies. Scan findings that contradict the attestation should prompt a query at bind, not a later denial.
- **Filing:** the credit has to sit in the filed Colorado rating plan. Credit percentages need actuarial support (review 4.4 already flags arbitrary credit numbers).
- **For Cedar Ridge:** it already has a WISP under the FTC Safeguards Rule following IRS Publication 4557 [PKG, application 4.2 and 7.1], so an IG1 attestation from Front Range IT with evidence is realistic.

### 3.2 External early warning (F5): ADAPT

**Idea.** Japan's large carriers pay investigation costs when an outside body warns the insured of a possible attack, even if nothing is found.

The US has the same alert sources:
- FBI victim notifications;
- CISA's Pre-Ransomware Notification Initiative [BK];
- banks, the insured's MSP, SaaS providers' breach notices;
- Harborline's own scanning.

**What it adds over planned T2-1f/W-09 and W-25:** those fixes say a *reasonably* suspected incident qualifies. This clause removes any argument about reasonableness when the trigger is an outside alert. It also gives the $2,500 "pre-incident assistance" a clean, separate job, which resolves the overlap flagged in **Planned (T2-8)**.

**Harborline draft: Section II, new definition**

> **Early warning** means a notice to you, from any of the following, that your **computer systems** may have been compromised, or that your credentials or data are being offered or used by criminals: the FBI, CISA, the U.S. Secret Service or another government agency; your bank; your **IT provider**; a **dependent provider**; a security company monitoring your systems; or us.

**Harborline draft: Coverage A, added sentence**

> An **early warning** is always a reasonably suspected **incident**. When you report one through any channel in Item 10, we will provide **incident response services** to investigate it, even if the investigation shows that nothing happened. An investigation that finds nothing is not an **incident** or **claim** for your claim-free reduction or when we price your renewal.

**Harborline draft: V.2.3, re-scoped**

> **Pre-incident assistance.** If you have a security question before anything is suspected and before any **early warning** (for example, whether an email is phishing or whether a vendor's security terms are adequate), we will provide up to $2,500 of legal or forensic advice. …

**Where:** Section II (definition), Coverage A (I.A), V.2.3, and V.6.2 (add "or an investigation of an **early warning** that finds nothing").

**Conflicts and dependencies:**
- Align the list of alert sources with the "government agency / dependent provider" list in the **Planned (W-25)** precautionary-shutdown text.
- A still ends at 72 hours / $25K. If the investigation runs on and nothing is found, B pays under **Planned (T2-1f)**, with the panel waiver in §3.4.
- Uses the term **IT provider** defined in §3.7.

**Cost note [assumption]:** alert frequency is uncertain. CISA reported issuing more than a thousand pre-ransomware notifications a year [BK, verify]. Cost is bounded by A's per-period cap (T2-8).

### 3.3 Yearly cap on retentions (F3): ADAPT

**Idea.** CFC's CPR lets insureds pay one deductible per policy term, however many events occur.

**Why it fits Harborline:**
- It completes the existing "one retention per incident" promise (III.1.3).
- It costs almost nothing. At a frequency of about 1.2–2% a year [PKG 4.2], the chance of two retention-bearing incidents in a year is roughly 0.01–0.02%, about $1–2 of expected cost per policy at $7,500 [assumption].
- It is easy to explain.

**Harborline draft: Declarations, Item 5, new row**

| Retention | Amount |
| --- | --- |
| **Most you pay in retentions each policy period** | One retention: **$7,500** (the retention shown above, after credits) |

**Harborline draft: Section III, part 1, new item 3A**

> **3A. A yearly cap on retentions.** Once the dollar **retentions** you have paid, for **incidents** you **discover** and **claims** first made against you during this **policy period**, add up to the amount in Item 5, no further dollar **retention** applies to later **incidents** or **claims** in that **policy period**. **Waiting periods** and coinsurance still apply.

**Where:** Item 5 and III.1 (after item 3).

**Conflicts and dependencies:**
- **III.1.4** (settling within your retention) becomes moot once the cap is met. No change is needed.
- **Planned (T2-1c):** one retention covers an incident and all its claims, even claims made in a later period. State that a retention paid under this rule counts toward the cap in the period when the **incident** was discovered.
- **V.6.1 claim-free reduction** and the **band table (review 4.3):** the cap equals whatever the reduced retention is.
- The **fraud 72-hour retention** ($2,500) counts toward the cap at the amount actually paid.
- **"Discover"** is undefined; its definition is **Planned (T2-10)**.

### 3.4 No retention on panel forensics and breach coach if reported within 72 hours (F2): ADAPT

**Idea.** Coalition Canada waives the retention on security and forensics when the insured uses Coalition's in-house IR. Emergence reportedly removed the excess for smaller insureds.

Harborline has no in-house IR team, but it does have a panel. It already rewards speed with its 72-hour fraud retention. Combining the two keeps the rule consistent and steers insureds to privileged, panel-led response.

**Harborline draft: Section III, part 2, new item 6**

> **6. No retention for a fast, panel-led response.** If you report an **incident** to us within 72 hours after you **discover** it, no **retention** applies to the fees of our panel breach coach and panel forensic firm under Coverage B. Your **retention** still applies to other loss from the same **incident**, such as notification costs, extortion payments, restoration costs or liability.

**Where:** III.2 (new item 6), with a footnote on the Item 6 B row ("$0 on panel coach and forensics if reported within 72 hours").

**Conflicts and dependencies:**
- **III.1.3 (one retention per incident):** write it so the single retention is taken from the *other* covered loss. It should not be deemed satisfied by waived fees.
- **Planned (T2-12)** already exempts panel vendors from consent. This is consistent.
- **Planned (T2-10):** needs the definition of "discover".

**Cost note [assumption]:** 1.21% frequency × about 70% of claims using panel forensics × $7,500 ≈ $60 a year per policy (about 1% of premium), partly offset by earlier reporting.

**Not recommended:** Emergence's broader "no excess under A$25M". It would remove the retention from most of Harborline's book.

### 3.5 Ransom-payment reporting support (F8): ADAPT

**Idea.** Australia's 2024 Act starts the insured's 72-hour clock when it *learns* that someone paid on its behalf. No Australian wording clause reflecting this was found.

The same gap exists for Harborline:
- III.3.5 requires a report "within 24 hours of making it". That is awkward when Harborline or its negotiator pays directly, which III.3.4 allows.
- US regimes with payment-report clocks include NYDFS Part 500.17(c) (24-hour notice of an extortion payment for covered entities) [BK] and CIRCIA's 24-hour ransom-payment report once the final rule is issued (still pending; see **Planned (T1-10)**).

**Harborline draft: Section III, part 3, replace item 5 and add item 6**

> **5. Report the payment.** Report any extortion payment to the FBI (through its Internet Crime Complaint Center) or CISA within 24 hours after it is made, whether you made it or we made it for you. [The "report the attack before any payment" requirement from planned fix T2-19 goes here.]
>
> **6. Help with government reports.** Some laws require you to report a ransom or extortion payment within a set time, and the clock can start when you learn that a payment was made for you. If we, or a negotiator we appoint, make a payment for you, we will give you in writing, within 12 hours after the payment, the facts such a report needs: the amount and currency, the date and time, the recipient's wallet or account, and the communications with the extortionist that we or our negotiator hold. We pay the reasonable cost of preparing and filing any report the law requires about the **cyber extortion** or the payment. You do not need our consent to file it.

**Harborline draft: Section II, "extortion expenses", add item 4**

> 4. the reasonable cost of preparing and filing reports about the **cyber extortion**, or about a payment, that a law requires you to make to a government agency.

**Where:** III.3.5–3.6 and the "extortion expenses" definition. Keep the existing last paragraph of III.3 ("If a law requires you to report … without our consent").

**Conflicts and dependencies:**
- **Planned (T2-19)** (report before any consented payment; sanctions reimbursement): merge the text.
- **V.1.5 "Legal deadlines come first":** consistent.
- **Planned (T1-10) CIRCIA status:** don't name CIRCIA in the form until the rule is final.
- **Other insurance (V.9):** the report-cost item sits inside Coverage C's limit.

### 3.6 Contractual services schedule (F6): ADAPT

**Idea.** CFC wrote prevention services into its wording. Delta AU, Emergence, Chubb Canada and Northbridge bundle defined services. Japan sells monitoring and insurance as one product.

Harborline already relies on services: the pre-issue scan, KEV notices under III.1.7, the claim-free "critical issues we report", and the hotline. But the form never says what the insured receives. Defining the services also fixes the undefined term "critical issue" (review 4.1).

**Harborline draft: Declarations, new Item 13 "Services included with your policy"**

| Service | What you get | When |
| --- | --- | --- |
| Internet exposure monitoring | We scan your internet-facing systems at least monthly and alert your security contact to any **critical issue** | Throughout the **policy period** |
| Incident response plan | A template plan for a business of your size, and a one-hour session with our team to complete it | Within 60 days after the policy starts, on request |
| Ransomware readiness check | A review of your backups and remote access, with a written list of fixes | Once each **policy period**, on request |
| Secure incident channel | A private messaging space for your response team to use if your email may be compromised | During any reported **incident** or **early warning** |

**Harborline draft: Section V, part 2, new item 4**

> **4. Services we provide.** We provide the services in Item 13 at no extra charge. They are not insurance, and using them does not reduce your limits or count as a **claim**. They help you lower your risk, but they cannot find every weakness. If a service misses something, or you choose not to use it, your coverage is not reduced.
>
> A **critical issue** is a vulnerability or exposure that we tell you in writing is critical, such as one listed in the U.S. government's Known Exploited Vulnerabilities catalog or a remote-access service exposed to the internet without multi-factor authentication.

**Where:** new Item 13, V.2.4, and a definition of **critical issue** in Section II. V.6.1 then uses the defined term.

**Conflicts and dependencies:**
- **III.1.7** (KEV coinsurance "we told you about in writing"): the monitoring service becomes the named channel. Say that notice goes to the security contact in Item 1 or the application.
- **V.3.4 scan estoppel / Planned (T2-7):** make clear that monthly monitoring results are not part of the **application**. Otherwise every monthly scan widens the estoppel.
- **Anti-rebating / inducement:** check that Colorado permits free loss-mitigation services. NAIC's 2020 amendments to the Unfair Trade Practices Act model allow value-added services related to the coverage or to loss mitigation [BK]; Colorado's adoption is unverified. File Item 13 with the form.
- **Services outside the limit:** **Planned (T2-8)** already asks for caps on Coverage A and pre-incident help. These services are not indemnity, so they need no cap, but the rationale should price them as expense.

### 3.7 "Your IT provider" clarifier (F9): ADAPT

**Idea.** Emergence names the insured's IT contractor and data processors as sources of covered loss.

Harborline covers most of these scenarios already, but the answer is spread across five definitions. Cedar Ridge's MSP (Front Range IT) patches, monitors and holds admin access [PKG]. One plain-English part settles which coverage responds.

**Harborline draft: Section II, new definition**

> **IT provider** means a business, other than an **insured**, that you hire under a written or electronic agreement to manage, support, monitor or secure your **computer systems**. An **IT provider** is also a **dependent provider**.

**Harborline draft: Section III, new part 9 "When something goes wrong at your IT provider"**

> 1. An attack that reaches your **computer systems** through your **IT provider** (for example, through its remote-management tools or login details stolen from it) is a **security failure** in your **computer systems**. Coverage D, not Coverage E, applies to the interruption.
> 2. A mistake by your **IT provider** that causes an outage of your **computer systems** is a **system failure**.
> 3. An attack on your **IT provider's** own systems that stops it serving you is covered under Coverage E.
> 4. If your **IT provider** tells you it has been attacked, that is an **early warning**. The reasonable cost of finding out whether your **computer systems** or data were affected is covered, even if they were not.
> 5. What your **IT provider** knows is not treated as what you know, for exclusion 2 or for Section V, part 1, unless an **executive** also knew.

**Where:** Section II (definition) and Section III (new part 9, after part 8).

**Conflicts and dependencies:**
- **Planned (W-34)** says an **executive** "does not include an outside IT provider". Item 5 depends on that fix, so keep the two consistent.
- **Planned (T2-0)** (cloud accounts are your systems): item 1 is the same logic applied to MSP tooling.
- **Planned (T2-3):** item 2 falls under the system-failure sublimit (D and F combined). Say so.
- **Planned (T2-4):** an **IT provider** is not an "infrastructure provider".
- **Planned (T2-1d)** (known-problems test): item 5 narrows whose knowledge counts.
- **Accumulation [BK]:** item 1 routes a mass MSP-tool compromise (e.g., Kaseya VSA, July 2021, which reached about 1,500 downstream businesses) to full-limit Coverage D. That is right for the insured and consistent with T2-3's rule that attacks on the insured's own systems are never widespread-limited. But it is a correlated loss for a vertical book whose members share a few MSPs (review Tier 6, "accumulation"). Name it in the reinsurance half-page.

### 3.8 Notes and examples (F10): ADAPT

**Idea.** CFC publishes an interactive wording with commentary and examples. Emergence combines its disclosure document and wording.

Harborline's cover page promises "plain-English notes" that the body doesn't contain (review 4.1). Two options:

- **(a) Recommended: companion guide.** A separate, unfiled "How your policy works" guide that walks through 6–8 Cedar Ridge-style scenarios (ransomware in tax season, a deepfake partner call, an MSP compromise, an FBI early warning). It stays outside the contract, so it can't create coverage by implication. It is still subject to advertising review.
- **(b) In-form examples in shaded boxes,** with this rule:

**Harborline draft: V.11.6, replacement**

> **6. Headings, notes and examples.** Headings, plain-English notes and examples (shown in shaded boxes) help you find your way and show how this policy may respond. They do not add to, remove or limit coverage. The policy wording controls.

**Where:** V.11.6. Fix the cover page's "How to read this policy" item 3 to match the chosen option.

**Conflicts:**
- In-form examples must be filed with the form.
- Examples that contradict the wording invite contra proferentem arguments. Keep them few and check each one against the final text.

### 3.9 Foreign privacy regulators (F15): ADOPT

**Idea.** Canadian forms respond to OPC and Québec CAI proceedings. Law 25 penalties are large.

Harborline's territory is worldwide (V.11.1). But "regulatory proceeding" names "a federal, state or local government agency", which a reader will take as US-only. A Denver CPA firm with Canadian-resident clients or staff could face an OPC inquiry.

**Harborline draft: Section II, "regulatory proceeding", replacement**

> **Regulatory proceeding** means a request for information, civil investigative demand, investigation or civil proceeding, arising from a **security failure** or **privacy event**, by:
> 1. a U.S. federal, state or local government agency (such as the Federal Trade Commission, a state attorney general or the U.S. Department of Health and Human Services); or
> 2. a government agency or data protection authority outside the United States (such as the Office of the Privacy Commissioner of Canada or Québec's Commission d'accès à l'information).

**Harborline draft: "personal information", first line**

> …information about an identifiable individual that any law, in the United States or elsewhere, requires to be protected…

**Where:** Section II, both definitions.

**Conflicts:**
- **Regulatory penalties** "where insurable" still governs. Foreign penal fines (e.g., Law 25 penal offences) are likely uninsurable, and administrative penalties are uncertain [BK]. Don't promise more.
- **Exclusion 17** (sanctions) is unaffected.
- **Planned (T1-8)** (one insurability rule) should use the same "where insurable under the law that applies" wording for foreign penalties.

---

## 4. OPTIONAL items: outlines only

### 4.1 Goodwill payments to affected people (F12)

A small, consented budget for gift cards or fee credits to affected clients, based on the Japanese 見舞金 practice. For a professional firm, a fee credit to affected clients may do more to prevent churn than the Coverage N lost-profit sublimit.

**Harborline draft outline:** add a breach-response-costs item 7:

> With our prior agreement, the cost of goodwill gestures (such as gift cards or fee credits) to individuals or clients whose information was affected, up to $[25] per individual and $[10,000] per **incident**, within the Coverage B limit. Offering them is not an admission of liability.

**Watch:**
- Class-action plaintiffs may argue about offsets.
- Keep the gestures small and uniform.

### 4.2 One reinstatement (F4)

The rationale declines unlimited reinstatements for aggregation reasons (L261). A middle path is a priced endorsement: **one** reinstatement of Coverages B, C and F for a second, unrelated **incident** discovered in the same period, capped at the original aggregate. It needs reinsurer sign-off. Best sold with the $2M option to data-heavy insureds (review #1).

### 4.3 Goods-diversion fraud (F11)

An endorsement to Coverage H for goods shipped on a **fraudulent instruction** that falsely appears to come from a customer. Relevant to distributors and manufacturers in the $1M–$50M band, not to CPA firms. Share the Coverage H limit; require verification of new ship-to addresses as the callback analogue.

### 4.4 MSP-embedded micro tier (F13)

Japan's お助け隊 shows that monitoring plus simple cover, sold by the security provider, reaches firms that never buy standalone cyber. For Harborline this is a **distribution** idea:
- MSP partners whose 24/7 monitoring meets the qualifying-MDR definition (**Planned T2-16**) sell a pre-priced $250K–$500K Harborline policy to clients with revenue under $5M;
- the MDR credit applies automatically.

Keep it out of the core form. Watch the producer-licensing and inducement rules.

---

## 5. Framework linkage: government baselines and their US analogues

| Source framework | What it is | Insurance linkage seen | Closest US analogue | How Harborline could reference it |
| --- | --- | --- | --- | --- |
| **ASD Essential Eight** (AU): 8 mitigation strategies, Maturity Levels 0–3 [BK] | Government-published; self-assessed or assessed by consultants | Renewal questions on ML1; ML2 said to unlock limits and price (vendor blogs [SS], low); no carrier credit table found | **CIS Controls v8.1 IG1** (56 safeguards) [BK]. E8 is narrower but deeper on application control, macros and hardening. CIS allowlisting (2.5) is IG2, not IG1 [BK] | Accept IG1 (optionally plus IG2 safeguard 2.5) as the "verified framework" in §3.1 |
| **CSA Cyber Essentials mark** (SG): certified by CSA-appointed bodies; 2-year validity; Cyber Trust mark above it; expanded to cloud, AI and OT [SS] | Government-run certification | Named insurers offer discounted rates [SS] | No US government mark. Nearest attestable options: **CIS IG1** assessment; **HITRUST e1** (foundational, 1-year assessment) [BK]; **SOC 2** (security criteria) for larger insureds; **CMMC Level 1** for defense-supply insureds [BK] | List as alternates in Item 7. **Do not** cite the FCC "U.S. Cyber Trust Mark" (an IoT product label) as an analogue [BK] |
| **CSA CISO-as-a-Service** (SG): up to 70% co-funding for SMEs to reach certification [SS] | Government subsidy | Leads into the discount | None federal. Some states run SMB cyber grant or assessment programs [BK, unverified for Colorado] | Mid-term earn-in (§3.1 item 4) plays the same "path to credit" role |
| **CERT-In 15 Elemental Cyber Defence Controls for MSMEs** (IN) [SS] | Government SME baseline | None found | **CISA Cyber Essentials** (guide) and **CISA Cross-Sector Cybersecurity Performance Goals** [BK] | Use as the plain-English "why these controls" reference in the application intro, not for credits (no attestation exists) |
| **METI/IPA お助け隊** (JP): certified bundle of monitoring, help desk, dispatch and simple insurance [SS] | Government certification of *service providers* | Insurance built in | **CISA Cyber Hygiene** free scanning [BK]; MSPs meeting a qualifying-MDR definition | §4.4 (distribution) and the Item 7 MDR credit |
| **FTC Safeguards Rule** (US, 16 CFR 314) | *Legal requirement* for GLBA "financial institutions", including tax preparers | n/a | This is the US baseline Cedar Ridge must already meet; IRS Publication 5708 gives a WISP template for tax professionals [BK] | For financial-institution insureds, a current WISP is a bind expectation, not a credit. Credit starts at IG1 attestation |
| **NIST CSF 2.0** (US; Small Business Quick-Start Guide; organizational profiles) [BK] | Voluntary framework | n/a | n/a | Define the target profile outcomes in Item 7 so "meets CSF 2.0" is testable |

**Proposed tier ladder (judgment, not market data).** Credits don't stack beyond the T2-16 cap.

| Tier | Test | What changes |
| --- | --- | --- |
| Standard | Bind expectations (MFA on email, remote and admin; backups; WISP if legally required) | Standard terms |
| Verified controls | Today's Item 7 rows | Retention credit, remote-access credit, no ransomware coinsurance, full Coverage H |
| **Verified framework (new)** | Independent IG1 / CSF 2.0 profile / HITRUST e1 attestation within 12 months | Premium credit; $2M/$3M and Coverage R without a supplement; short-form renewal |
| Monitored | Qualifying 24/7 MDR | Halved retention; 4-hour waiting period (as now) |

---

## 6. Jurisdiction-specific items: do not copy into a US admitted form

| Item | Jurisdiction | Why not | US analogue / what Harborline does instead |
| --- | --- | --- | --- |
| PDS + Target Market Determination; design and distribution obligations | Australia (Corporations Act Pt 7.8A; QBE AU says its PDS and TMD come "from your broker" [CAT]) [BK] | Statutory disclosure formats with no US equivalent | Filed form plus Declarations. A voluntary "who this policy is for" paragraph is fine |
| Insurance Contracts Act 1984 s.54 (insurer may not refuse a claim for a post-contract act; reduction only to the extent of prejudice); duty-of-disclosure regime | Australia [BK] | Statutory override that would reshape every condition | Harborline already reaches a similar result by design (IV.1 security lapses; V.3 honest mistakes). Under Colorado law, *Craft* limits notice-prejudice for claims-made deadlines (**Planned T1-6**) |
| Ransomware payment report to ASD within 72 hours (turnover ≥A$3M; 60 penalty units) | Australia, Cyber Security Act 2024 [SS] | Wrong agency, threshold and clock | FBI/IC3 or CISA report (III.3.5); NYDFS 500.17(c) for covered entities [BK]; CIRCIA once final. §3.5 covers the mechanism |
| Notifiable Data Breaches scheme (OAIC); statutory privacy tort (2024 amendments) | Australia [BK] | Different trigger ("eligible data breach") and regulator | State breach laws (Colorado C.R.S. 6-1-716: 30-day notice; AG notice at 500+ residents [BK]). Privacy tort claims fall under Coverage I |
| General Insurance Code of Practice timeframes; AFCA external dispute resolution | Australia [BK] | Industry code and ombudsman scheme | Colorado unfair-claims-practices statute and DOI complaints; Harborline V.7–V.8 already go further |
| Essential Eight / ML references in wording | Australia | Foreign government framework | §5 analogues, in the rating plan and Item 7, never as a coverage condition |
| Notifiable privacy breaches ("serious harm") | New Zealand, Privacy Act 2020 [BK] | Foreign regime | State breach laws; §3.9 covers foreign regulators generically |
| PDPA mandatory notification (PDPC); Cyber Essentials / Cyber Trust marks | Singapore [BK]/[SS] | Foreign regime and mark | §5 analogues. Don't import the "Cyber Trust" name |
| APPI reporting to the PPC; yen per-person 見舞金 amounts; お助け隊 certification | Japan [BK]/[SS] | Foreign regulator and amounts | US-dollar goodwill option (§4.1); CISA services (§5) |
| IRDAI UIN / "Use and File" filings; CERT-In 6-hour incident reporting; DPDP Act penalties (up to ₹250 crore); retail "sachet" micro-policies; group/master cyber policies | India [CAT]/[SS] | Foreign filing system, reporting clock and product formats | State form and rate filing; no general 6-hour US rule (closest: NYDFS 72h, CIRCIA 72h proposed, SEC 4 business days for public companies [BK]). Micro and group formats are outside the $1M–$50M segment |
| PDPA breach notice to the Commissioner within 72 hours (from June 1, 2025); fines up to RM1M; Cyber Security Act 2024 (NCII) | Malaysia [SS] | Foreign regime | State breach laws; §3.9 |
| Critical-infrastructure computer-systems ordinance (from Jan 2026); PDPO | Hong Kong [BK, verify] | Critical-infrastructure regime; not SMB | n/a |
| PIPEDA "real risk of significant harm" notices and 24-month breach records; Law 25 incident register, CAI notices, AMPs (C$10M / 2%) and penal fines (C$25M / 4%) | Canada / Québec [SS]/[BK] | Foreign statutes; penalty insurability is uncertain | §3.9 names the regulators generically; "where insurable" governs penalties |
| **Civil Code arts. 2500 and 2503:** defense costs *in addition to* limits, and liability proceeds reserved to injured third parties. A 2022 regulation lets certain contract categories and insured classes derogate | Québec [SS] | Harborline is defense-within-limits by design (notice 3). Copying Québec wording would silently double the liability limits | Keep defense within limits; confirm Colorado permits eroding limits for cyber [BK, verify]. **Note for the Corgi story:** Coalition's Active Cyber Policy is *not* offered in Québec, and its EBR endorsements exclude Québec [SS]/[PKG 02]. Québec-specific paper is the norm |
| French-first contracts of adhesion (Charter of the French Language, as amended by Bill 96) | Québec [BK] | Language law | None required. An optional Spanish-language summary is a separate US decision |
| Provincial regulators (FSRA, AMF) and fair-treatment guidance | Canada [BK] | Foreign supervisory regime | Colorado DOI |

---

## 7. Interaction map: new ideas vs planned fixes

| New item | Depends on or must align with | Risk if not aligned |
| --- | --- | --- |
| §3.1 Framework tier | T2-16 (stacking), W-21 (credit loss mid-term), T2-7 (scan estoppel), review #11, rating-plan filing | Credits stack past intent; scan contradicts attestation |
| §3.2 Early warning | T2-1f/W-09 (suspected trigger), W-25 (precautionary shutdown), T2-8 (service caps; pre-incident overlap), T2-10 (discover), V.6.2 | Two different "suspicion" tests in one form |
| §3.3 Yearly retention cap | III.1.3, III.1.4, T2-1c (incident-to-claim linkage), V.6.1, band table 4.3, T2-10 | Unclear which period a cross-period retention counts in |
| §3.4 Panel waiver | III.1.3, T2-12, T2-10; Item 6 B row | "One retention per incident" read as satisfied by waived fees |
| §3.5 Reporting support | III.3.4–3.5, T2-19, T1-10 (CIRCIA), V.1.5 | Insured misses a legal clock when the insurer pays |
| §3.6 Services schedule | III.1.7 (KEV notice), V.6.1 ("critical issue"), T2-7, T2-8, Colorado anti-rebating check | Monitoring results widen the estoppel; inducement objection at filing |
| §3.7 IT provider | W-34 (executive excludes MSP), T2-0, T2-3, T2-4, T2-1d; accumulation note (review Tier 6) | MSP knowledge imputed; MSP-tool attacks routed to E |
| §3.8 Examples | Cover page "How to read" item 3; V.11.6; review 4.1 cross-reference fix | Promise without content; examples read as grants |
| §3.9 Foreign regulators | T1-8 (one insurability rule), exclusion 17, V.11.1 | Overpromising on penal fines |

---

## 8. Sources

All [SS] unless marked otherwise. Dates are as shown in the URL or snippet; "n.d." means none was visible. None were opened.

**Australia / New Zealand**
- Emergence CEP-005.1 key changes (Feb 2026): https://emergenceinsurance.com/wp-content/uploads/sites/6/2026/02/Emergence_Cyber-Event-Protection_Summary-of-Key-Changes_CEP005-to-CEP005.1_02.26.pdf
- Emergence CEP-005.1 upgrade page (Feb 2026): https://emergenceinsurance.com/emergence-strengthens-cyber-event-protection-with-cep-005-1-upgrade/
- Emergence CEP-005.1 wording (02.26) [CAT]: https://emergenceinsurance.com/wp-content/uploads/sites/6/2024/02/Emergence_Cyber-Event-Protection_CEP-005.1_Important-Information-Policy-Wording_02.26.pdf ; NZ version [CAT]: https://emergenceinsurance.com/wp-content/uploads/sites/6/2024/02/Emergence-NZ_Cyber-Event-Protection_CEP-005.1_General-Information-Policy-Wording_02.26.pdf
- CEP-005 (2024) broker copy: https://www.centrewest.com.au/wp-content/uploads/2024/02/Emergence-Cyber-Event-Protection-CEP-005.pdf
- Insurance Business AU, "Emergence updates cyber policy wording for Australian SMEs" (Feb 2026): https://www.insurancebusinessmag.com/au/news/cyber/emergence-updates-cyber-policy-wording-for-australian-smes-565467.aspx
- Insurance Business AU, "Emergence Insurance revamps cyber policy" (n.d.; likely the CEP-005 launch; source of the "no excess under A$25M" snippet, **unconfirmed**): https://www.insurancebusinessmag.com/au/news/cyber/emergence-insurance-revamps-cyber-policy-478685.aspx
- CFC Cyber Proactive Response launch (Apr 2025): https://www.cfc.com/en-us/knowledge/news/2025/04/cfc-reinvents-cyber-insurance-with-launch-of-new-product/ ; Insurance Journal (Apr 2, 2025): https://www.insurancejournal.com/news/national/2025/04/02/818156.htm ; Insurance Edge (Apr 3, 2025): https://insurance-edge.net/2025/04/03/cfc-claims-two-world-firsts-lets-get-into-it/
- CFC nil deductible and separate IR limit (Aug 2024): https://www.cfc.com/en-us/knowledge/resources/articles/2024/08/cyber-coverage-highlights-nil-deductible-and-separate-limit-for-incident-response/ ; CFC interactive wording (Apr 2025): https://www.cfc.com/en-us/knowledge/resources/articles/2025/04/interactive-cyber-policy-wording/
- CFC Cyber Proactive Response AU wording (2025) [CAT]: https://psychology.org.au/getmedia/115ccab2-75db-462d-af0d-1a6fdf7d7b78/cyber-proactive-response-policy-wording-2025.pdf
- Chubb Cyber ERM 2.2 SME Marketplace (Chubb10-571-0722) [CAT]: https://www.chubb.com/content/dam/chubb-sites/chubb-com/au-en/business/cyber-insurance/documents/pdf/cyber-erm-version-2-2-policy-sme-marketplace-platform-au.pdf ; Chubb AU cyber services (48-hour emergency IR; 1-hour contact): https://www.chubb.com/au-en/business/cyber-services-overview.html ; E13 Widespread Event endorsement [CAT]: https://www.chubb.com/content/dam/chubb-sites/chubb-com/au-en/business/cyber-insurance/documents/pdf/erm-v2-2-e13-widespread-event-endorsement.pdf
- Delta Insurance AU Cyber Liability (Delta_AU_CYB_0824; fact sheet 10/2024) [CAT]; product page: https://deltainsurance.com.au/products/cyber-liability-insurance
- QBE NZ QCyberProtect CYB0625 (06/2025) [CAT]: https://www.qbe.com/media/qbe/apac/new-zealand/document-listing/2025/08/13/22/38/cyb0625-nz-qcyberprotect.pdf ; coverage sheet 2025: https://www.qbe.com/media/qbe/apac/new-zealand/files/qbe-nz-qcyberprotect-coverage-sheet-2025.pdf ; QCyberPrepare: https://www.qbe.com/newsroom/news/how-qbes-global-cyber-proposition-is-constantly-evolving-to-support-brokers-and-customers
- Zurich AU / Cowbell Prime One: https://www.insurancebusinessmag.com/au/news/cyber/zurich-rolls-out-standalone-cyber-policy-for-australian-smes-564522.aspx
- Australian ransomware payment reporting: https://www.minterellison.com/articles/mandatory-ransomware-payment-reporting-obligations-in-force ; https://www.twobirds.com/en/insights/2024/australia/australias-first-standalone-cyber-security-law-the-cyber-security-act-2024 ; https://www.coalitioninc.com/blog/cyber-insurance/australia-ransomware-reporting-laws
- Essential Eight and insurance (vendor sources, low weight): https://4it.com.au/cybersecurity/cyber-insurance-australian-sme-2026/ ; https://www.cyberpulse.com.au/2026/02/25/cyber-insurance-in-australia/ ; https://protectera.com.au/au-cyber-insurance-market-2026-what-smes-need-to-know-now/

**Asia**
- CSA Cyber Essentials: https://www.csa.gov.sg/our-programmes/support-for-enterprises/sg-cyber-safe-programme/cybersecurity-certification-for-organisations/cyber-essentials/certification-for-the-cyber-essentials-mark/ ; mark expansion: https://www.csa.gov.sg/news-events/press-releases/csa-s-cyber-essentials-and-cyber-trust-marks-expanded-to-include-cloud-security--artificial-intelligence-and-operational-technology/ ; insurer-discount list (snippet; exact page among the results not attributable): https://securitypulse.ai/resources/cyber-essentials-certification-singapore/ , https://arkshield.sg/cyber-essentials-mark-singapore-guide/
- Tokio Marine & Nichido サイバーリスク保険: https://www.tokiomarine-nichido.co.jp/hojin/baiseki/cyber/hosho02.html ; 2025 pamphlet: https://www.chuokai.or.jp/archive/insu/pdf/privacy/tokiomarine-nichido_pamphlet_2025.pdf ; services: https://www.tokiomarine-nichido.co.jp/hojin/baiseki/cyber/service.html
- MS&AD Cyber Protector: https://www.ms-ins.com/business/indemnity/pd-protector/ ; Sompo Japan: https://sompo-japan-cyber.jp/coverage/
- METI お助け隊: https://www.meti.go.jp/policy/netsecurity/otasuketai.html ; IPA: https://www.ipa.go.jp/security/otasuketai-pr/
- India: IRDAI guidelines update (Apr 2026): https://www.medianama.com/2026/04/223-lowdown-insurers-comply-dpdp-irdai-updates-cyber-security-guidelines/ ; Chambers 2026 India guide: https://practiceguides.chambers.com/practice-guides/cybersecurity-2026/india/ ; Go Digit commercial cyber (UIN IRDAN158CP0011V01202122) [CAT]
- Malaysia: https://privacymatters.dlapiper.com/2025/03/malaysia-guidelines-issued-on-data-breach-notification-and-data-protection-officer-appointment/ ; https://resourcehub.bakermckenzie.com/en/resources/global-data-and-cyber-handbook/asia-pacific/malaysia/topics/security-requirements-and-breach-notification

**Canada**
- Coalition ACP Canada (announced Mar 10, 2026): https://www.coalitioninc.com/en-ca/announcements/coalition-brings-active-cyber-policy-to-canada ; https://insurance-canada.ca/2026/03/11/coalition-launch-active-cyber-policy/ ; Insurance Journal (Mar 13, 2026): https://www.insurancejournal.com/news/international/2026/03/13/861837.htm ; Coalition Québec excess (Oct 2025): https://www.insurancejournal.com/news/international/2025/10/24/845042.htm
- Chubb Canada Cyber Stack (11/05/2025) [CAT]: https://www.chubb.com/content/dam/chubb-sites/chubb-com/ca-en/business-insurance/cyber-enterprise-risk-management-cyber-erm/documents/pdf/chubb_chubbcyberstack_stackingupyourdigitaldefense_sheet_110525-ca-en.pdf
- Travelers Canada CyberRisk highlight sheet (Jan 17, 2023) [CAT]: https://www.travelerscanada.ca/iw-documents/canada/CyberRisk-Coverage-Highlight-Sheet_230117.pdf
- Northbridge / CyberScout: https://cyberscout.com/en/press-releases/cyberscout-partners-with-northbridge-to-offer-commercial-policyholders-two-privacy ; https://www.northbridgeinsurance.ca/specialty-solutions/cyber-risk-insurance/
- Québec art. 2503 and the 2022 regulation: https://www.mccarthy.ca/en/insights/publications/quebec-modulates-duty-defend-certain-categories-insurance-and-insureds ; https://www.torys.com/our-latest-thinking/publications/2022/06/un-nouveau-reglement-assouplit-lobligation-de-defendre-des-assureurs-au-quebec
- Law 25 penalties: https://gowlingwlg.com/en/insights-resources/articles/2022/law-25-the-cost-of-a-privacy-breach-just-went-up ; https://www.mccarthy.ca/en/insights/publications/navigating-the-legislative-landscape-on-data-breaches-2026-data-breach-insights-part-3

---

## 9. Verify before quoting

1. **Emergence's "no excess under A$25M turnover":** which edition (CEP-005 or 005.1), and whether it applies to all sections or only event response.
2. **CFC CPR:** the exact structure of the nil deductible, unlimited reinstatements and "one deductible per term" option, and whether the AU 2025 wording carries the same options as the US launch.
3. **Chubb ERM 2.2:** whether the retention is waived on the 48-hour emergency IR expenses.
4. **Singapore insurer discounts:** which insurers, what percentage, and whether they are still current in 2026.
5. **MS&AD's ¥50,000 / ¥1,000** 見舞金 limits (open the Cyber Protector page).
6. **Colorado anti-rebating treatment** of free loss-mitigation services (§3.6), and whether Colorado has adopted the NAIC 2020 model amendments.
7. **Whether Colorado restricts defense-within-limits** for any line relevant to cyber.
8. **CISA Pre-Ransomware Notification volumes** before citing a number.
9. **HITRUST e1 and CMMC Level 1 details** before listing them in Item 7.
