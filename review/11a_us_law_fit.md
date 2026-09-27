# 11a. US and Colorado legal fit of the borrowed ideas (A1–A10, B1–B16, C1–C8)

Prepared September 27, 2026. Legal and filing lens only. Two other reports cover loss-data utility and US market prevalence.

**What this report asks of each idea:**
1. Does US or Colorado law already give this protection?
2. Can an admitted Colorado carrier file it?
3. Does it create legal risk?
4. How useful is it legally?

**Evidence labels:**
- **[snippet]**: seen in a web search result this session. The source was not opened.
- **[prior]**: taken from an earlier report in `review/` (mostly 05, 07 and 10d).
- **[background]**: my own knowledge, not verified this session.
- **[policy]**: the current Harborline text (`policy.md`).

**Method.** I ran 25 web searches. One direct download of the SB25-058 bill PDF was blocked at the proxy, and I did not retry it. No statute, regulation or opinion was read at source. **This is research, not legal advice.** Colorado coverage and regulatory counsel should confirm every point before filing.

**Rating keys:**
- **US-fit.** G: fileable as drafted. A: fileable with changes. R: doesn't translate.
- **Legal utility.**
  - H: changes a likely legal outcome, meaning whether a claim is paid or litigated.
  - M: resolves a real ambiguity that has been litigated.
  - L: restates default law, or adds a new benefit that resolves no legal dispute. Clarity value only.
  - Neg: adds dispute risk.
- **New cover.** A brand-new coverage (for example B1 or C1) changes whether something is paid only because it is new. I rate it L unless it also settles a legal fight. Whether it is worth buying is for the utility and market reports.

---

## 1. Bottom line

1. **Nothing on the list is unlawful for an admitted Colorado carrier.**
   - Colorado does not appear to prior-approve commercial P&C forms. Claims-made forms need an annual compliance certificate (C.R.S. 10-4-419) [snippet; the rest is background, verify].
   - So in Colorado, "fileable" mostly means two things: consistent with Colorado statutes, and supported by a rate.
   - **Only C8 is Red, and only as policy wording.** It is a distribution idea, not a clause.
   - **C1 (parametric BI) is Amber in Colorado but Red in New York.** New York's 2025 parametric statute covers only weather events measured by a government agency [snippet].
2. **Four ideas are legally strongest: A2, A3, A4 and A10.** Each changes whether a claim is paid in an area courts have fought over:
   - causation and anti-concurrent wording (A2; Colorado enforces anti-concurrent causation clauses as written);
   - the *Apache*/*Medidata* split and *Kane* (2025) on fraud (A3);
   - *CiCi v. HSB* (2026) on sublimits (A4);
   - cloud and infrastructure boundaries (A10).

   A5 (related incidents) and B9 (the services no-forfeiture promise) come next.
3. **A4 protects the insurer more than the insured.** Without it, contra proferentem and *CiCi* would favor Cedar Ridge. For the insured its value is certainty. Say so plainly if asked "does this protect the insured?"
4. **Several ideas repeat default law. They add clarity but no new protection:**
   - A1's "you never have to pay a ransom": no US case forces payment, and no search found an insurer arguing it.
   - A7: an FBI or bank alert already meets an objective "reasonable suspicion" test.
   - B6: under *Secrist*, Colorado already requires material and substantial disadvantage before a failure to cooperate counts.
   - B7: partly redundant.
   - B14: C.R.S. 10-4-110.5 already requires 45 days' notice, with reasons, before any coverage cut or premium increase at renewal.

   Keep them only as cheap, one-line clarity. Don't sell them as new protection.
5. **Five drafts create legal risk as written:**
   - **B13** ("policy at a glance"): a summary broader than the wording creates coverage by reasonable expectations (*Bailey*). It also risks a misrepresentation-of-policy-terms charge.
   - **B5** (backup definition): five new conditions mean five new ways to lose the credit.
   - **A5** (related incidents): if the first, small event was never reported, the campaign attaches to a closed policy year. *Craft* then enforces that year's claims deadline strictly, and nothing pays.
   - **A7** (early warning): an alert "always" being an incident can fix the discovery date and create a "known circumstance" under exclusion 2.
   - **A3** (payment fraud): the draft reintroduces "direct loss", the word *Apache* turned on.
6. **Three new legal findings:**
   - **A10:** the **system failure** definition itself excludes "internet infrastructure". Narrowing exclusion 12 alone won't bring an AWS-type internal DNS fault into D or P.
   - **A1:** the "written record" it creates matches what NYDFS 500.17(c) requires insureds to file. It will be disclosed, so don't promise privilege.
   - **A3:** UCC Article 4A (C.R.S. 4-4.5-202, -204) sometimes makes the bank refund a fraudulent wire. H should pay and then pursue the bank, and the insured must keep its one-year objection right.
7. **C3 (AI regulatory defense) should be defense-only.**
   - SB 26-189 violations are deceptive trade practices under the Colorado Consumer Protection Act, with fines up to $20,000 per violation [snippet]. Colorado public policy likely bars insuring such penal amounts [prior].
   - Today, Coverage J and exclusion 8 (unfair or deceptive trade practices) both block this cover [policy].
   - Enforcement waits for the Attorney General's rules. The law takes effect Jan 1, 2027 [snippet].
8. **B9: SB25-058 supports the hybrid services design.** Services written into the policy become policy benefits: they must be filed and rated, and a late service can support a C.R.S. 10-3-1115 "unreasonable delay" claim. If Harborline runs MDR for a tax preparer, Harborline also becomes a "service provider" under the FTC Safeguards Rule.
9. **Many items are legally neutral: A6, A9, B4, B8, B10–B12, C2 and C4.** Decide them on price and utility, not law.

---

## 2. Master table

| ID | Idea | Default US/CO law already gives it? | Fileable in CO admitted? | Legal risk | US-fit | Legal utility | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | Paying a ransom is never required; pre-payment routine; laws about paying | **Mostly.** No US rule makes an insured pay criminals to mitigate, and no case was found. But Harborline's own III.4.6 and "could have been restored with reasonable speed" create the argument | Yes. No state bans private-sector payments. NC and FL (and reportedly TN) bans reach public entities only | Promising privilege over a record NYDFS 500.17(c) makes you disclose. The 12-hour promise becomes a bad-faith yardstick | A | L (the pre-payment routine is M for OFAC and NYDFS compliance) | **Keep with change.** Drop the privilege promise. Add "reasonable speed never assumes a ransom payment" to **period of restoration**. Add "unless law enforcement advises otherwise" to the pre-payment report |
| A2 | Security terms count only when they mattered; closed list | **No.** Colorado has no UK s11-type statute and enforces anti-concurrent causation as written (*CIRSA v. Northfield*). The insurer proves exclusions, but a coinsurance is a limit, so the burden is unclear | Yes (insured-favorable) | Causation disputes on each ransomware claim. Two-times exposure (10-3-1116) if applied without evidence. Clashes with exclusion 2 and V.3.4 as written. Doesn't stop *ICS*-type rescission | A | **H** | **Keep with change.** Limit it to pre-incident controls. Make exclusion 2 yield for known, unexploited weaknesses. Define the causal test. Say V.3 (application) is separate |
| A3 | One payment-fraud trigger: you or your bank deceived; client accounts | **No.** Fraud coverage is the most-litigated cyber-crime area (*Apache* vs *Medidata*/*American Tooling*/*Principle*; *Kane*, N.M. 2025). UCC 4A sometimes puts wire loss on the bank | Yes | The draft says "direct loss" (the *Apache* word). Voluntary client reimbursement needs consent (*Stresscon*). Crime-policy overlap | A | **H** | **Keep with change.** Use "resulting from". Add recovery against the bank, and a duty to preserve the insured's 4A objection. Consent "not unreasonably withheld" for client refunds |
| A4 | Limits map; caps marked "applies across coverages" | **Default favors the insured** (contra proferentem; *CiCi*). A4 mainly makes the insurer's caps hold | Yes | Low. Item 6 and the text must match word for word, and name the insuring agreements | G | M (H for the insurer) | **Keep.** It is the fix *CiCi* asks for. Tell reviewers it trades an insured windfall for certainty |
| A5 | Related incidents are one; earliest period; continuity with another insurer | **Partly.** Related-claim clauses are enforced as written, and broad "logically or causally connected" wording is read broadly. No Colorado default for which first-party year a campaign belongs to | Yes | **Gap:** an unreported first event attaches the campaign to a closed year, and *Craft* enforces the claims deadline, so nothing pays. The other-insurer sentence is a drop-down promise | A | M | **Keep with change.** Apply the earliest-period rule only if the earliest incident was reported in time (to us or a prior insurer). Otherwise this policy responds. Make it subject to exclusion 2 |
| A6 | One retention per policy year | No (pure contract) | Yes (filed rule) | Minimal. Needs the same period rule as T2-1c | G | L | **Keep if priced.** Legally neutral |
| A7 | An external alert is always a reasonably suspected incident | **Largely yes.** Reasonable suspicion is objective, and an FBI, CISA or bank alert meets it. T2-1f does the real work | Yes | Double edge: it can fix the discovery date (and, with A5, the year) and create a "known circumstance" for exclusion 2 | A | L | **Keep with change.** Limit the deeming to the A and B trigger. Say an alert alone is not discovery or knowledge for exclusion 2. Or cut it to one sentence in Coverage A |
| A8 | Foreign privacy regulators | **No for J** (the definition lists US agencies only). "Personal information" already says "the law", not "US law" | Yes | Foreign penal fines often uninsurable; sanctions; currency conversion | A | L | **Keep with change, low priority.** Defense first; penalties "where insurable"; no criminal matters |
| A9 | Court attendance ($500/day) | No (claim expenses exclude staff pay) | Yes | None material | G | L | **Keep** (harmless). A utility and price call |
| A10 | Cloud-account tie-breaker; narrower exclusion 12 | **Partly.** A court would probably read the ambiguity for the insured, but only after a fight. **The system failure definition also excludes internet infrastructure** | Yes | Fixing only exclusion 12 leaves the definition's bar in place for D and P | A | M | **Keep with change.** Narrow "internet infrastructure" in the **system failure** definition too. Route D, E and P consistently with T2-0 |
| B1 | Deepfake and impersonation response | No (today it needs a security failure or privacy event) | Yes | Low. Platforms can refuse takedowns (Section 230). First-party only | G | L (new cover) | **Keep** as a small core or option. Legally clean |
| B2 | Executives' personal funds and identity | **Partly.** Reg E caps consumer loss from *unauthorized* electronic transfers, but not fraud-induced ones the victim authorized | Yes, with drafting | Executives aren't insureds for personal matters today. Overlap with homeowners and bank refunds | A | L | **Downgrade to optional.** Make executives insureds for H.3. Excess of Reg E, bank refunds and homeowners |
| B3 | AI voluntary shutdown | No | Yes | Conflicts unless merged with W-25 and T2-5 | A | L | **Keep with change.** One III.4.2 rewrite |
| B4 | Small-loss safe harbor on coinsurance | No | Yes (rating rule) | None | G | L | **Downgrade to a pricing option.** Pick either B4 or A2's softening, not both |
| B5 | Detailed "verified backups" definition | n/a (contract) | Yes | **Adds conditions** (weekly, MFA or separate domain, 30-day retention). Each is a new dispute point | A | **Neg** as drafted | **Keep with change.** Keep the policy test at today's two elements. Put the checklist in the application and evidence list (T3-7) |
| B6 | Warning and cure before a post-loss duty counts | **Largely yes.** Colorado requires material and substantial disadvantage for a cooperation defense (*Secrist*). Not for consent (*Stresscon*) or claims deadlines (*Craft*) | Yes | Must carve out the *Craft* deadline. A small procedural trap for the insurer | A | L | **Downgrade** to one courtesy sentence in V.2.1. Don't present it as new protection |
| B7 | You need answer only what we asked | **Partly.** Rescission needs a knowing, material misstatement (*Hollinger*). V.3.3 already says "knowingly and intentionally". V.3.2's "omission" could still reprice for unasked facts | Yes | None | G | L | **Keep** (one line), with T2-13 |
| B8 | Retention billed last; 6 interest-free installments | No | Yes. Written into the policy, it is part of the product, not a rebate | Credit and collection risk. Unpaid retention isn't premium | G | L | **Downgrade** to claims-operations practice |
| B9 | Security services outside the policy, plus a no-forfeiture promise | SB25-058 allows value-added services not specified in the policy (related to the coverage, for loss mitigation, reasonable cost, contact information) | Yes (hybrid) | If "specified", services become policy benefits (filing, rate, 10-3-1115 delay claims). A Harborline-run MDR is an FTC Safeguards "service provider". E&O | A | M | **Keep with change.** T2-7 first. Generic clause only. A separate service contract. Safeguards service-provider terms |
| B10 | Verified-framework tier (credit only) | n/a | Yes (rating plan) | An inaccurate attestation must lead only to V.3.2's repricing | G | L | **Keep** as a credit; never a condition |
| B11 | Earn credits mid-term | n/a | Yes, if in the filed rating rule | Premium can't move mid-term without a rule | A | L | **Keep with change.** File it as a retention rule |
| B12 | $0 retention with panel forensics within 72 hours | n/a | Yes | No Colorado anti-steering rule for cyber found | G | L | **Optional.** A pricing call |
| B13 | "Policy at a glance" page | n/a | Yes, but it is a representation of the policy | A summary broader than the wording creates coverage (*Bailey* prong 2) and risks a misrepresentation charge. Summaries already mismatch (W-35) | A | **Neg** as drafted | **Keep with change.** Write it last; cite the operative section on each line; never broader than the text |
| B14 | Renewal "what changed" table | **Largely yes.** C.R.S. 10-4-110.5: 45 days' first-class notice, with reasons, of any coverage decrease or unilateral premium increase at renewal | Yes | None; a compliance aid | G | L | **Keep** as a short condition that matches the statute. The table is the format |
| B15 | Legal-deadlines card | No legal duty | n/a (off the form) | Reliance on an out-of-date card | A | L | **Keep off the form.** Date it; add "your breach coach confirms" |
| B16 | Publish claims results against the service aims | n/a | n/a | Becomes a bad-faith benchmark; advertising rules | G | L | **Rationale line only** |
| C1 | Fast Downtime Payment (parametric BI) | No | **Probably, with the indemnity link.** Colorado defines insurance to include paying a set amount on a determinable contingency [background]. **New York:** weather-only statute | Wager or derivative label; basis-risk disclosure; a monitor-decides clause; multistate filings | A (CO); **R in NY** | L (new cover) | **Keep as "test next".** Keep the proof that you were affected and the revenue cap. File separately from the core form |
| C2 | One limit reinstatement | No | Yes, as a priced endorsement | Interplay with A5 and ERP | G | L | **Keep as an option** |
| C3 | AI regulatory defense | **No.** J needs a security failure or privacy event, and exclusion 8 bars deceptive-practice counts | Yes for defense. **Penalties likely uninsurable in CO** | Illusory penalty cover. Enforcement waits for AG rules | A | M (defense) | **Downgrade** to an optional, defense-only endorsement. Launch after AG rulemaking |
| C4 | $0 retention with qualifying MDR | No | Yes | Overlaps B9 if the insurer supplies the MDR | G | L | **Optional.** A pricing call |
| C5 | Goodwill payments to affected clients | **No.** The question is litigated (*Southwest v. Liberty*, 5th Cir. 2024: customer vouchers after an outage not automatically excluded) | Yes. A covered cost paid to third parties is not a rebate | Admission risk (Colorado's apology statute covers health care only). Payments to members of a pending class | A | L | **Optional.** Add a no-admission line, and counsel sign-off if a suit is pending |
| C6 | Lookalike-domain client fraud (no breach at the firm) | No. Impostor-payment cases split the loss between payer and payee case by case | Yes | Must waive subrogation against clients. Added fraud exposure | A | L (new cover) | **Optional, priced.** Add a subrogation waiver |
| C7 | Risk classes that set expected controls | n/a | Yes, as rating or eligibility | If classes become conditions, they work as forfeitures (see A2) | A | L | **Drop for now.** It is a fork |
| C8 | Distribution ideas (MSP-embedded, BOP, pools) | n/a | Not a form item | Producer licensing for MSPs; separate BOP filings | **R** (as wording) | n/a | **Drop from the form.** One strategy line, with a licensing caveat |

---

## 3. Notes per idea

### 3.0 Legal baseline used in every row

- **Filing.**
  - Colorado takes P&C filings through SERFF [snippet].
  - Claims-made forms must be certified each year as compliant with Colorado law (C.R.S. 10-4-419) [snippet].
  - Rates must not be excessive, inadequate or unfairly discriminatory (C.R.S. 10-4-403; Regulation 5-1-10) [snippet].
  - Policies for "exempt commercial policyholders" skip filing only if the buyer uses a qualified risk manager (Regulation 5-1-13) [snippet]. Cedar Ridge doesn't qualify.
  - I believe Colorado uses file-and-use (not prior approval) for commercial rates and does not prior-approve commercial forms [background; verify in the Division of Insurance's SERFF general instructions].
  - I found no Colorado readability statute for commercial forms [background].
  - Harder objections will come from prior-approval states when Corgi rolls out nationally.
- **Rebating.** C.R.S. 10-3-1104 bars rebates and inducements "not specified in the policy". SB25-058 amended it (the bill summary lists paragraph (1)(g)) [snippet].
  - Anything written into the filed policy is part of the product, not a rebate.
  - Anything outside the policy needs the SB25-058 safe harbor: it must relate to the coverage, aim mainly at loss mitigation, lower claim costs or risk education, cost a reasonable amount relative to the premium, and come with contact information [snippet].
  - The effective date was not verified.
- **Bad faith.** C.R.S. 10-3-1115/1116 treat business insureds as first-party claimants, including for benefits paid on their behalf, and allow two times the covered benefit plus fees [prior]. Every "we must show" and every service promise becomes a reasonableness yardstick.
- **Interpretation.**
  - Ambiguity is read against the insurer [background].
  - The insurer proves an exclusion applies [background].
  - Reasonable expectations has two prongs (*Bailey v. Lincoln General*, 2011): (1) an ordinary person would not understand from the wording that there is no coverage; (2) the insurer's own conduct led the insured to believe there was coverage [snippet].
  - Colorado enforces anti-concurrent causation clauses (*CIRSA v. Northfield*, Colo. App. 2008) [snippet].
- **Notice and conditions.**
  - First-party late notice needs prejudice (*Clementi*, 2001) [prior].
  - Claims-made deadlines are enforced without prejudice (*Craft*, 2015) [prior].
  - No-voluntary-payment clauses are enforced without prejudice (*Stresscon*, 2016) [prior].
  - A cooperation defense needs material and substantial disadvantage (*State Farm v. Secrist*, 33 P.3d 1272, Colo. App. 2001) [snippet].
- **Federal overlays for a CPA firm.**
  - **FTC Safeguards Rule:** tax preparers are GLBA financial institutions. They must notify the FTC within 30 days of a breach of unencrypted data of 500 or more consumers [prior].
  - **IRS Publication 4557:** a written security plan (WISP) [prior].
  - **NYDFS Part 500.17(c):** notice within 24 hours of an extortion payment, then within 30 days a written explanation of reasons, alternatives, diligence and OFAC checks [snippet]. It does not apply to Cedar Ridge.
  - **CIRCIA:** the final rule was targeted for September 2026, with 72-hour incident and 24-hour ransom-payment reports. It was not confirmed published [snippet].

### A1. Paying a ransom is never required

- **Default law.**
  - No case turned up in which an insurer argued an insured failed to mitigate by refusing to pay [snippet: a targeted search found none].
  - Mitigation asks only for reasonable steps. Courts are very unlikely to call paying a criminal, against FBI and OFAC advice, a required step [background].
  - In *G&G Oil* (Ind. 2021) the insurer argued the reverse, that paying was "voluntary", and lost [snippet/prior].
- **But the form creates the hook.** III.4.6 requires "reasonable steps to resume operations". The **period of restoration** ends when operations "could have been restored with reasonable speed" [policy]. If Harborline consents and the insured declines to pay, that second phrase is a live argument. So add: "Reasonable speed never assumes a ransom or extortion payment."
- **Legality.**
  - Payment is lawful for private US firms unless the payee is sanctioned. OFAC liability is strict, and a timely self-report to law enforcement is a mitigating factor [prior].
  - State bans cover public entities only: NC and FL (2022), and TN per one snippet [snippet]. Ohio's 2025 local-government rule is [background; verify]. New York's 2025 bills would add municipal 24-hour and 30-day reports [snippet].
  - There is no Colorado rule [prior].
- **NYDFS and privilege.** 500.17(c)'s 30-day explanation asks for the reasons for payment, the alternatives considered and the diligence done [snippet]. A1's "short written record" has the same content, which is good design. But a record made for a regulator is made to be disclosed. **Delete the promise that it "stays privileged"** (see also W-51).
- **Pre-payment report.** It supports OFAC mitigation. Add "unless law enforcement advises otherwise, or life or safety requires immediate payment".
- **The "12 hours" promise.** It will become a 10-3-1115 benchmark [prior]. Keep it only if Harborline means it.

### A2. Security terms count only when they mattered

- **Default law gives no causation rule.**
  - There is no Colorado equivalent of UK Insurance Act s11 [prior].
  - Texas has a general "contributed to the loss" statute for policy provisions (Tex. Ins. Code 705.004) [background]. I know of no Colorado analogue [background].
  - Colorado enforces anti-concurrent causation wording as written (*CIRSA v. Northfield*) [snippet], and Harborline's exclusions use "arising from".
  - A coinsurance is a limit, not an exclusion, so a court might not put the burden on the insurer. A2 settles that.
- **The denial pattern is real:**
  - CNA's "failure to follow minimum required practices" exclusion in *Columbia Casualty v. Cottage Health* (C.D. Cal.). It was dismissed in 2015 on dispute-resolution grounds and never decided [snippet].
  - *Travelers v. ICS* (rescission over an MFA answer; stipulated 2022) [prior].
  - The City of Hamilton, Ontario, 2025 denial over incomplete MFA [snippet; Canadian].
- **Scope limit.** The best-known "unrelated control" losses come through the **application** (rescission), which A2 leaves to V.3. A2 will not stop an *ICS*-type case; V.3.3 ("knowingly and intentionally") does. Say so in the rationale, and don't market A2 as the answer to *ICS*.
- **Changes needed:**
  1. Scope it to "how you manage security before an **incident**", so it doesn't swallow post-loss duties (cooperation, consent).
  2. Say expressly that exclusion 2 cannot be used for a known weakness that had not been exploited (W-07). Otherwise "no exclusion adds to this list" contradicts exclusion 2 on the face of the form.
  3. Reconcile the KEV rule with V.3.4 (W-22).
  4. State the test: "caused the **incident** or increased the covered loss". Name the evidence that meets it, such as the forensic report.
- **Risk.** Each ransomware coinsurance now needs a causation finding. Applying it without one invites a two-times claim under 10-3-1116. That is manageable, and it is the point.

### A3. One payment-fraud trigger, with client accounts

- **Litigation map** [prior]:
  - *Apache* (5th Cir. 2016): no coverage.
  - *Medidata* (2d Cir. 2018), *American Tooling* (6th Cir. 2018), *Principle Solutions v. Ironshore* (11th Cir. 2019): coverage.
  - *Interactive Communications* (11th Cir. 2018): no coverage.
  - *G&G Oil* (Ind. 2021): coverage.
  - New: *Kane v. Syndicate 2623-623*, 2025 WL 1733046 (N.M. Ct. App. June 16, 2025). Cover "for" a security breach was ambiguous, so a $4M+ post-breach fraudulent vendor payment was covered [snippet].
  - No Colorado appellate cyber-crime ruling was found [prior].
- **Draft defect.** Item 2 of the draft says "causes you a **direct** loss". That is the word *Apache* turned on. Use "resulting from", as T2-1 already says.
- **Default law partly protects the bank-deceived case.**
  - Under UCC Article 4A as adopted in Colorado (C.R.S. 4-4.5-202, -204), a bank that executes a wire it did not verify under an agreed, commercially reasonable security procedure must refund it. The customer must object within one year (4-4.5-505) [background].
  - Payroll ACH to employees' consumer accounts may fall outside 4A, because the federal Electronic Fund Transfer Act governs part of the transfer [background; verify].
  - So H should pay first and pursue the bank (V.10 already allows this). Add a duty to preserve the 4A objection.
- **Client accounts.** "With our consent" is enforceable without prejudice in Colorado (*Stresscon*) [prior]. Add "which we will not unreasonably withhold".
- **Insiders.** "Anyone acting against your interests" keeps rogue insiders in scope. V.9 (H excess of crime insurance) handles the overlap.
- **Filing.** Social-engineering cover inside a cyber form is routine [background].

### A4. Limits map and caps that say they apply across coverages

- ***CiCi Enterprises v. HSB Specialty*** (N.D. Tex., Judge Lindsay, Feb. 23, 2026) [snippet]:
  - $3M aggregate policy; ransom negotiated from $2M to $400K; losses over $1.2M.
  - HSB tried to cap everything at a $250K ransomware sublimit.
  - The court held the endorsement never said which insuring agreements it modified, so it didn't cap Cyber Extortion. The court found no prior ruling on such an endorsement.
  - Texas law. Colorado also reads ambiguity against the drafter [background].
- **Who it protects.** Without A4, two insured-favorable arguments are live:
  - "each incident" (W-08);
  - "the cap doesn't reach this coverage" (*CiCi*).

  A4 removes both. For Cedar Ridge the gain is certainty, not money. That is still worth having, and it is the honest answer to "does this protect the insured?"
- **Fix alongside it.** H's "(shared)" label, and whether proof-of-loss help erodes a sublimit (W-08).

### A5. Related incidents are one incident, first discovered in the earliest period

- **Law.**
  - Courts enforce related-claim definitions as written. Broad "logically or causally connected" wording is read broadly (a recent Fourth Circuit decision) [snippet].
  - An undefined "related" invites fights [background].
  - No Colorado cyber decision was found.
  - A5's tests (common cause, the same attacker's continuing access, a causal series) are standard.
- **Gap.**
  1. A small phishing event in year 1 is below the retention and never reported.
  2. In year 2, ransomware arrives through the same access.
  3. A5 treats both as one incident discovered in year 1, and says year 2 "does not respond".
  4. Year 1's claims deadline has passed. *Craft* enforces it strictly [prior], so the liability tail gets nothing.

  **Fix:** "The earliest-period rule applies only if the earliest related **incident** was reported to us, or to a prior insurer, within the time Section V allows. Otherwise, this policy responds." Make it subject to exclusion 2 and the continuity date.
- **Other-insurer sentence.** It is a drop-down promise if the prior carrier denies. That is insured-friendly and defensible. State it as intended and price it.
- **Filing.** Nothing conflicts with Colorado's claims-made certificate rule (10-4-419) [snippet].

### A6. One retention per policy year

- No default law. It is a deductible term in the filed rating plan.
- Legal points:
  - It needs the same period rule as T2-1c.
  - H's $2,500 fast-report retention should count toward the cap.
- No bad-faith or filing concern. Decide it on price.

### A7. An external alert is always enough

- **Default law.** "Reasonably suspected" is an objective test. An FBI or Secret Service victim notice, a CISA pre-ransomware notification or a bank fraud alert would meet it [background]. T2-1f already fixes the trigger. A7 adds certainty only.
- **Side effect.** If an alert is "always" a suspected incident:
  - it can also fix the **discovery** date, and with A5, the policy year;
  - an alert received before the continuity date can become a circumstance "an executive knew about" (exclusion 2).

  A vague bank notice ignored in month 11 could shift or bar cover.
- **Fix:** "For Coverages A and B only. An **early warning** is not, by itself, **discovery** of an **incident**, or knowledge of a circumstance under exclusion 2." Keep the claim-free sentence. It is good.

### A8. Foreign privacy regulators

- **Today.** **Regulatory proceeding** lists US agencies only, so an investigation by a foreign data protection authority is not a **claim** under J [policy]. **Personal information** says "the law requires", not "US law", so A8's second edit is clarity only.
- **Insurability.**
  - GDPR fine insurability varies by country.
  - The UK FCA forbids insuring its own penalties; the ICO takes no position; Germany is unsettled [snippet].
  - Colorado public policy disfavors insuring penal amounts (*Lira*; the TCPA-penalty snippet) [prior].
  - Keep "where insurable under applicable law" and promise nothing more.
- **Changes:**
  - exclude criminal proceedings;
  - convert currency by a stated rule (W-31);
  - keep exclusion 17 (sanctions).
- Exposure for Cedar Ridge is small. For Corgi startups with foreign users, it is larger.

### A9. Court attendance

- No default: **claim expenses** exclude the firm's own staff salaries [policy].
- Paying the firm for lost staff time is not a witness fee [background].
- Fileable as a small, sublimited benefit. Legally neutral.

### A10. Cloud-account tie-breaker and a narrower exclusion 12

- **Default law.** The W-01 cloud-account ambiguity would probably be read for the insured, but only after a dispute [prior]. *Kane* shows courts read loose causal words broadly [snippet]. The tie-breaker gives certainty on attacks like Snowflake, where data inside the insured's tenant is hit through the vendor.
- **New finding.** Narrowing exclusion 12 is not enough.
  - The **system failure** definition itself excludes "a failure of power, utility, telecommunications or internet infrastructure".
  - For Coverage P it means "the same events affecting **dependent systems**" [policy].
  - So an AWS-type internal DNS fault can fall out of D and P at the definition stage, before exclusion 12 or its carve-back is reached.
  - **Fix:** use the same narrow meaning of "core internet infrastructure" in both places.
- ***EMOI v. Owners*** (Ohio 2022): software-only harm isn't "physical loss" under a property form [prior]. That is why the cyber form must define its own outage triggers carefully.
- **Verify before relying on it:** the AWS Oct. 20, 2025 root cause [prior].

### B1. Deepfake and impersonation response

- No default. Today the policy needs a **security failure** or **privacy event** [policy].
- Legal notes:
  - Platforms may refuse takedowns because of Section 230 immunity [background].
  - Lookalike domains are handled through UDRP complaints or trademark claims. Those fees fit "lawyers to ask registrars" [background].
  - Colorado's deepfake statutes target elections and intimate images, not business impersonation [background].
- First-party only. Legally clean. Utility is the other reports' call.

### B2. Executives' personal funds and identity

- **Default law.** Reg E (12 CFR 1005.6) caps a consumer's loss from *unauthorized* electronic transfers if reported promptly. It doesn't cover fraud-induced transfers the consumer authorized [background]. So B2 matters mainly for authorized scams and wires.
- **Drafting.** Executives are insureds only "while acting for you" [policy]. Make them insureds for H.3. Pay excess of Reg E, bank refunds and homeowners identity-fraud cover.
- Written into the filed, priced form, it is not an inducement [background].
- Optional.

### B3. AI voluntary shutdown

- No default. SB 26-189 imposes notice, explanation and human-review duties, not shutdown duties [prior].
- The legal risk is internal inconsistency. Merge it into one III.4.2 rewrite with W-25 and T2-5:
  - a hijacked agent counts as a **security failure**;
  - a malfunction counts as a **system failure** (sublimited).

### B4. Small-loss safe harbor

- A contract and pricing term. There is no legal issue.
- It overlaps A2's softening of the coinsurance. Choose one mechanism, or state how they combine.

### B5. Precise definition of "verified backups"

- Today's III.1.6 test has two elements: a restore test within 12 months, and an offline or immutable copy [policy].
- B5 adds weekly frequency, admin MFA or a separate domain, and 30-day retention. Each new element is another fact the insurer can point to, and another fight about proof.
- Under A2 each must also be causal, which multiplies forensic disputes.
- **Keep the policy test at two elements.** Use the checklist to *earn* the credit at underwriting (T3-7), not to *apply* the coinsurance after a loss.

### B6. Warning and cure

- **Colorado already gives most of this:**
  - Cooperation: the insurer must show material and substantial disadvantage (*Secrist*) [snippet].
  - First-party notice: prejudice required (*Clementi*) [prior].
- **Where Colorado is strict, B6 must not reach:**
  - the claims-made deadline (*Craft*);
  - voluntary payments and consent (*Stresscon*). T2-12 handles consent separately.
- So B6 adds clarity, plus value for a multistate form in states with stricter cooperation rules [background].
- **Recommendation:** one sentence in V.2.1: "We will tell you in writing what we need and give you reasonable time to provide it."

### B7. You need answer only what we asked

- *Hollinger* allows rescission for a knowing, material misstatement **or concealment** [prior]. V.3.3 already limits rescission to knowing and intentional misstatements "in your application".
- The remaining gap is V.3.2. Its "error or **omission**" remedy could let Harborline reprice for a fact it never asked about.
- B7 closes that in one line. Pair it with T2-13 and T3-2.

### B8. Retention billed last, in installments

- Written into the filed policy, it is part of the product, not a rebate [background; see 3.0].
- Unpaid retention is not premium. It cannot ground cancellation under V.5.2 or C.R.S. 10-4-109.7 [prior]. Set-off is the only remedy, so there is credit risk.
- Legally neutral. It works better as a claims-operations practice than as a policy term.

### B9. Security services outside the policy, plus a no-forfeiture promise

- **SB25-058** [snippet]:
  - It permits value-added products or services at no or reduced cost when they are *not specified in the policy*.
  - They must relate to the coverage and aim mainly at loss control, lower claim costs or risk education.
  - Cost must be reasonable relative to the premium, and contact information must be given.
  - The NCOIL and NAIC models are similar [snippet].
  - Effective date and exact conditions not verified.
- **Two legal paths:**
  - **Specified in the policy:** the services are part of the insurance. They must be filed and rated, and a failure to deliver could be argued as an unreasonably delayed "benefit" under 10-3-1115 [background].
  - **Not specified:** the SB25-058 safe harbor applies.

  The hybrid (a generic clause plus a services guide) is right.
- **The no-forfeiture promise is the legally useful part.** It blocks the argument that ignoring an insurer alert, or declining a tool, is a failure to maintain security or cooperate. The KEV rule must be the only exception.
- **FTC Safeguards.** If Harborline or its vendor runs MDR for a tax preparer, it is that firm's "service provider". Cedar Ridge must select it, bind it by contract to safeguards, and oversee it (16 CFR 314.4(f)) [background].
- **Contract.** Draft the service contract with its own liability terms, and tell reinsurers about the E&O exposure.
- **Do T2-7 first,** so continuous scanning doesn't widen the scan estoppel.

### B10. Verified-framework tier

- A rating credit. It must be actuarially supported and not unfairly discriminatory (10-4-403) [background].
- If the IT provider's attestation proves wrong, the only remedy should be V.3.2 repricing (T2-13), never rescission.
- Never make it a coverage condition.

### B11. Earn credits mid-term

- Harborline's premium comes from filed rates and can't change mid-term without a filed rule [background]. A retention credit can, if the rating plan says so.
- File it as a retention rule. Premium changes wait for renewal.

### B12. $0 retention with panel forensics within 72 hours

- I found no Colorado anti-steering law for cyber vendors [background].
- Keep the non-panel option (III.2.3).
- A pricing and utility call.

### B13. "Policy at a glance"

- **Legal risk.**
  - Under *Bailey* prong 2, an insurer-made summary that leads an ordinary insured to expect coverage can defeat the wording [snippet].
  - Misrepresenting policy terms is an unfair practice (C.R.S. 10-3-1104) [background].
  - V.11.6 ("notes don't control") won't beat an expectation the insurer itself created [background].
- The current form already has summary-versus-wording mismatches (W-04, W-07, W-27, W-35, W-55) [prior].
- **Changes:**
  - generate the page last, after the Tier 1 and 2 fixes;
  - cite the operative section on every line;
  - never state anything broader than the wording;
  - or drop the page and delete the cover's promise of "plain-English notes".

### B14. Renewal "what changed" table

- **C.R.S. 10-4-110.5** already bars a unilateral premium increase or coverage decrease at renewal of listed commercial lines without 45 days' notice. The notice goes by first-class mail and must give the reasons and the renewal terms [snippet]. The list is illustrative ("such as"): it includes E&O and professional liability, and the prior review treated the parallel cancellation statute as reaching cyber [prior].
- 10-4-110 requires 45 days for nonrenewal [snippet]. Harborline gives 60 [policy].
- So the duty already exists. B14 is a good format for meeting it, and adds broadenings. Write the condition to match the statute.

### B15. Legal-deadlines card

- There is no legal duty, and the card creates reliance risk if it is out of date.
- Content [prior]:
  - FTC Safeguards: 30 days, 500 or more consumers;
  - C.R.S. 6-1-716: 30 days to residents and the Attorney General;
  - IRS: tax professionals report client data theft to the IRS [background];
  - CIRCIA: pending [snippet].
- Keep it off the form, dated, with "your breach coach confirms which apply".

### B16. Publish claims results

- A rationale line, not wording.
- Published results become evidence of the insurer's own standard in a 10-3-1115 case, and count as advertising [background].
- Fine if accurate.

### C1. Fast Downtime Payment (parametric BI)

- **Is it insurance?**
  - Few states have parametric-specific rules, so parametric products are generally regulated like any other insurance [snippet].
  - US regulators usually want some proof that the insured was actually affected, to distinguish a parametric policy from a derivative or wager [snippet].
  - C1's condition 3 ("you must have been affected"), the cap at 50% of revenue per hour, and the credit against D/E/P meet that.
- **Colorado.** I found no parametric statute. Colorado's statutory definition of insurance covers undertaking to pay a specified amount on determinable contingencies [background; verify C.R.S. 10-1-102]. That supports filing.
- **New York is Red on admitted paper.** A 2024 act, effective Jan. 12, 2025, added parametric insurance to Insurance Law §1113 only for **weather-related events measured by a government agency** [snippet]. A cloud-outage trigger doesn't fit.
- **Other states.** Maryland heard parametric-bill testimony in 2026 [snippet; contents not read].
- **NAIC.** No NAIC parametric model act was confirmed. One snippet claims a 2025 model adopted in 34 states. It is uncorroborated; do not repeat it.
- **Market channel.** Surplus lines is the main US channel for parametric [snippet]. AIG's product (Aug. 2026) is a US endorsement for eligible AIG cyber clients. Its paper (admitted or surplus lines) is unconfirmed [snippet].
- **Other risks:**
  - the monitor's data decides the trigger (keep V.8 review);
  - a basis-risk disclosure is needed;
  - "you keep the excess" invites an over-indemnity objection, which the revenue cap answers.
- **Filing strategy.** File it as a separate endorsement, so an objection doesn't hold up the core form.
- *Southwest Airlines v. Liberty* (5th Cir. 2024) shows that outage BI gets litigated [snippet]. Parametric avoids some of that, at the price of trigger disputes.

### C2. One limit reinstatement

- Reinstatement endorsements are ordinary on admitted paper once rated [background].
- State that the reinstated limit never covers related incidents (A5), and how it treats any extended reporting period.
- Legally neutral.

### C3. AI regulatory defense

- **SB 26-189** [snippet]:
  - signed May 14, 2026; effective Jan. 1, 2027;
  - the Attorney General enforces it alone, and there is no private right of action;
  - violations are deceptive trade practices under the Colorado Consumer Protection Act, with fines up to $20,000 per violation;
  - there is a 60-day cure period, except for knowing or repeat violations;
  - enforcement depends on AG rulemaking.
- **Today's form.** J requires a **security failure** or **privacy event**, and exclusion 8 bars deceptive-practice counts except regulatory proceedings arising from those events [policy]. So there is no cover today. A C3 endorsement must carve back exclusion 8 for this purpose.
- **Penalties** are likely uninsurable in Colorado as penal (the *Lira* reasoning; the TCPA-penalty snippet) [prior].
- **Offer defense only.** Exclusion 4 still applies to knowing violations. Launch after the AG's rules.

### C4. $0 retention with qualifying MDR

- A pricing term.
- If Harborline supplies the MDR, B9's service-provider and SB25-058 points apply.

### C5. Goodwill payments to affected clients

- **Not a rebate.** Rebate law targets inducements to buy insurance. Paying the insured's covered costs to third parties is a claim payment [background].
- **Why write it expressly.** In *Southwest Airlines v. Liberty* (5th Cir. 2024), customer vouchers after a system outage could not be excluded outright as "purely discretionary" [snippet]. The question gets litigated, and an express, sublimited term settles it.
- **Risks:**
  - Colorado's apology statute protects health-care providers, not CPA firms (C.R.S. 13-25-135) [background]. Keep "not an admission".
  - Payments or releases offered to members of a pending class need defense counsel's sign-off (court oversight of class communications) [background].

### C6. Lookalike-domain client fraud

- **New cover.** When a client pays an impostor, courts split the loss case by case, often by asking who could best have prevented it (for example *Arrow Truck Sales*, M.D. Fla. 2015; *Beau Townsend Ford*, 6th Cir. 2018) [background]. The firm is left chasing its own client.
- **Condition.** C6 must **waive subrogation against clients**. Otherwise the insurer would sue the insured's customers.
- Price it separately.

### C7. Risk classes

- As a rating or eligibility plan, it must be actuarially justified and not unfairly discriminatory [background].
- If a class sets expected controls that operate as conditions, they become forfeitures, and every A2 issue returns.
- It is a strategic fork. Drop it for this filing.

### C8. Distribution ideas

- Not policy wording.
- **Embedding in an MSP.** Anyone who sells, solicits or negotiates insurance needs a producer license (C.R.S. 10-2-401); referral-fee rules are narrow [background].
- **Embedding in a BOP.** That is a separate form filing.
- **Public-entity pools.** Pools are not insurers [background].
- One strategy line at most, with a licensing caveat.

---

## 4. Skip-list check (report 10, section 6)

| Skipped idea | Does US or Colorado law make it valuable or necessary? | Flag |
| --- | --- | --- |
| Full-limit system failure; full-limit non-IT contingent BI | No | Skip stands |
| Unlimited reinstatements; uncapped "any one claim" limits | No. **Correct the reason:** nothing in law bars them on admitted paper. The obstacle is actuarial support for the rate [background] | Reword "can't be rated on admitted paper" to "would need a rate we can't yet support" |
| Widespread-event limit across all coverages | No | Skip stands |
| Parametric supplier-downtime cover | No; New York's weather-only statute would also bar it there [snippet] | Skip stands |
| Criminal reward | Lawful in the US. Exclude public officials and sanctioned persons [background] | Skip on value, not law |
| Free insurance bundled with a certification | **US law strengthens the skip.** Free coverage is a premium rebate. SB25-058 covers services, not free insurance [snippet/background] | Skip stands, and more firmly |
| German fault-degree quota | Colorado bad-faith exposure (10-3-1115/1116) [prior] | Skip stands |
| France's 72-hour criminal complaint as a condition | US crime forms sometimes require a police report, but *Craft*/*Clementi* fights follow [prior] | Skip stands. H's 72-hour retention and A1's report are the right substitutes |
| EU statutory mechanics (withdrawal, risk increase, post-loss cancellation) | Colorado has its own mandatory mechanics: 10-4-109.7 (cancellation), 10-4-110 (nonrenewal), **10-4-110.5 (renewal cuts)** [snippet] | Skip the EU mechanics, but **mirror the Colorado ones** (D-5, D-6, B14) |
| GDPR, NIS2 and DORA terms | No | A8 keeps only the "where insurable" rule |
| "State of the art" security duty | No. The FTC Safeguards Rule requires "reasonable" safeguards; importing that as a policy condition would create the patching-denial problem [background] | Skip stands |
| **Defense outside limits by statute (Québec)** | **Not only Québec.** Some US states restrict defense-within-limits (eroding) policies, for example New York's Regulation 107 limits which lines may use them [background; verify]. No Colorado restriction found | **Flag for the multistate rollout.** Not needed for the Colorado filing |
| PDS, TMD, s.54; ASD, CERT-In and PDPC clocks | No | Skip stands |
| Neglected Software Exploit | No | Skip stands |
| Coalition features already in Harborline | No | Skip stands |
| Contingent bodily injury and property damage wrap | No | Skip stands |
| Goods-diversion fraud | No | Skip stands |
| Warranty plus insurance (Cysurance) | Warranties can be regulated as service contracts or insurance [background] | Skip stands |

**Result.** No skip is made necessary by Colorado law. One (defense outside limits) may become necessary in some other states. One skip reason (unlimited reinstatements) should be reworded, because the obstacle is actuarial, not legal.

---

## 5. Verify before quoting

In priority order:

1. **Colorado's commercial filing regime.** Is it file-and-use for rates, and are commercial P&C forms filed or prior-approved? Check the Division of Insurance's SERFF general instructions and Regulation 5-1-10 [background].
2. **SB25-058.** The final text, the conditions (including any non-discrimination rule), the effective date, and whether a generic mention in a policy counts as "specified" [snippet].
3. ***CiCi v. HSB*** (N.D. Tex. Feb. 23, 2026). The docket or reporter citation, and whether it was appealed [snippet].
4. ***Kane v. Syndicate 2623-623***, 2025 WL 1733046 (N.M. Ct. App. June 16, 2025). Whether it was taken further on appeal [snippet].
5. ***Southwest Airlines v. Liberty Insurance Underwriters*** (5th Cir. 2024). The citation and the scope of the "solely" holding [snippet].
6. **C.R.S. 10-4-110.5.** Whether its list of commercial lines reaches stand-alone cyber [snippet].
7. **New York Insurance Law §1113** parametric amendment: its scope (weather and government data only) and its effective date [snippet].
8. **The "NAIC Parametric Insurance Model Act (2025, 34 states)" snippet.** It is likely false. Don't repeat it without the NAIC model-law page.
9. **The AIG Parametric Cloud Outage Solution:** is it written admitted or surplus lines [snippet]?
10. **SB 26-189:** the penalty amount, the cure period and the AG rulemaking dependency [snippet].
11. **The Colorado definition of "insurance"** (C.R.S. 10-1-102) [background].
12. **Case citations:**
    - *State Farm v. Secrist*, 33 P.3d 1272 (Colo. App. 2001);
    - *CIRSA v. Northfield* (Colo. App. 2008);
    - the Colorado case placing the burden on the insurer to prove an exclusion [snippet/background].
13. **UCC 4A.** The Colorado section numbers, the one-year rule, and whether payroll ACH falls outside 4A [background].
14. **State ransom-payment bans:**
    - the NC and FL statute numbers;
    - Tennessee's scope;
    - Ohio's 2025 local-government rule;
    - New York's 2025 municipal bills [snippet/background].
15. **CIRCIA:** was the final rule published by the send date [snippet]?
16. ***Cottage Health*** (dismissed 2015) and **City of Hamilton** (Ontario, 2025) are snippet-level. Use them as illustrations only.
17. **Eroding-limits restrictions** in other states, including New York's Regulation 107 [background].
18. **The AWS Oct. 20, 2025 outage root cause** (internal DNS), before relying on the A10 point [prior].
