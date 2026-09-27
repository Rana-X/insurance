# Changes since the first draft (September 27, 2026)

This log covers the changes from the first v2 draft PDFs to version 3. Three independent checks were run on the first draft:
- a market fact check (`Verification_Market_Claims.md`);
- a legal fact check (`Verification_Legal_Claims.md`);
- a coverage-counsel review (`Coverage_Counsel_QA_Review.md`).

A separate third-party review of the first draft PDFs, with a link test, was also folded in.

## Policy

| Change | Why | Source finding |
| --- | --- | --- |
| **Payment fraud** again requires impersonation by someone who isn't an insured | The broader wording paid ordinary commercial fraud and staff theft, which belong to crime insurance | QA C-1 |
| Claims-made reporting made consistent: firm 90-day claim deadline; lock-in for reported incidents deems claims made and reported on the report date (or the last day of the period); the automatic 60-day extended reporting period applies on cancellation or non-renewal | The earlier text could leave a reported incident with no responding policy | QA C-2 |
| Early warning: Coverages A and B trigger on an early warning or reported suspicion during the period; pre-inception warnings are no longer protected from exclusion 2; investigations that find nothing don't end a claim-free year | Trigger failure and an unintended grant | QA H-1, M-9 |
| Vendor-side attacks on the insured's cloud accounts are a security failure under every coverage; provider outages go to E or P | The short coverage list left D, I, N and O gaps | QA H-2 |
| Security causation rule is a threshold test ("only if we show"), not "to the extent"; states that credits and the claim-free reduction affect price | Avoids a proportional reading; "only three terms" was otherwise untrue | QA H-3 |
| Ransomware coinsurance keyed to whether backups were verified when the incident happened | Previously fixed at issue | QA M-2 |
| "Applies across coverages" limited to the coverages the label names; P keeps its own limit | Avoids folding P into the $250K system-failure cap | QA M-3 |
| **Dependent systems** include the vendor's own hosting provider | Fourth-party gap (for example, a tax platform hosted on a hyperscaler) | QA M-4 |
| System failure definition and exclusion 12 aligned (satellites; "you do not operate"; carve-back limited to security or system failures within a vendor's systems) | Mismatch and an accumulation leak | QA M-5 |
| Computer fraud item 2 narrowed to altered records in the insured's systems; mailbox-sent requests stay payment fraud; diverted wages are the insured's loss | The $100K floor could be avoided; payroll diversion was unclear | QA M-6 |
| **Extra expense** covers catch-up costs for 30 days after restoration | The main cost of an outage for a professional firm | QA M-7 |
| Punitive-damages rule uses the law in Item 11; Item 11 states the Colorado rule; regulatory penalties use Item 11 law or the forum's, whichever allows | Keeps the general form general; one insurability test | QA M-8; legal #21 |
| **Incident** includes key customer events and impersonation events when purchased | Coverage S could never trigger | QA M-10 |
| Cancellation limited to two of Colorado's grounds (non-payment, 10 days with reasons; knowingly false application, 45 days), by first-class mail. An honest mistake never cancels the policy; the insurer may only decline to renew. Renewal-change notice states terms, premium, changes and reasons | C.R.S. 10-4-109.7 and 10-4-110.5 | Legal #12–16; QA M-1; third-party review |
| Full TRIA disclosure; fraud-warning comma | Required notice text | Legal §3, #17 |
| War definition adds "revolution" and "whether or not war is declared" | Closer to LMA 5567 | Legal #47 |
| Declarations restructured under one heading; proof-of-loss help shown in Item 4; option R shows $1M also available; T and system-failure option shown without placeholders; waiting periods referenced to Item 6 | Formatting and consistency | QA L-1, L-3, L-7, L-12; third-party review |
| Smaller wording fixes: extortion-expense consent, claim-expense consent, settlement clause, exclusion 13, run-off for wrongful collection, advance cap, retention and reputational-harm waiting periods | Consistency | QA L-2, L-4 to L-9 |
| Hotline changed to a reserved fictional number, (303) 555-0142 | An 800-555 number may be real | Market #64 |

## Application

| Change | Source finding |
| --- | --- |
| Eligibility line; "deny or reduce"; realistic completion time; starred answers explained | QA L-11; third-party review |
| 7.1, 7.4 and 7.5 ask facts, not legal conclusions; Colorado Privacy Act thresholds stated correctly | Legal #24, #51; QA M-14 |
| 3.6 retention answer no longer attributes 7 years to the IRS | Market #9 |
| Underwriter page: Coverage R and P reasons corrected; scan finding moved to the public website; MDR waiting period wording | QA H-4, M-13, L-1, L-11 |

## Decision rationale

| Change | Source finding |
| --- | --- |
| Coalition $116K described as its all-policyholder average; At-Bay figures sourced to the full report | Market #24, #25 |
| CCH and Kronos identified as attacks (Coverage E); Atlassian 2022 used as the non-malicious example for P | Market #5; QA H-4 |
| Severe-event table counts catch-up costs, and says $2M covers all but the very top of the range | QA H-5 |
| Corgi described as showing a sample $2M aggregate / $1M per event policy | Third-party review; QA M-12 |
| "Other numbers, and why" table; exclusions row completed; option prices; the second million's load explained | QA M-11; nice-to-haves 4 and 5 |
| "Three claims, start to finish" added to part 8 | QA nice-to-have 1 |
| War exclusion credited to Y5381, LMA 5567 and Beazley accurately | Legal #46; Market #6 |
| SB 690, *Travelers v. ICS*, *Apache* and cancellation rows described precisely; *Lira* and CiCi sources added | Legal #3, #8, #14, #37 |
| Overclaims removed (legal review wording, "broader than" list, "every coverage maps to a row") | QA M-12 |
| Sources: issued policies labelled as publicly posted; AIG link replaced with Insurance Journal; CCH extension, Atlassian and CFC sources added; bare links made clickable | Third-party review; market check |

## Not changed (deliberate)

- No widespread-event cap on Coverage E. The $500K sublimit is the accumulation control (rationale part 3).
- Market checks couldn't open some items (for example, some At-Bay figures, the Beazley form number, Coalition carve-backs). These rely on the author's earlier reading of the full documents, and are cited to those documents.
- Before sending: recheck California SB 690 after September 30, 2026, and the CIRCIA final rule.
