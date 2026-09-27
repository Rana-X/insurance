# 10. International and US inspiration: what to borrow for Harborline

Prepared September 27, 2026. This file merges four research reports into one prioritized list:
- `10a_uk_lloyds.md`: UK and Lloyd's market
- `10b_europe.md`: Germany, France, Switzerland, the Netherlands and EU rules
- `10c_apac_canada.md`: Australia, New Zealand, Japan, Singapore, India and Canada
- `10d_us_novel.md`: standout US forms and new product structures

The question was: which of the best small-business cyber policies around the world have ideas Harborline should take, and how would each one read in a US admitted policy under Colorado law?

**Evidence caveat (read first).**
- **Nothing was opened at source.** Every insurer, regulator and court host the four agents tried was blocked from this environment. Evidence is search-result level ("snippet"), a note in `catalog/`, or background knowledge. Each source report labels every item.
- **No carrier wording is quoted.** Every block marked **Harborline draft** is new drafting that shows the mechanism. **It is a draft. Rewrite it in your own words before it goes into the package.** The brief asks for your work, not an AI output.
- **Numbers are placeholders.** Every dollar amount, day count and percentage in the drafts is judgment, not market data. Each still needs pricing.

---

## 1. Bottom line

1. **Harborline is already at or ahead of the best SMB forms on most headline features** (section 2). The firm 50% BI advance, the insurer-bears-the-burden war attribution rule, the AI-agent trigger and written claims-service standards did not turn up anywhere else in these searches.
2. **The best ideas abroad are not new coverage lines. They fall into four groups:**
   - **Fairness rules**, so a small firm doesn't lose cover over something that didn't matter:
     - the UK Insurance Act's "relevance" rule and the German and Swiss causation rules;
     - the UK industry position that holding insurance never obliges anyone to pay a ransom;
     - warning and cure before any duty is enforced.
   - **Small, cheap coverages for professional firms:**
     - court attendance;
     - theft from client accounts the firm operates;
     - executives' personal funds;
     - deepfake and impersonation response.
   - **Structural mechanics:**
     - one retention per year;
     - a limits map with caps that say they apply across coverages;
     - related incidents tied to the earliest period;
     - an external alert as an automatic trigger.
   - **Transparency:** a one-page "policy at a glance", a renewal "what changed" table and a legal-deadlines card.
3. **Take ten now (Tier A, section 3).** They are small and mostly filing-safe, and seven of them finish fixes already on the list in `README.md` section 5. Together they add roughly one and a half pages to the policy.
4. **Name three optional covers as "what I'd test next" (Tier C, section 5):**
   - a **Fast Downtime Payment** (parametric BI), now live in the US through AIG and Parametrix;
   - **one limit reinstatement**, the bounded version of Brit's per-event limits and CFC's unlimited reinstatements;
   - **AI regulatory defense**.

   Each one answers a reviewer's likely "did you consider…?".
5. **Don't copy the statutory machinery** (section 6): Germany's fault-degree reductions, France's 72-hour complaint forfeiture, Québec's defense-outside-limits rule, and GDPR, NIS2 and DORA terms. Take the principle behind each one and leave the mechanism.

---

## 2. Where Harborline already matches or beats the best (don't re-copy)

| Harborline feature | Best comparable abroad or in the US | Verdict |
| --- | --- | --- |
| Firm 50% BI advance within 10 business days (V.7.4) | Coalition "Lifeline" cash advance (discretionary, Aug 2026); CFC interim BI payments (2025) | **Ahead.** Firm, not discretionary |
| War exclusion: the insurer must prove attribution, with a bystander promise | GDV AVB Cyber 2024 (a broader state-attack exclusion); LMA 5564–5567 | **Ahead.** Insured-friendlier than the German model |
| Defined **AI agent**, with hijacked and erring agents treated separately (after T2-5) | Beazley and CFC affirmative AI (Sept 2026); Emergence CEP-005.1 (AI-caused events) | **Ahead on the definition.** Affirmative AI itself is now standard (T4-4) |
| Written claims-service standards, with interest | Nothing comparable found. Closest: CFC's interactive wording; Chubb Australia's 1-hour incident-response contact | **Ahead** |
| Coverage A: 72 hours, $25K, outside the aggregate, $0 retention | CFC nil-deductible incident response (2024–25); Coalition Active Cyber Policy Canada, $0 with Coalition IR (Mar 2026); Chubb Australia's 48-hour emergency costs | **At par** |
| Scan-based credits and the known-exploited-vulnerability (KEV) coinsurance | Chubb Neglected Software Exploit; Dattak and Stoïk scans (France) | **At par or ahead.** The KEV rule is objective and notice-based |
| Betterment (Coverage G) | Travelers Canada CyberRisk | At par |
| Key customer and one forensic accountant | Coalition Enhanced Business Recovery (Aug 2026) | At par |
| Claim-free (vanishing) retention | Coalition | At par |
| Push-payment fraud in Coverage H | Emergence CEP-005 (Australia) | At par. Path fixes are planned (T2-1) |

Use this table in the interview. It shows the design was benchmarked, and it keeps you from "adding" features you already have.

---

## 3. Tier A: adopt now

| # | Idea | Borrowed from | What changes in Harborline | Fix-list link | Size |
| --- | --- | --- | --- | --- | --- |
| A1 | **Paying a ransom is never required**, plus a pre-payment routine and support for reports the law requires | NCSC with ABI, BIBA and IUA (UK, May 14, 2024); UK Home Office pre-payment notice proposal (response July 2025); Australia's Cyber Security Act 2024 (72-hour report of a payment made for you) | III.3 new opening and law paragraph; one sentence in III.4.6; back page | Implements **T2-19** | ~⅓ page |
| A2 | **Security terms count only when they mattered.** One closed list of conduct terms | UK Insurance Act 2015 s11; German GDV AVB Cyber (Feb 2024) with VVG §28; Swiss revised VVG Art. 45 (2022) | New III.1.9; IV.1 points to it | Implements **T2-17**; generalizes **T2-6** | ~⅓ page |
| A3 | **One payment-fraud trigger** naming both deceived parties (you and your bank), with **client accounts** you operate | HSB Cyber Suite CSC 02-2025 ("wrongful transfer event"); CFC (Mar 2025) and Aviva (Jul 2026) client-funds cover | Replaces **fraudulent instruction**; new **financial institution** and **client accounts** definitions; H.1; III.6.1 | **Replaces** W-02 and W-03 (**T2-1**, **T2-1a**) | Net ~0 |
| A4 | **Limits map**: each incident and each period, plus caps that say "applies across coverages" | *CiCi Enterprises v. HSB Specialty* (N.D. Tex., Feb 23, 2026); HSB; ISO CY 00 02 | Item 6 gets two columns; new III.1.1a–1b | Implements **T2-1e**, **T2-3**, **T2-6** | ~¼ page |
| A5 | **Related incidents are one incident**, discovered in the earliest period, with continuity for customers switching from another insurer | ISO CY 00 02 11 21 | New III.1.3a | Extends **T2-1c** (W-06); needs **T2-10** | ~⅙ page |
| A6 | **One retention per policy year** | CFC Cyber Proactive Response (Apr 2025) | New Item 5 row; new III.1.3A | Aligns with **T2-1c**, **T2-16** | ~⅛ page |
| A7 | **External early warning** (FBI, CISA, bank, IT provider or us) is always a reasonably suspected incident | Tokio Marine & Nichido SME cyber (Japan) | New **early warning** definition; one sentence in Coverage A; V.2.3 re-scoped | Extends **T2-1f**; resolves the **T2-8** overlap | ~⅙ page |
| A8 | **Foreign privacy regulators** named in "regulatory proceeding" | Canadian forms (OPC; Québec CAI under Law 25) | Two definitions | Uses **T1-8**'s insurability wording | 3 lines |
| A9 | **Court attendance**: $500 per person per day, $10K per period | Coalition UK 2026 specimen; CFC; Markel UK; Tokio Marine HCC NetGuard Plus | New III.7.6; **claim expenses** carve-out | Uses **T2-1e**'s per-period labeling | 4 lines |
| A10 | **Cloud-account tie-breaker** for attacks on the vendor's side, and a **narrower exclusion 12** so a cloud provider's internal DNS fault isn't "core internet infrastructure" | Beazley BBR and At-Bay hosted-systems approach (background); Oct 20, 2025 AWS outage | Sentence added to **cloud accounts**; exclusion 12 definition | Completes **T2-0** and **T2-4** | ~⅛ page |

### A1. Paying a ransom is never required (Section III.3 and III.4.6)

**Why:** III.4.6 ("take reasonable steps to resume operations") can be read to require paying when paying would shorten the outage, and the same argument can be run as failure to mitigate. Nothing in the form rules that out. The UK market put the opposite on record in 2024. For a small firm under pressure it is the most reassuring sentence the policy can contain.

> **Harborline draft (merged from 10a items 13–14, 10c §3.5 and T2-19). Rewrite in your own words.**
>
> **Paying is never required.** Whether to pay is your decision, made with our consent under the steps below. You never have to pay a ransom to keep any other coverage. We will not reduce what we pay under any coverage because you chose not to pay, even if paying might have shortened the outage. Coverage C pays negotiation, investigation and advice costs whether or not a payment is made.
>
> **Before any payment.** Before we consent to a payment, the attack must have been reported to the FBI or CISA; our breach coach will make the report for you if you ask. The breach coach will also screen the payee for sanctions, and keep a short written record of why a payment is being considered and what alternatives were assessed (such as restoring from backups). The breach coach holds that record for you so that it stays privileged where the law allows.
>
> **Laws about paying.** If a law requires you to notify a government agency before or after an extortion payment, to wait for permission, or to explain a payment afterwards, you may do so without our consent, and Coverage C pays the reasonable legal cost. A delay the law requires is not a breach of this policy. If we make a payment for you, we will give you within 12 hours the facts you need for any report the law requires. If a law forbids the payment, we will not pay it, but Coverage C still pays negotiation, investigation and advice costs.
>
> *Add to III.4.6:* "Reasonable steps do not include paying a ransom or other extortion payment."
>
> *Back page:* "You never have to pay a ransom to keep your coverage."

**Flags:**
- US clocks the "laws about paying" paragraph already absorbs:
  - NYDFS 500.17(c): 24 hours after a payment, plus a 30-day explanation (background; verify);
  - CIRCIA's proposed 24-hour ransom-payment report (final rule pending);
  - OFAC licensing.
- It replaces the current III.3 paragraph that begins "If a law requires you to report a ransom payment…". Don't double-count report 05's version of the same idea.

### A2. Security terms count only when they mattered (new Section III.1.9)

**Why:** the most resented small-business denials involve a missing control that had nothing to do with the loss. Harborline already applies the principle piecemeal: the KEV rule applies to an incident "it causes", and the callback cap applies when an employee "acts on an unverified instruction". But it doesn't apply it to the ransomware coinsurance. One rule, in one place, makes all the conduct terms consistent and gives IV.1 a single thing to point to.

> **Harborline draft (merged from 10a item 15 and 10b E1 and E2). Rewrite in your own words.**
>
> **9. How your security can affect what we pay.**
> 1. **A closed list.** Only three terms can reduce what we pay because of how you manage security: the ransomware coinsurance (part 1.6), the known-exploited-vulnerability coinsurance (part 1.7) and the lower Coverage H limit for an unverified instruction (Section III, part 6.1). No exclusion or condition adds to this list. (Section V, part 3, about your **application**, is separate.)
> 2. **The gap must have mattered.** Each of these terms applies only to the extent that the missing control or procedure caused the **incident** or made the loss larger. We must show this. If it affected only part of the loss, the term applies only to that part.
> 3. **Backups that worked anyway.** If you restore the affected data from your own backups, the ransomware coinsurance does not apply to that **incident**, even if they were not **verified backups**.
> 4. **Ordinary mistakes don't count.** An honest mistake or one-off lapse by an **employee** or **executive** does not trigger any of these terms. Only the situations the terms themselves describe do: backups not verified, a vulnerability we notified you about left unpatched and unmitigated for 45 days, or an unverified payment instruction acted on.
> 5. **Credits are part of your price.** The security credits in Item 7 follow whether the verified control is in place (part 1.5), whatever caused the **incident**.
> 6. This part does not change exclusion 4 (intentional wrongdoing).

**Choices made while merging (the source reports disagreed):**
- **Who proves the link: the insurer.** Report 10a and 10b's option A put the burden on the insurer. The European norm, and the UK s11 default, put it on the insured. The insurer burden matches Harborline's war-clause stance and Colorado's rule that the insurer proves an exclusion (background). The cost is a short forensic causation note on ransomware claims.
- **Credits stay objective.** Report 10a would put credit loss under the relevance rule too; 10b would not. Keep credits outside it (part 5). They are a priced term, checking causation for every retention adds claims friction, and W-21 ("substantially in place") already handles fairness. Say this in the rationale, or a reviewer will ask why credits don't need causation.
- **The German fault-degree quota is out.** A reduction "in proportion to the severity of fault" becomes a discretionary, bad-faith-exposed percentage fight in Colorado (C.R.S. 10-3-1115/1116), and it can't be priced. The KEV "notice plus 45 days" rule is already an objective stand-in for gross negligence.
- **Keep T2-6 as well.** Its narrow scope (restoration and BI from encryption only) is clearer than the general rule. The two work together.

### A3. One payment-fraud trigger, with client accounts (Section II; H.1; III.6.1)

**Why:** Cedar Ridge runs payroll for 40 clients and operates their accounts under delegated authority. The current form covers only "accounts you hold for clients" and only an *employee* being deceived. Planned fixes W-02 (bank impersonation) and W-03 (who is deceived) patch this in two places. HSB's filed admitted form does it in one definition.

> **Harborline draft (10d §4.1, with 10a item 12's client-account scope). Rewrite in your own words.**
>
> **Payment fraud** means a deliberate deception, by any means of communication (including email, text, messaging app, letter, phone or video call, and synthetic or deepfake audio or video), by anyone acting against your interests, that:
> 1. leads you, or a **financial institution** that holds your accounts or **client accounts**, to transfer money or securities, or to change payment or bank details that are then used for a transfer; and
> 2. causes you a direct loss, or a loss you must make good to a client.
>
> In this definition, "you" means the **named insured** acting through anyone authorized to make, approve or change its payments, including an **executive**, **employee**, individual independent contractor, or an **AI agent** acting within its authority.
>
> **Financial institution** means a bank, credit union, payroll or payment processor, broker-dealer or similar institution that holds or moves money or securities for you or your clients.
>
> **Client accounts** means accounts you hold for clients, and a client's own account that you are authorized in writing to operate or to start payments from (for example, for payroll or bill-paying services). For a client's own account, we pay only where you are legally obligated to reimburse the client, or you reimburse the client with our consent.
>
> *H.1 (replacement):* "**funds transfer loss** you incur because of **payment fraud** or **computer fraud**."
>
> *III.6.1 (added):* "The lower limit applies only when you acted on a request you did not verify. It never applies when the party deceived was your **financial institution**."

**Flags:**
- It **supersedes** W-02's separate "bank impersonation fraud" and W-03's rewrite of item 3. Keep W-02's other parts: the altered-batch wording in **computer fraud**, and "resulting from".
- "Anyone acting against your interests" keeps a rogue insider in scope, which HSB leaves out. Exclusion 4 (as fixed by T2-1h and T2-11) applies to the insider personally, and V.9 already makes H excess of a crime policy.
- It widens H for payroll and bill-pay firms. Price it, and ask about client-payroll volumes (T3-1 already does).
- Consequential edits:
  - the **incident** list;
  - Item 6 H's plain-English column;
  - Item 7's callback row;
  - application 5.2–5.3;
  - Coverage R.

### A4. Limits map and express cross-coverage caps (Item 6; new III.1.1a–1b)

**Why:** in *CiCi Enterprises v. HSB Specialty* (N.D. Tex., Feb 23, 2026) the court refused to apply a ransomware sublimit across insuring agreements because the endorsement didn't say it did. Harborline's planned system-failure cap (T2-3) and ransomware coinsurance scope (T2-6) are exactly that kind of cross-coverage term. They must say so expressly. The same table also answers W-08's per-incident vs per-period question.

> **Harborline draft (10d §4.2). Rewrite in your own words.**
>
> **1a. How the limits in Item 6 work.** Each limit in Item 6 shows two amounts: the most we will pay for any one **incident**, including every **claim** arising from it, and the most we will pay for all **incidents** in the **policy period**. Both are part of, and not in addition to, the policy aggregate limit in Item 4, unless Item 6 says "in addition".
>
> **1b. Caps that apply across coverages.** A limit marked "applies across coverages" in Item 6 is the most we will pay for that kind of loss under all coverages combined, whichever coverage or coverages the loss falls under. These caps are:
> (a) the **system failure** limit, which caps **business income loss**, **extra expense** and **restoration costs** caused by a **system failure**, under Coverages D and F combined; and
> (b) the ransomware coinsurance in part 1.6, which applies only to **restoration costs** and **business income loss** under Coverages D and F caused by ransomware encrypting or locking your **computer systems**.
>
> A limit not marked "applies across coverages" limits only the coverage it appears next to.

| Coverage (Cedar Ridge, illustrative) | Each incident | Policy period total | Applies across coverages? |
| --- | --- | --- | --- |
| B, C, D (attacks), F, I, J, L | $1,000,000 | $1,000,000 | No |
| System failure (D and F) | $250,000 | $250,000 | **Yes** |
| E | $500,000 | $500,000 | No |
| H (with callback) | $250,000 | $250,000 | No |
| K | $250,000 | $250,000 | No |
| M / N / O | $100K / $100K / $50K | same | No |
| A (in addition to the aggregate) | $25,000 | [per-period cap from T2-8] | No |

**Flags:** define "ransomware" once (T2-6). Decide W-08's open question: suggest that proof-of-loss help erodes only the aggregate, never a sublimit.

### A5. Related incidents are one incident, discovered in the earliest period (new III.1.3a)

> **Harborline draft (10d §4.3). Rewrite in your own words.**
>
> **3a. Related incidents are one incident.** **Incidents** are related if they share a common cause, involve the same attacker's continuing access, or form a causally connected series. Related **incidents**, and every **claim** arising from them, are one **incident**. That **incident** is treated as first **discovered** on the date the earliest of them was first **discovered**, and as reported on the date the first of them was reported to us.
>
> **Which policy responds.** If that date falls in an earlier policy period of a policy we issued to you, that policy responds, with one limit and one **retention**, and this policy does not. If the earlier policy was issued by another insurer, this policy still responds to the related **incidents** first **discovered** during this **policy period**, less anything that other insurer pays for them.

**Flags:**
- It needs **discover** defined (T2-10 / W-18).
- The trade-off to state in the rationale: a long campaign found in year 1 can use up year 1's limit, and year 2's fresh limit won't help. That is the ISO market position.
- The other-insurer sentence stops a new customer being stranded between Harborline and a prior carrier that uses a different trigger.

### A6. One retention per policy year (Item 5; new III.1.3A)

**Why:** firms hit once are often hit again soon. At-Bay reports twice the risk within two years (report 02). Examples are re-intrusion after ransomware, or a second fraud from the same stolen mailbox. A second $7,500 retention in the same year is the cash shock SMB cover exists to prevent. The cost is about $1–2 of expected loss per policy, at a frequency of 1.2–2% a year (report 10c §3.3; an assumption).

> **Harborline draft (merged from 10a item 2 and 10c §3.3, which were almost identical). Rewrite in your own words.**
>
> *Item 5, new row:* **Most you pay in retentions each policy period:** one retention, the amount shown above after any credit or claim-free reduction.
>
> **3A. A yearly cap on retentions.** Once the dollar **retentions** you have paid for **incidents** first **discovered**, and **claims** first made, in one **policy period** add up to the retention in Item 5, no further dollar **retention** applies in that **policy period**. A **claim** arising from an **incident** counts in the period in which the **incident** was first **discovered**. **Waiting periods** and coinsurance still apply.

**Flags:** Coverage H's $2,500 fast-report retention counts toward the cap at the amount paid. It needs the same period rule as T2-1c. It stands on its own: CFC pairs it with unlimited reinstatements, which Harborline declines.

### A7. An external alert is always enough (new definition; Coverage A; V.2.3)

**Why:** small firms usually learn of a compromise from outsiders. Planned fix T2-1f says a *reasonably* suspected incident qualifies. This removes any argument about reasonableness when the trigger is an outside alert. It also gives the $2,500 pre-incident help a clean, separate job, which resolves the T2-8 overlap.

> **Harborline draft (10c §3.2). Rewrite in your own words.**
>
> **Early warning** means a notice to you, from any of the following, that your **computer systems** may have been compromised, or that your credentials or data are being offered or used by criminals: the FBI, CISA, the U.S. Secret Service or another government agency; your bank; your **IT provider**; a **dependent provider**; a security company monitoring your systems; or us.
>
> *Coverage A, added:* An **early warning** is always a reasonably suspected **incident**. When you report one through any channel in Item 10, we will provide **incident response services** to investigate it, even if the investigation shows that nothing happened. An investigation that finds nothing is not an **incident** or **claim** for your claim-free reduction or when we price your renewal.
>
> *V.2.3, re-scoped:* **Pre-incident assistance** is for security questions before anything is suspected and before any **early warning** (for example, whether an email is phishing, or whether a vendor's security terms are adequate).

**Flags:**
- Define **IT provider** (report 10c §3.7): your outside IT contractor or managed service provider. It is never an **executive** (W-34).
- Align the list of alert sources with W-25's precautionary-shutdown text.
- The cost is bounded by Coverage A's per-period cap (T2-8).

### A8. Foreign privacy regulators (Section II)

> **Harborline draft (10c §3.9). Rewrite in your own words.**
>
> **Regulatory proceeding** means a request for information, civil investigative demand, investigation or civil proceeding, arising from a **security failure** or **privacy event**, by:
> 1. a U.S. federal, state or local government agency (such as the Federal Trade Commission, a state attorney general or the U.S. Department of Health and Human Services); or
> 2. a government agency or data protection authority outside the United States (such as the Office of the Privacy Commissioner of Canada or Québec's Commission d'accès à l'information).
>
> *Personal information, first line:* "…information about an identifiable individual that any law, in the United States or elsewhere, requires to be protected…"

**Flag:** penalties stay "where insurable under the law that applies" (T1-8). Foreign penal fines are likely uninsurable. Don't promise more.

### A9. Court attendance (new III.7.6)

> **Harborline draft (merged from 10a item 8 and 10d §4.12). Rewrite in your own words.**
>
> **6. Your time at hearings.** If we ask, or a court or arbitrator requires, an **executive** or **employee** to attend a trial, hearing, deposition, arbitration or mediation in a covered **claim**, we will pay you $500 for each day or part of a day each person attends, up to $10,000 per **policy period**. This is part of the aggregate limit, and no **retention** applies.
>
> *Claim expenses definition:* "…does not include your own staff's salaries or overhead, except as Section III, part 7.6 provides."

**Choice made:** 10d would make these payments **claim expenses**, and 10a would make them a separate payment. The separate payment is clearer: it pays the firm for lost billable time, not the defense. Either way it reduces the aggregate.

### A10. Cloud-account tie-breaker and a narrower exclusion 12

> **Harborline draft (10d §4.4 and §4.6). Rewrite in your own words.**
>
> *Added to the **cloud accounts** definition (T2-0):* If an attack on a **dependent provider's** systems gives someone unauthorized access to your **cloud accounts**, or damages, encrypts or exposes data in them, we treat it as a **security failure** affecting your **computer systems** for Coverages B, C, F and H. Any interruption caused by the provider's service being unavailable is covered under Coverage E (or Coverage P for a **system failure**), not Coverage D.
>
> *Exclusion 12, with T2-4:* "Core internet infrastructure" means the public domain name system (its root and top-level-domain servers), internet exchange points and internet backbone networks. It does not include a **dependent provider's** own systems, including the name servers it runs for its own services. (Utilities and telecoms stay in T2-4's separate **infrastructure provider** definition.)

**Why the second sentence:** the AWS outage of October 20, 2025 is widely reported to have started with a DNS fault *inside* AWS (background; verify). As written, exclusion 12 could exclude it, which would gut Coverage E for exactly the event customers fear most.

**Flag:** pay once where the **privacy event** definition ("while a **dependent provider** holds it for you") also applies.

---

## 4. Tier B: adapt, if there's room

These are worth doing, but each adds pages or a pricing decision. The drafts are in the source report named in the last column.

### Coverage

| # | Idea | Borrowed from | Harborline version | Draft |
| --- | --- | --- | --- | --- |
| B1 | **Impersonation and deepfake response**: expert analysis, takedown requests to platforms and registrars, PR, client warnings. No breach needed | Coalition Deepfake Response Endorsement (Dec 2025); Coalition UK 2026 specimen; Aviva Cyber Complete (Jul 2026) | New Coverage W, $25K per period, $2,500 retention, 90 days from discovery. It closes the gap the rationale currently names (T4-9). **Separate gap:** clients who pay fake invoices from a lookalike domain, with no breach at the firm, fall outside H.2. That is a real CPA-firm need but a priced option (C6) | 10d §4.10 |
| B2 | **Executives' personal funds and identity** after a breach of *the firm's* systems | CFC (Private Enterprise wordings; whether CPR v4.0 keeps it is unconfirmed) | New H.3, $25K within the H limit, excess of the executive's bank and homeowners cover. No callback cap. Exclusion 4 still applies | 10a item 11 |
| B3 | **AI voluntary shutdown**: switching off a misbehaving AI agent | Beazley AI Voluntary Shutdown endorsement (Sept 24, 2026) | New III.4.2a. A hijacked agent is treated as a security failure; any other malfunction as a system failure, inside the $250K cap. Merge with W-25 and T2-5 | 10d §4.11 |

### Fairness and claims handling

| # | Idea | Borrowed from | Harborline version | Draft |
| --- | --- | --- | --- | --- |
| B4 | **Small-loss safe harbor**: the coinsurances apply only above the first $50K | Hiscox Germany (reported waiver of the gross-negligence defense for losses up to €50K) | A new III.1.9 part 7. "First $50K" rather than "losses under $50K" avoids a cliff. The most it gives back is $10K per incident (20% × $50K). It softens the KEV coinsurance, so you could exclude KEV | 10b E3 |
| B5 | **Define verified backups** precisely: weekly, offline or immutable, admin access behind MFA or a separate domain, 30-day retention, and a restore test within the last 12 months | Hiscox Germany backup duty (source page not identified) | New definition used by III.1.6, Item 7 and the application. Feeds T3-7's evidence list | 10b E4 |
| B6 | **Warning and cure** before a post-loss duty (cooperation, documents) can affect a claim | German VVG §28(4) | "We will tell you in writing what we need and give you 30 days before any failure affects your claim." **Carve out** the claims-made reporting deadline (T1-6) and square it with T2-12 | 10b E6 |
| B7 | **You need answer only what we asked** | German VVG §19 | One line in V.3: the honest-mistake remedy applies only to questions on the application. Pair it with T2-13 and T3-2 | 10b E5 |
| B8 | **Retention billed last**, payable in six interest-free monthly installments | US pay-on-behalf practice, extended | One paragraph in "Two promises". Unpaid retention is not premium, so it can't ground cancellation. The remedy is set-off | 10d §4.13 |

### Services and pricing

| # | Idea | Borrowed from | Harborline version | Draft |
| --- | --- | --- | --- | --- |
| B9 | **Security services with a no-forfeiture promise.** The services themselves (threat alerts, phishing training, email security, MDR) sit outside the contract | CFC CPR (services written into the wording, Apr 2025); Stoïk and Dattak (France); Swiss carriers' training; Hiscox CyberClear Academy; AIG CyberEdge UK; LMA draft "compulsory module"; **Colorado SB25-058** (2025) | New V.12: "We may offer… They never reduce your cover… What we provide counts as verified." Keep the list in a services guide. **The reports disagreed** (below). **T2-7 must come first**, or continuous scanning widens the scan estoppel | 10d §4.8; 10c §3.6 |
| B10 | **Verified-framework tier**: an attestation by the insured's IT provider to CIS Controls v8.1 IG1, a NIST CSF 2.0 profile or an FTC Safeguards Rule written security program earns a credit and short-form renewal. **Never** a coverage condition | Singapore Cyber Essentials mark (insurer discounts); UK Cyber Essentials; Australia's Essential Eight; Germany's DIN SPEC 27076 CyberRisikoCheck | Item 7 row replacing, not stacking on, per-control credits (T2-16). Implements T3-7. Leave the percentage blank until priced | 10c §3.1; 10b E11; 10a item 16 |
| B11 | **Earn credits mid-term**, not only lose them | Dattak and Stoïk "dynamic" cover (France) | III.1.5: a control verified mid-term earns its retention credit from the date verified. Premium changes wait for renewal, since admitted rates can't move mid-term | 10b E10 |
| B12 | **$0 retention on panel forensics and breach coach** if reported within 72 hours | Coalition Active Cyber Policy Canada (Mar 2026); Emergence (Australia, reported) | Coverage B's investigation and breach-coach items only, not notification or PR. Steers insureds to the panel early | 10c §3.4 |

### Transparency

| # | Idea | Borrowed from | Harborline version | Draft |
| --- | --- | --- | --- | --- |
| B13 | **"Policy at a glance"** in fixed questions: what's covered, what isn't, the three conduct terms, your duties, how to cancel. Plus worked examples in a companion guide | EU IPID format; Hiscox UK policy summary (Dec 2024); CFC Key Facts and interactive wording (Apr 2025) | One page after the cover. The cover already promises "plain-English notes" that don't exist, so this delivers them. Generate it *after* the Tier 1 and 2 fixes. It must not contradict the wording (Colorado misrepresentation rules) | 10b E12; 10a item 19; 10c §3.8 |
| B14 | **Renewal "what changed" table** | Hiscox Germany synopsis (10/2023) | A renewal notice condition: every wording change, side by side, with who it helps. Complements V.11.7 liberalization | 10b E13 |
| B15 | **Legal clock card**: FTC Safeguards (500+ customers, 30 days), Colorado C.R.S. 6-1-716 (30 days), IRS reporting for tax preparers, NYDFS if relevant, CIRCIA when final | NIS2's staged 24h / 72h / 1-month clocks | Back page or the Coverage A welcome pack. Update it on send day (T1-10) | 10b E19 |
| B16 | **Publish claims results against the service "aims"** | ABI (UK) industry claims statistics (Nov 2025) | Insurer-level: one line in the rationale ("we'd publish results against V.7's aims yearly"). It supports T1-9 | 10a item 20 |

### Where the reports disagreed on services (B9), and the recommendation

- **10a, 10b and 10c:** write the service list into the filed form, never as an off-policy inducement.
- **10d:** Colorado SB25-058 amended the anti-rebating statute (C.R.S. 10-3-1104). Insurers may give loss-mitigation services "not specified in the policy". So keep them outside the contract.
- **Recommendation: a hybrid.**
  - The policy holds only the generic clause and the no-forfeiture promise.
  - Coverage A and the KEV notice stay contractual, as today.
  - Everything else goes in a services guide.
- **Two checks for counsel:**
  - Does a generic mention count as "specifying" a service? (verify)
  - If a Harborline-provided MDR fails, the insured's remedy lies in the service contract, not the policy. Flag that for reinsurers and E&O.

---

## 5. Tier C: optional priced add-ons, named in the rationale as "what I'd test next"

| # | Option | Borrowed from | Shape (all numbers are judgment) | Why optional | Source |
| --- | --- | --- | --- | --- | --- |
| C1 | **Coverage T: Fast Downtime Payment** (parametric BI) | LMA draft standard SME wording (UK, 2026; a US version planned); **AIG with Parametrix cloud-outage product (Aug 13, 2026)**. Parametrix paid within days of the Oct 2025 AWS outage | $1,000 per covered business hour after an 8-hour threshold (the same as D's waiting period). 40 hours per event ($40K), $80K per period. Named cloud services and regions, or an outage our IR team verifies. Paid within 5 business days, **credited against** D, E or P for the same interruption; you keep any excess. A $40K widespread-outage cap applies to T and P only, never D, E or F. The hourly amount is capped at 50% of average revenue per business hour | It needs an actuarial memo from monitor outage data, and filing may question a parametric trigger. Cedar Ridge's T would be priced against a ~$5,500 policy | 10d §5.1, §5.3–5.5 |
| C2 | **Coverage U: one limit reinstatement** | Brit C360 "any one claim" (Mar 2026); CFC unlimited reinstatements (2024–25); Emergence CEP-005.1 each-incident limit (Feb 2026) | Refills the aggregate once, for later unrelated incidents. Never for system failure, widespread outages, T or related incidents. Present it as "each incident $1M; period total $2M" | Uncapped frequency can't be rated on admitted paper. One bounded reinstatement can. Rewrite the rationale's "declined" row as "unlimited declined; bounded option offered" | 10d §5.2; 10a item 3 |
| C3 | **AI regulatory defense** | Beazley AI Regulatory Defense & Penalties endorsement (Sept 2026) | Extends J to proceedings under AI-specific laws (Colorado SB 26-189 from Jan 1, 2027). Defense always; penalties only where insurable; own sublimit | The law isn't in force yet, and there is no loss data | 10d §4.11; 10a item 18 |
| C4 | **$0 retention with qualifying MDR** | At-Bay InsurSec (Oct 2025); Coalition | $0 retention on B, C and F if reported within 24 hours of the MDR alert. It replaces the MDR credit rather than stacking on it | Depends on T2-16's MDR definition; a pricing call | 10d §4.9 |
| C5 | **Goodwill payments** to affected clients | MS&AD and Sompo (Japan) | A small per-client amount for apology gestures after a privacy event | Cheap client retention, but new to US buyers | 10c §4.1 |
| C6 | **Lookalike-domain client fraud**: clients who pay a fake invoice with no breach at the firm | Gap found in 10d §4.10 | Extend H.2 to **impersonation events**, within H's shared limit | Adds fraud exposure; price it separately | 10d §4.10 |
| C7 | **Risk classes** that set expected controls by class | Netherlands: CCV and Verbond van Verzekeraars risk classification, and the SME security mark | A risk-class table in Item 7 | **A fork, not an add-on.** It settles the open "credits or bind prerequisites?" question toward eligibility and changes the Item 7 economics. Adopt it fully or not at all | 10b E15 |
| C8 | **Distribution ideas**: MSP-embedded micro tier; BOP/embedded cyber; public-entity pools | Japan's METI/IPA お助け隊 bundle; HSB Cyber Suite; Hartford CyberChoice First Response (Dec 2025); pools | Outside the form. One line in the Corgi strategy note, if at all | Not a wording question | 10c §4.4; 10d ideas 18, 20 |

**Accumulation note (for the strategy half-page, Tier 6).** CPA firms share a few tax, payroll and IT platforms, so a cloud-trigger T is nearly always a widespread event. Cap T exposure per platform in February to April, or add a seasonal load. The reinsurance market for this exists (Parametrix placed Cumulus Re cloud-outage capacity for Hannover Re, 2026–27; snippet).

---

## 6. Skip, and why

| Idea | Seen at | Why not for Harborline |
| --- | --- | --- |
| Full-limit system failure; full-limit non-IT contingent BI | Emergence CEP-005.1 (Australia, Feb 2026); CFC CPR (2025) | Conflicts with the review-supported $250K system-failure cap (T2-3) and the systemic-risk design |
| Unlimited reinstatements; uncapped "any one claim" limits | CFC CPR; Brit C360 | Can't be rated on admitted paper. C2 offers the bounded version |
| Widespread-event limit across all coverages | Chubb Cyber ERM 2.2 E13 (Australia); Chubb PF-54815 (US) | T2-3 already scopes it: never on attacks on the insured's own systems. Use it only inside C1 |
| Parametric supplier-downtime cover | LMA 2026 draft | Needs Coverage P first; revisit with C1 |
| Criminal reward | Coalition UK (paid "at our discretion"); CFC not confirmed | 10a said adapt; 10d said skip. **Skip.** Low value for a CPA firm, awkward next to the ransom rules, and exclusion 17 complications |
| Free insurance bundled with a certification | UK Cyber Essentials (£25K cover, AIG) | A distribution quirk. B10 takes the useful part: the credit |
| German fault-degree quota (reduce "in proportion to the severity of fault") | VVG §28(2), §81(2) | Discretionary and bad-faith-exposed in Colorado; can't be priced. A2 takes the causation part |
| France's 72-hour criminal complaint as a *condition* of payment | LOPMI, Code des assurances L12-10-1 (Apr 2023) | A forfeiture with no US basis, inviting *Craft*-style deadline fights. A1 and T2-19 take the useful part, the report, as a service |
| Statutory EU mechanics: pre-contract disclosure tiers, risk-increase rules, 14-day withdrawal, mid-term premium adjustment, post-loss cancellation right | German VVG §§8, 19, 23–27, 40, 92; Swiss VVG Art. 2a | Statutory terms of art. Admitted US rates are filed. Post-loss cancellation would break V.5.2 and C.R.S. 10-4-109.7 |
| GDPR, NIS2 and DORA terms; GDPR fine-insurability language | EU | Wrong regimes. Use FTC Safeguards, GLBA, state breach laws, IRS Publication 4557 and CIRCIA |
| "State of the art" security duty | German IT-security law | Vague. It would re-create the patching-denial problem. Name the frameworks only in the application and B10 |
| Defense outside limits by statute | Québec Civil Code art. 2503 | Québec-only |
| Product disclosure statement, target market determination, s.54 mechanics; ASD, CERT-In and PDPC clocks; Essential Eight references | Australia, India, Singapore | Jurisdiction-specific. B10 and B15 use the US analogues |
| Neglected Software Exploit | Chubb Cyber ERM | Harborline's KEV rule already does this, more narrowly and fairly |
| Enhanced Business Recovery set; vanishing retention; pre-claim help | Coalition | Already in Harborline |
| Contingent bodily injury and property damage wrap | C&F Simple Cyber v6.0 (Sept 2025) | Not a CPA-firm exposure |
| Goods-diversion fraud | Emergence CEP-005.1 | Hits distributors, not professional offices |
| Warranty plus insurance | Cysurance | A different product |

---

## 7. How this changes the fix list in `README.md` section 5

| Fix | Change |
| --- | --- |
| **T2-1, T2-1a** (W-02, W-03) | **Replaced** by A3's single payment-fraud definition. Keep W-02's altered-batch and "resulting from" parts |
| **T2-1c** (W-06) | Extended by A5 (earliest period, other-insurer continuity) and A6 (one period rule for retentions) |
| **T2-1e, T2-3, T2-6** | Implemented by A4. The caps must say "applies across coverages" (*CiCi*) |
| **T2-1f, T2-8** | Extended by A7. The early-warning rule also removes the pre-incident help overlap |
| **T2-0, T2-4** | Completed by A10, including the exclusion 12 DNS narrowing |
| **T2-6, T2-17** | A2 becomes the single list that IV.1 points to. Keep T2-6's narrow scope as well |
| **T2-19** | Implemented inside A1 |
| **T2-5, W-25** | Merge with B3 (AI shutdown) in one III.4.2 rewrite |
| **T2-7** | A **prerequisite** for B9 (services) and B11 (earned credits) |
| **T2-13, T3-2** | Pair with B7 (answer only what's asked) |
| **T2-16** | Governs B10, B11, B12 and C4. One stacking rule for all of them |
| **T1-6** | B6's cure notice must carve out the claims-made reporting deadline |
| **T1-8** | A8 uses the same insurability wording for foreign penalties |
| **T3-7** | Implemented by B10's attestation, with B5's backup checklist |
| **T4-9** | Trade-offs: deepfake response is now B1 rather than "declined"; the $0-retention path is B12 or C4; add C1 and C2 as "considered, offered as options" |
| **Tier 6** (accumulation half-page) | Add the C1 accumulation note |

**Nothing in Tier A re-proposes a planned fix as new.** Where an idea overlaps a planned fix, the draft merges into that fix and says so.

---

## 8. Using this in the package

**In the policy:** Tier A only. It adds about a page and a half, and seven of the ten items finish fixes you'd make anyway. Add B1–B3 only if the page budget allows, since each is a new coverage paragraph and an Item 6 row.

**In the rationale:** one short paragraph and one table row. The paragraph sketch below is **draft only; write your own**:

> *Draft (rewrite in your own words):* I also compared Harborline with 2024–26 small-business wordings from the UK, Europe, Asia-Pacific and Canada. Most of what they offer, Harborline already has. I took four ideas: the UK rule that a security term applies only when it could have mattered to the loss; the UK industry position that insurance never obliges anyone to pay a ransom; CFC's single retention per year; and a limits table whose cross-coverage caps say so expressly, after a February 2026 Texas ruling struck down one that didn't. I left out Germany's fault-based reductions, because in Colorado they'd become discretionary disputes. Two options I'd test next are a fast downtime payment (as AIG and Parametrix launched in August 2026) and one limit reinstatement.

**In the interview:** three talking points.
1. "Harborline's fairness rules are borrowed from the UK Insurance Act and German law, but made objective so they can be filed and priced in Colorado."
2. "I looked at per-event limits and parametric BI. Here's why I'd offer them as bounded options rather than build them into the core."
3. "The *CiCi* ruling is why every cross-coverage cap in Item 6 says 'applies across coverages'."

**Before quoting any source:** check section 9. Every item is snippet-level.

---

## 9. Verify before quoting

The highest-value checks, in order:

1. ***CiCi Enterprises v. HSB Specialty*** (N.D. Tex., Feb 23, 2026): the docket or reporter citation, the endorsement wording, and whether it was appealed.
2. **UK Insurance Act 2015 s11**: the burden and the "could not have increased the risk" test, from legislation.gov.uk.
3. **NCSC, ABI, BIBA and IUA guidance** (May 14, 2024): the no-obligation position, and whether it recommends recording the decision.
4. **CFC Cyber Proactive Response** (Apr 2025):
   - the single-retention option;
   - the client-account social-engineering cover;
   - court attendance;
   - whether executives' personal funds survived from Private Enterprise.
5. **HSB CSC 02-2025**: the "wrongful transfer event" definition (Heartland PDF).
6. **ISO CY 00 02 11 21**: the earliest-period related-events rule. The snippet hedged ("will likely"), so check with a licensee.
7. **Colorado SB25-058**: its conditions, effective date, and whether a generic mention counts as "specified".
8. **AIG and Parametrix** (Aug 13, 2026): the US terms and admitted or surplus-lines status. **LMA SME wording**: whether it was published after May 2026.
9. **Tokio Marine & Nichido**: the external-alert trigger for investigation costs.
10. **Coalition Active Cyber Policy Canada** (Mar 2026): the scope of the $0 retention with Coalition IR.
11. **Hiscox Germany**: the €50K waiver (first €50K, or losses up to €50K?) and the backup standard.
12. **AWS, Oct 20, 2025**: the root cause (DNS inside AWS), before relying on the exclusion 12 point.
13. **Beazley September 2026 endorsements** and **Coalition's Deepfake Response Endorsement** limits.

Each source report has its own full verify list: 10a §7, 10b §6, 10c §9 and 10d §7.

---

## 10. Source reports

| Report | Scope | Items | Verdicts |
| --- | --- | --- | --- |
| `10a_uk_lloyds.md` | UK and Lloyd's: CFC, Hiscox, Coalition UK, Brit, Beazley, Aviva, Markel, AIG, LMA, NCSC/ABI, Insurance Act 2015 | 20 | 5 adopt, 11 adapt, 3 optional, 1 skip (item 16 is split: adapt the credit, skip the bundled insurance) |
| `10b_europe.md` | Germany (GDV, VVG, Hiscox DE), France (Stoïk, Dattak, LOPMI), Switzerland, Netherlands, EU (IPID, NIS2) | 20 | 5 adopt, 10 adapt, 2 optional, 3 skip |
| `10c_apac_canada.md` | Australia (Emergence, Chubb, Delta), Japan (Tokio Marine, MS&AD, Sompo, METI), Singapore, India, Canada (Coalition, Chubb, Travelers, Law 25) | 18 | 1 adopt, 8 adapt, 4 optional, 2 skip; the rest already in Harborline |
| `10d_us_novel.md` | HSB, ISO, *CiCi*, AIG/Parametrix, Brit, CFC, Coalition, At-Bay, Beazley, TMHCC, Chubb, C&F, Hartford, Cysurance, SB25-058 | 20 | 2 adopt, 11 adapt, 4 optional, 5 skip (items 11 and 12 are split) |
