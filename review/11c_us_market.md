# 11c. US market and buyer check: do the 34 borrowed ideas work in the US?

Prepared September 27, 2026. Lens: a US retail broker placing small-business cyber for a Denver CPA firm (Cedar Ridge Accounting Group: $8.5M revenue, payroll run for 40 clients, $1M aggregate, about $5,508 premium). This report covers market reality only. Other reports cover law and loss data.

**Evidence rules.**
- 25 of 25 web searches were used. No insurer page was opened. Everything web-based is search-result level.
- Labels:
  - **[snippet]**: a search result or its summary. Vendor and MSP blogs are marked "low reliability".
  - **[catalog]**: a row in `catalog/cyber_policies.csv`.
  - **[prior]**: an earlier report in `review/` (02, 04, 10, 10a–10d). Those reports are snippet-level themselves.
  - **[background]**: my own broker knowledge. Not verified this session.
- No carrier wording is quoted. Case holdings are paraphrased.

---

## 1. Bottom line

1. **Three ideas fix problems US courts have actually ruled on. Do them first.**
   - **A3 (payment fraud, client accounts, bank deceived)** is the most useful idea on the list for a CPA or payroll firm. US courts have repeatedly denied exactly this loss:
     - *Taylor & Lieberman v. Federal* (9th Cir. 2017): an accounting firm wired a client's money after a spoofed client email.
     - *RealPage v. National Union* (5th Cir. 2021): the insured controlled client funds at a payment processor but never "held" them.
     - *Mississippi Silicon v. AXIS* (5th Cir. 2021): the employee authorized the transfer, so only a $100K sublimit paid.
     - *Pestmaster v. Travelers* (9th Cir. 2016): a payroll-provider diversion case [background].
   - **A4 (limits map)** answers *CiCi v. HSB Specialty* (N.D. Tex., Feb 2026). A ransomware sublimit was not applied across coverages because the endorsement didn't say it was. Bad-faith claims against the insurer and its MGA are going to a jury [snippet].
   - **A2 (a security term counts only if it mattered)** answers the most-voiced US small-business fear: "they'll deny me over a control." See *Columbia Casualty v. Cottage Health* (2015) and the *Travelers v. ICS* MFA rescission (2022).
2. **Several ideas are table stakes. Harborline needs them, but they win nothing.** Don't sell them as innovations:
   - A5 (related incidents);
   - A8 (foreign regulators);
   - the A10 concept (your cloud tenant counts as your system);
   - B9 (bundled security services);
   - A9 (court attendance, which is now in Coalition's base form).
3. **Several ideas are cheap and invisible at quote time, but help at claim time.** Keep them short. They are A1, A6, A7, B7 and B8. B13–B15 belong in a welcome pack or on the renewal notice, not in the contract.
4. **Drop six:** B2, B4, B11, B16, C5 and C7. No US buyer asks for them. B4 only softens a coinsurance Harborline imposed on itself. C5's US equivalent is credit monitoring, which Harborline already pays for.
5. **Deepfakes worry buyers, but no US coverage fight was found.** The 2026 Travelers Risk Index says 54% of business leaders worry about AI phishing, deepfakes or social engineering [snippet]. No public US deepfake claim denial turned up. B1 is a real differentiator, since only Coalition sells a deepfake response endorsement. Re-scope it to what a CPA firm faces: lookalike domains and fake "firm" emails sent to clients.
6. **The biggest US gaps are not on the idea list:**
   - **breach response outside the aggregate**, or a bigger separate response limit. Coalition, CFC and Beazley's BBR all use one [prior][snippet];
   - **a social-engineering limit big enough for a payroll firm**. Sublimits of $100K–$250K are the top buyer complaint [snippet];
   - **a visible, priced full-limit system-failure buy-up**, because Coalition's surplus-lines form pays system failure at full limit [prior].
7. **Harborline's 20% ransomware coinsurance is itself a quote-comparison negative** in a soft 2026 market [background]. Rates are down 2–3% (Marsh, CIAB) [prior], and CRC calls it buyer-friendly [snippet]. A2's causation rule and a short B5 backup definition are the minimum repair.
8. **Parametric downtime pay (C1) and a limit reinstatement (C2) are surplus-lines or large-buyer features in the US** (AIG with Parametrix; CFC). They are good interview material. A CPA-firm broker will not ask for them. Keep both as "test next".
9. **Skip-list check:**
   - Full-limit system failure is **common, not table stakes**. Keep the $250K core, but price and show a buy-up.
   - Criminal reward is in Coalition's US base form at $25K [snippet]. It is otherwise uncommon and nobody asks for it. It's fine to skip. Adding it as a two-line discretionary benefit costs almost nothing.

---

## 2. Master table

**Class key:**
- **TS**: table stakes. Most offer it, and a buyer would notice if it were missing.
- **Common**: several carriers offer it.
- **Rare**: one or two offer it.
- **Absent**: not found in the US.

**Market fit:** Strong, OK, Weak or Poor (as defined in the brief).

| ID | Idea | US availability (who) | Class | Broker/buyer value | Real US disputes it prevents | Commercial risk | Market fit | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | Ransom never required; pre-payment routine; legal-report support | No US form states it expressly [background]. Carriers must consent to any payment. Panels do sanctions screening and FBI reports as routine [background]. 86% of Coalition claimants refused to pay [prior] | Absent (wording); TS (practice) | Low at quote. Reassuring at claim. Good interview line | None litigated. The public complaint was the reverse: insurers nudging municipalities to pay (2019 press) [background] | Low. BI may run longer where no one pays. Reinsurers neutral to positive | OK | Keep with change (shorten) |
| A2 | A security term counts only if it caused or worsened the loss; one closed list of terms | No general causation rule in US forms. They use failure-to-maintain exclusions, attestations and rescission [snippet][background]. Chubb NSE is time-based, not causal [prior] | Absent | High as a talking point. MSPs and brokers publicize the "attestation trap" [snippet, low reliability] | *Cottage Health* (2015, minimum-practices exclusion) [snippet]; *ICS* (2022, MFA; application, so only partly) [snippet] | Moderate. Insurer must prove causation, which costs forensic time. No real adverse selection, because credits stay priced | Strong | Keep |
| A3 | One payment-fraud trigger: you (incl. partners) or your bank deceived; client accounts you operate | Bank-deceived funds-transfer fraud is TS (Coalition, Beazley, Travelers, HSB wrongful transfer event) [prior][catalog]. Employee social engineering is TS but sublimited [snippet]. A client's own account you operate: rare (CFC and Aviva in the UK) [prior]. Most cover only the insured's own money [snippet] | TS (bank); Rare (client accounts) | Very high for payroll and bookkeeping firms. A broker will ask about it first | *Taylor & Lieberman* (2017); *RealPage* (2021); *Mississippi Silicon* (2021) [snippet]; *Pestmaster* (2016) [background] | Real fraud exposure. Price on client-payroll volume. Keep insider fraud excess of crime cover | Strong | Keep (top priority) |
| A4 | Limits map (each incident / period); caps say "applies across coverages" | Per-coverage limits under an aggregate are TS (ISO, HSB) [prior]. Express cross-coverage labels are rare. Drafters urge them after *CiCi* [prior] | TS (map); Rare (label) | Brokers: moderate to high (fewer surprises). Buyers: invisible | *CiCi v. HSB Specialty* (Feb 2026) [snippet]; *Mississippi Silicon* sublimit fight [snippet] | None. It protects the insurer too | Strong | Keep |
| A5 | Related incidents are one incident, in the earliest period; continuity for switchers | Related-claims and earliest-period rules are TS (ISO CY 00 02; claims-made practice) [prior][background]. Harborline already groups related incidents. Other-insurer continuity is rare | TS | Invisible. Brokers value clean switching, which full prior acts already gives | No cyber case found [snippet]. Common in D&O and E&O [background] | Low | Weak (TS, required) | Keep with change (short) |
| A6 | One retention per policy year | CFC Cyber Proactive Response: one aggregate excess however many incidents (on CFC's US pages; surplus) [snippet]. At-Bay caps retentions per incident only [prior] | Rare | Moderate talking point. Matters only for a second hit in the same year | None (an economic feature) | About $1–2 expected cost per policy [prior]. Slight moral hazard after the first hit | OK | Keep |
| A7 | An external alert (FBI, bank, MSP, us) always counts as a suspected incident | "Actual or reasonably suspected" triggers are common [background]. Coalition gives pre-claim help [prior]. An express outside-alert rule is absent | Common (suspected trigger) | Low at quote. Useful at claim | None found | Low. More false-positive IR spend, capped by A's limit | OK | Keep with change (merge into T2-1f) |
| A8 | Foreign privacy regulators in "regulatory proceeding" | Standalone forms commonly include foreign agencies [background]. Harborline lists US agencies only | TS | Low for Cedar Ridge. A comparison checklist would flag the gap | None | Negligible | Weak (TS, required) | Keep |
| A9 | Court attendance pay | In Coalition's surplus-lines Active Cyber Policy base form [snippet]. MICA e-Med ($10K) [snippet]; another US cyber form at $2K/day and $100K [snippet]; TMHCC healthcare [prior]. Accountants' professional liability often has similar pay [background] | Common | Low. It is a checklist item only | None | Negligible | Weak | Keep with change ($1,000/day) |
| A10 | Cloud-tenant tie-breaker; narrower DNS/infrastructure exclusion | Treating a third-party-hosted system as your own is TS in concept (At-Bay External Computer Systems; older BBR hosted-systems wording) [prior][background] | TS (concept) | Moderate to high after CrowdStrike and AWS. Brokers ask about cloud and outage language [snippet] | AWS Oct 2025: claim language was "not one size fits all" [snippet]. No denial suit found | Low. The DNS narrowing mainly helps P buyers | Strong | Keep |
| B1 | Impersonation and deepfake response (no breach needed) | Coalition Deepfake Response Endorsement (Dec 2025; global, including the US) [prior][snippet]. BOXX affirmative deepfake cover (mostly fraud) [snippet] | Rare | Moderate and rising: 54% worry about AI phishing and deepfakes [snippet] | None found. Arup ($25.6M) is Hong Kong, not a coverage case [snippet] | Low at $25K. Frequency unknown | OK | Keep with change (CPA scope) |
| B2 | Executives' personal funds and identity | Personal cyber is a personal-lines product (Chubb, AIG, PURE, HSB) [background] | Absent (commercial) | Low. Home and personal cover exist | None | Personal-lines blur; filing questions | Weak | Drop |
| B3 | AI voluntary shutdown | Beazley endorsement (Sept 24, 2026), called industry-first [prior]. Security-failure shutdown is common [prior] | Rare | Low for a CPA firm. 89% use AI, 59% govern it [snippet] | None (new) | Low if inside the $250K system-failure cap | OK | Keep with change (one sentence in T2-5/W-25) |
| B4 | Coinsurance waived on the first $50K | None [background] | Absent | Low. It softens Harborline's own coinsurance | None | Low ($10K maximum per incident) | Weak | Drop (fix the root instead) |
| B5 | Precise "verified backups" definition | Backup questions are near-universal on US applications [background]. Rare as a policy definition | Common (application) | Moderate. Objective tests cut disputes | None found. Theoretical while coinsurance exists | None | OK | Keep with change (short test) |
| B6 | Warning and 30 days to cure before a post-loss duty counts | None as wording [background]. Many states need prejudice for notice and cooperation defenses [background] | Absent | Low | Cooperation-clause denials occur generally [background]. No cyber case found | Low | Weak | Keep with change (one line, low priority) |
| B7 | You need answer only what we asked | Question-driven applications are normal. Express wording is rare [background] | Common (effect) | Moderate. Brokers fear rescission (ICS) | *ICS* (2022): the question was asked, so B7 alone wouldn't help. V.3's honest-mistake rule would [snippet][background] | Low. Needs a complete application | OK | Keep (one line) |
| B8 | Retention billed last, in installments | Pay-on-behalf is common. Deferring the retention is absent [background] | Absent | Moderate at claim; invisible at quote | None | Small credit risk ($7,500) | OK | Keep with change (service standard) |
| B9 | Security services plus a promise they never cut cover | Services are TS: Coalition Control, At-Bay, Travelers Cyber Risk Services (all policies, 2025), Cowbell, AIG small CyberEdge, Hiscox Academy [prior][catalog]. The promise is absent | TS (services); Absent (promise) | High expectation for services. The promise answers a real fear | None found | Service cost. Liability if an insurer-supplied MDR fails. SB25-058 fit | Strong | Keep (hybrid) |
| B10 | Verified-framework credit tier (CIS IG1, NIST, FTC Safeguards WISP) | Credits are per control (MFA, EDR, MDR), not per framework [background] | Rare | Low, but a WISP-based credit is cheap for tax firms | None | Uneven attestation quality | Weak | Make optional (rating program) |
| B11 | Earn credits mid-term | Rare [background] | Rare | Low | None | Admin; endorsement mechanics | Weak | Drop (handle at renewal) |
| B12 | $0 retention on panel forensics and breach coach if reported in 72 hours | Coalition: $0 with Coalition IR [prior]. CFC: nil deductible and a separate IR limit for SMEs [snippet]. At-Bay: $0 in packages [prior] | Common | High. It shows up in quote comparisons | Late reporting is a leading claim problem [snippet, low reliability] | Low. Early reports cut severity | Strong | Keep |
| B13 | One-page "policy at a glance" | Marketing summaries are common. Contractual summaries are rare [background] | Rare | Low for brokers; higher for Corgi's direct buyers | Risk runs the other way: a summary that contradicts the wording | Legal consistency risk | OK | Keep with change (non-contractual) |
| B14 | Renewal "what changed" table | Brokers do it. Some states require notice of reduced renewal terms [background] | Rare (carrier) | Moderate for brokers (E&O cover) | Broker E&O claims over unflagged changes [background] | Admin | OK | Keep with change (renewal notice) |
| B15 | Legal-deadlines card | A breach coach and carrier-app service [background] | Common (service) | Low | None | Staleness | Weak | Keep with change (welcome pack) |
| B16 | Publish claims results against service aims | No carrier found. Coalition and At-Bay publish loss reports, not service KPIs [prior] | Absent | Low | None | Reputational if aims are missed | Weak | Drop |
| C1 | Fast Downtime Payment (parametric BI) | AIG with Parametrix (Aug 2026) [prior]; Parametrix direct [prior] | Rare | Moderate interest after outages. Price-sensitive at $5.5K | CrowdStrike: many outages ended inside 8–12h waiting periods, so no pay; some forms cover malicious events only [snippet] | High accumulation (shared tax and payroll platforms); filing; basis risk | OK | Make optional (test next) |
| C2 | One limit reinstatement | CFC unlimited reinstatements (US pages) [snippet]; Coalition issued policy [prior] | Rare (admitted) | Moderate ("two limits for one premium") | None | Frequency pricing; needs aggregate reinsurance | OK | Make optional |
| C3 | AI regulatory defense | Beazley (Sept 2026) [prior] | Rare | Low for a CPA firm | None (no enforcement yet) | Unknown; insurability of penalties | Weak | Make optional (later) |
| C4 | $0 retention with qualifying MDR | At-Bay InsurSec (Oct 2025) [prior]; Coalition's shorter MDR wait [prior] | Rare to common | Moderate for security-forward firms. Cedar Ridge has no MDR | None | Favorable selection | OK | Make optional (Item 7) |
| C5 | Goodwill payments to affected clients | Absent. The US norm is credit monitoring and ID restoration, which is TS [background] | Absent | Low | None | Admission optics in class actions [background] | Poor | Drop |
| C6 | Lookalike-domain fraud on clients (no breach at the firm) | Invoice manipulation after a breach is common (Coalition, BBR) [prior]. The no-breach version is rarely covered [snippet] | Rare | Moderate to high for CPA firms | Domain and brand impersonation losses of about $1.57B (2020–24 claims data) [snippet] | Fraud outside the insured's control; hard to underwrite | OK | Make optional (priced) |
| C7 | Risk classes that set required controls by class | Class and revenue rating plus control gates are normal underwriting, not form text [background] | Absent (form) | Low; negative if read as prerequisites | None | Rating-plan filing | Weak | Drop from form |
| C8 | Distribution: BOP-embedded, MSP, affinity | Common: HSB Cyber Suite, Hartford CyberChoice First Response, Travelers, Chubb; AICPA program (CNA, run by Aon) [prior][catalog][snippet] | Common | Strategic, not wording | None | None | Strong (strategy) | Keep (one strategy line) |

**Tally:** 10 keep, 12 keep with change, 6 make optional, 6 drop.

---

## 3. Per-idea notes

### Tier A

**A1. Paying a ransom is never required.**
- **US availability.** No US small-business form I know of says this in words [background]. The market reached the same place through consent clauses and panel practice. Coalition says 86% of its ransomware claimants refused to pay in 2025 [prior]. Sanctions screening and reporting to the FBI or CISA are routine panel steps. Treasury's 2021 ransomware advisory treats cooperation with law enforcement as mitigating [background].
- **Buyer value.** A US broker won't compare quotes on it. It still reassures an owner, and it's a strong interview line.
- **Disputes.** No US case was found where BI was cut because the insured refused to pay. The real US complaint ran the other way: 2019 reporting that insurers steered municipal clients to pay because paying was cheaper [background].
- **"Laws about paying."**
  - The CIRCIA final rule was still not published by June 2026; the target is September 2026 [snippet].
  - Only North Carolina and Florida ban ransom payments, and only by public entities [snippet].
  - Neither is likely to apply to Cedar Ridge. Keep that paragraph generic.
- **Change.** Keep the core promise and the III.4.6 sentence. Drop the "12 hours" operational promise, and don't name specific statutes in the form.

**A2. Security terms count only when they mattered.**
- **Buyer value.** This is the US fear. MSP and broker content in 2025–26 is full of "attestation trap" and "denied over MFA" stories [snippet, low reliability]. Ignore their statistics (for example "82% of denials involve MFA"). The theme itself is real.
- **Disputes.**
  - *Columbia Casualty v. Cottage Health* (C.D. Cal. 2015) was the first US fight over a "failure to follow minimum required practices" exclusion. It was dismissed on a procedural point [snippet].
  - *Travelers v. ICS* (C.D. Ill. 2022) ended in rescission over an MFA answer on the application [snippet]. A2 deliberately leaves the application to V.3, so A2 alone would not have changed *ICS*. Say so in the rationale.
- **Market.** No US form has a general causation rule [background]. Harborline already has few conduct terms, so the cost is small.
- **Risk.** A forensic causation note on ransomware claims. Reinsurers should accept it, because the list is closed and credits stay objective.

**A3. One payment-fraud trigger with client accounts.**
- **Why it ranks first.** It addresses the most-litigated small-business cyber and crime loss, and the one a CPA or payroll firm is most exposed to.
- **Disputes.**
  - *Taylor & Lieberman* (9th Cir. 2017) is almost Cedar Ridge's own fact pattern. A business-management accounting firm received spoofed emails from a client and wired about $94K from the client's account. Forgery, computer fraud and funds-transfer fraud all failed. The firm knew of the transfer, and an email is not an entry into its system [snippet].
  - *RealPage* (5th Cir. 2021): about $6M of client rent money was lost from a payment-processor account the insured controlled. No cover, because the insured never "held" the funds [snippet].
  - *Mississippi Silicon* (5th Cir. 2021): employees authorized the transfer, so only the $100K social-engineering sublimit paid [snippet].
- **Harborline's current text.** Its **fraudulent instruction** needs an **employee** to transfer. That fails when the bank itself is deceived. It may also fail when a partner (an **executive**) acts. A US broker would spot both at once.
- **Market.** Bank-deceived funds-transfer fraud is table stakes [prior]. Operating a client's own account is rare. Brokers say most policies cover only the firm's own money [snippet].
- **Risk.** At-Bay reports fraud is 30% of claims, the average stolen amount is $285K, and small-business funds-transfer fraud is up 56% [prior]. Price it on client-payroll volume.
- **Flag.** Criminals also redirect clients' tax refunds by altering returns [snippet]. There the IRS, not a bank, is deceived. Decide whether that runs through H or through liability (I).

**A4. Limits map and express cross-coverage caps.**
- **Disputes.** *CiCi v. HSB Specialty* (N.D. Tex., Feb 23, 2026): a $250K ransomware sublimit endorsement did not cap the cyber-extortion coverage under a $3M policy. The court also let bad-faith claims go to a jury, including over the MGA's (At-Bay's) conduct [snippet]. Sublimit fights are the most common cyber and crime coverage disputes, as in *Mississippi Silicon* [snippet].
- **Market.** Per-coverage limits under an aggregate are standard. Labeling a cap "applies across coverages" is a drafting improvement, not a market feature.
- **Value.** Brokers read declarations closely, and the map makes comparison easy. Owners won't notice it.
- **Risk.** None. It makes Harborline's own caps enforceable.

**A5. Related incidents and the earliest period.**
- **Market.** Table stakes. Harborline's **incident** definition already groups related incidents at the first date.
- **What's new.** The "which policy year" rule and continuity when switching from another insurer. The switching sentence helps win takeover accounts, but brokers rarely raise it.
- **Disputes.** None found in cyber [snippet]. Related-claims fights are common in D&O and E&O [background].
- **Change.** Keep it to three sentences. Don't market it.

**A6. One retention per policy year.**
- **Market.** Rare in the US. CFC markets a single aggregate excess under Cyber Proactive Response on its US pages (surplus lines) [snippet]. At-Bay caps retentions only within one incident [prior].
- **Buyer value.** Moderate. It helps the owner hit twice in a year, and At-Bay reports firms hit once are twice as likely to be hit again within two years [prior].
- **Risk.** About $1–2 per policy [prior]. The slight moral hazard after the first hit is tempered by the coinsurances.
- **Verdict.** Cheap, and it differentiates from the admitted competition. Keep.

**A7. An external alert counts as a suspected incident.**
- **Market.** "Reasonably suspected" triggers are common [background]. Naming FBI, bank or MSP alerts is new.
- **Value.** Low at quote, useful at claim. Small firms often learn of a breach from outsiders.
- **Disputes.** None found.
- **Change.** Merge it into T2-1f as one sentence plus the list of sources. Keep the rule that a no-find investigation doesn't hurt the claim-free credit.

**A8. Foreign privacy regulators.**
- **Market.** Standalone forms commonly define regulatory proceedings to include foreign government agencies [background]. Harborline lists only US agencies.
- **Verdict.** Required, but gives no edge. Three lines. Keep the "where insurable" limit.

**A9. Court attendance.**
- **Market.** Common:
  - it moved into Coalition's surplus-lines Active Cyber Policy base form [snippet];
  - MICA e-Med pays up to $10K [snippet];
  - another US cyber form pays $2K a day up to $100K [snippet].
- **Value.** A comparison checklist item only. A CPA firm's accountants' professional liability policy may already pay for trial days [background; verify].
- **Change.** $500 a day looks thin next to $2K a day. Use $1,000 a day with a $10K–$25K cap. Keep it to four lines.

**A10. Cloud-account tie-breaker; narrower exclusion 12.**
- **Market.** Treating your tenant or hosted systems as yours is market-standard in concept [prior][background].
- **Value.** Cloud questions are now standard broker questions after CrowdStrike (July 2024) and AWS (Oct 20, 2025).
- **AWS numbers.** CyberCube estimated $38M–$581M insured, and Moody's a US mean of $22M [snippet]. The outage ran 15–16 hours against typical 8–12-hour waits [snippet]. A form that let a provider's internal DNS fault count as "core internet infrastructure" would be marked down by any broker who noticed.
- **Risk.** Low. The AWS-type event is non-malicious, so the narrowing mainly matters for Option P buyers.

### Tier B

**B1. Impersonation and deepfake response.**
- **Market.** Only Coalition sells a response endorsement (Dec 2025) [prior][snippet]. BOXX and others affirm deepfakes inside fraud cover [snippet].
- **Demand.** Real: 54% of business leaders worry about AI phishing and deepfakes (Travelers Risk Index, Sept 2026) [snippet].
- **Disputes.** No US denial case was found. Claims that carriers "excluded deepfakes on 1/1/2026" come from low-quality blogs. Don't use them [snippet, low reliability].
- **Change.** Aim it at the CPA risk: lookalike domains, fake "firm" email accounts and warnings to clients. A deepfake-video smear of a partner matters less. Keep it at a $25K core sublimit.

**B2. Executives' personal funds.** A personal-lines product in the US (Chubb, AIG, PURE, HSB personal cyber) [background]. Putting it in a commercial form raises filing questions and invites verification fights. No demand found. **Drop.** At most, mention a personal-cyber cross-sell in the strategy note.

**B3. AI voluntary shutdown.**
- **Market.** Beazley's endorsement (Sept 24, 2026) is the only one found [prior]. For a CPA firm, agent use is still low. Travelers says 89% of firms use AI and 59% govern it [snippet].
- **Change.** One sentence inside the T2-5/W-25 rewrite, under the $250K system-failure cap. Cheap, and a good interview point.

**B4. Small-loss safe harbor.**
- It exists nowhere in the US. It exists here only because Harborline has a ransomware coinsurance, which most US small-business forms don't carry [background].
- **Drop.** If the coinsurance costs sales, fix it directly: A2's "backups that worked anyway", or make the coinsurance a priced credit.

**B5. Precise "verified backups" definition.**
- Backup questions are on nearly every US application [background]. If Harborline keeps the coinsurance, an objective test prevents fights.
- **Change.** Use three tests: a restore tested in the last 12 months; an offline or immutable copy; and separate credentials or MFA for backup admin. Put the weekly and 30-day detail in the application, not the definition. Otherwise a technicality can trip the insured, which is the problem A2 exists to prevent.

**B6. Warning and cure.**
- No US form has this [background]. Harborline's late-notice prejudice rule (V.1.3) already covers most of the need.
- **Change.** One sentence for cooperation and document requests, with the claims-made deadline carved out. This is the lowest-priority Tier B item.

**B7. You need answer only what we asked.**
- Brokers fear rescission (*ICS*) [snippet]. This line plus V.3's honest-mistake rule is a real selling point to brokers.
- **Honesty point.** It would not have saved ICS, because the MFA question was asked. The honest-mistake re-rating rule would have. Keep it to one line.

**B8. Retention billed last.**
- **Market.** Absent [background].
- **Value.** Moderate at claim time. The owner avoids a $7,500 cash call in week one. Invisible at quote.
- **Change.** Make it a service standard ("we pay panel vendors in full and bill your retention; up to three monthly installments") rather than a coverage term. That keeps the credit exposure small.

**B9. Security services with a no-forfeiture promise.**
- **Services are table stakes.** Coalition Control, At-Bay, Travelers Cyber Risk Services (added to all policies in 2025), Cowbell Prime Plus, AIG's small CyberEdge tier and Hiscox Academy all bundle them [prior][catalog]. A buyer would notice their absence.
- **The promise is new.** It answers "if I ignore your alert, will you deny me?".
- **Change.** Keep the hybrid in report 10. Check SB25-058 and E&O exposure if an insurer-supplied MDR fails.

**B10. Verified-framework tier.**
- US credits are per control, not per framework [background]. An independent assessment is too costly for small firms.
- **Exception.** Tax and accounting firms must already keep a written security plan under the FTC Safeguards Rule [prior]. A credit for a current written plan that an IT provider attests to is cheap and relevant.
- **Make optional.** Put it in the rating manual, not the form.

**B11. Earn credits mid-term.** Rare and admin-heavy, with low demand. **Drop.** Handle it at renewal, or by endorsement on request.

**B12. $0 retention on panel forensics and breach coach.**
- **Market.** Coalition ($0 with its own IR team) and CFC (nil deductible; a separate IR limit is standard for SMEs) make this a line in quote comparisons [prior][snippet].
- Harborline's Coverage A is already $0 for 72 hours or $25K. B12 closes the rest of the gap.
- **Keep.** It pays for itself by pulling reports in early.

**B13. Policy at a glance.**
- Brokers use their own comparison grids. Owners buying direct, which is Corgi's channel, would use it.
- **Change.** Make it a non-contractual key-facts page that says the wording controls. Generate it last. Colorado misrepresentation risk applies if it contradicts the form.

**B14. Renewal "what changed" table.**
- Brokers already do this, and broker E&O claims over unflagged renewal changes are a known exposure [background].
- **Change.** Make it a renewal-notice commitment rather than policy text. Low cost, and brokers will like it.

**B15. Legal-deadlines card.**
- Useful for a CPA firm: the FTC Safeguards notice for 500+ customers, and the IRS Stakeholder Liaison contact after a breach [snippet][prior]. It's a service, not a term.
- **Change.** Move it to the Coverage A welcome pack and date it.

**B16. Publish claims results against service aims.** No US carrier publishes this, and brokers judge claims service by experience. **Drop.** At most, one line in the strategy note.

### Tier C

**C1. Fast Downtime Payment.**
- **Market.** In the US this is AIG with Parametrix (Aug 2026) and Parametrix direct [prior]. Both are aimed at larger buyers.
- **Why interest exists.** After CrowdStrike, brokers reported many outages ended inside 8–12-hour waiting periods and paid nothing. Some forms covered only malicious events, or put system failure under sublimits [snippet].
- **Risk.** CPA firms share tax and payroll platforms, so accumulation is severe. Filing is hard. Basis-risk complaints are likely.
- **Make optional.** "Test next", as report 10 says.

**C2. One limit reinstatement.**
- **Market.** CFC markets unlimited reinstatements to US brokers (its "two policies for the price of one" case study) [snippet]. It's rare on admitted paper.
- **Value.** A comparison talking point. It's rarely needed at $1M for a firm this size.
- **Make optional**, with an aggregate treaty behind it.

**C3. AI regulatory defense.** Only Beazley offers it (Sept 2026) [prior]. There is no enforcement yet, and Cedar Ridge's exposure is low. **Make optional later.** Check the exact name and date of Colorado's AI law before citing it.

**C4. $0 retention with MDR.**
- At-Bay InsurSec (Oct 2025) and Coalition's shorter MDR wait are the references [prior]. It attracts good risks.
- **Make optional.** Merge it into Item 7 as the MDR row. It replaces "halves your retention"; it doesn't stack.

**C5. Goodwill payments.** US buyers expect credit monitoring and identity restoration, which Harborline's Coverage B already pays. Gift cards look like an admission to US plaintiffs' lawyers [background]. **Drop.**

**C6. Lookalike-domain fraud on clients.**
- **Market.** Invoice manipulation that follows a breach is common [prior]. Losses from impersonation without a breach are usually not covered [snippet]. NetDiligence puts domain and brand-impersonation losses at about $1.57B in 2020–24 claims data [snippet].
- **Value.** Real for a CPA firm, but mostly as a client-liability exposure, which belongs in professional liability.
- **Make optional and price it.** Limit it to the firm's own lost fees and response costs.

**C7. Risk classes.** US underwriting already does this in the rating plan and appetite guides [background]. In the form it reads as extra prerequisites. **Drop from the form.**

**C8. Distribution.**
- **Market.** BOP cyber endorsements usually run $25K–$100K and often leave out social engineering [snippet]. That is the upgrade market for a Harborline-style standalone form.
- **Affinity.** The AICPA program is written by CNA and run by Aon [snippet], which shows affinity distribution works for CPAs.
- **Keep** as one strategy line: a state CPA society affinity plus MSP partners.

---

## 4. Skip-list check (report 10, section 6)

| Skipped idea | Is it expected in the US? | Should Harborline un-skip it? |
| --- | --- | --- |
| **Full-limit system failure** | **Common, not table stakes.** Coalition's surplus-lines form pays at full limit [prior]. Cowbell Prime 250 includes it; Prime 100 excludes it; Vouch sells it as an option; BBR 5.0 adds it to data recovery [prior]. After CrowdStrike, brokers focus on waiting periods and malicious-only wording [snippet] | **Keep the $250K core**, but **price and show a buy-up** in Item 6 ("higher limits available" must be real). Say plainly in the rationale that Coalition's surplus-lines form is broader here |
| **Full-limit non-IT contingent BI** | Rare (Coalition's form covers non-IT providers' system failures) [prior] | Keep skipped. Option P covers it |
| Unlimited reinstatements | CFC and Coalition (surplus lines) [snippet][prior] | Keep skipped; C2 is the bounded version |
| Widespread-event limit | Chubb only [prior] | Keep skipped |
| Parametric supplier downtime | Absent in US small-business cover | Keep skipped |
| **Criminal reward** | **In Coalition's US base form ($25K)** [snippet] and in TMHCC healthcare cyber [prior]. Uncommon elsewhere. No buyer asks for it | Skipping is fine. It will show as a "no" against Coalition's coverage checklist [snippet]. If the page budget allows, add two lines: up to $25K, at our discretion, excluding anything sanctions law forbids. It costs almost nothing |
| Free insurance with a certification | Absent in the US | Keep skipped |
| German fault quota; France complaint condition; EU statutory mechanics; GDPR, NIS2, DORA; "state of the art"; Québec; AU and SG regimes | Not US concepts | Keep skipped |
| Chubb NSE | One carrier | Keep skipped (KEV rule) |
| Coalition EBR set; vanishing retention; pre-claim help | Coalition only; Harborline has them | Keep skipped |
| Contingent BI and property damage wrap (C&F) | Rare, and for industrial classes | Keep skipped for CPA firms |
| Goods-diversion fraud; warranty plus insurance | Not relevant | Keep skipped |

**Net:**
- Nothing on the skip list is table stakes.
- Two items are worth a visible nod in the rationale: a full-limit system-failure buy-up, and criminal reward as a cheap optional line.

---

## 5. What US small-business buyers ask for most in 2025–26, and whether the list covers it

| Buyer or broker priority | Evidence | Covered by the idea list? |
| --- | --- | --- |
| **Price and speed** in a soft market | US cyber rates −2% (Marsh, Q2 2026) and −3.2% (CIAB) [prior]; CRC 2026 says buyer-friendly [snippet]; fast-bind platforms (Embroker) [snippet] | Not a wording item. Watch the premium: every add-on must earn its cost on a $5.5K policy |
| **Social-engineering and funds-transfer fraud limits** (sublimits of $100K–$250K are the top complaint) | [snippet]; At-Bay fraud data [prior] | **Partly.** A3 fixes the trigger but not the $250K limit. For a payroll firm, brokers will want $500K–$1M. Option R exists but is tied to endpoint MDR. Tie it to email security or verified callback instead [prior] |
| **Ransomware and BI, with waiting periods and outage definitions** | CrowdStrike and AWS commentary [snippet] | Partly: A10, C1. Harborline's 8-hour wait is at market |
| **Cloud outage / system failure / dependent BI** | [snippet][prior] | Partly (A10, C1). Full-limit buy-up **missing** (section 4) |
| **Affirmative AI and deepfake cover** | 54% worried (Travelers Risk Index 2026) [snippet] | Yes. Harborline already affirms AI; B1 and B3 add to it |
| **Breach response outside the aggregate** (or a big separate response limit) | Coalition separate-limits endorsement; BBR per-person services; CFC separate IR limit for SMEs [prior][snippet] | **Missing entirely.** Harborline puts only $25K / 72 hours outside the aggregate. A broker comparing against BBR or CFC will see it. Consider an optional separate $250K breach-response limit |
| **Low or zero retention** | Coalition, CFC, At-Bay [prior][snippet] | Yes: B12, C4, A6 |
| **Bundled security services** | Near-universal [prior] | Yes: B9 |
| **No denial over controls or the application** | [snippet]; *ICS* | Yes: A2, B7 and the existing V.3 |
| **CPA-specific: client funds and payroll accounts** | *Taylor & Lieberman*, *RealPage* [snippet] | Yes: A3 |
| **CPA-specific: redirected tax refunds and client tax identity theft** (altered returns; IRS notice) | [snippet] | **Missing.** Add IRS identity-theft help for affected clients (for example, help filing IRS identity-theft forms) as a line in Coverage B. Decide whether refund redirection is H or I |
| **CPA-specific: fit with accountants' professional liability** | Professional liability doesn't cover breach costs; cyber doesn't cover professional errors [snippet] | **Missing.** Add an "other insurance" line that makes cyber respond to claims arising from a security failure even if the professional liability policy might also respond, or a coordination note |
| **Contract and client requirements** (certificates, limits clients demand) | [background] | Not in the list. Minor |

**High-demand items missing from the list entirely:**
1. breach response outside the aggregate;
2. a social-engineering limit sized for payroll firms (and Option R tied to the right control);
3. a visible full-limit system-failure buy-up;
4. CPA tax-refund and IRS identity-theft help;
5. coordination with the firm's accountants' professional liability policy.

---

## 6. Verify before quoting

1. **Coalition's surplus-lines Active Cyber Policy base form:**
   - court attendance and criminal reward moved into the base form;
   - criminal reward is up to $25K.

   Source: Coalition help-center snippet. Open the Active Cyber Policy FAQ and a specimen.
2. ***Taylor & Lieberman v. Federal Ins. Co.*** (9th Cir. 2017, unpublished): citation, the amount (about $94K per snippet) and the exact holdings.
3. ***RealPage v. National Union*** (5th Cir., Dec 22, 2021, No. 21-10299): the "held" holding and the $6M net loss.
4. ***Mississippi Silicon Holdings v. AXIS*** (5th Cir., Feb 2021): the $100K social-engineering payment and the "knowledge or consent" holding.
5. ***Pestmaster Services v. Travelers*** (9th Cir. 2016): background only. Confirm the facts before citing.
6. ***CiCi Enterprises v. HSB Specialty*** (N.D. Tex., Feb 23, 2026): the docket, whether it went to trial or settled, and At-Bay's role as MGA.
7. ***Travelers v. ICS***: C.D. Ill., 2022 (stipulated rescission). One vendor blog misdates it to 2024.
8. ***Columbia Casualty v. Cottage Health*** (C.D. Cal. 2015): dismissed for failure to mediate. Don't describe it as a ruling on the exclusion.
9. **CFC US products:** unlimited reinstatements, a single aggregate excess, nil deductible, and whether they are written on US surplus-lines paper.
10. **Travelers Risk Index 2026:**
    - 58% name cyber as the top concern;
    - 54% worry about AI phishing and deepfakes;
    - small-business cyber buying is 50%, up from 43%;
    - 89% use AI and 59% govern it.
11. **CIRCIA final rule** status as of today (the target was September 2026).
12. **NetDiligence:** about $1.57B of domain and brand-impersonation losses (Dec 2025 blog).
13. **Court attendance amounts:** MICA $10K; the $2K-a-day, $100K form (the host document's carrier is unknown).
14. **Don't cite these vendor-blog statistics:**
    - "82% of denials involve MFA";
    - "40% of claims denied";
    - "74% closed without payment";
    - "carriers excluded deepfakes on 1/1/2026";
    - "Lloyd's and Munich Re require voice biometrics".
15. **Background items to check before relying on them:**
    - foreign regulators in standalone "regulatory proceeding" definitions (e.g., BBR);
    - rarity of ransomware coinsurance in US small-business forms;
    - accountants' professional liability trial-attendance pay;
    - state notice-of-reduced-coverage renewal rules.
16. **Colorado AI law:** name, bill number and effective date, before C3 cites it.

---

## Sources (search results, Sept 27, 2026; none opened)

**Cases and disputes**
- *Taylor & Lieberman*: [Lexology](https://www.lexology.com/library/detail.aspx?g=1bbfe97f-27f4-4aa1-82e2-55c6047c29b6); [FindLaw](https://caselaw.findlaw.com/court/us-9th-circuit/1852086.html); [SFAA](https://surety.org/law_library/taylor-lieberman-v-federal-insurance-company/)
- *RealPage*: [Justia](https://law.justia.com/cases/federal/appellate-courts/ca5/21-10299/21-10299-2021-12-22.html); [Traub Lieberman](https://www.traublieberman.com/perspectives/fifth-circuit-finds-no-coverage-for-6m-phishing-scheme-loss-where-insured-never-held-client-funds); [PropertyCasualtyFocus](https://propertycasualtyfocus.com/fifth-circuit-affirms-finding-of-no-coverage-for-phished-funds-never-held-by-insured/)
- *Mississippi Silicon*: [FindLaw](https://caselaw.findlaw.com/court/us-5th-circuit/2110118.html); [Hinshaw](https://www.hinshawlaw.com/newsroom-updates-computer-fraud-and-funds-transfer-fraud-coverages-not-triggered-by-social-engineering-phishing-scam.html); [Business Insurance](https://www.businessinsurance.com/article/20210205/NEWS06/912339623/Axis-wins-computer-fraud-case-with-silicon-maker-Burnside-Mississippi-Mississipp)
- *CiCi v. HSB*: [Insurance Business](https://www.insurancebusinessmag.com/us/news/cyber/court-blocks-hsbs-ransomware-sublimit-in-firstofitskind-cyber-ruling-567006.aspx); [Hunton](https://www.hunton.com/hunton-insurance-recovery-blog/court-refuses-to-slice-up-cicis-cyber-extortion-coverage); [Business Insurance](https://www.businessinsurance.com/ransomware-sublimit-doesnt-apply-to-cyber-claim-court/); [Legal 500](https://www.legal500.com/intelligence/united-states/insurance/court-rejects-insurers-attempt-to-cap-cyber-extortion-coverage-based-on-ransomware-sub-limit)
- *Cottage Health* / failure to maintain: [Reed Smith](https://www.reedsmith.com/articles/cyber-insurance-claims/pressure-points-in-cyber-insurance-policies-revealed-in-litigation/); [Business Insurance 2015](https://www.businessinsurance.com/article/20150515/NEWS06/150519893/Insurer-cites-cyber-policy-exclusion-to-dispute-data-breach-settlement-); [Technethics](https://www.technethics.com/columbia-casualty-v-cottage-health-system-i-e-when-your-cyber-insurance-is-not-what-it-seems/)
- *Travelers v. ICS* / MFA denials (low reliability): [Triton](https://tritoncomputercorp.com/blog/2026/05/01/why-cyber-insurance-policy-void-travelers-ics-declarations/); [Securafy](https://blog.securafy.com/cyber-insurance-attestation-trap-mfa-denied-claims)
- Social-engineering denial patterns: [Ward and Smith / NLR](https://natlawreview.com/article/social-engineering-fraud-and-your-crime-policy-why-your-insurer-may-deny-claim-and); [Aon FSG](https://www.aon.com/risk-services/financial-services-group/the-evolving-nature-of-social-engineering-claims)
- Client funds held in trust: [L Squared](https://www.l2insuranceagency.com/blog/why-law-firms-with-trust-and-fiduciary-departments-need-professional-liability-cyber-insurance-and-crime-insurance/); [Lockton Affinity](https://locktonaffinityadvisor.com/blog/understanding-the-fraud-coverage-within-a-cyber-liability-policy-computer-fraud-vs-funds-transfer-fraud/)

**Outages**
- CrowdStrike: [IRMI](https://www.irmi.com/articles/expert-commentary/coverage-for-the-crowdstrike-incident-under-cyber-insurance); [Coalition](https://www.coalitioninc.com/blog/crowdstrike-outage); [Coyle Group](https://thecoylegroup.com/the-crowdstrike-debacle-and-cyber-insurance/); [Aon](https://www.aon.com/en/insights/alerts/crowdstrike-and-windows-event-briefing-implications-and-initial-findings-for-cyber-reinsurers)
- AWS Oct 2025: [Claims Journal](https://www.claimsjournal.com/news/national/2025/10/23/333667.htm); [Moody's](https://www.moodys.com/web/en/us/insights/insurance/understanding-insured-losses-from-the-october-aws-cloud-outage.html); [Risk & Insurance](https://riskandinsurance.com/aws-outage-loss-estimates-range-from-38m-to-581m-as-cyber-insurers-face-moderate-impact/)

**Products and features**
- Coalition court attendance and criminal reward: [Coalition help center](https://help.coalitioninc.com/hc/en-us/articles/7665533052315-What-is-Coalition-s-Criminal-Reward-Coverage); [ACP FAQ](https://help.coalitioninc.com/hc/en-us/articles/33998071846811-Active-Cyber-Policy-FAQ); [Coverage checklist](https://assets.ctfassets.net/o2pgk9gufvga/6GDAqNBNDON9cmkVdLCzd5/363be97c2125f8b89a7ca2a0515fd786/Coalition_Coverage-Advantage-Checklist-US.pdf)
- Court attendance elsewhere: [MICA e-Med](https://www.mica-insurance.com/media/bffjzlav/micas-e-med-protection.pdf); [ACWA JPIA 2022 policy](https://www.acwajpia.com/wp-content/uploads/emember/downloads/2022%20Cyber%20Liability%20Policy.pdf)
- CFC: [Unlimited reinstatements](https://www.cfc.com/en-us/knowledge/resources/articles/2024/07/cyber-coverage-highlights-unlimited-reinstatements/); [5 steps / CPR](https://www.cfc.com/en-us/knowledge/resources/articles/2025/07/assessing-the-adequacy-of-our-cyber-insurance-coverage/); [Nil deductible](https://www.cfc.com/en-us/knowledge/resources/articles/2025/03/cyber-product-enhancements-nil-deductible/); [Two policies case study](https://www.cfc.com/en-us/knowledge/resources/case-studies/cyber-claims-case-study-two-policies-for-the-price-of-one/)
- Deepfake: [Coalition via fintech.global](https://fintech.global/2025/12/18/coalition-adds-deepfake-cover-to-cyber-insurance/); [CyberScoop](https://cyberscoop.com/url-coalition-cybersecurity-insurance-coverage-deepfakes-reputational-harm/); [BOXX](https://www.insurancebusinessmag.com/us/news/cyber/boxx-insurance-adds-affirmative-ai-and-deepfake-coverage-to-cyberboxx-business-policy-583408.aspx); [Embroker](https://www.embroker.com/blog/risk-management/deepfake-fraud-insurance-gaps/)
- Impersonation / lookalike domains: [NetDiligence](https://netdiligence.com/blog/2025/12/understanding-domain-security-brand-impersonation/); [Amwins](https://www.amwins.com/resources-and-insights/market-insights/article/how-cyber-and-crime-insurance-policies-respond-to-social-engineering)
- BOP cyber limits: [Vantage Point](https://vantagepointrisk.com/learning-center/standalone-cyber-vs-bop-cyber/); [myhaus](https://www.myhaus.com/blog/will-a-cyber-data-endorsement-protect-my-business); [The Hartford](https://www.thehartford.com/cyber-insurance)

**Market and buyers**
- Travelers Risk Index 2026: [Travelers IR](https://investor.travelers.com/newsroom/press-releases/news-details/2026/Travelers-Risk-Index-Cyber-Threats-Return-as-the-Top-Business-Concern/default.aspx); [Claims Journal](https://www.claimsjournal.com/news/national/2026/09/23/340321.htm); [Risk & Insurance](https://riskandinsurance.com/cyber-threats-top-business-concerns-agains-as-ai-reshapes-risk-travelers-survey/)
- CRC 2026: [At a glance](https://www.crcgroup.com/Tools-Intel/Specialty-Tools-Intel/2026-cyber-state-of-the-market-at-a-glance); Amwins 2026: [Outlook](https://www.amwins.com/resources-and-insights/market-insights/article/state-of-the-market-2026-outlook)
- Small-business sublimits and waiting periods (low reliability): [beancount.io](https://beancount.io/blog/2026/05/09/cyber-insurance-small-business-2026-mfa-requirements-ransomware-coverage-premium-benchmarks); [Huntress](https://www.huntress.com/blog/cyber-insurance-trends)
- CPA firms: [Seedpod](https://seedpodcyber.com/cyber-insurance-for-accounting-firms/); [CalCPA](https://www.calcpa.org/whats-happening/california-cpa-magazine/when-ransomware-hits-a-cpa); [ABA wire-fraud liability](https://www.americanbar.org/groups/tort_trial_insurance_practice/resources/brief/2025-spring/lawyer-liability-wire-transfer-fraud/)

**Law**
- CIRCIA: [Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/cisa-plans-to-finalize-cyber-incident-reporting-regulations-in-september-2026); [CISA](https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia)
- State ransom-payment bans: [CPO Magazine](https://www.cpomagazine.com/cyber-security/patchwork-of-us-state-regulations-becomes-more-complex-as-florida-north-carolina-ban-ransomware-payments/); [Aon](https://www.aon.com/risk-services/professional-services/ransomware-payment-prohibitions-do-they-work-and-will-more-states-adopt-them)

**Prior reports reused:** 02 (feature matrix, Coalition, At-Bay, Cowbell, Corgi), 04 (rates, AWS and CrowdStrike, carriers), 10 (idea list), 10a–10d (source drafts). **Catalog rows:** Travelers CYB-14306 and CYB-16001; HSB CSC 02-2025; TMHCC NGP 1000; AIG small CyberEdge; Hartford CyberChoice; C&F Simple Cyber v6.0.
