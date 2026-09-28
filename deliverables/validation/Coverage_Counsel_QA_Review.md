# QA review: Harborline cyber package (policy, application, rationale)

**Reviewed:** September 27, 2026. **Files:** `deliverables/Harborline_Policy.md` (P), `Harborline_Application_Cedar_Ridge.md` (A), `Harborline_Decision_Rationale.md` (R). The files were not edited. Section references use the policy's own numbering (for example, P III.1.9 means Section III, part 1.9).

**Scope note.** The source-by-source fact checks are in `verify/legal_claims.md` and `verify/market_claims.md`. This review includes those facts only where they change a finding (M-1, M-12, M-14, L-10, L-11, L-14).

---

## 1. Verdict

| Criterion | Grade | One line |
| --- | --- | --- |
| **Clarity** | **7/10** | Plain English, bold terms and good signposting. But the policy runs about 12,700 words with 20 coverages, and dense exception-on-exception clauses (III.1.3, III.1.9, the last paragraph of **computer systems**) plus 5–6-column tables will tire a reviewer reading the PDF. |
| **Judgment** | **7/10** | The design is well reasoned: a causation rule, the cloud boundary, a fraud rewrite tied to case law, a limit sized to the severe event. But the redraft opened three unintended grants (fraud with no impersonation element, a post-expiry notice tail, pre-inception early warnings). The rationale also backs P with attack examples and says "$2M covers it" of a range that reaches $2.2M. |
| **Practicality** | **8/10** | The underwriter page, the premium build, the service standards and the incident-first conditions are usable as they stand. It loses points for the cancellation conflict, for no catch-up cost cover for the sample firm, and for having no worked claim example. |
| **Resourcefulness** | **8/10** | Case law is mapped to specific wording choices, alongside Y5381, UK Insurance Act s11 and *CiCi*. It loses points for a few misattributed or unsourced facts (Coalition $116K, CFC, SB 690 scope), sources that are issued policies posted by third parties, and a claimed "legal review". |

**Bottom line:** the package meets every requirement of the brief and is above the bar for a take-home. Fix the 2 Critical and 5 High findings before submitting (about half a day). All but H-4 and H-5 are single-paragraph wording swaps.

---

## 2. Must-fix findings

### Critical

#### C-1 · Payment fraud lost its impersonation element (regression)
- **Where:** P II **Payment fraud**. Also affects H, Item 6 H and R §4 "Why payment fraud was rewritten".
- **Problem:** The old **fraudulent instruction** required an instruction that "falsely appears to come from" a trusted party. The new definition covers *any* "deliberate deception ... by anyone acting against your interests" that leads to a payment. That includes ordinary commercial fraud and theft by your own staff, and a Colorado court will read it as written.
- **Example:**
  - A bookkeeper sets up a fake vendor and deceives a partner into approving $180K over six months. That is "deception by anyone acting against your interests", so Coverage H pays up to $500K. This is fidelity cover the product never underwrote.
  - A real software reseller knowingly bills for licenses it never delivers. That is also covered.
  - V.9.1 ("H applies in excess of any crime or fidelity insurance") shows the drafter expected an overlap, but not this one.
- **Replace the definition with:**
  > **Payment fraud** means a deliberate deception by someone who is not an **insured**, by any means of communication (including email, text, messaging app, letter, phone or video call, and synthetic or deepfake audio or video), in which that person pretends to be, or to act for, you, an **executive**, **employee**, client, vendor, **financial institution** or other person you deal with, or falsely claims that genuine payment or bank details have changed, and that:
  > 1. leads you, or a **financial institution** that holds your accounts or **client accounts**, to transfer money or securities, or to change payment or bank details that are then used for a transfer; and
  > 2. causes a loss to you, or a loss you must make good to a client.
  >
  > In this definition, "you" means the **named insured** acting through anyone authorized to make, approve or change its payments, including an **executive**, **employee**, individual independent contractor, or an **AI agent** acting within its authority.
- **Add to R §4, after "It uses 'resulting from'":** "It still requires impersonation. Commercial disputes and theft by the firm's own staff stay with crime insurance (OP)."

#### C-2 · "Reports lock in coverage" (V.1.4) conflicts with the firm claim deadline, the automatic ERP and the renewal
- **Where:** P V.1.2, V.1.4, V.5.4; Item 9; exclusion 2 (last clause).
- **Problems:**
  1. **Deemed date outside the policy.** A report made after expiry, which V.1.4 allows "within the time in part 1.2", deems the later claim "first made on the date you reported". That date falls outside the **policy period**, so trigger item 3 fails. Yet V.1.4 also says the claim "is covered only under this policy".
  2. **The firm deadline can defeat every locked-in claim.** V.1.2 requires each **claim** to be reported within 90 days after expiry and calls this "firm". Under *Craft*, a firm date is enforced without prejudice. A class action that arrives in month 20 cannot meet it, and V.1.4 never says the claim is treated as *reported* on the lock-in date.
  3. **Free discovery tail.** V.1.4 is not limited to incidents **discovered** during the period, so an incident first found 60 days after expiry can be locked in.
  4. **Circular clauses.** V.5.4 says the automatic ERP "does not apply if other insurance you have covers the claim". On a Harborline renewal, the renewal points back through exclusion 2 ("reported under an earlier policy that covers it"). Each policy says the other one covers.
  5. **Ambiguous deadline.** V.1.2 says "90 days after the policy period ends, **or** before the end of any extended reporting period". That does not say which applies, and gives no window after an optional ERP ends.
- **Example:** Ransomware with data theft is discovered October 10, 2027. It is reported November 20, 2027, 36 days after expiry. A class action is filed March 2028.
  - The deemed date is November 20, 2027, which is outside the period.
  - The automatic ERP is displaced by the Harborline renewal, and the renewal excludes the claim under exclusion 2.
  - V.1.2's deadline expired January 13, 2028.
  - Possibly nothing responds, the exact failure the redraft was meant to fix (W-06).
- **Replace V.1.2 with:**
  > 2. **Deadline for claims.** You must report a **claim** no later than 90 days after the **policy period** ends. For a **claim** first made during an optional extended reporting period, the deadline is 60 days after that period ends. These deadlines are firm, except as part 1.4 says.
- **Replace V.1.4 with:**
  > 4. **Reports lock in coverage.** If, during the **policy period** or within 90 days after it ends, you report an **incident** you **discovered** during the **policy period**, or facts you learned of during the **policy period** that could reasonably lead to a **claim**, every later **claim** arising from it, or from the same or **related** facts, is treated as first made and reported on the date you reported, or on the last day of the **policy period** if you reported after it ended. It is covered only under this policy, whenever it is actually made. You do not need to say who might sue. Send us each such **claim** as soon as practicable after it is made; the deadline in part 1.2 does not apply to it.
- **Replace V.5.4 with:**
  > 4. **Automatic extended reporting.** If this policy is cancelled or not renewed, then for 60 days after it ends, **claims** first made against you during those 60 days, arising from **incidents**, **media wrongful acts** or **wrongful collection** that first happened before this policy ended, are treated as made on the last day of the **policy period**. This does not apply to a **claim** covered by other cyber insurance you buy to replace this policy.
- **Item 9, Automatic row:** "60 days after the policy ends, if it is cancelled or not renewed (Section V, part 5.4)".

### High

#### H-1 · Early warning: an FBI call that finds nothing fails the trigger, and a pre-inception warning escapes exclusion 2
- **Where:** P I "When coverage applies" items 1–2; I.A (last two sentences); II **Breach response costs** lead-in; IV exclusion 2; V.6.1 vs V.6.2.
- **Problems:**
  1. **Trigger failure.** Trigger item 2 requires every first-party coverage, including A and B, to have an incident "**discovered**" during the period. Coverage A says an early warning "alone does not mean you have **discovered** an **incident**". An FBI call that finds nothing therefore fails the trigger on a literal reading.
  2. **B's window never opens.** B's costs must be incurred "within 12 months after you **discover**". With no discovery, the window never starts, so B's promise to pay "the cost of finding out that none happened" pays nothing.
  3. **The exclusion 2 sentence only works as a grant.** "Does not count as knowledge under exclusion 2" only has effect for warnings received *before* the continuity date, because exclusion 2 ignores later knowledge. It lets a firm with a known compromise buy cover. A warning received between signing the application and inception is also not a "misstatement in the application" (V.3.2–3.3), so neither rescission nor exclusion 2 reaches it.
  4. **Claim-free status conflict.** V.6.2 says an early-warning investigation "is not treated as a claim". V.6.1 says any payment beyond the retention, other than Coverage A, ends a claim-free year. A B payment for the same investigation falls between the two.
  5. **Minor mismatch.** Coverage A covers an "actual or suspected" incident; trigger item 1 says "reasonably suspected".
- **Example:** In September 2026, before inception, the FBI tells Cedar Ridge its credentials are for sale. No one updates the application. In November 2026 a breach traced to those credentials costs $400K. Exclusion 2 cannot be used, because the early-warning sentence protects it, and rescission is unavailable.
- **Replace:**
  - Trigger item 1, second sentence:
    > For Coverage A, an actual or suspected **incident**, and for Coverage B, an actual or reasonably suspected **incident**, meets this requirement, even if an investigation later shows that none happened.
  - Trigger item 2:
    > 2. For coverages for your own losses (A–H, M–P, S and T), you first **discover** the **incident** during the **policy period**. For Coverages A and B, it is enough that you received an **early warning**, or reported a suspected **incident**, during the **policy period**.
  - Coverage A, last two sentences:
    > An **early warning** is always a suspected **incident** for Coverages A and B. By itself, it does not mean you have **discovered** an **incident** for any other coverage.
  - **Breach response costs** lead-in:
    > ...reasonable costs you incur within 12 months after you **discover** a **security failure** or **privacy event** or, for one that is only suspected, within 12 months after you report it to us.
  - Exclusion 2, second sentence:
    > A circumstance does not include: (a) a vulnerability, missing patch or other security weakness that, as far as any **executive** knew, had not been exploited; (b) anything disclosed in your **application**, unless the Declarations or an endorsement exclude it; or (c) an **early warning** that an investigation completed before the **continuity date** found was not an **incident**.
  - V.6.1, definition of claim-free year:
    > A claim-free year is a policy year in which we paid nothing beyond your **retention**, apart from Coverage A, pre-incident assistance, and the cost of investigating an **early warning** or suspected **incident** that turned out not to be an **incident**.

#### H-2 · The cloud-account deeming rule (last paragraph of **computer systems**) creates gaps in D, I, N and O and misroutes provider suspensions
- **Where:** P II **Computer systems**, last paragraph; also D, E and P.
- **Problems:**
  1. **The short list invites a narrow reading.** A vendor-side attack that reaches your **cloud accounts** is treated as a **security failure** "for Coverages B, C, F and H" only. By *expressio unius*, the insurer can argue that D, I, M, N and O do not respond to the same event. That is wrong, because unauthorized access to a **cloud account** is already a **security failure** on your **computer systems**, so the list either does nothing or does harm.
  2. **Provider suspensions fall in a gap.** "Any interruption caused by the provider's service being unavailable is covered under Coverage E" misroutes the case where the provider suspends *your* tenant because *your* account was compromised. E needs a security failure *at the provider*; D is barred. Neither responds.
  3. **Grant language for an option.** "Is covered under ... Coverage P" in a definition reads as a grant of P even when P was not bought.
- **Example:** A vendor-side token theft (scenario 5) lets an attacker wipe SharePoint and lock the tenant for 4 days. The insurer argues D is not on the list, and E does not apply because Microsoft's service stayed up. That means no business interruption cover on a $2M policy.
- **Replace the last paragraph with:**
  > It does not include **dependent systems**. If an attack on a **dependent provider's** systems gives someone unauthorized access to your **cloud accounts**, or damages, encrypts or exposes data in them, it is a **security failure** affecting your **computer systems** under every coverage. An interruption caused only because a **dependent provider's** service is unavailable to you, other than one caused by a **security failure** in your own **computer systems**, falls under Coverage E (or, for a **system failure**, Coverage P if purchased), not Coverage D.

#### H-3 · The causation rule (III.1.9) says "to the extent", which reads as proportional, and "only three terms" is untrue
- **Where:** P III.1.9; IV.1 "Security lapses"; R Summary item 4 and §5 "One rule for security".
- **Problems:**
  1. **A proportional reading.** "Each applies only *to the extent* that the missing control ... caused the incident or made the loss larger" reads as proportional. The 20% would then apply only to the extra loss the gap caused, and a limit such as the $100K fraud floor cannot be applied "to the extent" at all. R says "only if the gap mattered", which is a threshold test. A court will take the proportional reading.
  2. **"Only three" is untrue.** Losing a security credit (III.1.5) raises the retention without any causation test. So does the claim-free reduction's patch condition (V.6.1). IV.1, which V.11.6 makes operative, repeats "only three" without the credit caveat.
  3. **Confusing references.** "Parts 6 and 7 above, and the lower Coverage H limit in part 6 of this Section" refers to two different "part 6"s.
- **Example:** A firm without verified backups suffers $400K of encryption loss. The insurer shows the gap added $60K. Under "to the extent", the insured pays 20% × $60K = $12K, not 20% × $400K = $80K.
- **Replace III.1.9 with:**
  > 9. **How your security can affect what we pay.** Only three terms can reduce what we pay because of your security practices: the ransomware coinsurance (part 1.6), the known-exploited-vulnerability coinsurance (part 1.7) and the lower Coverage H limit (part 6.2 of this Section). Each applies only if we show that the missing control or procedure caused the **incident** or made the loss larger. If we show that, the term applies as its part describes. No exclusion or condition reduces what we pay because of your security practices. Separately, your **retention**, **waiting period** and claim-free reduction depend on the security credits and conditions in part 1.5 and Section V, part 6. They are part of your price. What you told us in your **application** is dealt with in Section V, part 3.
- **IV.1 "Security lapses", replace the last sentence with:**
  > Only three disclosed terms can reduce what we pay because of your security practices, and each applies only if the gap mattered to the loss (Section III, part 1.9). Losing a security credit can raise your **retention** (Section III, part 1.5).
- **R Summary item 4:**
  > **Security affects price, not whether you're covered.** Only three disclosed terms can cut a payment for security reasons, and each applies only if the gap mattered to the loss. Losing a credit can raise the retention.

#### H-4 · The rationale backs Coverage P with two cyberattacks (CCH 2019, Kronos 2021)
- **Where:** R §2 L4 row; R §3 sublimit row for P; A underwriter row "(6.1, 4.24)".
- **Problem:** CCH (malware) and Kronos (ransomware) were attacks. Harborline pays them under **core** Coverage E, not optional P, which covers non-malicious outages only. This undercuts the one option Cedar Ridge bought. A reader who knows cyber will notice at once.
- **Replace the R §2 L4 row with:**
  > | L4 | **Vendor or cloud outage** | Vendors and customers caused 14% of At-Bay's 2025 claims, averaging $145K. Multi-day outages of shared platforms are rare but severe | Attacks on platforms, such as CCH (May 2019, malware, several days, with an IRS filing extension) and Kronos (December 2021, ransomware, weeks), fall under Coverage E. Non-malicious failures, such as Atlassian (April 2022, a faulty maintenance script took some customers offline for up to two weeks) and AWS (October 2025), fall under Coverage P | E (attacks); P (non-malicious, optional) |
- **Note:** keep the AWS example only if M-4 is fixed by extending **dependent systems** to hosting providers; otherwise drop it.
- **Replace the R §3 P row with:**
  > | Dependent system failure (P, optional) | $250K, 24-hour wait | The most systemic trigger: one vendor bug or cloud fault hits every customer at once, so it is optional, with a longer wait. It targets multi-day failures like Atlassian's in 2022, not short blips. Attacks on platforms (CCH 2019, Kronos 2021) are already covered by E |
- **Replace the A underwriter row with:**
  > | Tax and payroll platforms would stop the business; 1-day tolerance in tax season (6.1, 4.24) | Attacks on these platforms are covered by core Coverage E ($500,000). Coverage P recommended and purchased for non-malicious outages: $250,000, 24-hour waiting period |

#### H-5 · The headline limit: "$2M covers it" of a $0.9M–$2.2M range, and deferrable tax-season work is counted as lost income
- **Where:** R §3 severe-event table and the paragraph after it; R §9 parametric row; P II **Extra expense** (fixed in M-7).
- **Problems:**
  1. **Arithmetic.** The severe total reaches $2.2M, and "A $2M limit covers it" is not true of the top of the range.
  2. **Lost income.** The table counts "about 10 business days" of tax-season revenue ($250K–$450K) as lost income. §9 says the same firm's downtime is "mostly deferrable", and the policy's business income formula would pay little of it. The real cost is catch-up work after restoration, which the wording doesn't cover (M-7).
  3. **Misattributed figure.** Per the market check, $116K is Coalition's all-policyholder average, not an under-$25M figure.
- **Replace the R §3 lost-income row with:**
  > | Lost income and extra expense (about 10 business days in season, after the 8-hour wait): overtime and temporary staff to catch up, extension work, and fees lost when clients leave | $250K–$450K |
- **Add under the R §3 table:**
  > Tax-season work is mostly delayed rather than lost, so most of this line is the cost of catching up, which the policy pays as **extra expense**.
- **Replace the paragraph after the table with:**
  > A $1M limit covers the typical claim easily: Coalition's average claim across all policyholders was $116K, and At-Bay's for firms under $25M was $180K. But a $1M limit can run out in exactly the event that would threaten the business. A $2M limit covers all of this range except its very top, which assumes the worst case on every line at once. $3M stays available where a client contract requires it.

### Medium

#### M-1 · Cancellation: V.3.2 conflicts with V.5.2's "only", and "fraud" is not a Colorado ground
- **Where:** P V.3.2, V.5.2, V.5.3; R §8 cancellation row.
- **Problem:**
  - V.3.2 lets the insurer cancel on 60 days' notice when it "would not have issued this policy at all". V.5.2 says the insurer "may cancel **only** for non-payment ... or fraud", so a court will strike the V.3.2 right.
  - C.R.S. 10-4-109.7 lists closed grounds: non-payment (with reasons), a false statement knowingly made in the application, or a substantial change in risk. "Fraud" is broader than that list.
  - V.5.3 omits the content that C.R.S. 10-4-110.5 requires in a renewal-change notice (reasons, renewal terms, premium).
- **Replace V.5.2 with:**
  > 2. **We may cancel only:** for non-payment of premium, on 10 days' written notice stating the reason; because a statement in your **application** was knowingly false, on 45 days' written notice; or as part 3.2 of this Section allows, where the correct answer shows a substantially different risk, on 60 days' written notice. State law may require longer notice.
- **V.5.3, second sentence:**
  > If we offer to renew with a higher premium or reduced coverage, we will tell you in writing at least 45 days before this policy ends, giving the reasons, each change and the renewal premium.
- **Change V.5.5 and R §8 to match.** Replace "non-payment or fraud" with "non-payment or a knowingly false application".

#### M-2 · Ransomware coinsurance is keyed to what Item 7 showed at issue, not to the backups at the time of loss
- **Where:** P III.1.6; Item 7; A underwriter row "(4.21, 4.23)".
- **Problem:** "If Item 7 shows that you did not earn the backup credit" fixes the test at issue. Item 7 will always show "Yes" for Cedar Ridge, so a lapsed restore test does nothing, even though the underwriter page says "To keep the credit, retest by June 12, 2027". The reverse also fails: a firm without the credit at issue that later adds verified backups still pays the coinsurance.
- **Replace the first sentence of III.1.6 with:**
  > If your backups were not verified when the **incident** happened, you pay 20% of the **restoration costs**, **business income loss** and **extra expense** under Coverages D and F that result from **ransomware** encrypting or locking your **computer systems**, after the **retention**.
- **Item 7, backup row, last cell:** "No ransomware coinsurance while backups stay verified (restore tested within the last 12 months; Section III, part 1.6)".

#### M-3 · "Applies across coverages" can be read to fold P into the $250K system failure cap
- **Where:** P Item 6 heading and D row; III.1.1.
- **Problem:** The Item 6 heading defines the label as "the most we will pay for that kind of loss under **all coverages** combined". P loss is the same kind of loss: business income caused by a **system failure**. III.1.1 says D and F only. This is the *CiCi* problem the label was meant to prevent.
- **Replace the Item 6 heading sentence with:**
  > A limit marked "applies across coverages" is the most we will pay for that kind of loss under the coverages it names, combined (Section III, part 1.1).
- **D row limit cell:** "Attacks: $2,000,000. **System failure: $250,000 for D and F combined** (Coverage P has its own limit)".
- **Add to the end of III.1.1:**
  > It does not reduce Coverage P, which has its own limit.

#### M-4 · Fourth-party gap: a SaaS vendor's cloud host is not a **dependent system**
- **Where:** P II **Dependent systems**; R §6 "Public internet infrastructure" row (the AWS example).
- **Problem:** **Dependent systems** are those "a **dependent provider** operates". Cedar Ridge's tax platform runs on a hyperscaler Cedar Ridge has no contract with. An AWS fault like October 2025's is not a failure of systems the platform "operates", so P and E can be denied. Yet R cites AWS as the case the definition was built for.
- **Replace (if P and E should reach hosting, the recommended choice; price it):**
  > **Dependent systems** means the computer systems a **dependent provider** operates, or has a hosting or cloud provider operate for it, to provide services to you, other than your **cloud accounts**.
- **Otherwise,** state the exclusion in the definition and delete the AWS sentence from R §6.

#### M-5 · Exclusion 12 and the **system failure** definition don't match
- **Where:** P IV exclusion 12; II **System failure**.
- **Problems:**
  - Exclusion 12 lists "satellites" and limits itself to infrastructure "you do not operate". **System failure** does neither.
  - Exclusion 12's carve-back ("under Coverages E and P, to an event at a **dependent provider's** own systems") invites the argument that a vendor data-center power failure is an event at its own systems and so is covered under P. That is the accumulation risk exclusion 12 exists to stop.
- **Replace the last sentence of the system failure definition's exclusions with:**
  > It does not include planned downtime, or a failure of electricity, water, gas or other utilities, telecommunications, satellites or **public internet infrastructure** that you do not operate (for Coverage P, that the **dependent provider** does not operate).
- **Replace the exclusion 12 carve-back with:**
  > This does not apply to loss from a **security failure** affecting your **computer systems**, or, under Coverages E and P, to a **security failure** or **system failure** within a **dependent provider's** own systems.

#### M-6 · The overlap of payment fraud and computer fraud decides whether the $100K floor applies; payroll diversion is unclear
- **Where:** P II **Computer fraud** item 2; III.6.2; **Funds transfer loss**.
- **Problems:**
  1. **Most BEC can escape the floor.** Most BEC runs through a compromised mailbox. The insured will call the altered email a "payment instruction" altered through "your **computer systems**" (computer fraud item 2), where the $100K floor "never applies". That defeats the moral-hazard purpose R §3 gives the floor.
  2. **Payroll diversion.** "Does not include personal funds of **employees**" lets the insurer argue that a diverted paycheck was the employee's money. Payroll diversion is a common small-business fraud.
- **Replace computer fraud item 2 with:**
  > 2. alter a payment batch, payroll file, or payee or bank record held in your **computer systems**, which you then approve or release without knowing it was altered.
- **Add to III.6.2:**
  > A request sent from, or through, a compromised mailbox or account is still **payment fraud** for this part.
- **Add to the end of Funds transfer loss:**
  > Wages or other amounts you must pay again because **payment fraud** diverted them are your loss, not an **employee's** personal funds.
- **Alternatively,** if the author prefers the insured-friendly result, say so in R §3 instead.

#### M-7 · Business interruption pays nothing for catch-up work after systems return, which is the sample firm's main cost
- **Where:** P II **Extra expense**; **Period of restoration**.
- **Problem:** Extra expense must be incurred to avoid business income loss, and only during the period of restoration. A CPA firm in March loses little income, because the work is deferred. Its cost is overtime and temporary staff *after* restoration, which falls outside both limbs (scenario 3).
- **Replace the definition with:**
  > **Extra expense** means reasonable additional costs you incur to avoid or reduce **business income loss**, or to catch up on work the interruption delayed, such as renting equipment, paying overtime or temporary staff, hiring outside IT staff or moving work to other systems. It includes catch-up costs incurred up to 30 days after the **period of restoration** ends. Costs to avoid **business income loss** are covered up to the loss they avoid.

#### M-8 · **Damages** hardcodes Colorado into the one-size form, with two different tests for what is insurable
- **Where:** P II **Damages**; **Regulatory penalties**; III.7.5; R §5 PP row.
- **Problem:**
  - "Colorado law, shown in Item 11, does not" sits in Section II, which the cover promises is identical for every business. A policy whose Item 11 names another state would contradict itself.
  - **Damages** uses "the law that governs this policy" while penalties use "the law that applies", so two different insurability tests apply. Per the legal check, "multiplied" damages are not settled in Colorado.
- **Replace the second sentence of Damages with:**
  > Punitive, exemplary or multiplied damages are included only where the law shown in Item 11 of the Declarations allows them to be insured.
- **In Regulatory penalties and J,** replace "the law that applies" with "the law shown in Item 11 of the Declarations, or of the place where the **regulatory proceeding** is brought, whichever allows it".
- **Put the Colorado statement in HIC-CY-CO** and change R §5 to "the Colorado endorsement says so plainly".

#### M-9 · Exclusion 2(b) covers known losses the applicant disclosed
- **Where:** P IV exclusion 2(b).
- **Problem:** "A circumstance does not include ... anything disclosed in your **application**." An applicant who writes "ransomware last month, notices going out" gets that loss covered unless the underwriter remembers to endorse it out.
- **Fix:** Covered by the H-1 replacement of exclusion 2: "(b) anything disclosed in your **application**, unless the Declarations or an endorsement exclude it".

#### M-10 · Coverage S can never be triggered
- **Where:** P II **Incident**; I trigger items 1–2; Item 6 S row.
- **Problem:** A **key customer event** is not an **incident**, but trigger items 1–2 require one. Item 6 has no place to name the key customer. (W-38, W-39 and W-12 from the earlier review; this one is still open.) The **incident** definition also relies on an undefined "invoice fraud covered under Coverage H", which is redundant because H.2 requires a **security failure**.
- **Replace the Incident definition with:**
  > **Incident** means a **security failure**, **system failure**, **privacy event**, **cyber extortion**, **payment fraud**, **computer fraud**, **adverse publication** or, if purchased, an **impersonation event** (Coverage T) or **key customer event** (Coverage S). **Incidents** arising from the same or **related** facts are one **incident**, occurring when the first one occurred.
- **Item 6 S row, "What it pays for" cell,** add: "Key customer(s) named: ____".

#### M-11 · The rationale does not explain every number, and "Every restriction names one of five reasons" overclaims
- **Where:** R §3 and §5.
- **Problem:**
  - Many key numbers have no reason anywhere: the 8-hour wait, 20% coinsurance, 45 days for a KEV, 180 days, K $250K, G $25K, the $100K floor, the $5,000 threshold, 70% on refused settlements, ERP 75%/125%, the $50K proof-of-loss help, the $2,500 pre-incident help.
  - The §5 table omits exclusions 3, 5, 6, 9, 13, 14, 16, 18 and 19.
- **Add at the end of R §3** (the reasons are drafts; the author should confirm them):
  > **Other numbers, and why**
  >
  > | Number | Where | Why |
  > | --- | --- | --- |
  > | 8-hour wait (4 with MDR) | D, E | Filters out blips a business absorbs; in line with the market. MDR shortens outages, so it earns a shorter wait |
  > | 180-day period of restoration | D, E, P | Covers a rebuild plus a full tax season; longer outages are rare with tested backups |
  > | 20% coinsurance | III.1.6, 1.7 | Large enough to reward the control, small enough that the business still gets 80% of a serious loss |
  > | 45 days to fix a notified KEV | III.1.7 | About three times CISA's two-week deadline for federal agencies, so a firm relying on an outside IT provider has time |
  > | $100K floor; $5,000 threshold | III.6 | The floor still pays a typical small diversion. The threshold catches almost every BEC wire without forcing calls on routine payments |
  > | K $250K; G $25K | Item 6 | Card assessments for a small merchant using a hosted page rarely reach six figures. $25K buys a year of MFA, EDR and backup upgrades for a 60-person firm |
  > | 70% after a refused settlement | III.7.2 | Shares the cost of refusing 70/30: firmer than At-Bay's 80/20, softer than a full cap |
  > | ERP 60 days automatic; 12 or 24 months at 75% or 125% | Item 9 | Typical market pricing for 1- and 2-year tails |
  > | $50K proof-of-loss help; $2,500 pre-incident help | III.1.8, V.2.3 | A typical forensic-accountant engagement; about 5–8 hours of breach-coach advice |
- **Add a row to the R §5 table:**
  > | Contract liability, claims between insureds, unsolicited communications, natural disasters, government orders, nuclear and pollution, investment losses, ill-gotten profits, the retroactive date | OP / PP / MH | Standard market exclusions. Each has a carve-back where a cyber event is the real cause (for example, contract duties to protect data, or spam sent by an attacker) |

#### M-12 · Overclaims a hiring manager will test
- **Where and replacement:**
  - **R §10 item 2** ("A Colorado and U.S. legal review of each clause") suggests a lawyer's sign-off. Replace with:
    > **Law.** I checked each clause against Colorado and federal law and the cases listed below (notice, cancellation, punitive damages, fraud warnings, terrorism disclosure, rebating, and fraud and sublimit case law). A licensed Colorado coverage lawyer should review it before filing.
  - **R §10 item 1:**
    > **Consistency.** I cross-checked every bold term against the definitions, and every Declarations number against the wording.
  - **R note on numbers** ("checked at the level noted there": no levels are noted). Replace with:
    > ...come from the published sources listed at the end.
  - **R §1 "Fit with Corgi"** ("I kept that two-number way of thinking about limits"): the policy has one aggregate. Replace with:
    > I considered that two-number structure but chose a single $2M aggregate for Cedar Ridge, because its danger is one severe event, not two average ones (part 3).
  - **R §9 "broader than the forms I compared"** lists employee privacy claims, which R §4 says Coalition already covers, plus rogue insiders and paper records, which are common in the market. Replace the list with:
    > any-channel payment fraud that reaches the bank and client accounts; a firm, not discretionary, business interruption advance; "paying a ransom is never required"; a causation test for every security-based reduction; seven days of first response outside the limit.
  - **R §5 war exclusion** ("adds what those lack": per the legal check, LMA 5567 already has attribution, the burden of proof and "sovereign state"). Replace the sentence and its four bullets with:
    > Harborline follows Beazley's war and cyber war exclusion and the Lloyd's Y5381 criteria, and takes attribution and the insurer's burden of proof from LMA 5567. For small insureds it adds continued help while attribution is pending, and says expressly that "state" never means a U.S. state.
  - **R §2 lead** ("Every coverage in the policy maps to a row"): L, Q, S and T don't. Replace with:
    > Every loss path has a coverage, and every core coverage but media liability (L) maps to a row. L and the options are explained in part 4.

#### M-13 · The reason given for Coverage R doesn't hold
- **Where:** A underwriter row "(5.4, 5.5)"; R §3 payment fraud row.
- **Problem:** "One diverted batch plus recovery costs fits within the limit" is already true of the core $250K limit ($210K batch). The real reason is that the limit is annual: a second diversion, or one compromise that redirects several clients' batches, would exhaust it.
- **Replace the A row result with:**
  > Coverage R recommended and purchased: fraud limit $500,000. The core $250,000 would pay one diverted batch, but it is the limit for the whole year: a second diversion, or one compromise that redirects several clients' batches, would exhaust it.
- **Replace the second sentence of the R §3 row with:**
  > Firms that move client money need more: one diversion of Cedar Ridge's largest batch (about $210K) nearly uses the $250K annual limit, so it buys $500K.

#### M-14 · The application still asks for legal conclusions, contrary to R §7
- **Where:** A 7.1, 7.4, 7.5 (R §7 says "it asks for facts").
- **Replace:**
  - 7.1:
    > | 7.1 | Do you prepare tax returns, or provide bookkeeping, payroll or other financial services, for individuals? | ☒ Yes ☐ No. Our written information security plan follows IRS Publication 4557 |
  - 7.4:
    > | 7.4 | If you accept payment cards, which PCI self-assessment questionnaire does your processor ask you to complete? | SAQ A (hosted payment page; see 3.10) |
  - 7.5: correct the Colorado Privacy Act second threshold, per the legal check. The threshold is 25,000 consumers *plus* revenue or discounts from selling personal data. Suggested question:
    > Do you process the personal data of 100,000 or more Colorado residents a year, or of 25,000 or more while earning revenue from selling personal data?

### Low

| ID | Where | Problem | Exact fix |
| --- | --- | --- | --- |
| L-1 | P Item 7 MDR row; A underwriter "(4.17)"; III.4.3; III.1.3; III.8.2 | Item 7 cuts the wait "for attacks". III.4.3 cuts it for "Coverages D and E", which includes system failure. Section III also hardcodes Declarations numbers (8/4/24 hours; "14-day"), which breaks the general form | Item 7 and A: "cut the waiting period for Coverages D and E from 8 to 4 hours". III.4.3: "3. **Waiting periods.** The **waiting period** starts when the interruption begins. Item 6 shows it for each coverage, and Item 7 shows any reduction you earned." III.1.3 and III.8.2: replace "the 14-day period" and "the 14-day waiting period" with "the reputational harm waiting period in Item 6" |
| L-2 | P II **Retention**; **Reputational harm period** | The Retention definition says the **waiting period** applies to reputational harm, but **waiting period** means business interruption hours. "Reputational waiting period" is undefined | Retention, last sentence: "For business interruption, the **waiting period** applies instead; for reputational harm, the reputational harm waiting period in Item 6 applies instead." |
| L-3 | P III.1.8; Item 4; V.7.4 | The $50K proof-of-loss help is not on the Declarations. The advance cap (25% of aggregate, $500K) exceeds P's $250K limit | Item 4, add row: "\| **Proof-of-loss help** \| Up to $50,000 per **incident** for a forensic accountant (Section III, part 1.8). Part of the aggregate limit, not of the coverage it supports \|". V.7.4: "...up to 25% of the policy aggregate limit or the limit of the coverage that applies, whichever is lower..." |
| L-4 | P II **Extortion expenses** vs V.2.2 | "If incurred with our prior written consent" covers panel negotiators, but V.2.2 says panel vendors need no consent | "**Extortion expenses** means the following. Item 1 requires our prior written consent; items 2 and 3 need it only if you use a vendor outside our panel:" |
| L-5 | P V.4.2 | Run-off after acquisition omits **wrongful collection** (Q) | "...but only for **incidents**, **media wrongful acts** and **wrongful collection** before the change." |
| L-6 | P III.7.2 | "Our payment for that **claim** is capped" but then pays 70% more, which is not a cap | "If you do, we pay the settlement amount and the **claim expenses** incurred up to your refusal, and 70% of further **damages** and **claim expenses**. You pay the rest." |
| L-7 | P Declarations notice vs V.11.6 | The notice says "This page summarizes your coverage", but V.11.6 makes the Declarations operative wording | "**How to read this page.** Items 1–12 are part of your policy. The 'plain English' column in Item 6 is a summary; the policy wording controls. Words in bold are defined in Section II." |
| L-8 | P IV exclusion 13 | "Other physical events" can be read to include theft or loss of a device (security failure item 4) and physical break-ins | "Fire, flood, earthquake, windstorm, explosion or other natural or physical catastrophe. This does not apply to theft or loss of a device, or to physical access used to carry out a **security failure**." |
| L-9 | P II **Claim expenses** vs V.2.2 | The definition requires costs "incurred by us or with our consent", but V.2.2 reimburses costs incurred without consent unless we were harmed | Claim expenses: "...incurred by us, with our consent, or as Section V, part 2.2 allows..." |
| L-10 | R, various | (a) "$500K or $1M option (R)" but the Declarations and application offer only $500K. (b) Retention table "A quarter to a whole day" for under $2.5M is really about 0.25–0.6 of a day at $1M+ revenue. (c) CFC cited with no source. (d) SB 690 described as limiting wiretap suits; per the legal check it ends pen-register/trap-and-trace suits (Penal Code 638.51). (e) "Paid-claim frequency" is Coalition's *claims* frequency. (f) Draft-history phrases ("The dollar cap is unchanged"; "it was undefined"). (g) "Coalition's breach response services (72 hours)" could not be verified | (a) Item 6 R: "$500,000 or $1,000,000"; or R: "$500K option (R)". (b) "A quarter to two-thirds of a day". (c) Add the CFC March 2025 cybercrime URL (in market_claims.md). (d) "California SB 690 (ends private pen-register and trap-and-trace suits over website tracking) \| ... \| Wiretap (section 631) claims remain, so Coverage Q stays". (e) "Claim frequency (Coalition: 1.21% under $25M; I assume higher for firms holding tax data)". (f) "The $25K cap per incident keeps the extra time cheap"; "Triggers, notice and exclusions all turn on this word; leaving it undefined invites a fight over which policy year responds". (g) Cite the issued form and page, or drop "(72 hours)" |
| L-11 | A | (a) The pre-issue scan scans internet-facing systems, yet its only finding is on the isolated internal print server. (b) "Deny a claim" vs V.3.4's "deny or reduce". (c) "About 20 minutes" for about 75 questions plus evidence. (d) "7-year retention, following IRS guidance": the IRS general period is 3 years | (a) "...one medium finding (an outdated TLS setting on our website's web server)". (b) "We won't later use anything that scan showed to deny or reduce a claim." (c) "about 30–45 minutes, plus time to gather the evidence". (d) 3.6: "Records kept 7 years under our retention policy (longer than the IRS's general 3-year period), then securely deleted" |
| L-12 | P formatting | "## Cover page" and "## Back page" print as draft labels. The Declarations are split into three H2s ("Items 1–5", "Item 6", "Items 7–12") that sit alongside Sections I–V in the PDF bookmarks. Heading punctuation is mixed ("Item 6." vs "Items 1–5:"). Section II has no subtitle. The optional coverages table has 6 columns; the H row's plain-English cell is about 45 words | Delete the "## Cover page" heading (the H1 already titles the page). Rename "## Back page..." to "## If something happens: six steps". Make "## Declarations" the only H2, with "### Item 1. Named insured" to "### Item 12. Forms and endorsements" under it, and delete the three grouping H2s. "## Section II. Definitions: what the bold words mean". Drop the "Purchased?" column by listing purchased options first, marked "(purchased)". H plain English: "Money you or your bank are tricked or hacked into sending, including from client accounts you run, and customer payments diverted by fake invoices sent from your hacked systems" |
| L-13 | P Important notices item 10 | A filed policy that cites competitors' forms in its notices looks like a draft | Retitle: "**Specimen drafting note (not part of a filed form).**" Keep the text |
| L-14 | P Important notices item 8; A fraud warning | Per the legal check, one comma differs from C.R.S. 10-1-128(6)(a) | "...denial of insurance, and civil damages." |

---

## 3. Scenario traces (Cedar Ridge, current wording)

All limits are per policy period and within the $2M aggregate unless marked. Coverage A (7 days, $25K per incident, $75K per period, no retention, outside the aggregate) responds to every scenario, because each is an actual or suspected **incident**.

**1. A spoofed partner email diverts a $210K client payroll batch.**
- **Route:** **payment fraud**. Deception by email; "you" acts through the payroll staffer; the money moves from a **client account** (item 2: a client's own account Cedar Ridge is authorized to operate).
- **Pays:** H.1 **funds transfer loss**, limited to what Cedar Ridge is legally obligated to repay the client (or repays with consent), plus recovery costs.
- **Limit:** $500,000 (R), shared with H.2. The $100K floor does not apply: the procedure and training are verified, and a staffer's failure to call back does not reduce the limit (III.6.2).
- **Retention:** $7,500, or $2,500 if reported to Harborline within 72 hours of an executive learning of it (the only dollar retention for H).
- **Does not respond:** I, because a pure spoof is not a **security failure** or **privacy event**; the client's consequential claims go to the accountants' professional liability policy. G, because G needs a **security failure**.
- **Other terms:** H is excess of any crime policy. Recoveries go first to the retention.
- **Watch:** if the "spoof" actually came from a hacked mailbox, it is also **computer fraud** and a **security failure** (B pays the mailbox review), and the floor argument disappears (M-6). As drafted, H would also pay if the "partner" were a real insider running a scheme (C-1).

**2. An impostor phones the bank, and the bank wires money out.**
- **Route:** **payment fraud**; the deceived party is a **financial institution** holding Cedar Ridge's accounts.
- **Pays:** H.1.
- **Limit:** $500,000. The $100K floor never applies when a bank was deceived.
- **Retention:** $7,500, or $2,500 if reported within 72 hours.
- **Other terms:**
  - III.6.4 requires prompt written notice to the bank to preserve the UCC Article 4A refund right (the bank bears the loss if it did not follow the agreed security procedure).
  - Harborline pays without waiting for the bank, then subrogates (V.10).
  - If the account was a client's, only the amount owed to the client is covered.
- **Result:** covered as intended. The earlier gap (W-02) is closed.

**3. Ransomware in March 2027: restored from backups, 6 days down.**
- **Route:** **security failure** plus **cyber extortion**.
- **Pays:**
  - A (first 7 days).
  - B: forensics beyond A. If data was stolen, notice to about 31,000 people, monitoring, and IRS IP PIN help.
  - C: negotiation, investigation and sanctions costs even though they don't pay (with consent).
  - D: business income loss and extra expense for about 5.7 days after the 8-hour wait, at the $2,000,000 attack limit, adjusted for tax season (III.4.1). A 50% advance arrives within 10 business days.
  - F: restoration and malware removal, $2,000,000.
  - G: up to $25,000 of upgrades within 90 days.
  - M if devices are bricked ($100,000).
  - N if the press covers it (14-day wait, $100,000).
- **Retention:** one $7,500 for the incident; D uses the waiting period instead.
- **Coinsurance:** none. The June 12, 2026 restore test is under 12 months old, there is an immutable and an offline copy, and they restored from backups anyway (III.1.6). The KEV rule bites only if a notified vulnerability left unfixed for more than 45 days was the way in.
- **Gaps:**
  - Catch-up overtime after restoration is not covered, and deferred tax work produces little "lost" income (M-7).
  - An attack after June 12, 2027 without a retest still carries no coinsurance, because the test is keyed to Item 7 (M-2).
  - Later lawsuits and regulator inquiries are safe only after the C-2 fix.

**4. A tax-platform vendor bug causes a 3-day outage.**
- **Route:** a non-malicious **system failure** at a **dependent provider** (standard online terms are enough, III.4.4). The provider's service is unavailable, so the **computer systems** definition routes the loss to P, not D.
- **Pays:** P (purchased): business income loss and extra expense after the 24-hour wait, so about 48 hours.
- **Limit:** $250,000.
- **Retention:** no dollar retention.
- **Other terms:** seasonality adjustment; proof of loss within 120 days; forensic accountant up to $50K; advance available.
- **Without P:** nothing pays. It is not a **security failure**, so E does not apply, and D is routed away.
- **Risks:**
  - The insurer may argue the $250K system-failure cap "applies across coverages" and so includes P (M-3).
  - If the root cause sat with the platform's cloud host, **dependent systems** may not reach it (M-4).
  - Catch-up costs are not covered (M-7).

**5. Microsoft 365 tenant compromised through a vendor-side token theft.**
- **Route:** an attack on a **dependent provider** that gives access to Cedar Ridge's **cloud account**. It is deemed a **security failure** on Cedar Ridge's **computer systems** "for Coverages B, C, F and H". It is also a **privacy event** (personal information in the mailboxes, "including while a **dependent provider** holds it").
- **Pays:**
  - B ($2,000,000): forensics, mailbox review, notices.
  - I and J through the privacy event ($2,000,000 each).
  - H ($500,000) if the tenant was used to send fake invoices (H.2) or divert payments (computer fraud through a cloud account).
  - F for restoration.
  - N if the press covers it.
  - E ($500,000, 8-hour wait) only if Microsoft's own service goes down.
- **Retention:** one $7,500.
- **Gap:** D and O are not on the deeming list. If the attacker locks or wipes the tenant, or Cedar Ridge takes it offline, the insurer can argue there is no business interruption cover (H-2).
- **War exclusion:** state-linked espionage is not excluded unless the operation had a "major detrimental impact" on a state. The tenant is treated as located in Denver, and the insurer bears the burden of proof. Subrogation against Microsoft is limited by its terms.

**6. An FBI early-warning call that finds nothing.**
- **Intended result:**
  - A: 7 days, $25,000, no retention.
  - B: pays "the cost of finding out that none happened", above a $7,500 retention.
  - Not a claim for renewal pricing (V.6.2).
- **As drafted:**
  - Trigger item 2 requires the incident to be "**discovered**" in the period, and Coverage A says an early warning alone is not discovery, so the literal trigger fails.
  - B's 12-month cost window runs from discovery, so it never opens.
  - A B payment ends the claim-free year under V.6.1 despite V.6.2.
  - The exclusion 2 sentence matters only for warnings received *before* inception, where it works as a grant.
- **Result:** paid in practice (Harborline runs A), but the wording needs the H-1 fix.

---

## 4. Nice-to-have improvements

1. **Add "Three claims, start to finish"** (half a page, at the end of R §8 or on the policy's back page), using traces 1, 3 and 4 above: what the firm did, what was paid, under which coverage, and what the firm paid. This is the most direct answer to the brief's "show how it works in practice".
2. **Cut the policy by about 15%.** Merge IV.1 into III.1.9 and the Section I promises, since they repeat each other. Cut the second copy of the claims-made and defense notices from the Declarations. Shorten 15.1 of the war exclusion.
3. **Punitive damages and penalties.** Consider a most-favorable-jurisdiction clause (the market norm, and what the previous draft had), or say in R §5 why Harborline chose not to.
4. **Show prices for the options** (Q, S, T, full-limit system failure) on the Declarations or in R §7. R says the full-limit option is "available and priced", but no price appears anywhere.
5. **Explain the 25% increased-limit factor.** The second $1M costs $1,530 against $60–150 of expected loss (a 4–10% loss ratio). Add one line on risk load and parameter uncertainty.
6. **Sources.**
   - Replace the two issued policies hosted by third-party insureds (ASTRO America, MWV Homeless Alliance) with carrier specimen forms, or label them "issued policy, publicly posted by the insured".
   - Add URLs for At-Bay's InsurSec report and Lloyd's Y5381.
   - Re-check the SB 690 outcome after September 30.
7. **Corgi facts.** Re-read every Corgi statement against the press release and corgi.insure. A Corgi reader will check them first.
8. **Eligibility.** Add a one-line eligibility statement to the cover or the application ("U.S. businesses with $1M–$50M revenue; not the classes in question 1.13").
9. **Item 6 T row.** "N/A (offered at $25,000)" is unusual on a Declarations page. Use "Not purchased" and move the offer terms to the application.
