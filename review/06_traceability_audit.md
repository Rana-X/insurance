# Traceability Audit: does the package explain every choice?

Red-team review, September 27, 2026. Package audited: policy.md (cover, notices, Declarations Items 1–12, Sections I–V, back page), application.txt (Cedar Ridge sample + underwriter page), rationale.md, 04_references.txt / Sources.csv (33 sources), Claim_Ledger.json (C1–C26), 00_submission_guide.txt, Quality_Review.md, round1_findings.md.

Question asked by the candidate: *"See if we explained everything properly: why we selected anything here, like words and numbers and our assumptions."*

---

## 0. How to read this audit

**Reference keys**

- **L##**: line number in rationale.md (for example, L40 is the retention row of the Declarations table).
- **Item n / I.x / II / III.n.m / IV.n / V.n.m**: policy Declarations item, Section I coverage letter, Section II definition, Section III part.item, Section IV exclusion, Section V part.item.
- **App x.y**: application question. **UW**: the application's underwriter page ("how these answers set the policy terms").
- **#n**: source number in 04_references / Sources.csv. **Cn**: Claim_Ledger id.
- **R1**: already reported in round1_findings.md. Where an R1 item appears, only the new angle is added.
- **[PR]**: my professional reasoning. It is **not** in the package and must be checked before the candidate relies on it.
- **[SS]**: search-snippet-level evidence from the three web searches run today (sources in section 14).

**Column meanings**

- **Explained?** **Yes** means the rationale gives a reason for this specific value or word. **Partial** means it explains the feature but not the number or wording, or the reason is weak. **No** means nothing in the rationale explains it.
- **Evidence**: what backs the explanation. This is a 04 source, a ledger claim, "own design" (the rationale says so), or "unsupported" (asserted, no source or ledger entry).
- **Verdict** (primary verdict first):
  - **OK**
  - **Needs explanation** (the rationale is silent or weak)
  - **Needs citation** (a reason is given, but its source isn't in 04 or the ledger)
  - **Inconsistent** (documents disagree, or the rationale misdescribes the policy)
  - **Consider changing** (the choice itself looks weak)

---

## 1. Headline results

| Measure | Count |
| --- | --- |
| Decision-bearing elements inventoried | **207** (Numbers 100 · Terms/word choices 46 · Structural choices 46 · Assumptions 15) |
| Explained **Yes** in rationale | 76 (37%) |
| Explained **Partial** | 61 (29%) |
| Explained **No** | 52 (25%) |
| Not applicable (sample-insured facts, QR-only figures) | 18 (9%) |
| Primary verdict **OK** | 86 |
| Primary verdict **Needs explanation** | 65 |
| Primary verdict **Needs citation** | 19 |
| Primary verdict **Inconsistent** | 32 |
| Primary verdict **Consider changing** | 5 |
| By category (Yes / Partial / No) | Numbers 23 / 37 / 26 (plus 14 n/a) · Terms 15 / 12 / 17 (plus 2 n/a) · Structure 36 / 5 / 5 · Assumptions 2 / 7 / 4 (plus 2 n/a) |
| Cross-references checked (policy, application, rationale, 04) | 52, of which 5 fail or misdirect (section 8) |
| Rationale statements about the policy checked against the text | 33, of which 13 are untrue, stale or overstated (section 10) |
| Summary claims checked against support below | 17, of which 7 are unsupported or only partly supported (section 11) |

**Pattern.** The rationale is strong on **what** was borrowed and **why a feature exists**. It is weak on **why a specific number**. Of the 86 numeric elements that are design choices (the other 14 are sample-insured facts), only 23 are explained Yes; 37 are Partial and 26 have no explanation. Structural choices are the opposite: 36 of 46 are fully explained. Almost every sublimit, time window and percentage that the candidate invented (rather than copied from At-Bay or Coalition) has no stated reason. Words fare better, but three word choices are contradicted by the policy text: "executive" called "narrow", service standards called "binding", and "waiting period" used for both hours and days.

**No 48-hour window** appears anywhere in the package (checked all files), so there is nothing to reconcile there.

---

## 2. Top 30 unexplained or weakly explained choices

These are ranked by how likely a Corgi reviewer is to ask "why?". Each entry has (i) the gap, (ii) the best available justification, and (iii) a draft sentence. Drafts are deliberately plain, and each is labeled **draft — rewrite in your own words**.

### 1. Premium: $6,120 base, −$612, $5,508 total (Item 3)

**(i) Gap.** Nothing explains how $6,120 was set. C26 marks it "non-factual, design assumption". It equals exactly $5,508 ÷ 0.9, so it reads as reverse-engineered from the total.

Both premium benchmarks are unverified:
- $2,330–$4,048 has no source or ledger entry (R1).
- The Vouch $7,078 figure (#17) has no URL, and C16 is "uncertain" (R1).

**New: the rationale contradicts itself.**
- L251 says "No primary 2025–26 median-premium data found".
- L25 and L329 still lean on "Vouch's $7,078 median".
- L25 says $5,508 "sits between" the benchmarks, but L329 says pricing is "near" $7,078.

**(ii) Best justification.** The package can support the **direction** of the premium, but not its level:
- The core is broader than the market (Summary #3; L329).
- Cedar Ridge holds about 31,000 people's SSNs and tax records (App 3.1–3.2).
- Two clients require $1M of cyber cover (App 2.6).

[PR] Show a transparent placeholder method. For example, $6,120 is a 0.61% rate-on-line on a $1M limit. Alternatively, use "base rate per $1,000 revenue × industry factor × limit factor", with the factors stated as assumptions. If the Vouch link can't be restored, drop all premium benchmarks rather than keep unverified ones.

**(iii) Draft — rewrite in your own words.** "The $6,120 base premium is a placeholder, about 0.6% of the $1M limit, set to show how credits change the price. It is not a rated figure. An actuary would replace it using loss data for firms that hold this many tax records."

### 2. Retention schedule by revenue band (Item 5; L13; L40)

**(i) Gap.** Only one band appears anywhere: "Standard retention (revenue $5M–$25M) | $10,000". The Summary says retentions run "from $2,500 to $25,000", but:
- No document shows the full schedule.
- $25,000 as a retention appears nowhere else.
- The band edges ($5M, $25M) are never explained.
- The comparator retentions in L40 ("Vouch and Corgi ($10K); At-Bay and Coalition ($2,500)") are not in the ledger.

**New conflict.** Item 5 and V.6.1 set a claim-free "minimum of $2,500". If the smallest band's retention is $2,500, the 25% MFA+EDR credit takes it to $1,875, below the stated minimum. The package never says whether credits can go below $2,500.

**(ii) Best justification.**
- The $25M edge is where At-Bay's claims data splits: C2 ($180K average severity under $25M) and C8 ($208K vs $373K fraud losses).
- L40 gives the logic: "$2,500 fits very small firms, $10K mid-sized ones".
- [PR] A defensible rule of thumb is a retention of roughly 0.1% of revenue, rounded to market steps. $10,000 is about 0.12% of Cedar Ridge's $8.5M.

**(iii) Draft — rewrite in your own words.** "Retentions follow three revenue bands: $2,500 under $5M, $10,000 from $5M to $25M, and $25,000 from $25M to $50M. The $25M break matches At-Bay's claims data, and each step keeps the retention near 0.1% of revenue. Credits and claim-free reductions never take a retention below [$2,500 / half the band amount]."

### 3. Security-credit design: 25% / 50% / 10% / 4 hours (Items 3, 5, 7)

**(i) Gap.** The evidence explains direction only:
- C3: 60% of Akira ransomware victims had EDR and were still compromised.
- C4: remote access was the entry point in 87% of ransomware claims.
- C15: Coalition offers a "reduced MDR waiting period" but gives no number of hours.

Unexplained:
- Why 25% for MFA+EDR, 50% for 24/7 MDR, 10% for remote access, and 4 hours for the MDR waiting period.
- Why two controls move the retention while one moves the premium.
- Whether credits stack. Item 5 says MDR "would halve it" (from $7,500 to $3,750?) while Item 7 says "$5,000" (R1).
- Whether the 4-hour wait applies to Coverage E (vendor attacks), where the insured's own monitoring can't help. L294 says "attack waiting period only", which is ambiguous.

Remote-access MFA is also rewarded twice: it is part of the MFA+EDR credit and the premise of the 10% credit.

**(ii) Best justification.** C3 supports "EDR alone is worth less than half". C4 supports a separate reward for remote access.

[PR] One coherent logic the candidate could adopt:
- Controls the pre-issue scan can **verify from outside** (exposed RDP, end-of-life VPN) earn a **premium** credit, because they are confirmed facts that lower claim frequency.
- Self-attested controls that **limit loss size** (EDR, 24/7 MDR) move the **retention and waiting period**, which is where they reduce the insurer's cost.
- Retention credits don't stack; the best one applies.

**(iii) Draft — rewrite in your own words.** "Hardened remote access earns a premium credit because it was the way in for 87% of At-Bay's ransomware claims, and our scan can confirm it. MFA with EDR cuts the retention by a quarter, not half, because 60% of Akira victims had EDR and were still breached. Only 24/7 monitoring, which acts on the alerts, halves it. Retention credits don't stack."

### 4. Admitted paper and Colorado law (notice 4, Item 11, 00 guide)

**(i) Gap.**
- Admitted status is explained in one row (L38) with no source. NAIC #15 ("admitted vs surplus-lines context") is listed but never cited in the rationale body.
- The trade-off isn't stated. QR's steel-man says "Admitted paper is slower than surplus competitors … Holds; say so in the memo", and this was not done.
- "Choice of law: Colorado" (Item 11) and the 00 guide's "the policy follows Colorado law" are never explained.
- Item 11 also sets the court venue (V.8.3) and the interest rate (V.7.3), so "choice of law" is a narrower label than its actual role.
- R1 found at search-snippet level that Corgi's cyber is written by a risk retention group. A Corgi reviewer will notice the contrast.

**(ii) Best justification.**
- L38: "State-approved form and guaranty fund protection matter to small businesses".
- Notice 4 mentions the guaranty association.
- Colorado is Cedar Ridge's home state (Item 1).
- [PR] Admitted forms generally follow the law of the state of issue, so Item 11 is a per-policy entry, not a product-wide choice.

**(iii) Draft — rewrite in your own words.** "I modeled Harborline as an admitted insurer so a small business buying without a broker gets a state-approved form and guaranty-fund protection. The cost is slower filings and less pricing freedom than surplus lines. Colorado law applies here only because Cedar Ridge is in Denver; each policy uses its insured's home state."

### 5. Coverage A cap ($25,000 for 72 hours) and pre-incident help ($2,500) (Item 4, I.A, V.2.3)

**(i) Gap.**
- The only reason given for $25,000 is "Needed to price it" (L232). That explains why a cap exists, not why this amount.
- $2,500 is 2.5× Coalition's $1,010 pre-claim assistance (C11), with no reason given.

**New: the two services overlap.**
- Pre-incident help applies to "something suspicious that is not yet an **incident** (such as a phishing attempt or an unusual login)" (V.2.3).
- Coverage A already responds to "an actual or **suspected** incident" (I.A).
- A phishing attempt or unusual login is a suspected incident, so it isn't clear when the $2,500 would ever apply.

Also:
- III.1.2 names only Coverage A as sitting outside the aggregate. Pre-incident help is outside it per Item 4 and V.2.3, but III.1 doesn't say so.
- R1: neither service has a per-period cap.

**(ii) Best justification.**
- C11: Coalition provides 72-hour breach response outside limits and $1,010 of pre-claim help.
- [PR] $25,000 roughly buys the first three days of breach-coach time plus initial forensic triage for a small firm. The cap stops the free service from turning into a full investigation outside the limit.
- Define pre-incident help as questions **before anything is suspected**, or fold it into Coverage A.

**(iii) Draft — rewrite in your own words.** "The first 72 hours of help are free and outside the limit, up to $25,000, roughly what a breach coach and first-response forensics cost in the first three days. Pre-incident help is for questions before anything is suspected, such as 'is this email phishing?'. So it is small: $2,500, against Coalition's $1,010."

### 6. Sublimit amounts for D (system failure), K, M, N, O and G (Item 6)

**(i) Gap.** The rationale explains why each coverage is core and why it has a sublimit (L72, L82, L238), but never why these amounts:

| Coverage | Sublimit | What the rationale says about the amount |
| --- | --- | --- |
| D, system failure | $250K | Nothing |
| K, PCI | $250K | Nothing at all |
| M, bricking | $100K | Nothing |
| N, reputational harm | $100K | Nothing |
| O, cryptojacking | $50K | Nothing |
| G, security improvements | $25K | "a small, clear budget" |

**(ii) Best justification.**
- D (system failure): Aon's CrowdStrike analysis (#18) supports having a sublimit. [PR] $250K equals the fraud limit and 25% of the aggregate.
- M: [PR] Cedar Ridge has 71 laptops, 14 phones and 2 servers (App 4.4). Replacing all of them costs roughly $100K.
- K: [PR] Cedar Ridge takes cards only through a hosted page (SAQ A), with about $410K a year in card volume (App 3.10). Card-brand assessments scale with the number of cards exposed.
- N and O: nothing in the package. Label them honestly as introductory sublimits pending data.

**(iii) Draft — rewrite in your own words.** "Coverages the market only recently put in base forms (bricking, reputational harm, cryptojacking) come in at small sublimits so they don't move the base price. $100,000 would replace every laptop, phone and server at a firm like Cedar Ridge. PCI is capped at $250,000 because most small merchants take cards through a hosted page, as Cedar Ridge does."

### 7. The two 20% coinsurances: ransomware without verified backups; known-exploited vulnerability unpatched for 45 days (Item 7, III.1.6–1.7, IV.1)

**(i) Gap.**
- Neither 20% is explained. L123 says "Market coinsurance practice", with no source.
- The 45 days comes from Chubb's endorsement (L146), which isn't in 04 (R1).

New issues:
- **The two coinsurances can stack.** A ransomware attack through an unpatched known-exploited vulnerability, with unverified backups, triggers both, and the policy is silent.
- **"Ransomware" is undefined.** It's unclear whether the backup coinsurance applies to business interruption and restoration after a ransomware attack, or only to Coverage C.
- **The wording differs.** IV.1 says "stayed unpatched"; III.1.7 says "unpatched and unmitigated".

**(ii) Best justification.** [SS] Chubb's Neglected Software Exploit endorsement allows 45 days from public vulnerability disclosure (CVE publication), then shifts a rising share of loss to the insured over the following months. The snippets reach about 25% after a year, but they disagree on the exact steps, so treat those as unverified.

Harborline's version is gentler on the trigger (only vulnerabilities in CISA's Known Exploited Vulnerabilities catalog (#33), and the clock starts at the insurer's written notice). It is simpler on the amount (a flat 20%).

**(iii) Draft — rewrite in your own words.** "A flat 20% is enough to change behavior but still leaves 80% of the loss paid. It applies only after we have warned you in writing and you've left the hole open 45 days, which is Chubb's grace period, and never twice for the same loss."

### 8. Service standards: "we aim" in the policy, "binding" in the rationale (V intro, V.7, L162, L178, L247)

**(i) Gap.**
- V.7 says "we **aim** to" (1 hour, 30 days, 15 days).
- L162 says the conditions "turn 2026 marketing promises (fast response, cash advances, one accountant) into **binding contract terms**".
- L178 says "Turns marketing claims into **contract promises** a small business can rely on".
- The V intro calls Parts 7–8 "**commitments**".
- L247 records that the policy was deliberately softened from "Firm promises" to "Service standards". L162 and L178 were never updated to match.

The numbers themselves are also unexplained. "Coalition advertises a 5-minute average response" is not in the ledger (R1), and it doesn't explain why 1 hour.

**(ii) Best justification.** L247: "Unfair claims practices laws already set timelines". [PR] The standards restate those duties in plain numbers and add one real remedy (statutory interest on late payment). One promise is genuinely firm: the business interruption advance ("we will advance").

**(iii) Draft — rewrite in your own words.** "Response, decision and payment times are service standards, not guarantees. The payment standard has teeth, because we add statutory interest if we're late. The business interruption advance is the one firm promise, because payroll can't wait."

### 9. "Executive": called narrow, drafted broad (II Executive; L110)

**(i) Gap.** L110 says: "Executive defined narrowly | Coalition's 'senior executive' | Prior-knowledge rules should apply only to people who would actually know."

The text says: "any owner, partner, principal, officer, director, managing member or general counsel, **and the person responsible for your information technology or security**."

- In a CPA partnership, "any partner" can be many people.
- The security-failure definition covers rogue acts only by an "employee (other than an **executive**)". Including the IT lead therefore removes the insider with the most access from the rogue-employee cover that L94 and IV.1 advertise.
- "Executive" also drives known problems (IV.2.2), rescission (V.3.3), intentional acts (IV.2.4) and the notice trigger (V.1.1). The breadth matters everywhere.

**(ii) Best justification.** [PR] Including the IT lead for **knowledge** makes sense, because that person is most likely to know about a problem before inception. Two options:
- Keep the IT lead in the definition but carve them out of the rogue-act exception, or
- Reword L110 from "narrowly" to "decision-makers plus the IT lead".

**(iii) Draft — rewrite in your own words.** "'Executive' means owners, officers and the person running IT, because they are the people whose knowledge should count for 'known problems'. An insider attack by anyone else is covered; I [chose / chose not] to cover a rogue IT lead, because …"

### 10. Target market: $1M–$50M revenue and 10–250 employees (Summary L9; 00 guide)

**(i) Gap.**
- No source for either range.
- The evidence base is mostly firms under $25M (C2, C8).
- "10–250 employees" appears only in the rationale Summary. It isn't in the 00 guide, the policy or the application's eligibility questions.
- "Unlike startups, they buy cyber insurance to survive ransomware and fraud, often without a broker or IT team" is unsupported.
- NAIC #15 is listed for "market size" but never used.

**(ii) Best justification.**
- Cedar Ridge's own history shows the lower-end alternative: a $50K cyber sublimit inside a business owners policy (App 2.5).
- The $25–100M fraud figure (C8) supports extending Coverage R upward.
- [PR] 250 employees matches common definitions of a small or mid-sized enterprise.

**(iii) Draft — rewrite in your own words.** "I aimed at firms from $1M to $50M in revenue. Below that, most businesses buy a small cyber add-on to their business owners policy, as Cedar Ridge did; above it, firms usually use brokers and bespoke programs. My claims data mostly covers firms under $25M, so terms above that are less tested."

Either drop "10–250 employees" or add it to the 00 guide and to eligibility.

### 11. Claim-free reduction: 25% a year to a $2,500 floor (Item 5, V.6.1, L176, L231)

**(i) Gap.**
- The 25% step and the $2,500 floor are unexplained.
- The source (#6 Coalition FAQ) was not re-opened.
- "Claim-free" is undefined, and it's unclear whether reductions compound or are linear (R1).
- Item 5 omits V.6.1's "or on a timeline we agree in writing".

**(ii) Best justification.** [SS] Coalition's Vanishing Retention cuts the retention 25% after one claim-free year, 50% after two and 100% after three. It applies to insureds under $100M revenue with retentions of $25K or less. It requires fixing critical vulnerabilities within 30 days.

So Harborline copies Coalition's first step and 30-day rule and stops at a floor instead of vanishing. **L176's "kept modest" is accurate and can now be cited.** Coalition's steps are measured from the original retention, which suggests Harborline should be linear too ($7,500 → $5,625 → $3,750 → $2,500 floor), not compounding as QR's worked example assumes.

**(iii) Draft — rewrite in your own words.** "The claim-free reduction follows Coalition's Vanishing Retention: 25% of the original retention per claim-free year, if critical findings are fixed within 30 days. It stops at $2,500 instead of reaching zero, so an insured always keeps a stake in the first loss."

### 12. Business interruption cash advance: 50%, 10 business days, $250K cap (V.7.4)

**(i) Gap.**
- The cap's only reason is "Needed to price it" (L248).
- 50% and 10 business days are unexplained.
- A fixed $250K doesn't scale with the $2M and $3M limit options (App 2.2). QR describes it as "25% of the $1M limit".

**(ii) Best justification.**
- C15: Coalition's Cashflow Lifeline is discretionary; Harborline's is firm.
- [PR] 10 business days is one biweekly payroll cycle.
- [PR] Advancing only 50% of the estimate to date keeps the advance below the likely final payment, so clawbacks are rare.
- [PR] Consider stating the cap as "25% of the aggregate".

**(iii) Draft — rewrite in your own words.** "Once coverage is confirmed we advance half our estimate within 10 business days, about one payroll cycle, capped at $250,000 (a quarter of a $1M limit). Advancing half keeps us from overpaying before the numbers are final."

### 13. Duty to defend, and defense costs inside the limits (notice 3, III.7.1, III.7.3)

**(i) Gap.** The rationale has no row for either choice, although the policy repeats "Defense costs reduce your limits" four times.

**(ii) Best justification.** [PR] Both are common in small-business cyber forms. Verify this against At-Bay's form (#1) and Coalition's issued policy (#4), which were checked for other terms.
- A duty to defend matters most to firms without in-house counsel.
- Defense inside limits keeps the price predictable.
- The 100% defense on mixed claims (L137) softens the trade-off.

**(iii) Draft — rewrite in your own words.** "We defend claims ourselves rather than reimburse you, because a small business shouldn't have to find and pay lawyers first. Defense costs sit inside the limit, as in the forms I compared, which keeps the premium predictable. The trade-off is that a long lawsuit can use up the limit."

### 14. Business interruption and reputational time windows: 180 days; 14 days + 90 days (N); 90 days (S)

**(i) Gap.**
- The 180-day restoration period is argued with "Vouch's 90 days is too short when about 1 in 10 ransomware cases cause 30+ days of downtime" (L48). A 30-day outage fits inside 90 days, so the argument doesn't work.
- Coverage N's 14-day wait and 90-day period have no rationale.
- Coverage S's 90 days has no rationale.

**(ii) Best justification.**
- C12: At-Bay uses 180 days; L102 says Coalition does too.
- [PR] The period of restoration runs until **operations return to their prior level**, not just until systems work. An outage that crosses tax season (App 4.20: "about 1 day during tax season") can cost revenue for months.
- [PR] For N, 14 days separates reputational loss from the outage itself (which D covers), and 90 days is one quarter.

**(iii) Draft — rewrite in your own words.** "Restoration runs 180 days because revenue recovers more slowly than systems: an accounting firm that loses its April filing window loses clients for the season. Reputational harm starts after 14 days, so it doesn't overlap the outage itself, and runs one quarter."

### 15. Key customer: 10%, naming, and why Coverage S is optional (II Key customer, I.S, App 1.10)

**(i) Gap.**
- Why 10% is never explained.
- **Mismatch:** App 1.10 asks "more than 10%"; the definition says "at least 10%".
- The definition requires a customer "named in Item 6", but Item 6 has no field for names.
- Coverage S shows no limit or waiting period.
- An attack on a key customer isn't an "incident" as defined, yet coverage condition I(2) requires the insured to "first discover the **incident**".
- Why S is optional isn't stated.

**(ii) Best justification.**
- [PR] 10% is the major-customer disclosure threshold in U.S. GAAP segment reporting (ASC 280).
- C15: Coalition offers Key Customer cover.
- Most small businesses have no 10% customer. Cedar Ridge's largest client is about 3% (App 1.10).

**(iii) Draft — rewrite in your own words.** "A key customer is one that provides 10% or more of revenue, the same threshold accountants use to disclose major customers. The cover is optional because most small businesses, Cedar Ridge included, don't have a customer that large."

### 16. Fraud: $100K reduced limit, $5,000 callback threshold, phone and video channels (Item 7, III.6.1)

**(i) Gap.**
- The $100K is unsourced. L214 says "$100K–$250K social engineering sublimits are common" with no source.
- The $5,000 threshold is attributed to Coalition's application and FBI/IC3 guidance (L133). Neither is in 04.

**New: the verification rule doesn't cover every channel the policy sells.**
- The verification procedure applies only to bank-detail changes and to transfer requests "received by email or message".
- The fraudulent-instruction definition sells phone, video call and letter channels.
- The policy doesn't say whether a transfer made on an unverified deepfake **phone call** counts as an "unverified instruction" that drops the limit.

**(ii) Best justification.**
- C8: At-Bay's average fraud loss is $208K for firms under $25M.
- C10 as resolved: 52% of Coalition's funds-transfer fraud began as email compromise.
- [PR] $100K is 40% of the full limit, at the low end of the market range the rationale cites.

**(iii) Draft — rewrite in your own words.** "Without callback verification the fraud limit drops to $100,000, but only when an employee acts on a request nobody checked. The check applies to bank-detail changes and to transfers over $5,000, the threshold Coalition's application uses, whether the request comes by email, phone or video."

### 17. $2,500 fraud retention for reporting within 72 hours (Item 6 H, I.H, III.6.3)

**(i) Gap.**
- 72 hours is explained (C5, L46, L79). $2,500, a two-thirds cut, is not.
- It's unclear whether $2,500 is fixed for every revenue band or should scale.
- The one-retention rule applies "the largest applicable" retention. So whenever the same incident also triggers Coverage B (for example, a hacked mailbox needing forensics), the $7,500 applies and the reward disappears.

**(ii) Best justification.** C5: 70% of fraud reported within 3 days recovered some funds, against 27% after 30 days. [PR] Express it as one-third of the band retention so it scales.

**(iii) Draft — rewrite in your own words.** "Reporting fraud within 72 hours cuts the retention to a third, $2,500 for Cedar Ridge, because At-Bay found 70% of fast reporters recover some money versus 27% after 30 days. Every dollar recovered lowers what we pay."

### 18. Security improvements (G): $25K and the 90-day window

**(i) Gap.**
- $25K is unexplained.
- The 90 days is attributed to At-Bay's "Post-Cyber Event Hardening", which isn't in 04 (R1).

**New: the 90-day clock has no consistent start.**
- The definition starts it at "a covered **security failure**".
- III.5.3 says only "you must make it within 90 days", with no start point.
- A security failure is often discovered months after it happens, so the window can close before anyone knows. Every other time limit in the policy runs from discovery.

Also, "Included in incident retention" in Item 6 is an undefined phrase.

**(ii) Best justification.** L310 says Coalition's 25% betterment allowance was "Confirmed", although it isn't in C11's text. [PR] A fixed budget is easier to understand than a betterment percentage, and $25K funds about a year of MFA, EDR and backup subscriptions for a firm of Cedar Ridge's size.

**(iii) Draft — rewrite in your own words.** "After a covered attack we pay up to $25,000 for the fix our team recommends, if you make it within 90 days of discovering the attack. A fixed budget is simpler than a betterment percentage and covers a first year of the tools that would have stopped it."

### 19. Reporting windows and extended-reporting price (Item 9; V.1.2; V.5.4–5.5)

**(i) Gap.**
- The 60-day automatic extended reporting period is unexplained.
- Its interaction with the 90-day post-period reporting deadline in V.1.2 is unclear (R1).
- "Annual premium", the base for the 75% and 125% prices, is undefined: $6,120 or $5,508?
- The 60-day window to buy extended reporting is unexplained.

**(ii) Best justification.**
- L166: Coalition allows "60 days after it for late-discovered incidents".
- C12: At-Bay prices extended reporting at 75% and 125%.

**(iii) Draft — rewrite in your own words.** "Claims made during the policy can be reported up to 90 days after it ends. Claims first made in the 60 days after it ends are covered automatically if the incident happened before. Extended reporting costs 75% or 125% of the premium you actually paid, matching At-Bay."

### 20. Plain-language devices promised but not delivered consistently

**(i) Gap.**
- **Plain-English notes.** The cover says "**Plain-English notes** and headings help you find your way", and V.11.6 refers to "plain-English notes". The body contains none. There are no "In short" boxes; the only plain-English devices are the Item 6 column and the IV.1 box.
- **Bold.** "Words in bold are defined", but bold is also used for about 100 run-in headings and for emphasis (for example, "**We bear the burden of proving this exclusion applies.**" and "**covered as described in part 1**").
- **Declarations.** The Declarations mostly leave defined words unbolded (retention, incident, waiting period, system failure). Under the Section II rule ("Words in **bold** have these meanings … including the Declarations"), those words are therefore not defined there.
- **One concept, two names.** "Business interruption restoration period" (Item 6) and "**period of restoration**" (II) are the same thing.
- **One term, two meanings.** "Waiting period" is defined in hours for business interruption, but Coverage N uses a 14-day "reputational waiting period", which is undefined.

**(ii) Best justification.** The plain-English column (L37) and the "What this policy does not exclude" box (L145) are real devices, so point to them.

**(iii) Draft — rewrite in your own words.** "Plain-English help is built into the Declarations' 'what it pays for' column and the 'what we don't exclude' box. Bold headings are labels; only bold words that appear in Section II carry defined meanings."

### 21. Coverage O promises "utility" charges the definition doesn't cover

**(i) Gap.**
- Item 6 O says "Extra cloud, **utility** and phone charges". III.8.3 says "This includes extra cloud, **utility** and telephone charges".
- The definition of **service fraud loss** covers only "charges from your cloud, hosting or telephone providers".
- The rationale (L238) mentions only "$50K including cloud charges".

**(ii) Best justification.** C13: Beazley BBR 5.0 covers cryptojacking including cloud charges. [PR] The electricity used by hijacked hardware is the classic cryptojacking cost for on-premises systems.

**(iii) Draft — rewrite in your own words.** "Cryptojacking cover pays the extra cloud, phone and electricity bills a hijacked system runs up, capped at $50,000 because these bills usually surface within one billing cycle." Fix the definition to add utility providers, or drop "utility" from Item 6 and III.8.3.

### 22. The accounting-firm tailoring is never claimed as tailoring

**(i) Gap.**
- **Funds held for clients.** Funds transfer loss includes money taken "from accounts you hold for clients" (II), which fits Cedar Ridge's payroll work for 40 business clients (App 5.4). There is no rationale row for it.
- **Uneven use of the sample.** Seasonality (III.4.1) is explained (L128), and paper records are explained (L95). But the rationale never states that the sample insured drove specific wording.

**(ii) Best justification.** App 1.8 and 5.4. C23: tax preparers are financial institutions under the FTC Safeguards Rule.

**(iii) Draft — rewrite in your own words.** "Funds transfer loss includes money taken from accounts you hold for clients, because firms like Cedar Ridge run client payroll, and one spoofed instruction can empty a client's account, not just the firm's."

### 23. Ownership and size thresholds: 50% subsidiaries, 20% insured-versus-insured, 25% acquisitions, 90-day grace

**(i) Gap.**
- None of these numbers has a stated reason.
- L173 cites Coalition's change-in-control clause but not the 25% figure.

**(ii) Best justification.** [PR]
- More than 50% is control.
- 20% is the usual accounting presumption of significant influence (ASC 323, equity method).
- 25% of revenue is a common automatic-acquisition threshold in management-liability and cyber forms.
- 90 days is one quarter.

**(iii) Draft — rewrite in your own words.** "Companies you control (more than 50%) are insureds. A company holding a 20% stake either way can't sue you under the policy, because at that level the firms aren't independent. Acquisitions under 25% of your revenue are small enough to add without re-underwriting."

### 24. "Discover" is undefined, yet the discovery trigger is a headline choice

**(i) Gap.**
- L64 presents the discovery trigger as a key design choice. The trigger in I(2) is "you first discover the **incident**", and "discover" is undefined.
- The documents use different starting points:

| Provision | Starting point |
| --- | --- |
| V.1.1 (notice) | "an **executive** becomes aware" |
| G (security improvements) | the date of the security failure |
| III.1.5 (credits) | "first discovered" |
| II, breach response costs | 12 months "after discovering" |

**(ii) Best justification.** [PR] Define discovery once, as the moment an executive first learns facts that would make a reasonable person believe an incident occurred, and run every clock from it.

**(iii) Draft — rewrite in your own words.** "An incident is 'discovered' when an executive first learns of it. That one moment starts every deadline in the policy."

### 25. Standard exclusions with no rationale (IV.2: 1, 3, 11, 13, 14, 16, 19; 7 only partly)

**(i) Gap.** Seven of 19 exclusions have no rationale:
- 1: bodily injury and property damage
- 3: before the retroactive date
- 11: patents and trade secrets
- 13: natural disasters and physical events
- 14: government orders
- 16: nuclear and pollution
- 19: profits you weren't entitled to

Exclusion 7 (employment practices) is explained only through its employee-privacy carve-back.

**(ii) Best justification.** [PR] These keep a cyber policy from overlapping property, general liability, employment practices and patent insurance. L141 says the exclusions follow Coalition's list for structure; confirm each against Coalition's policy (#4).

**(iii) Draft — rewrite in your own words.** "The remaining exclusions are standard across the forms I reviewed. They keep this policy from duplicating property, general liability, employment and patent insurance that small businesses buy elsewhere."

### 26. Fraud cover sits above crime insurance, but the application never asks about it (V.9)

**(i) Gap.** V.9 makes Coverage H excess of any crime or fidelity insurance (L182: "avoids double recovery for fraud"). The application never asks whether the applicant has crime or fidelity cover, so the underwriter can't price where H actually sits.

**(ii) Best justification.** [PR] Crime insurance is the traditional home for social-engineering fraud. Add an application question so the two covers can be coordinated and priced.

**(iii) Draft — rewrite in your own words.** "Fraud cover sits above any crime policy you already have, because crime insurance is the traditional home for this risk. We ask about it so you aren't charged twice."

### 27. Terrorism premium $0 and taxes $0 (notice 7, Item 3)

**(i) Gap.** Both are unexplained.

**(ii) Best justification.** [PR]
- The federal terrorism program (TRIA) requires insurers to offer the cover and to disclose its premium. A $0 charge is a pricing decision and should be stated as one.
- Admitted premiums usually include state premium tax in the rate rather than showing it as a separate line.

**(iii) Draft — rewrite in your own words.** "Terrorism cover is included at no separate charge because cyber terrorism is already part of the risk we price. As an admitted insurer, state premium tax is built into the rate, so it doesn't appear as a separate line."

### 28. Credit monitoring for 24 months; breach costs within 12 months (II Breach response costs)

**(i) Gap.**
- The 24 months rests on L105's "Matches common legal requirements", with no source.
- The 12-month window to incur breach costs is unexplained.

**(ii) Best justification.** [PR] Some states require longer monitoring after Social Security number breaches; Connecticut's 24 months is one example (verify). "Or longer if the law requires" covers any outliers.

**(iii) Draft — rewrite in your own words.** "We pay 24 months of credit monitoring, the longest period common state laws require after a Social Security number breach, and more if a law requires it."

### 29. Verified backups: restore test within 12 months (Item 7, III.1.6)

**(i) Gap.**
- Why 12 months is never explained.
- The package cites CIS Controls v8.1 (#32) for its credits, but [PR] CIS Safeguard 11.5 calls for testing recovery **quarterly** (verify against #32). The policy's standard is looser than the framework it cites, and the rationale doesn't say so.
- Cedar Ridge's test (June 12, 2026) lapses during the term (R1).

**(ii) Best justification.** Practicality for firms without full-time IT staff. Tested backups are "the single best ransomware defense" (L123).

**(iii) Draft — rewrite in your own words.** "We ask for one tested restore a year, less often than CIS recommends, because that's realistic for a small firm and still proves the backups work. The test must fall within 12 months before an incident."

### 30. Full prior acts, and a continuity date at inception (Item 8, App 2.5, 2.8)

**(i) Gap.**
- L50 explains the pairing in one line.
- It doesn't explain why a first-time standalone buyer gets full prior acts.
- It doesn't explain why the continuity date is inception even though Cedar Ridge had a $50K cyber sublimit in its business owners policy (App 2.5).
- With no retroactive date, condition I(1) and exclusion 3 do nothing for this insured. That's fine, but it's worth one line.

**(ii) Best justification.** L50: "Broad cover while still excluding problems already known." [PR] Attackers often sit undetected for months, and exclusion 2 (known problems) protects the insurer.

**(iii) Draft — rewrite in your own words.** "Cedar Ridge gets full prior acts because attacks often go unnoticed for months before discovery. The continuity date protects us by excluding only what an executive already knew. The old business owners policy sublimit wasn't comparable standalone cover, so there was no earlier continuity date to carry over."

---

## 3. Numbers with no defensible basis in the package: justify, change or drop

"Basis" means a source, ledger claim or stated reasoning in the package. Items with only a [PR] basis are **defensible but not yet defended**.

| Number | Where | Basis in package | Recommendation | Why |
| --- | --- | --- | --- | --- |
| $6,120 base premium | Item 3 | None (C26 "non-factual") | **Justify** as a labeled placeholder with a method, or show only the illustrative net | It reads as $5,508 ÷ 0.9 |
| $2,330–$4,048 premium comparators | L25 | None (R1) | **Drop** unless sourced | Unledgered; contradicts L251 |
| $7,078 Vouch median | L25, L329, #17 | Unverifiable (C16; R1) | **Drop** unless link restored | L251 says no median data found |
| 10–250 employees | L9 | None | **Drop**, or add to 00 guide and eligibility | Appears only once |
| $25,000 top retention band | L13 | None | **Justify** with a full band table | Never shown in policy or application |
| $5M band edge | Item 5 | None | **Justify** ([PR] ~0.1% of revenue) | $25M edge is defensible (C2), $5M isn't |
| $25,000 Coverage A cap | Items 4 and 6, I.A, II, III.1.2 | "Needed to price it" | **Justify**; add a per-period cap (R1) | Amount unexplained |
| $2,500 pre-incident help | Item 4, V.2.3 | Coalition $1,010 (C11) | **Change**: merge into Coverage A or redefine; otherwise justify | Overlaps "suspected incident" |
| $2,500 fraud retention for 72-hour reporting | Item 6 H | None for the amount | **Change** to a proportion (for example, one-third of band), or justify | Doesn't scale by band; lost under the largest-retention rule |
| $2,500 retention floor | Item 5, V.6.1 | None | **Justify** and resolve the conflict with the smallest band | Credits can breach it |
| $25,000 security improvements (G) | Item 6 | "a small, clear budget" | **Justify** ([PR] one year of controls) | Amount unexplained |
| $100,000 reduced fraud limit | Item 7 | Unsourced "$100K–$250K common" | **Justify and cite** | Needs a market source |
| $250,000 system-failure sublimit | Item 6 D | Aon supports a sublimit (#18) | **Justify** amount ([PR] 25% of aggregate) | Existence explained, size not |
| $250,000 PCI | Item 6 K | None | **Justify** (SAQ A) or change | No row explains it |
| $100K / $100K / $50K (M, N, O) | Item 6 | None for amounts | **Justify** M (fleet cost); **label** N and O as introductory | |
| $250,000 advance cap | V.7.4 | "Needed to price it" | **Change** to 25% of aggregate, or justify fixed | Doesn't scale with $2M or $3M limits |
| 50% advance, 10 business days | V.7.4 | None | **Justify** ([PR] payroll cycle) | |
| 25% / 50% retention credits; 10% premium credit | Items 5 and 7 | Direction only (C3, C4) | **Justify** | Levels unexplained |
| 4-hour MDR waiting period | Item 7 | Coalition "reduced" wait (C15), no hours | **Justify**, or change to "halved" | |
| 20% ransomware coinsurance | Item 7, III.1.6 | "Market practice", unsourced | **Justify**; add a no-stacking rule | |
| 20% known-exploited-vulnerability coinsurance | III.1.7 | None for 20% | **Justify**, or change to a graduated scale like Chubb's [SS] | |
| 45-day patch window | III.1.7 | Chubb (not in 04) | **Cite** (add Chubb to 04) | |
| 14-day wait, 90-day period (N) | Item 6 N, II | None | **Justify** | Also a term conflict |
| 90 days (S) | I.S | None | **Justify** or align with the 180-day restoration period | |
| 1 hour / 30 days / 15 days | V.7.1–7.3 | Weak (5-minute claim unledgered) | **Justify** via claims-handling timelines | |
| 60-day automatic extended reporting; 60-day election; 60-day non-renewal; 10 / 30-day cancellation notice | Item 9, V.5 | None | **Justify** (Coalition's 60 days, L166; state minimums) | Low risk |
| 12-month restore test | Item 7 | None | **Justify** (looser than CIS [PR]) | |
| 24-month credit monitoring | II | "common legal requirements" | **Cite** | |
| 10% key customer; 20% insured-vs-insured; 25% acquisitions; 50% subsidiaries | II, IV.2.6, V.4.1 | None | **Justify** (accounting thresholds [PR]) | |
| $1M / $2M / $3M limit options | App 2.2 | None | **Justify** why $3M is the ceiling | |
| "About 20 minutes" to complete | App intro | None | **Drop**, or say "we estimate" | Unsupported marketing claim |
| $5,000 callback threshold | III.6.1, App 5.3 | Coalition's application, FBI/IC3 (neither in 04) | **Cite** | |

**No number needs to be dropped on substance except the unsourced benchmarks ($2,330–$4,048; $7,078) and "10–250 employees".** Everything else is defensible with one sentence, but that sentence is currently missing.

---

## 4. Matrix A: numbers (100 elements)

### A1. Limits and sublimits

| ID | Element | Where | Explained? (rationale quote) | Evidence | Consistency | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| N1 | Aggregate $1,000,000 | Item 4; III.1.1; App 2.2, 2.6 | **Yes**. L13 "covers At-Bay's 2026 average claim for firms under $25M revenue ($180K), with room for ransomware ($422K…)"; L39 "Both real small-business policies used $1M" | #13 C2; #2, #4 | Consistent everywhere. App 2.6 (clients require $1M) supports it but isn't cited in rationale | OK |
| N2 | Limit options $1M / $2M / $3M | App 2.2 | **No** | None | Not mentioned in policy or rationale | Needs explanation |
| N3 | Coverage A cap $25,000 | Item 4; Item 6 A; I.A; II Incident response services; III.1.2 | **Partial**. L232 "Capped at $25,000 \| Needed to price it" | Amount: none | Same in 5 places; no per-period cap (R1) | Needs explanation |
| N4 | Coverage A window, 72 hours | Same | **Yes**. L42 "72-hour incident response outside the limit, $0 retention… Coalition… Free early help means faster calls" | #4 C11 | Consistent | OK |
| N5 | Pre-incident help $2,500 | Item 4; V.2.3 | **Partial**. L169 "Coalition's pre-claim assistance ($1,010…)" | C11 ($1,010) | Not listed in III.1 (limits); overlaps I.A "suspected incident" | Consider changing |
| N6 | B limit $1M (full) | Item 6 | **Partial** (Summary #1: "always included") | None | Consistent | OK |
| N7 | C limit $1M (full) | Item 6 | **Yes**. L44 "Vouch's $62,500 ransomware sublimit sits far below At-Bay's $508K average ransomware claim" | C1 ($508K); $62,500 not in ledger | $508K here vs $422K in Summary L13 (R1) | Needs citation |
| N8 | D limit $1M (attacks) | Item 6; I.D | **Yes** (L44) | C1 | Consistent | OK |
| N9 | D system-failure sublimit $250K | Item 6; I.D; III.4.3 | **Partial**. L72 "a sublimit balances protection and accumulation risk" | #18 Aon; #10; #4 | "(higher limits available)" has no matching option (R1) | Needs explanation |
| N10 | E limit $500K | Item 6 | **Yes**. L47 "half the limit balances protection against systemic cloud-outage risk"; L73 "…averaging $145K" | C6; comparators At-Bay $1M and Vouch $25K not in ledger | "(full-limit option available)" not in Part 2 (R1); L47 misquotes C6 ("Vendor-caused" vs "Vendors and customers") | Needs citation |
| N11 | F limit $1M | Item 6 | **Partial**. L75 "restoration is a large part of ransomware cost" | Unsupported | Consistent | OK |
| N12 | G limit $25K | Item 6; I.G | **Partial**. L76 "a small, clear budget" | "Post-Cyber Event Hardening" not in 04 (R1) | Consistent | Needs explanation |
| N13 | H limit $250K, shared | Item 6; I.H; Item 7 | **Yes**. L45 "Covers the $208K average fraud loss under $25M" | C8; #2, #4 | Consistent | OK |
| N14 | H reduced limit $100K (no callback) | Item 7; III.6.1 | **Partial**. L214 "$100K–$250K social engineering sublimits are common"; L236 | Unsupported | Consistent | Needs citation |
| N15 | R option $500K | Item 6 Part 2; I.R | **Yes**. L45 "option for firms nearer $373K ($25–100M)" | C8 | Consistent | OK |
| N16 | R option $1M with 24/7 MDR | Item 6 Part 2 | **Yes**. L237 "At-Bay's MDR packages offer up to $1M" | #12 (not re-opened; no ledger entry) | L45 and L214 still say "$500K option" only | Needs citation |
| N17 | K PCI $250K | Item 6 | **No** (L82 explains core placement only) | None | Consistent | Needs explanation |
| N18 | I, J, L at $1M | Item 6 | **Partial** (full limit implied) | None | Consistent | OK |
| N19 | M bricking $100K | Item 6 | **Partial**. L238 "Core, with sublimits ($100K; …)" | C13 (placement only) | "(full-limit option available)" not in Part 2 (R1) | Needs explanation |
| N20 | N reputational $100K | Item 6 | **Partial** (L238) | C13 | Consistent | Needs explanation |
| N21 | O cryptojacking $50K | Item 6 | **Partial**. L238 "$50K including cloud charges" | C13 | Scope mismatch: see T39 | Needs explanation |
| N22 | Proof-of-loss help $50K per incident, inside aggregate | III.1.8; II Business income loss | **Yes**. L100 "Coalition sells it as a separate $50K coverage" | #4 (L310 "Confirmed"), #8 C13; **C11 text omits $50K** | Consistent | Needs citation |
| N23 | Business interruption advance cap $250K | V.7.4 | **Partial**. L248 "Capped at $250K \| Needed to price it" | None | Fixed dollar amount while QR calls it "25% of the $1M limit" | Needs explanation |
| N24 | "Most payable in one year: $1,027,500" | QR only | n/a | n/a | Assumes per-period caps that don't exist (R1) | Inconsistent |

### A2. Retentions and credits

| ID | Element | Where | Explained? | Evidence | Consistency | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| N25 | Standard retention $10,000 | Item 5; Item 7; App 2.3; UW | **Partial**. L40 "Vouch and Corgi ($10K)… $10K mid-sized ones" | Comparators not in ledger | Consistent | Needs citation |
| N26 | Band edges $5M / $25M | Item 5; UW | **No** | $25M matches C2 and C8 bands (unstated) | Only one band shown anywhere | Needs explanation |
| N27 | Retention range $2,500–$25,000 | L13 | **Partial** | None | $25,000 as a retention appears nowhere else; lowest band collides with the $2,500 floor (N36) | Inconsistent |
| N28 | MFA+EDR credit 25%, giving $7,500 | Item 5; Item 7; UW | **Partial**. L229 "60% of Akira ransomware victims had a leading EDR tool and were still compromised" | C3 | Consistent math | Needs explanation |
| N29 | 24/7 MDR halves the retention ($5,000) | Item 5; Item 7 | **Partial** (L229) | C3; C15 | Item 5 "would halve it" vs Item 7 "$5,000" (R1); stacking rule missing | Inconsistent |
| N30 | $7,500 on B, C, F, I–M, O | Item 6 | **Yes** (derived) | Math | Consistent | OK |
| N31 | G: "Included in incident retention" | Item 6 G | **No** | None | Undefined phrase; if only D (time retention) applies, G's dollar retention is unclear | Needs explanation |
| N32 | H $2,500 if reported within 72 hours | Item 6 H; I.H; III.6.3 | **Partial** (72 hours only: L46, L79) | C5 | The largest-retention rule (III.1.3) overrides it when B co-triggers | Needs explanation |
| N33 | A retention $0 | Items 4 and 6; I.A | **Yes** (L42) | C11 | Consistent | OK |
| N34 | One retention per incident (the largest) | Item 5; III.1.3 | **Yes**. L41, L120 | C12 | Consistent | OK |
| N35 | Claim-free reduction 25% a year | Item 5; V.6.1 | **Partial**. L176 "Coalition's Vanishing Retention… kept modest" | #6 (not re-opened); [SS] Coalition 25%/50%/100% | Compounding vs linear unclear (R1); QR assumes compounding | Needs explanation |
| N36 | Claim-free floor $2,500 | Item 5; V.6.1 | **No** | None | Conflicts with $2,500 lowest band plus credits | Inconsistent |
| N37 | Fix critical findings within 30 days | Item 5; V.6.1; UW | **Partial**. L231 | [SS] Coalition requires the same 30 days | Item 5 omits "or on a timeline we agree in writing"; UW says fixing a **medium** finding keeps eligibility (R1) | Inconsistent |
| N38 | Hardened remote access: 10% premium credit | Item 3; Item 7; UW | **Partial**. L230 "remote access tools were the entry point in 87%" | C4 | Item 3 labels it generically "Security credit" | Needs explanation |
| N39 | MDR waiting period 4 hours | Item 7 | **Partial**. L294 "MDR shortens the attack waiting period only" | C15 (no hours) | Unclear whether it reaches E (vendor attacks) | Needs explanation |

### A3. Waiting periods and time windows

| ID | Element | Where | Explained? | Evidence | Consistency | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| N40 | Business interruption waiting period 8 hours (D, E) | Item 6; Item 7; UW; II | **Yes**. L48, L101, L233 | #9, #18; no ledger entry | Consistent | OK |
| N41 | Restoration period 180 days | Item 6; II | **Yes**, but weak. L48 "Vouch's 90 days is too short when about 1 in 10 ransomware cases cause 30+ days of downtime" | C9, C12 | Consistent; the argument doesn't prove 90 < need | Consider changing (the wording) |
| N42 | N waiting period 14 days | Item 6; II; III.8.2 | **No** | None | Defined "waiting period" is in hours, for business interruption | Inconsistent |
| N43 | N period up to 90 days | Item 6; II | **No** | None | Consistent | Needs explanation |
| N44 | S: up to 90 days after key customer restored | I.S | **No** | None | No limit or waiting period shown for S | Needs explanation |
| N45 | G: 90 days | II; III.5.3 | **Partial**. L108 | At-Bay hardening (not in 04) | Definition runs from "security failure"; III.5.3 has no start point | Inconsistent |
| N46 | Breach costs incurred within 12 months of discovery | II; III.2.4 | **No** | None | Consistent | Needs explanation |
| N47 | Credit monitoring 24 months | II Breach response costs (4) | **Partial**. L105 "Matches common legal requirements" | Unsupported | Consistent | Needs citation |
| N48 | H: report within 72 hours | Item 6; I.H; III.6.3 | **Yes**. L46, L79 | C5 | Consistent | OK |
| N49 | Ransom payment reported within 24 hours | III.3.5; III.3 closing | **Yes**. L126–127, L244 | #27 C20; NYDFS 500 (not in 04) | Consistent | Needs citation (NYDFS) |
| N50 | Bank and FBI fraud report "ideally within 24 hours" | III.6.3 | **Partial**. L133 "FBI/IC3" | Not in 04 | Consistent | Needs citation |
| N51 | Containment without consent in the first 72 hours | V.2.2 | **No** | None | Matches the Coverage A window (unstated) | Needs explanation |
| N52 | Response contact within 1 hour | V.7.1 | **Partial**. L178 "Coalition advertises a 5-minute average response" | Unledgered (R1) | Back page says "Our breach coach answers 24/7" | Needs explanation |
| N53 | Written coverage position in 30 days | V.7.2 | **Partial**. L247 "Unfair claims practices laws already set timelines" | Unsupported | Consistent | Needs citation |
| N54 | Pay undisputed amounts in 15 days, plus statutory interest | V.7.3 | **Partial** (L178, L247) | Unsupported | Consistent | Needs citation |
| N55 | Advance 50% of estimated loss | V.7.4 | **Partial** (L179) | C15 | Consistent | Needs explanation |
| N56 | Advance within 10 business days | V.7.4 | **No** | None | Consistent | Needs explanation |
| N57 | Internal review answered in 30 days | V.8.1 | **Partial** (L181 "Our own design") | Own design | Consistent | OK |
| N58 | Proof of loss 120 days after restoration ends | III.4.5 | **Partial**. L131 "A long outage can outlast a 90-day deadline" | #4 | Consistent | OK |
| N59 | Record review up to 12 months after proof of loss | III.4.6 | **No** | None | Consistent | OK |
| N60 | 12 months of history for business interruption loss | III.4.1 | **Yes** (L128) | #1, #4 | Consistent | OK |
| N61 | Report within 90 days after policy ends | V.1.2 | **Yes**. L166 (vs Coalition 60) | #4 | Interaction with 60-day automatic ERP undefined (R1) | Needs explanation |
| N62 | Automatic extended reporting 60 days | Item 9; V.5.4 | **No** (L51 covers 75%/125% only) | Could cite L166 | Consistent | Needs explanation |
| N63 | Optional extended reporting 12 months / 75%, 24 months / 125% | Item 9; V.5.5 | **Yes**. L51, L175, L303 | C12 | "Annual premium" base undefined | OK |
| N64 | Extended reporting purchase window 60 days | V.5.5 | **No** | None | n/a | Needs explanation |
| N65 | Non-renewal notice 60 days | V.5.3 | **No** (L271 lists as needing review) | None | n/a | Needs explanation |
| N66 | Insurer cancellation notice: 10 days (non-payment) / 30 days (fraud) | V.5.2 | **No** | None | n/a | Needs explanation |
| N67 | Notify removal of a control within 30 days | III.1.5; V.4.3 | **No** | None | Consistent | OK |
| N68 | Acquisition grace 90 days | V.4.1 | **Partial** (L173) | #4 (not ledgered) | Consistent | OK |
| N69 | Known-exploited vulnerability: 45 days after written notice | III.1.7; IV.1 | **Partial**. L146 "Chubb's… 45-day patch grace period" | Chubb not in 04 (R1); [SS] | IV.1 "unpatched" vs III.1.7 "unpatched and unmitigated" | Needs citation |
| N70 | Restore test within 12 months | Item 7; III.1.6 | **No** | [PR] CIS 11.5 is quarterly | Lapses mid-term for Cedar Ridge (R1) | Needs explanation |
| N71 | Policy period Oct 15, 2026 to Oct 15, 2027, 12:01 a.m. | Cover; Item 2 | n/a (sample fact) | App 2.1, 2.5 | Consistent | OK |
| N72 | Continuity date = inception (Oct 15, 2026) | Item 8 | **Partial** (L50) | #4 | Prior $50K business owners policy cover not addressed | Needs explanation |

### A4. Percentages

| ID | Element | Where | Explained? | Evidence | Consistency | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| N73 | Ransomware coinsurance 20% (insurer pays 80%) | Item 7; III.1.6 | **Partial**. L123 "Market coinsurance practice, applied as a reward" | Unsupported | "Ransomware" undefined; scope unclear | Needs citation |
| N74 | Known-exploited-vulnerability coinsurance 20% | III.1.7; IV.1 | **No** (L245 explains adding it, not the level) | [SS] Chubb uses a graduated scale | Can stack with N73; silent | Needs explanation |
| N75 | Settlement (hammer) clause 70% | III.7.2 | **Yes**. L136, L267 | C11, C12, C13 | Consistent | OK |
| N76 | 100% defense on mixed claims | III.7.4 | **Yes**. L137 "At-Bay's allocation clause" | Not in C12's text | Consistent | Needs citation |
| N77 | Subsidiaries owned more than 50% | II Insured | **No** | None | Consistent | OK |
| N78 | Insured-vs-insured 20% ownership | IV.2.6 | **No** | None | Consistent | Needs explanation |
| N79 | Acquisitions under 25% of revenue covered automatically | V.4.1 | **Partial** (L173, no %) | None | Consistent | Needs explanation |
| N80 | Key customer 10% | II; App 1.10; UW | **No** | None | App "more than 10%" vs definition "at least 10%" | Inconsistent |

### A5. Dollar thresholds and premium

| ID | Element | Where | Explained? | Evidence | Consistency | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| N81 | Callback threshold $5,000 | III.6.1; App 5.3 | **Yes**. L133 "Coalition's application asks about verifying transfers over $5,000; FBI/IC3 callback guidance" | Neither in 04 | Consistent. Item 7 label "for **all** payment and bank-detail changes" is looser than III.6.1 | Needs citation |
| N82 | Dual approval above $10,000 | App 5.1 | n/a (applicant's own control; no policy term) | n/a | Doesn't feed any credit | OK |
| N83 | Terrorism premium $0 | Notice 7; Item 12 | **No** | None | Item 3 has no terrorism line | Needs explanation |
| N84 | Taxes and fees $0 | Item 3 | **No** | None | Consistent with admitted status (unstated) | Needs explanation |
| N85 | Base premium $6,120 | Item 3 | **No** | C26 non-factual | Equals $5,508 ÷ 0.9 | Needs explanation |
| N86 | Credit −$612 | Item 3 | **Yes** (math: QR) | QR | Label "Security credit (see Item 7)": only one of five Item 7 rows changes premium | Consider changing (label) |
| N87 | Total $5,508, "illustrative" | Item 3; 00 guide; L25, L251, L329 | **Partial** | C16 uncertain; $2,330–$4,048 unsupported | L251 "No primary 2025–26 median-premium data found" vs L25 and L329 citing a Vouch "median" | Inconsistent |
| N88 | Premium positioned "between" (L25) vs "near" $7,078 (L329) | Rationale | n/a | n/a | Two framings | Inconsistent |

### A6. Sample-insured facts (application)

| ID | Element | Where | Explained? | Evidence | Consistency | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| N89 | Revenue $8.1M last year / $8.5M projected | App 1.9; UW | n/a | n/a | UW uses projected $8.5M; the rule for which figure sets the band is unstated | Needs explanation |
| N90 | 62 employees (54 full-time, 8 seasonal); Boulder office of 9 | App 1.4, 1.11; 00 guide | n/a | n/a | Consistent ("62-person") | OK |
| N91 | About 31,000 people's records, about 88% in Colorado | App 3.2–3.3; App 7.5 | n/a | C24 | 7.5 says "below the consumer-volume thresholds". About 27,300 Colorado residents is above the 25,000 prong, which applies only with data sales, so the reason given is wrong even if the answer is right (build on R1) | Inconsistent |
| N92 | 2,400 individual and 380 business clients; payroll for 40 | App 1.8, 5.4 | Not tied to "accounts you hold for clients" | n/a | Consistent | Needs explanation |
| N93 | Largest client about 3% | App 1.10 | n/a | n/a | Consistent with "Coverage S not needed" | OK |
| N94 | Restore test June 12, 2026; restored in 6 hours | App 4.19; UW | n/a | n/a | Lapses mid-term (R1) | OK |
| N95 | Can operate 1 day in tax season, 3 otherwise | App 4.20 | Not used in rationale | n/a | Supports III.4.1 seasonality and the 8-hour wait | OK |
| N96 | Scan Sept 20, 2026: no critical, one medium finding | UW | n/a | n/a | "Fix … keeps … eligible" vs policy's critical-only rule (R1) | Inconsistent |
| N97 | Patching: 72 hours internet-facing, 14 days otherwise; tracks the known-exploited catalog | App 4.10 | n/a | #33 | Consistent with III.1.7 | OK |
| N98 | 71 laptops, 14 phones, 2 servers | App 4.4 | n/a | n/a | EDR "all devices" vs "laptops and servers" (R1) | OK |
| N99 | "Most businesses finish in about 20 minutes" | App intro | **No** | Unsupported | n/a | Consider changing |
| N100 | Loss-history and declination look-back of 3 years | App 2.7, 8.1 | **Partial** (L201 "Standard underwriting practice") | Unsupported | Consistent | OK |

---

## 5. Matrix B: defined terms and word choices (46 elements)

| ID | Term / word choice | Where | Explained? | Evidence | Consistency | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | "Retention" rather than "deductible" | Item 5 "Retention (your deductible)"; II Retention | **No** (rationale itself says "deductibles": L41, L111, L120) | [PR] Market term; covers dollar and time retentions | Retention definition: "For business interruption, the retention is the **waiting period**". Item 6 N puts "14-day waiting period" in the retention column, but N is not business interruption | Needs explanation |
| T2 | "Security failure" rather than "breach" | II; used 31 times | **No** | [PR] Must trigger on ransomware, denial of service, device loss and AI-agent actions even with no data exposure; "breach" has statutory meanings | Cover and Item 6 still say "data breaches" and "after a breach" (acceptable in plain-English copy) | Needs explanation |
| T3 | "Incident" | II; retention unit ("each incident"); triggers | **Partial**. L111 "Related incidents and claims treated as one" | C12 | I(1) lists "media wrongful act or other **incident**", but the incident definition omits media wrongful acts; key-customer attacks (S) are not incidents | Inconsistent |
| T4 | "Discover" / "first discover" | I(2); II Breach response costs; III.1.5; I.H | **No** (undefined) | None | V.1.1 uses "after an **executive** becomes aware"; G runs from the security failure | Needs explanation |
| T5 | "Executive" | II; IV.2.2, IV.2.4; V.1.1; V.3.3; security failure | **Yes**, but untrue. L110 "Executive defined narrowly" | #4 | Text includes "any owner, partner…" and the IT lead | Inconsistent |
| T6 | "Employee" (including volunteers, interns, leased workers) | II | **No** | None | Consistent | OK |
| T7 | "Dependent provider" (any provider, written or electronic agreement) | II; III.4.4 | **Yes**. L104, L240 | #4, #6 | Matches App 6.1–6.2 | OK |
| T8 | "Dependent systems" | II | **Yes**. L93 | #1, #4 | Consistent | OK |
| T9 | "Computer systems" (cloud accounts you administer, personal devices, connected devices) | II | **Yes**. L93 | #1, #4 | Consistent | OK |
| T10 | "System failure" (vendor updates in; infrastructure out) | II; I.D, F, P | **Yes**. L103 | #4, #18 | Item 6 D plain-English matches | OK |
| T11 | "Wrongful collection" | II; IV.2.10; I.Q | **Yes**. L96 | #4 | Consistent | OK |
| T12 | "Tracking technology" (includes chatbots, session replay) | II | **Partial** (L84, L96) | C7 | App 3.8 lists the same tools | OK |
| T13 | "Adverse publication" ("previously non-public") | II; I.N | **No** | None | Consistent | OK |
| T14 | "Reputational waiting period" | II Reputational harm period | **No** | None | Undefined; clashes with defined "waiting period" (hours, business interruption) | Inconsistent |
| T15 | "AI agent" | II; security failure (5) | **Yes**. L185, L243 | Own design | App 6.6 mirrors the definition; rationale files it under the Conditions table | OK |
| T16 | "Fraudulent instruction" (any channel) | II; I.H | **Yes**. L98, L309 | C12, #4 | Verification rule covers email and messages only (III.6.1); employee-transfer prong (R1) | Inconsistent |
| T17 | "Funds transfer loss" including "accounts you hold for clients" | II | **No** | None | Fits App 5.4 | Needs explanation |
| T18 | "Computer fraud" | II | **Partial** | None | Consistent | OK |
| T19 | "Invoice manipulation loss" (net cost; delivered or will deliver) | II; I.H(2); III.6.5 | **Yes**. L99, L241 | #3; C11; C13 | Consistent | OK |
| T20 | "Key customer" | II; I.S; App 1.10 | **No** | None | "Named in Item 6", but no field exists; greater-than vs at-least 10% | Inconsistent |
| T21 | "Continuity date" | Item 8; II; IV.2.2 | **Partial** (L50) | #4 | Consistent | OK |
| T22 | "Full prior acts" | Item 8; II; App 2.8 | **Partial** (L50) | #4 | Consistent | Needs explanation |
| T23 | "Specimen" | Cover; notice 1 | **Yes** (QR) | n/a | Consistent | OK |
| T24 | "Plain-English notes" | Cover "How to read" #3; V.11.6 | **No** | n/a | No such notes exist in the body; there are no "In short" boxes | Inconsistent |
| T25 | "Words in bold are defined" convention | Cover; II intro | **No** | n/a | Bold used for about 100 non-defined run-ins; Declarations leave defined terms unbolded | Inconsistent |
| T26 | "We / you" voice | Policy; application | **Partial** (L62 on "we will pay") | n/a | Policy consistent; rationale mixes I/we (R1); application uses "we" for both the insurer (instructions) and the applicant (answers) | Needs explanation |
| T27 | "Service standards" vs "commitments" vs "binding" | Cover; V intro; V.7; L162, L178, L247 | **Partial** (L247 records the change) | n/a | V intro "commitments"; L162 "binding contract terms"; policy "we aim" | Inconsistent |
| T28 | "Security credit(s)" | Items 3, 5, 7; II Waiting period; III.1.5 | **Partial**. L123 "applied as a reward" | n/a | One word covers a premium credit, retention credits, a coinsurance waiver and limit preservation; undefined | Needs explanation |
| T29 | "Claim-free" | Item 5; V.6.1 | **No** | n/a | Undefined (R1) | Needs explanation |
| T30 | "Critical issue / finding" | Item 5; V.6.1; UW | **No** | n/a | Undefined severity scale; UW relies on "medium" | Needs explanation |
| T31 | "Substantially in place" | III.1.5 | **No** | n/a | Undefined standard | Needs explanation |
| T32 | "Ransomware" | Item 7; III.1.6 | **No** | n/a | Undefined; appears only inside the malicious code and cyber extortion definitions | Needs explanation |
| T33 | "Extended reporting period" | Notices 2; I(3); Item 9; V.5 | **No** | n/a | Not a bold defined term, although central to the claims-made trigger | Needs explanation |
| T34 | "Policy aggregate limit" | Item 4; III.1.1 | **Yes** (L119) | #4 | Bold but not in II (acceptable) | OK |
| T35 | "Breach coach", "panel", "incident response team" | II; III.2; III.4.2; III.5.3; V.7 | **Partial** (L124) | n/a | Undefined but operative (G requires the team's written recommendation) | Needs explanation |
| T36 | "Business interruption restoration period" vs "period of restoration" | Item 6 (bold); II | **No** | n/a | Same concept, two names | Inconsistent |
| T37 | Bold "**security failure or system failure**" as one phrase | I.F; II Restoration costs | n/a | n/a | Formatting: not a defined term | Inconsistent |
| T38 | "Invoice fraud covered under Coverage H" (within "incident") | II Incident; III.6.5 | **Yes**. L292 | n/a | Consistent | OK |
| T39 | "Service fraud loss" | II; I.O; Item 6 O; III.8.3 | **Partial** (L238) | C13 | Definition: "cloud, hosting or telephone providers"; Item 6 and III.8.3 add "utility" | Inconsistent |
| T40 | "Media content" (including AI-created) | II; IV.1 | **Yes**. L158 | #25, #26, C19 | Consistent | OK |
| T41 | "Personal information" (biometric; paper) | II | **Yes**. L95, L97 | #4 | Left unbolded in I.Q and the wrongful collection definition | OK |
| T42 | "Privacy event" (including data held by a dependent provider) | II | **Partial** (L95) | #4 | Consistent | OK |
| T43 | "Damages": punitive under the most favorable law | II; III.7.5 | **Yes**. L106 | #4 | Consistent | OK |
| T44 | "Admitted insurer" | Cover; notice 4; Declarations | **Partial** (L38) | Unsupported (#15 unused) | L38 "Coalition (admitted)" vs #6 "Coalition's newer surplus-lines form" | Needs explanation |
| T45 | "Choice of law" label for Item 11 | Item 11; V.7.3; V.8.3 | **No** | n/a | Also used as venue and interest-rate state | Needs explanation |
| T46 | Novelty words: "no competitor has" (L31), "No competitor explains" (L37), "is new" (L49); ten "Our own design" labels | Rationale | n/a | Based on 5 forms | Universal claims from a small sample; "Recoveries repay the insured's retention first \| Our own design" (L135) is a common market term | Consider changing (wording) |

---

## 6. Matrix C: structural choices (46 elements)

| ID | Choice | Where | Explained? | Evidence | Consistency | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | Core plus options in one form | Item 6; I intro | **Yes**. Summary #1; L43 | #11 | Consistent | OK |
| S2 | Admitted insurer | Notice 4; Declarations | **Partial**. L38 | #15 listed, not used | Trade-off missing (QR steel-man "say so in the memo") | Needs explanation |
| S3 | Colorado law (Item 11); "the policy follows Colorado law" (00 guide) | Item 11; 00 guide | **No** | None | Guide implies product-wide; Declarations imply per-policy | Needs explanation |
| S4 | Discovery trigger for first-party; claims-made-and-reported for liability | Notice 2; I "When coverage applies" | **Yes**. L64 | #1, #4 | "Discover" undefined (T4) | OK |
| S5 | Duty to defend | III.7.1 | **No** | None | n/a | Needs explanation |
| S6 | Defense inside limits | Notice 3; Declarations; II Claim expenses; III.7.3 | **No** | None | Consistent in four places | Needs explanation |
| S7 | One aggregate with sublimits inside | Item 4; III.1.1 | **Yes**. L119 | #4 | Consistent | OK |
| S8 | Coverage A and pre-incident help outside the aggregate | Item 4; III.1.2; V.2.3 | **Yes**. L42, L119, L169 | C11 | III.1 names only A | Inconsistent |
| S9 | One retention per incident | Item 5; III.1.3 | **Yes** | C12 | Consistent | OK |
| S10 | Waiting period as a time deductible (loss during the wait never paid) | II Waiting period | **Yes**. L101 | #18 | Consistent | OK |
| S11 | M, N, O moved into core | Item 6; L238–239 | **Yes** | C13; #6 | L83's "Borrowed from" cell still argues the old split | OK |
| S12 | P optional | Item 6; I.P | **Yes**. L74 | #18 | Consistent | OK |
| S13 | Q optional (priced) | Item 6; I.Q | **Yes**. L84 | C7; #28 | Summary's "Rarer or systemic risks stay optional" doesn't fit Q (CIPA drives 34% of liability claims) | OK |
| S14 | R optional | Item 6; I.R | **Partial** (L45, L237) | C8; #12 | Consistent | OK |
| S15 | S optional | Item 6; I.S | **Partial** (L184, L216) | C15 | Why optional not stated; no limit shown | Needs explanation |
| S16 | System failure in core (D) with a sublimit | Item 6; I.D | **Yes**. L72 | #18, #10, #4 | Consistent | OK |
| S17 | Vendor attacks (E) in core at $500K | Item 6; I.E | **Yes**. L73 | C6 | Consistent | OK |
| S18 | G is the only way the policy pays for upgrades | III.5.3 | **Yes**. L76 | #4 | Consistent | OK |
| S19 | Trigger rules stated once, up front | I | **Yes**. L63 | #4 | Consistent | OK |
| S20 | Pay vendors directly | I "Two promises" | **Yes**. L67 | Coalition approach not in 04 or ledger | Consistent | Needs citation |
| S21 | Affirmative AI promise | I "Two promises"; IV.1 | **Yes**. L66, L158 | #25, #26, C19 | Consistent | OK |
| S22 | "What this policy does not exclude" box | IV.1 | **Yes**. L145 | Own design | Cross-references resolve | OK |
| S23 | Unexplained standard exclusions: 1, 3, 11, 13, 14, 16, 19 (and 7 in part) | IV.2 | **No** | None | n/a | Needs explanation |
| S24 | Modern war exclusion (attribution, insurer burden, continued help) | IV.2.15 | **Yes**. L153–155 | #7 C14; #22; #23 | Consistent | OK |
| S25 | Known-exploited coinsurance as the only patching consequence | III.1.7; IV.1 | **Partial**. L146, L245 | Chubb (not in 04) | Summary #5 says the policy doesn't use "patching lapses"; L212 omits the coinsurance | Inconsistent |
| S26 | Honest mistakes and proportionate remedy; rescission only for knowing misstatements | V.3.2–3.3 | **Yes**. L170–171 | C18; UK Insurance Act 2015 not in 04 (R1) | Application omits "material" | OK |
| S27 | Pre-issue scan estoppel | V.3.4; App intro | **Yes**. L172, L246 | Own design | Consistent | OK |
| S28 | Notice-prejudice standard and 90-day window | V.1.2–1.3 | **Yes**. L166 | #4; "Frequently cited denial trigger" (L213) unsupported | R1 issues | Needs citation |
| S29 | Circumstances notice | V.1.4 | **Yes**. L167 | #4 | Consistent | OK |
| S30 | Service standards | V.7.1–7.3 | **Partial** | See T27 | "Aim" vs "binding" | Inconsistent |
| S31 | Business interruption cash advance | V.7.4 | **Yes** (as a feature). L179 | C15 | Numbers unexplained (N55–56) | OK |
| S32 | Single forensic accountant | V.7.5 | **Yes**. L180 | C15 | Consistent | OK |
| S33 | Dispute ladder (review, mediation, court or arbitration) | V.8 | **Yes**. L181, L249 | Own design | Consistent | OK |
| S34 | Liberalization | V.11.7 | **Yes**. L250 | "Coalition's one-year liberalization clause": not ledgered | Consistent | Needs citation |
| S35 | Worldwide territory | V.11.1 | **Yes**. L183 | #4 (quote not ledgered) | Consistent | OK |
| S36 | Other-insurance order: A and B primary; H excess of crime; rest excess | V.9 | **Yes**. L182 | #4 | Application never asks about crime or fidelity cover | Needs explanation |
| S37 | Pro rata refund if the insured cancels | V.5.1 | **Yes**. L174 | #4 | Consistent | OK |
| S38 | Recoveries go to the insured's retention first | III.6.4; V.10.2 | **Yes**. L135 "Our own design" | Common market term [PR] | Consistent | OK |
| S39 | Change-in-control run-off | V.4.2 | **Yes**. L173 | #4 | Consistent | OK |
| S40 | Insurer may cancel only for non-payment or fraud | V.5.2 | **No** | None | Consistent | Needs explanation |
| S41 | Application built on NIST CSF 2.0 functions and CIS v8.1 | App Part 4 | **Yes**. Summary #7; L196 | #31, #32 | Section headers match the six functions | OK |
| S42 | Two signatures (executive and IT lead) | App Part 9 | **Yes**. L202 | C18 | Consistent | OK |
| S43 | Underwriter page mapping every starred answer to a term | UW | **Yes**. Summary #7 | n/a | All 8 starred answers are mapped | OK |
| S44 | Coverage letters A–S aligned across documents | Item 6; I; App 2.4 | **Yes**. L65 | Own design | Consistent | OK |
| S45 | "What to do" back page | Back page | **Yes**. L54 | #2 | "Our breach coach answers 24/7" vs V.7.1 "we aim … within one hour" | Inconsistent |
| S46 | Declined features (unlimited reinstatements, zero retention after ransomware, deepfake endorsement) | L257–263 | **Yes** | #12 (secondary); Coalition deepfake endorsement not in 04 (R1) | L261 assumes a "new carrier", which is stated nowhere else | OK |

---

## 7. Matrix D: assumptions (15 elements)

| ID | Assumption | Where | Explained? | Evidence | Consistency | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | Premium is illustrative | Item 3; 00 guide; L251 | **Partial** | C26 | See N85–N88 | Inconsistent |
| A2 | Retention band schedule $2,500–$25,000 | L13; L40 | **Partial** | Comparators not ledgered | Full table missing; floor conflict | Inconsistent |
| A3 | Target $1M–$50M revenue | L9; 00 guide | **No** | None; evidence mostly under $25M | Consistent between rationale and guide | Needs explanation |
| A4 | 10–250 employees | L9 only | **No** | None | Absent from 00 guide, policy and application | Inconsistent |
| A5 | Example industries (accounting, clinics, retailers, light manufacturers) | L9 | **Partial** | n/a | HIPAA question (App 7.2) and HHS example support clinics; key customer supports manufacturers | OK |
| A6 | "Unlike startups … often without a broker or IT team" | L9 | **No** | Unsupported | Cedar Ridge has an IT manager and a managed IT provider (App 1.15, 4.3) | Needs citation |
| A7 | Sample insured profile | Application; 00 guide | **Partial** | n/a | Mostly consistent; see N89–N98 | OK |
| A8 | Regulatory status date | L273 "(September 26, 2026)"; 00 guide "as of September 27, 2026"; 04 footer Sept 27 | n/a | C20, C21 | One-day mismatch | Inconsistent |
| A9 | Direct distribution ("Producer: Direct (no broker)") | Declarations | **Partial** (L9) | Unsupported | Not listed in 00 guide assumptions | Needs explanation |
| A10 | Harborline is a "new carrier" | L261 | **No** | n/a | Not stated in 00 guide or policy | Needs explanation |
| A11 | Admitted and Colorado | Notice 4; Item 11; 00 guide | **Partial** | See S2, S3 | See S3 | Needs explanation |
| A12 | Figures as of Sept 27, 2026 | 04 footer | n/a | n/a | Consistent with guide | OK |
| A13 | Colorado amendatory endorsement not reproduced | Notice 9; Item 12; 00 guide | **Yes** | n/a | Consistent | OK |
| A14 | "Items a real filing would still need" | 00 guide vs L269–271 | **Partial** | n/a | Guide omits the service-standard interest remedy, key-customer pricing and mixed-claim defense listed in L271 | Inconsistent |
| A15 | CIRCIA unpublished; SB 690 awaiting the Governor | L277, L280; 00 guide | **Yes** | C20, C21, #27, #28 | Consistent (the Sept 30 deadline passes three days after submission, so recheck on the day) | OK |

---

## 8. Check 1: cross-references

All cross-references in policy.md, application.txt and rationale.md were checked, plus the "Where" column of 04. There are **52 references: 47 resolve correctly and 5 fail or misdirect.**

| Reference | Location | Target | Result |
| --- | --- | --- | --- |
| "Item 12 … not reproduced" | Notice 9 | Item 12 lists HIC-CY-CO | OK |
| "Security credit (see Item 7)" | Item 3 | Item 7 | OK (label ambiguous, N86) |
| "Item 6 … shows them as purchased" | I intro | Item 6 Part 2 | OK |
| "lower limit shown for it in Item 6" | I.D; III.4.3 | $250K | OK |
| "verification procedure shown in Item 7" | I.H | Item 7 callback row | OK |
| "reduced retention shown in Item 6" | I.H; III.6.3 | $2,500 | OK |
| "amount shown in Item 6" | I.R | Part 2 row R | OK |
| "Item 8" (continuity; retroactive) | II | Item 8 | OK |
| **"a customer named in Item 6"** | II Key customer | Item 6 has no naming field | **Fails** |
| "Item 1", "Item 2" | II Named insured; Policy period | Items 1, 2 | OK |
| "Item 6 … (up to 90 days)" and "reputational waiting period shown there" | II Reputational harm period | Item 6 N | OK (term conflict, T14) |
| "Items 5 and 6" | II Retention | Items 5, 6 | OK |
| "Item 6 … (or Item 7, if a security credit applies)" | II Waiting period | 8 hours / 4 hours | OK |
| "Section III, part 1" (forensic accounting) | II Business income loss | III.1.8 | OK |
| "covered as described in part 1" | III.4.5 | III.1.8 | OK |
| "Item 4" / "Item 6" | III.1.1 | Items 4, 6 | OK |
| "Item 7" | III.1.5; III.1.6 | Item 7 | OK |
| "Item 7" | III.6.1 | Item 7 | OK |
| "14-day waiting period in Item 6" | III.8.2 | Item 6 N | OK |
| "part 2" | IV intro | IV.2 | OK |
| "(Section III, part 1)" | IV.1 Security lapses | III.1.7 | OK |
| "(see Section V, part 3)" | IV.1 Honest mistakes | V.3 | OK |
| "(exclusion 15)" | IV.1 Cyber terrorism | IV.2.15 | OK |
| "Parts 7 and 8 set out commitments" | V intro | V.7, V.8 | OK target; wording conflicts (T27) |
| "Item 10" | V.1.1 | Item 10 | OK |
| "Item 7 (see Section III, part 1)" | V.4.3 | III.1.5 | OK |
| "state shown in Item 11" | V.7.3; V.8.3 | "Choice of law: Colorado" | Resolves; label narrower than use (T45) |
| "(see Important notices, item 7)" | Item 12 TRIA row | Notice 7 | OK |
| **"Full citations are in the accompanying Decision Rationale"** | Notice 10 | Rationale lists 27 sources, unnumbered; 04 has the 33 numbered | **Misdirects**: should point to 04 |
| **"Plain-English notes"** | Cover; V.11.6 | No such notes in body | **Fails** (T24) |
| "(policy Section V, part 3)" | App intro | V.3 | OK |
| "(Section V, part 3)" | L211 | V.3 | OK |
| "(Section III, part 1; Section IV, part 1)" | L212 | III.1.5 and III.1.7; IV.1 | OK |
| "(Section V, parts 1 and 6)" | L213 | V.1; V.6.2 | OK |
| "(Section V, part 7)" | L215 | V.7.4–7.5 | OK |
| "Section III (parts 1 and 6)" | L295 | III.1.6; III.6.1 | OK |
| "exclusion 6" | L336 | IV.2.6 | OK |
| "Item 7 now says MDR shortens the attack waiting period only" | L294 | Item 7 | OK |
| "Item 4 / Item 5 / Item 6" | L337 | Items 4, 5, 6 | OK |
| "see Item 7" example | L35 | Item 7 | OK |
| #1 "Items 5 and 9; Section III part 7; exclusion 15" | 04 | Largest-retention rule, extended reporting, hammer, war wording | OK |
| #4 "Coverage A; Section III part 7; Section V part 2" | 04 | A; hammer; V.2.3 pre-incident | OK |
| #5 "Section V part 7" | 04 | V.7.4–7.5 | OK |
| #8 "Coverages H, M, N, O; Section III parts 1, 4, 6, 7" | 04 | III.1.8, III.4.2, III.6.1, III.7.2 | OK |
| #12 "Optional Coverage R; Item 7" | 04 | R; Item 7 | OK |
| #19 "Coverage C; III part 3; exclusion 17; notice 6" | 04 | All match | OK |
| #29 "Section V part 1 (legal deadlines first)" | 04 | V.1.5 | OK |
| #33 "Section III part 1" | 04 | III.1.7 | OK |
| **#15 NAIC "Where: Rationale"** | 04 | Never cited in the rationale body | **Fails** |
| **#17 Vouch "Where: Rationale Summary and Section I rationale"** | 04 | The figure is in the Summary and Market benchmark, not Insuring agreements | **Misdirects** |
| #14 Coalition claims report "How we used it" | 04 | Lists 58%, 47% and 72%, which appear nowhere in the package; only 52% is used | Misdescribes use (counted under section 12) |
| #25 Lathrop "Section I; definition of AI agent" | 04 | Rationale credits the AI-agent definition to "Our own design" | Partial |

---

## 9. Check 2: bold terms, defined terms and duplicate names

**Defined but unused.** None. All 52 defined terms (57 counting the pronouns) are used at least once outside their definition. The thinnest are "restoration costs", "computer replacement costs" and "service fraud loss", each used once outside Section II.

**Bold but not defined, where it matters** (the rest are run-in headings):

- "**security failure or system failure**" appears as one bold phrase (I.F; II Restoration costs).
- "**covered as described in part 1**" (III.4.5) is bold emphasis on a cross-reference.
- These are bold labels that behave like terms but aren't in Section II: "**Policy aggregate limit**", "**Pre-incident assistance**", "**One retention per incident**", "**Claim-free reduction**" (Item 5) vs "**Claim-free retention reduction**" (V.6.1), "**Security credits**", "**Verification procedure**", "**Ransomware coinsurance**", "**Known-exploited vulnerabilities**", "**Invoice fraud**", "**Business interruption restoration period**".
- Sentence-length bold emphasis contradicts "Words in bold are defined": "**We bear the burden of proving this exclusion applies.**", "**Never delay a notice that the law requires you to make.**" and "**Think something is wrong? Call us first…**".

**Defined terms used unbolded** (so, under II's own rule, not carrying the defined meaning):

- "personal information" in I.Q and in the wrongful collection definition.
- "system failure" in Item 6 D.
- "waiting period" in Item 6 D, E, N and twice in II Reputational harm period.
- "key customer(s)" in Item 6 S.
- "incident", "claim" and "retention" throughout the Declarations.
- "executive(s)" in Item 8.

**Undefined but operative:** discover; ransomware; extended reporting period; claim-free; critical issue; substantially in place; reputational waiting period; breach coach; panel; incident response team; security credit; annual premium (extended reporting price); "incident retention" (Item 6 G).

**Same concept, two names (across documents):**

| Concept | Names used | Fix |
| --- | --- | --- |
| Restoration window | "Business interruption restoration period" (Item 6) / "period of restoration" (II) / "restoration period" (rationale) | Use the defined term |
| Time deductible | "waiting period" (II, hours) / "14-day waiting period" and "reputational waiting period" (N) / "time deductible" (L101) | Rename N's as "reputational qualifying period" and define it |
| Your first-dollar share | "retention" (policy) / "deductible" (Item 5 heading; L41, L111, L120) | Keep the bridge; say why once |
| Claim-free benefit | "Claim-free reduction" (Item 5) / "Claim-free retention reduction" (V.6.1) / "Vanishing Retention" (L176) | Pick one |
| Service promises | "service standards" (cover, V.7) / "commitments" (V intro) / "binding contract terms" (L162) / "contract promises" (L178) | Align to "service standards" |
| Settlement clause | "Settlement" (III.7.2) / "hammer clause" (L136, L255, L267) | Fine for an insurance reader; one gloss helps |
| Verification | "Callback verification" (Item 7) / "verification procedure" (III.6.1) / "callback procedure" (UW, App 8.2) | Align |
| EDR scope | "EDR on all devices" (Item 7, UW) / "all laptops and servers" (App 4.13) | R1; align |
| Vendor share of claims | "Vendor-caused claims are 14%" (L47) / "Vendors and customers caused 14%" (L73, C6) | Use C6 wording |
| Average ransomware claim | $508K (L44, C1, all firms) / $422K (L13, C2, under $25M) | R1; use $422K for the target market |
| Pre-incident help | "Pre-incident assistance" (policy) / "pre-incident help" (QR) / "pre-claim assistance" (Coalition) | Fine |

---

## 10. Check 3: rationale statements about the policy vs the policy text

33 statements checked: **20 true, 13 untrue, stale or overstated.** The table lists only the failures.

| # | Rationale statement | Policy text | Finding |
| --- | --- | --- | --- |
| 1 | L110 "Executive defined narrowly" | II Executive: "any owner, partner, principal, officer, director, managing member or general counsel, and the person responsible for your information technology or security" | **Untrue**; broader than a "senior executive" definition |
| 2 | L162 "into binding contract terms"; L178 "contract promises" | V.7.1–7.3: "we aim to…" | **Untrue** for response and decision; true only for the advance |
| 3 | L13 "Retentions scale with revenue, from $2,500 to $25,000" | Item 5 shows only $5M–$25M → $10,000 | **Unverifiable** from the policy |
| 4 | L45, L214 "$500K option" | I.R and Item 6: "$500,000, or $1,000,000 with 24/7 managed detection and response" | **Stale / incomplete** |
| 5 | L233 "8 hours, with higher limits available"; L234 "full-limit option" | No such options in Item 6 Part 2 or App 2.4 | **Untrue** (R1) |
| 6 | L294 "new 12-hour system failure wait" | 8 hours | **Stale** (R1) |
| 7 | L296 "Employees are insureds … \| **Open** \| … must carve back" | IV.2.6 already carves back; L336 says "Fixed" | **Stale; contradicts L336** |
| 8 | L293 "Declarations letters, limits and retentions match Sections I–III \| Pass" | O "utility" vs definition; N retention cell vs Retention definition; G's 90-day start; key customer "named in Item 6"; pre-incident missing from III.1 | **Overstated** |
| 9 | Summary #5 "common denial reasons this policy does not use, such as patching lapses" | III.1.7 20% coinsurance for unpatched known-exploited vulnerabilities | **Overstated**; say "except one disclosed coinsurance" |
| 10 | L212 "No security-lapse exclusion; credits survive attacker tampering" | True, but omits III.1.7 | **Incomplete** |
| 11 | L203 and UW "Disclosed gaps can't be used to deny a claim later" | No clause says this. V.3.4 covers scan findings; V.3.2 covers honest mistakes. It holds only by implication (no failure-to-maintain exclusion) | **Unanchored**; cite the mechanism |
| 12 | L83 "P–S optional … \| Coalition includes many of these in its base form" | Cell argues for core, not optional; the parenthetical is a revision note | **Stale** |
| 13 | L194 Data types and record counts set "Breach response and privacy limits" | Coverage B is fixed at $1M; no limit varies with records | **Untrue** (they set price, not limits) |

**True and verified (20):** L41/L120 (one retention); L42 (72-hour help outside the limit, $0 retention); L48/L102 (8 hours, 180 days); L63 (triggers once); L64 (discovery vs claims-made); L93 (computer systems vs dependent systems); L100 (forensic accounting for any first-party loss); L103 (system failure scope); L104 (dependent provider); L126 (five-step extortion); L131 (120 days); L136 (70%); L137 (100% on mixed claims); L153–155 (war); L157 (investment losses carve-back); L166 (90-day window); L176 (claim-free conditions, minus the agreed-timeline alternative); L179 (50%, 10 days, $250K); L223 (23 adjustments: counted, correct); Summary #7 (every starred answer maps).

**Placement and wording issues (not counted above):**
- L184 (Coverage S) and L185 (AI agents) sit in the **Conditions** table. They are an insuring agreement and a definition.
- L5 says "real 2025–26 competitor policies", but At-Bay's form is 08/2023 (#1).
- L38 "Coalition (admitted)" vs #6 "Coalition's newer surplus-lines form": name the specific form.

---

## 11. Check 4: Summary claims vs support below

17 Summary claims checked: **10 supported, 7 unsupported or only partly supported.**

| Summary claim (L9–L27) | Supported below? | Where / gap |
| --- | --- | --- |
| Market is $1M–$50M revenue, 10–250 employees | **No** | No section supports either range; see A3, A4 |
| "Unlike startups … often without a broker or IT team" | **No** | Unsupported; Cedar Ridge has IT staff |
| #1 Corgi is liability-first and modular; suits startups | **Yes** | L327, L319; #11 |
| #1 Losses that hit small businesses most are core; rarer or systemic ones optional | **Partial** | L43, L74, L84; Q doesn't fit "rarer or systemic" |
| #2 $1M covers $180K average, room for $422K ransomware | **Yes** | L39; C2 |
| #2 Retentions $2,500–$25,000 scale with revenue | **Partial** | L40 covers $2,500 and $10K; **$25,000 never supported** |
| #2 Retentions fall with verified security | **Yes** | L229, Item 7 |
| #3 Led the market on honest mistakes, fraud, cash flow | **Yes** | L170, L77, L179 |
| #3 "where small businesses most often get hurt" | **Partial** | L170 "Application errors are the leading denial cause" and L213 "Frequently cited denial trigger": no sources |
| #3 Matched on 70% hammer; cautious on vendor system failure | **Yes** | L136, L267; L74 |
| #4 Plain "means" definitions; rogue employees, personal devices, paper, deepfakes included; infrastructure excluded | **Yes** | L92–L103 (rogue-employee claim weakened by T5) |
| #5 Exclusions open with non-denial reasons "such as patching lapses" | **Partial** | L145–146; contradicted by III.1.7 |
| #5 Modern war wording because legacy wording failed in Merck | **Yes** | L153; #23 |
| #6 Honest mistakes; prejudice-only late notice; firm advance and single accountant | **Yes** | L166, L170, L179–180 |
| #7 NIST CSF 2.0 and CIS v8.1; every starred answer maps | **Yes** | L196; UW |
| Trade-offs: $5,508 between $2,330–$4,048 and Vouch $7,078 | **No** | $2,330–$4,048 appears nowhere below; Vouch unverifiable; **L251 says no median data found** |
| "What I'd do with more time" | **Yes** | L269–271 |

---

## 12. Check 5: source traceability, beyond round 1

1. **The rationale's Sources list has 27 entries; 04 has 33.**
   - Missing from the rationale list: #17 Vouch blog, #21 AICPA Tax Adviser, #27 CIRCIA status, #29 SB 446, #30 Colorado Privacy Act and #33 CISA's known-exploited catalog. #28 is represented only by Goodwin.
   - The rationale cites sources by name, never by 04 number. **Adding "[#n]" to each rationale row would make every "Borrowed from" cell traceable in one step.**
2. **04 #14 (Coalition claims report) lists four statistics; only one is used.** 58% email-fraud share, ransom demands up 47%, and 72% of privacy claims citing CIPA appear nowhere else. Only 52% is used. Meanwhile L219's "privacy claims doubled in the first half of 2026" is not listed (R1). Align 04 to actual use.
3. **04 #15 NAIC** claims use in the Rationale; the rationale body never cites it.
4. **Figures used in the rationale but absent from the ledger** (beyond R1's list):
   - Vouch $62,500 ransomware sublimit (L44).
   - Vouch $25K and At-Bay $1M dependent business interruption (L47).
   - Retention comparators: Vouch/Corgi $10K, At-Bay/Coalition $2,500 (L40).
   - Coalition $50K proof of loss and 25% betterment (L100, L310; C11's text omits both).
   - At-Bay allocation clause (L137).
   - 8-hour waits at Coalition, At-Bay and Vouch (L48, L233).
   - Coalition 60-day late-discovery window (L166).
   - "$100K–$250K sublimits are common" (L214).
   - "Application errors are the leading denial cause" (L170).
   - "Late notice … frequently cited" (L213).
   - "most reported events are handled at no cost" (L177).
   - "Coalition's application asks about … $5,000" (L133).
5. **Sources named in the rationale or application but missing from 04** (additions to R1's ~10): Coalition's application; Coalition Affirmative AI endorsement; Coalition Vanishing Retention (now confirmable [SS]); Coalition liberalization clause; IRS Publication 4557 (App 7.1).
6. **Notice 10 publicly relies on sources 04 marks weak.** It names Lloyd's Y5381 (#22: no link, not re-opened) and the FTC Safeguards Rule (#20: not re-opened). It also calls the Beazley documents "published policy forms", but #7 is an endorsement and #8 is a summary of contract changes.
7. **QR says "22 of 26 audited claims are fully supported"; the ledger shows 21 supported, 4 uncertain and 1 non-factual.** QR isn't for submission, but don't quote "22".
8. **The CS labels are sensible.** The 04 introduction's split (21 checked, 11 secondary, 1 needs a link) is arithmetically correct.

---

## 13. Other correctness fixes found during the audit

These are not "why" questions, but a reviewer would spot them.

1. **Colorado fraud warning is incomplete** (App Part 9). Colorado's required statement (C.R.S. 10-1-128) continues after "…civil damages" with a sentence about insurers or agents who defraud policyholders or claimants being "reported to the Colorado division of insurance within the department of regulatory agencies" [SS]. The sample omits it.
2. **The two coinsurances can stack** (III.1.6 + III.1.7). Add "never more than 20% in total" or state that they stack.
3. **Coverage O "utility"** (T39). Fix the definition or the Declarations.
4. **G's 90-day clock** (N45). Run it from discovery.
5. **Key customer naming field and ">10%" vs "≥10%"** (T20, N80).
6. **III.1 omits pre-incident help** as sitting outside the aggregate (S8).
7. **IV.1 "unpatched" vs III.1.7 "unpatched and unmitigated"** (N69).
8. **III.5.1 restores digital assets "to their condition before the security failure"** but omits system failure, which Coverage F also covers.
9. **Application intro says "Deliberate misstatements can void coverage"**, without V.3.3's "material". Add "material".
10. **Item 5 omits "or on a timeline we agree in writing"** (V.6.1).
11. **Rationale L296 "Open"** vs L336 "Fixed". Delete the stale row.
12. **Back page "Our breach coach answers 24/7"** vs V.7.1 "hotline answered around the clock … aim … within one hour".
13. **Regulatory date** L273 (Sept 26) vs 00 guide (Sept 27).

---

## 14. Sources for the three web checks run today

- Coalition Vanishing Retention (25% after year one, 50% after year two, 100% after year three; under $100M revenue and retentions of $25K or less; critical vulnerabilities fixed within 30 days): [Coalition, How Vanishing Retention Rewards Security-Conscious Policyholders](https://www.coalitioninc.com/blog/cyber-insurance/how-vanishing-retention-rewards-security-conscious-policyholders); [Coalition, Active Cyber Policy FAQ](https://help.coalitioninc.com/hc/en-us/articles/33998071846811-Active-Cyber-Policy-FAQ). Search-snippet level.
- Chubb Neglected Software Exploit endorsement (45-day grace from CVE publication, then a graduated insured share; exact steps inconsistent across snippets): [Chubb, Cyber Insurance Products](https://www.chubb.com/us-en/business-insurance/products/cyber-insurance/cyber-insurance-products.html). Search-snippet level; the underlying endorsement was not opened.
- Colorado fraud warning text, C.R.S. 10-1-128(6)(a): [Coalition Against Insurance Fraud, Colorado Fraud Warning](https://insurancefraud.org/regulations/colorado-fraud-warning-section-10-1-128-6a/); [Justia, C.R.S. 10-1-128](https://law.justia.com/codes/colorado/title-10/general-provisions/article-1/part-1/section-10-1-128). Search-snippet level.

Items labeled **[PR]** (for example ASC 280's 10% threshold, ASC 323's 20% presumption, CIS Safeguard 11.5's quarterly testing, Connecticut's 24-month monitoring rule, and TRIA's application to cyber) are professional knowledge that was **not** web-verified in this pass. Confirm them before putting them in the rationale.
