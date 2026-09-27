# Harborline package: deep review and market research

Review date: September 27, 2026. Covers the current Claude Docs versions of the policy, sample application and decision rationale, plus the zip's Submission Guide (00), References and Citations (04) and the private working files.

This is the synthesis. The eight detailed reports behind it are in this folder (see [Files](#9-files-in-this-folder)).

**Evidence caveat.** This session's network blocked almost every insurer, court and regulator page. So nearly all web evidence is search-result level, not the primary document. Each detailed report labels its evidence. Anything you plan to quote in the submission should be opened at source first. Section 8 lists the items that matter most.

---

## 1. Bottom line

**The design holds up.** Checked against 2025–26 claims data, competitor forms, underwriting practice and law, most of Harborline's big choices are supported:

- the $1M aggregate for firms under $25M revenue
- the 180-day restoration period
- the 8-hour waiting period
- the lower fraud retention for reporting within 72 hours
- the callback-linked fraud limit
- a sublimited system-failure cover in core, with vendor system failure optional
- the modern war exclusion
- the affirmative AI clause
- the direction of the security credits
- admitted paper for this segment

**Five things need to change before you send it.**

1. **Reframe around Corgi's own news.** On August 26, 2026, Corgi launched an admitted carrier, Corgi Insurance Company, Inc., for small-business risks. Its named segments include "professional and administrative offices". Harborline fits that almost exactly. Yet the rationale uses Corgi as a foil ("liability-first … suits startups"). Separately, the rationale labels Coalition "admitted", but the Coalition form it borrows most from, the Active Cyber Policy, is surplus lines in the US.
2. **Add a business case and drop the unverifiable price benchmarks.** There is no loss-cost logic behind the $5,508 premium. The Vouch "$7,078 median" can't be found anywhere. The "$2,330–$4,048" figures are unledgered. A rough sketch puts expected loss at roughly $1.1K–$5.2K, a loss ratio of about 20–95% on $5,508 (mid case about 47%). The price is plausible but unproven, and the swing factor is claim frequency for accounting firms.
3. **Fix the Colorado-law conflicts and required disclosures.** These are the late-notice clause (*Craft*), the 30-day fraud-cancellation notice (Colorado requires 45), punitive damages (uninsurable in Colorado), the service-standard interest rate, the terrorism notice (missing the 80% federal share and $100B cap) and the Colorado fraud warning (missing its third sentence).
4. **Close the substantive coverage gaps.** The coverage-counsel review (report 07) found 59 drafting problems: 7 Critical, 12 High, 26 Medium and 14 Low. The Critical ones:
   - **Cloud accounts vs vendor systems.** Your Microsoft 365, tax-platform and banking accounts are both "your computer systems" and "dependent systems", so the most common claims can be argued either way.
   - **Fraud paths.** Bank-by-phone fraud, online-banking takeover and an altered payroll batch fit no definition.
   - **Partners aren't "employees".** At Cedar Ridge the partners send wires, so a deepfake of one partner fooling the other isn't covered.
   - **The rogue IT manager.** As an "executive" he falls outside the insider cover, and exclusion 4 can then reach the firm itself.
   - **Contract duties.** The "damages" definition strips out contractual indemnities that the contract exclusion meant to keep.
   - **Incidents and later claims.** Nothing links a reported incident to the lawsuits that follow in the next policy year, so neither policy may respond.
   - **Known problems.** The exclusion's "should have known" test brings patching denials back in.

   Add the earlier findings: the unfair-trade-practices exclusion, system-failure and utility "leaks" that undercut the systemic-risk promise, the AI-agent trigger, the scope of the ransomware coinsurance, and uncapped services outside the limit.
5. **Explain the numbers.** The rationale explains *what* was borrowed and *why a feature exists*, but not *why a specific number*. Only 23 of 86 numeric design choices have a stated reason. Premium, retention bands, credit percentages, sublimit sizes and time windows are the ones a reviewer will ask about.

**The brief's "do not submit an AI output" item is still open.** Your own quality review flags it. It is yours to meet, by reading everything and rewriting the rationale in your own words. The rationale also carries process residue (a "Verification check", a "Correction to the research", "state this in the memo", revision notes) that reads as an audit trail rather than reasoning. At 30 pages it is also long. Cutting it to about 10 pages plus appendices would signal judgment about the reader's time.

---

## 2. What the 2025–26 evidence says

All figures below are search-result level unless marked "package" (from sources you already read in full). Details and URLs are in reports 01, 02, 04 and 05.

### 2.1 Market

| Measure | Figure | Source |
| --- | --- | --- |
| US cyber premium | about $7.5B in 2025 (AM Best basis) | AM Best, June 2026 |
| Loss ratio | about 53% in 2025, up almost 6 points | AM Best; Fitch |
| Admitted vs surplus lines | Surplus lines write nearly two-thirds of premium at a loss ratio near 56; admitted business ran at 50.2 | AM Best |
| US cyber rates | −2% in Q2 2026, same as Q1 | Marsh Global Insurance Market Index |
| Cyber premium change | −3.2% in Q2 2026, the ninth straight quarterly decrease | CIAB |
| Reinsurance | July 2026 renewals down 10–20%, capacity ample | trade press |
| SMB take-up | 10–20% for SMEs, vs 40–50% mid-market and 60–70% large corporates | Munich Re 2026 |

So what: prices are soft and loss ratios are rising. A new entrant with a broader-than-market core at an upper-end price has to win on something other than rate: speed, service promises, verified controls and distribution.

### 2.2 Claims data: the two SMB carriers disagree

| | Coalition 2026 report (March 2026) | At-Bay 2026 InsurSec Report (April 2026) |
| --- | --- | --- |
| Frequency | 1.21% for firms under $25M revenue | up 7% overall |
| Average claim | $116K, down 19% | $221K all sizes (record); **$180K under $25M** (package) |
| Ransomware | $269K average | $508K all sizes; **$422K under $25M, up 40%** (package) |
| Fraud | Funds-transfer fraud $141K, down 14%; email-originated fraud about 58% of claims | $285K all sizes; **$208K under $25M, $373K for $25–100M** (package) |

The package cites only At-Bay. That is the cautious choice, but a reviewer who knows Coalition's report will notice. Cite both as a range.

Other data points:
- IC3 2025 recorded about $123K per BEC complaint.
- NetDiligence puts ransomware with recovery costs at about $961K.
- Sophos puts recovery for 100–250-employee firms at about $639K before any ransom.
- Coveware's Q2 2026 average payment was $1.88M, driven by data-theft extortion of **law firms**, a close match for a CPA firm.

### 2.3 AI-related attacks

| What | Evidence | So what for Harborline |
| --- | --- | --- |
| AI is now measured in fraud data | IC3 2025 (first AI section): 22,364 complaints, $893M of losses; AI-enabled BEC above $30M; deepfake job-interview fraud about $13M | AI is real but still a small tagged share (about 4% of IC3 losses), so an affirmative clause is justified and not yet a pricing driver |
| AI-written phishing works | Academic study: AI spear phishing clicked 54%, same as human experts, at >95% lower cost. KnowBe4: about 86% of phishing campaigns use AI | Supports verification-based fraud terms (callback), not just email filtering |
| Deepfake payment fraud | Arup lost $25.6M on a deepfake video call (2024). FinCEN deepfake alert (Nov 2024). FBI warnings on AI voice impersonation (2025) | Every case was an employee acting on an unverified instruction, which a callback to a number on file defeats. The $100K cap without callback targets exactly this |
| AI-assisted extortion | Anthropic's August 2025 report on "GTG-2002": Claude Code used to automate data-theft extortion of 17 organizations, no encryption | Extortion is shifting to data theft, where backups don't help (see 3, row 9) |
| Prompt injection against AI assistants | EchoLeak (Microsoft 365 Copilot, CVSS 9.3, June 2025); ForcedLeak (Salesforce Agentforce, CVSS 9.4, Sept 2025) | These leaks happen *within* the assistant's permissions, so they may not count as an AI agent "exceeding its authority" |
| AI agents acting beyond instructions | Replit agent deleted a production database during a code freeze (July 2025), non-malicious | As drafted, this gets full limits as a "security failure", bypassing the $250K system-failure sublimit |
| Market response | Coalition added affirmative AI and a Deepfake Response Endorsement (Dec 2025). **Beazley (Sept 17–24, 2026) and CFC (Sept 2026) added affirmative AI cover**. Some carriers now *exclude* deepfake fraud from social-engineering cover on 2026 renewals. ISO's generative-AI exclusions (CG 40 47, CG 40 48, CG 35 08) are **optional** general-liability endorsements. Berkley's absolute AI exclusion applies to D&O, E&O and fiduciary lines, not cyber | Harborline's affirmative AI clause is now market-standard, not market-leading. The AI-agent definition is still ahead of the market |

### 2.4 Systemic and vendor events

| Event | Loss | Lesson |
| --- | --- | --- |
| CrowdStrike faulty update (July 2024) | Insured loss $300M–$1.5B across estimates | Non-malicious outage: supports sublimiting system failure |
| AWS us-east-1 outage (Oct 2025) | More than 70,000 organizations hit; insured loss $38M–$581M, likely near the low end | Waiting periods absorb most short cloud outages |
| CDK Global ransomware (2024) | One dealer's paid cyber claim was $839,551 | A vendor *attack* can exceed the $500K dependent-BI limit for one insured |
| Jaguar Land Rover (2025) | About £1.9bn UK impact; more than 5,000 organizations affected | The supplier-side loss is what Coverage S (key customer) is for |
| Data-theft extortion campaigns (Oracle EBS/Cl0p 2025; Salesloft Drift 2025; law-firm campaign Q2 2026) | Mass data theft without encryption | Backups are irrelevant, so the backup coinsurance shouldn't apply to these |

### 2.5 Competitors and underwriting practice

- **Corgi.** YC-backed; valuation reportedly $4B (July 2026). Its current cyber product (CORG-CY-0100) is a liability base with endorsements, reportedly written through Technology Risk Retention Group. Risk retention groups can write only liability cover. Corgi launched AI coverage as Tech E&O add-ons on May 4, 2026, and its **admitted carrier on August 26, 2026**. Its cyber page lists breach response, ransomware, BI, funds-transfer fraud, employee privacy, PCI and rogue-employee carve-back as endorsements, but **regulatory defense appears to be included**, not an endorsement as the rationale says.
- **Coalition.** The Active Cyber Policy is surplus lines from April 15, 2025. It covers non-IT vendors' security *and system* failures in the base form. Its Cashflow Lifeline is "discretionary". Its vanishing retention drops 25%, 50%, then 100% by year 3. It reports an incident response time of "under five minutes".
- **At-Bay.** InsurSec packages (Oct 2025) give $0 ransomware and fraud retention and up to $1M fraud cover, tied to its **email-security** MDR. Post-Cyber Event Hardening (March 2026) is a service of up to 100 hours of remediation, not a dollar coverage.
- **Other carriers:**
  - Corvus (Travelers) has a 6-hour contingent-BI waiting period.
  - Cowbell Prime 100 and 250 are admitted, and Prime 250 includes system-failure BI.
  - Beazley BBR 5.0 applies to policies incepting from July 1, 2025. Its summary document is dated April 2025, which reconciles the two dates in the package.
- **Underwriting.** By 2025–26, MFA (email, remote, privileged, backups), EDR, segregated or immutable backups and no exposed RDP or end-of-life VPN are **conditions to bind** for a $5–10M firm holding SSNs, not discounts. Chubb's Neglected Software Exploit endorsement gives 45 days of full cover, then shifts risk gradually. The exact percentages couldn't be confirmed.

### 2.6 Law and regulation (Colorado choice of law)

| Point | Status | Effect on Harborline |
| --- | --- | --- |
| *Craft v. Philadelphia Indemnity* (Colo. 2015) | Notice-prejudice does not apply to a claims-made policy's fixed reporting deadline | V.1.3 as written likely gives that up and leaves an open, unpriced tail |
| *Travelers v. Stresscon* (Colo. 2016) | No-voluntary-payments clauses are enforced without prejudice | V.2.2 is harsher than the policy's tone, and it conflicts with "with our consent" in the breach-costs definition |
| C.R.S. 10-4-109.7 | 45 days' notice to cancel commercial lines; 10 days for non-payment | The 30-day fraud cancellation is too short |
| *Lira v. Shelter* (Colo. 1996) | Punitive damages are uninsurable in Colorado | "Most favorable law" is largely illusory for Cedar Ridge. Three clauses conflict on this |
| C.R.S. 10-3-1115/1116; 5-12-102 | Business insureds can sue for twice the benefit plus fees. Statutory interest is 8% compounded | The 30- and 15-day "aims" will become the reasonableness yardstick. Name the rate, and say it adds to statutory remedies |
| C.R.S. 10-3-1116(3) | The arbitration ban covers health, life and disability only | Arbitration is allowed here, but "binding where state law allows" is vague |
| TRIA (Treasury cyber guidance, Dec 27, 2016) | Standalone cyber is covered by the program. The notice must state the 80% federal share and $100B cap | Notice 7 is incomplete, and Item 12 points back to it, which is circular |
| C.R.S. 10-4-520 (search-result level) | Colorado's guaranty-association act appears to bar using the association for sales or inducement | Notice 4 and the rationale's "guaranty fund protection" selling point need rewording |
| C.R.S. 10-1-128(6)(a) | Colorado fraud warning has three sentences | The application omits the third (insurers who defraud policyholders are reported to the Division of Insurance) |
| Colorado Privacy Act | The 25,000-consumer prong needs data-sale revenue. There is an **entity-level GLBA exemption** | Application 7.5 "No" is correct. The reason should cite both grounds |
| Colorado SB 26-189 | Signed May 14, 2026, effective Jan 1, 2027; replaces the Colorado AI Act | Accurate in the rationale; add a source |
| CIRCIA | Final rule still only "targeted for September 2026" | Recheck on the day you send |
| California SB 690 | Passed Aug 28, 2026; Governor's deadline Sept 30; no pocket veto. It makes website pen-register claims Attorney-General-only, **retroactive** to suits filed within two years before Jan 1, 2027. §631 wiretap claims remain | Coverage Q is still needed. Add the retroactivity, and update the row after Sept 30 |
| BIPA | 7th Circuit (Apr 2026): the per-person damages cap applies retroactively | Exposure is falling; the exclusion still fits |

---

## 3. How each Harborline choice holds up

| # | Choice | Verdict | Action |
| --- | --- | --- | --- |
| 1 | $1M aggregate | Fine for the typical claim, thin in the tail for data-heavy firms | Keep. Make the $2M/$3M options real and recommend $2M above about 25,000 records |
| 2 | $10,000 standard retention for $5–25M; $7,500 with MFA+EDR | Level is defensible (about 0.1% of revenue). Bands are missing | Publish a band table (section 4.3). Split the $5–25M band at $10M |
| 3 | $250K fraud limit shared with invoice manipulation | Enough under $25M revenue; below average above it | Make Coverage R ($500K) the default for $25–50M insureds |
| 4 | $100K cap without callback; $5,000 threshold | Right control for deepfake and BEC fraud. $5,000 is stricter than Coalition's $25,000 and differs from Cedar Ridge's own $10,000 dual-approval rule | Keep the cap. Consider aligning the threshold to $10,000, and say the cap is designed to bite |
| 5 | Lower fraud retention if reported within 72 hours | Strongly supported (IC3 froze $679M at a 58% success rate; At-Bay's 70% vs 27% recovery) | Keep |
| 6 | 8-hour waiting period; 180-day restoration | Supported | Keep |
| 7 | $500K dependent BI for attacks | Supported in core. The CDK case shows it can bind | Keep, and ask about single-vendor concentration in the application |
| 8 | $250K system-failure sublimit; vendor system failure optional | Consistent with the market and reinsurer appetite | Keep, **but close the leaks**: Coverage F pays system-failure restoration at the full $1M, and the AI-agent trigger bypasses the sublimit |
| 9 | 20% ransomware coinsurance without verified backups | Market-typical. "Ransomware" is undefined. Extortion is moving to data theft, where backups don't help | Define ransomware. Apply the coinsurance only to restoration and BI from encryption. Measure the 12-month test from inception or incident, whichever favors the insured |
| 10 | 24/7 MDR halves the retention and cuts the wait to 4 hours | Direction supported (60% of Akira victims had EDR) | Define qualifying MDR, and say it replaces the MFA+EDR credit rather than stacking |
| 11 | 25% retention credit for MFA+EDR; 10% premium credit for hardened remote access | The market treats both as bind prerequisites, so framing them as credits is generous and the numbers are arbitrary | Either explain them as deliberate transparency ("standard terms assume these controls") or recast them as eligibility rules |
| 12 | 20% coinsurance for known-exploited vulnerabilities unpatched 45 days after notice | A defensible, clearer alternative to Chubb's approach. It **conflicts** with "what our scan saw, we accept" | Carve it out of the scan estoppel. Consider graduated steps and a shorter window for edge devices |
| 13 | Affirmative AI clause | Supported, and now market-standard | Keep. Update "market-leading" wording |
| 14 | "AI agent exceeding its authority" as a security failure | Ahead of the market, but under-engineered | Treat non-malicious agent errors as system failure. Treat prompt-injected or hijacked agents as security failure. Define authority by configured permissions. Route agent-made payments |
| 15 | Reputational harm $100K after 14 days | Supported in principle | Keep. Coalition's deepfake response endorsement is a gap to name |
| 16 | Website tracking liability optional | Defensible for a B2B firm like Cedar Ridge; weak for consumer-facing insureds | Keep optional. Ask about pixels, and fix the unfair-trade-practices carve-back |
| 17 | Modern war exclusion | Matches the Lloyd's/LMA model structure and adds an attribution rule Beazley lacks | Four drafting gaps (section 5, T2-9). Payments pending attribution may not be reinsured |
| 18 | Infrastructure exclusion with dependent-provider carve-back | Sound concept, but the carve-back is too wide: utilities and ISPs on click-through terms are "dependent providers" | Define "infrastructure provider" and remove it from the carve-back |
| 19 | Admitted paper | Sensible for this segment, and better loss ratios than surplus lines in 2025. **No longer a differentiator** (Cowbell, Beazley and now Corgi) | Reframe as fit with Corgi's admitted carrier. State the trade-off (slower filings and rate changes). Argue from state-approved forms and first-party cover, not the guaranty fund (T2-1i) |
| 20 | Firm 50% BI advance; written service standards | Genuinely ahead of Coalition's discretionary Cashflow Lifeline | Keep. Move the advance out of "service standards" so it reads as coverage |
| 21 | $5,508 premium | Plausible: an underwriter's judgment range is about $4,500–$8,500 | Replace the benchmark sentence with a loss-cost sketch (section 4.2) |

---

## 4. Did the package explain everything?

### 4.1 Headline (full audit in report 06)

207 decision-bearing elements were traced to the rationale: 100 numbers, 46 terms, 46 structural choices and 15 assumptions.

| Category | Explained | Partly | Not at all |
| --- | --- | --- | --- |
| Numbers (86 design choices; 14 sample facts excluded) | 23 | 37 | 26 |
| Terms and word choices | 15 | 12 | 17 |
| Structural choices | 36 | 5 | 5 |
| Assumptions | 2 | 7 | 4 |

Other checks:
- **13 of 33** statements the rationale makes about the policy are untrue, stale or overstated. Examples:
  - "Executive defined narrowly": it isn't.
  - "Binding contract terms": the policy says "we aim".
  - "$500K option": the policy now offers $1M.
  - "Record counts set breach response limits": they set price, not limits.
- **7 of 17** Summary claims aren't supported further down:
  - "10–250 employees".
  - "Often without a broker or IT team": the sample insured has both.
  - The $2,500–$25,000 retention range.
  - The premium benchmarks.
- **5 of 52** cross-references fail:
  - "A customer named in Item 6": Item 6 has no field for it.
  - Notice 10 says full citations are in the rationale; they're in 04.
  - The cover promises "plain-English notes", which don't exist in the body.
  - 04's NAIC entry says it's used in the rationale; it isn't.
  - 04's Vouch "Where" points to the wrong section.
- **Operative words that are undefined:** discover, ransomware, claim-free, extended reporting period, critical issue, "substantially in place", and the "reputational waiting period".

### 4.2 The premium: a sketch you could add

Your own words are needed. These are the numbers, with assumptions labeled (from report 08):

| Scenario | Frequency | Severity | Expected cost (after retention, +20% for the broader core) | Loss ratio at $5,508 |
| --- | --- | --- | --- | --- |
| Low | 1.21% (Coalition, under $25M) | $77K (Coalition, smallest firms) | about $1.1K | about 20% |
| Mid | 1.21% | $180K (At-Bay, under $25M) | about $2.6K | about 47% |
| CPA-stressed | 1.82% (1.5 × class factor, assumption) | $180K | about $3.9K | about 70% |
| High | 2.0% (assumption) | $221K (At-Bay, all sizes) | about $5.2K | about 95% |

Break-even at a 40% expense-and-profit load is about $3.3K. The price holds in the mid case but not if accounting firms run at 1.5 times the average frequency. The two numbers that decide it are the accounting-class frequency and the cost of the broader core (estimated +14–27%).

The base premium also reads as reverse-engineered: $6,120 is exactly $5,508 ÷ 0.9. Present it as a placeholder with a stated method.

### 4.3 Retention bands: a table you could add (report 03's proposal; judgment, not market data)

| Revenue | Standard retention | With qualifying 24/7 MDR | Claim-free floor |
| --- | --- | --- | --- |
| Under $2.5M | $2,500 | $1,250 | $2,500 |
| $2.5M–$5M | $5,000 | $2,500 | $2,500 |
| $5M–$10M (Cedar Ridge, $8.5M) | $10,000 | $5,000 | $5,000 |
| $10M–$25M | $15,000 | $7,500 | $7,500 |
| $25M–$50M | $25,000 | $12,500 | $12,500 |

The rule is roughly 0.1–0.15% of revenue, rounded to market steps. It also fixes a conflict: today the claim-free floor is a flat $2,500, and the MFA+EDR credit would take a $2,500 band below that floor.

### 4.4 The numbers a reviewer is most likely to ask "why?" about

| Number | Where | What the package says now | Best available basis (for you to put in your own words) |
| --- | --- | --- | --- |
| $6,120 base / $5,508 net | Item 3 | "Illustrative" | Loss-cost sketch (4.2). Drop the unverifiable benchmarks |
| $2,500–$25,000 retention range | Summary | Stated, never shown | Band table (4.3) |
| 25% / 50% retention credits; 10% premium credit; 4-hour wait | Items 5 and 7 | Direction only | Controls the scan can verify from outside earn premium credits; controls that limit loss size move the retention. 60% of Akira victims had EDR, so EDR alone earns less. The 87% remote-access entry rate supports the remote-access credit. Credits don't stack |
| $25,000 Coverage A; $2,500 pre-incident | Item 4 | "Needed to price it" | $25K buys about 3 days of breach coach and triage for a small firm. Add a per-period cap. Pre-incident help overlaps "suspected incident", so merge or redefine it |
| $250K system-failure sublimit | Item 6 D | Aon supports *a* sublimit | 25% of the aggregate. Realized systemic losses were outages. Apply it to F as well |
| $250K PCI | Item 6 K | Nothing | Cards go through a hosted page (SAQ A), so card-brand assessment exposure is modest |
| $100K / $100K / $50K (M, N, O) | Item 6 | Nothing | Bricking: about the cost of the laptop fleet. Reputational harm and cryptojacking: introductory sublimits for hard-to-measure losses |
| $25K security improvements (G) | Item 6 | "Small, clear budget" | About one year of MFA, EDR and MDR subscriptions for a 60-person firm. Run its 90-day clock from discovery |
| 20% coinsurances | III.1.6–1.7 | "Market practice" | Market pattern (75/25 splits are common). Say they don't stack |
| 45 days (known-exploited vulnerabilities) | III.1.7 | Nothing | Chubb's grace period; add Chubb to 04 |
| 14-day wait, 90 days (N); 90 days (S) | Item 6; I.S | Nothing | Time for a news cycle to hit revenue; a bounded period for hard-to-measure loss |
| 1 hour / 30 days / 15 days; 50% advance in 10 business days, $250K cap | V.7 | Coalition's "5-minute response" | A payroll cycle for the advance. Colorado's bad-faith statute is the backdrop. Make the $250K cap 25% of the aggregate so it scales with limit |
| 12-month restore test | Item 7 | Nothing | Annual testing is a common expectation. Measure from inception or incident |
| $5,000 callback threshold | III.6.1 | Coalition's application; FBI/IC3 (neither in 04) | Cite them, or align to $10,000 |
| 10% key customer; 20% insured-vs-insured; 25% acquisitions; 50% subsidiaries | II; IV.2.6; V.4.1 | Nothing | Common accounting and control thresholds (label as your reasoning) |
| 24 months of credit monitoring | II | "Common legal requirements" | Cite a state rule, or say "market practice" |
| $1M–$50M revenue; 10–250 employees | Summary | Nothing | Tie the band to At-Bay's $25M split and Corgi's admitted appetite. Drop "10–250 employees" |

---

## 5. Prioritized fix list

**Tag key:**
- **(P1)** the other session's first pass, items 1–20
- **(P2)** its second pass, items 21–40
- **(R1)** my first review
- **New** found by this research

Report numbers show where the detail is.

### Tier 1. Before sending: accuracy, legal disclosures and strategy

| ID | Fix | Where | Tag / report |
| --- | --- | --- | --- |
| T1-1 | Reframe the Corgi comparison. Harborline is a small-business cyber form that fits Corgi's new admitted carrier and its professional-office appetite, and Corgi startups graduating into this revenue band. Rewrite "liability-first … suits startups" and the Corgi column of the benchmark table (regulatory defense is included, not an endorsement) | Rationale Summary, Declarations row, Market benchmark | New · 02, 08 |
| T1-2 | Fix "Coalition (admitted)". Name the form each time, and note that the Active Cyber Policy is surplus lines | Rationale Declarations row; Insuring agreements rows | New · 02 |
| T1-3 | Remove the Vouch $7,078 figure (2 places) and the "$2,330–$4,048" comparators. Replace them with a loss-cost sketch and soft-market context (Marsh US cyber −2%; CIAB −3.2%) | Summary; Market benchmark; 04 item 17 | R1, P2-37 · 03, 08 |
| T1-4 | Terrorism notice: add the 80% federal share and $100B cap, reproduce or fix the circular Item 12 reference, and cite Treasury's Dec 27, 2016 cyber guidance | Notice 7; Item 12 | P2-21 · 05 |
| T1-5 | Colorado fraud warning: add the statute's third sentence | Application Part 9 | P2-22 · 05, 06 |
| T1-6 | Late notice: make the 90-day deadline firm for claims, keep the prejudice test for incidents, and make automatic ERP cover claims first made in its 60 days | V.1.2–1.3; V.5.4 | R1 · 05 (*Craft*) |
| T1-7 | Fraud cancellation notice: 30 days → 45 | V.5.2 | New · 05 |
| T1-8 | Punitive damages: one rule, stated once, plus a plain note that Colorado doesn't allow insuring them | Damages definition; III.7.5; Item 11 | New · 05 |
| T1-9 | Service standards: name 8% compounded (C.R.S. 5-12-102), say interest adds to statutory remedies, and stop calling "aims" "binding" in the rationale | V.7.2–7.3; rationale Conditions | New · 05, 06 |
| T1-10 | Update the regulatory rows on the day you send: SB 690 (outcome after Sept 30; retroactivity) and CIRCIA. Use one as-of date (Sept 26 vs 27 mismatch) | Rationale Regulatory status; 00 guide | R1 · 05 |
| T1-11 | Remove the "Sep 26, 2026 · @R" byline from all three docs; it prints on page 1 of each PDF | All three docs | R1 |

### Tier 2. Coverage wording: substantive

| ID | Fix | Where | Tag / report |
| --- | --- | --- | --- |
| T2-0 | **Cloud accounts vs dependent systems.** Define "cloud accounts" (the tenants, identities, settings and data you control in an online service) as part of *your* computer systems. Exclude them from "dependent systems". Say a provider's own bug or update is a system failure at a dependent provider (Coverage P) | Computer systems; dependent systems; system failure | New · 07 (W-01) |
| T2-1 | **Fraud paths.** Bank-direct fraud ("leads an employee, **or your financial institution**, to transfer…", or a separate "bank impersonation fraud"). Extend computer fraud to **client accounts** and to transfers you approved without knowing they'd been altered (payroll batches). Replace "direct result" with "resulting from" | Fraudulent instruction; computer fraud; funds transfer loss; III.6.1 | R1, P1-2 · 05, 07 (W-02) |
| T2-1a | **Partners aren't employees.** Fraudulent instruction item 3 requires an *employee* to transfer. Change it to anyone authorized to make, approve or change payments (executives, employees, contractors, and an AI agent acting within its authority). Use "whoever receives or approves the request" in III.6 | Fraudulent instruction item 3; III.6.1–6.2 | New · 07 (W-03) |
| T2-1b | **Contract duties.** Carve back into "damages" contractual duties to keep data secure, to pay for notifying people after a privacy event, and PCI amounts. Otherwise the contract-exclusion carve-back saves only defense costs | Damages item 4; IV.2.5 | New · 07 (W-05) |
| T2-1c | **Incident-to-claim linkage.** A reported incident locks in every later claim from it under this policy, without having to name who might sue. Exclusion 2's "reported under a prior policy" applies only where that earlier policy covers it. One retention covers an incident and all its claims. Define "related" | V.1.4; IV.2.2; III.1.3; incident and claim | New · 07 (W-06) |
| T2-1d | **Known problems.** Tie "should have known" to the continuity date. Carve out unexploited vulnerabilities and anything disclosed in the application | IV.2.2; Item 8 | New · 07 (W-07) |
| T2-1e | **Sublimits per period.** Say whether each Item 6 sublimit is per incident or per policy period, and whether proof-of-loss help erodes it | Item 6; III.1.1; III.1.8 | New · 07 (W-08) |
| T2-1f | **Suspected incidents.** The trigger ("first happened") can defeat Coverages A and B when an investigation finds nothing. Say a reasonably suspected incident qualifies | Section I trigger item 1 | New · 07 (W-09) |
| T2-1g | **Carve-backs as grants.** "Where an exclusion says it does not apply to something, that thing stays covered" turns every carve-back into a grant (e.g., unpurchased Coverage P through exclusion 12). Say coverage still depends on the insuring agreements | Section IV introduction | New · 07 (W-14) |
| T2-1h | **Exclusion 4 scope.** "Committed with an executive's knowledge" can reach an outside attack the IT manager is watching, and "criminal" reaches statutory crimes such as CIPA. Require "knowledge and consent", a final ruling or admission, and apply that standard to all coverages | IV.2.4; IV.2.19 | New · 07 (W-13) |
| T2-1i | **Guaranty association.** Colorado's guaranty-association statute (C.R.S. 10-4-520, search-result level) appears to bar using the association for sales or inducement. Replace notice 4's guaranty sentence with "licensed by the Colorado Division of Insurance; this form is filed with it". Stop using "guaranty fund protection" as a selling point in the rationale | Notice 4; rationale Declarations row | New · 07 (W-16) |
| T2-2 | Unfair-trade-practices exclusion: carve back claims under I (and Q, if bought) arising from a security failure, privacy event or wrongful collection | IV.2.8 | R1 · 05 |
| T2-3 | Widespread events and system-failure leak: apply the $250K system-failure sublimit to D and F combined. If you add a widespread-event limit, scope it to E, P and system-failure F only, never to attacks on the insured's own systems | I.F; Item 6 | P1-5 (scoped) · 04 |
| T2-4 | Infrastructure carve-back: define "infrastructure provider" (utilities, telecoms, internet backbone, DNS) and remove it from "dependent provider" or from the carve-back | IV.2.12; dependent provider definition | New · 04 |
| T2-5 | AI agent: non-malicious agent errors → system failure (sublimited); prompt-injected or hijacked agents → security failure ("acts on instructions from anyone other than you, including hidden instructions in content it processes"); define authority by configured permissions; say whether agent-made payments fall under Coverage H | Security failure item 5; AI agent definition | New · 01, 04 |
| T2-6 | Ransomware coinsurance: define ransomware; apply only to restoration and BI from encryption (not data-theft extortion); say it doesn't stack with the known-exploited-vulnerability coinsurance (cap 20% in total) | III.1.6–1.7 | P1-11, P1-15 · 01, 05 |
| T2-7 | Scan estoppel: delete "or should have shown"; carve out known-exploited vulnerabilities you were notified about; remove scan results from the definition of "application" | V.3.4; III.1.7; application definition | P1-16 · 03, 04, 05 |
| T2-8 | Services outside the limit: per-period caps for Coverage A and pre-incident help; state that pre-incident help is also outside the aggregate in III.1; resolve the overlap with "suspected incident" | Item 4; I.A; III.1.2; V.2.3 | R1, P1-1 · 06 |
| T2-9 | War exclusion: say "state" means a sovereign country, never a U.S. state (otherwise "outside the state that suffered" can read as outside Virginia); add "a cyber operation carried out as part of a war"; restore LMA's "functioning of the state" qualifier; add a cloud-location rule; say evidence relied on is shared; decide how pending-attribution payments sit with reinsurance | IV.2.15 | New · 04, 05, 07 (W-10) |
| T2-10 | Define "discover" (an executive's or the named security contact's awareness), matching notice and exclusion 2. Also limit "you" in the first-party coverages to the named insured and its subsidiaries | Section I trigger; definitions; insured/you | P1-4 · 07 (W-18) |
| T2-11 | Rogue IT lead: carve back into "security failure" for rogue acts by employees *or executives* acting against your interests. Keep them in the knowledge group. Stop exclusion 4 and imputation reaching the firm unless the managing partner, CFO or general counsel took part or knew | Security failure; IV.2.4; IV.1; V.3.3 | P1-6 · 05, 07 (W-04) |
| T2-12 | Voluntary payments and consent: reimburse reasonable, necessary unconsented costs absent prejudice; exempt panel vendors, legally required notices and first-72-hour containment from "with our consent" | V.2.2; breach response costs definition | New · 05 |
| T2-13 | Honest-mistake remedy. "Terms we would have offered" could let the insurer add an exclusion after a loss, so limit it to premium, retention and credits. Say what happens if the true answer would have led to a decline (cancel on notice, keep covering what came before). Apply rescission only to the insureds who made or knew of the misstatement | V.3.2–3.3 | New · 03, 05, 07 (W-15) |
| T2-14 | Insured-vs-insured: carve back a claim by *any* natural-person insured (partners too) about their own personal information | IV.2.6 | New · 05 |
| T2-15 | Key customer: add a naming field (or drop "named"); align "at least 10%" with the application's "more than 10%"; define a key-customer event; pay "during the outage and up to 90 days after" | I.S; definition; Item 6 | P1-8 · 06 |
| T2-16 | Credits: one rule for stacking; fix "would halve it" ($3,750 vs $5,000); define claim-free and whether the 25% compounds; define qualifying MDR | Items 5 and 7; V.6.1 | R1, P1-9, P1-10 · 03 |
| T2-17 | Security lapses: IV.1 should list all three disclosed ways security changes terms (backup coinsurance, callback cap, known-exploited-vulnerability coinsurance) | IV.1 | P1-3 |
| T2-18 | Small wording fixes: "utility" charges missing from service fraud loss (and add AI/LLM API providers); media wrongful act isn't an "incident" in the trigger; G's 90-day clock should run from discovery; III.5.1 omits system failure; "unpatched" vs "unpatched and unmitigated"; Coverage A should accept any Item 10 channel; bold used on non-defined text; phantom "higher limits available" options | Various | R1, P1-7, P1-12, P1-13 · 06 |
| T2-19 | Sanctions exclusion should also cover reimbursing a payment *you* made to a prohibited person. OFAC mitigation credit turns on reporting the *attack* early, so require a report before any consented payment | IV.2.17; III.3.5 | New · 05 |

### Tier 3. Application

| ID | Fix | Tag / report |
| --- | --- | --- |
| T3-1 | Add the missing questions underwriters ask in 2026: end-of-life systems (the pre-issue scan already found a legacy print server; Windows 10 support ended Oct 14, 2025); remote-support tools and how the IT provider and other vendors get in; backup credential segregation and MFA on backups; records by type and records processed for the 40 payroll clients; wire, ACH and client-payroll volumes; hardening; IRS e-file credential protection; prior policy and retro date | P2-25–29 (partial) · 03 |
| T3-2 | Remove misrepresentation traps: 1.13 "payment processing" is undefined while the firm runs client payroll; "(hardware security keys)" turns a tick into a warranty; 3.5 bundles three encryption questions; 6.6 is fragile; 8.1 terms are undefined; optional text (8.2) should not be able to ground rescission; "deliberate misstatements" needs "material" | New · 03, 06 |
| T3-3 | Ask facts rather than legal conclusions in Part 7. Delete 7.6 (CIRCIA), which is unanswerable until the rule is final. Reword 7.5 to cite the GLBA exemption and "under 100,000 consumers, no data sales" | New · 03, 05 |
| T3-4 | HIPAA 7.2: either "no healthcare clients" or "Yes, business associate agreements with N medical-practice clients". Auditing a medical practice usually touches patient billing data, so "financial statements only" is risky | P2-24 (changed) |
| T3-5 | Card data: 3.1 ticks "payment cards" while 3.10 says card data never touches the firm's systems | P2-23 |
| T3-6 | Underwriter page: fixing a *medium* scan finding doesn't affect the claim-free reduction (critical only). Note that backups must be retested by June 2027. Mirror the mid-term 30-day duty to report a removed control | R1, P2-30 · 03 |
| T3-7 | Evidence: attach an EDR console export, restore-test log and callback procedure for each starred credit, not only the MFA report | New · 03 |

### Tier 4. Rationale content

| ID | Fix | Tag / report |
| --- | --- | --- |
| T4-1 | Add the "why this number" explanations (section 4.4), a retention band table (4.3) and a pricing sketch (4.2) | New · 06, 03, 08 |
| T4-2 | Cite both Coalition's and At-Bay's severity data; label $508K as all sizes and $422K as under $25M | R1 · 01 |
| T4-3 | Re-cite "privacy claims doubled in H1 2026" to Coalition's blog (it's real; the March report isn't the source) | Correction · 01 |
| T4-4 | Update the AI claims: affirmative AI is now market-standard (Beazley, CFC, Sept 2026); ISO's AI exclusions are *optional* endorsements; keep "no competitor wording" only for the AI-agent definition | New · 04 |
| T4-5 | Replace the Marsh "all lines" wording with Marsh's US *cyber* −2% (Q2 2026); update ledger C17 | New · 03, 04 |
| T4-6 | Soften the absolutes: "no competitor has" → "none of the forms we reviewed"; "Executive defined narrowly" (it isn't); "binding contract terms" (the policy says "aim"); "phone calls and letters" (phone and video are arguably already "electronic" at Coalition, so letters may be the real difference); "Cowbell excludes system failure" → Prime 100 only; Vouch figures come from one insured's certificate; $1,010 is from one issued policy | P2-35 · 02, 06 |
| T4-7 | Remove stale or wrong lines: "$500K option" (twice); "12-hour" wait and "D, H and M updates" (old letters); the "Open … state this in the memo" row; five "(updated September 2026)" notes; "record counts set breach response limits"; JLR "attack on its suppliers" → "the attack on Jaguar Land Rover, which disrupted more than 5,000 UK organizations including its suppliers"; "serves the clarity criterion" (twice) | R1, P2-33, P2-36 · 06 |
| T4-8 | Add missing sources to 04: Chubb NSE, Corvus, UK Insurance Act 2015, CISA #StopRansomware, FBI/IC3 2025 report, NYDFS Part 500, Colorado SB 26-189, Coalition Deepfake Response and Enhanced Business Recovery announcements, At-Bay Post-Cyber Event Hardening, Coalition privacy blog, Coalition application, IRS Publication 4557. Fix 04 items 11, 14, 15 and 17, and the missing-link count | R1 · 02, 06 |
| T4-9 | State the trade-offs a reviewer will raise: admitted paper is slower to re-price; Harborline is narrower than Coalition on system failure and vendor system failure; no deepfake-response or $0-retention path | New · 02, 04 |
| T4-10 | Voice and length: one voice (yours), cut process sections to one short "how I validated this" paragraph, and aim for about 10 pages plus appendices | R1, P2-33, P2-34 · 08 |

### Tier 5. Package and formatting

- After the fixes, re-check 00 and 04 against the documents: coverage letters, the widespread-event limit, and source counts.
- Tab names are already fixed, so the page headers are clean.
- Remove the byline (T1-11).
- The quality review's "22 of 26 supported" is 21 by the ledger. It's private, but don't quote it.

### Tier 6. Worth adding if you have time (strategic)

From report 08:
- A one-page executive memo up front.
- A "who it's for and why Corgi" half-page.
- A paper and filing plan: admitted vs risk retention group vs surplus lines, with a lead state.
- An accumulation and reinsurance half-page. Include the non-obvious risk that CPA firms share a few tax, payroll and IT vendors, so an outage in tax season hits the whole book.
- A competitive map.
- A "what I'd cut" list.
- KPIs and the first three tests.

---

## 6. Corrections to earlier reviews

- **"Privacy claims doubled in H1 2026" is real.** It's a Coalition blog post. I (round 1) said it couldn't come from the March report. That's right, but the fix is to re-cite it, not to cut it.
- **Application 7.5.** Round 1 overstated the exposure. The 25,000-consumer prong needs data-sale revenue, and Colorado exempts GLBA financial institutions. The "No" is right.
- **Beazley BBR 5.0 date.** The summary document is dated April 2025, and it applies to policies incepting from July 1, 2025. Both dates are right; label them.
- **Marsh.** A US cyber-specific −2% figure exists for Q2 2026. The ledger's C17 note can be updated.
- **Other session, pass 1.** It praised the late-notice clause; under *Craft* it needs the fix in T1-6. Its item 17 is already handled by III.1.3.
- **Other session, pass 2.** Its HIPAA fix (#24) risks a new inaccuracy (T3-4). Its terrorism citation should be the Dec 27, 2016 cyber guidance. "The references file and submission guide match the documents" isn't quite right (T4-8).
- **At-Bay's AI claim.** The other session checked the At-Bay PDF and found it supports the rationale's AI claim. Keep it, and add IC3 2025 as a second source.
- **Guaranty fund as a selling point.** Reports 02, 04 and 08 (and the "why admitted" interview answer in 08) treat guaranty-fund protection as a benefit to cite. Report 07 found Colorado appears to bar using the guaranty association in sales, so drop that argument (T2-1i).

---

## 7. Interview prep

Report 08 section 7 has 15 likely questions with answers grounded in the package, and 5 questions to ask Corgi. The five most likely:

1. "Walk me through the $5,508. Is it adequate?" Use the loss-cost sketch (4.2), and name the swing factor (accounting-firm frequency).
2. "Why SMBs, when Corgi insures startups?" Corgi's admitted carrier, graduating startups, and the same contract-driven purchase trigger. Cedar Ridge is buying because two clients require $1M.
3. "Why admitted, not a risk retention group or surplus lines?" Most of this cover is first-party, which a risk retention group can't write. State-approved forms fit small-business buyers, and admitted cyber ran a better loss ratio than surplus lines in 2025. The cost is filing time. Don't pitch the guaranty fund as a benefit: Colorado appears to bar using it for sales (T2-1i).
4. "What's the biggest risk?" Adverse selection in a soft market, and vendor concentration across a vertical book in tax season.
5. "What would you cut?" Reputational harm and cryptojacking back to options, the claim-free reduction until priced, and a shorter rationale.

---

## 8. What still needs verifying before you quote it

Open these at source (they were blocked here):
- **Coalition 2026 claims report:** $116K, $141K, $269K, the 1.21% frequency and the 58% email-fraud share.
- **IC3 2025 report:** $893M, >$30M AI-enabled BEC, $3.05B BEC, and the Recovery Asset Team's $679M and 58%.
- **Coveware Q2 2026:** the $1.88M payment and law-firm campaign.
- **Verizon DBIR 2026:** the 48% third-party share.
- **AM Best and Fitch June 2026:** the 53% loss ratio and the 50.2 vs 56 split.
- **Marsh and CIAB Q2 2026:** the −2% and −3.2%.
- **Corgi admitted carrier release (Aug 26, 2026)**, including whether cyber is or will be written on it.
- **Corgi's cyber page:** that regulatory defense is included.
- **Beazley and CFC affirmative AI (Sept 2026).**
- **Case citations recalled from memory:** Stresscon, Lira, Craft and Principle Solutions v. Ironshore. Check reporter cites before quoting.
- **Colorado non-renewal notice period** (C.R.S. 10-4-110) and whether 10-4-109.7 reaches cyber.
- **Colorado guaranty-association advertising rule** (C.R.S. 10-4-520): what it bars, and whether any notice is prescribed.
- **Chubb Neglected Software Exploit percentages:** unconfirmed; don't quote any.
- **The issued At-Bay, Coalition and Vouch documents:** reconfirm the ERP, hammer, $1,010 pre-claim and short-rate refund claims if you keep them.

---

## 9. Files in this folder

| File | What it covers |
| --- | --- |
| `00_round1_findings.md` | My first-pass review of the zip and docs (reported in chat earlier) |
| `01_threat_landscape.md` | 2025–26 SMB claims data, systemic events, AI-related attacks in depth, accounting-firm specifics, and a verdict on each Harborline choice |
| `02_insurtech_products.md` | Coalition, At-Bay, Corvus, Cowbell, Vouch, Corgi, Beazley and AI insurers: profiles, a 37-row feature matrix, and tests of 13 competitor claims in the rationale |
| `03_underwriting_pricing.md` | 2026 underwriting practice, a question-by-question application benchmark, the credit-design review, pricing plausibility and a retention band proposal |
| `04_market_exclusions_ai.md` | Market economics, exclusion trends (war, infrastructure, widespread events, neglected software), AI exclusions and affirmative AI, and admitted paper |
| `05_law_regulation_caselaw.md` | Colorado law, federal and state cyber rules, coverage case law, and a 27-row clause → law → fix table with draft wording |
| `06_traceability_audit.md` | The "why each word and number" audit: 207 elements, the top 30 gaps with draft explanations, cross-reference and consistency checks |
| `07_wording_counsel_review.md` | Coverage-counsel review: loss scenarios run through the wording, findings by severity with replacement text |
| `08_strategy_corgi_fit.md` | Corgi fact base, the SMB cyber opportunity, business case, how a hiring manager will read the package, recommendations and interview prep |

Draft sentences in these reports are labeled "draft — rewrite in your own words". They're there to show the reasoning, not to be pasted in.
