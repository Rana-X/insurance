# 12. Harborline design spine: building the policy from first principles

Prepared September 27, 2026. This is the map for rewriting the three documents. It works through eight questions in order. Each answer:
- sets a piece of the policy;
- gives the reason for it;
- becomes one section of the decision rationale.

Anything in the policy that can't trace back to one of these answers gets cut.

**How to use it:**
- **Section 1** is the brief and how it's judged.
- **Section 2** is the one-sentence purpose.
- **Section 3** is the eight questions, with current answers and open decisions.
- **Section 4** is the story order for the rationale.
- **Section 5** is the work list, in order.
- **Section 6** lists your decisions.

Numbers marked *[estimate]* are judgment built on the data in reports 01, 03 and 11b. They are placeholders to check, not priced results.

---

## 1. The brief, and how it will be judged

**Task:** draft a cyber policy for a small-to-mid-sized business that looks and feels like a real policy. Plus a filled-in sample application, and a decision rationale. Deliver as PDF. **48 hours from the email.** "You may use AI, but do not submit an AI output."

| The brief asks for | Where it lives | Status |
| --- | --- | --- |
| Cover page, disclaimers, declarations | Policy: cover, important notices, Items 1–12 | Exists. Fix the notices (README T1-4, T1-5, T2-1i) |
| Insuring agreements, definitions, coverage sections, exclusions, conditions | Policy Sections I–V | Exists. Wording fixes in README Tier 2 |
| Reasonable assumptions (limits, deductibles, covered events) | Declarations; rationale | **Numbers exist; reasons mostly don't.** This document supplies them |
| Enough detail to work in practice | Claims promises, conditions, application-to-terms page | A strength |
| At least 3 external references, cited | Rationale; references file | Exists. Fix the Vouch figure and the stale Corgi framing (T1-1 to T1-3) |
| Sample application, filled in | Application | Exists. Fixes in README Tier 3 |
| Rationale: why these limits, why include or exclude, how definitions are built, trade-offs | Rationale | **Rebuild it around section 4 below** |

**What they score:**
1. **Clarity**: is it easy to understand?
2. **Judgment**: did you include the right details?
3. **Practicality**: could a real company use it?
4. **Resourcefulness**: did you use outside material intelligently?

They also say "how you think, what you prioritize, and how you execute." For a strategy role, the rationale is where you show all four. A first-principles chain, where every number traces to a reason, is the clearest way to show judgment.

---

## 2. The purpose, in one sentence

> **Harborline keeps a small business open and solvent after a cyber event. It pays the losses the business can't absorb, pays them fast enough to keep it running, and leaves the small, predictable costs with the business.**

The insurer's half of the same sentence: it can promise this only for risks it can price. That means guarding against three things:
- **moral hazard**: insuring or encouraging carelessness;
- **accumulation**: one event hitting every customer at once;
- **public policy**: covering what the law forbids.

Every restriction in the policy must name which of these it protects, or name one of two other reasons:
- "covered by another policy"; or
- "can't be priced yet".

---

## 3. The eight questions

### Q1. Who is it for, and what job does it do?

| | |
| --- | --- |
| **Answer** | US small and mid-sized businesses with $1M–$50M revenue, written on admitted paper under Colorado law. Office-based and professional firms first. The sample applicant is **Cedar Ridge Accounting Group**: a Denver CPA firm with $8.5M revenue and about 60 staff that runs payroll for 40 clients |
| **Why** | The brief says small-to-mid-sized. This band is where most firms have no standalone cyber cover (report 08). Corgi's new admitted carrier (Aug 26, 2026) targets main-street and professional-office businesses [snippet]. A CPA firm is a hard, realistic test: client money, tax data, seasonal peaks and shared cloud platforms |
| **The job** | Keep the firm running through a cyber event, and pay what would otherwise drain its cash |
| **In the policy** | Cover page ("who this is for"); eligibility in the application |
| **Status** | Solid. Fix the rationale's Corgi framing (T1-1) |

### Q2. How does this kind of firm actually lose money? (the loss map)

This is the foundation. Every coverage must map to a row, and every row should have a coverage or a stated reason why not.

| # | Loss path | How often (firms under $25M) | How much | Cedar Ridge twist | Covered by |
| --- | --- | --- | --- | --- | --- |
| L1 | **Payment fraud**: a fake invoice, spoofed partner or client email, bank impersonation, or an altered payroll batch | The most common claim. Business email compromise plus funds-transfer fraud are 58% of Coalition's claims; funds-transfer fraud alone is 27% [data via prior] | Average $141–208K [prior] | Moves client payroll. One diverted batch is $200–400K, which the firm may owe the client [estimate] | H (after the A3 fix) |
| L2 | **Ransomware, with downtime and restoration** | About 15% of claims [estimate from prior] | $269–422K on average for firms under $25M [prior] | Can tolerate about 1 day of downtime in tax season, 3 days otherwise (application 4.20). Revenue is about $34K a business day, higher from February to April [estimate] | C, D, F (plus A and B) |
| L3 | **Data breach: notification, credit monitoring, then lawsuits** | A breach needing notice hits 0.4–0.6% of firms a year [estimate]. There were 1,822 data-breach class actions in 2025, up 18% [data] | Response $50–250K; class action defense and settlement $0.3–1M+ [estimate] | Holds Social Security numbers for thousands of clients. CPA firms are in plaintiffs' pipelines [snippet] | B, I, J, K |
| L4 | **Vendor or cloud outage** (tax, payroll or email platform) | Frequent for short outages; multi-day ones are rare [data] | Lost fees and overtime | CCH (May 2019, 3–5 days) and Kronos (Dec 2021, weeks) are the outages CPA firms fear [snippet] | E (attacks on vendors); P (vendor system failure, optional) |
| L5 | **Own system failure**: a bad update or a failed server | Occasional | Usually small | — | D and F, capped at $250K |
| L6 | **Regulators** (FTC Safeguards Rule, state attorneys general) | Follows L3 | Defense $25–100K | Tax preparers are covered by the FTC Safeguards Rule | J |
| L7 | **Insider or rogue employee** | Rare | Varies | An IT lead with admin rights | Security failure carve-back (T2-11) |
| L8 | **AI-enabled attacks**: deepfake voice for payment fraud; hijacked AI agents | Rising; concern is high, losses so far small for SMBs [snippet] | Folds into L1 and L2 | Partner voice cloning in tax season | Through L1 and L2; AI-agent trigger |

**Status:**
- The map was never written down. **Add it to the rationale** as its first real section.
- Gaps it exposes:
  - L1's fraud paths (A3);
  - L4's cloud boundary (A10);
  - L3's client tax-identity follow-on (report 11, section 5).

### Q3. What can the firm pay itself without real harm? (the retention)

| | |
| --- | --- |
| **Current** | $7,500 per incident. $2,500 for fraud reported within 72 hours. Security credits cut it by 25% or 50%. A claim-free year reduces it by 25% |
| **Why this number** | 1. **Absorbable:** $7,500 is under a quarter of one day's revenue ($8.5M ÷ 250 business days ≈ $34K), about 0.09% of annual revenue [estimate]. 2. **Filters out small claims:** first-call help (Coverage A: 72 hours, $0 retention) handles minor events, so the retention only bites on real incidents. 3. **In the market band** for firms of this size (report 03's band table, README section 4.3). 4. **Rewards good security:** the credits give the firm a reason to adopt MFA, EDR and verified backups |
| **Rule for other firms** | Scale the retention with revenue using the band table, so every firm pays roughly the same share of a day's revenue |
| **In the policy** | Item 5; III.1.3 |
| **Status** | Number fine; **reasoning missing** from the rationale. Fix the credit arithmetic (T2-16) |

### Q4. What loss would sink the firm? (the limit)

**What Corgi does.** Corgi's startup cyber is sold "up to **$1M per claim / $2M aggregate**", claims-made, with defense inside the limits [snippet: corgi.insure]. That two-number format is the liability-market convention (general liability is sold as $1M per occurrence / $2M aggregate) for three reasons:
- **Contracts ask for it.** Client contracts and certificates of insurance are written in that language. Enterprise clients commonly require $2M–$5M [snippet].
- **It caps one bad event.** No single claim can take more than $1M, which protects the insurer.
- **It leaves room for a second event.** A firm hit once is about twice as likely to be hit again within two years (At-Bay) [prior].

**First principles for Cedar Ridge.** For a first-party-heavy small-business policy, the danger is usually **one severe event**, not two average ones. The severe but plausible single event for Cedar Ridge is ransomware with data theft in tax season [estimate; every line is judgment]:

| Cost | Range |
| --- | --- |
| Forensics, breach coach, negotiation | $100–150K |
| Restoration of systems and data | $100–200K |
| Lost income (about 10 business days in season, after the 8-hour wait) | $250–450K |
| Notification and credit monitoring for affected clients | $100–250K |
| Regulator defense (FTC or state attorney general) | $25–100K |
| **Subtotal without a lawsuit** | **about $0.6–1.2M** |
| Class action, a 25–35% chance after an SSN breach [estimate] | +$0.3–1M |
| **Severe total** | **about $0.9–2.2M** |

**What that means:**
- A **$1M limit** covers the typical claim with plenty of room. At-Bay's average is $180K for firms under $25M [prior]. But the severe single event can pass it.
- A **$2M limit** covers the severe event.
- A $2M aggregate adds about $60–150 a year of expected payments to Cedar Ridge. That is **10 to 30 times** what a Corgi-style second $1M adds (under $5 a year) [estimate, 11b].
- Going from $1M to $2M usually costs well under double the premium [snippet].

**Options (your decision):**

| Option | Structure | Protects against | Fits |
| --- | --- | --- | --- |
| A | $1M each incident / $2M per year (Corgi-style) | Two events in one year | Liability-heavy buyers and contract requirements. It does not fix the one-big-event gap |
| **B (recommended for Cedar Ridge)** | **$2M each incident / $2M per year** | One severe event | Data-heavy or seasonal firms. For Cedar Ridge: thousands of SSNs and a tax-season peak |
| C | $1M / $1M (today) | The typical claim | Firms with few records and no client money |

**Rule for other firms** (report 08's rule, made explicit):
- **$1M** base.
- **$2M** if the firm holds more than about 25,000 sensitive records, moves client money, or depends on a seasonal peak.
- **$3M** when a contract requires it.

The rationale can then say: *"I kept the two-number format buyers know from Corgi and general liability, but sized the numbers from the loss map. Cedar Ridge's worst realistic single event is $0.9–2.2M, so it needs $2M for one incident, not a second $1M."*

- **In the policy:** Item 4; Item 6 in two columns (each incident / policy period). The two columns are also the *CiCi* fix (A4).
- **Status:** **Open decision.** The application already lists $1M, $2M and $3M options with no explanation (report 06).

### Q5. What do we pay for? (the coverages)

Each coverage exists because of a row in the loss map:

| Coverage | Loss map row | Keep? |
| --- | --- | --- |
| A. First-call incident response (72 hours, outside the limit, $0 retention) | All rows (speed) | Keep. It is the most buyer-visible promise. Consider stretching it (report 11: replaces B12) |
| B. Breach response | L3 | Keep. Add client tax-identity help (report 11, section 5) |
| C. Extortion | L2 | Keep. Add the "paying is never required" line (A1) |
| D. Business interruption (your systems) | L2, L5 | Keep. 8-hour wait; 50% advance |
| E. Dependent business interruption (vendors attacked) | L4 | Keep |
| F. Data restoration | L2, L5 | Keep |
| G. Betterment | L2 (stops a repeat) | Keep |
| H. Payment fraud | L1 | **Fix the triggers (A3). Resize the limit for firms that move client money** |
| I. Privacy liability | L3 | Keep. Coordinate with professional liability |
| J. Regulatory | L6 | Keep |
| K. PCI | L3 (cards) | Keep; small for a CPA firm |
| L. Media | Website and social media content | Keep; small |
| M, N, O. Reputation and other smaller covers | L3 follow-on | Keep if each has one sentence tying it to a loss path |
| P–S (optional) | L4 (vendor system failure), and others | Optional; price them |

**Status:** mostly there. The two gaps are fraud paths (A3) and the cloud boundary (A10). Anything that can't point to a row should be cut or made optional.

### Q6. What do we cap or exclude, and why?

Every restriction must name its reason.

**Reason key:**
- **MH**: moral hazard;
- **ACC**: accumulation;
- **PP**: public policy or the law;
- **OP**: another policy covers it;
- **NP**: can't be priced yet.

| Restriction (current draft) | Reason | Holds up? | Action |
| --- | --- | --- | --- |
| $250K system-failure cap across D and F | ACC (one bad update hits many firms), NP | Yes | Keep. Say "applies across coverages" (*CiCi*). Show a priced full-limit buy-up |
| 8-hour waiting period | MH, and to filter out small blips | Yes; matches the market | Keep |
| 20% ransomware coinsurance without verified backups | MH (backups are the strongest control) | **Only if the gap mattered** | Keep, with A2's causation rule. Encryption losses only (T2-6). Short backup test (B5) |
| 20% coinsurance for an unpatched notified vulnerability (45 days) | MH | Yes. Objective and notice-based | Keep; don't stack with the ransomware coinsurance (T2-6) |
| $100K fraud cap when a payment request wasn't verified by callback | MH (callback stops most fraud) | Yes, but only when the insured was deceived | Keep. It never applies when the bank was deceived (A3) |
| $250K payment-fraud limit | MH, NP | **Too small for firms moving client money** | Keep for most firms. Offer $500K–$1M for payroll and bookkeeping firms |
| War exclusion (with the attribution burden on us) | ACC | Yes | Keep. Fix "state" (T2-9) |
| Infrastructure exclusion (power, telecoms, internet backbone) | ACC | Yes, if narrow | Narrow it here and in the system-failure definition (A10) |
| Intentional acts; prior known incidents | MH | Yes | Fix the scope (T2-1h, T2-1d) |
| Sanctions; punitive damages where uninsurable | PP | Yes | One insurability rule (T1-8) |
| Contract liability; unfair trade practices | OP; PP | Mostly | Carve-backs (T2-1b, T2-2) |
| Bodily injury, property damage, professional errors | OP | Yes | Coordinate with professional liability |

**Rationale test:** one line per restriction, as "[Restriction] exists because [reason]; it bites only when [condition]." If a line can't be written, the restriction goes.

### Q7. Who do we insure, and at what price?

| | |
| --- | --- |
| **Principle** | Ask only questions that change the price or the terms. Verify the controls that matter most (MFA, EDR, backups, callback) with evidence, not a tick-box. Use the pre-issue scan to find problems, not to deny claims (T2-7) |
| **Price** | $5,508 for Cedar Ridge. The rationale has no calculation behind it. Add the loss-cost sketch from README section 4.2: expected loss about $2.6K, a mid-case loss ratio near 47%, and expenses and profit on top. Remove the Vouch figure (T1-3) |
| **Monitoring** | This is what AIG, Coalition and At-Bay do differently: scans and alerts choose better risks and prevent losses. Harborline has the pre-issue scan and alerts on known-exploited vulnerabilities. The services sit outside the contract (SB25-058), and only the promise that services never cut cover goes in the policy (B9) |
| **In the policy** | Items 7 and 8; the application; its last page (how answers set terms) |
| **Status** | Application fixes (Tier 3). Pricing sketch needed |

### Q8. How do we pay when something happens?

| | |
| --- | --- |
| **Principle** | For a small firm, the real killer is cash timing. Pay fast and pay vendors directly |
| **Current** | 72-hour first response at $0; a panel of vendors; pay-on-behalf; a 50% business-interruption advance within 10 business days; written service standards with interest |
| **Why** | Every one of these answers "keep it running". This is Harborline's strongest part, and ahead of the market (report 10, section 2) |
| **Status** | Keep. Fix the interest rate reference and the "aims" versus "binding" wording (T1-9). Make the advance scale with the limit (report 06) |

---

## 4. The story: rationale outline (about 10 pages)

The rationale should read as the eight answers in order, so the reviewer sees the reasoning build.

1. **Summary**, half a page: the purpose sentence, who it's for, the four or five decisions that matter most, and what was deliberately left out.
2. **Who it's for, and why this segment.** Q1. The Corgi fit goes here, in one or two sentences.
3. **How these firms lose money.** Q2: the loss map table, with sources. This is the heart of the rationale.
4. **The structure.** Q3 and Q4: the retention and limit logic with the arithmetic, the Corgi comparison, and the limit rule.
5. **What's covered, and why.** Q5: one line per coverage, pointing to the loss map.
6. **What's limited or excluded, and why.** Q6: one line per restriction, with its reason.
7. **How definitions are built.** The brief asks for this explicitly. Plain words; defined terms in bold; triggers tied to the loss paths; one definition per concept (e.g., one "payment fraud").
8. **Underwriting and price.** Q7: the application-to-terms page, the loss-cost sketch, and monitoring.
9. **Claims.** Q8: the service promises, and why cash timing matters.
10. **Trade-offs and what I'd test next.** The options you rejected and why:
    - per-event limits and reinstatements;
    - parametric downtime pay;
    - full-limit system failure;
    - deepfake response.
11. **Sources.** At least three; you have far more. Label the date of each.

Keep your own voice. Cut process narration. Every number should appear once, with its reason (T4-1, T4-10).

---

## 5. Work list, in order

With the 48-hour clock, do this in order and stop wherever time runs out. Each step leaves a better submission than the one before.

1. **Decide the limit** (Q4) and the fraud-limit approach (Q6). Everything downstream uses these numbers.
2. **Legal must-fixes** (README Tier 1):
   - Corgi framing;
   - Coalition's surplus-lines status;
   - the Vouch figure;
   - the terrorism notice;
   - the Colorado fraud warning;
   - late notice;
   - 45-day cancellation notice;
   - punitive damages;
   - interest;
   - regulatory update;
   - the byline.
3. **The three changes that really protect:**
   - A3, payment fraud;
   - A2, the causation rule for security terms;
   - A10, the cloud boundary.

   Plus the limits map in two columns (A4), which comes with Q4.
4. **Rewrite the rationale** in the section 4 order: loss map, limit and retention arithmetic, and one line per restriction.
5. **Other Tier 2 wording fixes**, highest first, per the README.
6. **Application fixes** (Tier 3) and the pricing sketch.
7. **Final pass:**
   - match the declarations to the text;
   - check every cross-reference;
   - check the PDF export;
   - read it all once, aloud, in your own voice.

---

## 6. Decisions for you

1. **Limit for Cedar Ridge.** Option A ($1M / $2M, Corgi-style), **B ($2M / $2M, recommended)** or C ($1M / $1M).
2. **Fraud limit for firms moving client money.** Keep $250K, or offer $500K–$1M? The recommendation is to offer it, and to show it as an option in Item 6.
3. **Which optional covers to show:** P (vendor system failure, 24-hour wait), a full-limit system-failure buy-up, and deepfake response. Recommendation: show all three as priced options, but buy only P for Cedar Ridge.
4. **The deadline.** When is the submission due? That decides how far down the section 5 list to go.
