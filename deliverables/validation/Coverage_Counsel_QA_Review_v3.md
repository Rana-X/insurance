# QA review, version 3: Harborline cyber package

**Reviewed:** September 27, 2026, against the committed text (commit "Remove honest-mistake cancellation and fix the Atlassian source"). **Files:** `Harborline_Policy.md` (P), `Harborline_Application_Cedar_Ridge.md` (A), `Harborline_Decision_Rationale.md` (R), `Submission_Guide.md` (G). The files were not edited. P III.1.9 means policy Section III, part 1.9. The rendered HTML, PDFs and zip match the sources.

---

## 1. Verdict and grades

| Criterion | Grade | One line |
| --- | --- | --- |
| **Clarity** | **8/10** | The Declarations, signposting and cross-references are now clean. But three Section III sentences (III.1.1, III.2.4, III.7.5) still carry the old rules and now contradict the fixed definitions. |
| **Judgment** | **8/10** | The v2 fixes are well aimed and mostly exact. Two fixes stopped at the definition: insider theft can still reach Coverage H, and the D, E and P grants block the new catch-up costs. |
| **Practicality** | **8/10** | The underwriter page, the premium build and the three worked claims are usable as they stand. Claim 2 only pays as described once D's grant is fixed. |
| **Resourcefulness** | **8/10** | Sources are broad, linked and tied to specific wording. A few statements about Corgi, competitors' settlement clauses and LMA 5567 are still unverified or overstated. |

**Bottom line:** the package meets every requirement of the brief and is above the bar. No new Critical findings. Before sending, fix the 2 High findings and sweep the Medium ones. All are wording swaps, about 2–3 hours of work.

**Checks that passed**
- **Cross-references.** Every reference resolves to the right place, including "Section III, part 1.9", "part 6.2 of this Section", "Section V, part 2.3", "part 1.4", "part 5.3", "Items 7 and 11" and "Section V, part 11.6".
- **Premium arithmetic.** $6,120 + $1,530 + $600 + $280 = $8,530; −$853 (10%) gives $7,677. $5,508 and $2,169 are correct. The expected-loss table adds up to 25%, 42% and 61%.
- **Letters and terms.** Coverages A–T are consistent across P, A, R and G. Every bold term is defined, and no definition is orphaned.
- **Removed term.** "Fraudulent instruction" appears only in the private v2 QA review, not in any deliverable or rendered file.

---

## 2. Previous findings: status

| ID | Status | Current wording (brief) and residual issue |
| --- | --- | --- |
| C-1 | **Partly** | Impersonation is restored: "a deliberate deception by someone who is not an **insured** … pretends to be, or to act for …". But an employee is an **insured** only "while acting for you". An employee running a scheme is not acting for you, so is arguably not an insured. **Computer fraud** has no insider limit at all. See N-1. |
| C-2 | Fixed | V.1.2: "These deadlines are firm, except as part 1.4 says." V.1.4: "treated as first made and reported on the date you reported, or on the last day of the **policy period**…". V.5.4: "does not apply to a **claim** covered by other cyber insurance you buy to replace this policy." Item 9 matches. |
| H-1 | **Partly** | The trigger items, Coverage A, the **breach response costs** window, exclusion 2(c) and V.6.1 are all fixed. But III.2.4 still says costs "must be incurred within 12 months after you **discover** the **incident**" (N-4). An early warning is a "suspected" incident, while B needs a "reasonably suspected" one (N-12). |
| H-2 | Fixed | "…it is a **security failure** affecting your **computer systems** under every coverage…" |
| H-3 | Fixed | III.1.9: "Each applies only if we show that the missing control or procedure caused the **incident** or made the loss larger." IV.1 and R Summary 4 match. |
| H-4 | Fixed | R L4: "The outages CPA firms remember were attacks: CCH … and Kronos…"; Atlassian is the example for P. The R §3 P row and the A underwriter row match. |
| H-5 | Fixed (R) | "A $2M limit covers all of this range except its very top." The catch-up cost this relies on is blocked by D's grant (N-2). |
| M-1 | Fixed | V.5.2: "…on 45 days' written notice. An honest mistake is never a reason to cancel (part 3.2)." V.3.2 now runs to expiry, with non-renewal only. V.5.3 has the renewal-change content, and V.5.5 and R §8 match. |
| M-2 | Fixed | III.1.6: "If your backups were not verified when the **incident** happened…". Item 7 matches. |
| M-3 | **Partly** | Item 6 and the D row are fixed, and III.1.1 adds "It does not reduce Coverage P". But III.1.1 still says "under all coverages combined, whichever coverage the loss falls under" (N-3). |
| M-4 | **Partly** | **Dependent systems** now covers systems a provider "has a hosting or cloud provider operate for it". But E, P, exclusion 12, the **system failure** carve-out and the cloud-account deeming rule still say "at", or "within", a **dependent provider's** own systems (N-6). |
| M-5 | Fixed | **System failure** and exclusion 12 are aligned (satellites; "that you do not operate"; the carve-back reaches only failures "within a **dependent provider's** own systems"). |
| M-6 | Fixed as recommended | Computer fraud item 2 is narrowed, and the mailbox sentence is in III.6.2. The wages sentence covers **payment fraud** only (N-11). |
| M-7 | **Partly** | **Extra expense** now "includes catch-up costs incurred up to 30 days after the **period of restoration** ends". But the D, E and P grants pay only extra expense "you incur during the **period of restoration**" (N-2). |
| M-8 | **Partly** | **Damages**, **Regulatory penalties** and J now point to Item 11. III.7.5 still says "only where insurable under the law that applies" (N-5). |
| M-9 | Fixed | Exclusion 2(b): "…unless the Declarations or an endorsement exclude it". |
| M-10 | Fixed | **Incident** now includes "**key customer event** (Coverage S)". The S row says "Key customers are named here when purchased". |
| M-11 | Fixed | The "Other numbers, and why" table and the exclusions row are added. Two numbers are still unexplained (L-10). |
| M-12 | **Partly** | §10, the note on numbers, Corgi and the §9 list are fixed. Still overclaimed: the §2 lead (G, M, N and O map to no row) and the §5 war text ("adds what the models lack" includes the burden of proof and "sovereign state", both already in LMA 5567). See N-9. |
| M-13 | Fixed | A: "…it is the limit for the whole year: a second diversion…". The R §3 row matches. |
| M-14 | Fixed | 7.1, 7.4 and 7.5 now ask for facts, and the Colorado Privacy Act thresholds are split correctly. |

---

## 3. New findings

### Critical
None.

### High

#### N-1 · Insider theft can still reach Coverage H (C-1 is only partly closed)
- **Where:** P II **Payment fraud** (first line), **Insured** item 2, **Computer fraud**; P IV.1 "Rogue insiders"; P V.9.1; R §4 ("theft by the firm's own staff stay with crime insurance").
- **Problem:**
  1. **Payment fraud.** It excludes deception "by someone who is … an **insured**". But **Insured** covers **employees** only "while acting for you", and **Employee** only "while working for you". A bookkeeper who invents a vendor, or who falsely tells a partner that a vendor's bank details changed, is not acting for the firm, so is arguably not an insured.
  2. **Computer fraud.** It covers "someone's unauthorized … use of your **computer systems**" with no insider limit, and the $100K lower limit never applies to it.
  3. **Result.** Fidelity loss reaches H, primary where the firm has no crime policy. That contradicts R §4.
- **Example:** A payroll clerk adds a ghost employee to a client's payroll file, and a partner releases the batch. That is computer fraud item 2, paid in full up to $500K.
- **Replace** the opening of **Payment fraud** with:
  > **Payment fraud** means a deliberate deception by someone who is not your current owner, partner, member, officer, employee or individual independent contractor (whether or not acting for you at the time), and who is not acting in collusion with one, by any means of communication …
- **Add** at the end of **Computer fraud**:
  > It does not include a transfer or alteration made by, or in collusion with, your current owner, partner, member, officer, employee or individual independent contractor. Theft by your own people belongs to crime or fidelity insurance.
- **Replace** IV.1 "Rogue insiders" with:
  > **Rogue insiders.** Attacks by **employees** or **executives** acting against your interests are covered for you, except theft of money or securities by your own people, which belongs to crime or fidelity insurance. Exclusion 4 applies to the insider personally, and to you only as it says.
- **Alternative:** if insider computer fraud should stay covered, keep the policy and change R §4 to: "It still requires impersonation, so commercial disputes stay with crime insurance. Staff theft is covered only where it runs through the firm's systems as computer fraud, and then in excess of any crime policy."

#### N-2 · The D, E and P grants block the catch-up costs that M-7 added and that R's claim 2 relies on
- **Where:** P I.D, I.E and I.P ("**extra expense** you incur during the **period of restoration**") against P II **Extra expense** ("includes catch-up costs incurred up to 30 days after the **period of restoration** ends"). Also R §3 "Other numbers" ("plus 30 days of catch-up costs"), R §6 **Extra expense** row, and R §8 claim 2 ("Overtime to catch up for 30 days after restoration counts as extra expense").
- **Problem:** The insuring agreement limits payment to costs incurred during the period of restoration, which excludes exactly the post-restoration catch-up costs. An insurer will cite the grant. At best the insured wins on ambiguity after a dispute. This is the sample firm's main business interruption cost.
- **Replace I.D (first sentence) with:**
  > **D. Business Interruption.** When a **security failure** or **system failure** interrupts your **computer systems** for longer than the **waiting period**, we will pay the **business income loss** you incur during the **period of restoration** and your **extra expense**, including catch-up costs incurred up to 30 days after the **period of restoration** ends.
- **Replace I.E with:**
  > **E. Dependent Business Interruption.** When a **security failure** affecting the **dependent systems** you rely on interrupts them for longer than the **waiting period**, we will pay the **business income loss** you incur during the **period of restoration** and your **extra expense**, including catch-up costs incurred up to 30 days after the **period of restoration** ends.
- **Replace I.P with:**
  > **P. Dependent System Failure Business Interruption.** When a **system failure** affecting the **dependent systems** you rely on interrupts them for longer than the **waiting period** shown for Coverage P in Item 6, we will pay the **business income loss** you incur during the **period of restoration** and your **extra expense**, including catch-up costs incurred up to 30 days after the **period of restoration** ends.

  (The E and P wording also fixes N-6.)

### Medium

#### N-3 · III.1.1 still defines "applies across coverages" as "all coverages" (M-3 residual)
- **Where:** P III.1.1, second sentence, against the Item 6 heading ("under the coverages it names, combined").
- **Problem:** The operative Section III sentence keeps the *CiCi*-style reading the Item 6 fix removed. The later "It does not reduce Coverage P" treats the symptom, not the rule.
- **Replace with:**
  > A limit marked "applies across coverages" is the most we will pay for that kind of loss under the coverages it names, combined, whichever of them the loss falls under.

#### N-4 · III.2.4 still starts the breach-cost window at discovery (H-1 residual)
- **Where:** P III.2.4, against the **Breach response costs** lead-in.
- **Problem:** For an early warning that finds nothing, there is never a discovery, so III.2.4's window never opens. That is the same failure H-1 fixed in the definition.
- **Replace with:**
  > 4. **Breach response costs** must be incurred within 12 months after you **discover** the **incident** or, for one that is only suspected, within 12 months after you report it to us.

#### N-5 · III.7.5 keeps a second insurability test (M-8 residual)
- **Where:** P III.7.5 ("only where insurable under the law that applies").
- **Replace with:**
  > 5. **Penalties and punitive damages.** We pay **regulatory penalties** only where insurable, as that definition explains, and punitive damages only as the definition of **damages** allows.

#### N-6 · The fourth-party fix stops at the definition (M-4 residual)
- **Where:**
  - P I.E and I.P ("at a **dependent provider**");
  - the last paragraph of **Computer systems** ("an attack on a **dependent provider's** systems");
  - **System failure** ("that the **dependent provider** does not operate");
  - exclusion 12's carve-back ("within a **dependent provider's** own systems");
  - **Public internet infrastructure** ("a **dependent provider's** own systems").
- **Problem:** The tax platform's cloud host is not a **dependent provider**, because Cedar Ridge has no agreement with it. So a fault or attack at the host is not "at a **dependent provider**", even though the host's systems are now **dependent systems**. R §2 and §6 present hosting as covered.
- **Example:** An attack on the hyperscaler takes the tax platform down for 3 days. The insurer argues that E needs a security failure "at a dependent provider", and the host is not one.
- **Replace:**
  - I.E and I.P: as in N-2.
  - **Computer systems**, last paragraph, first clause:
    > If an attack on **dependent systems** gives someone unauthorized access to your **cloud accounts**, …
  - **System failure**:
    > …(for Coverage P, that neither the **dependent provider** nor its hosting or cloud provider operates).
  - Exclusion 12's carve-back:
    > …or, under Coverages E and P, to a **security failure** or **system failure** within **dependent systems**.
  - **Public internet infrastructure**, last sentence:
    > It does not include **dependent systems**, including the name servers a **dependent provider** or its hosting provider runs for its own services.

#### N-7 · Item 6 shows two amounts in the R limit cell, and the application offers only $500,000
- **Where:** P Item 6 R row ("$500,000 (replaces $250,000 for Coverage H); $1,000,000 also available"); P I.R ("becomes the amount shown for Coverage R in Item 6"); A 2.4 and the underwriter row; R §3 ("$500K or $1M option (R)") and §7 ($520).
- **Problem:**
  - **Operative text.** The Declarations are operative (V.11.6), and I.R points to "the amount shown", but two amounts are shown. An insured can argue for $1M.
  - **Application.** The application gives no $1M choice and never says why $500K was chosen over $1M. The rationale is consistent with a $1M option; the application is not.
- **Replace:**
  - Item 6 R row, limit cell:
    > $500,000 (replaces $250,000 for Coverage H)
  - Item 6 R row, plain-English cell:
    > Raises the Coverage H limit to $500,000 or $1,000,000
  - A 2.4:
    > ☒ R. Increased fraud limit (☒ $500,000 ☐ $1,000,000)
  - A underwriter row, append:
    > $1,000,000 was offered for $520; $500,000 covers two diversions of the largest batch.

#### N-8 · Draft history and process notes a hiring manager will notice (R)
- **Where and replacement:**
  - §4 heading "Why payment fraud was rewritten." →
    > **Why payment fraud is written this way.**
  - §4 "My first draft had four of these gaps:" →
    > Narrower wordings leave four gaps:

    Also change the bullets to the present tense ("can be deceived", "holds").
  - §4 "The new **payment fraud** definition closes all four." →
    > Harborline's **payment fraud** definition closes all four.
  - §6 **Cloud accounts** row, "An earlier draft let a Microsoft 365 mailbox be read as both. That ambiguity cuts both ways…" →
    > Without a clear boundary, a Microsoft 365 mailbox could be read as both, and that ambiguity cuts both ways on the most common claims.
  - §7 "I also removed traps. The application no longer asks the insured to state legal conclusions (for example, whether it falls under a privacy statute); it asks for facts." →
    > The application avoids traps: it asks for facts, not legal conclusions (for example, how many Colorado consumers' data the firm processes, not whether a privacy statute applies).
  - Summary 2 "not the $1M I started with" →
    > rather than the $1M base
  - §4 M/N/O row "(now including AI-service charges)" →
    > (including AI-service charges)
  - §10 "I checked the draft three ways:" →
    > I checked the package three ways:

#### N-9 · Overclaims that survive (R)
- **§2 lead.** "every core coverage except media liability (L) maps to a row" is untrue: G, M, N and O appear in no §2 row. Replace with:
  > Every loss path has a coverage. Media liability (L), the smaller core coverages (G, M, N and O) and the options are explained in part 4.
- **§5 war.** "It adds what the models lack for small insureds:" lists the burden of proof and "sovereign state". Per the legal check (#46), LMA 5567 already has both. Replace that sentence and its three bullets with:
  > It takes the insurer's burden of proof and the "sovereign state" meaning from LMA 5567 and states both in plain words, adding that "state" never means a U.S. state. For small insureds it adds one thing the models lack: continued help while attribution is pending, with no repayment.
- **§9 "broader than the forms I compared".** The first bullet claims any-channel fraud reaching the bank and client accounts, but §4 credits HSB (bank deception) and CFC (client accounts) with those features. Replace the first bullet with:
  > any-channel payment fraud that reaches the bank and client accounts in one trigger (HSB and CFC each cover part of this);
- **§10 item 1.** "every bold term … every Declarations number" is contradicted by N-2 to N-6. Replace with:
  > **Consistency.** I cross-checked the bold terms against the definitions, and the Declarations numbers against the wording.
- **Summary 1.** "…are always covered" ignores limits and exclusions. Replace with:
  > **The losses that hit small businesses most are core coverages.**
- **§4.** "Fraud coverage is where U.S. courts disagree most often" is an unsourced superlative. Replace with:
  > Fraud coverage is one of the most litigated areas of cyber and crime insurance.

#### N-10 · Corgi facts are not what the market check verified
- **Where:** R §1 "Fit with Corgi" ("$2M aggregate, $1M per event and a $10K retention"); R §3 ("Corgi's structure of $1M per event").
- **Problem:** The market check (#6) recorded corgi.insure as "up to $1M per claim / $2M aggregate". "Per event" and "$10K retention" are unverified. This is the first thing a Corgi reader will check.
- **Replace:**
  - §1:
    > Corgi's cyber page describes its startup policy as offering up to $1M per claim and $2M in the aggregate.
  - §3:
    > I also considered Corgi's structure of $1M per claim with a $2M aggregate.
  - Add the $10K retention only after confirming it on the page on submission day.

#### N-11 · Payroll diversion through a hacked account is not treated as the firm's loss
- **Where:** P II **Funds transfer loss**, last sentence ("because **payment fraud** diverted them").
- **Problem:** The most common payroll diversion is an attacker changing direct-deposit details in the payroll platform. That is **computer fraud** item 2 (a payee record in a **cloud account**). The personal-funds exclusion then lets the insurer call the re-paid wages the employee's money.
- **Replace with:**
  > Wages or other amounts you must pay again because **payment fraud** or **computer fraud** diverted them are your loss, not an **employee's** personal funds.

#### N-12 · An early warning is "suspected" for B, but B needs "reasonably suspected"
- **Where:** P I.A ("An **early warning** is always a suspected **incident** for Coverages A and B"); I.B ("actual or reasonably suspected"); trigger item 1; R §6 ("They shouldn't have to argue about whether an FBI call was 'reasonable suspicion'").
- **Problem:** The rationale's promise is not delivered for B: the insurer can still argue that a thin warning was not "reasonably" suspected.
- **Replace** in I.A:
  > An **early warning** is always a reasonably suspected **incident** for Coverages A and B.

### Low

| ID | Where | Problem | Exact replacement |
| --- | --- | --- | --- |
| L-1 | P Item 7, payment-procedure row | This operative Declarations text states the $100K rule with no causation test | "Coverage H at its full limit. Without the procedure or training, a $100,000 limit can apply, but only as Section III, part 6.2 allows" |
| L-2 | R §8 claim 2; P "If something happens" step 1; R Summary 5 | "The first seven days of response cost nothing": Coverage A is capped at $25,000 per incident. "Advances 50% of the estimated loss": V.7.4 says the business interruption loss "to date" | Claim 2: "Coverage A pays the hotline, breach coach and first-response forensics for the first seven days, up to $25,000, with no retention." Also: "…advances 50% of its estimate of the business interruption loss to date." Step 1: "…the first 7 days of expert help cost you nothing, up to $25,000." |
| L-3 | R §3 "Other numbers", 70% row; R §9 "narrower" list | "The market middle (Coalition and Beazley BBR 5.0 use 70%…)" is in neither fact check. It also conflicts with §9, which lists 70% as *narrower* than the compared forms | "\| 70% after a refused settlement \| III.7.2 \| Shares the cost of a refused settlement 70/30: firmer than At-Bay's 80/20 (AB-CYB-001.2), softer than a full cap \|" |
| L-4 | P II **Extortion expenses** against V.2.2 | Items 2 and 3 "need" consent for a non-panel vendor, but V.2.2 reimburses unconsented costs unless we were harmed (the same issue fixed for **claim expenses**) | "Item 1 always requires our prior written consent. Items 2 and 3 need it only if you use a vendor outside our panel, and even then Section V, part 2.2 applies:" |
| L-5 | P V.5.2 against V.3.3 | Cancellation needs only that "you knowingly made a false statement". Rescission needs an **executive** and a *material* misstatement, so the milder remedy has the looser test | "…or because an **executive** knowingly made a material false statement in your **application**, on 45 days' written notice." |
| L-6 | P III.1.7, last sentence | "This is the only way patching affects your coverage", yet V.6.1 ties the claim-free reduction to fixing critical issues within 30 days | "This is the only way patching can reduce what we pay for a loss. Section V, part 6.1 explains how fixing critical issues affects the claim-free reduction." |
| L-7 | P IV exclusion 3 | It omits **wrongful collection**, unlike trigger item 1, V.4.2 and V.5.4 | "Any **incident**, **media wrongful act** or **wrongful collection** that first happened before the **retroactive date**." |
| L-8 | R §3 lost-income row | "Fees lost when clients leave" falls after restoration, so it is not **business income loss**; only N pays it, up to $100K | "…overtime and temporary staff to catch up for up to 30 days after restoration, extension work, and fees lost during the outage" |
| L-9 | R §9 | "Part 1.9's causation rule" is ambiguous (R also has a part 1). "The firm 50% advance delivers cash speed for attacks": V.7.4 also covers P | "The causation rule in Section III, part 1.9 takes the fair part." Also: "…delivers cash speed for covered outages." |
| L-10 | R §3 "Other numbers" | The $2,500 fast-report H retention (72 hours) and N's 14-day wait are not explained anywhere | Add: "\| $2,500 H retention if reported within 72 hours \| Item 6; III.6.3 \| The first 24–72 hours decide whether a bank recall works, so fast reporting earns a lower retention \|" and "\| 14-day wait, then up to 90 days \| N \| Filters out a short news cycle; 90 days captures the client losses that follow a public breach \|" |
| L-11 | R retention table, last row | At $25M–$50M revenue, $25,000 is 0.125–0.25 of a day | "An eighth to a quarter of a day" |
| L-12 | R "A note on numbers"; Sources | The note promises sources "with links", but the At-Bay report, Y5381 and the TRIA guidance have none. The At-Bay line also omits $145K, $221K and $285K | "…come from the published sources listed at the end, with links where the source is public." At-Bay line: "source of the $145K, $180K, $208K, $221K, $285K, $422K, $508K and 14% figures" |
| L-13 | R §8 advance row | It omits V.7.4's second cap | "…up to 25% of the aggregate or the coverage's own limit, whichever is lower" |
| L-14 | R §5 | "Every restriction names one of five reasons", but the last row names three. The "Known problems" row misses the new exceptions | "Each restriction is tied to one or more of five reasons:" Also: "…Unexploited weaknesses, anything disclosed (unless endorsed out) and early warnings cleared before the continuity date are carved out" |
| L-15 | A 7.1 | "Run payroll … for individuals", but Cedar Ridge runs payroll for 40 *business* clients | Answer: "☒ Yes ☐ No. Tax preparation for about 2,400 individuals; payroll for 40 business clients. Our written information security plan follows IRS Publication 4557 and the FTC Safeguards Rule" |
| L-16 | A 8.2; A underwriter backup row | 8.2 says "deny a claim" (elsewhere "deny or reduce"). The backup row says "To keep the credit", but it is coinsurance, not a credit | "…can't be used to deny or reduce a claim". Backup row: "No ransomware coinsurance while backups stay verified. Retest by June 12, 2027 to stay free of it" |
| L-17 | P Item 6, optional table | It still has 6 columns, and the "Purchased?" column duplicates the limit column (v2 L-12 not done) | Drop "Purchased?"; list P and R first, marked "(purchased)" |
| L-18 | `Harborline_Corgi_Package.zip` | The zip bundles `2_Keep_Private_Working_Files` (the v2 QA review, the change log and the fact checks) with the send folder. Sending the zip itself would expose internal process notes | Build a send-only zip from `1_Send_to_Corgi`, and keep the private folder out of any file that leaves the machine |

---

## 4. Three claims, start to finish: trace against the wording

| Claim | Pays as described? | Notes |
| --- | --- | --- |
| 1. Spoofed partner email, $210K client batch | **Yes** | **Payment fraud** (a non-insured impersonates an **executive**); a **client account** item 2; **funds transfer loss** limited to what is owed to the client. $2,500 retention (reported within 72 hours) under the $500K R limit. The staffer's missed callback does not trigger the $100K limit (III.6.2). |
| 2. Ransomware, 6 days, restored from backups | **Partly** | Catch-up overtime is blocked by D's grant (N-2). "Cost nothing" overstates Coverage A's $25K cap (L-2). The advance is 50% of the business interruption loss *to date*. The retention and the absence of coinsurance are correct. |
| 3. Vendor bad update, 3 days | **Yes**, for lost income | **System failure** at a **dependent provider** on online terms; P's 24-hour wait; $250K, outside the D/F cap (III.1.1). Any post-restoration catch-up has the same N-2 problem. The CCH counterfactual under E ($500K, 8 hours) is correct. |

---

## 5. Brief compliance and presentation

- **Brief:** met.
  - The policy has a cover, notices and disclaimers, Declarations (Items 1–12), insuring agreements, definitions, coverage details, exclusions, conditions and a claims page.
  - The application is filled in, with an underwriter page.
  - The rationale covers limits, inclusions and exclusions, the definitions structure and trade-offs.
  - There are more than 30 external references, most of them linked.
- **Draft history and process notes:** N-8. Also L-18 (the private files in the zip).
- **Overclaims:** N-9, N-10 and L-3.

---

## 6. Top 5 edits

1. **Close the insider route into H (N-1).** Change the payment fraud lead-in, add the computer fraud insider sentence and adjust IV.1 "Rogue insiders". Or change R §4 to match the policy.
2. **Rewrite the D, E and P grants (N-2 plus N-6).** Catch-up costs then actually pay, and E and P reach the vendor's cloud host.
3. **Sweep the three stale Section III sentences (N-3, N-4, N-5) and the B "reasonably suspected" gap (N-12).** Four one-line swaps.
4. **Make the Item 6 R limit cell a single amount and offer $1M on the application (N-7).** Add the wages-via-computer-fraud fix (N-11).
5. **Clean the rationale (N-8, N-9, N-10).** Remove the draft-history lines, correct the §2 lead, the §5 war and §9 claims, and match Corgi's page ("$1M per claim / $2M aggregate").
