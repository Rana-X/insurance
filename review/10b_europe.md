# 10b. Continental Europe: SMB cyber ideas worth adapting for Harborline

Prepared September 27, 2026. Scope: continental European small-business cyber policies and regulation, 2023–2026 (Germany, France, Switzerland, the Netherlands, Spain, plus EU-level context). Harborline context: a US admitted policy for businesses with $1M–$50M revenue, sample insured Cedar Ridge (a Denver CPA firm), Colorado law.

**Evidence caveat (read first).** Nothing in this report was opened at source. The network blocked every primary document I tried: curl to gdv.de, and WebFetch to content.markel.com, gesetze-im-internet.de, legifrance.gouv.fr and brochureware.hiscox.de. I didn't retry any blocked domain. No European wordings were in the local `policies/` folder. So the evidence is at four levels, each marked on every item:

| Label | Meaning |
| --- | --- |
| **opened** | Primary document read. *None in this report.* |
| **snippet** | Search-engine summary or result snippet. "Title only" means only the result title was seen. |
| **catalog** | Note in `/home/user/insurance/catalog/cyber_policies.csv` / `CATALOG.md` (itself mostly snippet-level). |
| **background** | My own knowledge of the statute or market, not checked this session. |

I used all 20 web searches. Nordic and Italian carriers weren't searched, and that is a gap. Every "draft" clause below is **new Harborline wording**. None of it is carrier text. Carrier or statute wording appears only as short paraphrases or labeled snippet phrases.

---

## 0. Bottom line

1. **Europe's best idea for Harborline is how conduct affects payment, not a coverage grant.** German law (VVG §28), the GDV model conditions and Swiss law (revised VVG Art. 45, 2022) apply a security lapse only if **(a)** it was more than ordinary negligence and **(b)** it actually caused or enlarged the loss. Harborline already avoids security *exclusions*. It should adopt the **causation rule** and the **"ordinary mistakes never count"** rule. It should **not** adopt the German *fault-degree quota* (reducing payment "in proportion to the severity of fault"). In a Colorado admitted form that becomes a discretionary percentage fight under the bad-faith statute, and it can't be priced. Harborline's "we told you in writing and you didn't fix it within 45 days" rule already works as an objective, fileable stand-in for "gross negligence".
2. **Small-loss safe harbor.** Hiscox Germany reportedly waives the gross-negligence defense for losses up to €50,000. The adaptation: Harborline's coinsurances apply only to covered loss above the first $50,000. Most SMB claims then pay fast and in full.
3. **Security tooling in the policy.** Stoïk (France, now distributed with MMA) and Dattak bundle attack-surface scans, cloud-configuration scans and phishing simulations in the premium. Swiss carriers (Mobiliar, Zurich, AXA) include staff awareness training. This fits Harborline's scan-based design. It must be **written into the filed form**, never used as an off-policy inducement, and never made a condition of coverage.
4. **Credits should work both ways mid-term.** Today Harborline credits can only be *lost* mid-term. The Dattak/Stoïk "dynamic" model lets them be *earned* mid-term too.
5. **France's 72-hour criminal complaint rule (LOPMI) must not be copied as a forfeiture.** Its useful kernel is a service: "our team helps you file the FBI/IC3 report within 72 hours". Planned fix T2-19 already covers the one real condition, a report before any consented ransom.
6. **Transparency tools.** Three are worth adapting: the EU's standard one-page product summary (IPID); Hiscox Germany's side-by-side "what changed" synopsis at renewal; and the Dutch public-private risk-class scheme, which ties expected controls to a firm's risk class. The risk-class scheme is the cleanest answer to the open review question "credits or bind prerequisites?"

Verdict count across 20 items: **ADOPT 5 · ADAPT 10 · OPTIONAL 2 · SKIP 3.** Harborline already has, or has planned, the substance of six of them.

---

## 1. Summary table

"Has it?" means whether Harborline already has the substance. The "Planned fix" column cross-references `README.md`.

| # | Idea | Source (country) | Evidence | Verdict | Has it? | Planned fix overlap |
| --- | --- | --- | --- | --- | --- | --- |
| E1 | Security duties apply only with fault **and causation**; ordinary negligence never counts; intent forfeits | GDV AVB Cyber (Feb 2024) + VVG §28 (DE); revised VVG Art. 45 (CH, 2022) | snippet + background | **ADAPT** (causation and fault tiers yes; fault-degree quota no) | Partly (KEV coinsurance is causation-based; ransomware coinsurance isn't) | T2-6, T2-17 |
| E2 | "Disguised obligation" rule: a conduct-based exclusion is treated as a duty, so the protections apply | German case law (BGH doctrine) | background | **ADOPT** (as a drafting rule) | Mostly (IV.1 "security lapses") | T2-1d, T2-17 |
| E3 | Gross-negligence waiver for losses up to €50K; no "market-usual" pre-loss duties | Hiscox DE (CyberClear / "Cyberversicherung by Hiscox") | snippet | **ADAPT** (first-$50K safe harbor) | No | T2-6 |
| E4 | Precise, testable backup standard (weekly; offline or immutable; admin access behind 2FA or separate domain; 30-day retention) | Hiscox DE (source page not identified) | snippet | **ADAPT** (define **verified backups**) | Partly (III.1.6) | T2-6, T3-1 |
| E5 | You need disclose only what the insurer asked in writing; separate warning of consequences | VVG §19 (DE) | background | **ADOPT** | No (V.3 covers the remedy, not the scope) | T2-13, T2-7 |
| E6 | No penalty for a post-loss duty unless the insurer first warned you in writing | VVG §28(4) (DE) | background | **ADOPT** (cure notice) | No | T1-6, T2-12 |
| E7 | 72-hour criminal complaint as a condition of paying cyber-attack losses | France, LOPMI, Code des assurances Art. L12-10-1 (in force Apr 24, 2023) | snippet | **ADAPT** (service, not forfeiture) | Partly (III.3.5, III.6.3) | T2-19 |
| E8 | Security platform in the premium: external scans, AD and cloud (M365) scans, phishing simulation, in-house 24/7 incident response | Stoïk (FR; MMA partnership Apr 2026); Dattak (FR) | snippet | **ADAPT** (filed "protection services") | Partly (pre-issue scan, KEV notices) | T2-7 |
| E9 | Free staff awareness training included (e.g., 12 months) | Mobiliar, Zurich (SoSafe), AXA (CH) | snippet | **ADAPT** (inside E8's clause) | No | none |
| E10 | "Dynamic" cover: posture and terms update during the term | Dattak, Stoïk (FR) | snippet | **ADOPT** (earn credits mid-term) | No (credits can only be lost, III.1.5) | T2-16 |
| E11 | Standardized SME security check done by an IT provider and accepted by insurers | DIN SPEC 27076 CyberRisikoCheck (BSI/BVMW, DE); MonAideCyber (ANSSI, FR) | snippet | **ADAPT** (IT-provider attestation) | No | T3-7 |
| E12 | Standard one-page product summary with fixed questions ("What is not insured? Are there restrictions? What are my obligations?") | EU IPID (IDD); French "very apparent" exclusions rule | catalog + background | **ADAPT** ("Policy at a glance") | Partly (cover page "What's inside") | T2-17, T2-1e |
| E13 | Side-by-side "what changed" synopsis when the wording changes | Hiscox DE synopsis 10/2023 | snippet (title only) | **ADOPT** | No (liberalization only, V.11.7) | none |
| E14 | Industry-standard non-binding model wording as a benchmark; SMB FAQ on the war exclusion | GDV AVB Cyber; Gothaer FAQ | snippet + catalog | **OPTIONAL** (rationale only) | n/a | T4-9 |
| E15 | Public-private risk classes that set the expected controls, plus an SME security certification mark | Netherlands: CCV / Verbond van Verzekeraars risk classification; "Keurmerk Digitale Basisveiligheid MKB" | snippet | **ADAPT** (risk-class table in Item 7) | No | Review item 11; T2-16 |
| E16 | Micro-SME "Kompakt" tiers and industry-class tariffs with short questionnaires | ERGO Kompakt, rhion CVK, AXA ByteProtect Kompakt, Hiscox CyberClear Start, ERGO Branchentarif (DE) | catalog | **OPTIONAL** (future "Essentials" edition) | No | none |
| E17 | 2024 war update: war needn't be physical; exclusion for state attacks on critical infrastructure | GDV AVB Cyber (Feb 2024) | snippet | **SKIP** | Yes, and Harborline's is more insured-friendly | T2-9 |
| E18 | Cloud-provider data events covered, provider *outage* not; technical-failure BI sublimited (€250K) | GDV 2024; Markel Pro Cyber v2; SV BI module (Sept 2024) | snippet + catalog | **SKIP** | Yes (E, P, $250K system-failure sublimit) | T2-0, T2-3 |
| E19 | Staged incident-reporting clocks (24h / 72h / 1 month) | NIS2 Art. 23 (EU) | background | **ADAPT** ("legal clock card" with US clocks) | Partly (back page, Coverage A) | T1-10 |
| E20 | Regulatory fines "where insurable" | GDPR fines: insurable in only 2 of 30 countries (Aon/DLA Piper 2018) | snippet | **SKIP** (EU-specific) | Yes | T1-8 |

---

## 2. Special focus: how the GDV/German model handles security duties, and what translates to Colorado

### 2.1 How the German system works

**The model wording.** The GDV (German Insurance Association) publishes the *AVB Cyber*. These are non-binding model conditions designed with SMEs in mind. They were first published in 2017 and revised in February 2024. The catalog dates the current PDF to 2024-02. Its structure is Part A: A1 general, A2 service and cost modules (before and after a loss), A3 liability, A4 own damage including BI and data restoration. Part B holds general conditions. [catalog; press coverage Feb 19, 2024, snippet]

**The security duties ("Obliegenheiten").** These are *conduct duties*, not exclusions or warranties. The 2024 revision rewrote them "to reflect the current state of technology and to be easier to understand". The baseline named in press coverage: regular backups, strong passwords, individual accounts, virus scanners, firewalls and promptly installed security updates. [GDV press release and trade press, Feb–Mar 2024, snippet]

**The statutory consequence scheme (VVG §28, since the 2008 VVG reform abolished the old all-or-nothing rule).** It is semi-mandatory for SMEs: VVG §32 bars deviations to the policyholder's detriment, except for "large risks" under §210. [§28(2) snippet; rest background]

| Breach of a pre-loss duty | Consequence |
| --- | --- |
| Not at fault, or ordinary (simple) negligence | **No reduction** |
| Gross negligence | Insurer may reduce payment **"in proportion to the severity of the fault"**. The policyholder bears the burden of disproving gross negligence (§28(2)). |
| Intent | Insurer is free of liability (§28(2)) |
| Any of the above, but the breach **did not cause** the insured event, its determination or the amount of the loss | **Full payment** (causation counter-proof, §28(3)). This isn't available if the breach was fraudulent. |
| Post-loss information duties | Any reduction requires that the insurer warned the policyholder in a **separate written notice** (§28(4)) |
| Pre-loss duty breach | Insurer may terminate within one month of learning of it, unless the breach was neither intentional nor grossly negligent (§28(1)) |

A parallel rule, VVG §81(2), lets the insurer reduce payment in proportion to fault where the policyholder *caused the insured event* by gross negligence.

**Switzerland moved the same way in 2022.** Under revised VVG Art. 45, an agreed penalty for breaching a duty doesn't apply if the breach was not culpable, **or** if the policyholder shows the breach had no influence on the loss event or on the amount owed. [snippet: Bär & Karrer; justement.ch]

### 2.2 What the German courts have done with it (2023–2024)

| Case | Holding (as reported) | Lesson for Harborline | Evidence |
| --- | --- | --- | --- |
| **LG Tübingen, May 26, 2023, 4 O 193/21.** First German cyber judgment: ransomware, about €2.86M restoration costs | Rejected a §81(2) gross-negligence reduction. The security gaps already existed at inception, and the insurer had chosen not to examine them, so it **accepted the status quo** | This is the German twin of Harborline's "what our scan saw, we accept" (V.3.4). It supports keeping that rule, narrowed per T2-7 | snippet (vsma.de; wilhelm-rae.de; gleisslutz.com) |
| **LG Kiel, May 23, 2024, 5 O 128/21** | Risk-question answers on malware protection and updates were false. The court held this was fraudulent misrepresentation, so the insurer could avoid the contract (§123 BGB) | Once insurers drop technical duties, **the application becomes the battleground**. Harborline's "rescission only for knowing misstatements" (V.3.3) is right, and E5 plus T3-2 (removing application traps) matter more | snippet (dr-bahr.com; experten.de) |
| **LG Hagen, 9 O 258/23** | Reported as stressing the AVB's role and the policyholder's prevention and proof duties. Details not seen | Unknown. Verify before citing | snippet (title and summary only; ferner-alsdorf.de) |

**The market trend.** Some German carriers now advertise that they **waive "market-usual" pre-loss security duties**. Hiscox Germany is one [snippet]. A Noerr article titled "Der Verzicht auf technische Obliegenheiten und seine Folgen" ("waiving technical duties and its consequences") analyzes the effect [title only]. The consequence is visible in Kiel: the insurer's defense moves to misrepresentation in the risk questionnaire.

### 2.3 Harborline's current approach, mapped onto the German scheme

| German mechanism | Harborline equivalent | Gap |
| --- | --- | --- |
| Duties with fault-graded consequences | No duties. Security affects **price** (credits, Item 7) and three **disclosed penalties**: ransomware coinsurance (III.1.6), KEV coinsurance (III.1.7) and the callback cap (III.6.1) | None in principle. Harborline is simpler |
| Causation counter-proof (§28(3); CH Art. 45) | KEV coinsurance applies only to an incident "it causes". The callback cap applies only when an employee acts on an unverified instruction | The **ransomware coinsurance has no causation link**: it applies even to data-theft extortion where backups are irrelevant. T2-6 narrows its scope. E1 supplies the principle behind that fix |
| Ordinary negligence → no penalty | III.6.2 "one slip does not cut your limit" (fraud only) | Not general. E1 generalizes it |
| Gross negligence → quota | The KEV rule: *we told you in writing, and you left it unpatched and unmitigated for 45 days*, so you pay 20% | This is effectively an **objective, pre-priced definition of gross negligence**. Keep it |
| Intent → forfeiture | Exclusion 4 (intentional wrongdoing by executives) | Fine, with T2-1h/T2-11 fixes |
| Insurer bears the burden? | The war exclusion puts the burden on Harborline. Elsewhere the policy is silent | In Germany and Switzerland the *policyholder* proves non-causation. Harborline can go further for the insured (see the E1 draft options) |

### 2.4 Does a proportional "fault-based reduction" translate to US/Colorado law?

**Short answer: the structure translates; the discretionary fault quota doesn't.**

1. **No statutory home.** US insurance law has no counterpart to VVG §28. Coverage conditions are generally enforced all-or-nothing, softened by case-law doctrines: notice-prejudice (which Colorado applies to occurrence policies but not to claims-made reporting deadlines, per *Craft*, a package source), construing ambiguity against the insurer, waiver and estoppel, and some states' "contribute-to-loss" statutes [background]. A German-style quota would be purely contractual, and courts would have no body of case law to calibrate "severity of fault". Germany has built its body since 2008.
2. **Bad-faith exposure.** Colorado lets first-party claimants recover twice the covered benefit plus fees for unreasonable delay or denial (C.R.S. 10-3-1115/1116, package source). Every discretionary percentage ("we reduce by 40% because your fault was serious") becomes a reasonableness question for a jury. A fixed 20% triggered by an objective fact doesn't.
3. **Form filing and clarity.** A term letting the insurer choose a reduction by degree of fault is open-ended. It invites a regulator objection that it is ambiguous, and courts would construe it against Harborline [background; confirm Colorado's form-review standard].
4. **Pricing and reinsurance.** A fixed coinsurance can be rated and reinsured. A judge-set quota can't.
5. **Where US practice already converges.** US practice uses fixed, disclosed risk-sharing: backup coinsurance, sublimits without callback, and Chubb's Neglected Software Exploit tiers (package source; percentages unconfirmed). The closest common-law cousin is **UK Insurance Act 2015 s.11**, which the rationale already borrows for honest mistakes: an insurer can't rely on a breached risk-control term if the breach could not have increased the risk of the loss that actually occurred [background].

**Recommendation.** Take the German *architecture*:
- intent forfeits;
- ordinary mistakes never count;
- the middle band triggers a **fixed, filed** share;
- nothing applies without **causation**.

Then express the middle band through objective triggers, as Harborline already does ("notified in writing + 45 days"), never through "degree of fault". Drafts are in E1 and E2.

---

## 3. Item cards

Each card lists: source · what it does · why it helps SMBs · evidence · verdict · Harborline status · draft (ADOPT/ADAPT only) · where it goes · conflicts.

### Theme A: Security duties and conduct-based terms

#### E1. Fault- and causation-gated security terms

- **Source.** GDV *AVB Cyber*, Feb 2024 revision (catalog dates the PDF 2024-02), whose security duties operate through VVG §28. Also Swiss revised VVG Art. 45 (in force Jan 1, 2022).
- **What it does.** A security lapse reduces payment only if it was more than ordinary negligence and it caused or enlarged the loss. Intent forfeits cover.
- **Why it helps SMBs.** Small firms rarely have perfect hygiene. This rule stops a denial because an unrelated control was missing, which is the classic SMB grievance.
- **Evidence.**
  - GDV press release, Feb 2024: https://www.gdv.de/gdv/medien/medieninformationen/versicherungsschutz-gegen-cyberangriffe-gdv-veroeffentlicht-neue-musterbedingungen--168132 (snippet)
  - Versicherungsmonitor, Feb 19, 2024: https://versicherungsmonitor.de/2024/02/19/gdv-legt-neue-cyber-musterbedingungen-vor/ (snippet)
  - VVG §28: https://www.gesetze-im-internet.de/vvg_2008/__28.html (snippet for §28(2); rest background)
  - Swiss VVG Art. 45: https://www.baerkarrer.ch/de/publications/claims-made-policen,-art.-38-vvg-und-der-revidierte-art.-45-vvg (snippet)
  - Model PDF, 2024-02: https://www.gdv.de/resource/blob/6100/a0fed56c4947751cdc20b5206c171d98/01-allgemeine-versicherungsbedingungen-fuer-die-cyberrisiko-versicherung-avb-cyber--data.pdf (catalog; blocked)
- **Verdict: ADAPT.** Adopt causation, "ordinary mistakes never count" and one home for all conduct terms. **Skip** the fault-degree quota (section 2.4).
- **Status.** Partly. The KEV coinsurance and callback cap are causation-linked; the ransomware coinsurance isn't.

**Draft (Harborline wording). New Section III, part 1.9 "How your security can affect what we pay":**

> **9. How your security can affect what we pay.**
> 1. **Only three terms.** Only these terms can reduce what we pay because of how you manage security: the ransomware coinsurance (item 6 of this part), the known-exploited-vulnerability coinsurance (item 7 of this part) and the lower Coverage H limit for an unverified instruction (Section III, part 6, item 1). Section V, part 3 (your **application**) can also change your terms. Nothing else in this policy does.
> 2. **The gap must matter.** Each of these terms applies only to the extent that the missing control caused the **incident** or made the loss larger. If having the control would not have prevented the **incident** or reduced the loss, we pay as if it had been in place. *[Option A, more generous than Europe: "We must show this link." Option B, the European norm: "It applies unless you show the missing control made no difference."]*
> 3. **Backups that worked anyway.** If you restore the affected **digital assets** from your own backups, the ransomware coinsurance does not apply to that **incident**, even if your backups were not **verified backups**.
> 4. **Ordinary mistakes never count.** An honest mistake or one-off lapse by an **employee** or **executive** does not trigger any of these terms. Only the situations these terms describe do: backups not verified, a notified vulnerability left unpatched and unmitigated for 45 days, or an unverified payment instruction acted on.
> 5. **Credits work differently.** The security credits in Item 7 are part of your price. They follow whether the verified control is in place (item 5 of this part), whatever caused the **incident**.
> 6. This part does not change exclusion 4 (intentional wrongdoing).

- **Where.** Section III, part 1, after item 8. Cross-reference it from IV.1 "Security lapses" and Item 7.
- **Conflicts.**
  - **T2-6** plans to limit the ransomware coinsurance to restoration and BI from encryption. Part 9.2 reaches the same result by principle. Use both: T2-6's scope, plus 9.2 for anything left over.
  - **T2-17** (IV.1 must list all three disclosed penalties). Part 9.1 becomes the single list, and IV.1 points to it.
  - Credit loss in part 1.5 stays objective (9.5). Say so, or reviewers will ask why credits don't also need causation.
  - Option A is costlier to administer. Ransomware claims will need a short forensic causation note.

#### E2. "Disguised obligation" drafting rule

- **Source.** German case-law doctrine (*verhüllte Obliegenheit*): a clause drafted as an exclusion that really describes the insured's conduct is treated as a duty, so the VVG §28 protections (fault and causation) still apply.
- **What it does.** It prevents insurers from avoiding the protections by relabeling duties as exclusions.
- **Why it helps SMBs.** Harborline's promise "we don't exclude security lapses" only holds if *no* exclusion reintroduces conduct, such as exclusion 2's "should have known".
- **Evidence.** Background knowledge (doctrine well established in German insurance law). No specific judgment cited. Verify before naming one.
- **Verdict: ADOPT** as a drafting rule.
- **Status.** Mostly: IV.1 "Security lapses".

**Draft. Replace the IV.1 "Security lapses" bullet:**

> **Security lapses.** No exclusion in part 2, and no condition in Section V, applies because you failed to patch, back up, encrypt, configure or maintain a security control, or because you should have known about a vulnerability. The only ways your security practices can reduce what we pay are listed in Section III, part 1.9.

- **Where.** IV.1, first bullet.
- **Conflicts.**
  - **T2-1d** (known problems' "should have known" brings patching denials back). This sentence overrides it. Still make the T2-1d fix so the two don't read as a conflict.
  - The known-problems exclusion should keep applying to *known incidents and claims*, just not to security posture.

#### E3. Small-loss safe harbor (from Hiscox Germany's gross-negligence waiver)

- **Source.** Hiscox SA, Germany: CyberClear (the latest catalog edition is 06/2022) and "Cyberversicherung by Hiscox" (synopsis dated 10/2023). Reported features:
  - the insurer "waives the defense of gross negligence for losses up to €50,000";
  - the wording "does without market-usual pre-loss obligations".
- **What it does.** Small claims are paid without any argument about the insured's security conduct.
- **Why it helps SMBs.** Most SMB claims are small. A dispute-free zone speeds payment and builds trust at trivial expected cost.
- **Evidence.** Search summary drawn from these results, with the specific page not identified and the edition unknown (snippet):
  - https://www.hiscox.de/geschaeftskunden/cyber-versicherung/vergleich/
  - https://www.maklermitfliege.de/cyber-vergleich.html
  - https://www.cyberdirekt.de/wann-cyberversicherung-zahlung-verweigern-kann/

  It is unclear whether "up to €50,000" means the first €50K of any loss or only losses totaling €50K or less. **Verify before citing Hiscox.**
- **Verdict: ADAPT.** Use "first $50,000", which has no cliff. The alternative, losses totaling $50K or less, would make a $51K loss worse off than a $49K one.
- **Status.** No.

**Draft. Add to new III.1.9:**

> 7. **Smaller losses are paid in full.** The ransomware and known-exploited-vulnerability coinsurance apply only to covered loss above $50,000 for any one **incident**, after your **retention**. For the first $50,000, we pay as if your backups were **verified backups** and every vulnerability we notified you about had been fixed.

- **Where.** III.1.9, part 7, or a separate III.1.10.
- **Conflicts.**
  - It softens the KEV coinsurance, which the review endorsed as a clear alternative to Chubb's approach. Accept that, or exclude KEV from the safe harbor.
  - T2-6 non-stacking (a 20% total cap) still applies above $50K.
  - Pricing: the maximum give-back is $10,000 per incident (20% × $50K). State it in the rationale.
  - Has no effect on the callback cap, which only bites above $100K.

#### E4. A precise, testable backup standard

- **Source.** Search summary attributed to Hiscox Germany's conditions (edition not identified):
  - at least a weekly full backup;
  - either an offline backup permanently physically separated from the systems, or an immutable online backup that administrators can reach only with 2FA or from a separate domain;
  - kept at least 30 days.

  The same summary lists Hiscox's risk questions: layered permissions, firewall, updating antivirus, backups no older than a week, passwords, **four-eyes approval for transfers over €10,000**, 2FA for home office, and prompt updates.
- **What it does.** Replaces a vague "backups" duty with checkable criteria. The key one is credential separation: attackers delete backups with stolen admin credentials.
- **Why it helps SMBs.** The insured knows exactly what earns the credit, and the IT provider can attest to it (E11).
- **Evidence.** Snippet, from the search "Cyberversicherung by Hiscox grobe Fahrlässigkeit…". Results included https://www.kuv24-cyber.de/_downloads/assets/746_BEDINGUNGEN_Hiscox_CyberClear_202206.pdf and https://www.ing-ism.de/magazin/cyberversicherung-obliegenheiten-leitfaden-kmu/. The exact source isn't known. **Don't quote it as Hiscox text.**
- **Verdict: ADAPT.**
- **Status.** Partly. III.1.6 requires a restore test within 12 months plus an offline or immutable copy. It has no credential-separation or retention test.

**Draft. New Section II definition, which III.1.6 and Item 7 then use:**

> **Verified backups** means backups of your critical **digital assets** that, when the **incident** is discovered:
> 1. are made at least weekly;
> 2. include a copy that is offline (physically disconnected from your **computer systems**) or immutable (cannot be changed or deleted before its retention period ends);
> 3. cannot be deleted or changed using your everyday administrator accounts: access needs multi-factor authentication or a separate account or domain;
> 4. keep at least 30 days of restore points; and
> 5. have been successfully test-restored within 12 months before the **policy period** began or before the **incident**, whichever helps you.

- **Where.** Section II. Rewrite III.1.6's last sentence and the Item 7 "Verified backups" row to use the term.
- **Conflicts.**
  - **T3-1** adds application questions on backup credential segregation and MFA. Align the questions with items 3–4.
  - **T2-6** ("measure the 12-month test… whichever favors the insured"). Item 5 implements that choice. Don't duplicate it.
  - Cedar Ridge's application (daily cloud backups plus an immutable copy, a weekly offline copy, and a restore test on June 12, 2026) likely qualifies. It doesn't state retention days or admin separation, so add those questions.
  - **Side evidence.** Hiscox's reported €10,000 four-eyes threshold supports aligning Harborline's $5,000 callback threshold to Cedar Ridge's $10,000 (review item 4). That is already under consideration, so it isn't a new proposal.

#### E5. Disclosure limited to the questions asked, with a separate warning

- **Source.** German VVG §19:
  - pre-contract disclosure covers only circumstances the insurer asked about **in text form** (§19(1));
  - rights for misstatement depend on a **separate written warning** of consequences (§19(5));
  - if the insurer would have accepted on other terms, those terms apply (§19(4)).
- **What it does.** The insured has no duty to volunteer information, and the insurer carries the risk of not asking.
- **Why it helps SMBs.** Owners fill in forms with an IT vendor and don't know what's "material". Kiel (2024) shows that disputes move to the questionnaire.
- **Evidence.** Background. The statute wasn't opened this session.
- **Verdict: ADOPT.** The contract-adaptation half is already in V.3.2, via the UK Insurance Act model.
- **Status.** No. V.3 covers remedies, not the scope of the duty.

**Draft. New V.3.5 and V.3.6:**

> 5. **You only need to answer what we ask.** Your duty to tell us about your business is limited to the questions in our written **application** and any follow-up questions we ask in writing before the **policy period** begins. We will not deny, reduce or rescind coverage because you did not tell us something we did not ask about. If an answer you gave changes before the **policy period** begins, please tell us.
> 6. **We warn you clearly.** Our **application** shows, on its own page and in plain words, what happens if an answer is wrong. We may rely on part 3 (rescission) only if that page was part of the **application** you signed.

- **Where.** Section V, part 3. Add the warning page to the application next to the Colorado fraud warning.
- **Conflicts.**
  - **T2-13** (limit the honest-mistake remedy to premium, retention and credits, and handle the would-have-declined case) is complementary. E5 sets the *scope* of the duty; T2-13 sets the *remedy*.
  - **T2-7** (remove scan results from the "application" definition): consistent, because scan results aren't "questions we asked".
  - **T1-5** (the Colorado fraud warning's third sentence) still required.
  - Exclusion 2 (known problems) is not a disclosure rule. Keep it separate (T2-1d).

#### E6. Warning and cure before any post-loss duty affects a claim

- **Source.** VVG §28(4): a breach of a post-loss information duty has consequences only if the insurer warned the policyholder of them in a separate written notice.
- **What it does.** The insurer can't spring a cooperation defense.
- **Why it helps SMBs.** A small firm mid-crisis may miss a document request. A written warning with time to cure avoids forfeiture by oversight.
- **Evidence.** Background.
- **Verdict: ADOPT.**
- **Status.** No. V.2.1 imposes cooperation but states no consequence and no cure process.

**Draft. New V.2.4:**

> 4. **We warn you before a cooperation problem affects your claim.** If we believe you have not done something this Section asks of you after an **incident** or **claim**, such as giving us information, documents or access, we will tell you in writing:
> - what is missing;
> - what could happen to your claim if it stays missing; and
> - that you have at least 15 business days to provide it.
>
> We will reduce what we pay only if you still do not do it without good reason, and only to the extent the failure actually harmed our ability to respond, investigate or defend. This part does not change the deadline for reporting **claims** in part 1.

- **Where.** Section V, part 2.
- **Conflicts.**
  - **T1-6** (*Craft*): the claims-made reporting deadline must stay firm. The last sentence protects that.
  - **T2-12** (voluntary payments and consent) is related. Decide whether an unconsented cost goes through this cure route. My view: yes for costs, no for settlements.
  - It is more generous than Colorado requires (*Stresscon* enforces no-voluntary-payment clauses without prejudice). A deviation in the insured's favor is permissible.

### Theme B: Assistance, services and tooling

#### E7. France's 72-hour criminal complaint rule, recast as a reporting service

- **Source.** LOPMI, Law No. 2023-22 of Jan 24, 2023, Art. 5, which created **Code des assurances Art. L12-10-1**, in force **Apr 24, 2023**.
- **What it does.**
  - Any insurance payment for losses from an attack on an automated data-processing system (Penal Code Arts. 323-1 to 323-3-1) is **conditional on the victim filing a criminal complaint within 72 hours** of becoming aware of the attack.
  - It applies to legal persons, and to natural persons acting professionally.
  - It is **public order**: the parties can't contract out.
- **Why it helps SMBs (in France).** It feeds law enforcement intelligence and, in principle, deters ransom payment. As a *forfeiture* it is harsh on an SMB in crisis.
- **Evidence (snippet).**
  - Légifrance (blocked): https://www.legifrance.gouv.fr/codes/id/LEGISCTA000047048148
  - Fidal: https://www.fidal.com/en/node/16218
  - WTW, May 2023: https://www.wtwco.com/fr-fr/insights/2023/05/risques-cyber-decryptage-de-la-loi-lopmi
  - Verspieren: https://www.verspieren.com/fr/entreprise/article/iard/consequences-loi-lopmi-assurance-risques-cyber
- **Verdict: ADAPT** as a service. **Do not** copy the forfeiture (see section 4).
- **Status.** Partly. III.3.5 requires reporting a ransom *payment* to the FBI or CISA within 24 hours, with a prejudice test. III.6.3 encourages IC3 reports on fraud.

**Draft. New III.2.6, with a small III.3.5 edit:**

> 6. **We help you report the crime.** As part of Coverage A, our incident response team will help you prepare and, with your permission, submit a report of the **incident** to the FBI (through its Internet Crime Complaint Center or a local field office). Where it helps, it will also report to other law enforcement, ideally within 72 hours after you discover the **incident**. Your breach coach decides what the report says, to protect legal privilege. Making this report is not a condition of coverage, except as stated in part 3 for extortion payments.

- **Where.** Section III, part 2, plus a cross-reference on the back page.
- **Conflicts.**
  - **T2-19** already plans the one real condition: report the attack before any consented payment, which is what earns OFAC mitigation. Keep that and cite it. Don't add a general 72-hour forfeiture.
  - Privilege: forensic detail shared with law enforcement can waive work-product protection. The breach-coach sentence handles this.
  - Coverage A's $25,000 and 72-hour cap must absorb the effort. It's small.

#### E8. Security tooling bundled into the policy

- **Source.**
  - **Stoïk** (French MGA): its "Stoïk Protect" platform is "fully included in the insurance contract at no extra cost". It covers external attack-surface scanning (EASM), Active Directory scans, cloud scans (Microsoft 365, AWS, Azure, GCP) and phishing simulations. Every policy also includes technical vulnerability scans, a "Starter" human-security module and access to in-house 24/7 incident response.
  - **MMA and Stoïk** partnered for SME cyber (Apr 22, 2026, title only).
  - **Dattak** (French, launched 2021; €11M Series A with XAnge, Breega and Bpifrance, €18M raised in total; about 1,000 clients; broker-distributed) sells "dynamic insurance coupled with cybersecurity tools, for the same price as traditional insurance". Its funding date wasn't shown in the snippets.
- **What it does.** Turns the policy into a year-round risk-reduction service.
- **Why it helps SMBs.** SMBs lack security staff. Continuous findings with fix-it steps are what they actually use, and they cut losses for insured and insurer.
- **Evidence (snippet).**
  - https://www.stoik.com/assurance
  - https://www.planet-fintech.com/Stoik-devoile-Stoik-Protect_a4717.html
  - https://www.echangesassurances.org/actualites/stoik-cyber-assurance-avis-garanties-tarifs-2026
  - https://www.lassuranceenmouvement.com/2026/04/22/mma-et-stoik-sunissent-pour-la-cyber-des-pme/
  - https://presse.bpifrance.fr/dattak-leve-11meur-en-serie-a-et-affirme-ses-grandes-ambitions-pour-offrir-la-meilleure-protection-de-cyber-assurance-et-cyber-securite
  - https://www.dattak.io/fr/blog/francais-dattak-levee-fonds
- **Verdict: ADAPT.**
- **Status.** Partly: a pre-issue scan (V.3.4) and written KEV notices (III.1.7). It has no continuous service, cloud-configuration check or training.

**Draft. New Section V, part 12 "Protection services included with your policy" (E9's training is item 3):**

> **12. Protection services included with your policy.**
> 1. During the **policy period** we provide, at no extra charge:
>    - monthly scans of your internet-facing systems and email domains;
>    - a check of your Microsoft 365 or Google Workspace security settings if you connect it to our service; and
>    - alerts when we find a **critical issue**, with plain-English steps to fix it.
> 2. **These services never reduce your coverage.** Using them or not, and anything they find or miss, does not affect your coverage. The one exception: an alert about a vulnerability on the U.S. government's Known Exploited Vulnerabilities catalog is the written notice described in Section III, part 1.7.
> 3. **Training.** We also give your **employees** and **executives** access to online security-awareness training and simulated phishing exercises for the **policy period**. Taking part is voluntary.
> 4. These services help you reduce risk. They are not a guarantee that you will not suffer an **incident**, and they do not replace your own IT provider.
>
> *New definition:* **Critical issue** means a vulnerability on the Known Exploited Vulnerabilities catalog, or remote access without multi-factor authentication, on an internet-facing system we identify.

- **Where.** Section V (new part 12). Add a line on the cover page and in "Policy at a glance" (E12).
- **Conflicts and US points.**
  - **T2-7 becomes mandatory.** With continuous scanning, V.3.4's "or should have shown" would make Harborline estopped on everything a monthly scan could have caught. Delete it as T2-7 plans.
  - **"Critical issue" is undefined today** (review 4.1). This definition also feeds the claim-free reduction (V.6.1).
  - **Rebating and inducements.** Free services of value can be illegal inducements unless they are part of the filed contract and priced. Put them *in the form*, as drafted. Confirm whether Colorado has adopted the NAIC's 2020 amendments to Model 880 permitting loss-mitigation value-added services [background; verify under C.R.S. 10-3-1104].
  - **Vendor liability.** Keep "not a guarantee", and contract the scanning to a vendor with its own E&O cover.
  - **Cost.** Price per insured. External scans are cheap; M365 posture checks and phishing platforms cost more.

#### E9. Free awareness training (Swiss carriers)

- **Source.**
  - **Mobiliar**: business cyber customers get "12 months of cyber-awareness training free". Its SME product is described as including a "CyberRisk-Check".
  - **Zurich Switzerland**: free access to SoSafe online training.
  - **AXA Switzerland**: "a free basic package of prevention services".
  - Catalog: AXA CH wording, edition 06.2024; Zurich CH wording, 01.2024.
- **What it does.** Adds training to the policy.
- **Why it helps SMBs.** Phishing and business email compromise are the dominant SMB loss path, and AI-written phishing performs like human-written phishing (report 01). Training is cheap and directly on-risk.
- **Evidence (snippet; Mobiliar and CyberRisk-Check details come partly from a comparison site, so treat them as weak).**
  - https://www.mobiliar.ch/unternehmen/haftung-und-recht/cyberversicherung
  - https://www.zurich.ch/de/firmenkunden/sach-cyber/cyberversicherung
  - https://www.axa.ch/de/unternehmenskunden/angebote/inventar-immobilien/cyberversicherung.html
  - https://www.cyberversicherung.ch/cyberversicherung-vergleich/
- **Verdict: ADAPT.** The draft is E8, item 3. Keep participation voluntary and not a credit condition, so the Coverage H callback rule stays the only fraud control that changes terms.
- **Status.** No.
- **Conflicts.** If later made a credit, it collides with the credit stacking rules (T2-16).

#### E10. "Dynamic" cover: earn credits mid-term

- **Source.** Dattak ("dynamic insurance", snippet). Stoïk (the platform tracks exposure "throughout the insurance contract", snippet).
- **What it does.** Terms respond to posture changes during the year, both ways.
- **Why it helps SMBs.** An owner who adds MDR in month 3 benefits now rather than at renewal. It also rewards acting on Harborline's own scan findings.
- **Evidence.** As in E8 (snippet).
- **Verdict: ADOPT.**
- **Status.** No. III.1.5 and V.4.3 let credits be *lost* mid-term, but not *earned*.

**Draft. Replace III.1.5's first sentence and add a sentence:**

> 5. **Security credits.** The credits in Item 7 apply to every **incident** first discovered while the verified control is substantially in place. **Earning a credit during the policy period:** if you put a control listed in Item 7 in place during the **policy period**, send us the evidence Item 7 asks for (or an attestation under part 1.10). Once we verify it (we aim to within 10 business days), the retention, waiting-period and coinsurance credits apply to **incidents** first discovered after the date you sent complete evidence. They do not apply to an **incident** arising from facts an **executive** knew about before that date. Premium credits apply from your next renewal. *[Or pro rata mid-term, if our filed rating rules allow.]* (The rest of part 5 is unchanged.)

- **Where.** III.1.5. Add a mirror line in V.4.3.
- **Conflicts.**
  - **T2-16** (one stacking rule; define qualifying MDR). A mid-term MDR credit must follow the same "replaces, doesn't stack" rule.
  - Filing: a mid-term retention change needs a filed rule. A mid-term *premium* change needs a filed rating rule; hence the renewal default.
  - Adverse selection (installing MDR after a known compromise) is handled by "first discovered after" plus the knowledge carve-out.

#### E11. Standardized SME security check, accepted as evidence

- **Source.**
  - **DIN SPEC 27076 "CyberRisikoCheck"** (Germany), developed by the BSI with the SME association BVMW for firms with up to about 50 employees. A qualified IT provider walks the firm through **27 requirements in 6 areas** in 1–2 hours and delivers a prioritized report. Federal and state subsidies are available. Providers say many cyber insurers accept the report as evidence, but that claim comes from provider marketing and is weak.
  - **MonAideCyber** (France, ANSSI): a free, roughly 1.5-hour diagnostic on a structured questionnaire covering 6 themes, delivered by volunteer "cyber helpers". More than 3,300 organizations had used it in its first months. It is paired with the paid "ExpertCyber" label for vetted providers.
  - **Spain**: INCIBE's 017 helpline (142,767 queries in 2025) and Kit Digital vouchers of up to €12,000 for cybersecurity services for firms with 10–49 employees.
- **What it does.** A cheap, standard, third-party-run check that insurers can rely on.
- **Why it helps SMBs.** Evidence for credits comes from the firm's own IT provider in one sitting, not a scramble for screenshots.
- **Evidence (snippet).**
  - https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/KMU/CyberRisikoCheck/CyberRisikoCheck_node.html
  - https://systag.com/blog/din-spec-27076/
  - https://www.cpme.fr/actualites/economie/dirigeants-de-tpe-pme-prenez-votre-cyberdepart-avec-un-diagnostic-gratuit-propose-par-letat
  - https://www.cybermalveillance.gouv.fr/tous-nos-contenus/label-expertcyber/decouvrir-le-label-expertcyber
  - https://www.incibe.es/incibe/linea-de-ayuda-en-ciberseguridad/kit-difusion
  - https://cibersafety.com/kit-digital-ciberseguridad/
- **Verdict: ADAPT.** A US version: a one-page Harborline attestation mapped to **CIS Controls v8.1 IG1** (already cited in the policy) and CISA's Cross-Sector Cybersecurity Performance Goals [background]. Cedar Ridge's managed IT provider, Front Range IT Partners, signs it.
- **Status.** No. Evidence rules are planned in T3-7.

**Draft. New III.1.10, with a note in Item 7:**

> 10. **Proving a control the easy way.** Instead of sending screenshots or exports, you may have your IT provider complete and sign our one-page Control Attestation for the controls in Item 7. We accept a signed attestation as evidence for a credit, at the start of the **policy period** or during it (Section III, part 1, item 5). The attestation becomes part of your **application**. If it turns out to be wrong through an honest mistake, Section V, part 3 applies, and the most that can change is the credit.

- **Where.** III.1 and the Item 7 footnote. Add the attestation form to the application package.
- **Conflicts.**
  - **T3-7** (evidence for each starred credit) is operationalized, not duplicated: the attestation is the standard evidence format.
  - **T2-13**: "the most that can change is the credit" presumes T2-13's remedy limit.
  - **T2-7**: attestations sit in "application", scan results don't.
  - Optional: offer to reimburse the IT provider's fee (amount to be priced; don't invent one).

### Theme C: Transparency and plain language

#### E12. "Policy at a glance" in the EU IPID format

- **Source.** The EU Insurance Product Information Document, required for non-life products under the Insurance Distribution Directive and a 2017 Commission implementing regulation [background]. It is a short standardized summary with fixed questions:
  - What is insured?
  - What is not insured?
  - Are there any restrictions on cover?
  - Where am I covered?
  - What are my obligations?
  - When and how do I pay?
  - When does the cover start and end?
  - How do I cancel the contract?

  Examples in the catalog:
  - Beazley BBR EU IPID (Feb 2026): https://www.cyberservices.beazley.com/globalassets/2026-02/beazley-bbr-ipid-aoc-version.pdf
  - Allianz Austria IPID (2025): https://www.allianz.at/content/dam/onemarketing/cee/azat/privat_pdf/assistance/IPID-2025-Assistance-Cyber.pdf

  Related French rules: exclusions must be "formal and limited", and exclusion clauses must appear in "very apparent characters" (Code des assurances L113-1, L112-4) [background]. EIOPA's SME survey (launched Sept 20, 2023) names "complexity of the products" and "lack of clarity on the benefits and exclusions" as barriers [snippet]. French SME take-up fell to 27.6% in 2026 from 33.6% in 2025 (Hiscox barometer, snippet).
- **Why it helps SMBs.** The single biggest barrier Europe identifies is not understanding what's excluded or restricted. The "restrictions" and "obligations" questions force the insurer to say it on page 2.
- **Evidence.** Catalog; background; snippet: https://www.eiopa.europa.eu/eiopa-launches-survey-access-cyber-insurance-smes-2023-09-20_en and https://www.channelnews.fr/la-souscription-dune-assurance-cyber-par-les-tpe-pme-francaises-est-en-recul-158896
- **Verdict: ADAPT.** Voluntary in the US.
- **Status.** Partly. The cover page has a "What's inside" navigation table, not a summary of restrictions.

**Draft. New page after the cover page:**

> **Your policy at a glance** *(a summary; the policy wording controls)*
>
> | Question | Short answer | Where |
> | --- | --- | --- |
> | What is covered? | Your own costs and lost income after a cyberattack, system failure or online fraud, and claims and regulatory actions against you | Section I |
> | What is not covered? | Among others: war and major state cyber operations; physical injury and damage; problems your executives knew about before the continuity date; intentional wrongdoing by executives; power, telecom and internet infrastructure failures | Section IV |
> | Are there limits on what we pay? | $1,000,000 in total. Lower limits for fraud ($250,000; $100,000 if an unverified payment instruction is acted on), system failure ($250,000), vendor attacks ($500,000) and others. An 8-hour waiting period for lost income. **Only three things about your security can reduce a payment**, and never on the first $50,000 | Items 4–7; III.1.9 |
> | Where are you covered? | Worldwide, where legally permitted | V.11.1 |
> | What must you do? | Answer our application questions accurately. Call us as soon as you suspect a problem. Tell us within 30 days if you remove a verified control. Cooperate with us. Report claims by the deadline | V.1–V.4 |
> | When do you pay? | [Payment terms] | Item 3 |
> | When does cover start and end? | [Dates]. Claims against you must be first made, and reported, during the policy period or an extended reporting period | Items 2, 8, 9 |
> | How do you cancel? | Any time, with a pro rata refund | V.5.1 |

- **Where.** Immediately after the cover page. Merge it with or replace "What's inside".
- **Conflicts.**
  - **T2-17** (IV.1 lists all security-related penalties). The "three things" line must match III.1.9 exactly.
  - **T2-1e** (whether sublimits apply per incident or per period). The summary must say which once decided.
  - Colorado's unfair-practices statute bars misrepresenting policy terms (C.R.S. 10-3-1104). Every figure must match the wording, and the page must be regenerated from the Declarations.
  - The "$50,000" figure assumes E3 is adopted.

#### E13. Side-by-side "what changed" synopsis at renewal

- **Source.** Hiscox Germany publishes a synopsis ("Gegenüberstellung der wesentlichen Neuerungen", roughly "comparison of key changes") between wording editions, dated 10/2023.
- **What it does.** Shows the insured what changed at renewal.
- **Why it helps SMBs.** Silent narrowing at renewal is a top SMB complaint. A change table lets the owner, or their broker, see it in five minutes.
- **Evidence.** Title only (blocked on fetch): https://brochureware.hiscox.de/sites/default/files/documents/cyberversicherung-by-hiscox-synopse-102023.pdf
- **Verdict: ADOPT.**
- **Status.** No. V.11.7 liberalization covers broadenings only.

**Draft. New V.6.3:**

> 3. **What changed at renewal.** With every renewal offer we send a side-by-side table of every change to your policy wording, limits, **retentions**, credits and premium, marking each change as broader, narrower or neutral for you. If a change narrows your coverage, we tell you at least 60 days before renewal, or longer if state law requires. If we leave a narrowing change out of the table, the earlier, broader wording applies to you until your next renewal.

- **Where.** Section V, part 6.
- **Conflicts.**
  - V.5.3 (60-day non-renewal notice) should use the same period.
  - Confirm Colorado's renewal-change notice rules [background; verify C.R.S. 10-4-110 and related provisions].
  - The last sentence is a strong estoppel. Filing reviewers will accept it because it favors the insured; the actuary should note it.

#### E14. Industry model wording as a benchmark; FAQ-style explanations

- **Source.**
  - GDV *AVB Cyber*: an industry-standard, non-binding SME model since 2017 (see E1).
  - Gothaer's broker FAQ on the war exclusion and switching service providers ("FAQ Kriegsausschluss und Dienstleisterwechsel", title only): https://partner.gothaer.de/media/bilder_partnerportal/produkte_1/sach/gewerbekunden/cyber_versicherung/faq_kriegsauschluss_cyber.pdf
  - The US analogue is coming: the LMA plans a US SME model wording (report 09).
- **Verdict: OPTIONAL.** Add a short "Harborline vs the market standard" table to the rationale, not the policy. When the LMA US SME model appears, map Harborline against it. An FAQ on the war exclusion could go in the rationale or on the back page. No clause.

### Theme D: Rating and product architecture

#### E15. Risk classes that set the expected controls (Netherlands)

- **Source.**
  - **"Risicoklasse-indeling Digitale Veiligheid"** (Digital Security Risk Classification), developed under the Centre for Crime Prevention and Safety (CCV). Partners are the employers' groups VNO-NCW and MKB-Nederland, the Dutch Association of Insurers (Verbond van Verzekeraars), the National Police, Cyberveilig Nederland, NLdigital, the CIO Platform, the Digital Trust Center and the Ministry of Economic Affairs. Firms are sorted into risk classes, each with a matching set of measures.
  - **"Keurmerk Digitale Basisveiligheid MKB"** (SME digital baseline security mark), a CCV certification scheme, version 1.0; the PDF path is dated 2025/12.
  - Dutch insurers are tightening minimum security terms and differentiating premiums for demonstrated measures.
  - Separately, Swiss carriers reportedly now require MFA, EDR and tested backups as prerequisites (comparison-site snippet, weak).
- **What it does.** Controls are expected in proportion to risk, not as one list for all.
- **Why it helps SMBs.** A 5-person landscaper and a CPA firm holding thousands of SSNs shouldn't face the same checklist.
- **Evidence (snippet).**
  - https://www.verzekeraars.nl/publicaties/actueel/nieuwe-risicoklasseindeling-vergroot-cyberweerbaarheid-mkb
  - https://www.verzekeraars.nl/publicaties/actueel/keurmerk-digitale-basisveiligheid-mkb-gelanceerd
  - https://hetccv.nl/app/uploads/2025/12/DBV-MKB-versie-1.0.pdf
  - https://www.cyberversicherung.ch/cyberversicherung-vergleich/

  Launch dates of the classification and the mark weren't shown.
- **Verdict: ADAPT.** This is the structural answer to review item 11: the market treats MFA and EDR as bind prerequisites, not credits.
- **Status.** No.

**Draft. New preamble to Item 7 (illustrative; the thresholds are Harborline judgment):**

> **Item 7. Your risk class and security controls.** We place you in a risk class based on the sensitive data you hold and whether you move money for others. Controls marked "assumed" are built into your price. Controls marked "credit" improve your terms.
>
> | Risk class | Typical business | Assumed | Credit |
> | --- | --- | --- | --- |
> | 1. Standard | Little sensitive data beyond employee records; no client funds | MFA on email; backups; supported software | EDR; verified backups; callback |
> | 2. Elevated (**your class**) | Holds clients' Social Security, tax or financial account data, or moves client money | MFA on email, remote access and admin accounts; EDR on all devices | Verified backups; hardened remote access; callback; 24/7 MDR |
> | 3. High | Very large record counts or payment processing | Class 2 controls plus verified backups | 24/7 MDR; hardened remote access; callback |
>
> If a control assumed for your class is missing, we tell you before your policy starts and quote the terms that apply.

- **Where.** Item 7 header. The retention band table (review 4.3) stays by revenue; the risk class sits alongside it.
- **Conflicts.**
  - This **replaces** the current "25% retention credit for MFA+EDR" framing for class 2. It is a pricing decision, and it closes review item 11 in favor of "eligibility".
  - **T2-16** (stacking) and the retention bands (review 4.3) must be re-cut.
  - Premium impact must be re-derived.
  - If the candidate prefers to keep "deliberate transparency" credits, downgrade this item to OPTIONAL.

#### E16. Micro-SME "Kompakt" tiers and industry tariffs

- **Source (catalog).**
  - ERGO Cyber-Versicherung **Kompakt** ("cheaper variant covering selected own-damage and service costs")
  - rhion Cyber-Versicherung **Kompakt** (CVK 2019, form S2116, edition 2020-10)
  - AXA Germany **ByteProtect 5.1 Kompakt** for turnover up to €10M
  - Hiscox **CyberClear Start**
  - Gothaer **GewerbeProtect** cyber module (up to €10M turnover; form 216308, 2023-07)
  - ERGO **Branchentarif** (industry-class tariff) application 50075881 (2021-03)
- **Why it helps SMBs.** Short forms and industry-class rating reach micro-businesses that won't fill in a 9-part application.
- **Verdict: OPTIONAL.** Harborline starts at $1M revenue. An "Essentials" edition for under $2.5M or $5M revenue, with a short application, core B/C/D/F/H/I only and pre-set credits, is a plausible roadmap item for the rationale's "what I'd do next". No clause.

### Theme E: Coverage terms Harborline already has

#### E17. GDV 2024 war and state-attack update

- **Source.** GDV *AVB Cyber*, Feb 2024. As reported:
  - a war needn't involve physical weapons, so digital warfare is excluded;
  - there is a new exclusion for losses that are a "direct or indirect consequence" of a successful state attack on critical infrastructure.
- **Evidence (snippet).**
  - https://versicherungsmonitor.de/2024/02/19/gdv-legt-neue-cyber-musterbedingungen-vor/
  - https://www.versicherungsbote.de/id/4913641/Cyberversicherung-GDV-aktualisiert-Musterbedingungen/
  - Gothaer FAQ (title only), as in E14
- **Verdict: SKIP.** Harborline's LMA-style exclusion 15 is already more SMB-friendly: bystander carve-back, cyber terrorism and state-linked crime covered, burden on the insurer, and help continuing while attribution is pending. Don't import "indirect consequence" language; it's broader. The one GDV point, that cyber war needn't be physical, is already planned in **T2-9** ("add a cyber operation carried out as part of a war").

#### E18. Cloud-provider events and BI mechanics

- **Source.**
  - **GDV 2024** lifted most of the old exclusion for external service providers. Data at a cloud, data-center or SaaS provider that is manipulated, infected or accessed without authorization is covered. The provider's mere outage (unavailability) stays excluded [snippet].
  - **Markel Pro Cyber v2** sublimits technical-failure BI to €250K [catalog]: https://content.markel.com/api/public/content/MARKEL-Cyber-Pro-Cyber-Bedingungen-GER
  - **SV SparkassenVersicherung** has a separate cyber BI module (Sept 2024) [catalog].
- **Verdict: SKIP.** Harborline already goes further: Coverage E covers attacks at a dependent provider, P optionally covers provider system failure, and the core has a $250K system-failure sublimit. The GDV split between data events and availability events *validates* **T2-0** (cloud accounts as your systems; provider bugs routed to P) and **T2-3**. Markel's €250K independently supports Harborline's $250K sublimit; cite it in the rationale's "why this number".

### Theme F: Regulatory-inspired

#### E19. A "legal clock card" (inspired by NIS2's staged reporting)

- **Source.** NIS2 Directive (EU) 2022/2555, Art. 23: an early warning within 24 hours, an incident notification within 72 hours, and a final report within one month [background]. France's LOPMI adds a 72-hour complaint clock (E7).
- **What it does.** Makes the deadlines visible in one place.
- **Why it helps SMBs.** Owners don't know which clocks started when they found the breach. Listing them on the back page is cheap and prevents missed legal deadlines.
- **Verdict: ADAPT**, with **US** clocks only. Never NIS2 terms.
- **Status.** Partly: the back page item 5, Coverage A's "guidance on legal notice deadlines", and V.1.5.

**Draft. Back page addition. Every row is to be verified by counsel; the citations are background knowledge.**

> **Legal clocks that may apply to you.** Our breach coach will confirm which apply from your first call.
>
> | If… | Who you may need to tell | Deadline |
> | --- | --- | --- |
> | Personal information of Colorado residents was breached | Affected residents; the Colorado Attorney General if 500 or more residents | No later than 30 days after you determine a breach occurred (C.R.S. 6-1-716) |
> | Unencrypted information of 500 or more customers was taken (FTC Safeguards Rule; covers tax preparers and accounting firms) | Federal Trade Commission | As soon as possible, and no later than 30 days after discovery |
> | Client tax data was stolen | IRS (Stakeholder Liaison) and state tax agencies | As soon as possible |
> | You paid a ransom | FBI or CISA | Within 24 hours of paying (this policy, Section III, part 3) |
> | Residents of other states were affected | Varies by state | Your breach coach will tell you |
>
> **You never need our permission to meet a legal deadline.**

- **Where.** Back page, after item 5.
- **Conflicts.**
  - **T1-10** (recheck CIRCIA on the day of sending). Add a CIRCIA row only if the final rule is in force and reaches the insured.
  - Every row must be checked at source before use, especially the Colorado 30-day period, the FTC rule's effective date (2024) and the IRS channel.
  - Keep the card consistent with Item 10 and V.1.5.

#### E20. Regulatory-fine insurability

- **Source.**
  - Aon/DLA Piper, "The price of data security" (May 2018): GDPR fines were insurable in only Norway and Finland among 30 European countries. https://www.aon.com/attachments/risk-services/Aon_DLA-Piper-GDPR-Fines-Guide_Final_May2018.pdf
  - K&L Gates overview (Feb 23, 2026): insurability is contested, generally a public-policy question, and unsettled in Germany (BGB §138). https://www.klgates.com/Insurability-of-Financial-Penalties-for-Personal-Data-Breaches-Overview-of-Leading-European-Jurisdictions-2-23-2026
- **Evidence.** Snippet.
- **Verdict: SKIP.** It's EU-specific, and Harborline already pays regulatory penalties "where insurable" (J). Its planned fix is **T1-8** (one punitive/penalty rule, plus a Colorado note).

---

## 4. EU-, German- and French-specific features not to copy into a US admitted form

| Feature | Why it doesn't transfer | US analogue for Harborline |
| --- | --- | --- |
| **Fault-degree quota** (VVG §28(2) and §81(2): reduce "in proportion to the severity of fault") | Rests on a statute and 15+ years of German case law. In Colorado it becomes a discretionary, bad-faith-exposed reduction (C.R.S. 10-3-1115/1116) that can't be priced | Fixed, filed coinsurance triggered by objective facts, gated by causation (E1). The KEV "notice + 45 days" rule is the objective proxy for gross negligence |
| **Statutory pre-contract disclosure regime** (VVG §19: rescission, termination and adaptation tiers keyed to fault; "Textform") | Statutory mechanics and terms of art | Contractual version (E5) plus V.3. Colorado misrepresentation law and the required fraud warning (T1-5) still govern |
| **Risk-increase scheme** (VVG §§23–27, "Gefahrerhöhung") | Statutory | V.4.3 30-day notice of a removed control, plus mid-term earning (E10) |
| **Post-loss cancellation right** (common in German forms; VVG §92/§111 for property and liability) | Would breach Harborline's cancellation promise and Colorado's cancellation limits (C.R.S. 10-4-109.7: 45 days; 10 for non-payment; package source) | Keep V.5.2: cancellation only for non-payment or fraud (with T1-7's 45-day fix) |
| **14-day right of withdrawal** (DE VVG §8; CH VVG Art. 2a) | Consumer-protection device; not required for US commercial lines | V.5.1: cancel any time with a pro rata refund is enough |
| **Premium-adjustment clauses** (e.g., HDI's annual review with a 5% threshold, catalog form 7003031470; VVG §40) | US admitted rates are filed; no unilateral mid-term re-rating | Rate changes at renewal only, disclosed via E13 |
| **LOPMI 72-hour complaint as a condition of payment** (Code des assurances L12-10-1; public order, French-law contracts only) | No US statutory basis. As a filed forfeiture it's harsh and invites *Craft*-style strict-deadline fights | E7 service, plus T2-19's pre-payment report. OFAC treats early reporting and cooperation as mitigating (2021 advisory, already cited) |
| **GDPR, NIS2 and DORA terms** (DPAs, "essential/important entity", NIS2's 24h/72h/1-month clocks, DORA's ICT third-party register) | Wrong regimes. NIS2 applies to medium and large entities in listed EU sectors; DORA applies to EU financial entities | FTC Safeguards Rule (tax preparers and CPA firms), GLBA, state breach laws, IRS Publication 4557, CIRCIA (pending). Use DORA's vendor register only as an *underwriting idea* (vendor-concentration questions, T3-1) |
| **GDPR fine insurability language** | EU public-policy question; fines insurable almost nowhere | "Where insurable under applicable law" plus Colorado's punitive-damages rule (T1-8) |
| **"Stand der Technik" (state of the art) security duties** | Vague; borrowed from German IT-security law. A US "industry standard" duty would re-create the patching-denial problem | Name the frameworks the policy already cites (CIS Controls v8.1 IG1, NIST CSF 2.0) only in the application and attestation (E11), never as a coverage condition |
| **IPID as a legal document** (IDD; "demands and needs" statement) | EU regulatory format | Voluntary "Policy at a glance" (E12), subject to Colorado's rules against misrepresenting policy terms |
| **War clause referencing a state attack on "critical infrastructure", with "direct or indirect" causation** (GDV 2024) | Broader than the LMA-style clause Harborline uses, and would undercut its bystander promise | Keep exclusion 15, with T2-9 fixes ("state" means a sovereign country) |
| **Public schemes** (BSI CyberRisikoCheck subsidies; MonAideCyber; INCIBE 017 and Kit Digital; Dutch Digital Trust Center) | National programs | CISA's free services and Cross-Sector Performance Goals, SBA/SBDC resources, FTC small-business guidance, IRS resources for tax professionals [background; check CISA service eligibility for private firms]. Mention them in the attestation guide (E11) |
| **Assistance written as a separate insurance class** (Solvency II class 18; hotlines often run by assistance carriers) | EU licensing structure | Coverage A delivered by panel vendors inside the filed form (as now); watch rebating rules for any service outside the form (E8) |

---

## 5. How the drafts interact with each other and with planned fixes

1. **One home for conduct-based terms.** E1 (III.1.9), E2 (IV.1), E3 (safe harbor) and E12 (the "three things" line) must use identical wording. Implement them with **T2-6** (ransomware scope and non-stacking) and **T2-17** (IV.1 list) as one edit.
2. **The scan estoppel must shrink before tooling grows.** E8 (continuous scanning) makes **T2-7** (delete "or should have shown") a prerequisite, not a nice-to-have.
3. **Evidence pipeline.** E11 (attestation) feeds E10 (mid-term credits) and implements **T3-7**. E4's backup definition gives the attestation its checklist.
4. **Application law.** E5 (disclosure scope) and **T2-13** (remedy) should be drafted together, with **T3-2** (removing traps). Kiel (2024) shows why.
5. **Claims process.** E6 (cure notice) must carve out the claims-made reporting deadline (**T1-6**) and be reconciled with **T2-12** (voluntary payments).
6. **E15 is a fork.** Adopting risk classes resolves review item 11 toward "eligibility" and changes the Item 7 economics. It shouldn't be adopted halfway.

---

## 6. What to verify before quoting

- **Opened at source (all blocked here):**
  - GDV *AVB Cyber* 2024 text: the security duties clause and war/state-attack clause numbers
  - VVG §§19, 28, 81
  - Code des assurances L12-10-1
  - Hiscox Germany: current wording, the €50K gross-negligence waiver (first €50K, or losses up to €50K?), the backup duty text, and the 10/2023 synopsis
  - Markel Pro Cyber v2 €250K technical-failure sublimit
- **LG Hagen 9 O 258/23**: holding not seen. LG Tübingen and LG Kiel: check citations and facts in a legal database.
- **Stoïk**: the included-tools list and "no extra cost", the MMA partnership terms (Apr 2026), and the markets Stoïk operates in. **Dattak**: funding date and product scope.
- **Mobiliar, Zurich and AXA Switzerland** training and prevention inclusions. Some details come from a comparison site.
- **Dutch risk classification and keurmerk**: launch dates and class definitions.
- **US points (background knowledge):**
  - Colorado adoption of the NAIC Model 880 value-added-services amendment
  - Colorado commercial form-filing regime
  - C.R.S. 6-1-716 (30 days; 500-resident AG threshold)
  - FTC Safeguards Rule notification (500+ customers; 30 days)
  - IRS reporting channel for tax preparers
  - CISA service eligibility
- **Gaps not searched:** Nordic carriers (If, Tryg, Gjensidige), Italy (Generali, UnipolSai), Belgium, Austria beyond the catalog, AXA France's SME cyber offer, and EIOPA's published SME survey results (only the 2023 launch notice was found). The IAIS/FSI "Cyber insurance unpacked" paper (June 2026) was seen as a title only: https://www.iais.org/uploads/2026/06/FSI-IAIS-Insights-Cyber-insurance-unpacked-the-corporate-digital-safety-net.pdf

---

## 7. Sources (all snippet-level unless marked)

**Germany**
- GDV press release, new model conditions (Feb 2024): https://www.gdv.de/gdv/medien/medieninformationen/versicherungsschutz-gegen-cyberangriffe-gdv-veroeffentlicht-neue-musterbedingungen--168132
- Versicherungsmonitor (Feb 19, 2024): https://versicherungsmonitor.de/2024/02/19/gdv-legt-neue-cyber-musterbedingungen-vor/
- Versicherungsbote: https://www.versicherungsbote.de/id/4913641/Cyberversicherung-GDV-aktualisiert-Musterbedingungen/
- VGV (Mar 5, 2024): https://www.vgv-gmbh.de/blog/2024/03/05/cyber-versicherung-gdv-fasst-musterbedingungen-neu/
- GDV AVB Cyber PDF, 2024-02 (catalog; blocked): https://www.gdv.de/resource/blob/6100/a0fed56c4947751cdc20b5206c171d98/01-allgemeine-versicherungsbedingungen-fuer-die-cyberrisiko-versicherung-avb-cyber--data.pdf
- GDV model risk questionnaire (catalog): https://www.gdv.de/resource/blob/6102/0e5e65afe025a091c76d45ed5cb0bdbe/02-risikofragebogen-cyber-data.pdf
- Gothaer war-exclusion FAQ (title only): https://partner.gothaer.de/media/bilder_partnerportal/produkte_1/sach/gewerbekunden/cyber_versicherung/faq_kriegsauschluss_cyber.pdf
- VVG §28 (blocked): https://www.gesetze-im-internet.de/vvg_2008/__28.html
- LG Tübingen (2023):
  - https://www.vsma.de/urteil-zur-cyberversicherung-landgericht-tuebingen-bringt-licht-ins-cyber-dunkel/
  - https://www.wilhelm-rae.de/en/node/174
  - https://www.gleisslutz.com/de/know-how/cybersecurity-cyberversicherung-vor-gericht
- LG Kiel (2024):
  - https://www.dr-bahr.com/news/cyberversicherung-muss-bei-falschangaben-fuer-schaeden-aus-einem-hacker-angriff-nicht-zahlen.html
  - https://www.experten.de/id/4929502/cyberurteil-lg-kiel-wertet-falschangaben-als-arglistige-taeuschung/
- LG Hagen: https://www.ferner-alsdorf.de/lg-hagen-zur-einstandspflicht-einer-cyberversicherung/
- Noerr on waiving technical duties (title only): https://www.noerr.com/de/insights/cyberversicherung-der-verzicht-auf-technische-obliegenheiten-und-seine-folgen
- Hiscox Germany:
  - https://www.hiscox.de/geschaeftskunden/cyber-versicherung/vergleich/
  - synopsis 10/2023 (title only): https://brochureware.hiscox.de/sites/default/files/documents/cyberversicherung-by-hiscox-synopse-102023.pdf
  - CyberClear 06/2022 (catalog): https://brochureware.hiscox.de/sites/default/files/documents/bedingungen-hiscox-cyberclear-062022-1.pdf
- DIN SPEC 27076 / BSI CyberRisikoCheck: https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/KMU/CyberRisikoCheck/CyberRisikoCheck_node.html

**France**
- LOPMI / L12-10-1:
  - https://www.legifrance.gouv.fr/codes/id/LEGISCTA000047048148 (blocked)
  - https://www.fidal.com/en/node/16218
  - https://www.wtwco.com/fr-fr/insights/2023/05/risques-cyber-decryptage-de-la-loi-lopmi
  - https://www.verspieren.com/fr/entreprise/article/iard/consequences-loi-lopmi-assurance-risques-cyber
- Stoïk:
  - https://www.stoik.com/assurance
  - https://www.planet-fintech.com/Stoik-devoile-Stoik-Protect_a4717.html
  - https://www.lassuranceenmouvement.com/2026/04/22/mma-et-stoik-sunissent-pour-la-cyber-des-pme/
- Dattak:
  - https://presse.bpifrance.fr/dattak-leve-11meur-en-serie-a-et-affirme-ses-grandes-ambitions-pour-offrir-la-meilleure-protection-de-cyber-assurance-et-cyber-securite
  - https://www.dattak.io/fr/blog/francais-dattak-levee-fonds
- MonAideCyber and ExpertCyber:
  - https://www.cpme.fr/actualites/economie/dirigeants-de-tpe-pme-prenez-votre-cyberdepart-avec-un-diagnostic-gratuit-propose-par-letat
  - https://www.cybermalveillance.gouv.fr/tous-nos-contenus/label-expertcyber/decouvrir-le-label-expertcyber
- Hiscox France barometer:
  - https://www.channelnews.fr/la-souscription-dune-assurance-cyber-par-les-tpe-pme-francaises-est-en-recul-158896
  - https://www.hiscox.fr/courtage/blog/rapport-2025-sur-la-gestion-des-risques-cyber

**Switzerland**
- Revised VVG Art. 45:
  - https://www.baerkarrer.ch/de/publications/claims-made-policen,-art.-38-vvg-und-der-revidierte-art.-45-vvg
  - https://justement.ch/de/doc/act/ch/221_229_1/chap_1/sec_8/lvl_u3/art_45
- Mobiliar: https://www.mobiliar.ch/unternehmen/haftung-und-recht/cyberversicherung
- Zurich: https://www.zurich.ch/de/firmenkunden/sach-cyber/cyberversicherung
- AXA: https://www.axa.ch/de/unternehmenskunden/angebote/inventar-immobilien/cyberversicherung.html
- Comparison site: https://www.cyberversicherung.ch/cyberversicherung-vergleich/

**Netherlands**
- https://www.verzekeraars.nl/publicaties/actueel/nieuwe-risicoklasseindeling-vergroot-cyberweerbaarheid-mkb
- https://www.verzekeraars.nl/publicaties/actueel/keurmerk-digitale-basisveiligheid-mkb-gelanceerd
- https://hetccv.nl/app/uploads/2025/12/DBV-MKB-versie-1.0.pdf

**Spain**
- https://www.incibe.es/incibe/linea-de-ayuda-en-ciberseguridad/kit-difusion
- https://cibersafety.com/kit-digital-ciberseguridad/

**EU level**
- EIOPA SME survey launch (Sept 20, 2023): https://www.eiopa.europa.eu/eiopa-launches-survey-access-cyber-insurance-smes-2023-09-20_en
- Aon/DLA Piper (May 2018): https://www.aon.com/attachments/risk-services/Aon_DLA-Piper-GDPR-Fines-Guide_Final_May2018.pdf
- K&L Gates (Feb 23, 2026): https://www.klgates.com/Insurability-of-Financial-Penalties-for-Personal-Data-Breaches-Overview-of-Leading-European-Jurisdictions-2-23-2026
- Catalog IPIDs:
  - Beazley EU (02/2026): https://www.cyberservices.beazley.com/globalassets/2026-02/beazley-bbr-ipid-aoc-version.pdf
  - Allianz Austria (2025): https://www.allianz.at/content/dam/onemarketing/cee/azat/privat_pdf/assistance/IPID-2025-Assistance-Cyber.pdf

**Background knowledge (not checked this session):** NIS2 Art. 23; the IDD/IPID regulation; VVG §§19, 28(1), (3), (4), 32, 81, 210; Code des assurances L112-4, L113-1; UK Insurance Act 2015 s.11; the NAIC Model 880 2020 amendments; C.R.S. 6-1-716; the FTC Safeguards Rule notification requirement; CISA services.
