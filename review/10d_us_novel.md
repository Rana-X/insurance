# 10d. Standout US forms and novel cyber structures: what Harborline should borrow

Review date: September 27, 2026. Scope: US SMB cyber forms and endorsements from 2024 to 2026, plus new product structures from anywhere, judged against Harborline HIC-CY-100 (10/26) and the fixes already planned in `README.md`.

## Evidence caveat (read first)

- **Nothing was opened at source.** A single attempt each was made at 18 document hosts, including heartlandmutualinsurance.com (HSB CSC 02-2025), cfins.com (C&F Simple Cyber v6.0), insurancexdate.com (ISO CY 00 02), gny.com, munichre.com, hiscox.com, thehartford.com, tmhcc.com, britinsurance.com, parametrixinsurance.com, stoik.io, aaisonline.com and verisk.com. Every one was blocked (HTTP 000). None was retried.
- **20 of 20 WebSearch calls were used.** Everything below is labelled with one of these evidence levels:
  - **search-snippet**: text from a search result or its summary. Paraphrased, never quoted as carrier wording.
  - **catalog note**: a row in `catalog/cyber_policies.csv`.
  - **prior report**: reports 02, 03, 04 or 09 in this folder, which are themselves snippet-level.
  - **background knowledge**: my own understanding, not verified this session.
- **No carrier clause text is reproduced.** Every block marked "Harborline draft" is new drafting for Harborline. Put it in your own words before it goes into the package.
- **What the task asked for but could not be found:**
  - **AAIS.** No AAIS cyber coverage form turned up in the catalog or in one targeted search. AAIS is not relied on anywhere below.
  - **ISO CY 00 02 11 21.** It is copyrighted and licensee-only, so only summaries were available.

---

## 1. Bottom line

1. **The admitted forms confirm the direction of Harborline's planned Tier 2 fixes. They also add three filing-tested refinements:**
   - HSB's single payment-fraud trigger, which names both the insured and its bank as the party deceived;
   - ISO's rule that related events are treated as discovered in the earliest policy period;
   - the February 2026 *CiCi Enterprises v. HSB Specialty* ruling. It struck down a ransomware sublimit because the sublimit didn't say it applied across insuring agreements. Harborline's planned cross-coverage caps must say so expressly.
2. **The biggest new-structure idea is an optional "Fast Downtime Payment".** It pays a fixed amount per hour after an objective trigger, within days and with no proof of loss, and the payment is credited against the indemnity BI claim. AIG launched a Parametrix-monitored cloud-outage product on August 13, 2026, and Parametrix paid claims within days of the AWS outage of October 20, 2025. So this is now a live US structure, not a thought experiment. Section 5 sketches how it would sit next to Harborline's aggregate.
3. **Per-event limits (Brit C360, March 2026) and unlimited reinstatements (CFC) are real, but uncapped frequency is hard to rate on admitted paper.** Harborline should offer **one priced reinstatement** instead, which works out the same as "per-incident limit, with an annual cap of twice that limit".
4. **Harborline already has most of 2026's headline SMB features:**
   - Coalition's August 2026 Enhanced Business Recovery set: key customer, a single forensic accountant, a cash advance and a shorter MDR wait;
   - vanishing retention, pre-claim help, pay-on-behalf, betterment and voluntary shutdown.

   Its firm 50% advance is still ahead of Coalition's discretionary Lifeline. Three gaps remain:
   - **deepfake and impersonation response**;
   - **a $0-retention path**;
   - **an AI voluntary-shutdown rule**.
5. **Colorado SB25-058 (2025) lets insurers give free loss-mitigation services that aren't specified in the policy.** Harborline can therefore bundle security tools the way Elpha, Stoïk and Coalition do. It should keep the services outside the contract and put only a no-forfeiture promise in the policy.

### Verdict summary

| # | Idea | Source | Verdict | Harborline today |
| --- | --- | --- | --- | --- |
| 1 | One payment-fraud trigger naming both deceived parties | HSB Cyber Suite CSC 02-2025 | **ADAPT** | Partly (T2-1/T2-1a planned) |
| 2 | Limits map (each incident / policy period) and cross-coverage caps that say so expressly | HSB CSC; ISO CY 00 02; *CiCi v. HSB* (Feb 2026) | **ADOPT** | No (T2-1e, T2-3 planned) |
| 3 | Related events treated as discovered in the earliest period | ISO CY 00 02 11 21 | **ADOPT** | No (W-06 covers incident-to-claim only) |
| 4 | Cloud-account tie-breaker for vendor-side attacks | Beazley BBR and At-Bay hosted-systems approach | **ADAPT** | No (W-01 planned) |
| 5 | Fast Downtime Payment (parametric BI) | AIG + Parametrix (Aug 2026); LMA SME draft (2026) | **ADAPT** (optional Coverage T) | No |
| 6 | Widespread-outage cap, used only as an accumulation control | Chubb Widespread Event PF-54815 (06/21) | **ADAPT** (Fast Downtime Payment and P only) | No |
| 7 | Per-event limits and reinstatement | Brit C360 (Mar 2026); CFC; Coalition | **ADAPT** (optional Coverage U, one reinstatement) | No (declined earlier) |
| 8 | Security services outside the contract, plus a no-forfeiture promise | Elpha, Stoïk Protect, Coalition Control, Hiscox CyberClear Academy, Travelers Cyber Risk Services; CO SB25-058 | **ADAPT** | Partly (scan, alerts) |
| 9 | $0-retention path with qualifying MDR | At-Bay InsurSec (Oct 2025); Coalition | **ADAPT** (optional) | Partly (MDR halves the retention) |
| 10 | Deepfake and impersonation response costs | Coalition Deepfake Response Endorsement (Dec 2025) | **ADAPT** | No (named gap, T4-9) |
| 11 | AI voluntary shutdown; AI regulatory defense | Beazley AI endorsements (Sept 2026) | **ADAPT** (shutdown) / **OPTIONAL** (regulatory) | No |
| 12 | Court-attendance compensation; reward expenses | Tokio Marine HCC (NetGuard Plus / e-MD) | **ADAPT** (court) / **SKIP** (reward) | No |
| 13 | Retention billed last (extends pay-on-behalf) | Pay-on-behalf practice; Harborline adaptation | **ADAPT** | Pay-on-behalf yes |
| 14 | Neglected Software Exploit | Chubb Cyber ERM | **SKIP** (already has KEV rule) | Yes, narrower |
| 15 | Enhanced Business Recovery set | Coalition (Aug 2026) | **SKIP** (already has all four) | Yes |
| 16 | Vanishing retention; pre-claim help | Coalition | **SKIP** (already has) | Yes |
| 17 | Contingent bodily injury and property damage "wrap" | C&F Simple Cyber v6.0 (Sept 2025) | **OPTIONAL** (segment-dependent) | No |
| 18 | Embedded / BOP cyber | HSB Cyber Suite; Hartford CyberChoice First Response (Dec 2025); Chubb Studio | **OPTIONAL** (distribution) | N/A |
| 19 | Warranty plus insurance | Cysurance | **SKIP** | N/A |
| 20 | Public-entity pools, affinity programs and security grants | Public-entity pools; Munich Re Specialty (2026) | **OPTIONAL** (distribution) | N/A |

---

## 2. Idea register

One entry per idea: source, what it does, why it's good for SMBs, evidence, fit and verdict. Drafts for every ADOPT or ADAPT item follow in section 4.

### 1. HSB Cyber Suite: one payment-fraud trigger that names both deceived parties

- **Source.** Hartford Steam Boiler (Munich Re), Cyber Suite Coverage Form **CSC 02-2025**, 24 pages. It is filed white-label by regional mutuals (Heartland, GNY, West Bend, Acuity, Erie).
- **What it does.** Misdirected Payment Fraud responds to a **"wrongful transfer event"**. That is a deliberate criminal deception of the insured, **or of a financial institution with which the insured has an account**, by someone who is not an employee, using email, fax or phone, that leads either one to send money or divert a payment. The loss from one wrongful transfer event is capped by a sublimit that is part of the Annual Aggregate Limit. (All of this is paraphrase.)
- **Why it's good for SMBs.** Bank-by-phone fraud is covered without a second definition. The deceived party is the business, not "an employee", so partners and owners are included.
- **Evidence.**
  - Form title and page count: [CSC 02-2025 PDF](https://heartlandmutualinsurance.com/wp-content/uploads/2024/12/Cyber-Suite-Coverage-Form-CSC-02-2025.pdf) (catalog note; blocked).
  - Definition and per-event sublimit: search-snippet (Sept 27, 2026) summarizing HSB Cyber Suite material. The candidate pages were [West Bend highlights WB-2827](https://www.pianational.org/docs/default-source/products/west-bend_cyber-suite-coverage_wb-2827.pdf), [GNY overview (2024-12)](https://www.gny.com/sites/default/files/file/2024-12/CyberSuite_Coverage_GNY.pdf) and [Acuity](https://www.acuity.com/the-focus/agent/acuitys-newest-cyber-coverages). The exact page wasn't identified.
- **Fit.** It solves T2-1 (bank-direct fraud) and T2-1a (partners) in one definition, where W-02 and W-03 plan two. Don't copy two things:
  - the **non-employee** limit, because Harborline covers rogue insiders (W-04);
  - the **email, fax or phone** list, because Harborline's "any means" is broader.
- **Verdict: ADAPT.**

### 2. Limits map and cross-coverage caps that say so expressly

- **Sources.**
  - HSB CSC 02-2025: per-event sublimits "part of, and not in addition to" the Annual Aggregate Limit (paraphrase).
  - ISO CY 00 02 11 21: four first-party and four claims-made liability insuring agreements, each with its own limit, all subject to a policy aggregate.
  - ***CiCi Enterprises, LP v. HSB Specialty Insurance Co.*** (N.D. Tex., Judge Sam A. Lindsay, **February 23, 2026**). A $250K "Ransomware Event Sublimit Endorsement" didn't cap the cyber-extortion insuring agreement under a $3M aggregate policy. If HSB meant the sublimit to apply whichever insuring agreement was triggered, it had to say so expressly. The ruling is reported as the first of its kind.
- **What it does.** Every limit shows its unit: each event, each period, or both. A cap meant to run across coverages says that it does.
- **Why it's good for SMBs.** Owners can see what they bought, and it heads off per-event versus per-period fights (W-08).
- **Evidence.**
  - HSB: search-snippet (same search as idea 1).
  - ISO: [InsuranceXDate CY 00 02](https://www.insurancexdate.com/insurance-forms/CY/CY-00-02/) (catalog note and search-snippet); [Law.com, July 26, 2021](https://www.law.com/insurance-coverage-law-center/2021/07/26/iso-commercial-cyber-product-replaced-part-one-cy-00-03-11-21-sections-i-iv-423-117619/) (search-snippet).
  - *CiCi*: [Hunton](https://www.hunton.com/hunton-insurance-recovery-blog/court-refuses-to-slice-up-cicis-cyber-extortion-coverage); [Insurance Business](https://www.insurancebusinessmag.com/us/news/cyber/court-blocks-hsbs-ransomware-sublimit-in-firstofitskind-cyber-ruling-567006.aspx); [Phelps drafting note](https://www.phelps.com/insights/drafting-ransomware-sublimits-that-hold-up-what-insurers-can-learn-from-cici-enterprises.html) (all search-snippet, Sept 27, 2026). Check the reporter citation before quoting.
- **Fit.** Harborline plans two cross-coverage caps: the $250K system-failure limit over D and F (T2-3), and the ransomware coinsurance limited to restoration and BI (T2-6). Both are exactly what *CiCi* says must be express. The CiCi policy was HSB Specialty's standalone cyber form, not Cyber Suite.
- **Verdict: ADOPT.**

### 3. ISO: related events are one event, treated as discovered in the earliest period

- **Source.** ISO Commercial Cyber Insurance Policy **CY 00 02 11 21**. It replaced CY 00 01 01 18 in many states. Circular LI-CY-2017-005 introduced the first edition (catalog note).
- **What it does.** Related cyber incidents, extortion threats, breaches or claims arising from the same facts are treated as one event, discovered in the **earliest** policy period in which any part was discovered. The summary says "will likely treat", so it is hedged.
- **Why it's good for SMBs.** One limit and one retention per attack campaign. No gap when the tail of an attack spills into the renewal.
- **Evidence.** Search-snippet (Sept 27, 2026), from the results for [InsuranceXDate](https://www.insurancexdate.com/insurance-forms/CY/CY-00-02/) and [PropertyCasualty360 FC&S, Aug 8, 2021](https://www.propertycasualty360.com/fcs/2021/08/08/iso-commercial-cyber-product-replaced-part-one-cy-00-03-11-21-sections-i-iv/).
- **Fit.** W-06 already links an incident to its later claims and defines "related". It does not say **which first-party policy year** a related incident belongs to, and the ISO rule fills that gap. It needs one addition for a new customer: continuity when the earlier policy was issued by another insurer.
- **Verdict: ADOPT.** It extends W-06; it does not replace it.

### 4. Cloud-account tie-breaker for attacks on the vendor's side

- **Sources.**
  - Beazley BBR's older US forms bring systems that a third party operates under written contract to host the insured's data or applications into "computer systems". (Background knowledge, from BBR F00403 and F00104 in the catalog: [F00403 PDF](https://eperils.com/wp-content/uploads/2016/09/f00043-042014.pdf); not re-verified.)
  - At-Bay AB-CYB-001.2 has "External Computer Systems" in its computer-system definition (prior report 02, from the issued policy).
- **What it does.** Data you store at a SaaS or cloud vendor is treated as yours when an attack reaches it.
- **Fit.** W-01 plans the reverse split: the tenant is yours, and the vendor's infrastructure is a dependent system. That is cleaner for BI and should be kept. One case is still unresolved. When attackers breach the **vendor** and corrupt or encrypt data **inside your tenant** (Snowflake- or Salesloft-Drift-type events), it is unclear whether that is a security failure "affecting your computer systems" (B, C, F, H at full limit) or only an E event. A one-sentence tie-breaker closes it.
- **Verdict: ADAPT** (add-on to W-01).

### 5. Fast Downtime Payment (parametric BI)

- **Sources.**
  - **AIG Parametric Cloud Outage Solution with Parametrix monitoring (launched August 13, 2026).** A 2-hour waiting period with no monetary retention after it. Payment follows a predefined formula based on the downtime of AWS, Azure or Google Cloud in designated US and EU regions, which are split into three tiers with different payout formulas.
  - **Parametrix** paid clients within days of the **October 20, 2025 AWS outage**.
  - Parametrix placed **Cumulus Re III**, $35M of retrocession for Hannover Re for 2026–27 against sustained cloud outages.
  - **LMA draft standard SME cyber wording (UK).** It had been in development for about 8 months as of May 21, 2026, with "parametric-style" fixed amounts per hour or day for BI and supplier downtime, and a US adaptation is planned. The LMA published an SME **property and BI** model wording on June 30, 2026, but no cyber SME wording was found published by Sept 27, 2026.
- **Why it's good for SMBs.** Cash in days, no forensic accounting for short outages, and cover for cloud outages the insured can't prove or can't afford P for.
- **Evidence.**
  - [The Insurer, Aug 13, 2026](https://www.theinsurer.com/cyber-risk/news/aig-launches-parametric-cloud-outage-solution-backed-by-parametrixs-monitoring-2026-08-13/); [Artemis (AIG)](https://www.artemis.bm/news/aig-launches-parametric-cloud-outage-insurance-working-with-parametrix/); [Artemis (AWS payout)](https://www.artemis.bm/news/parametrix-pays-claims-swiftly-after-aws-outage-triggers-parametric-policies/); [Insurance Business (Cumulus Re)](https://www.insurancebusinessmag.com/reinsurance/news/breaking-news/parametrix-issues-largest-cumulus-re-cat-bond-for-cloud-risks-571189.aspx) (all search-snippet, Sept 27, 2026).
  - [The Insurer, May 21, 2026 (LMA cyber)](https://www.theinsurer.com/ti/news/lma-gives-details-on-incoming-standardised-cyber-wordings-for-uk-sme-market-2026-05-21/) (prior report 09); [LMA property/BI wording, June 30, 2026](https://lmalloyds.com/lma-launches-new-sme-property-and-business-interruption-model-wording/) (search-snippet).
- **Fit.** It sits on top of D, E and P as a guaranteed floor, and it fits Harborline's cash-crunch thesis (the firm 50% advance).
- **Verdict: ADAPT** as optional Coverage T. The full design is in section 5.

### 6. Widespread-outage cap, used only as an accumulation control

- **Source.** Chubb Cyber ERM **Widespread Event Endorsement**. US: PF-54815 (06/21) (prior report 04; blocked). AU: ERM v2.2 E13.
- **What it does.** Separate limits, retentions and coinsurance for events that also hit parties with no relationship to the insured. They can be set for all widespread events, or by peril: severe vulnerability exploits, severe zero-day exploits (one limb turns on reporting within 45 days of the associated incident) and software supply-chain exploits.
- **Evidence.** [Chubb AU endorsement PDF](https://www.chubb.com/content/dam/chubb-sites/chubb-com/au-en/business/cyber-insurance/documents/pdf/erm-v2-2-e13-widespread-event-endorsement.pdf); [Chubb article](https://www.chubb.com/au-en/articles/business/a-better-way-to-define-and-insure-systemic-cyber-events.html) (search-snippet, Sept 27, 2026).
- **Fit.** T2-3 says never to cap attacks on the insured's own systems this way. So Harborline uses a widespread-outage cap **only** for the new Fast Downtime Payment and for optional P, never for D, E or F.
- **Verdict: ADAPT** (narrow).

### 7. Per-event limits and reinstatement

- **Sources.**
  - **Brit C360** (UK SME, launched March 2026). The full limit applies on an "any one claim" basis an unlimited number of times in the period. Limits go up to £5M, with no-referral quotes up to a £250M figure (probably turnover).
  - **CFC** "unlimited reinstatements" (July 2024 article).
  - **Coalition** issued policy: unlimited reinstatements (prior report 02, from the issued policy).
- **Why it's good for SMBs.** One big loss doesn't leave the business bare for the rest of the year. At-Bay reports that firms hit once are twice as likely to be hit again within two years (prior report 02).
- **Evidence.** [Brit release](https://www.britinsurance.com/news/brit-launches-new-cyber-product-for-smes); [Insurance Business UK](https://www.insurancebusinessmag.com/uk/news/cyber/brit-targets-sme-cyber-gap-with-new-any-one-claim-product-569152.aspx); [CIR, Mar 19, 2026](https://www.cirmagazine.com/cir/c2026031901.php); [CFC, July 2024](https://www.cfc.com/en-us/knowledge/resources/articles/2024/07/cyber-coverage-highlights-unlimited-reinstatements/) (all search-snippet).
- **Fit.** Unlimited frequency is hard to rate and file on admitted paper, and Harborline declined it earlier (report 02, row 37). A **single, priced reinstatement** gets most of the value with a hard annual cap.
- **Verdict: ADAPT** as optional Coverage U. See section 5.

### 8. Security services outside the contract, plus a no-forfeiture promise

- **Sources.**
  - **Elpha Secure:** its own security software is embedded in every policy, and its cybercrime limit rose to $500K in February 2026 (prior report 02; sample policy [PDF](https://elphasecure.com/docasset/documents/Sample-Policy.pdf), catalog note).
  - **Stoïk (France):** Stoïk Protect is included in the contract, with an external scan, phishing simulation, Active Directory scan and cloud scan. It writes up to €7.5M, with Swiss Re and Tokio Marine HCC among its capacity partners, and had about €50M of GWP in 2025. [Stoïk docs](https://docs.stoik.io/onboarding/why-do-insurees-have-a-stoik-protect-account) (search-snippet).
  - **Coalition Control, Hiscox CyberClear Academy and Cowbell Prime Plus services:** catalog notes and prior report 02.
  - **Travelers Cyber Risk Services:** no-cost services. Travelers says users are "almost 20% less likely" to have a breach and have "nearly 27% lower total claim costs" ([Travelers sustainability page](https://sustainability.travelers.com/drivers-of-sustained-value/cybersecurity/cyber-product-offerings), search-snippet, Travelers' own data).
- **Colorado law.** **SB25-058, the "Insurance Rebate Reform Model Act"** (2025 Session Laws ch. 84), amended C.R.S. 10-3-1104. Insurers may give value-added products or services **not specified in the policy**, free or at reduced cost, if they relate to the coverage and aim mainly at loss mitigation, lower claim costs, education, risk monitoring or risk reduction. Customer-protection conditions apply. [Bill page](https://leg.colorado.gov/bills/sb25-058); [session law PDF](https://content.leg.colorado.gov/sites/default/files/documents/2025A/bills/sl/2025a_sl_084.pdf) (search-snippet). The snippet's line that cybersecurity help is "specifically" allowed may be the summarizer's gloss, so verify it.
- **Fit.** Harborline already scans before issue and sends critical alerts. The step to add is to keep the tools **outside** the contract, because SB25-058 applies only to services not specified in the policy, and to promise in the policy that services never cut cover.
- **Verdict: ADAPT.**

### 9. $0-retention path with qualifying MDR

- **Sources.**
  - **At-Bay InsurSec packages** (October 2, 2025): zero retention on ransomware and financial fraud for qualifying package buyers. Stance MDR for Email can raise fraud sublimits to $1M.
  - **Coalition:** $0 retention when its in-house incident response is used.
  - **Coalition EBR:** a shorter waiting period with top-tier MDR.
  - All from prior report 02: [Business Wire (At-Bay)](https://www.businesswire.com/news/home/20251002591457/en/); [Coalition announcement](https://www.coalitioninc.com/announcements/coalition-eliminates-out-of-pocket-security-and-forensics-costs-for-policyholders-facing-a-cyber-claim) (search-snippet).
- **Fit.** Harborline halves the retention and cuts the wait to 4 hours with MDR, and Coverage R lifts fraud to $1M with MDR. Review T4-9 names the missing $0 path as a trade-off. Adding it is cheap: $7,500 × about 1.2% frequency is about $90 a year of expected cost (package loss-cost sketch; judgment).
- **Verdict: ADAPT** (optional tier).

### 10. Deepfake and impersonation response

- **Source.** **Coalition Deepfake Response Endorsement** (added globally, December 2025). It pays for deepfake forensic analysis, legal work to get the content taken down, and crisis PR.
- **Evidence.** [Coalition](https://www.coalitioninc.com/announcements/coalition-adds-deepfake-response-endorsement); [SiliconANGLE, Dec 9, 2025](https://siliconangle.com/2025/12/09/coalition-expands-cyber-insurance-cover-deepfake-driven-reputation-attacks/) (search-snippet).
- **Why it's good for SMBs.** A fake partner video, or a lookalike "cedarridge-cpa.com" domain used to phish clients, needs no breach of the insured. Today Harborline's B, H.2 and N all require a security failure or privacy event, so none responds.
- **Verdict: ADAPT.** Row 15 of the synthesis's section 3 table and T4-9 name this as a gap; it is not a planned fix.

### 11. AI voluntary shutdown; AI regulatory defense

- **Source.** Beazley, September 17–24, 2026: affirmative AI cover confirmed, plus **AI Voluntary Shutdown** (BI when you switch off your own malfunctioning AI) and **AI Regulatory Defense & Penalties** (fines under AI-specific laws).
- **Evidence.** [Insurance Journal, Sept 25, 2026](https://www.insurancejournal.com/news/national/2026/09/25/886788.htm) (prior report 09; search-snippet).
- **Fit.**
  - T2-5 moves non-malicious agent errors to system failure. It doesn't cover the insured's own decision to switch an agent off. W-25 covers precautionary shutdowns only for a security failure.
  - AI regulation (Colorado SB 26-189, effective 2027) sits outside Coverage J, which needs a security failure or privacy event.
- **Verdict.** Shutdown: **ADAPT**. Regulatory: **OPTIONAL**. It matters for AI deployers; Cedar Ridge's exposure is low.

### 12. Court-attendance compensation (and reward expenses)

- **Source.** Tokio Marine HCC. The e-MD/MEDEFENSE Plus material lists sublimits for post-breach remediation, TCPA defense, **reward expenses** and **court attendance costs** ([TMHCC healthcare page](https://www.tmhcc.com/en-us/products/cyber-and-tech/cyber-for-healthcare), search-snippet). The NetGuard Plus NGP 1000 (04/2020) base form includes dependent system failure, bricking and cyber crime (catalog note). Whether NetGuard Plus itself has court-attendance cover is **not verified**.
- **Fit.** Harborline's claim expenses exclude "your own staff's salaries". At a partner-led CPA firm, deposition and trial days are real lost billings.
- **Verdict.** Court attendance: **ADAPT** (small). Reward expenses: **SKIP**, because they add little for SMBs and law enforcement rarely acts on paid tips in cyber cases.

### 13. Retention billed last (extends pay-on-behalf)

- **Source.** A Harborline adaptation. Pay-on-behalf and direct vendor billing are market practice (Harborline's "We pay vendors directly"). No carrier was found that bills the retention after the event: background knowledge, and not claimed as market practice.
- **Why it's good for SMBs.** The owner doesn't have to find $7,500 in cash during week one of a ransomware attack.
- **Verdict: ADAPT** (small).

### 14. Chubb Neglected Software Exploit

- **Source.** Chubb Cyber ERM. Prior reports 03 and 04 describe it as 45 days of full cover, then a gradual shift of risk to the insured. Its percentages were not confirmed, so don't quote any.
- **Fit.** Harborline's KEV rule (III.1.7) is narrower and clearer, and graduated steps are already planned (T2-7 and row 12 of the synthesis).
- **Verdict: SKIP** as a new item. Harborline already has it.

### 15. Coalition Enhanced Business Recovery (August 2026)

- **What it is.** Key Customer Coverage, Rapid Review (one neutral forensic accountant), Cashflow Lifeline (an early cash advance) and a shorter MDR waiting period.
- **Evidence.** [Coalition](https://www.coalitioninc.com/announcements/coalition-unveils-enhanced-business-recovery-endorsements); [IA Magazine, Aug 17, 2026](https://www.iamagazine.com/2026/08/17/coalition-releases-enhanced-business-recovery-endorsements/) (search-snippet).
- **Fit.** Harborline already has all four: S, V.7.5, V.7.4 and the MDR 4-hour wait. Its advance is **firm**, while Coalition's is described as "discretionary" (prior report 02).
- **Verdict: SKIP** as new. Use it as evidence in the rationale that the design matches the 2026 market.

### 16. Vanishing retention; pre-claim assistance

- **Source.** Coalition: vanishing retention of −25%, −50%, then −100% by year 3, conditional on fixing critical vulnerabilities (prior report 03), and pre-claims assistance (prior report 02).
- **Fit.** Harborline has both: V.6.1 and V.2.3. The planned fixes are T2-8 and T2-16.
- **Verdict: SKIP** as new.

### 17. Contingent bodily injury and property damage wrap

- **Source.** Crum & Forster **Simple Cyber Version 6.0** (September 4, 2025; about 15 pages). It is designed to "wrap around" the insured's P&C program and gives **full limits for contingent bodily injury and property damage** from a cyber event, plus bricking and reputational loss.
- **Evidence.** [C&F product page](https://www.cfins.com/property-casualty/cyber-insurance/simple-cyber-policy/) (search-snippet); [v6.0 specimen](https://www.cfins.com/wp-content/uploads/2021/05/Simple-Cyber-General-v6-2025.09.04.pdf) (catalog note; blocked).
- **Fit.** It is valuable for manufacturers, clinics and restaurants in the $1M–$50M band, whose GL and property policies now carry cyber exclusions. It is not needed for Cedar Ridge. It conflicts with Harborline's exclusion 1 and would need a GL-coordination clause.
- **Verdict: OPTIONAL**, as a later endorsement for non-office classes.

### 18. Embedded / BOP cyber

- **Sources.**
  - **HSB Cyber Suite:** BOP-embedded, $50K–$1M limits, sold through mutuals and regionals (catalog notes). Cal Mutual's "Cyber Suite 2.0" brochure is dated October 2025.
  - **The Hartford CyberChoice First Response:** nationwide except AK, LA and VT, quoted alongside the Spectrum BOP on ICON. It offers system-failure and administrative-error options and post-incident remediation. [Hartford release, Dec 2025](https://ir.thehartford.com/news/news-details/2025/The-Hartford-Bolsters-Cyber-Insurance-for-Small-Businesses/default.aspx) (search-snippet).
  - **Chubb Studio Connect** small-business cyber and **Beazley** breach-response endorsement solutions (catalog notes).
- **Fit.** This is a distribution idea for Corgi's admitted carrier (a Harborline companion quoted with a BOP), not a clause. The clause needed, coordinating with a BOP data-compromise sublimit, is already planned (W-30, W-43).
- **Verdict: OPTIONAL.**

### 19. Warranty plus insurance

- **Source.** Cysurance: a vendor warranty plus a discounted insurance program (Protect360 via Amwins), with "no application or underwriting required" for certified solutions (prior report 02; [Cysurance](https://www.cysurance.com/services/), search-snippet).
- **Why skip.**
  - A warranty is the vendor's promise about its product. Bundling it on admitted paper raises service-contract and rebating questions.
  - "No underwriting" conflicts with Harborline's verified-controls model.
  - The only useful lesson is already covered by W-30 and W-43: a vendor warranty payment shouldn't reduce Harborline's payment except to avoid double recovery.
- **Verdict: SKIP.**

### 20. Public-entity pools, affinity programs and security grants

- **Sources.**
  - Public-entity pools buy cyber excess over a pooled primary. Great American writes up to $10M over pool primaries ([Great American](https://www.greatamericaninsurancegroup.com/about-us/business-operations/product/cyber-risk/public-entity-risk-pools), search-snippet).
  - Munich Re Specialty is funding **cybersecurity grant programs**, vulnerability management and tabletop exercises for public entities in 2026 ([Munich Re](https://www.munichre.com/specialty/north-america/en/insights/cyber-and-technology/cyber-losses-public-entities-face-cyber-risk.html), search-snippet).
- **Fit.** Two ideas transfer:
  - **Affinity programs**, for example through a state CPA society. They give group-level services and let Harborline watch vendor concentration across a vertical book, the tax-season risk named in Tier 6.
  - **Pre-loss security grants**, delivered as SB25-058 value-added services (idea 8).

  Neither needs policy text.
- **Verdict: OPTIONAL** (distribution).

---

## 3. How the admitted forms solve Harborline's Tier 2 drafting problems

| Tier 2 problem | What admitted or bureau forms do (evidence) | Harborline's planned fix | What to take |
| --- | --- | --- | --- |
| **Cloud accounts vs dependent systems** (T2-0 / W-01) | Nothing was verified in HSB, ISO or AAIS text. Background knowledge: older Beazley BBR forms bring third-party hosting under written contract into "computer systems"; At-Bay uses "External Computer Systems" (prior report 02, from the issued policy). HSB's "computer attack" is aimed at systems the insured owns, leases or operates (background; not verified) | W-01: define **cloud accounts** as yours, remove them from **dependent systems**, and route a provider's own bug to P | Keep W-01. Add the vendor-side-attack tie-breaker (idea 4, draft 4.4). Evidence is weak here, so don't claim an admitted-form precedent |
| **Fraud paths and who can be deceived** (T2-1, T2-1a / W-02, W-03, W-12) | **HSB CSC 02-2025:** "wrongful transfer event" means deception of **the insured or its financial institution** by a non-employee, via email, fax or phone; per-event sublimit within the annual aggregate (search-snippet) | W-02 adds a separate **bank impersonation fraud**; W-03 rewrites item 3 of **fraudulent instruction** | **Merge them into one "payment fraud" definition** (draft 4.1). Don't copy HSB's non-employee limit or channel list |
| **Related incident and claim linkage** (T2-1c / W-06) | **ISO CY 00 02 11 21:** related events are one event, discovered in the **earliest** period in which any part was discovered (search-snippet, hedged) | W-06: an incident report locks in later claims, a "related" test, and one retention | **Add the first-party deemed-discovery rule, with a continuity carve-out for other insurers** (draft 4.3) |
| **Carve-back language** (T2-1g / W-14) | Not verified in any admitted text this session. Background: bureau forms put exceptions inside each exclusion. Courts commonly hold that an exception to an exclusion does not itself grant coverage | W-14: "that exclusion does not remove coverage… coverage still depends on the insuring agreements" | W-14 matches common practice; **nothing new to add**. Also decide whether the IV.1 box is operative (W-35) |
| **Per-period sublimits** (T2-1e / W-08) | **HSB:** per-event sublimit within the annual aggregate. **ISO:** a limit for each insuring agreement under the aggregate. ***CiCi v. HSB* (Feb 23, 2026):** a cross-coverage cap that doesn't say it applies across coverages won't be enforced that way (search-snippet) | W-08: label every Item 6 limit as per period; T2-3 caps system failure over D and F; T2-6 narrows the ransomware coinsurance | **Adopt a two-column limits map and an express "applies across coverages" rule** (draft 4.2) |
| **Suspected incidents** (T2-1f / W-09) | Nothing verified. Background: data-compromise forms generally trigger on an actual compromise, not a suspected one (not verified) | W-09: a reasonably suspected incident qualifies for A and B even if nothing is found | W-09 appears **more generous than what I could verify**. Keep it, and add "including the cost of finding out that no **incident** happened" to B's forensic item |

---

## 4. Harborline drafts for ADOPT and ADAPT items

Every block below is labelled "Harborline draft". Bold words are defined terms, existing or new. "Conflicts" lists the clauses and planned fixes each draft touches.

### 4.1 Payment fraud (idea 1): ADAPT

**Where it goes.** Section II. It replaces **fraudulent instruction** and W-02's proposed **bank impersonation fraud**. Section I H.1, the **incident** definition and III.6 also change.

> **Harborline draft**
>
> **Payment fraud** means a deliberate deception, by any means of communication (including email, text, messaging app, letter, phone or video call, and synthetic or deepfake audio or video), by anyone acting against your interests, that:
> 1. leads you, or a **financial institution** that holds your accounts or **client accounts**, to transfer money or securities, or to change payment or bank details that are then used for a transfer; and
> 2. causes you a direct loss, or a loss you must make good to a client.
>
> In this definition, "you" means the **named insured** acting through anyone authorized to make, approve or change its payments, including an **executive**, **employee**, individual independent contractor, or an **AI agent** acting within its authority.
>
> **Financial institution** means a bank, credit union, payroll or payment processor, broker-dealer or similar institution that holds or moves money or securities for you or your clients.
>
> H.1 (replacement): "**funds transfer loss** you incur because of **payment fraud** or **computer fraud**."

**Conflicts and flags.**
- **Replaces two planned fixes.** It supersedes W-02's separate **bank impersonation fraud** and W-03's item-3 rewrite. Pick one approach. This one is shorter and mirrors a filed admitted structure.
- **Keeps W-02's other parts.** Keep **client accounts**, the altered-batch wording in **computer fraud**, and "resulting from".
- **III.6 and W-12.** The $100K lower limit should apply only when **you** (not your bank) acted on an unverified request. State that it never applies when the deceived party is the **financial institution**.
- **Rogue insiders.** "Anyone acting against your interests" keeps insider-perpetrated fraud in scope, which HSB leaves out. Exclusion 4 (as fixed by W-04 and W-13) applies to the insider personally. V.9 already makes H excess of crime or fidelity cover, so a crime policy responds first.
- **Consequential edits.** Update the **incident** list, Item 6 H's plain-English column, Coverage R, Item 7's callback row and application 5.2–5.3.

### 4.2 Limits map and express cross-coverage caps (idea 2): ADOPT

**Where it goes.** The Item 6 heading and table, and Section III.1 (new items 1a and 1b). It uses W-08's per-period rule and adds a per-incident column.

> **Harborline draft**
>
> **1a. How the limits in Item 6 work.** Each limit in Item 6 shows two amounts: the most we will pay for any one **incident**, including every **claim** arising from it, and the most we will pay for all **incidents** in the **policy period**. Both are part of, and not in addition to, the policy aggregate limit in Item 4, unless Item 6 says "in addition".
>
> **1b. Caps that apply across coverages.** A limit marked "applies across coverages" in Item 6 is the most we will pay for that kind of loss under all coverages combined, whichever coverage or coverages the loss falls under. These caps are:
> (a) the **system failure** limit, which caps **business income loss**, **extra expense** and **restoration costs** caused by a **system failure**, under Coverages D and F combined;
> (b) the ransomware coinsurance in part 1.6, which applies only to **restoration costs** and **business income loss** under Coverages D and F caused by ransomware encrypting or locking your **computer systems**; and
> (c) if purchased, the Fast Downtime Payment limit and the widespread-outage limit in Coverage T.
>
> A limit not marked "applies across coverages" limits only the coverage it appears next to.

**Declarations sketch (Item 6, illustrative for Cedar Ridge).**

| Coverage | Each incident | Policy period total | Applies across coverages? |
| --- | --- | --- | --- |
| B, C, F, I, J, L | $1,000,000 | $1,000,000 | No |
| D (attacks) | $1,000,000 | $1,000,000 | No |
| System failure (D and F) | $250,000 | $250,000 | **Yes** |
| E | $500,000 | $500,000 | No |
| H (with callback) | $250,000 | $250,000 | No |
| K | $250,000 | $250,000 | No |
| M / N / O | $100K / $100K / $50K | same | No |
| A (in addition to the aggregate) | $25,000 | [$75,000] (T2-8) | No |

**Conflicts and flags.**
- **Builds on W-08 and implements the T2-3 and T2-6 decisions.** The per-incident column is new. For most lines it equals the period total, so the column mainly makes the choice visible.
- **Proof-of-loss help.** Decide W-08's open question: does the $50K proof-of-loss help erode a sublimit? My suggestion is no, it erodes only the aggregate.
- **Ransomware.** Define "ransomware" once (T2-6) so that 1b(b) has a defined trigger.

### 4.3 Related incidents and the earliest period (idea 3): ADOPT

**Where it goes.** Section III.1 (new item 3a), next to W-06's rewritten III.1.3 and V.1.4. It reuses W-06's "related" test.

> **Harborline draft**
>
> **3a. Related incidents are one incident.** **Incidents** are related if they share a common cause, involve the same attacker's continuing access, or form a causally connected series. Related **incidents**, and every **claim** arising from them, are one **incident**. That **incident** is treated as first **discovered** on the date the earliest of them was first **discovered**, and as reported on the date the first of them was reported to us.
>
> **Which policy responds.** If that date falls in an earlier policy period of a policy we issued to you, that policy responds, with one limit and one **retention**, and this policy does not. If the earlier policy was issued by another insurer, this policy still responds to the related **incidents** first **discovered** during this **policy period**, less anything that other insurer pays for them.

**Conflicts and flags.**
- **Needs W-18.** Depends on W-18's definition of **discover**.
- **Matches W-06's exclusion 2 fix.** "Reported under an earlier policy that covers it" lines up with the continuity carve-out.
- **Trade-off to state.** One limit per campaign means a long campaign found in year 1 can exhaust year 1's limit, and year 2's fresh limit won't help. That is the market (ISO) position. Say so in the rationale.
- **Other insurers.** The carve-out stops a new customer being stranded between Harborline and a prior carrier that uses a different trigger.

### 4.4 Cloud-account tie-breaker for vendor-side attacks (idea 4): ADAPT

**Where it goes.** Section II, a sentence added to W-01's **cloud accounts** definition.

> **Harborline draft**
>
> If an attack on a **dependent provider's** systems gives someone unauthorized access to, or damages, encrypts or exposes data in, your **cloud accounts**, we treat it as a **security failure** affecting your **computer systems** for Coverages B, C, F and H. Any interruption caused by the provider's service being unavailable is covered under Coverage E (or Coverage P for a **system failure**), not Coverage D.

**Conflicts and flags.**
- **Two routes stay separate.** It builds on W-01 and keeps W-01's route for a provider's own bug (P).
- **No double recovery.** It doesn't overlap the **privacy event** definition, which already covers data "while a **dependent provider** holds it for you". Where both apply, say the loss is paid once (Part 5 item 4 of report 07, non-duplication).

### 4.5 Fast Downtime Payment (idea 5): ADAPT, optional Coverage T

The full clause and how it sits next to the aggregate are in **section 5**.

### 4.6 Widespread-outage cap (idea 6): ADAPT, for Coverage T and P only

**Where it goes.** A new Section II definition, applied in Coverage T and in P's Item 6 row.

> **Harborline draft**
>
> **Widespread outage** means an outage of a **named cloud service** or other **dependent provider's** service, or of widely used software, that at the same time interrupts many organizations that have no business relationship with each other. We decide this from the provider's own public status reports, the **outage monitor**, or a public alert from the U.S. Cybersecurity and Infrastructure Security Agency. It applies only to Coverage T and, if purchased, Coverage P. It never limits Coverages D, E or F.

**Conflicts and flags.**
- **Follows T2-3.** The core promise on attacks against your own systems is untouched.
- **A trap in exclusion 12.** The AWS outage of October 2025 is widely reported to have started with a DNS resolution fault inside AWS (background knowledge). Exclusion 12's "core internet infrastructure (such as the domain name system)" could be read to exclude it. T2-4 should limit exclusion 12 to **public** DNS root, top-level-domain and backbone infrastructure, not a provider's internal systems.

### 4.7 Limit reinstatement (idea 7): ADAPT, optional Coverage U

The full clause is in **section 5**.

### 4.8 Security services outside the contract (idea 8): ADAPT

**Where it goes.** Section V, new part 12 ("Security services we offer"). The services themselves go in a separate services guide, not in the policy.

> **Harborline draft**
>
> **12. Security services we offer.** We may offer you security tools and services, such as vulnerability alerts, phishing training, email security or managed detection and response, free or at a reduced cost. They are not part of this policy's coverage. We offer them on the same terms to every policyholder in the same risk class.
> 1. **They never reduce your cover.** Using them, choosing not to, or a failure of any of them is never a reason for us to deny or reduce payment under this policy. The only exception is the known-exploited-vulnerability rule in Section III, part 1.7, when our written notice under that rule was sent to your security contact.
> 2. **What we provide counts as verified.** A control we provide or monitor for you counts as verified for the credits in Item 7 for as long as we provide it.

**Conflicts and flags.**
- **Rebating.** SB25-058 covers only services "**not specified in the insurance policy**". The clause names services generically so that it doesn't "specify" them. Counsel should confirm this reading. If the services are treated as specified, they become coverage and need form and rate filing.
- **Scan estoppel.** It fits T2-7 (remove scan results from the "application" definition). It needs the KEV notice mechanics fixed first (W-22: notice to whom).
- **Insurer liability.** If a Harborline-provided MDR fails, the insured's claim against Harborline sits in the service contract, not the policy. Flag this for reinsurers and E&O.

### 4.9 $0-retention path with qualifying MDR (idea 9): ADAPT, optional tier

**Where it goes.** A new row in Item 7 and a new Section III.1 item 5a.

> **Harborline draft**
>
> **5a. Zero retention with qualifying MDR.** If Item 7 shows that you have **qualifying MDR**, and you report an **incident** to us through any channel in Item 10 within 24 hours after your MDR provider first alerts you to it, your dollar **retention** for that **incident** is $0 under Coverages B, C and F. The **waiting period** still applies to business interruption. This replaces, and does not add to, the MDR retention credit in Item 7. [If Item 7 also shows qualifying email security, the same applies to Coverage H.]

**Conflicts and flags.**
- **Depends on T2-16.** It needs T2-16's definition of **qualifying MDR** and its one stacking rule. It also resolves the "would halve it" arithmetic for MDR users who report fast.
- **Claim-free reduction.** The claim-free reduction (V.6.1) is irrelevant where the retention is $0.
- **H retention.** Keep the 72-hour H retention rule for non-MDR insureds.

### 4.10 Deepfake and impersonation response (idea 10): ADAPT

**Where it goes.** A new core coverage (call it **W**; skip "V", which would read like Section V, and T and U are the new options) or a new item in Coverage B with its own Item 6 sublimit. New Section II definitions, and **impersonation event** added to the **incident** definition.

> **Harborline draft**
>
> **W. Impersonation Response.** We will pay **impersonation response costs** you incur because of an **impersonation event** first **discovered** during the **policy period**, up to the limit in Item 6. No **security failure** or **privacy event** is needed.
>
> **Impersonation event** means the publication or use, without your permission, of synthetic media (including deepfake audio or video), a lookalike website or internet domain, or a fake social media or messaging account, that falsely presents itself as you, or as an **executive** or **employee** speaking for you.
>
> **Impersonation response costs** means reasonable costs, incurred with our consent within 90 days after you **discover** an **impersonation event**, for:
> 1. an expert to analyze the content and report on whether it is fake;
> 2. lawyers to ask platforms, registrars and hosts to remove the content, website, domain or account;
> 3. public relations help; and
> 4. warning your clients about the impersonation.

**Suggested Item 6 terms.** $25,000 per policy period, with a $2,500 retention. This is judgment, not market data. Coalition's limit wasn't found.

**Conflicts and flags.**
- **Incident list.** Adding **impersonation event** to **incident** brings in Coverage A (72-hour help), reporting, aggregation and the claim-free rules. Check each one.
- **Not reputational harm.** N (reputational harm) stays tied to a **security failure** or **privacy event**. Don't extend lost-profit cover to impersonation without pricing it.
- **A further gap, not proposed here.** Clients who pay fake invoices from a lookalike domain, with no breach of the insured, fall outside H.2, which needs a **security failure**. Extending H.2 to **impersonation events** within H's shared limit is a real need for a CPA firm, but it adds fraud exposure. Treat it as a separate priced option.
- **Coverage L.** L (media) is unaffected: the fake is not your **media content**.

### 4.11 AI voluntary shutdown (idea 11): ADAPT

**Where it goes.** Section III.4, a new item 2a. Merge it with W-25's precautionary-shutdown fix.

> **Harborline draft**
>
> **2a. Switching off an AI agent.** If you suspend an **AI agent**, or the systems it runs on, because it is exceeding its authority, acting on instructions from someone other than you, or malfunctioning, and a reasonable business in your position would have done the same to limit harm, the resulting interruption is covered as if caused by:
> (a) a **security failure**, if someone other than you caused the behavior (for example, through hidden instructions in content the agent processed); or
> (b) a **system failure**, subject to its lower limit, in every other case.

**Conflicts and flags.**
- **Ties to T2-5 and W-57.** It matches T2-5's split between a hijacked agent (security failure) and an erring agent (system failure), and needs W-57's "authority" fix.
- **Limits map.** Under draft 4.2(a), case (b) sits inside the $250K system-failure cap.
- **AI regulatory defense (OPTIONAL, not drafted).** If offered, extend J by endorsement to regulatory proceedings under AI-specific laws (e.g., Colorado SB 26-189 from January 1, 2027). Pay defense, and penalties only where insurable, with a separate sublimit.

### 4.12 Court-attendance compensation (idea 12): ADAPT

**Where it goes.** Section III.7, a new item 6. Amend the **claim expenses** definition ("does not include your own staff's salaries or overhead, except under Section III, part 7.6").

> **Harborline draft**
>
> **6. Your time in court.** If we ask an **executive** or **employee** to attend a trial, hearing, arbitration, deposition or mediation in a covered **claim**, we will pay you $500 for each day or part of a day each person attends, up to $10,000 per **policy period**. These amounts are **claim expenses**.

**Conflicts and flags.**
- **Amounts are judgment.** The $500 a day and $10,000 cap are mine; TMHCC's amounts weren't found.
- **Erodes limits.** Because these are **claim expenses**, they reduce limits (Important notice 3).

### 4.13 Retention billed last (idea 13): ADAPT

**Where it goes.** Section I "Two promises", appended to "We pay vendors directly", and Section III.1.3.

> **Harborline draft**
>
> We pay covered vendors' invoices in full as they come due, including amounts that fall within your **retention**, and then bill you for your **retention**. You may pay it in up to six equal monthly installments without interest. If you don't pay it, we may deduct it from any later payment we owe you under this policy.

**Conflicts and flags.**
- **W-43 (retention mechanics).** Say that amounts paid this way still count as your **retention**.
- **Non-payment.** Unpaid retention isn't premium, so it can't ground cancellation under V.5.2 (which is limited to non-payment of premium and fraud). The set-off sentence is the only remedy.
- **V.10 recoveries.** Unchanged: recoveries still reimburse your **retention** first.

---

## 5. Fast Downtime Payment and per-event limits next to Harborline's aggregate

### 5.1 Coverage T: Fast Downtime Payment (optional)

> **Harborline draft**
>
> **T. Fast Downtime Payment.** If a **downtime trigger** first occurs during the **policy period**, we will pay you the hourly amount shown in Item 6 for each **covered downtime hour**, up to the per-event and policy-period limits shown there. You do not need to prove the amount of your loss. We will pay within 5 business days after the trigger is confirmed and you have met condition 3.
>
> **Downtime trigger** means either:
> 1. **Cloud trigger:** an outage of a **named cloud service**, in a region you use, that the **outage monitor** confirms lasted longer than the trigger threshold in Item 6, whatever its cause except war (exclusion 15); or
> 2. **Verified outage trigger:** an interruption of your **computer systems** caused by a **security failure**, that our incident response team confirms stopped your core operations for longer than the trigger threshold in Item 6.
>
> **Named cloud service** means a service listed in Item 6, such as your email, file-storage, tax-preparation or payroll platform, with the provider and region you use.
>
> **Outage monitor** means the independent service named in Item 6 that measures the availability of **named cloud services**. Its measurements decide the cloud trigger, except for obvious error. You may ask for them to be reviewed under Section V, part 8.
>
> **Covered downtime hour** means each full hour of an outage that falls within your **business hours**, after the trigger threshold has passed, up to the maximum number of hours in Item 6.
>
> **Business hours** means 7 a.m. to 7 p.m., Monday to Saturday, local time at your address in Item 1, unless Item 6 shows other hours.
>
> **Conditions for Coverage T**
> 1. **Credit against your indemnity claim.** Any Fast Downtime Payment for an interruption is deducted from what we later pay under Coverages D, E or P for the same interruption. If your proven loss under those coverages is less than the Fast Downtime Payment, you keep the difference.
> 2. **Limits.** Fast Downtime Payments are part of the policy aggregate limit. They also count toward the limit of Coverage D, E or P for the same interruption.
> 3. **You must have been affected.** Within 30 days after the outage ends, tell us that it stopped you using the **named cloud service** or your **computer systems** for your operations, and give us any record we reasonably ask for, such as a provider notice, a log or a screenshot.
> 4. **One event.** Outages of the same service, or from the same **security failure**, that start within 72 hours of each other are one event.
> 5. **Widespread outages.** For a **widespread outage**, the most we will pay under Coverage T in the **policy period** is the widespread-outage limit in Item 6.
> 6. **Not covered:** planned maintenance announced at least 24 hours ahead, or an outage that began before the **policy period**.

### 5.2 Coverage U: Limit Reinstatement (optional)

> **Harborline draft**
>
> **U. Limit Reinstatement.** If covered payments for one **incident** reduce the policy aggregate limit, we will reinstate it once, up to the amount shown in Item 6, for later **incidents** that are not related to that **incident**.
> 1. **Which incidents it covers.** The reinstated limit applies only to **incidents** first **discovered** after the date our payments first reduced the aggregate limit, and to **claims** arising from them.
> 2. **What it never covers.** It never applies to: the first **incident**, or any **incident** or **claim** related to it; **system failure**; **widespread outages**; or Coverage T.
> 3. **Sublimits.** Each Item 6 sublimit is reinstated once in the same way, up to its original amount.
> 4. **Once only.** There is only one reinstatement in each **policy period**, including any extended reporting period.

### 5.3 How the pieces stack (Cedar Ridge illustration; every number is a Harborline judgment)

| Layer | What it pays | Unit | Cedar Ridge setting | Relationship to the aggregate |
| --- | --- | --- | --- | --- |
| A: Incident response | 72 hours of breach coach and triage | Each incident | $25,000 (and a per-period cap under T2-8) | In addition to the aggregate |
| **T: Fast Downtime Payment** | $ per covered hour after a trigger; no proof of loss | Per event / per period | **$1,000 per hour** (at most 50% of average revenue per business hour: $8.5M ÷ 3,744 business hours ≈ $2,270, so ≈ $1,135). **Threshold 8 hours**, the same as D's waiting period. **Up to 40 covered hours per event** ($40,000). **$80,000 per period**. **Widespread-outage limit $40,000 per period** | Inside the aggregate. Credited against D, E and P |
| D / E / P: indemnity BI | Proven lost profit and continuing expenses after the waiting period | Per incident / per period | D $1M (attacks), $250K system failure (across D and F); E $500K; P not bought | Inside the aggregate |
| V.7.4: cash advance | 50% of the estimated loss to date, within 10 business days | Per incident | Up to $250,000 (T2 suggests 25% of the aggregate) | An advance, not extra limit. **Calculate it net of any Fast Downtime Payment** |
| **U: Limit Reinstatement** | Refills the aggregate once for later, unrelated incidents | Once per period | $1,000,000, so at most $2M per period | Adds to the aggregate for later incidents only |

**Why the threshold matches the 8-hour waiting period.** The benefit of T is **speed and certainty of cash**, not a shorter wait. A lower threshold (AIG uses 2 hours for larger buyers) would pay for frequent short blips. It would also price T out of a $5,508 policy.

**Worked examples.**

1. **Tax-platform bug, March. P not bought.**
   - The outage runs from Tuesday 09:00 to Thursday 12:00. The threshold passes at Tuesday 17:00.
   - Covered hours: Tuesday 17–19 (2), Wednesday 07–19 (12) and Thursday 07–12 (5), a total of **19 hours**.
   - Payment: **$19,000**, within 5 business days.
   - D doesn't apply: under W-01, a vendor bug is a system failure at a dependent provider. P wasn't bought, so no indemnity follows. The $19,000 reduces the aggregate to $981,000.
   - *If P had been bought* and proven BI was $32,000, P would pay $32,000 − $19,000 = **$13,000**.
2. **Ransomware on the firm's own systems, 6 days down.**
   - Our IR team confirms the trigger at hour 8. T pays the 40-hour maximum, **$40,000**, within 5 business days.
   - Proven D loss is later $150,000, so D pays **$110,000** more. The cash advance is 50% of the estimate less the $40,000 already paid.
   - D's limit and the aggregate are reduced by $150,000 in total.
3. **Two unrelated attacks with Coverage U.**
   - In March, ransomware followed by a class action uses the full $1,000,000.
   - In August, an unrelated BEC loses $180,000. Without U, nothing is left. With U, the aggregate is refilled once, and H pays $180,000 less the retention ($2,500 if reported within 72 hours).
   - Any claim related to the March attack stays capped at the original $1M.

### 5.4 Accumulation controls

| Control | Where | Why |
| --- | --- | --- |
| Named services and regions only, listed at bind (add an application question on critical SaaS and cloud regions) | Item 6; definition of **named cloud service** | Lets you count exposure by provider and region |
| Hourly amount capped at 50% of average revenue per business hour | Item 6 rating rule | Limits over-insurance and moral hazard, and keeps T indemnity-like for filing |
| 8-hour threshold; 40 covered hours per event; business hours only | Item 6; definitions | Most cloud outages are short. The cap turns T into severity cover, not nuisance cover |
| Per-period and widespread-outage limits | Coverage T conditions 2 and 5 | Nearly every cloud-trigger event is widespread by nature, so the widespread limit is the effective cloud-trigger cap |
| Credit against indemnity | Coverage T condition 1 | For an event that also triggers D, E or P, T adds speed, not extra loss. The net extra cost is the waiting-period and short-outage layer |
| Seasonal concentration: CPA firms share a few tax and payroll platforms | Underwriting (Tier 6 accumulation note) | Cap total T exposure per platform in February to April, or add a seasonal load |
| Reinsurance of the parametric layer | Insurer side, not policy text | A Cumulus Re-style cloud-outage cover exists (Parametrix placed $35M of retrocession for Hannover Re for 2026–27) |
| **Considered and rejected:** a portfolio-wide pro-rata clause ("if payments to all policyholders exceed $X we reduce each one") | — | It undercuts the certainty that is the product's whole point, and invites objection at filing on admitted paper |
| U excludes system failure, widespread outages, T and related incidents | Coverage U item 2 | Keeps the reinstatement a frequency cover for independent attacks, not a systemic add-on |

### 5.5 Filing and legal notes (for counsel)

- **Is a parametric payment insurance?** Condition 3 (you were actually affected) and the hourly cap tied to revenue keep T tied to a real loss and an insurable interest. Admitted filing will still need an actuarial memorandum using the monitor's outage history. I have not estimated T's price. Each expected covered hour a year costs $1,000, so outage frequency at an 8-hour threshold decides whether T is affordable.
- **The monitor's data decides the cloud trigger.** The "obvious error" exception and access to V.8 review keep that from being unreviewable.
- **Other insurance.** Say in V.9 that T pays first and is not reduced by any other insurance.
- **Coverage U.** It needs a rate for the chance of a second, independent severe incident. At-Bay's finding that firms hit once are twice as likely to be hit again within two years (prior report 02) is the starting point. The load is a judgment and is not given here.
- **Per-incident framing.** You can present U the way Brit presents per-event limits, as "each incident $1M; policy period total $2M". The two are economically the same, and the per-incident framing reads better in the Declarations.

---

## 6. OPTIONAL and SKIP items: one-line reasons

- **Contingent bodily injury and property damage wrap (C&F): OPTIONAL.** Useful for non-office classes whose GL and property policies exclude cyber. Not needed for a CPA firm, and it would need GL-coordination wording and exclusion 1 changes.
- **Embedded / BOP cyber (HSB, Hartford, Chubb): OPTIONAL.** A distribution route for Corgi's admitted carrier. The policy-side coordination is already planned (W-30, W-43).
- **AI regulatory defense (Beazley): OPTIONAL.** Price it for AI deployers once Colorado SB 26-189 takes effect (January 1, 2027).
- **Pools and affinity programs: OPTIONAL.** Group services and concentration monitoring; security grants as SB25-058 services.
- **Reward expenses (TMHCC): SKIP.** Low SMB value.
- **Warranty plus insurance (Cysurance): SKIP.** Warranty regulation, and "no underwriting" doesn't fit a verified-controls design.
- **Chubb NSE, Coalition EBR, vanishing retention, pre-claim help: SKIP as new.** Harborline already has them; the planned fixes cover the gaps (T2-7, T2-8, T2-16).
- **Uncapped "any one claim" limits (Brit): SKIP in favor of U.** Unlimited frequency is hard to rate and file admitted, and a systemic event could hit a whole vertical book repeatedly.

---

## 7. Verify before you quote anything

1. **HSB CSC 02-2025.** The "wrongful transfer event" definition, its channel list, the non-employee condition and the per-event sublimit language. Open the Heartland PDF.
2. ***CiCi Enterprises v. HSB Specialty*** (N.D. Tex., Feb 23, 2026). Get the reporter or docket citation, the exact endorsement wording, and whether it was appealed.
3. **ISO CY 00 02 11 21.** The related-events and "earliest policy period" rule. The snippet said "will likely", so check with a licensee.
4. **AIG/Parametrix.** The launch terms (2-hour wait, tiers, regions) and whether the product is written admitted or surplus lines in the US.
5. **LMA SME cyber wording.** Whether it was published after May 2026, and how the per-hour payment is structured.
6. **Brit C360.** The limit mechanics (is there an overall cap?) and what the £250M figure refers to.
7. **Colorado SB25-058.** The exact conditions (reasonable cost, non-discrimination, disclosure), its effective date, and whether services named generically in a policy count as "specified".
8. **Coalition Deepfake Response Endorsement limits, and Beazley's September 2026 endorsement names and terms.**
9. **AWS October 20, 2025 root cause (DNS)**, before relying on the exclusion 12 point in 4.6.
10. **Background-knowledge items.** Beazley BBR's hosted-systems definition and HSB's "computer attack" scope. Don't cite either without opening the forms.

---

## 8. Sources

**Search-snippet, run Sept 27, 2026 (20 searches):**
- HSB Cyber Suite CSC 02-2025 (Heartland PDF, title and excerpts): https://heartlandmutualinsurance.com/wp-content/uploads/2024/12/Cyber-Suite-Coverage-Form-CSC-02-2025.pdf
- HSB wrongful transfer event (summary of HSB Cyber Suite materials): https://www.pianational.org/docs/default-source/products/west-bend_cyber-suite-coverage_wb-2827.pdf ; https://www.gny.com/sites/default/files/file/2024-12/CyberSuite_Coverage_GNY.pdf ; https://www.acuity.com/the-focus/agent/acuitys-newest-cyber-coverages
- *CiCi Enterprises v. HSB Specialty* (N.D. Tex., Feb 23, 2026): https://www.hunton.com/hunton-insurance-recovery-blog/court-refuses-to-slice-up-cicis-cyber-extortion-coverage ; https://www.insurancebusinessmag.com/us/news/cyber/court-blocks-hsbs-ransomware-sublimit-in-firstofitskind-cyber-ruling-567006.aspx ; https://www.phelps.com/insights/drafting-ransomware-sublimits-that-hold-up-what-insurers-can-learn-from-cici-enterprises.html
- ISO CY 00 02 11 21: https://www.insurancexdate.com/insurance-forms/CY/CY-00-02/ ; https://www.law.com/insurance-coverage-law-center/2021/07/26/iso-commercial-cyber-product-replaced-part-one-cy-00-03-11-21-sections-i-iv-423-117619/ ; https://www.propertycasualty360.com/fcs/2021/08/08/iso-commercial-cyber-product-replaced-part-one-cy-00-03-11-21-sections-i-iv/
- AAIS (no cyber form found): https://aaisviews.aaisonline.com/aais-views/tag/cyber
- Crum & Forster Simple Cyber: https://www.cfins.com/property-casualty/cyber-insurance/simple-cyber-policy/
- Chubb Widespread Event: https://www.chubb.com/content/dam/chubb-sites/chubb-com/au-en/business/cyber-insurance/documents/pdf/erm-v2-2-e13-widespread-event-endorsement.pdf ; https://www.chubb.com/au-en/articles/business/a-better-way-to-define-and-insure-systemic-cyber-events.html
- AIG / Parametrix (Aug 13, 2026); AWS payout (Oct 2025); Cumulus Re III: https://www.theinsurer.com/cyber-risk/news/aig-launches-parametric-cloud-outage-solution-backed-by-parametrixs-monitoring-2026-08-13/ ; https://www.artemis.bm/news/aig-launches-parametric-cloud-outage-insurance-working-with-parametrix/ ; https://www.artemis.bm/news/parametrix-pays-claims-swiftly-after-aws-outage-triggers-parametric-policies/ ; https://www.insurancebusinessmag.com/reinsurance/news/breaking-news/parametrix-issues-largest-cumulus-re-cat-bond-for-cloud-risks-571189.aspx
- LMA: https://www.theinsurer.com/ti/news/lma-gives-details-on-incoming-standardised-cyber-wordings-for-uk-sme-market-2026-05-21/ ; https://lmalloyds.com/lma-launches-new-sme-property-and-business-interruption-model-wording/ (June 30, 2026) ; https://mgaa.co.uk/parametric-solutions-in-cyber-on-the-up-as-sme-coverage-needs-grow/
- Brit C360 (Mar 2026): https://www.britinsurance.com/news/brit-launches-new-cyber-product-for-smes ; https://www.insurancebusinessmag.com/uk/news/cyber/brit-targets-sme-cyber-gap-with-new-any-one-claim-product-569152.aspx ; https://www.cirmagazine.com/cir/c2026031901.php
- CFC unlimited reinstatements (July 2024): https://www.cfc.com/en-us/knowledge/resources/articles/2024/07/cyber-coverage-highlights-unlimited-reinstatements/
- Stoïk: https://docs.stoik.io/onboarding/why-do-insurees-have-a-stoik-protect-account ; https://www.stoik.com/en-us/insurance
- Public-entity pools: https://www.greatamericaninsurancegroup.com/about-us/business-operations/product/cyber-risk/public-entity-risk-pools ; https://www.munichre.com/specialty/north-america/en/insights/cyber-and-technology/cyber-losses-public-entities-face-cyber-risk.html
- Coalition EBR (Aug 2026) and Deepfake Response (Dec 2025): https://www.coalitioninc.com/announcements/coalition-unveils-enhanced-business-recovery-endorsements ; https://www.iamagazine.com/2026/08/17/coalition-releases-enhanced-business-recovery-endorsements/ ; https://www.coalitioninc.com/announcements/coalition-adds-deepfake-response-endorsement ; https://siliconangle.com/2025/12/09/coalition-expands-cyber-insurance-cover-deepfake-driven-reputation-attacks/
- The Hartford CyberChoice First Response (Dec 2025): https://ir.thehartford.com/news/news-details/2025/The-Hartford-Bolsters-Cyber-Insurance-for-Small-Businesses/default.aspx ; https://www.iamagazine.com/2025/12/08/the-hartford-bolsters-cyber-insurance-for-small-businesses/
- Tokio Marine HCC: https://www.tmhcc.com/en-us/products/cyber-and-tech/cyber-netguard-plus ; https://www.tmhcc.com/en-us/products/cyber-and-tech/cyber-for-healthcare
- Travelers CyberRisk and Cyber Risk Services: https://www.travelers.com/business-insurance/cyber-insurance/cyberrisk ; https://sustainability.travelers.com/drivers-of-sustained-value/cybersecurity/cyber-product-offerings
- Colorado SB25-058: https://leg.colorado.gov/bills/sb25-058 ; https://content.leg.colorado.gov/sites/default/files/documents/2025A/bills/sl/2025a_sl_084.pdf

**Catalog notes** (`catalog/cyber_policies.csv`): HSB CSC 02-2025 (Heartland); HSB Cyber Suite 2.0 brochure (Cal Mutual, 2025-10); C&F Simple Cyber v6.0 (2025-09-04) and MCM v6; ISO CY 00 02 11 21, CY 00 01 01 18, CY 00 03 and CY 00 10; Hiscox CyberClear admitted CYBCL-CYB P0001A CW (10/2019) and the CyberClear Academy factsheet; TMHCC NGP 1000 (04/2020), NGP-RNA (08/2025) and the broad-appetite sheet (12/2025); Hartford CyberChoice and Spectrum BOP pages; Travelers CYB-16001 CW and CYB-14306; Chubb PF-48169 (02/19) and Studio Connect; Cowbell Prime 100 (11/22); Beazley BBR 5.0 F00653 (02/2025 per snippet) and the BBR 5.0 changes summary; Coalition Active Cyber Policy issued copies; Elpha Secure sample policy.

**Prior reports in this folder:** 02 (Coalition, At-Bay, Cowbell, Elpha, Cysurance); 03 and 04 (Chubb NSE and Widespread Event, including PF-54815 (06/21)); 09 (LMA draft, Brit, Beazley September 2026 AI endorsements).

**Background knowledge (not verified this session):** the Beazley BBR hosted-systems definition; HSB "computer attack" scope; courts' treatment of exceptions to exclusions; the AWS October 2025 DNS root cause.
