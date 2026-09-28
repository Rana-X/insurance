# 03. Underwriting, application benchmarking, credit design and pricing: Harborline / Cedar Ridge

Reviewer stance: senior SMB cyber underwriter. Review date: 2026-09-27.
Scope: `application.txt` (all), `policy.md` Items 3–7, Section III parts 1 and 6, Section IV part 1, Section V parts 3–6, and `rationale.md` ("Summary", "Sample application design", "2026 evidence check", "Market benchmark"). This builds on `round1_findings.md` and doesn't repeat those points unless something new turned up.

## Evidence labels used throughout

| Label | Meaning |
| --- | --- |
| **[E-snip]** | Market evidence seen only as a web-search result snippet or summary. The primary document couldn't be opened (see below). Treat it as indicative and re-check it before quoting in the submission. |
| **[E-pkg]** | A figure from the package's own cited sources (for example the At-Bay 2026 InsurSec Report). I didn't re-verify it here. |
| **[K]** | Well-established public fact I know but didn't re-verify in this round (dates of CISA BOD 22-01, Windows 10 end of support). |
| **[J]** | My professional underwriting judgment. It is not market evidence. |

**Research limits.** I used all 22 of the 22 permitted WebSearch calls. WebFetch and curl were blocked (EGRESS_BLOCKED or proxy 403) on every host I tried: tmhcc.com, beazley.com, chubb.com, travelers.com, asset.trvstatic.com, siegelagency.com, help.coalitioninc.com, static.fmgsuite.com, phly.com, pdffiller.com, westchester.com, herodevs.com and lmalloyds.com. As a result, I couldn't read any real application form in full. The benchmarking in Part 2 rests on search snippets of specific questions, plus judgment about what is standard. Where I couldn't confirm that a carrier asks a question, the tables say "not confirmed". They don't guess.

---

## 0. Bottom line

1. **The market has moved from rewarding controls to requiring them.** For a $5–10M professional-services firm holding SSNs, the following are close to universal preconditions to bind in 2025–26, not sources of discount: MFA on email, remote access and privileged access, EDR, segregated or immutable backups, and no exposed RDP or end-of-life VPN [E-snip; J]. Harborline presents three of these as *credits*: the 25% retention credit for MFA+EDR, the 10% premium credit for hardened remote access, and the absence of backup coinsurance. That is generous framing. It also makes the "standard" terms a fiction, because almost every insurable applicant in this band will earn them [J].
2. **The strongest designs are aligned with the market.** These are the MDR credit and 4-hour waiting period, the claim-free reduction, the callback-linked fraud limit and ransomware coinsurance for unverified backups. The weakest are the pre-issue scan estoppel ("should have shown") and the KEV coinsurance clause. The KEV clause is far narrower than Chubb's Neglected Software Exploit model, and it **conflicts with the estoppel** for any vulnerability the pre-issue scan saw.
3. **The application misses the three questions that most matter for this risk.** First, end-of-life and unsupported systems: the pre-issue scan itself found a legacy print server, and Windows 10 lost support on 2025-10-14 [K]. Second, how the managed IT provider (MSP) and other vendors get remote access, and which remote-management tools they use. Third, backup credential segregation and MFA on the backup console. For a CPA firm it also misses per-type record counts, the records processed for payroll clients, and money-movement volumes.
4. **$5,508 is plausible [J].** It sits at or above the generic SMB "$1M limit" ranges seen in 2026 [E-snip], which is right for a CPA class with about 31K SSNs, client payroll and a broader-than-market core. It is not supported by the two benchmarks the rationale cites. The Vouch "$7,078 median for $5–10M revenue" figure still can't be found: Vouch publishes an **overall median of $2,755 across 2,034 clients** and **$2,082 for firms under $1M revenue** [E-snip]. The "$2,330–$4,048" figures come from two issued policies for what appear to be small nonprofits, and I couldn't verify them.
5. **Rates are soft.** Marsh puts U.S. cyber at −2% in Q2 2026 [E-snip]. CIAB reports cyber at −3.2% in Q2 2026, the ninth straight quarterly decrease [E-snip]. Gallagher calls 2026 U.S. pricing "essentially flat" [E-snip].
6. **The retention band table is missing, but easy to supply.** A defensible rule is a standard retention of about 0.1–0.15% of revenue, rounded to five steps from $2,500 to $25,000, with the claim-free floor set per band rather than a flat $2,500 (Part 5) [J].

---

## 1. SMB cyber underwriting practice, 2025–2026

### 1.1 Minimum control expectations for an $8.5M professional-services risk

| Control | What the market asks or requires (evidence) | 2025–26 status for a $5–10M PII-heavy risk [J] | Harborline treatment |
| --- | --- | --- | --- |
| **MFA: email** | Travelers' MFA attestation (form CYB-14306, the form at issue in *Travelers v. ICS*) asks for MFA on "all employees accessing email through a website or cloud service" [E-snip] | Precondition to bind | App 4.6 (credit ★) |
| **MFA: remote access** | Travelers: MFA for **all** remote access by employees, **contractors and third-party providers** [E-snip]. Coalition asks about MFA on VPN, RDP, RDWeb, RD Gateway and other remote access [E-snip]. Beazley asks about MFA for remote access to the network, cloud or on-premises, including VPN [E-snip] | Precondition. Exposed RDP or an end-of-life VPN usually means decline or pre-bind remediation | App 4.6 and 4.8. **Vendor/contractor access isn't asked.** Earns a 10% premium credit |
| **MFA: privileged/admin** | Travelers: internal **and** remote admin access to directory services, **network backup environments**, network infrastructure, endpoints and servers [E-snip]. Chubb ERM forms: separate MFA for privileged access, including internal access [E-snip]. Coalition: network, cloud-admin and privileged accounts [E-snip] | Precondition. MFA on the backup console is increasingly asked on its own | App 4.6 "Cloud and admin accounts". **No backup-console or internal privileged-access scope** |
| **EDR** | Marsh: EDR, MFA and PAM are the three controls insurers recommend most often [E-snip]. Chubb forms ask EDR % coverage [E-snip]. A secondary summary of Travelers says it asks for the EDR vendor and workstation/server coverage [E-snip, secondary] | Precondition at this size in most markets | App 4.13, a yes/no with 100% (credit ★) |
| **24/7 MDR** | Sold with the policy at At-Bay (InsurSec packages, Oct 2025) and Coalition (MDR premium credit up to 12.5%) [E-snip] | A pricing or terms lever, not a requirement, at $8.5M | App 4.14. Halves the retention and cuts the wait to 4h |
| **Backups** | Coalition: at least weekly backups of critical data and systems kept **offline or on a separate network** [E-snip]. Chubb: offline or air-gapped, **immutable/WORM**, and access through **separate privileged accounts not joined to Active Directory** [E-snip]. Beazley asks whether a cloud backup is really a "syncing service" such as OneDrive or Dropbox [E-snip] | Precondition. Carriers increasingly ask about credential segregation, not just "offline" | App 4.18–4.19. **No question on credential segregation, MFA on backups or backup encryption** |
| **EOL software/hardware** | Chubb's Neglected Software Exploit (NSE) endorsement treats end-of-life/end-of-support software and unpatched CVEs as risk-shared losses [E-snip]. A secondary summary says Travelers asks about EOL systems and whether they're segregated or internet-exposed [E-snip, secondary]. Carriers are adding EOL exclusions or time-escalating coinsurance [E-snip] | Asked almost everywhere. Internet-facing EOL is often a decline | **Not asked.** The pre-issue scan found a "legacy print server" |
| **Patch cadence** | Beazley asks whether critical patches are actively managed [E-snip]. Marsh lists patched systems as a top-5 control [E-snip]. CISA BOD 22-01 sets federal KEV deadlines of 2 weeks for newer CVEs and 6 months for older ones [K] | Critical/KEV patches within 14–30 days; internet-facing faster | App 4.10 (72h / 14 days) |
| **PAM** | Chubb: are privileged accounts controlled by a PAM solution [E-snip]. Marsh ranks PAM in the top 5 and among the three most recommended [E-snip] | Asked. Full PAM is rarely required below $10M, but separate admin accounts and no local admin are expected | App 4.9 (separate admin accounts). No PAM tool or service-account question |
| **Hardening** | Marsh: "hardening techniques" had the strongest link to lower incident likelihood, about 6x [E-snip] | Increasingly asked (macros, PowerShell, LAPS) | **Not asked** |
| **Logging/monitoring** | Marsh top-5 control [E-snip] | Asked in longer forms | App 4.15 |
| **Email security/DMARC** | Beazley asks which controls protect inbound email [E-snip]. I found no DMARC-specific evidence this round | SPF/DKIM/DMARC and filtering expected [J] | App 4.11 (strong answer) |
| **Training/phishing** | No carrier-specific evidence this round | Expected annually, with phishing simulation [J] | App 4.12 |
| **Funds-transfer verification** | Coalition asks whether a secondary channel validates funds-transfer requests **over $25,000** [E-snip]. Social-engineering grants often carry callback or dual-authorization conditions [E-snip] | Expected for any firm that moves money. Often a condition of the social-engineering sublimit | App 5.2–5.3 ($5,000 threshold) |

**Evidence strength.** Much 2026 commentary says controls "have transitioned from pricing credits to binary insurability gates" [E-snip, low-quality secondary]. That matches my experience [J], but I would cite the carrier questions above instead.

### 1.2 Outside-in scanning, continuous monitoring and mid-term alerts
- Coalition and At-Bay build active scanning into pricing and monitor continuously [E-snip]. At-Bay alerts the insured **and the broker** when it detects new critical vulnerabilities. Its own analysis says a critical vulnerability found mid-policy significantly increases the chance of a claim [E-snip]. Coalition runs continuous attack-surface monitoring and alerts [E-snip]. Its vanishing retention is conditional on resolving the critical vulnerabilities that Coalition Control flags [E-snip].
- Typical practice [J]: scan findings become **pre-bind subjectivities**. For example, "close exposed RDP / patch this KEV before binding". Mid-term alerts come with a remediation expectation. I found **no** carrier that estops itself from relying on its own scan the way Harborline Section V part 3.4 does, and the package's own rationale says so ("Competitors don't bind themselves to scans").

### 1.3 Attestation, warranty and rescission practice
- **Travelers v. ICS** (C.D. Ill. No. 22-cv-2145, August 2022) is still *the* reference case. A signed MFA attestation was wrong: MFA protected only the firewall. The parties stipulated that the policy was void from inception [E-pkg; E-snip]. My search didn't surface a newer published cyber rescission decision from 2025–26. Commentary says carriers responded by moving to **evidence-based underwriting**, meaning dated exports of conditional-access and MFA reports, EDR coverage, restore-test logs and patch SLAs [E-snip].
- In many U.S. states an *innocent* material misrepresentation can still support rescission [E-snip, secondary]. The rule varies by state, and counsel needs to confirm it [J]. Harborline's proportionate remedy (re-rate to the terms we would have offered) and its limit of rescission to knowing, intentional misstatements are **well above market for the insured**. They follow the UK Insurance Act 2015 model, and state filing review is needed.

### 1.4 Coinsurance, sublimits and endorsements for missing controls
- **Chubb Neglected Software Exploit (NSE)** endorsement (introduced 2021, attached to Cyber ERM) [E-snip]:
  - It gives full coverage for 45 days, then "gradually re-weights risk sharing between the Insured and Insurer as time passes".
  - The 0–45 day band carries 0% coinsurance and 100% of the limit.
  - Later day bands carry schedule-negotiated coinsurance, excess and sublimits.
  - The trigger covers **both** a CVE with an available patch left unapplied **and** software that has reached end of life or end of support.
  - I could **not** verify the exact percentages for the later bands. Don't quote any in the submission.
  - Chubb also uses a Widespread Event endorsement with its own limits, retention and coinsurance (catalog note, non-U.S. specimen).
- **Ransomware.** Agency guidance describes ransomware coinsurance splits such as 75/25 and ransomware sublimits (for example $250K inside a $1M aggregate) as common for weaker risks [E-snip]. The package's own source shows Vouch at a $62,500 ransomware sublimit [E-pkg].
- **Social engineering.** Sublimits are common. Coverage grants often carry callback-to-known-number and dual-authorization conditions [E-snip]. For comparison, Amwins' new SME Cyber+ product advertises $500K social-engineering and invoice-manipulation limits [E-snip].

### 1.5 Rating factors
- The exposure base is almost always **revenue**, multiplied by industry and other factors. That comes from an analysis of filed rate plans: Romanosky et al., *Journal of Cybersecurity*, 2019, "Content analysis of cyber insurance policies: how do carriers price cyber risk?" [E-snip]. **Record counts** and employee counts appear as secondary exposure bases or modifiers [E-snip].
- A **security modifier** comes from the questionnaire and, at Coalition and At-Bay, from the scan [E-snip].
- Standard factors [J]: industry hazard class (accounting and financial services rate above average because of regulated data and BEC), prior incidents and claims, limits and retention, coverage breadth (system-failure BI, bricking, social engineering), and state or regulatory footprint.

### 1.6 Retentions by revenue band
Public evidence is thin and mostly from secondary sources:
- "Small businesses" most often carry $1,000–$2,500, and "larger SMBs" $5,000–$25,000 [E-snip, secondary: Insureon, seedpodcyber].
- The package's own issued-policy benchmarks show **$2,500** on At-Bay's and Coalition's small-insured policies, and **$10,000** at Vouch and Corgi (startup-oriented) [E-pkg].
- My proposal is in Part 5.

### 1.7 MDR-linked packages
- **At-Bay InsurSec packages** (press release, 2025-10-02) [E-snip]:
  - retention as low as **$0** on ransomware and financial fraud
  - up to **$1M** financial-fraud coverage
  - ransomware cover "activates right away", without the usual waiting period
  - the same premium year over year even after a ransomware claim
  - all of this requires At-Bay's own MDR
- **Coalition**: up to a **12.5% premium credit** for Coalition MDR customers (U.S. and Canada) [E-snip]. The package's source also reports a reduced MDR waiting period (April 2026) [E-pkg].

---

## 2. Application benchmarking

### 2.1 Comparators and evidence quality

| Carrier | Document used | Evidence |
| --- | --- | --- |
| Coalition | Application question set as published by a third party (cybcovsol.com "Questions for Coalition Cyber Insurance"), plus Coalition's help article on quote data | [E-snip] |
| Travelers | CyberRisk MFA Attestation CYB-14306 (catalog edition 2023-03), as described in *Travelers v. ICS* commentary, plus a secondary summary of the Travelers application | [E-snip]; the secondary summary is weaker |
| Chubb | Cyber ERM proposal and ransomware supplementary forms (UK, SG, MY, IE editions; **non-U.S.**). One snippet says Chubb's live U.S. small-business application is far shorter | [E-snip] |
| Beazley | U.S. forms F00863 (04/2023, under $250M) and F00657 (04/2023, over $250M), plus the UK sub-£20M questionnaire, via snippets and a broker blog | [E-snip] |
| Tokio Marine HCC | NetGuard Plus NGP-NBA 9.2024 (cataloged as current) | **Blocked, not read.** Not used in the table |

Legend: **✔** = confirmed in a search snippet this round; **●** = standard on essentially all cyber applications [J, not re-verified per form]; **?** = not confirmed this round (the carrier may well ask it); **—** = generally not asked [J].

### 2.2 Question-by-question comparison

| Harborline Q | Topic | Coalition | Travelers | Chubb | Beazley | Assessment |
| --- | --- | --- | --- | --- | --- | --- |
| 1.1–1.4, 1.6, 1.14 | Identity, address, entity, contact | ● | ● | ● | ● | Standard |
| 1.5 | Website and email domains | ● (needed for scan) [J] | ● | ● | ● | Standard. Fine |
| 1.7–1.8 | Industry, NAICS, operations | ● | ● | ● | ● | Standard. The 1.8 answer shows **outsourced payroll for clients**, a material exposure that 1.13 and 5.4 don't follow up properly |
| 1.9 | Revenue (last FY, next 12 months) | ● | ● | ● | ● | Standard exposure base [E-snip: Romanosky 2019]. Ask for **monthly revenue seasonality** too (tax season) to price BI [J] |
| 1.10 | Customer above 10% of revenue | ? | ? | ? | ? | **Unusual** for cyber. Acceptable only because it drives optional Coverage S. Ask it only when S is requested |
| 1.11 | Employees | ● | ● | ● | ● | Standard |
| 1.12 | Subsidiaries | ● | ● | ● | ● | Standard |
| 1.13 | Prohibited or high-hazard classes | ● [J] | ● [J] | ● [J] | ● [J] | Standard idea, but **"payment processing" is undefined**. Cedar Ridge answered "No" while running payroll for 40 clients (5.4). That is a misrepresentation trap (§2.5) |
| 1.15 | Security contact for alerts | ✔ (alerts) | ? | ? | ? | Good. Matches Coalition and At-Bay alerting practice |
| 2.1–2.4 | Dates, limit, retention, options | ● | ● | ● | ● | Standard. 2.3 cites a "revenue band" that no document defines (Part 5) |
| 2.5 | Current cyber insurance | ● | ● | ● | ● | Standard. Add carrier, limit, **retro date** and continuity date (needed for the "full prior acts" in 2.8) |
| 2.6 | Why buying standalone | — | — | — | — | Unusual but harmless. Useful because it surfaces **contractual requirements** (two clients require $1M) |
| 2.7 | Declined, cancelled or non-renewed | ● | ● | ● | ● | Standard |
| 2.8 | Retroactive date | ● | ● | ● | ● | Standard |
| 3.1 | PII types | ✔ (PII/PHI) | ? | ? | ✔ | Good list |
| 3.2 | Number of individuals | ✔ (record count) | ? | ? | ✔ (**per type**) | **Gap.** One total only. Ask counts **per type** (SSN, financial account, health), records **processed for clients** (payroll employees) and the peak count in tax season |
| 3.3 | States of residence | ? | ? | ? | ? | Useful and uncommon. Keep it |
| 3.4 | Paper records | ? | ? | ? | ? | Keep, because the policy covers paper |
| 3.5 | Encryption: laptops, email, cloud | ? | ? | ? | ? | **Triple-barrelled.** The "Yes" covers three things at once, and 5.7 says some PDFs go by ordinary email. Split it into separate questions (§2.5). Also ask about **servers and backups** |
| 3.6 | Retention/deletion schedule | ? | ? | ? | ? | Fine |
| 3.7 | Privacy policy | ● [J] | ● [J] | ● [J] | ● [J] | Standard |
| 3.8 | Website tracking tools | ? | ? | ? | ? | Emerging (pixel/CIPA supplements) [J]. Good |
| 3.9 | Sell/share for advertising | ? | ? | ? | ? | Fine |
| 3.10 | Payment cards | ● [J] | ● [J] (catalog suggests a PCI supplement, unverified) | ● [J] | ● [J] | Standard |
| 4.1–4.2 | Security owner, written program | ? | ? | ? | ? | Fine. The FTC Safeguards Rule makes 4.2 verifiable |
| 4.3 | Outside IT provider | ? | ? | ? | ? | **Gap.** No follow-up on **how the MSP connects** (RMM tool, MFA on the MSP's accounts, least privilege) |
| 4.4 | Asset inventory | ? | ? | ? | ? | **Gap.** Follow with "any end-of-life OS, software or devices, and are they internet-facing or segmented?" |
| 4.5 | Risk assessment | ? | ? | ? | ? | Fine |
| 4.6 ★ | MFA scopes | ✔ (VPN, RDP, RDWeb, RD Gateway, admin/privileged) | ✔ (email, **all** remote incl. third parties, admin to directory, **backups**, network, endpoints) | ✔ (separate MFA for privileged, incl. internal) | ✔ (remote incl. VPN) | Harborline scope is **narrower than Travelers'**. Add **backup console**, **internal privileged/domain admin** and **vendor/contractor remote access**. The "(hardware security keys)" wording adds an absolute factual claim (§2.5) |
| 4.7 | Accounts without MFA | ? | ? | ? | ? | **Best-practice innovation.** An exceptions register invites honest disclosure |
| 4.8 ★ | Remote-access method | ✔ (RDP/VPN) | ✔ (remote access) | ? | ✔ | **Gap.** Doesn't ask about **remote-support tools** (ScreenConnect, AnyDesk, TeamViewer, RMM) or **vendor access** |
| 4.9 | Separate admin accounts | ? | ✔ (PAM, secondary) | ✔ (PAM) | ? | Good basics. Add number of domain admins, **service accounts with privileges** and whether a PAM or LAPS tool is used |
| 4.10 | Patch timing | ? | ? | ? | ✔ | Good. Framed as an absolute SLA (§2.5) |
| 4.11 | Email protections | ? | ? | ? | ✔ | Strong |
| 4.12 | Training | ● [J] | ● [J] | ● [J] | ● [J] | Standard |
| 4.13 ★ | EDR on all laptops and servers | ✔ (EDR "essential") | ✔ (vendor, coverage, secondary) | ✔ (% coverage) | ✔ (endpoint protection) | Ask for the **EDR product** and **% coverage by device type**, including phones and the seasonal machines. There's no evidence attached, unlike 4.7 |
| 4.14 ★ | 24/7 MDR | ? | ? | ? | ? | Good. Needs a definition of qualifying MDR (Part 3) |
| 4.15 | Log retention | ? | ? | ? | ? | Fine (a Marsh top-5 control) |
| 4.16–4.17 | IR plan and test | ✔ (tested IR plan) | ? | ? | ? | Good. Add "IR retainer or breach counsel on retainer?" (optional, since Harborline has a panel) |
| 4.18 ★ | Backup method | ✔ (weekly, offline or separate network) | ? | ✔ (air-gap, WORM, **separate non-AD credentials**) | ✔ ("syncing service?") | **Gap.** Ask about **credential segregation**, **MFA on backup console**, **backup encryption** and whether M365 is backed up by a third-party tool |
| 4.19 ★ | Last full restore test | ? | ? | ? | ? | Good. The answer tested the file server only, not M365 (see Part 3, row 4) |
| 4.20 | Downtime tolerance | ? | ? | ? | ? | Good for BI pricing |
| 5.1 | Who can send wires; dual approval | ? | ? (possible SE supplement, unverified) | ? | ? | **Gap.** Ask **annual wire/ACH volume**, **largest single transfer** and number of payees changed per year |
| 5.2 ★ | Callback on bank-detail changes | ✔ (secondary validation) | ? | ? | ? | Good |
| 5.3 ★ | Callback for transfers over $5,000 | ✔ (threshold **$25,000**) | ? | ? | ? | Harborline's threshold is **stricter** than Coalition's (Part 3) |
| 5.4 | Moves money for clients | ? | ? | ? | ? | **Gap.** Ask **annual client payroll dollars**, whether funds pass through Cedar Ridge accounts, whether the firm can initiate debits from client accounts, and client-held trust or escrow funds |
| 5.5 | Positive pay | ? | ? | ? | ? | Good |
| 5.6 | BEC/deepfake training, code word | ? | ? | ? | ? | Good, and ahead of the market |
| 5.7 | How invoices are sent | ? | ? | ? | ? | Unusual. Justified by the invoice-manipulation coverage |
| 6.1–6.3 | Critical vendors, terms, vendor review | ? | ? | ? | ? | Fine. Vendor concentration is now scored [E-snip, secondary] |
| 6.4–6.6 | AI use, rules, autonomous agents | ? | ? | ? | ? | Emerging. The wording of 6.6 is risky (§2.5) |
| 6.7 | Software development | ● [J] | ● [J] | ● [J] | ● [J] | Standard screen for tech E&O |
| 7.1–7.3, 7.5–7.6 | Regulatory status (legal conclusions) | — | — | — | — | Asked as **legal conclusions**, which is unusual (§2.4 and §2.5). Ask for facts instead |
| 7.4 | PCI DSS | ● [J] | ● [J] | ● [J] | ● [J] | Standard |
| 7.7 | Biometrics | ? | ? | ? | ? | Common since the BIPA cases [J]. Fine |
| 8.1 | Incidents or claims, last 3 years | ● | ● | ● | ● | Standard. Terms undefined (§2.5) |
| 8.2 | Stopped attacks (optional) | — | — | — | — | Novel and good, but say whether optional text is part of the "application" (§2.5) |
| 8.3 | Regulator inquiries | ● [J] | ● [J] | ● [J] | ● [J] | Standard |
| 8.4 | Known circumstances | ● | ● | ● | ● | Standard |
| Part 9 | Two signatures, reasonable-inquiry statement | ? | ✔ (signed MFA attestation) | ? | ? | The reasonable-inquiry knowledge qualifier is good. Note that the IT manager is an "executive" under the policy (§2.5) |
| **Missing** | **EOL/unsupported systems** | ? (unsupported software affects eligibility [E-snip]) | ✔ (secondary) | ✔ (NSE policy term) | ? | **Add (priority 1)** |
| **Missing** | **Remote-support/RMM tools; vendor and MSP remote access** | ? | ✔ (MFA for third-party remote access) | ? | ? | **Add (priority 1)** |
| **Missing** | **Backup credential segregation, MFA on backups, backup encryption** | ? | ✔ (MFA on backup environments) | ✔ | ? | **Add (priority 1)** |
| **Missing** | **Hardening** (macros, PowerShell, LAPS, CIS benchmarks) | ? | ? | ? | ? | Add (Marsh's top control) |
| **Missing** | **Records by type, and records processed for clients** | ✔ | ? | ? | ✔ | **Add (priority 1 for a CPA firm)** |
| **Missing** | **Wire/ACH volumes, client funds** | ? | ? | ? | ? | **Add (priority 1)**. It sizes the $250K fraud limit |
| **Missing** | **IRS e-file (EFIN) compromise or IRS notices** | — | — | — | — | Add for tax preparers [J]. Tax-identity fraud is a CPA-specific loss pattern |
| **Missing** | **Prior-policy claims and continuity** | ● | ● | ● | ● | Add prior carrier, retro date and any notices given under the BOP sublimit |

### 2.3 (a) Missing questions that matter for Cedar Ridge, in priority order [J unless marked]
1. **End-of-life systems.** "List any operating systems, software, firmware or devices past vendor end of support. Are any internet-facing? How are they segregated?" The pre-issue scan already flagged a legacy print server with outdated encryption. With 71 laptops, check for Windows 10 remaining after its **2025-10-14** end of support [K]. Chubb's NSE puts EOL exploitation into a risk-sharing regime [E-snip]. Harborline asks nothing, so it can't price this and has no term that touches EOL.
2. **Remote-support tools and third-party access.** "Which remote management or support tools are installed (RMM, ScreenConnect, AnyDesk and similar)? Who can use them? Is MFA enforced on the MSP's and each vendor's access?" Travelers' attestation covers contractor and third-party remote access [E-snip]. For a firm whose patching is fully outsourced (4.3), the MSP's own tooling is the largest single remote-access path.
3. **Backup resilience detail.** Ask about credentials separate from the domain, MFA on the backup console, encryption, whether the immutable copy has a lock period, and whether M365 is backed up by a third-party tool rather than only kept in retention. Chubb [E-snip] and Travelers [E-snip] both go this deep.
4. **Records by type and records processed as a service provider.** The 31,000 figure mixes clients, dependents and "employees". It is unclear whether that means Cedar Ridge staff or the **payroll clients' employees**, which could be thousands more SSNs and bank accounts. Beazley asks for counts per type [E-snip] and Coalition asks for PII/PHI counts [E-snip].
5. **Money movement.** Ask annual outbound wire/ACH dollars and count, largest single transfer, payroll dollars processed for the 40 clients, whether client funds flow through firm accounts, and whether the firm holds debit authority over client accounts. Without these, the $250K fraud limit and the $5,000 callback threshold are unanchored.
6. **Privileged and service accounts.** Ask the number of domain and global admins, whether any service account has admin rights (the MFA exception in 4.7 is a scanner account), and whether a PAM tool or LAPS is used [E-snip: Chubb PAM].
7. **Hardening.** Ask about Office macro blocking, PowerShell restrictions, local-admin removal (partly covered in 4.9) and CIS benchmark baselines [E-snip: Marsh].
8. **CPA-specific.** Ask about IRS EFIN/e-Services credential protection and any IRS notices of suspicious filings. Tie this to the IRS Publication 4557 WISP already cited in 7.1 [J].
9. **Prior coverage continuity.** Ask the prior carrier, limit and retro date, and whether any matter was notified under the BOP cyber sublimit. The answer supports the "full prior acts" in 2.8.
10. **Optional.** Ask whether an IR retainer or breach counsel is on retainer (4.16 partly covers this) and whether an MDM tool manages the 14 phones.

### 2.4 (b) Unusual or over-reaching questions [J]
- **7.1, 7.2, 7.3, 7.5, 7.6 are phrased as legal conclusions** ("Are you subject to…", "Are you a covered entity…"). Carriers normally ask for **facts** (record counts, data types, sector) and decide applicability themselves.
  - 7.6 (CIRCIA) is effectively **unanswerable** today, because the final rule isn't published (round-1 verification). For a CPA firm it has almost no underwriting value. **Delete it.**
  - 7.5 asks an SMB to apply Colorado Privacy Act thresholds and exemptions that round 1 already showed are contestable.
- **1.10 (customer concentration)** is off-topic for cyber unless Coverage S is requested. Make it conditional.
- **2.6 (why buying)** is harmless, but should be optional.
- **6.2 (how you agreed to vendor terms)** is legitimate for the dependent-BI wording (click-through terms), though unusual.
- **8.2 (stopped attacks)** is a good disclosure prompt, but see §2.5.
- Nothing is truly over-reaching in scope. The form is actually **light** on the technical depth that 2025–26 carriers ask for (Part 2.3).

### 2.5 (c) Wording that creates misrepresentation or rescission risk
1. **1.13 "payment processing" is undefined, yet the answer is "No"** while 1.8 and 5.4 show payroll processing for 40 business clients. After a payroll-diversion loss, an adjuster could argue that 1.13 was answered incorrectly. **Fix:** define it ("processing card or ACH payments for third parties as your main business"), or add a separate "payroll services for others" question with volumes.
2. **4.6 "Cloud and admin accounts (hardware security keys)"** turns a ticked box into a factual warranty that *every* cloud and admin account uses FIDO keys. One admin using authenticator-app MFA makes the answer technically false. ICS was lost on exactly this kind of scope mismatch [E-snip]. **Fix:** ask the method in a separate optional field.
3. **"All" and "100%" absolutes** in 4.6 (email, all users), 4.13 (100% of laptops and servers) and 4.10 (patch SLAs stated as fact). **Fix:** ask for the percentage and the target versus actual (for example "% of critical patches applied within 14 days last quarter"). Route exceptions to 4.7.
4. **3.5 is a compound question.** "Encrypted on laptops, in email and in cloud storage" is answered "Yes" while 5.7 admits PDFs sent by ordinary email. **Fix:** split it into three questions and add servers and backups.
5. **6.6 "Can any AI tool send payments, emails or files without a person approving each step?"** "No" is fragile. Mail-flow rules, scheduled portal notifications, payroll batch automations or a Copilot agent could all be read as sending "files" without step approval. **Fix:** narrow it to "AI agents with permission to initiate payments or external communications".
6. **8.1 terms are undefined** ("data breach", "cyber-related claim"). The March 2026 credential phish (8.2) could arguably be a "data breach" of credentials. **Fix:** define the terms, or add "including events disclosed in 8.2 are not treated as misstatements of 8.1".
7. **Optional narrative (8.2) is still "application".** The policy defines **application** as "everything you… gave us". An incomplete *optional* narrative could be argued to be a misstatement. **Fix:** say that optional disclosures can only add to coverage and can't ground rescission.
8. **Scan results are defined as part of the application** (policy definition: "…including the application form, attachments **and security scan results**"). But Harborline runs the scan. That makes the insured *adopt* the insurer's scan as its own representation, which inverts the estoppel intent. **Fix:** remove scan results from "application".
9. **The "honest mistake" remedy is silent on the would-have-declined case.** Section V part 3 says "apply the premium and terms we would have offered". If the true answer would have led to a decline (for example exposed RDP), the remedy is undefined and litigation-prone. The UK Insurance Act model it borrows handles this case explicitly. **Fix:** add a proportional-payment fallback (pay the ratio of premium charged to premium that should have been charged), or state that coverage continues on the most adverse terms offered for that class.
10. **The IT manager signs, and is an "executive".** The policy defines **executive** to include "the person responsible for your information technology or security", and executives' knowledge is imputed to the named insured. Two signatures improve accuracy, but they also widen the group whose *knowing* misstatement allows rescission. This is acceptable, but disclose it in plain English next to the signature block [J].
11. **"We will tell Harborline if any answer changes before the effective date"** doesn't mention the **mid-term 30-day duty** to report removal of a credited control (Section III part 1.5, Section V part 4.3). **Fix:** mirror that duty on the application.
12. **7.5 legal-conclusion answer.** It is legally contestable (round 1). Under Harborline's knowing-misstatement rule it is low risk, but at a carrier with standard rescission wording it would be a trap. Replace it with factual questions.

---

## 3. Credit design against market practice

| # | Harborline term | Market reference (evidence) | Verdict | Are the numbers justified? | Recommended fix [J] |
| --- | --- | --- | --- | --- | --- |
| 1 | **25% retention credit for MFA+EDR** ($10,000 to $7,500) | MFA and EDR are the most-recommended controls and effectively bind prerequisites at this size [E-snip: Marsh; Travelers attestation; Coalition]. I found no carrier that gives a *retention credit* for them | **Generous framing, low dollar stakes** ($2,500 per incident) | **Arbitrary.** No loss-cost support. It means an $8.5M CPA firm *without* MFA or EDR is insurable at $10K, which invites adverse selection | Make MFA (email, remote, privileged, backups) and EDR **eligibility requirements** above $2.5M revenue or for SSN-heavy classes. Set the band retention on the controlled risk. If a control is missing: decline, or +50% retention and ransomware coinsurance |
| 2 | **24/7 MDR halves the retention; attack waiting period 8h to 4h** | At-Bay packages: $0 retention on ransomware and fraud, no waiting period, premium lock, tied to its own MDR [E-snip]. Coalition: up to 12.5% premium credit for MDR [E-snip] and a reduced MDR waiting period [E-pkg] | **Typical (mid-market)** | Directionally supported: At-Bay 2026 says 60% of Akira victims had EDR [E-pkg]. The 50% is a judgment call. Proportionate between Coalition's premium credit and At-Bay's $0 | **Define qualifying MDR.** It should be 24/7 human-staffed, with authority to isolate hosts, cover at least 95% of endpoints, include M365 identity telemetry, and have a response SLA. State it **replaces** credit 1 rather than stacking: halve $10,000 = $5,000, which fixes the round-1 inconsistency. Require evidence (the MDR contract) |
| 3 | **10% premium credit for hardened remote access** | At most carriers, exposed RDP or an EOL VPN is a decline or pre-bind subjectivity, not a missed discount [J; E-snip: Coalition RDP/VPN MFA questions]. At-Bay 2026: remote access was the entry point in 87% of ransomware claims [E-pkg] | **Generous; risky as designed** | The 10% is arbitrary. It gives away premium for the *normal* state, and the credit can't follow a VPN that becomes KEV-listed mid-term (SonicWall, Fortinet, Ivanti) | Remove it as a credit and fold the assumption into base rates. Make exposed RDP or EOL remote tools a **bind subjectivity**. Tie mid-term remote-access KEVs to the scan-and-notice regime (row 7) |
| 4 | **20% ransomware coinsurance without verified backups** (restore tested within 12 months, offline or immutable copy) | Ransomware coinsurance (for example 75/25) and ransomware sublimits are common for weaker risks [E-snip]. Chubb uses coinsurance in its NSE and Widespread Event forms [E-snip] | **Typical, and well-targeted** | 20% is within the market pattern. The 12-month test is reasonable | (a) Measure the 12 months **from inception or incident, whichever favors the insured**, so Cedar Ridge's June 2026 test doesn't lapse in June 2027 mid-term (round 1). (b) Define a "successful restore test": at least one **critical system** restored from the offline or immutable copy. Cedar Ridge tested only the file server; M365 wasn't tested. (c) Add **credential segregation** to "verified". (d) Keep the "disabled by attacker" protection |
| 5 | **$100K fraud cap without callback** (full $250K with it) | Social-engineering sublimits and callback conditions are common [E-snip]. Coalition's validation question and Amwins' $500K SME fraud limit bracket the market [E-snip] | **Typical. More insured-friendly than conditions-precedent wording** (the "one slip" rule) | $100K and $250K are market-shaped figures. $250K is consistent with the package's $208K average fraud loss under $25M revenue [E-pkg] | Fix the round-1 gap: the "directly to your bank" wording. For CPA or payroll risks, **size the fraud limit from 5.1/5.4 volumes** (new questions). Coverage R ($500K) may be the right recommendation for a firm moving client payroll |
| 6 | **$5,000 callback threshold** (for any transfer requested by email or message; bank-detail changes at any amount) | Coalition's question uses **$25,000** [E-snip] | **Strict (insurer-favorable)** | $5K is a judgment call. It is below the insured's own $10K dual-approval threshold (5.1), which creates two thresholds staff must remember and so more "unverified instruction" findings | Align with the insured's procedure: callback on **all** bank-detail changes (already the rule) plus transfers **of $10,000 or more**. Or keep $5K but say that "one slip" also covers threshold confusion |
| 7 | **20% coinsurance for KEV-listed vulnerabilities unpatched 45 days after our written notice** | Chubb NSE: risk-sharing starts after **45 days from CVE or patch availability** with no insurer notice needed, **also covers EOL software**, and coinsurance **escalates** with time [E-snip]. Federal agencies patch KEVs within 2 weeks (2021+ CVEs) or 6 months (older) under BOD 22-01 [K] | **Generous, low bite, and one conflict** | 45 days echoes Chubb's first band, but the clock starts only after *our* notice. The trigger is only KEVs *we* can see from outside, and there is no EOL trigger | (a) **Resolve the conflict with Section V part 3.4.** A KEV the *pre-issue scan* showed would be protected by the estoppel ("we will not… reduce coverage… because of any condition that our pre-issue security scan showed"), which neutralizes this clause. Carve out "conditions we notified you in writing to remediate". (b) Add **EOL internet-facing systems** we notify you about. (c) Define "unmitigated": a vendor-documented workaround or taking the system offline counts. (d) Send notices to both the security contact and the main contact (1.14, 1.15) and to the broker, so a stale contact can't defeat or trigger the clause unfairly |
| 8 | **Claim-free reduction of 25% a year to a $2,500 floor**, conditional on current contacts and fixing criticals within 30 days | Coalition's vanishing retention: −25% after year 1, −50% after year 2, **−100% (to zero) after year 3**, conditional on resolving critical vulnerabilities flagged in Coalition Control [E-snip] | **Typical; less generous than Coalition** | The structure is borrowed from Coalition, and the floor adds prudence. **A flat $2,500 floor is arbitrary across bands.** For a $25K-retention insured it would be a 90% reduction | Define "claim-free": no paid loss above retention, and Coverage A or pre-incident use doesn't count (already stated). Say whether steps are **% of the standard band retention** (linear) or compounding: linear gives $7,500, $5,625, $3,750, $2,500; compounding gives $7,500, $5,625, $4,219, $3,164, $2,500. Set the floor at **50% of the band's standard retention**, minimum $2,500 (Part 5). Reset after a paid claim |
| 9 | **"What our scan saw, we accept"** (no denial, reduction or misrepresentation claim for anything the pre-issue scan "showed, or should have shown") | No carrier found doing this. The rationale concedes it. Market practice: scan findings become **pre-bind subjectivities** and mid-term alerts carry remediation expectations [E-snip: At-Bay, Coalition] | **Risky / novel** | Not a number, but the "should have shown" standard is open-ended: which scanner, which ports, authenticated or not? It invites expert-witness fights | Narrow it to: "We will not treat as a misrepresentation any condition **listed in the pre-issue scan report we gave you**." Delete "or should have shown". Make clear it doesn't override items we required you to remediate (row 7) or the credit rules. Remove "security scan results" from the definition of **application** (§2.5 item 8) |

**Cross-cutting credit issues [J]**
- **Verification is uneven.** Only 4.7 (MFA) attaches evidence. EDR, backups and callback are self-attested, even though the form says "where we ask for evidence, attach…". The 2025–26 market norm is dated exports [E-snip]. Require an EDR console export, a restore-test log and the callback procedure document for each ★ credit.
- **"Substantially in place"** (Section III part 1.5) is undefined. Add a threshold, for example EDR on at least 95% of endpoints, and say who bears the burden of proof.
- **Headline versus effective terms.** Because credits 1 and 3 will be earned by nearly every insurable applicant, the $10,000 retention and $6,120 base premium are effectively list prices nobody pays. Underwriters and actuaries should rate from the credited position.

---

## 4. Pricing plausibility

### 4.1 Rate environment (2025–26)

| Source | Finding | Evidence |
| --- | --- | --- |
| Marsh Global Insurance Market Index, Q2 2026 (July 2026) | Global cyber −4% (twelfth consecutive quarterly decline, after −5% in Q1). **U.S. cyber −2%**, the same as Q1 | [E-snip] |
| CIAB P&C Market Survey, Q2 2026 (August 2026) | Cyber premiums averaged **−3.2%**, the **ninth** straight quarterly decrease | [E-snip] |
| Gallagher, 2026 Cyber Insurance Market Outlook | U.S. market "essentially flat pricing in 2026" | [E-snip] |
| WTW (as quoted by a secondary page in results) | Cyber rate changes in a −5% to +5% band | [E-snip, secondary; primary WTW page not seen] |
| Gallagher Re (reinsurance) | U.S. cyber reinsurance rates reported down 32% at an April 1 renewal; ample capacity | [E-snip; the renewal year wasn't stated in the snippet] |
| Amwins | Launched SME Cyber+ with $500K social-engineering and invoice-fraud limits: a competitive SME market | [E-snip] |

**Note on Claim Ledger C17.** The ledger records Marsh's 2% as the U.S. *composite* and says no cyber figure was found. This round's snippet attributes a **2% decline specifically to U.S. cyber** in Q2 2026. Both may be true. Check the Marsh page, then reword the rationale to cite the cyber-specific figure.

### 4.2 Premium benchmarks found

| Benchmark | Figure | Comparable? | Evidence |
| --- | --- | --- | --- |
| Vouch, overall median cyber premium | **$2,755** (2,034 clients) | Weak. Startup and tech-heavy book, all revenues | [E-snip: vouch.us/blog/cyber-insurance] |
| Vouch, under $1M revenue | **$2,082** median | Not comparable (revenue) | [E-snip] |
| Vouch, "$7,078 median for $5–10M revenue" | **Not found** in any search, this round or round 1 | — | Remove it |
| Insureon, accountants' cyber | About $90/month median, roughly $1,060/year. The snippet also gives a $58/month average and "$1,900–$4,600" for smaller firms from an unidentified page | Not comparable. Micro firms, often lower limits | [E-snip, internally inconsistent] |
| Aggregator ranges, $1M limit, $1–10M revenue | "$1,500–$5,000/yr". Another: "$1,000–$7,500 for $1M". Mid-market $10–50M "$5,000–$35,000" | Weak. Unknown methodology | [E-snip, low-quality secondary] |
| At-Bay/Coalition issued policies cited by the rationale | "$2,330–$4,048" | **Unverifiable here** (astroa.org and mwvhomelessalliance.org are blocked). By domain, both insureds look like **small nonprofits** [J]. They are single data points, not benchmarks | Rationale; not in ledger (round 1) |

### 4.3 Judgment on $5,508 [J]
- **Plausible range for this risk in the 2026 soft market: about $4,500–$8,500** for $1M aggregate at a $7,500 retention on admitted paper. The factors behind this range are:
  - accounting class, with about 31K SSN-bearing records and tax-season BI sensitivity
  - payroll processing for 40 clients, which is a heavy BEC and funds-transfer exposure
  - a broader-than-market core: system-failure BI, bricking, reputational harm, any-channel and deepfake fraud, invoice manipulation, employee privacy and paper records
  - strong controls: MFA incl. hardware keys, EDR, DMARC reject, immutable and offline backups, callback, positive pay, tested IR plan
- $5,508 sits in the **lower-middle** of that range. It is defensible for a well-controlled account. It is at or above the generic "$1M for $1–10M revenue" ranges [E-snip], which is right for the class.
- **Implied-frequency sanity check (illustrative, not actuarial).** The package cites At-Bay's 2026 average claim of $180K for insureds under $25M revenue [E-pkg]. The calculation runs as follows:
  1. Net of the $7,500 retention, the average claim is about $172.5K.
  2. A target loss ratio of 60–65% on $5,508 gives expected losses of about $3,300–$3,580.
  3. $3,300–$3,580 divided by $172.5K implies an annual claim frequency of about **1.9–2.1%**.
  4. That frequency is reasonable for an SMB professional-services book *including* fraud claims [J]. If the true frequency for CPA firms is higher, which BEC exposure makes likely, the premium is light rather than heavy.
- **What weakens the price.** The 10% remote-access credit (−$612) pays for a condition the market treats as a prerequisite (Part 3, row 3). Without it, $6,120 is still inside the plausible range.
- **Rationale wording to replace the benchmark sentence:** "The illustrative $5,508 premium is a judgment-based figure, subject to actuarial rating. Public benchmarks are sparse. Vouch reports an overall median cyber premium of $2,755 for a startup-heavy book. Broker and aggregator guides place $1M limits for $1–10M revenue firms at roughly $1,500–$7,500. Rates are soft: CIAB reports cyber premiums down 3.2% in Q2 2026, and Marsh reports U.S. cyber down 2%. We place Cedar Ridge in the upper half of generic ranges because of its SSN volume, client payroll processing and Harborline's broader core." (Re-verify each figure at source before submitting.)

---

## 5. Retention bands: a proposed table

The rationale says retentions scale "from $2,500 to $25,000", and the application cites a "$5M–$25M" band, but no band table exists. The market evidence is thin: small businesses carry $1,000–$2,500, larger SMBs $5,000–$25,000 [E-snip, secondary], and the package's own issued-policy references show $2,500 (At-Bay, Coalition) and $10,000 (Vouch, Corgi) [E-pkg]. The structure below is **my judgment**. It anchors the standard retention at about **0.1–0.15% of revenue**, rounded to a standard step and capped at $25K for an SMB product.

| Band | Revenue | Standard retention (assumes MFA+EDR as eligibility) | Retention as % of revenue | With qualifying 24/7 MDR (−50%) | Claim-free floor (50% of standard, min $2,500) | Higher-retention options |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Under $2.5M | $2,500 | ≥0.10% | $1,250 | $2,500 (no step-down) | $5,000 |
| 2 | $2.5M–$5M | $5,000 | 0.10–0.20% | $2,500 | $2,500 | $10,000 |
| 3 | $5M–$10M (**Cedar Ridge, $8.5M**) | **$10,000** | 0.10–0.20% | $5,000 | $5,000 | $15,000 / $25,000 |
| 4 | $10M–$25M | $15,000 | 0.06–0.15% | $7,500 | $7,500 | $25,000 / $50,000 |
| 5 | $25M–$50M | $25,000 | 0.05–0.10% | $12,500 | $12,500 | $50,000 / $100,000 |

**Notes [J]**
- **Cedar Ridge's standard retention is unchanged at $10,000.** Under this table, though, the 25% MFA+EDR credit would become an eligibility rule. That moves Cedar Ridge back to $10,000 unless Harborline chooses to keep the credit as a marketing feature. If the credit is kept, add a "MFA+EDR (−25%)" column: $1,875 (floored at $2,500), $3,750, $7,500, $11,250 and $18,750.
- **The present "$5M–$25M" band is too wide.** A 5x revenue spread sharing one retention means $5M firms carry 0.2% of revenue while $25M firms carry 0.04%. Split it at $10M.
- **Fraud retention (Coverage H)** can stay one step below the band, with the $2,500 fast-report reduction.
- **Class adjustment.** For classes with heavy money movement (payroll services, title, law firms with trust accounts), consider a separate fraud retention one band higher when callback isn't evidenced.
- **Unresolved band edges.** Round 1 found that the rationale's "$2,500 to $25,000" range doesn't define where $2,500 applies (under $2.5M? under $5M?). The table fixes that.

---

## 6. Prioritized fixes

1. **Add the missing questions** (Part 2.3, items 1–5): EOL systems, remote-support and vendor access, backup credential segregation and MFA, records by type and processed for clients, and money-movement volumes.
2. **Resolve the estoppel–KEV conflict** (Part 3, rows 7 and 9). Delete "or should have shown", and remove "security scan results" from the definition of **application**.
3. **Remove the absolute-scope traps** (§2.5, items 1–6): the undefined "payment processing" in 1.13, the "(hardware security keys)" warranty, triple-barrelled 3.5 and broad 6.6.
4. **Recast MFA+EDR and hardened remote access as eligibility, not credits.** Or, if they are kept for transparency, label them "standard terms assume these controls".
5. **Define qualifying MDR** and make the MDR credit an alternative to the MFA+EDR credit, not an addition.
6. **Fix the backup test window** (inception or incident, whichever favors the insured) and define "successful restore test".
7. **Publish the band table** (Part 5) and a band-relative claim-free floor.
8. **Replace the premium benchmark sentence** (Part 4.3). Drop the $7,078 figure. Drop the "$2,330–$4,048" framing unless both documents are re-verified and described as small-nonprofit single data points.
9. **Add a would-have-declined fallback** to the honest-mistake condition, as the UK Insurance Act model it borrows does.

---

## Sources (all accessed 2026-09-27; search-snippet level unless marked)

**Controls, applications and attestations**
- Marsh McLennan, "12 key controls" and controls research: marshmma.com/us/insights/details/cyber-resilience-twelve-key-controls-to-strengthen-your-security.html; insurancebusinessmag.com/us/news/risk-management/key-controls-linked-to-decreased-risk-of-cyber-incidents--report-442177.aspx; reinsurancene.ws/marsh-mclennan-research-links-cybersecurity-controls-and-reduced-cyber-risk/
- Coalition application questions (third-party-hosted): cybcovsol.com/Coalition-Application.pdf. Coalition quote-data help article: help.coalitioninc.com/hc/en-us/articles/7665931229851 (blocked; snippet only)
- Chubb Cyber ERM proposal forms (non-U.S.): chubb.com/…/chubb-cyber-erm-proposal-form-revenue-below-rm1billion.pdf; chubb.com/…/11100a_chubb_cyber_erm_extensive_proposal_form.pdf; scribd.com/document/736427089/Ransomware-Supplementary-Proposal
- Travelers v. ICS and the MFA attestation: tritoncomputercorp.com/blog/2026/05/01/why-cyber-insurance-policy-void-travelers-ics-declarations/. Insurance Journal, 2022-08-30 (package Source 24). Catalog entry travelers-cf4a70b9 (CYB-14306, 2023-03)
- Beazley applications: beazley.com/globalassets/product-documents/application/beazley_cyber_insurance_application_below_250m.pdf (F00863 04/2023); beazley.com/globalassets/product-documents/app-form/beazley-cyber-insurance-application-short-sub-20m.pdf (UK); bindledger.com/blog/how-to-answer-the-beazley-cyber-insurance-application
- Evidence-based underwriting commentary: compyl.com/guides/cyber-insurance-readiness-guide/; seedpodcyber.com (several pages; low-quality secondary)

**Coinsurance, EOL and endorsements**
- Chubb NSE: chubb.com Cyber ERM Factsheet (APAC); chubb.com/…/chubb_neglected_software_cyber_case_studies_uk.pdf; westchester.com/…/Westchester_CyberSystemicRiskProductUpdate.pdf (Broker FAQ, Oct 2021); lmalloyds.com/wp-content/uploads/2025/09/Chubb-Cyber-ERM-V2.2-Policy-Documents-1-003-International.pdf (all blocked for fetch; snippets only)
- HeroDevs, "Cyber Insurance and End-of-Life Software: What's Excluded in 2026": herodevs.com/blog-posts/cyber-insurance-and-end-of-life-software-whats-excluded-in-2026
- Coinsurance and sublimits (agency guidance): coverlink.com/cyber-liability-insurance/cyber-solutions-the-role-of-coinsurance-sublimits-in-cyber-insurance-policies/; horstinsurance.com; bitnerhenry.com
- Social engineering: holmesmurphy.com/blog/social-engineering-fraud-is-escalating-are-your-controls-and-coverage-keeping-up/; seedpodcyber.com/cyber-insurance-sublimits-explained/

**Monitoring, MDR and retention programs**
- At-Bay InsurSec packages, 2025-10-02: at-bay.com/press_releases/launches-industry-first-solutions-that-unlock-crucial-cyber-insurance-coverage-for-ransomware-and-financial-fraud/; businesswire.com/news/home/20251002591457/en/
- At-Bay, "How Active Risk Monitoring Lowers Losses": at-bay.com/articles/active-risk-monitoring-lowers-losses/
- Coalition MDR premium credits: coalitioninc.com/blog/cyber-insurance/premium-credits-mdr
- Coalition vanishing retention: coalitioninc.com/blog/cyber-insurance/how-vanishing-retention-rewards-security-conscious-policyholders
- Coalition Active Cyber Policy: coalitioninc.com/blog/cyber-insurance/introducing-the-active-cyber-policy

**Rating, pricing and market**
- Romanosky et al., "Content analysis of cyber insurance policies: how do carriers price cyber risk?", *Journal of Cybersecurity* 5(1), 2019: academic.oup.com/cybersecurity/article/5/1/tyz002/5366419
- Marsh Q2 2026 Global Insurance Market Index: marsh.com/en/corp/about/news/global-commercial-insurance-falls-6-percent-q2-2026.html; insurancejournal.com/news/national/2026/07/23/878716.htm
- CIAB Q2 2026 P&C Market Survey: ciab.com/resources/q2-2026-pc-market-survey; insurancejournal.com/news/national/2026/08/20/882240.htm
- Gallagher 2026 Cyber Insurance Market Outlook: ajg.com/news-and-insights/2026-cyber-insurance-market-outlook/
- Gallagher Re cyber reinsurance: reinsurancene.ws/us-cyber-rates-drop-32-at-april-1-bespoke-solutions-surge-amid-ample-reinsurance-capacity-gallagher-re/
- Amwins Cyber+: insurancebusinessmag.com/us/news/cyber/amwins-launches-cyber-to-address-sme-cyber-insurance-gaps-554636.aspx
- Vouch: vouch.us/blog/cyber-insurance (overall median $2,755; under $1M revenue $2,082)
- Insureon accountants' cost: insureon.com/finance-accounting-business-insurance/accountants-auditors/cost
- Deductible ranges: insureon.com/small-business-insurance/cyber-liability/how-much-cyber-liability-do-i-need; seedpodcyber.com/cyber-insurance-deductibles-explained/
- Aggregator price ranges (low quality): proinsgrp.com/business/cyber-liability-insurance/cost/; seedpodcyber.com/how-much-does-cyber-insurance-cost/; beancount.io/blog/2026/05/09/…

**Package sources relied on, not re-verified [E-pkg]**
- At-Bay 2026 InsurSec Report: $180K average claim under $25M revenue; 60% of Akira victims had EDR; 87% remote-access entry; $208K average fraud loss
- Coalition April 2026 MDR waiting-period change
- Vouch declarations ($62,500 ransomware sublimit)
