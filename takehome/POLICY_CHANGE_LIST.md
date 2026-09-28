# Policy change list — CORG-CY-0200 (merged from 4 reviews)

How to apply: work top to bottom. Part 1 needs your yes/no. Part 2 is exact text swaps, in page order; each **Current** quote appears once in the policy (line breaks joined by spaces). Replacements are the same length or shorter unless noted, so pagination should hold. Part 3 is formatting/styling instructions with no or few text changes. If a Part 3 instruction touches a sentence already changed in Part 2, apply Part 2 first.


## Part 1 — Coverage fixes that need your decision (recommended: apply A-2, A-3, A-8)

### A-2 · Error · Page 16 · Coverage H, Special conditions
**Problem:** "employees" is bold, so it takes the defined meaning ("any past or present employee", Def. 22). Definitions 10 and 37, however, exclude only a *current* owner, partner, member, officer, employee or individual independent contractor. As printed, the Coverage H summary says a former employee's fraud is not payment fraud. The operative definitions say it is.
**Current:** "Theft by your own owners, partners, employees or individual contractors is not payment fraud or computer fraud."
**Fix:** "Theft by current owners, partners, employees or individual contractors is not payment fraud or computer fraud."

---

### A-3 · Inconsistency · Pages 16, 27, 29 · Coverage H(2) / Def. 31 vs Def. 53: insider invoice diversion
**Problem:** H is meant to exclude insider theft ("Theft by your own … employees … is not payment fraud or computer fraud"). But H part (2) is triggered by a *security failure*, and a security failure expressly includes acts "caused by an employee or executive acting outside their authority or against your interests" (Def. 53). As a result, an employee who uses the firm's email to redirect customer invoices triggers H(2) and Def. 31, while the same employee stealing by funds transfer does not. A claims handler would pay one and deny the other.
**Current (Def. 31, last sentence):** "It does not matter whether you delivered before or after the diverted payment."
**Fix:** "Delivery timing is irrelevant. Payment fraud's insider exclusion also applies."

### A-5 · Inconsistency · Page 21 · Section III, part 1, first vs fourth rule
**Problem:** Rule 1 says the largest retention always applies. Rule 4 then makes the $2,500 H retention "the only dollar retention" for H loss. For an incident that triggers both B and H, the two rules conflict, because rule 1 is not stated as subject to rule 4.
**Current:** "If different retentions could apply, the largest one applies."
**Fix:** "Except under item 4, if retentions differ, the largest applies."

### A-6 · Inconsistency · Page 36 · Section VII, part 9.1 vs 9.2
**Problem:** Part 9.1 makes every coverage except A, B and H excess of other valid insurance. Part 9.2 (and Coverage I's special conditions) makes I respond "as if that other insurance did not exist" when E&O insurance also applies. 9.1 does not defer to 9.2. Cedar Ridge carries $2M of accountants' E&O, so this conflict will actually arise.
**Current:** "All other coverages apply in excess of other valid insurance, unless that insurance is written specifically to sit above this policy."
**Fix:** "Subject to part 9.2, other coverages apply in excess of other valid insurance, unless it is written to sit above this policy."

### A-7 · Inconsistency · Pages 11, 23, 34 · Consent for voluntary notices and non-panel vendors vs VII 2.2
**Problem:** Coverage B says "voluntary notices do [need consent]", Def. 4(g) pays them only "if we agree in advance", and I 1.3 allows a non-panel vendor only "if we agree". Section VII 2.2, however, reimburses any otherwise-covered cost incurred without consent "unless the lack of consent actually harmed us", and it carves out only extortion payments. Def. 4 says 2.2 "explains when you need our consent", so it is unclear which rule wins.
**Current (VII 2.2):** "This rule never waives prior written consent for an extortion payment or the costs of acquiring and transferring it under paragraph a of extortion expenses."
**Fix:** "This rule never waives advance consent for voluntary notices (breach response costs, paragraph g) or for paragraph a of extortion expenses." (If the no-prejudice rule is also meant to cover non-panel vendors, as Def. 24 implies for negotiators, leave I 1.3 as is. Otherwise add 1.3 to this carve-out.)

### A-8 · Inconsistency · Pages 14, 32 · Section I 3.3 shutdown cover vs exclusion 14
**Problem:** Part 3.3 covers an interruption when you shut down "on advice from … a government agency". Exclusion 14 removes loss arising from "an order to shut down your systems" by a government authority, whatever the cause. So a shutdown the government *advises* is covered, but one it *orders* for the same security failure is excluded.
**Current:** "This does not apply to a regulatory proceeding, or to a law enforcement request to preserve or hand over evidence about a covered incident."
**Fix:** "This does not apply to a regulatory proceeding, a shutdown under Section I, part 3.3, or a law enforcement request for evidence about a covered incident."

### A-9 · Inconsistency · Pages 34–35 · Standard for deliberate misstatement: VII 3.3 vs 5.2 and 5.5
**Problem:** Rescission requires that an executive "knowingly and intentionally made a material misstatement". Cancellation (5.2) and loss of the extended reporting option (5.5) use a lower, differently worded test ("knowingly made a material false statement" / "a knowingly false application statement"). The insurer could cancel mid-term on facts that would not support rescission.
**Current (5.2):** "because an executive knowingly made a material false statement in your application"
**Current (5.5):** "if the reason was non-payment or a knowingly false application statement."
**Fix (5.2):** "because of a deliberate misstatement under part 3.3"
**Fix (5.5):** "if the reason was non-payment or a deliberate misstatement under part 3.3."

### A-14 · Inconsistency · Page 17 · Coverage K trigger vs definition of claim
**Problem:** Liability coverages require a **claim**. For card matters, the definition requires "a *written* demand for PCI fines and assessments", but K is triggered by any "demand".
**Current:** "When it applies. A demand under your merchant services agreement"
**Fix:** "When it applies. A written demand under your merchant services agreement"

### A-15 · Inconsistency · Page 35 · VII 4.2 promises an extended reporting period that 5.5 does not grant
**Problem:** Part 4.2 says that after an acquisition "You may buy an extended reporting period", but 5.5 makes the option available only "If either of us cancels or does not renew".
**Current (5.5):** "If either of us cancels or does not renew, you may buy 12 months"
**Fix:** "If either of us cancels or does not renew, or part 4.2 applies, you may buy 12 months". This is 22 characters longer. If length is fixed, delete the last sentence of 4.2 instead.

---


#### Also raised by the pages 1–18 reviewer
1. **Coverage C, which costs are still paid when no ransom is paid (p.12).** Special conditions says "negotiation, investigation and sanctions-screening costs", but "Laws about paying" says "negotiation, investigation and advice costs". What we pay lists all four (including legal advice on lawfulness). Make both lists "negotiation, investigation, sanctions-screening and legal advice costs", or confirm the difference is intended.
2. **Outage guide note, utility outages (p.13).** "E and P do not cover general utility, telecommunications or public-internet outages" implies D might. Exclusion 12 applies to every coverage (with a carve-back for a security failure affecting your computer systems), and the system failure definition also leaves these outages out. Consider "Exclusion 12 applies to utility, telecommunications and public-internet outages", which would also match the existing "Exclusion 13 also applies..." sentence.
3. **Notice timing standard (p.4, Item 4 note).** "Report as soon as possible" is a stricter standard than Section VII, part 1.1 ("as soon as practicable"), which is backed by the actual-prejudice rule in 1.3. Consider aligning the wording (for example "as soon as you can") so the Declarations do not seem to set a stricter test.
4. **Coverage H, What we pay (p.16).** "Amounts you must repay clients from client accounts" is narrower than definition 27, which also covers amounts repaid with our consent. Either say "amounts taken from client accounts that you repay" or add "or repay with our consent".
5. **F-9/F-10 assumption.** These edits treat Item 7 as this insured's actual Declarations and drop the "unless ... selected" wording from rows D and F. If the Declarations are also meant to work as a blank form, keep the conditional but write it as "unless System Failure Full Limit is selected".


#### Also raised by the pages 19–37 reviewer
1. **"Employee" in Definitions 10 and 37 conflicts with Definition 22 (p.24, p.28).** Both definitions exclude a "current ... **employee** ... (even if not acting for you at the time)". The bold defined term covers past and present employees but only "while working for you", so "current" and "even if not acting for you" contradict the definition they rely on. The fix is to un-bold "employee" in those two lists or add "(whether or not working for you at the time)". Either change affects who counts as an insider, so the author needs to decide.
2. **Exclusion 4, named-insured imputation leaves out the CEO (p.31).** The exclusion applies to the named insured only if its "owner, managing partner or managing member, chief financial officer or general counsel" took part. Definition 23 (executive) also lists the CEO and the IT/security designee. Section VII 3.3 treats any executive's knowledge as the named insured's for rescission. If the CEO is left out on purpose (the owner usually is the CEO in a small business), say so. If not, add the CEO to the list. Adding the CEO narrows coverage.
3. **Exclusion 19, "the person's written admission" has no person (p.33).** Exclusion 4 names an executive, but Exclusion 19 names no one, so it is unclear whose admission triggers it: any insured's, or only the named insured's? Picking one changes when the exclusion bites.
4. **Definitions intro: "bold terms" vs. "wherever these terms appear" (p.23).** The first sentence limits definitions to bold terms. The second applies them "wherever these terms appear", which suggests non-bold uses count too. Decide which rule is meant and delete the other. It matters for terms that appear unbolded, such as "employee" in some lists.
5. **VII 5.2, "stating the reason" (p.35).** As written, the reason must be stated only for a non-payment cancellation. If a misrepresentation cancellation must also state its reason (usual, and often required by state law), move "stating the reason" so it covers both.
6. **III.3 "Security controls" sits under Section III (Retention) (p.21).** It concerns coverage and the application, not the retention. Moving it (for example to VII 3) would read better, but it changes the structure and would shift pages, so the edit list leaves it where it is.


## Part 2 — Text swaps, in page order (91 edits)

### F-1 · Page 1 · Key points, Claims against your business
**Current:** "A claim must generally be first made against you during the policy period or an applicable extended reporting period. You must also report it as Section VII requires. This is called claims-made and reported coverage."
**Replace with:** "This is claims-made and reported coverage: a claim must generally be first made against you during the policy period or any extended reporting period, and reported as Section VII requires."
**Why:** Leads with the label, then explains it in one sentence instead of three; "any extended reporting period" matches Section I, condition 3.

### F-2 · Page 1 · Key points, Your own losses
**Current:** "Your own losses. Other coverages generally require you to first discover the incident during the policy period. Incident response services (A) and Breach response costs (B) also cover early warnings and suspected incidents as Section I provides."
**Replace with:** "Your own losses. You must generally first discover the incident during the policy period. For Incident response services (A) and Breach response costs (B), an early warning or suspected incident in that period is enough."
**Why:** "Other coverages" makes the reader work out which, and the lead-in already says it. The second sentence now states the A/B rule (Section I, condition 2) instead of pointing to it.

### F-3 · Page 1 · Key points, Settlement decisions
**Current:** "If you reject a settlement we recommend and the claimant would accept, you may pay 30% of later covered damages above the proposed settlement and later claim expenses. Section IV, part 2 explains the calculation."
**Replace with:** "If you reject a settlement we recommend and the claimant would accept, you pay 30% of covered damages above that amount and of later claim expenses, once your retention is used. See Section IV, part 2."
**Why:** The original can be read as "30% of damages above (the settlement and later claim expenses)". The new wording removes that reading and replaces the vague "may" with the actual condition, the retention.

### G-3 · Page 1 · Cover, last paragraph
**Current:** "Read this policy with its Declarations and listed endorsements. The reading guide explains the terms and where to find each rule."
**Replace with:** "Read this policy with its Declarations and endorsements."
**Why:** This instruction appears four times in the document. The second sentence is navigation filler.

### A-10 · Inconsistency · Pages 2, 1, 8, 17 · Name of Section I part 6
**Problem:** The Contents entry does not match the section heading, the PDF bookmark, or the cover page and Important notices, which both tell the reader to look for "Claims and investigations against you".
**Current (Contents):** "6. Claims against you: I-L and optional Q"
**Fix:** "6. Claims and investigations against you: I-L, optional Q". If Contents width is tight, change the heading, bookmark, cover and notice 2 to "Claims against you" instead.

### F-4 · Page 3 · Terms you will see, Aggregate and sublimit
**Current:** "The aggregate is the shared annual pool. A sublimit caps a particular coverage within it, unless stated otherwise."
**Replace with:** "The aggregate is the shared annual pool. A sublimit caps one coverage and, unless stated otherwise, is part of it."
**Why:** "unless stated otherwise" had nothing clear to attach to; now it plainly covers the outside-the-aggregate exceptions (A, pre-incident assistance).

### G-4 · Page 3 · How to read this policy, last line
**Current:** "This guide helps you find and understand the policy. It does not change coverage."
**Replace with:** "" (delete)
**Why:** Meta-commentary that 11.6 already covers once G-30 adds "examples" to it.

### A-1 · Error · Pages 4–7 · Declarations page footers
**Problem:** The Declarations are form CORG-CY-0201 (the page 4 header and Item 12 both say so), but every Declarations page footer prints the policy-form number CORG-CY-0200. A real forms-control reviewer would reject this: the pages show the wrong form number.
**Current:** "Corgi Insurance Company, Inc. | CORG-CY-0201 (10/26)" (p. 4 header) … footer on pp. 4, 5, 6, 7: "CORG-CY-0200 (10/26)"
**Fix:** On pages 4–7 only, change the footer to "CORG-CY-0201 (10/26)". Leave pages 1–3 and 8–37 as CORG-CY-0200.

### F-5 · Page 4 · Item 4, note under table
**Current:** "Reports through a channel listed in Item 4, including a hotline call, count as notice even if we have not acknowledged them. Report as soon as possible, and meet any legally required notice deadline. Telling a monitoring provider is not notice to us unless the report reaches an Item 4 channel."
**Replace with:** "A report through any channel above, including a hotline call, is notice even if we have not acknowledged it. Report as soon as possible and meet any legal notice deadline. Telling a monitoring provider is not notice unless the report reaches one of these channels."
**Why:** The note sits inside Item 4, so repeating "a channel listed in Item 4" and "an Item 4 channel" reads like it was written to stand alone.

### A-23 · Minor · Page 4 · Name of pre-incident service
**Problem:** Item 5 is the only place that calls it "help". Item 6, Section II, VII 2.3 and VII 6.2 all say "pre-incident assistance".
**Current:** "Pre-incident help, outside the aggregate"
**Fix:** "Pre-incident assistance, outside the aggregate"

### F-7 · Page 4 · Item 5, "One annual pool" note
**Current:** "No amount is reserved for any one coverage. A $600,000 insurer payment leaves $1,400,000. A $250,000 sublimit is part of this pool, not extra money. A payment uses up both the relevant sublimit and the annual pool."
**Replace with:** "No amount is reserved for any one coverage: a $600,000 payment leaves $1,400,000 for everything else. A $250,000 sublimit is part of this pool, not extra money; a payment under it reduces both."
**Why:** Joins the example to the point it proves, and removes the separate sentence that repeated "sublimit" and "pool".

### F-8 · Page 5 · Item 6, intro paragraph
**Current:** "Where a waiting period replaces the dollar retention, loss during those hours is not covered. Section III, part 1 explains how one retention applies to an incident."
**Replace with:** "Where a waiting period replaces the dollar retention, loss during the wait is not covered. Under Section III, part 1, one dollar retention applies to each incident."
**Why:** "Those hours" is wrong for N's 14-day wait. The cross-reference now states the rule instead of only pointing to it.

### F-9 · Page 5 · Item 7, row D
**Current:** "Security failure: policy aggregate. Accidental system failure: $250,000 shared with F, unless the aggregate is selected. / 8-hour wait; no dollar retention"
**Replace with:** "Security failure: policy aggregate. Accidental system failure: $250,000 shared with F. / 8-hour wait; no dollar retention"
**Why:** The Declarations should show the actual choice. System Failure Full Limit is not selected (page 6), so the hypothetical "unless" clause is noise, and it used a third name for the option.

### F-10 · Page 5 · Item 7, row F
**Current:** "Security failure: policy aggregate. Accidental system failure: $250,000 shared with D, unless the aggregate is selected. / Item 6 retention"
**Replace with:** "Security failure: policy aggregate. Accidental system failure: $250,000 shared with D. / Item 6 retention"
**Why:** Same as row D.

### F-11 · Page 5 · Item 7, row G
**Current:** "$25,000 / Ordinary Item 6 retention; same-incident credit"
**Replace with:** "$25,000 / Item 6 retention, applied once per incident"
**Why:** "Same-incident credit" is a term the policy never defines. The new text says what it means: retention already paid for that incident counts.

### G-27 · Page 5 · Item 7, row H
**Current:** "$250,000 selected. / Item 6 retention; $2,500 if reported within 72 hours"
**Replace with:** "$250,000 / Item 6 retention; $2,500 if reported within 72 hours"
**Why:** A stray "selected." Other rows state only the limit.

### F-12 · Page 6 · Optional extensions, note under table
**Current:** "Both limits are part of the policy aggregate. P has its own cap, separate from the accidental-system-failure cap shared by D and F. Section I explains when each coverage applies and what it pays."
**Replace with:** "Both limits are part of the policy aggregate. Section I explains when each coverage applies and what it pays."
**Why:** The P row already says "separate from the shared D/F cap", so the middle sentence says it a second time.

### G-28 · Page 6 · Declarations subheading
**Current:** "Limit choices for existing cover"
**Replace with:** "Limit choices for core cover"
**Why:** "existing" implies prior insurance.

### F-14 · Page 6 · Limit choices block, note
**Current:** "Item 7 sets H's limit. The D/F full-limit option is not selected. These choices leave the policy aggregate and P unchanged."
**Replace with:** "System Failure Full Limit (Section I, part 4) is not selected. These choices do not change the policy aggregate or P."
**Why:** Removes "Item 7 sets..." inside Item 7, and gives the option one name everywhere instead of "D/F full-limit option".

### F-15 · Page 6 · Security controls and claims
**Current:** "A missing or failed security or payment control does not, by itself, reduce an otherwise covered payment. Section III, part 3 explains this rule. Section VII, part 3 explains how application errors and deliberate misstatements are handled. The selected limits, retentions, waiting periods and other policy terms still apply."
**Replace with:** "A missing or failed security or payment control does not, by itself, reduce an otherwise covered payment (Section III, part 3). Application errors and deliberate misstatements are handled under Section VII, part 3. Limits, retentions, waiting periods and other terms still apply."
**Why:** Turns the two "Section X explains..." sentences into short references and cuts the paragraph by about a quarter.

### A-24 · Minor · Page 7 · Item 8 name for Coverage P
**Problem:** The coverage name differs from Item 7 and Section I ("Accidental technology-provider outage").
**Current:** "Selected extension P: accidental provider outage"
**Fix:** "P. Accidental technology-provider outage"

### G-25 · Page 7 · Item 8 table, third row
**Current:** "Taxes, surcharges and fees (assumed)"
**Replace with:** "Terrorism (TRIA), taxes and fees"
**Why:** The TRIA notice says the terrorism premium "is shown in Item 8", but no row shows it.

### G-37 · Page 7 · Item 12 table, row 4
**Current:** "Terrorism Risk Insurance Act Disclosure (Legal notices, item 7)"
**Replace with:** "Terrorism Risk Insurance Act Disclosure (Legal notices, item 1)"
**Why:** Keeps the cross-reference correct after G-35.

### A-22 · Formatting · Pages 8–9 · Notices heading and numbering
**Problem:** "IMPORTANT NOTICES" is the only all-caps page-level heading (Contents: "Important notices"). Its numbering 1–6 then continues as 7–8 under a separate "Legal notices" heading, and an unnumbered callout sits above item 7.
**Current:** "IMPORTANT NOTICES" … "7. Terrorism Risk Insurance Act disclosure" … "8. Fraud warning (Colorado)."
**Fix:** "Important notices". Renumber the Legal notices "1." and "2.", and change the Item 12 reference to "(Legal notices, item 1)". Move the 80% callout below the TRIA paragraph.

---

### G-21 · Page 8 · Important notice 2
**Current:** "Two timing rules generally apply:"
**Replace with:** "Two timing rules apply:"
**Why:** A hedge inside the claims-made notice weakens the one notice regulators care about.

### F-16 · Page 8 · Important notices, 3
**Current:** "Claim expenses, including covered legal fees, count toward your retention, the amount you pay. Payments we make for those expenses reduce the limit available for settlements and other covered payments. They can use it up completely."
**Replace with:** "Claim expenses, including covered legal fees, count toward your retention. Our payments for them reduce, and can use up, the limit available for settlements and other covered payments."
**Why:** Three sentences become two, and the gloss on "retention" (already explained on pages 3 and 5) is removed.

### G-9 · Page 9 · Legal notices, callout above TRIA
**Current:** "The 80% figure below concerns government reimbursement to the insurer. It does not set your claim payment percentage. Your payment follows the policy terms, including the program cap described below."
**Replace with:** "" (delete)
**Why:** A gloss on a statutory disclosure. Regulators expect the TRIA notice as written, and the explainer reads as machine over-explaining.

### G-35 · Page 9 · Legal notices numbering
**Current:** "7. Terrorism Risk Insurance Act disclosure"
**Replace with:** "1. Terrorism Risk Insurance Act disclosure"
**Why:** The numbering continues from the previous page's Important notices even though the page has a new title.

### G-36 · Page 9 · Legal notices numbering
**Current:** "8. Fraud warning (Colorado)."
**Replace with:** "2. Fraud warning (Colorado)."
**Why:** Same as G-35.

### F-17 · Page 10 · When coverage applies, condition 1
**Current:** "For Coverage A, an actual or suspected incident, and for Coverage B, an actual or reasonably suspected incident, meets this requirement, even if an investigation later shows that none happened. For the shutdown cover in Section I, part 3.3, a reasonably suspected security failure also qualifies even if none occurred."
**Replace with:** "A suspected incident also qualifies, even if none happened: any suspected incident for Coverage A, a reasonably suspected one for Coverage B, and a reasonably suspected security failure for the shutdown cover in Section I, part 3.3."
**Why:** The original put the subject far from its verb ("For Coverage A, an actual..., and for Coverage B, ..., meets"). Now there is one rule followed by the three cases.

### G-10 · Page 10 · Section I, "Terms that apply to every coverage"
**Current:** "Artificial intelligence. Using artificial intelligence, machine learning or synthetic media (including deepfakes) to cause, carry out or detect an incident or claim does not, by itself, exclude it."
**Replace with:** "Artificial intelligence. We do not exclude an incident or claim because AI, machine learning or deepfakes were used to cause or detect it."
**Why:** Active voice, and it removes the "does not, by itself" tic, which appears three times in the document.

### F-18 · Page 10 · Terms that apply to every coverage, final paragraph
**Current:** "The limits in Section II, retentions in Section III, defense and settlement rules in Section IV, and the definitions, exclusions, conditions and listed endorsements apply to the coverages below. Each group includes its operating rules; the common liability rules are in Section IV. Optional extensions apply only if purchased in Item 7."
**Replace with:** "Sections II to VII and any listed endorsements apply to the coverages below. Each group of coverages is followed by its operating rules."
**Why:** Section IV was named twice, and the last sentence repeats the first paragraph on this page ("P and Q apply only if purchased in Item 7").

### F-19 · Page 11 · Coverage B, Special conditions
**Current:** "Costs must generally be incurred within 12 months. Monitoring and identity-restoration services arranged within that window may continue for their covered term. Legally required notices need no consent; voluntary notices do. Section I, part 1.4."
**Replace with:** "Costs must be incurred within 12 months, but monitoring and identity-restoration services arranged in that window continue for their covered term. Legally required notices need no consent; voluntary notices do. Section I, parts 1.4-1.5."
**Why:** "Generally" and "may" were standing in for the exception, which the sentence now states. The reference now also points to 1.5, the notice rule.

### G-11 · Page 11 · Operating rule 1.2
**Current:** "Where appropriate, the breach coach hires forensic experts to support legal advice. This does not guarantee that their work is legally privileged; that depends on the facts and the law."
**Replace with:** "The breach coach may hire forensic experts to support legal advice. Privilege is not guaranteed."
**Why:** A hedge ("Where appropriate") plus a disclaimer that explains itself.

### F-20 · Page 12 · Operating rule 2.2
**Current:** "2.2. Assess the threat together. Together, we will consider"
**Replace with:** "2.2. Assess the threat together. We will consider"
**Why:** Removes the "together. Together" echo.

### G-13 · Page 13 · Section I part 3, outage guide intro
**Current:** "Outage guide. Use this table to find the relevant coverage below. It does not change coverage. Every limit shown is part of the shared policy aggregate."
**Replace with:** "Outage guide. Every limit shown is part of the policy aggregate."
**Why:** Removes navigation filler and a meta-disclaimer.

### F-21 · Page 13 · Outage guide table, row 2
**Current:** "D / $250,000 shared with F, unless the aggregate is selected"
**Replace with:** "D / $250,000 shared with F; see System Failure Full Limit"
**Why:** Uses the option's one name (and can link to it) instead of "unless the aggregate is selected".

### F-22 · Page 13 · Outage guide, note under table
**Current:** "Your cloud accounts are the accounts, settings and data you control. If only the provider's service is unavailable, E or P applies. An attack that reaches your cloud accounts can trigger coverage for your own systems. Section V's definition of computer systems explains the distinction."
**Replace with:** "Your cloud accounts (the accounts, settings and data you control) are part of your computer systems (Section V), so an attack that reaches them is treated as affecting your own systems. If only the provider's service is unavailable, E or P applies."
**Why:** The line between D and E/P was split over four sentences, ending with "can trigger". The definition of computer systems (12a) includes your cloud accounts, so it can be stated as a rule.

### F-23 · Page 13 · Coverage D, Limit and your share
**Current:** "For a system failure, $250,000 shared by D and F, unless Item 7 selects the aggregate. An 8-hour waiting period applies instead of a dollar retention."
**Replace with:** "For a system failure, $250,000 shared by D and F, unless System Failure Full Limit is selected. An 8-hour waiting period applies, with no retention."
**Why:** One name for the option. The second sentence is shortened, following P's "applies, with no dollar retention", so the longer option name fits in the same length.

### F-24 · Page 14 · Coverage P, Special conditions
**Current:** "This is the accidental technology-provider outage extension selected in Item 7."
**Replace with:** "Applies only if purchased in Item 7."
**Why:** The original restates the heading. The point that matters is that P needs to be purchased, which is also how Section I's intro puts it.

### F-25 · Page 14 · Operating rule 3.3
**Current:** "We treat the resulting interruption as caused by that security failure under Coverage D or E, as applicable. This applies if you act on advice from our incident response team, a government agency or a dependent provider, or use your own reasonable judgment. If no security failure occurred, the covered interruption window is at most 72 hours from shutdown, including the unpaid waiting period."
**Replace with:** "If you act on advice from our incident response team, a government agency or a dependent provider, or on your own reasonable judgment, we treat the resulting interruption as caused by that security failure under Coverage D or E, as applicable. If no security failure occurred, cover is limited to 72 hours from shutdown, including the unpaid waiting period."
**Why:** Puts the condition before the result it controls, and replaces "covered interruption window" with plain words. The condition itself is unchanged.

### F-26 · Page 14 · Operating rule 3.4
**Current:** "Each of D, E and P has its own wait in Item 7. Its clock starts when an interruption qualifying under that coverage begins. Interrupted hours from the same incident add up for that coverage; simultaneous outages count once. Another affected system or provider does not restart that coverage's wait. Qualifying hours under different coverages may run concurrently, but completing one wait does not satisfy another. Business income loss and extra expense incurred during the applicable wait are not covered."
**Replace with:** "D, E and P each have their own waiting period in Item 7. It starts when an interruption that qualifies under that coverage begins. Within each coverage, interrupted hours from the same incident add up, overlapping hours count once, and a further affected system or provider does not restart the wait. Waiting periods under different coverages can run at the same time, but meeting one does not meet another. We do not pay business income loss or extra expense incurred during a waiting period."
**Why:** Uses the defined term "waiting period" instead of "wait"/"clock". The three same-coverage rules become one list, and "run concurrently"/"satisfy" become plain words. Keep the existing paragraph break before "Waiting periods under different coverages".

### F-27 · Page 15 · Coverage F, Limit and your share
**Current:** "For a system failure, the $250,000 limit shared with Coverage D, unless Item 7 selects the aggregate."
**Replace with:** "For a system failure, $250,000 shared with Coverage D, unless System Failure Full Limit is selected."
**Why:** One name for the option, matching D.

### F-28 · Page 15 · Coverage G, Limit and your share
**Current:** "$25,000 (Item 7), subject to the ordinary dollar retention in Item 6. Amounts paid toward another dollar retention for the same incident count toward it. H's reduced retention applies only to H; an interruption waiting period does not replace G's dollar retention."
**Replace with:** "$25,000 (Item 7), after the ordinary retention (Item 6). Anything already paid toward a dollar retention for the same incident counts toward it. Neither H's reduced retention nor an interruption waiting period replaces it."
**Why:** Uses the "after the retention (Item 6)" pattern from the other coverages, and puts the two exceptions (H's reduced retention, waiting periods) in one sentence.

### F-29 · Page 15 · System Failure Full Limit block
**Current:** "Selecting the policy aggregate for accidental system failure under D and F raises their shared $250,000 cap to the amount left in the aggregate. It adds no separate money. The events covered, payments, D waiting period and F retention stay the same. Coverage P is unchanged."
**Replace with:** "This option raises the $250,000 system failure cap shared by D and F to the amount left in the policy aggregate. It adds no money. What D and F cover and pay, the D waiting period, the F retention and Coverage P do not change."
**Why:** Describes the option without a fourth name for it ("selecting the policy aggregate"), relies on the heading for "only if selected", and joins the two "stays the same" sentences.

### F-30 · Page 16 · Operating rule 5.3
**Current:** "The recovery-cost and reimbursement order in Section VII, part 10.2 applies to all money recovered after we pay."
**Replace with:** "Money recovered after we pay is applied in the order set out in Section VII, part 10.2."
**Why:** Removes the stacked noun phrase "recovery-cost and reimbursement order".

### B-1 · Page 19 · Operating rules for M, N and O, 7.1
**Current:** "We pay for equivalent hardware if repair is not reasonably possible, or replacement costs no more than repair. M pays for replacement, not physical repair."
**Replace with:** "We pay for equivalent hardware if repair is not reasonably possible or would cost at least as much as replacing it. M does not pay for physical repair."
**Why:** "replacement costs no more than repair" reads at first as the defined term "computer replacement costs" and puts the comparison back to front; the second sentence repeated the first. (The same phrase appears in Coverage M on p.18; that belongs to the front-half reviewer.)

### B-2 · Page 19 · Section II, part 1, second paragraph
**Current:** "A limit described as shared with another coverage is shared by the named coverages for that type of loss. For example, the system failure cap covers business income loss, extra expense and restoration costs caused by a system failure under D and F combined. P has its own limit, which this cap does not reduce."
**Replace with:** "A shared limit is a single amount for all the coverages it names, for that type of loss. For example, the system failure cap covers business income loss, extra expense and restoration costs caused by a system failure under D and F combined. P has its own limit, separate from this cap."
**Why:** The opening sentence defined "shared" with "shared"; the last line now uses the Declarations' own wording ("separate from the shared D/F").

### G-16 · Page 19 · Section II example box
**Current:** "Assumes one fully covered claim, no earlier payments, and no other sublimit or payment-sharing rule applies. This illustration does not change the policy."
**Replace with:** "Assumes one covered claim and no earlier payments."
**Why:** Stacked assumptions plus a meta-disclaimer. 11.6 covers examples once G-30 is applied.

### B-3 · Page 20 · Section II, part 3, first paragraph, last sentence
**Current:** "This payment uses up the aggregate, but not the limit of the coverage it supports."
**Replace with:** "This fee reduces the aggregate, but not the limit of the coverage it supports."
**Why:** "Uses up the aggregate" sounds like it exhausts the whole aggregate; "reduces" is what is meant.

### B-4 · Page 20 · Section II, part 3, second paragraph
**Current:** "The fee follows the supported coverage's retention rules and creates no additional dollar retention. Fees supporting an interruption are eligible only if that interruption exceeds its waiting period; reasonable documentation fees may be incurred during the wait. Allocate fees supporting different coverages by the work performed."
**Replace with:** "The fee follows the retention rules of the coverage it supports and adds no dollar retention of its own. For an interruption, we pay it only if the interruption outlasts its waiting period, including reasonable fees incurred during the wait. If the work supports several coverages, we split the fee by the work done for each."
**Why:** Says who pays and when in active voice; the semicolon clause ("may be incurred during the wait") left it unclear whether those fees are paid; the bare imperative "Allocate" had no subject.

### B-8 · Page 20 · Section II, part 4 (layout)
**Current:** "4. Costs that fit more than one coverage."
**Replace with:** "4. Costs that fit more than one coverage. [no text change: indent part 4 and its three follow-on paragraphs to match parts 1-3]"
**Why:** Formatting fix only; wording unchanged.

### B-5 · Page 20 · Section II, part 4, first paragraph
**Current:** "We pay each item of cost only once. We reasonably allocate mixed invoices according to the services performed and apply the relevant limit and retention to each allocated item. We do not apply a lower limit merely because an item also fits another coverage."
**Replace with:** "We pay each cost only once. If one invoice covers services under different coverages, we split it reasonably by service and apply each coverage's limit and retention to its share. We do not apply a lower limit just because a cost also fits another coverage."
**Why:** "Mixed invoices" and "allocated item" are claims-department jargon; the rewrite says what a mixed invoice is and what happens to it.

### B-6 · Page 20 · Section II, part 4, second paragraph
**Current:** "If the same service qualifies under both A and B, we apply A first, up to its remaining per-incident and annual limits. Otherwise eligible B costs remain covered whether or not A is available or exhausted. No amount is charged to both benefits."
**Replace with:** "If a service qualifies under both A and B, we pay it under A first, up to A's remaining per-incident and annual limits. Costs that qualify under B stay covered under B even if A is unavailable or used up. Nothing is paid under both."
**Why:** "Otherwise eligible B costs" and "charged to both benefits" read twice; "benefits" is not the policy's word for coverages.

### B-7 · Page 20 · Section II, part 4, third paragraph
**Current:** "Physical hardware replacement costs qualify only under M, not as restoration costs or extra expense, except for security improvement costs covered under G. This does not bar otherwise covered software or firmware restoration under F, or temporary equipment rental as extra expense."
**Replace with:** "Replacing physical hardware is covered only under M, or under G as a security improvement cost. It is not a restoration cost or extra expense. This does not affect restoring software or firmware under F, or renting temporary equipment as extra expense."
**Why:** The G exception sat at the end of a sentence after the "not" list, so it read as an exception to the wrong thing; the rewrite states the rule, then the carve-outs.

### B-9 · Page 21 · Section III, part 1 (numbering)
**Current:** "1. One retention per incident. 1. One dollar retention applies"
**Replace with:** "1. One retention per incident. 1.1. One dollar retention applies [and renumber the next three sub-items 1.2, 1.3, 1.4]"
**Why:** Formatting fix only; wording unchanged.

### B-10 · Page 21 · Section III, part 1, sub-item 2
**Current:** "Business interruption has the waiting period instead of a dollar retention, and reputational harm has the reputational harm waiting period in Item 7."
**Replace with:** "Business interruption and reputational harm use their waiting periods in Item 7 instead of a dollar retention."
**Why:** One rule stated once instead of twice with "reputational harm" three times.

### G-18 · Page 21 · III.3 Security controls, opening
**Current:** "We use your security and payment-control answers to assess the insurance application. They are not a promise that those controls will always work."
**Replace with:** "Your security answers describe your controls; they are not a warranty that the controls will work."
**Why:** "Warranty" is the term of art a reviewer expects. The "not a promise" phrasing is conversational.

### G-32 · Page 22 · Section IV heading (and Contents)
**Current:** "IV. Defense & Settlement of Claims"
**Replace with:** "IV. Defense and Settlement"
**Why:** Removes the ampersand from a contract heading. Set the Contents entry to the same words.

### B-11 · Page 22 · Section IV, part 2, retention paragraph
**Current:** "Apply the dollar retention once, first to part (a) and then, if any retention remains, to part (b). We pay what remains in part (a), plus 70% of what remains in part (b). You pay the retention and 30% of the amount left in part (b). Costs used to meet the retention are not also subject to that 30% share. Amounts already applied to the retention or paid by us count once."
**Replace with:** "We apply the dollar retention once: first to part (a), then any remainder to part (b). We pay the rest of part (a) and 70% of the rest of part (b). You pay the retention and the other 30% of the rest of part (b). No cost counts twice, whether it went toward the retention or was paid by us."
**Why:** Two anti-double-counting sentences say the same thing; "what remains"/"the amount left" alternate for one idea. The worked example below still checks out ($14,000 / $16,000).

### B-12 · Page 22 · Section IV, part 5
**Current:** "We pay regulatory penalties only where insurance is allowed under their definition. We pay punitive damages only as the definition of damages allows."
**Replace with:** "We pay regulatory penalties and punitive damages only where the law allows them to be insured, as the definitions in Section V set out."
**Why:** "Where insurance is allowed under their definition" suggests the definition, not the law, permits insurance; one sentence covers both.

### G-19 · Page 23 · Section V preamble
**Current:** "Bold terms in the body text, including the Declarations, have the meanings below. The definitions apply wherever these terms appear. Headings and repeated labels help you find information."
**Replace with:** "Bold terms in this policy and the Declarations, singular or plural, have the meanings below."
**Why:** Removes two filler sentences and adds the standard singular/plural rule.

### B-13 · Page 23 · Definition 4, lead-in
**Current:** "within 12 months after you discover a security failure or privacy event or, for one that is only suspected, within 12 months after you report it to us. Section VII, part 2.2 explains when you need our consent. The timing exception for monitoring and identity-restoration services in Section I, part 1.4 also applies."
**Replace with:** "within 12 months after you discover a security failure or privacy event, or after you report it to us if it is only suspected. Section VII, part 2.2 explains when you need our consent; Section I, part 1.4 lets monitoring and identity-restoration services run past that window."
**Why:** Removes the repeated "within 12 months" and says what the 1.4 "timing exception" actually does, so the reader need not flip back.

### B-14 · Page 23 · Definition 5, paragraph a
**Current:** "Treat that expected net loss as a negative amount when adding the continuing expenses in paragraph b; and"
**Replace with:** "An expected net loss counts as a negative amount when added to paragraph b; and"
**Why:** Shorter, same instruction; "the continuing expenses in paragraph b" repeats paragraph b's own text.

### B-17 · Page 23 · Definition 5 (layout)
**Current:** "b. normal operating expenses, including payroll, that must continue during the interruption."
**Replace with:** "b. normal operating expenses, including payroll, that must continue during the interruption. [no text change: indent b to match a; set the two follow-on paragraphs flush with the definition text, not as hanging indents. Same outdent problem on the closing paragraphs of Definitions 6, 10, 12, 15 and 17 and on Definition 17's items a-b]"
**Why:** Formatting fix only; wording unchanged.

### B-15 · Page 23 · Definition 5, first follow-on paragraph
**Current:** "From the total in paragraphs a and b, subtract revenue actually earned during the interruption, less the expenses incurred to earn it that are not already included in paragraph b."
**Replace with:** "From the total of paragraphs a and b, subtract what you actually earned during the interruption: revenue, less the costs of earning it not already in paragraph b."
**Why:** "Subtract X, less Y" stacks two minus signs in one clause; naming the result first ("what you actually earned") makes the arithmetic readable.

### B-16 · Page 23 · Definition 5, delayed-work paragraph
**Current:** "Also subtract the net benefit of delayed work completed later, but only to the extent not already reflected in the actual-revenue deduction above. Allow for additional completion costs and net income from other work displaced. Costs paid as extra expense cannot also reduce that deduction. Do not deduct saved expenses already excluded from paragraph b. Minimum loss: zero."
**Replace with:** "Also subtract the net benefit of delayed work you complete later, except to the extent the deduction above already counts it. The benefit allows for extra costs to finish the work and net income lost on other work it displaced, but not for costs paid as extra expense. Do not deduct saved expenses that paragraph b already leaves out. Minimum loss: zero."
**Why:** The hot spot: the two loose follow-up sentences are folded into one, making it clear the completion-cost and displaced-work allowances reduce the benefit, while extra-expense costs cannot.

### B-18 · Page 25 · Definition 12, closing paragraph
**Current:** "If an attack on dependent systems gives someone unauthorized access to your cloud accounts, or damages, encrypts or exposes data in them, it is a security failure affecting your computer systems under every coverage. An interruption caused only because a dependent provider's service is unavailable to you, other than one caused by a security failure in your own computer systems, falls under Coverage E (or, for a system failure, Coverage P if purchased), not Coverage D."
**Replace with:** "If an attack on dependent systems gives someone unauthorized access to your cloud accounts, or damages, encrypts or exposes data in them, the attack counts as a security failure affecting your computer systems under every coverage. An interruption caused only by a dependent provider's service being unavailable to you, and not by a security failure in your own computer systems, falls under Coverage E (or Coverage P, if purchased, for a system failure), not Coverage D."
**Why:** "Caused only because ..., other than one caused by ..." contradicts itself on first read; "it" had no clear antecedent.

### B-19 · Page 25 · Definition 16, paragraph d (numbering)
**Current:** "except: (a) amounts you would have owed anyway; (b) amounts you owe under a contract duty"
**Replace with:** "except: (i) amounts you would have owed anyway; (ii) amounts you owe under a contract duty [and (c) PCI fines -> (iii) PCI fines]"
**Why:** Formatting fix only; wording unchanged.

### B-20 · Page 28 · Definition 37, opening
**Current:** "means deliberate deception through any means of communication, including email, text, messaging app, letter, phone or video call, and synthetic or deepfake audio or video. The person carrying out the deception must not be your current owner, partner, member, officer, employee or individual independent contractor (even if not acting for you at the time), or be acting in collusion with one of them. They must pretend to be, or to act for, you, an executive, employee, client, vendor, financial institution or another person you deal with, or falsely claim that genuine payment or bank details have changed. The deception must:"
**Replace with:** "means deliberate deception, through any means of communication (including email, text, messaging app, letter, phone or video call, and synthetic or deepfake audio or video), by someone who pretends to be, or to act for, you, an executive, employee, client, vendor, financial institution or another person you deal with, or who falsely claims that genuine payment or bank details have changed. The deceiver must not be your current owner, partner, member, officer, employee or individual independent contractor (even if not acting for you at the time), or be acting in collusion with one of them. The deception must:"
**Why:** Says what payment fraud is (impersonation or a fake change of bank details) before who is excluded; the old order made the reader hold the exclusion before learning the test.

### B-21 · Page 29 · Definition 45
**Current:** "where insurable under the law shown in Item 11 of the Declarations, or of the place where the regulatory proceeding is brought, whichever allows it."
**Replace with:** "where insurable under either the law shown in Item 11 of the Declarations or the law of the place where the regulatory proceeding is brought."
**Why:** "Or of the place..., whichever allows it" is an elliptical construction; "either" states the same most-favourable-law rule directly.

### A-26 · Minor · Page 29 · Definition of retention cites Items 6 and 7
**Problem:** Item 7 shows no retention amounts apart from repeating H's $2,500. Item 6 is where retentions are set.
**Current:** "the dollar amount shown in Items 6 and 7 of the Declarations"
**Fix:** "the dollar amount shown in Item 6 of the Declarations"

### B-22 · Page 30 · Definition 56, third and fourth paragraphs
**Current:** "It does not include planned downtime, or a failure of electricity, water, gas or other utilities, telecommunications, satellites or public internet infrastructure that you do not operate (for Coverage P, that neither the dependent provider nor its hosting or cloud provider operates). For Coverage P, it means the same events affecting dependent systems."
**Replace with:** "It does not include planned downtime, or a failure of electricity, water, gas or other utilities, telecommunications, satellites or public internet infrastructure that you do not operate. For Coverage P, it means the same events affecting dependent systems, but excluding such a failure unless the dependent provider or its hosting or cloud provider operates it."
**Why:** Moves the Coverage P variation out of a mid-sentence parenthetical and into the paragraph that already handles Coverage P. (+8 characters, but page 30 ends about 250pt above the footer before the forced break to Section VI, so nothing moves.)

### B-23 · Page 31 · Section VI, introduction
**Current:** "Each exclusion applies as written. If an exception to an exclusion applies,"
**Replace with:** "If an exception to an exclusion applies,"
**Why:** Filler: every policy term applies as written; the sentence adds nothing and invites the reader to wonder what else it could mean.

### B-24 · Page 31 · Exclusion 2, lead-in
**Current:** "Known problems. This exclusion applies to any incident, claim or circumstance that:"
**Replace with:** "Known problems. Any incident, claim or circumstance that:"
**Why:** Matches the pattern of every other exclusion (heading, then the excluded matter).

### B-25 · Page 31 · Exclusion 2, second list
**Current:** "For this exclusion, a circumstance does not include: (a) a vulnerability, missing patch or other security weakness that, as far as any executive knew, had not been exploited; (b) anything disclosed in your application, unless the Declarations or an endorsement exclude it; or (c) an early warning that an investigation completed before the continuity date found was not an incident."
**Replace with:** "For this exclusion, a circumstance does not include: (i) a vulnerability, missing patch or other security weakness that, as far as any executive knew, had not been exploited; (ii) anything disclosed in your application, unless the Declarations or an endorsement exclude it; or (iii) an early warning found not to be an incident by an investigation completed before the continuity date."
**Why:** Two consecutive lists both labelled (a)-(c) make "exclusion 2(b)" ambiguous; item (iii) untangles a relative clause nested inside a relative clause. (The +3 characters are the roman numerals; item (iii) still wraps to two lines.)

### B-26 · Page 31 · Exclusion 4, third sentence
**Current:** "This exclusion applies only after a final, non-appealable ruling in the matter or in a separate proceeding, or the person's written admission, establishes the act."
**Replace with:** "This exclusion applies only once the act is established by a final, non-appealable ruling (in this or a separate proceeding) or the person's written admission."
**Why:** The verb "establishes" arrived 20 words after its subject; the reader had to go back to find what was being established.

### B-27 · Page 32 · Exclusion 15, part 1, last two sentences
**Current:** "In this exclusion, "state" means a sovereign country, and "government" means its national government. It never means a U.S. state."
**Replace with:** "In this exclusion, "state" means a sovereign country, never a U.S. state, and "government" means its national government."
**Why:** "It" followed "government", so the U.S.-state carve-out appeared to attach to the wrong word.

### A-29 · Minor · Page 33 · Contraction in an exclusion title
**Problem:** "weren't" is the only contraction in the policy's operative text.
**Current:** "19. Profits you weren't entitled to."
**Fix:** "19. Profits you were not entitled to."

### B-28 · Page 34 · Section VII, part 1.4, second paragraph
**Current:** "Every later claim arising from it or the same or related facts is treated as first made and reported on your report date. If you report after the policy period ends, we use its last day."
**Replace with:** "A later claim arising from what you reported, or from related facts, is treated as first made and reported on your report date (the policy period's last day if you report after it)."
**Why:** "It" pointed back across a paragraph break to either "your report" or "an incident"; "we use its last day" left "its" and "use" for the reader to decode. "The same facts" as the report is simply "what you reported", so it is not lost. Must not grow: this paragraph fills its third line exactly.

### B-29 · Page 34 · Section VII, part 2.3
**Current:** "If you have a security question before anything is suspected and before any early warning (such as whether an email is phishing, or whether a vendor's security terms are adequate), we will provide up to $2,500 per policy period of legal or forensic advice."
**Replace with:** "Before anything is suspected and before any early warning, we will provide up to $2,500 per policy period of legal or forensic advice on security questions, such as whether an email is phishing or a vendor's security terms are adequate."
**Why:** The examples were separated from "security question" by the timing condition, so they read as examples of early warnings.

### B-30 · Page 34 · Section VII, part 3.2, first paragraph, last sentence
**Current:** "Only answers to questions we asked in the application can count as an error or omission."
**Replace with:** "An error or omission can only be in an answer to a question we asked in the application."
**Why:** Puts the subject first; the original reads as if answers "count as" something else.

### B-31 · Page 34 · Section VII, part 3.2, second paragraph
**Current:** "A change takes effect only from the date we tell you in writing. It never applies to an incident already discovered or a claim already made."
**Replace with:** "Any change applies only from the date we tell you in writing, and never to an incident already discovered or a claim already made."
**Why:** One timing rule in one sentence.

### B-32 · Page 35 · Section VII, part 3.3, second paragraph
**Current:** "What one insured knows is not treated as knowledge of another insured. The exception is an executive's knowledge, which is treated as knowledge of the named insured."
**Replace with:** "What one insured knows is not treated as known by another, except that an executive's knowledge is treated as the named insured's."
**Why:** Rule and exception in one sentence; drops the "The exception is..." restart.

### B-33 · Page 35 · Section VII, part 5.4, first sentence
**Current:** "If this policy is cancelled or not renewed, then for 60 days after it ends, claims first made against you during those 60 days, arising from incidents, media wrongful acts or wrongful collection that first happened before this policy ended, are treated as made on the last day of the policy period."
**Replace with:** "If this policy is cancelled or not renewed, a claim first made against you within 60 days after it ends is treated as made on the last day of the policy period, if it arises from an incident, media wrongful act or wrongful collection that first happened before this policy ended."
**Why:** The 60 days were stated twice and the verb ("are treated") came after a 25-word interruption; the condition now follows the rule.

### B-34 · Page 35 · Section VII, part 5.5, second paragraph
**Current:** "The extension includes the automatic 60 days; it does not start after them."
**Replace with:** "It starts when the policy ends and includes the automatic 60 days."
**Why:** States the start date positively instead of by negation.

### A-28 · Minor · Page 36 · Heading promises benefits the text denies
**Problem:** The first sentence under the heading is "There is no automatic claim-free retention reduction."
**Current:** "6. RENEWAL BENEFITS"
**Fix:** "6. RENEWAL"

### G-33 · Page 36 · VII.7.1
**Current:** "we aim to have a member of our incident response team contact you within one hour of your report."
**Replace with:** "a member of our incident response team will contact you within one hour of your report."
**Why:** "aim" is marketing language in a contract. Make it a promise, or delete the sentence. 7.2 has the same issue.

### A-27 · Minor · Page 36 · VII 8.3 venue cites a choice-of-law item
**Problem:** Item 11 names the governing law, not a state for suit.
**Current:** "either of us may go to court in the state shown in Item 11 of the Declarations."
**Fix:** "either of us may go to court in the state whose law Item 11 names."

### B-35 · Page 37 · Section VII, part 10.2
**Current:** "First deduct reasonable costs of obtaining the recovery and reimburse whoever bore them. Do not deduct or reimburse the same cost twice, including costs we already paid under H. The remaining money first reimburses your retention and uninsured loss, then reimburses us."
**Replace with:** "A recovery first repays the reasonable costs of obtaining it, to whoever paid them, but no cost is repaid twice, including costs we already paid under H. What is left repays your retention and uninsured loss first, then us."
**Why:** Bare imperatives ("First deduct", "Do not deduct") with no one to address; the rewrite follows the money in order.

### G-30 · Page 37 · VII.11.6
**Current:** "Headings, the cover page and the "Reporting an incident" summary help you use the policy."
**Replace with:** "Headings, examples, the cover page and the reporting summary help you use the policy."
**Why:** One clause now covers every example and guide, so the scattered "does not change" lines can go.


## Part 3 — Formatting and styling instructions (13)

### A-4 · Inconsistency · Pages 5, 14, 18, 19, 21, 29, 30 · Waiting periods cited to Item 7 instead of Item 6
**Problem:** Item 6 is titled "Retention and waiting periods" and is the only item that lists every wait in one place. Seven operative passages cite Item 7 instead; Item 7 repeats the waits only inside its table rows. Other passages cite no item at all (D, E), and Def. 51 cites "Items 6 and 7". Def. 58 also defines a waiting period in "hours" for "business interruption coverage", but N's wait is 14 *days*, and Item 6 says "loss during those hours".
**Current:**
- P (p. 14): "longer than the waiting period in Item 7."
- 3.4 (p. 14): "Each of D, E and P has its own wait in Item 7."
- 7.2 (p. 19): "After the waiting period in Item 7, we pay lost net profit only."
- III 1.2 (p. 21): "reputational harm has the reputational harm waiting period in Item 7."
- Def. 51 (p. 29): "for reputational harm, the reputational harm waiting period in Item 7 applies instead."
- Def. 58 (p. 30): "Waiting period means the hours shown in Item 7 that an interruption must last before business interruption coverage begins."
- Item 6 (p. 5): "loss during those hours is not covered."
**Fix:** Change "Item 7" to "Item 6" in the first five quotes. Def. 58: "Waiting period means the time shown in Item 6 that an interruption must last before business interruption coverage begins." Item 6: "loss during that time is not covered." Leave the "(Item 7)" after "90 days" in Coverage N, because the 90-day period appears only in Item 7.

### A-12 · Inconsistency · Pages 15, 25, 28, 35 · Defined-term styling applied to verbs in operative text
**Problem:** Section V says "Bold terms in the body text … have the meanings below." Automatic bolding has made verbs into defined terms, so these passages literally read as the defined **damages** (judgments and settlements) or **claim** (a demand against you).
**Current:**
- F (p. 15): "A security failure or system failure **damages**, corrupts or deletes your digital assets"
- Def. 12 (p. 25): "or **damages**, encrypts or exposes data in them"
- Def. 37 (p. 28): "or falsely **claim** that genuine payment or bank details have changed"
- VII 3.4 (p. 35): "we will not deny or reduce coverage, or **claim** misrepresentation"
**Fix:** Remove bold and the definition link from these four words. No text change.

### A-13 · Inconsistency · Pages 9, 14 · TRIA disclosure presented as a separate form but printed inside the policy form
**Problem:** Item 12 lists CORG-IL-0001 as its own form, but the disclosure appears as "item 7" of Legal notices on a page footed CORG-CY-0200. The disclosure also says the terrorism premium "is shown in Item 8", but Item 8 has no terrorism line. The $0 appears only in the note beneath the table.
**Current:** "CORG-IL-0001 (10/26) | Terrorism Risk Insurance Act Disclosure (Legal notices, item 7)" / "The portion of your annual premium attributable to this coverage is shown in Item 8 of the Declarations."
**Fix:** Either print the TRIA text on its own page footed "CORG-IL-0001 (10/26)", or change the Item 12 title to "TRIA disclosure (printed in Legal notices)". In Item 8, rename the row "Taxes, surcharges and fees (assumed)" to "Terrorism (TRIA), taxes and fees (assumed)" so the premium is shown in the table.

### A-16 · Formatting · Pages 10, 19, 22 (vs Contents p. 2) · Section heading capitalization
**Problem:** Contents and every other section heading use sentence case, but three body headings (and their bookmarks) use title case, and one uses "&".
**Current:** "I. Insuring Agreements" / "II. Limits of Insurance" / "IV. Defense & Settlement of Claims"
**Fix:** "I. Insuring agreements" / "II. Limits of insurance" / "IV. Defense and settlement of claims"

### A-18 · Formatting · Pages 32–33 · Exclusion 15 internal numbering 1–5
**Problem:** Sub-parts "1."–"5." sit inside exclusion 15 in a list numbered 1–20, so "exclusion 2" and "part 2 of exclusion 15" look the same. Inside the exclusion, "Part (b)" and "unless (a) or (b) applies" refer to letters within sub-part 1.
**Current:** "1. What is excluded: …" … "5. Help continues while responsibility is being established." / "Part (b) does not apply" / "not excluded unless (a) or (b) applies."
**Fix:** Renumber the sub-parts "15.1."–"15.5."; "Part 15.1(b) does not apply"; "not excluded unless 15.1(a) or (b) applies."

### A-19 · Formatting · Pages 25, 31 · Repeated letter sequences in the same provision
**Problem:** Exclusion 2 uses (a)/(b) for the exclusion and then (a)/(b)/(c) again for the carve-outs. Def. 16(d) nests "(a) (b) (c)" inside the lettered list a–d. Both make citations ambiguous; "(a)" could mean either list.
**Current:** Excl. 2: "For this exclusion, a circumstance does not include: (a) a vulnerability … (b) anything disclosed … (c) an early warning …" / Def. 16d: "except: (a) amounts you would have owed anyway; (b) amounts … and (c) PCI fines"
**Fix:** Change both inner lists to (i), (ii), (iii).

### A-20 · Formatting · Pages 21–22, 31–35 · Run-in headings are only partly bold
**Problem:** Run-in headings in Sections II–IV, VI and VII are set in regular weight. Defined-term bolding then highlights random words inside them. In Section I, "When it applies." and similar labels are fully semibold.
**Current:** "1. One **retention** per **incident**." / "6. **Claims** between **insureds**." / "10. **Wrongful collection** and biometric laws." / "4. Mixed **claims**." / "1.2. Deadline for **claims**." / "1.3. Late notice of **incidents**."
**Fix:** Set every run-in heading, including all exclusion titles and VII part titles, fully semibold, as in Section I. No text change.

### A-21 · Formatting · Pages 6, 7, 8, 9, 14, 15, 30, 36, 37 · Definition styling on non-defined and quoted uses
**Problem:** Bolding and links to definitions appear inside statutory text and on colloquial or compound uses. This alters the mandated Colorado and TRIA wording and suggests meanings the policy does not intend.
**Current:** "civil **damages**" (CO fraud warning, p. 9); "the combined **insured** losses" (TRIA, p. 9); "your **claim** payment percentage" (p. 9); "exemplary damages to be **insured**" (Item 11, p. 7); "Security controls and **claims**" (p. 6); "**claims**-made", "our **incident** response panel", "application and **claims**" (p. 8); "pre-**incident** assistance" (pp. 5, 19, 34, 36); "our **incident** response team" (pp. 14, 15, 30, 36); "automatic **claim**-free" (p. 36); "a **claims** professional" (p. 36); "Reporting an **incident**" (p. 37)
**Fix:** Remove bold and the link from each listed occurrence. No text change.

### A-25 · Minor · Pages 5–6 · Stray text and self-reference inside Item 7
**Problem:** The H row ends with a stray "selected.", and Item 7 cites itself.
**Current:** "$250,000 selected. / Item 6 retention; …" / "Item 7 sets H's limit. The D/F full-limit option is not selected."
**Fix:** "$250,000 / Item 6 retention; …" / "The table above sets H's limit. The D/F full-limit option is not selected."

### A-30 · Minor · Various · Terms used like defined terms but not defined
**Problem:** "incident response team" (pp. 14, 15, 30, 36: G and Def. 54 depend on its written recommendation), "subsidiaries" (Def. 30), "policy aggregate" (defined only inside Item 7), "reputational harm waiting period" (Defs. 49, 51; III 1.2) and "a dependent provider's systems" (excl. 15.2, instead of the defined **dependent systems**).
**Current:** e.g. "our incident response team recommends in writing an upgrade" / "a dependent provider's systems, located outside the country"
**Fix:** Change "a dependent provider's systems" to "dependent systems". Change "incident response team" to "breach coach or panel forensic firm" in G, 4.3 and Def. 54, or add a one-line definition. Change "subsidiaries" in Def. 30 to "the companies in paragraph a".

### A-31 · Minor · Application p. 1 vs Declarations Item 1 · Subsidiaries answer
**Problem:** The application says "No subsidiaries seeking cover", which implies subsidiaries may exist. The Declarations say "no subsidiaries". Under Def. 30(a), any subsidiary owned over 50% is an insured whether or not it is "seeking cover".
**Current (application):** "No subsidiaries seeking cover."
**Fix:** "No subsidiaries."

### A-32 · Minor · Page 17 · Coverage K and Q do not point to Section IV
**Problem:** I, J and L end with "Section IV." but K and Q do not, although Section IV applies to "Coverages I, J, K, L and Q".
**Current:** "Special conditions. Chargebacks and ordinary processing fees are not covered." / "Special conditions. Biometric information is not covered."
**Fix:** Append " Section IV." to both.

---

### F-13 · Page 6 · Limit choices block, heading, column head and D/F row
**Current:** "Limit choices for existing cover Existing coverage Selected limit ... $250,000 shared cap; full limit not selected"
**Replace with:** "Limit options for core coverages | Coverage | Selected limit ... $250,000 shared cap; System Failure Full Limit not selected"
**Why:** "Existing cover" is unclear (existing compared with what?), and the row now uses the option's name from Section I. The right-hand cell has room (rendered page 6 checked). Along with F-6, this is one of only two edits that run longer.


## Part 4 — Optional: sample labels in the Declarations
The reviewer suggests removing sample wording from Item 8. I recommend keeping ONE clear sample disclaimer (the cover already has one), so these are optional.

### G-8 · Page 7 · Declarations, Item 8 note
**Current:** "All prices are exercise assumptions, not a quote. Taxes, fees and the included certified-terrorism premium are assumed to be $0. No payment is actually due; no insurance is issued."
**Replace with:** "Sample premium only (see cover). Certified-terrorism premium: $0."
**Why:** The third sample disclaimer. It also makes the TRIA premium disclosure explicit, which the page-9 notice relies on.

### G-23 · Page 7 · Item 8 table header
**Current:** "Illustrative amount"
**Replace with:** "Amount"
**Why:** The sample status is on the cover. A Declarations schedule should read as issued.

### G-24 · Page 7 · Item 8 table, last row
**Current:** "Total due for this sample"
**Replace with:** "Total annual premium"
**Why:** Same reason as G-23.


## Part 5 — Skipped as duplicates

- F-6 overlaps A-23 (kept A-23)
- G-1 overlaps F-1 (kept F-1)
- G-12 overlaps F-19 (kept F-19)
- G-14 overlaps F-28 (kept F-28)
- G-15 overlaps F-29 (kept F-29)
- G-17 overlaps B-6 (kept B-6)
- G-2 overlaps F-2 (kept F-2)
- G-20 overlaps B-23 (kept B-23)
- G-22 overlaps B-34 (kept B-34)
- G-26 overlaps F-11 (kept F-11)
- G-29 overlaps A-11 (kept A-11)
- G-34 overlaps A-29 (kept A-29)
- G-39 overlaps B-9 (kept B-9)
- G-5 overlaps F-7 (kept F-7)
- G-6 overlaps F-14 (kept F-14)
- G-7 overlaps F-15 (kept F-15)
- A-11: F-9/10/13/14/21/23/27/29 already unify the name as "System Failure Full Limit"
- A-17: same as B-9
- G-38: same as A-1
- G-39: same as B-9
- G-40: same as A-19
- G-41: same as A-18
- G-31: covered by A-4