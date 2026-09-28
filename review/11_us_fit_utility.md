# 11. Do the borrowed ideas work in the US, and do they really protect? (US fit and utility test)

Prepared September 27, 2026. This merges three independent checks of the 34 ideas in report 10:
- `11a_us_law_fit.md`: US and Colorado law, and whether each idea can be filed;
- `11b_loss_utility.md`: loss data, and dollars of protection to Cedar Ridge each year;
- `11c_us_market.md`: what US carriers offer, what buyers ask for, and real US claim disputes.

**Evidence caveat.** About 70 web searches, all read at search-result level. No statute, opinion or policy form was opened at source. Case citations and statistics must be checked before quoting (section 7). Utility dollar figures are estimates built on the claims data in reports 01 and 03, with the arithmetic in 11b section 3.

---

## 1. Bottom line

1. **Most of the 34 ideas are drafting hygiene or reassurance, not protection.**
   - All 34 together are worth about **$480 a year** to Cedar Ridge in expected claim payments (range $400–600). That is about **9% of the $5,508 premium**.
   - **One idea, A3 (payment fraud), is about 37% of that.**
   - "Hygiene" still matters: it prevents disputes and makes caps enforceable. It just isn't a reason to buy.
2. **Only three ideas clear all three tests (law, loss data, market):**
   - **A3, one payment-fraud trigger covering partners, the bank and client accounts.** As drafted, roughly 35–55% of the fraud losses a payroll-running CPA firm realistically suffers would be denied or disputed. US courts have denied exactly these losses: *Taylor & Lieberman v. Federal* (9th Cir. 2017, an accounting firm), *RealPage v. National Union* (5th Cir. 2021, client funds "controlled" but not "held") and *Mississippi Silicon v. AXIS* (5th Cir. 2021, employee-authorized transfer).
   - **A2, a security term counts only if it mattered to the loss.** It stops a $30–60K coinsurance cut on a ransomware claim where the backup gap made no difference. It answers the most common US small-business fear ("they'll deny me over a control"). Colorado law gives no such default.
   - **A10, the cloud-account tie-breaker plus narrower infrastructure wording.** It settles which coverage pays when an attack on a vendor hits Cedar Ridge's own cloud tenant. The law check found a second bar: the **system failure** definition *also* excludes "internet infrastructure".
3. **Several ideas repeat what US or Colorado law already gives the insured.** Keep them only as one-line clarity, or drop them:
   - A1 ("you never have to pay a ransom"): no US case forces payment.
   - A7 (an external alert is a suspected incident): an FBI or bank alert already meets the reasonable-suspicion test.
   - B6 (warning and cure): Colorado's *Secrist* rule already requires real prejudice for a cooperation defense.
   - B14 (renewal "what changed"): C.R.S. 10-4-110.5 already requires 45 days' notice, with reasons, of any cut at renewal.
4. **Five drafts in report 10 create legal risk as written, and are fixed in section 4:**
   - A1 promises privilege over a record NYDFS requires to be filed;
   - A3 uses "direct loss", the word *Apache* turned on;
   - A5 can leave nothing paying if the first event was never reported;
   - A7 can fix the discovery date and trigger exclusion 2;
   - B13 creates coverage if the summary is broader than the wording.
5. **Take 15 ideas out of the policy.** No US buyer asks for them, they pay cents a year, or they cost more than they give. Two of them (B14, B15) survive as practice outside the policy, and C8 as one strategy line:
   - A9, B2, B3, B4, B6, B8, B11, B14, B15, B16;
   - C1 for CPA firms, C2, C5, C7, C8.
6. **The biggest protection gaps aren't on the idea list at all.** They are structural:
   - the limit options (does a $1M aggregate fit, or should $2M and $3M be real options?);
   - a fraud limit sized for a payroll firm;
   - enough breach-response capacity;
   - a priced full-limit system-failure buy-up;
   - tax-identity help for the firm's clients;
   - coordination with the firm's accountants' professional liability policy.

   A $2M limit option protects Cedar Ridge **10 to 30 times more per premium dollar** than a limit reinstatement (11b). **This is the strongest evidence for rebuilding the policy from first principles** (limits, retention, the few restrictions the insurer needs) rather than adding features.

---

## 2. Scorecard: all 34 ideas

**Keys:**
- **Law:** US-fit (G fileable as drafted / A with changes / R doesn't translate), then legal utility (H changes whether a claim is paid / M resolves a litigated ambiguity / L restates default law / Neg adds dispute risk).
- **Loss:** real protection to Cedar Ridge (High / Medium / Low / Cosmetic / Negative), then mid expected value in $ a year.
- **Market:** US class (TS table stakes / Common / Rare / Absent), then market fit (Strong / OK / Weak / Poor).
- **Final:**
  - **Core**: put it in the policy.
  - **Hygiene**: put it in, merged into a planned fix, and don't sell it as a benefit.
  - **Option**: a priced add-on or rating-plan item.
  - **Practice**: do it outside the policy.
  - **Drop**.

| ID | Idea | Law | Loss | Market | Final | Why (the deciding reason) |
| --- | --- | --- | --- | --- | --- | --- |
| **A3** | One payment-fraud trigger; partners, bank and client accounts | A · **H** | **High** · $175 | TS (bank) / Rare (client accounts) · **Strong** | **Core, first priority** | Closes the fraud paths US courts have denied. $200K+ tail for a client payroll diversion |
| **A2** | Security terms count only if they mattered | A · **H** | Medium · $14 ($55 without the backup credit) | Absent · **Strong** | **Core** | Colorado has no causation default and enforces anti-concurrent wording as written. Top buyer fear |
| **A10** | Cloud-account tie-breaker; narrower infrastructure wording | A · M | Medium · $25 | TS (concept) · Strong | **Core** | Settles vendor-side attacks. Fix the **system failure** definition as well as exclusion 12 |
| A4 | Limits map; caps say "applies across coverages" | G · M (H for the insurer) | Low for the insured · ~$0 | TS (map) / Rare (label) · Strong (brokers) | **Hygiene** | It makes the insurer's caps hold after *CiCi*. For the insured the gain is certainty, not money. Say that honestly |
| A5 | Related incidents: earliest period, continuity | A · M | Low · $25 | TS · Weak | **Hygiene** (inside T2-1c) | Expected on every form. Apply the earliest-period rule only if the earliest event was reported in time |
| A1 | Ransom never required; pre-payment routine | A · L (M for the pre-payment report) | Low · $15 | Absent (wording) / TS (practice) · OK | **Core, one line** | Reassurance plus OFAC hygiene. Harborline's own III.4.6 creates the argument, so one sentence closes it |
| A7 | External alert = suspected incident | A · L | Low · $25 | Common · OK | **Hygiene** (one sentence in T2-1f) | Default law already gets there. An alert alone must not count as "discovery" or knowledge |
| A8 | Foreign privacy regulators | A · L | Cosmetic · <$1 | TS · Weak | **Hygiene** (one line) | Worth almost nothing to Cedar Ridge, but a broker's comparison checklist flags the gap. It costs nothing |
| B5 | Define "verified backups" | A · **Neg** as drafted | Medium · ±$10 on claims (bigger prevention value) | Common (application) · OK | **Core, short** | Keep the policy test short and outcome-based. Put the detailed checklist in the application (T3-7). Otherwise it adds five ways to lose |
| B7 | You need answer only what we asked | G · L | Low · $5 | Common · OK | **Core, one line** (with T2-13) | Closes the "unasked fact" route. Pair with V.3's honest-mistake rule, which is what would have saved *ICS* |
| B9 | Security services, plus a no-forfeiture promise | A · M | Medium (services) · ~$120 from services | TS (services) · **Strong** | **Core** (hybrid) | Services cut claims. Keep them outside the contract (SB25-058); only the promise goes in the policy. T2-7 first |
| B13 | "Policy at a glance" | A · **Neg** as drafted | Cosmetic · $0 | Rare · OK | **Core, non-contractual** | The cover already promises it. Write it last, cite a section on each line, and never make it broader than the wording (*Bailey*) |
| B1 | Deepfake and impersonation response | G · L | Medium · $40 | Rare · OK | **Option** (~$75), CPA-scoped | Real in tax season, but small dollars and no US coverage fight found. Scope it to lookalike domains, fake firm emails and cloned partner voices |
| A6 | One retention per year | G · L | Low · $2–10 | Rare · OK | **Option** (one line if kept) | A sweetener worth dollars a year. Don't sell it as protection |
| B12 | $0 retention on panel forensics if reported in 72h | G · L | Low · $35 | Common · **Strong** | **Change:** stretch Coverage A instead | Buyers compare it, but it overlaps Coverage A. A longer or bigger Coverage A does the same job with no new mechanism |
| B10 | Verified-framework credit | G · L | Low · $0 on claims | Rare · Weak | **Option** (rating plan) | A pricing tool, not protection. Keep it out of the form |
| C4 | $0 retention with qualifying MDR | G · L | Low (MDR buyers $40–50) | Rare/Common · OK | **Option** (rating plan) | A hook to sell MDR. Replace the MDR credit rather than stacking on it |
| C6 | Lookalike-domain client fraud, no breach | A · L | Low for CPA · $60 | Rare · OK | **Option** (invoice-heavy classes) | A real gap, but a poor fit for CPA fees. Needs a waiver of subrogation against clients |
| C3 | AI regulatory defense | A · M (defense) | Cosmetic · $1–5 | Rare · Weak | **Later** (2027, defense only) | The law takes effect Jan 1, 2027. Penalties are likely uninsurable in Colorado |
| A9 | Court attendance | G · L | Cosmetic · $1 | Common · Weak | **Drop** | Pays about 15–20% of a rare partner day. Mention it only if checklist parity with Coalition matters |
| B2 | Executives' personal funds | A · L | Cosmetic · $2–5 | Absent (commercial) · Weak | **Drop** | Reg E, banks and homeowners cover most of it. Causation fights. Personal cyber is a personal-lines product |
| B3 | AI voluntary shutdown | A · L | Cosmetic · $0–2 | Rare · OK | **Drop** as an item | No autonomous agents at Cedar Ridge. T2-5's routing does the work |
| B4 | Coinsurance only above the first $50K | G · L | **Negative** | Absent · Weak | **Drop** | It blunts the backup incentive exactly where it should bite. Fix the root cause (A2, B5) instead |
| B6 | Warning and cure | A · L | Low · $5 | Absent · Weak | **Drop** | Colorado's *Secrist* rule already requires prejudice. It would slow every claim |
| B8 | Retention billed last, in installments | G · L | **Negative** | Absent · OK | **Drop** | Worth about $3 to the insured; costs more in bad debt and collection friction |
| B11 | Earn credits mid-term | A · L | Low · $4 | Rare · Weak | **Drop** | Renewal handles it. Admin cost |
| B14 | Renewal "what changed" | G · L | Cosmetic | Rare · OK | **Practice** | Statute already requires the notice (10-4-110.5). Use the table as the notice format |
| B15 | Legal-deadlines card | A · L | Cosmetic · $2–5 | Common (service) · Weak | **Practice** (welcome pack) | The breach coach already does this. A card goes stale |
| B16 | Publish claims results | G · L | Cosmetic | Absent · Weak | **Drop** | Every published miss becomes bad-faith evidence |
| C1 | Fast Downtime Payment (parametric) | A in CO; **R in NY** · L | Low for CPA (Negative as core) | Rare · OK | **Drop for CPA class**; name it as considered | About $1.3–2.7K of technical premium (25–50%) for downtime a CPA firm can defer, and every firm on one platform claims at once. CPA firms need Coverage P with a 24-hour wait |
| C2 | One limit reinstatement | G · L | Cosmetic · <$5 | Rare · OK | **Drop** | A $2M/$3M limit option protects 10–30 times more per dollar |
| C5 | Goodwill payments | A · L | Low | Absent · Poor | **Drop** | The US norm is credit monitoring, which Harborline already pays. It also carries admission risk in class actions |
| C7 | Risk classes | A · L | Low | Absent (form) · Weak | **Drop** | An underwriting redesign, not a clause |
| C8 | Distribution ideas | **R** as wording | Cosmetic | Common · Strong (strategy) | **Strategy line only** | Not a wording question. Producer-licensing caveat for MSPs |

**Tally:**
- **Core:** A3, A2, A10, A1, B5, B7, B9, B13.
- **Hygiene** (merged into planned fixes): A4, A5, A7, A8.
- **Option / rating plan:** B1, A6, B10, C4, C6; B12 becomes a Coverage A change.
- **Later:** C3.
- **Practice:** B14, B15.
- **Drop:** A9, B2, B3, B4, B6, B8, B11, B16, C1 (CPA), C2, C5, C7, with C8 kept as a strategy line only.

---

## 3. Where the three checks disagreed, and the call

| Idea | Law | Loss | Market | Call |
| --- | --- | --- | --- | --- |
| B12 ($0 panel retention) | Neutral | Low; overlaps Coverage A | Strong; appears in quote comparisons | **Stretch Coverage A** (longer clock or bigger cap). It gets the buyer-visible result without a second mechanism |
| A9 (court attendance) | Harmless | Cosmetic | Common; in Coalition's base form | **Drop.** Protection value is about $1 a year. If checklist parity matters, add one line at $1,000 a day |
| B5 (backup definition) | Negative as drafted | Medium | OK | **Short outcome-based test in the policy; checklist in the application.** That keeps the prevention value without new forfeiture routes |
| A4 (limits map) | High for the insurer | ~$0 for the insured | Strong with brokers | **Keep, and be honest** that it protects the insurer's caps. The insured gets certainty |
| A8 (foreign regulators) | Low | Cosmetic | Table stakes | **One line.** It costs nothing and removes a checklist "no" |
| C2 (reinstatement) | Fine | Cosmetic | OK | **Drop; offer real $2M/$3M limits instead** |
| C1 (parametric) | Amber (Red in NY) | Low or Negative for CPA | Interview material | **Name it as considered and rejected for this class.** Offer Coverage P with a 24-hour wait |

---

## 4. Corrections to report 10's drafts

| Draft | Problem | Fix |
| --- | --- | --- |
| A1 | It promises privilege over a decision record that NYDFS 500.17(c) requires regulated firms to file. The 12-hour promise becomes a bad-faith yardstick (C.R.S. 10-3-1115) | Drop the privilege promise. Replace "within 12 hours" with "promptly". Add to **period of restoration**: "reasonable speed never assumes a ransom was paid". Add "unless law enforcement advises otherwise" to the pre-payment report |
| A2 | Scope unclear; clashes with exclusion 2 and V.3.4; doesn't stop an *ICS*-style rescission | Limit it to pre-incident controls. Define the causal test. Make exclusion 2 yield for known, unexploited weaknesses. Say V.3 (the application) is separate |
| A3 | "Causes you a direct loss" reintroduces the word *Apache v. Great American* turned on | Use "resulting from". Add a right to recover from the bank under UCC Article 4A (C.R.S. 4-4.5-202, -204), and a duty to preserve the insured's one-year objection right. For refunds to clients, our consent "will not be unreasonably withheld" (*Stresscon*) |
| A5 | If the first small event wasn't reported, the campaign attaches to a closed year. Under *Craft*, nothing pays | Apply the earliest-period rule only if the earliest incident was reported in time, to us or a prior insurer. Otherwise this policy responds. Keep exclusion 2 |
| A7 | "Always" an incident can fix the discovery date and create a known circumstance under exclusion 2 | Limit it to the A and B trigger. State that an alert alone is not discovery or knowledge |
| A10 | Narrowing exclusion 12 alone leaves the **system failure** definition's own "internet infrastructure" bar | Narrow both, and route D, E and P consistently with T2-0 |
| B5 | Five new conditions mean five new ways to lose the credit | Keep today's two elements in the policy. Move the checklist to the application and the evidence list |
| B13 | A summary broader than the wording creates coverage (*Bailey* prong 2) | Non-contractual label; one section cite per line; generate it last from the final wording |
| C1 | New York's 2025 parametric statute covers weather events only | Colorado Amber, New York Red. Moot for the CPA class |
| C3 | Violations of Colorado's AI law are deceptive trade practices, fined up to $20,000 per violation. Those penalties are likely uninsurable, and exclusion 8 blocks the claim today | Defense only, after the Attorney General's rules. Not before 2027 |
| Fact | The Wolters Kluwer CCH outage was **May 2019**, not 2021 | Fix it wherever cited |

---

## 5. What's missing from the list entirely (the real protection levers)

These came up in the market and loss checks. Each is bigger than any single borrowed idea except A3.

| Gap | Why it matters for a CPA firm | Evidence | Suggested direction (to decide in the first-principles design) |
| --- | --- | --- | --- |
| **Limit options** | Firm-threatening uninsured loss starts around $250–500K (3–6% of revenue). A severe ransomware event plus a class action can pass $1M | 11b section 2.1; ransomware severity $269–422K; 1,822 data-breach class actions in 2025 (Duane Morris 2026) | Make $2M and $3M real, priced options. Set a written rule for which limit fits which firm |
| **Fraud limit for payroll firms** | Sublimits of $100K–$250K are the top broker complaint. A client payroll batch is $200–400K | 11c section 5; 11b A3 | $500K–$1M option for firms moving client money. Tie it to verified callback and email security, not MDR |
| **Breach-response capacity** | Coalition, CFC and Beazley BBR give a separate or larger response limit. Harborline puts only $25K / 72 hours outside the aggregate | 11c section 5 | Stretch Coverage A (this also absorbs B12), or offer a separate response limit |
| **Full-limit system-failure buy-up** | It is common in the US (Coalition's surplus-lines form, Cowbell Prime 250). "Higher limits available" must be real | 11c section 4 | Keep the $250K core. Show a priced buy-up |
| **Tax-platform outage cover** | CCH (May 2019, 3–5 days) and Kronos (Dec 2021, weeks) are the outages CPA firms fear | 11b C1 | Coverage P (dependent system failure) with a 24-hour wait, rather than parametric |
| **Tax-identity help for clients** | Stolen return data leads to fraudulent refunds and IRS identity-theft cases for clients | IRS data-theft guidance; about 300 tax-professional incidents in H1 2025 (IRS/Security Summit) | A line in Coverage B: help clients file IRS identity-theft affidavits and get IP PINs. Decide whether redirected refunds sit in H or I |
| **Coordination with professional liability** | Accountants' professional liability doesn't cover breach costs, and cyber doesn't cover professional errors. A client suit after a breach can fall between the two | 11c section 5 | An "other insurance" line: cyber responds to claims arising from a security failure or privacy event even if professional liability might also respond |

---

## 6. What this means for the design

1. **Adding features is the wrong lever.** The whole borrowed list is worth about 9% of premium to the insured. The protection lives in the structure:
   - the right limit;
   - a retention the firm can absorb;
   - fraud and response limits sized to how this kind of firm actually loses money;
   - as few restrictions as the insurer needs, each with a stated reason.
2. **Use the utility test as the permanent filter** for every clause. A clause stays only if it passes all six:
   1. It maps to a real loss.
   2. It changes the outcome (paid instead of denied, or paid sooner).
   3. It can be priced and afforded.
   4. The insurer can manage it without moral hazard or accumulation.
   5. It can be filed in Colorado.
   6. It can be explained in one sentence.
3. **Honest labels in the rationale:**
   - "Protection": A3, A2, A10, the missing levers.
   - "Clarity": A1, A5, A7, A8, B7, B13.
   - "Insurer hygiene": A4.
   - "Considered and rejected": C1, C2, B4, and the rest of the drop list, with one reason each.

---

## 7. Verify before quoting

Highest value first. The full lists are in 11a section 5, 11b section 5 and 11c section 6.

1. **Case law:**
   - *Taylor & Lieberman v. Federal* (9th Cir. 2017, unpublished);
   - *RealPage v. National Union* (5th Cir. Dec 22, 2021, No. 21-10299);
   - *Mississippi Silicon v. AXIS* (5th Cir. 2021);
   - *Apache v. Great American* (5th Cir. 2016);
   - *Medidata* (2d Cir. 2018) and *American Tooling* (6th Cir. 2018);
   - *CiCi Enterprises v. HSB Specialty* (N.D. Tex. Feb 23, 2026; docket, and trial or settlement status);
   - *Travelers v. ICS* (C.D. Ill. 2022, a stipulated rescission);
   - *Columbia Casualty v. Cottage Health* (C.D. Cal. 2015: dismissed for failure to mediate, **not** a ruling on the exclusion);
   - *State Farm v. Secrist* (Colo. App. 2001);
   - *CIRSA v. Northfield* (Colo. App. 2008).
2. **Colorado statutes:**
   - C.R.S. 10-4-110.5 (renewal notice);
   - 10-4-419 (claims-made certification);
   - 10-3-1104 as amended by SB25-058 (its text and effective date);
   - the Colorado AI Act (SB 26-189): effective date and penalty provisions.
3. **Colorado filing regime:** whether commercial forms are file-and-use (Division of Insurance SERFF instructions).
4. **New York's 2025 parametric statute:** scope.
5. **Data:**
   - Coalition 2026 Cyber Claims Report;
   - At-Bay 2026 InsurSec;
   - Duane Morris 2026 (1,822 filings);
   - ITRC 2025 (3,322);
   - IRS tax-professional incidents;
   - Parametrix 2025 cloud outage data;
   - AWS October 20, 2025 (about 15 hours; DNS automation);
   - Kronos December 2021 duration.
6. **Do not cite** vendor-blog denial statistics ("82% of denials involve MFA", "40% of claims denied" and similar).

---

## 8. Source reports

| Report | Lens | Searches | Headline |
| --- | --- | --- | --- |
| `11a_us_law_fit.md` | US and Colorado law, filing | 25 | Nothing is unlawful on Colorado admitted paper. A2, A3, A4 and A10 are legally strongest. Five drafts need fixing. C8 is Red as wording, and C1 is Red in New York |
| `11b_loss_utility.md` | Loss data and expected value | 22 | All 34 are worth about $480 a year. A3 alone is High. B4 and B8 are Negative |
| `11c_us_market.md` | US carriers, brokers, disputes | 25 | 10 keep, 12 keep with change, 6 optional, 6 drop. Five high-demand gaps are missing from the list |
