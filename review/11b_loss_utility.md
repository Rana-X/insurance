# 11b. Loss utility of the 34 borrowed ideas: do they really protect Cedar Ridge?

Prepared September 27, 2026. The lens here is claims reality and loss economics only. Law and US market prevalence are covered in other reports.

**Evidence labels**
- **[data]**: a named report with a year. I saw it only at search-result level, because fetching was blocked. Nothing was opened at source.
- **[snippet]**: a secondary page or an unattributed search summary. Lower quality.
- **[prior]**: from `review/` reports 01, 03, 10 or the README.
- **[estimate]**: my judgment. The reasoning is shown in section 3.

I used 22 web searches. No policy wording is quoted.

---

## 1. Bottom line

- **Only one idea is High utility: A3, a single payment-fraud trigger that covers partners, the bank and client accounts.**
  - As drafted, Harborline would deny or dispute roughly 35–55% of the fraud losses a payroll-running CPA firm realistically suffers.
  - A3 is worth about $90–450 a year to Cedar Ridge in expected claim dollars (mid about $175).
  - It also covers a $200K+ client payroll diversion.
  - It accounts for about 35–40% of the expected value of all 34 ideas combined.
- **All 34 ideas together are worth about $400–600 a year to Cedar Ridge in expected claims** [estimate: the sum of the mid values in section 4 is about $480].
  - That is roughly 9% of the $5,508 premium, and about 18% of the mid expected loss of about $2.6K [prior].
  - Most of the list is drafting hygiene, reassurance or transparency. That is not bad, but it is not protection.
- **Top 5 by real protection value:**
  1. **A3**, payment fraud (High).
  2. **A2**, security terms count only when they mattered. It stops a $30–60K coinsurance cut on a ransomware claim when the backup gap made no difference.
  3. **A10**, the cloud-account tie-breaker. It settles which coverage pays when an attack on a vendor hits Cedar Ridge's own cloud tenant.
  4. **B1**, impersonation and deepfake response. The event is real and targets CPA firms, and it has no cover today, but the dollars are small.
  5. **B5**, a precise backup standard. It means fewer fights on the costliest claim type, and better backups.
- **Bottom 5:**
  1. **B8**, retention paid in installments. The insured gains about $3 a year, while the insurer carries more than that in bad debt and has to collect from a claimant. Negative.
  2. **B4**, the small-loss safe harbor. It gives back up to $10K exactly where coinsurance is meant to bite. Negative.
  3. **C2**, one limit reinstatement. It is worth under $5 a year, and a $2M aggregate option protects 10–30 times more per dollar.
  4. **A9**, court attendance. It is worth about $1–3 a year and pays about 15–20% of a partner's real day.
  5. **B2**, executives' personal funds. It is worth $2–5 a year, and every claim would bring a causation fight.
  - Close behind: A8, B3, C3, B14, B16 and C8.
- **Tier A is mostly hygiene, not protection.**
  - A4, A5 and A7 either restate what Harborline already does or mainly protect the insurer. What it already does: one incident for related events, Coverage A for suspected incidents, and calls never counting against you. A4 makes the system-failure cap enforceable after *CiCi*.
  - Keep them, merged into the planned fixes, but don't sell them as benefits.
  - A6 (one retention a year) is worth about $2–10 a year, A9 about $1–3, and A8 under $1.
- **C1 (Fast Downtime Payment) is the costliest idea and a poor fit for a CPA firm.**
  - A cloud trigger paying $1,000 an hour after 8 hours would need roughly $1.3–2.7K a year of technical premium, 25–50% of today's premium [estimate].
  - It pays for downtime that Cedar Ridge says it can absorb: 1 day in tax season, 3 days otherwise [prior].
  - Every CPA firm on the same platform would trigger at once.
  - Its attack trigger duplicates the existing 50% advance within 10 business days.
  - What CPA firms actually fear is a multi-day tax or payroll platform outage. Two examples: CCH in May 2019 was down 3–5 days, and Kronos in December 2021 was down for several weeks [snippet]. That points to optional Coverage P with a 24-hour wait, not a parametric trigger.
- **The best loss reducers in the list are services, not clauses.** At-Bay says no MDR customer filed an Akira claim in 2025 [snippet]. B9 and C4 are worth offering for that reason, but the clause wording adds little. Free services must stop short of MDR, which costs more than the whole premium.
- **Corrections to the brief:**
  - The Wolters Kluwer CCH malware outage was in **May 2019**, not 2021 [snippet].
  - I found no Coalition H1 2026 frequency update. The only H1 2026 item is the privacy-claims blog [prior].

---

## 2. Master table

### 2.1 Base rates used (arithmetic in section 3.0)

| Input | Value for Cedar Ridge | Label |
| --- | --- | --- |
| Paid-claim frequency | 1.2–2.0% a year, mid 1.6% | [prior]: Coalition 1.21% under $25M; CPA-stressed 1.82% |
| Fraud loss events | about 0.6% a year | [estimate]: 35–40% of claims (Coalition: BEC+FTF 58% of claims, FTF 27%; At-Bay fraud about 30% [prior]) |
| Ransomware or extortion | about 0.25% a year | [estimate]: about 15% of claims |
| Breach needing notice | 0.4–0.6% a year | [estimate]; cross-checked against IRS tax-pro incident counts below |
| Severity | average claim $116–180K; ransomware $269–422K; fraud $141–208K | [prior] |
| Revenue per business day | about $34K, more in February–April | [estimate]: $8.5M ÷ 250 |
| Downtime tolerance | 1 day in tax season, 3 days otherwise | [prior]: application 4.20 |
| Cost of money | 8–10% a year | [estimate]; Colorado statutory rate 8% [prior] |
| Firm-threatening uninsured loss | more than about $250–500K | [estimate]: 3–6% of revenue |

**How to read the table:**
- **EV** = chance the clause matters × dollars at stake × chance the outcome actually flips.
- "Today" means Harborline as drafted, before the fixes planned in README section 5.
- **Table figures are [estimate]s** built from the inputs above. Section 3 gives sources and arithmetic.
- **CR** = Cedar Ridge.

### 2.2 The table

| ID | Idea | Scenario (Cedar Ridge) | Freq/yr (clause matters) | Severity | Outcome change | EV $/yr | Tail value | Insurer cost | Utility | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | Ransom never required | Ransomware hits; CR refuses to pay; the insurer calls the longer outage avoidable | 0.003–0.013% | $50–300K of BI | Today: almost surely paid (the argument is theoretical). With: argument closed | $2–40 (mid 15) | Small | $0–15; helps OFAC compliance | Low (reassurance) | Keep, one-line version |
| A2 | Security terms count only if they mattered | Backup credit lapses, but backups work or the attack was data theft; 20% coinsurance applied | 0.03% (CR); 0.12% (insured without the backup credit) | 20% × $150–300K = $30–60K | Today: 20% cut. With: full payment unless the gap mattered | ~14 (CR); ~55 (without credit) | Moderate: avoids a $30–80K cut on a $300–400K event | $15–55 (0.3–1%) + $2–5K causation note per claim | Medium | Keep with change (merge with T2-6, T2-17) |
| A3 | One payment-fraud trigger incl. bank and client accounts | A partner, the bank or a payroll client's account is deceived; money is lost | 0.15–0.45% | $20–250K gross; ~$70K net | Today: 35–55% of these denied or disputed. With: paid | 90–450 (mid 175) | **High**: a client payroll batch is $200–400K and the firm may owe it | +$150–400 (3–7%) vs today; ~0 vs T2-1/T2-1a, which it replaces | **High** | **Keep, first priority**; rate on payroll volume |
| A4 | Limits map, cross-coverage caps | A bad vendor update wipes the file server; does the $250K system-failure cap span D and F? | 0.01–0.05% | $0–250K | Today: ambiguous; after *CiCi* a court may confine the cap (insured gets more). With: clear (insured gets less) | about −5 to +5 | None for insured; large for insurer (accumulation) | Saves leakage | Low (insurer hygiene) | Keep; don't market it |
| A5 | Related incidents: earliest period | Re-extortion or a class action lands in a later period; two policies point at each other | 0.02–0.05% | $7.5K (second retention) to $300K (gap) | Today: one-incident rule exists; the real gap is claim lock-in (T2-1c). With: tidier | 10–40 (mid 25) | Medium, but carried by T2-1c | ~0; earliest-period rule can shrink a multi-year campaign to one limit | Low | Keep with change (fold into T2-1c) |
| A6 | One retention per year | Two unrelated incidents in one year | ~0.03% | $2.5–7.5K | Today: two retentions. With: one | 2–10 | None (0.09% of revenue) | $2–10; slight moral hazard | Low | Drop (or one-line sweetener) |
| A7 | External alert counts as a suspected incident | IT provider, bank or FBI alert; investigation finds nothing | 0.15–0.5% | $3–15K of triage | Today: Coverage A already responds to suspected incidents, and calling never counts against you. With: no argument | 10–40 (mid 25) | Indirect (earlier containment) | $25–60 more Coverage A use, offset by avoided losses | Low | Keep with change (one sentence in T2-1f) |
| A8 | Foreign privacy regulators | Canadian client data; Canadian privacy regulator inquiry | ~0.0005% | $20–50K | Today: arguably covered (not limited to US agencies). With: certain | <1 | None | ~0 | Cosmetic | Drop (add only for firms with foreign customers) |
| A9 | Court attendance, $500/day | A partner attends a mediation or deposition in a breach class action | 0.04–0.09% | $1–3K paid; real cost $2.4–4K per person-day | Today: unpaid. With: ~15–20% of the real cost | 1–3 | None | $2–5 + tracking | Cosmetic | Drop |
| A10 | Cloud-account tie-breaker; narrower exclusion 12 | (a) An attack at the tax or payroll vendor exposes or corrupts CR's tenant. (b) An outage from a DNS fault inside AWS | (a) 0.02–0.09%. (b) 0 for CR (no Coverage P) | (a) $25–150K. (b) $2–10K per outage for P buyers | (a) Today: fight over whether only E applies or B/C/F/H do. With: settled. (b) Today already carved back; needed once T2-4 narrows the carve-back | (a) 10–60 (mid 25). (b) 50–150 for P buyers | Moderate (CDK-type vendor events) | (a) $20–40. (b) cloud accumulation inside P | Medium | Keep both; pair (b) with P's widespread-event cap |
| B1 | Impersonation and deepfake response | A lookalike domain or cloned partner voice targets clients in tax season; takedown, client warnings, PR | 0.3–1% | $5–25K costs; $3–20K net | Today: nothing (not an incident) except $2.5K of pre-incident advice. With: up to $25K | 15–80 (mid 40) | None ($25K cap) | $40–100 (0.7–1.8%) | Medium | Make optional (~$75) |
| B2 | Executives' personal funds | Firm-breach data used to drain a partner's personal account | 0.02–0.05% | $0–25K net of bank and homeowners cover | Today: not covered; consumer accounts mostly protected by Reg E. With: small top-up | 2–5 | None | Small + causation fights | Cosmetic | Drop |
| B3 | AI voluntary shutdown | A Copilot or agent misbehaves; CR switches it off | <0.05% | ~$0 (drafting tool; no autonomous agents) | Today: little or no loss. With: same | 0–2 | None | ~0 | Cosmetic | Drop; keep T2-5 routing |
| B4 | Coinsurance only above first $50K | Ransomware without verified backups | 0.06% (CR); 0.25% (without credit) | at most $10K | Today: coinsurance applies. With: up to $10K back | 3–30 | None | 0.5–1% for insureds without the credit; weaker backup incentive | **Negative** | Drop |
| B5 | Define verified backups | After ransomware: fight over test scope, test date or MFA | 0.05–0.08% | $30–60K (the 20% coinsurance) | Today: vague, so either side can argue. With: clear, both ways; better backups up front | ±10 on claims; larger loss-prevention value | Moderate (backups separate $168K claims from $510K claims) | ~0; reduces loss | Medium | Keep with change (checklist in application; short outcome-based definition) |
| B6 | Warning and cure before a post-loss duty | Slow documents; insurer cites non-cooperation | 0.02–0.03% | $50–200K | Today: prejudice rules and service standards already restrain. With: 30-day notice first | ~5 | Small | 0.1–0.3%; slows every claim | Low | Drop (or one sentence) |
| B7 | Answer only what we asked | After a loss, the insurer cites a fact the application never asked about | 0.02–0.05% | $10–30K (re-rating) | Today: honest-mistake rule already limits the remedy. With: closes the unasked-fact route | ~5 | Small | ~0.1%; slight adverse selection | Low | Keep with change (one line with T2-13) |
| B8 | Retention billed last, 6 installments | Cash squeeze after a claim | 1.6% (any claim) | $7.5K deferred ~3.5 months ≈ $220 | Today: pay up front. With: deferred | ~3 | None | $5–15 bad debt + collections; friction with a fresh claimant | **Negative** | Drop |
| B9 | Security services, no-forfeiture promise | Alerts, training and email security cut incidents | Clause: tiny. Services: every year | Services avoid ~30% of claims for users | Today: no program, and no forfeiture term except the KEV notice | Clause ~5; services ~120 to the insured | Indirect | Free services $50–200; MDR ~$10K+/yr can't be free | Medium (services) | Keep with change (hybrid; T2-7 first) |
| B10 | Verified-framework tier | IT provider attests to CIS IG1 or NIST CSF | n/a (pricing) | Credit $275–550 | No claim change | 0 on claims | None | 5–10% credit, offset by selection; attestation quality | Low | Make optional (rating-plan item) |
| B11 | Earn credits mid-term | CR buys MDR in month 4, then has a claim in month 9 | ~0.1% | $2.5–5K retention difference | Today: waits for renewal. With: applies from verification | ~4 | None | ~0.1%; admin | Low | Keep (one line) |
| B12 | $0 retention on panel forensics and breach coach if reported in 72h | A BEC mailbox review runs past Coverage A's 72 hours; nothing to notify | ~0.7% | at most $7.5K (average ~$5K) | Today: retention applies after Coverage A. With: $0 | 25–50 (mid 35) | None | $25–60 | Low | Drop (stretch Coverage A's clock instead) |
| B13 | Policy at a glance | Office manager needs to know what to do | n/a | n/a | No claim change; may speed the first call | ~0 | None | Drafting; must not contradict the wording | Cosmetic | Keep (the cover already promises it) |
| B14 | Renewal "what changed" table | Wording changes at renewal | n/a | n/a | None | 0 | None | Admin | Cosmetic | Drop from form; do it as practice |
| B15 | Legal clock card | Missed 30-day FTC or Colorado notice | 0.01–0.02% | $10–50K | Today: the breach coach already gives deadlines. With: a backup reminder | 2–5 | None | Stale-card risk | Cosmetic | Welcome pack, not the policy |
| B16 | Publish claims results | n/a | n/a | n/a | None for the insured | 0 | None | Published misses become bad-faith evidence | Cosmetic | Rationale line only |
| C1 | Fast Downtime Payment (parametric) | A cloud region or tax platform is down over 8 hours; or ransomware | Cloud: 0.2–0.4 **events**/yr. Attack: 0.25% | $1K per business hour; ~$4K per cloud event; cap $40K | Today: cloud failure not covered (no P); attacks paid under D/E, 50% advance in 10 business days. With: cash in 5 days, no proof | Payouts $800–1,600; real loss avoided ~$200–600 | Low (CPA downtime is mostly deferrable) | Technical premium ~$1.3–2.7K (25–50%); severe tax-season accumulation | Low (CPA); Negative if core | Make optional, not for CPA class; offer P with a 24h wait |
| C2 | One limit reinstatement | Aggregate exhausted, then an unrelated BEC | ~0.0005% | ~$150K | Today: nothing left. With: refilled | <5 | Rare but firm-threatening | Likely 3–8% ($165–440) | Cosmetic | Drop; make $2M/$3M limits real |
| C3 | AI regulatory defense | Colorado AG inquiry under the new AI law | 0.001–0.01% | $25–100K | Today: not covered (J needs a security or privacy event). With: defense | 1–5 | None | ~0.1% | Cosmetic | Drop now; revisit after 2027 |
| C4 | $0 retention with qualifying MDR | MDR alert, reported within 24h | ~1% for MDR buyers; 0 for CR today | $3.75–5K | Today: retention halved. With: $0 | 40–50 (MDR buyers) | None | $40–50 for MDR buyers, offset by selection | Low (a sales hook for MDR) | Make optional (replace, don't stack) |
| C5 | Goodwill payments to clients | Gift or fee credit to ~2,800 clients after a breach | 0.4–0.6% | $30–70K of spending | Today: not covered; credit monitoring and N meet the need | Payments 50–150; real value lower | None | 1–2%; spending only because it's covered | Low | Drop |
| C6 | Lookalike-domain client fraud | Clients pay fake invoices; no breach at the firm | 0.3–1% | $7–70K of fees at cost | Today: not covered (H.2 needs a security failure). With: covered | 30–150 (mid 60) | Low for CPA | $100–200 (2–4%); proof and collusion friction | Low (CPA); Medium for invoice-heavy classes | Make optional (invoice-heavy classes) |
| C7 | Risk classes | A class table sets expected controls | n/a | n/a | No claim change; can shrink who is insurable | 0 | None | Underwriting redesign | Low | Drop from this version |
| C8 | Distribution ideas | n/a | n/a | n/a | None | 0 | None | n/a | Cosmetic | Drop from the form; one strategy line |

---

## 3. Per-idea notes (arithmetic)

### 3.0 How the base rates were built

- **Claim frequency.**
  - Coalition's under-$25M frequency is 1.21% [prior].
  - Report 08's CPA-stressed case is 1.82% [prior].
  - I use 1.6% as the mid. Reported incidents, including below-retention events and Coverage A calls, run about 2–3 times that: 3–5% a year [estimate].
- **Fraud.**
  - 1.6% × 35–40% ≈ 0.6% a year.
  - Coalition: BEC plus FTF are 58% of claims, and FTF alone is 27%. At-Bay: fraud is about 30% of claims [prior].
  - Payroll activity pushes Cedar Ridge up, not down.
  - For context, AFP's 2026 survey found 48% of organizations under $1B revenue had actual payments-fraud losses in 2025, and 74% saw BEC [data]. The respondents are larger treasury teams, so this is context, not a rate.
- **Ransomware.**
  - 1.6% × about 15% ≈ 0.25% a year [estimate].
  - At-Bay says ransomware frequency for firms under $25M rose 21% [prior].
- **Breach needing notice.**
  - IRS stakeholder liaisons logged about 300 tax-professional data incidents in H1 2025, affecting up to 250,000 clients, after about 200 by spring 2024 [snippet: IRS/Security Summit].
  - About 600 a year spread over roughly 100–150K tax-preparation firms [estimate] gives 0.4–0.6% a year. That matches the claims mix.
- **Litigation.**
  - About 1,822 data-breach class actions were filed in 2025, up 18% on 2024 and more than 200% on 2022 (Duane Morris Class Action Review 2026) [data].
  - The ITRC counted 3,322 publicly reported compromises in 2025 [data].
  - Filings cluster on SSN breaches, and CPA firms are in the plaintiffs' pipeline: Forrestall CPAs, MBE CPAs and Schiff & Associates were all under investigation in 2025–26 [snippet].
  - I use a 25–35% chance of a suit after a notified breach of about 31,000 SSN-bearing records [estimate].
  - Courts dismiss more cases, and few reach class-certification rulings [data: Duane Morris]. So depositions are uncommon, and settlements often come early.

### Tier A

**A1. Paying a ransom is never required.**
- **Scenario.** Ransomware encrypts the file server. Cedar Ridge won't pay, and recovery takes three weeks. The insurer argues that paying would have cut this to one week, so two weeks of BI came from failing to take reasonable steps.
- **Frequency.**
  - Ransomware is about 0.25% a year. Most victims don't pay: 86% refused at Coalition [prior], and data-theft-only payments fell to a record-low 15% in Q2 2026 [data: Coveware].
  - A mitigation fight needs three things together: a refusal, slow or failed backups, and an insurer willing to argue the point. I put that at 1–5% of ransomware claims. I know of no reported US case where an insurer cut BI because the insured refused to pay.
  - 0.25% × 1–5% gives 0.003–0.013% a year.
- **Severity.** One to three extra weeks. Most CPA work is deferred rather than lost, so net BI is about $5–15K a day, or $50–300K.
- **EV.** 0.0001 × $150K ≈ $15 a year.
- **Side effects.**
  - Insurers usually prefer that the insured not pay, since the ransom is covered loss. Coveware (July 2026) also says re-extortion after payment is increasingly common [snippet].
  - So the clause costs almost nothing. The real-world friction runs the other way: the insured wants to pay and the insurer is slow to consent. A1 doesn't touch that.
  - The pre-payment report to the FBI or CISA mainly protects the insurer's OFAC position. It matters in about 0.25% × 15% ≈ 0.04% of policies a year.
- **Verdict.** Keep the one-sentence version and the back-page line. It is reassurance at near-zero cost. Don't present it as protection.

**A2. Security terms count only when they mattered.**
- **What already happens.**
  - The known-exploited-vulnerability (KEV) coinsurance already applies only to incidents the vulnerability causes.
  - The callback cap already applies only when someone acts on an unverified request, with a one-slip rule.
  - Only the ransomware coinsurance lacks a causation test, so that is where A2 bites.
- **Frequency.**
  - Cedar Ridge earns the backup credit, but its June 2026 restore test lapses in June 2027, four months before the policy ends [prior].
  - Chance the credit is lost or disputed at a ransomware event: about 37% of the year × 50% not retested ≈ 18%, plus 5% for other disputes, ≈ 23%.
  - Chance the gap didn't matter, because backups worked anyway or the attack was data theft only: about 50% [estimate].
  - Cedar Ridge: 0.25% × 23% × 50% ≈ **0.03%** a year. An insured without the credit: 0.25% × 50% ≈ **0.12%**.
- **Severity.** 20% × $150–300K of restoration and BI from encryption (after T2-6 narrows it) = $30–60K.
- **EV.** About $14 for Cedar Ridge. About $55 for an insured without the credit.
- **Insurer cost.** The same amounts, plus a forensic causation note of about $2–5K on each coinsurance claim. Moral hazard is small, because the coinsurance still bites when backups actually fail.
- **Verdict.** Keep with change.
  - Keep three things: the rule that backups which worked cancel the coinsurance; the limit to encryption losses (T2-6); and the list of three terms in IV.1 (T2-17).
  - Drop the insurer-burden causation test for the callback cap. That cap is already objective.

**A3. One payment-fraud trigger, with bank and client accounts.**
- **The gap today.**
  - Cedar Ridge runs payroll for 40 clients through its payroll platform [prior].
  - As drafted, Coverage H pays only when an employee is deceived, and only from the firm's accounts or accounts it holds for clients.
  - Three realistic paths fall outside:
    - a partner, who is an executive and not an employee, approves the transfer;
    - the bank itself is deceived;
    - a client's own account is debited, for example after a fake request changes a client employee's direct-deposit details.
- **Frequency.**
  - Fraud events run about 0.6% a year.
  - Share in the gaps: executive deceived 15–25%, bank deceived 5–10%, client-account social engineering 15–25%. That totals 35–55% [estimate].
  - I use 40%, because some client-account losses might reach Coverage I if there was a security failure and a written demand.
  - 0.6% × 40% ≈ **0.25% a year** (range 0.15–0.45%).
- **Severity.**
  - Wires average $141–208K [prior]. Payroll diversions are smaller, about $10–80K. A blend is about $100K gross.
  - Net of the $2.5–7.5K retention and partial recoveries, it is about $70K. On recoveries: IC3's Recovery Asset Team froze funds in 58% of cases, and At-Bay found 70% of victims who reported within 3 days recovered some money [prior].
- **EV.** 0.0025 × $70K ≈ **$175 a year** (range $90–450).
- **Tail.** A whole payroll batch for a 100–200-person client is $200–400K, and the firm may owe it to the client. Coverage H's $250K cap binds here, so the optional $500K limit (Coverage R) matters for payroll firms.
- **Insurer cost.**
  - The same $150–400 (3–7% of premium) against the form as drafted. About $0 against T2-1 and T2-1a, which A3 replaces.
  - Adverse selection toward payroll and bookkeeping firms: rate on client payroll volume (T3-1).
  - Claims friction falls, since there are no fights over who was deceived. No accumulation.
- **Verdict.** Keep, as the first priority.

**A4. Limits map and cross-coverage caps.**
- **Today.** Item 6 doesn't say whether sublimits are per incident or per period, or whether the system-failure cap spans D and F. After *CiCi* [prior], a court may refuse to apply an unlabeled cap across coverages. That ambiguity favors the insured.
- **Frequency.** A system-failure outage past the waiting period is about 0.5–1% a year [estimate]. Losses approach $250K in 2–5% of those, so 0.01–0.05% a year.
- **For the insured.** A4 makes the cap enforceable, so the insured gets *less* in exactly those cases. Clarity roughly offsets that. EV is about −$5 to +$5.
- **For the insurer.** Large. The cap is the main defense when a CrowdStrike-type event hits every policy at once; insured loss estimates for that event ran $300M–$1.5B [prior].
- **Verdict.** Keep as drafting hygiene. Call it clarity, not a benefit.

**A5. Related incidents are one incident, in the earliest period.**
- **Today.** Related incidents already count as one incident, and related claims as one claim. The real gap is timing: a class action filed after renewal over a breach reported the year before. Fixing that is T2-1c's job.
- **Frequency.**
  - Class-action path: breach with notice 0.5% × suit 25–35% × lands in a later period 50% × a two-policy dispute 20% ≈ 0.01–0.02% a year.
  - Re-extortion path: 0.25% × 10% × 20% ≈ 0.005% a year.
  - Total is about 0.02–0.05% a year [estimate].
- **Severity.** From a second $7.5K retention up to a $150–300K gap on a class action.
- **EV.** 0.0003 × $80K ≈ $25 (range $10–40).
- **Side effect.** The earliest-period rule leaves a long campaign on year 1's limit.
- **Verdict.** Keep with change. Fold it into T2-1c and keep the continuity sentence for customers switching from another insurer.

**A6. One retention per policy year.**
- **Frequency.**
  - At-Bay says firms hit once are twice as likely to be hit again within two years [snippet].
  - Chance of a second unrelated claim in the same policy year, given a first: about 2 × 1.6% × 0.5 year ≈ 1.6%. Joint chance: 1.6% × 1.6% ≈ **0.03% a year**.
  - Small incidents rarely stack below the retention, because Coverage A already absorbs them at $0.
- **Severity.** $2.5–7.5K, which is 0.03–0.09% of revenue.
- **EV.** 0.0003 × $7.5K ≈ $2, up to about $10 counting small incidents.
- **Cost.** $2–10 per policy; report 10 said $1–2 [prior]. After one retention the insured has no skin in the game for the rest of the year, but that effect is minor.
- **Verdict.** Drop from the core. If kept, call it a sweetener, not protection.

**A7. An external early warning is always a suspected incident.**
- **Today.** Coverage A already responds to suspected incidents, and calling never counts against the claim-free reduction or renewal pricing. T2-1f adds a reasonably suspected incident to the trigger.
- **Frequency.**
  - CISA has sent more than 4,300 pre-ransomware notifications since early 2023, about 1,500 a year nationwide [snippet]. For one firm that is well under 0.1% a year.
  - The common alerts come from the IT provider, the EDR tool or the bank. They lead to a hotline call in 3–10% of years [estimate].
  - A dispute over whether the suspicion was reasonable arises in about 5% of those, so 0.15–0.5% a year.
- **Severity.** $3–15K of triage, inside Coverage A's $25K.
- **EV.** 0.003 × $8K ≈ $25.
- **Loss prevention.** CISA claims about $9B of damage prevented [snippet; self-reported]. That value flows mostly to the insurer, through fewer ransomware claims.
- **Cost.** $25–60 more Coverage A use, offset by avoided losses.
- **Verdict.** Keep with change: one sentence inside T2-1f, and no separate definition list.

**A8. Foreign privacy regulators.**
- **Frequency.** Breach 0.5% × foreign-resident data involved about 10% × a foreign regulator acting against a small US firm about 1% ≈ 0.0005% a year [estimate].
- **Severity.** $20–50K of defense. **EV under $1.**
- **Today.** Arguably covered already: the definition doesn't say the agency must be American, and ambiguity favors the insured.
- **Verdict.** Drop. Add it only for firms with foreign customers.

**A9. Court attendance.**
- **Frequency.** Breach with notice 0.5% × class action 25–35% × a partner attends a mediation or deposition 30–50% ≈ 0.04–0.09% a year. Early dismissals and pre-certification settlements make depositions rare; mediation days are more common [estimate from Duane Morris data].
- **Severity.** 2–6 person-days × $500 = $1–3K. A partner's real billable day is about $2.4–4K ($300–500 an hour × 8) [estimate], so the clause pays about 15–20% of it.
- **EV.** 0.0006 × $2K ≈ $1.
- **Cost.** $2–5, plus tracking days.
- **Verdict.** Drop. At this size it has no real claims relevance.

**A10. Cloud-account tie-breaker and a narrower exclusion 12.**
- **Part (a), today.** A cloud tenant is arguably both the insured's own computer system and a dependent system (T2-0). If an attack at the vendor is filed as dependent-only, E pays BI. Restoration (F), extortion (C) and payment fraud (H) are then disputed.
- **Part (a), numbers.**
  - Third parties were involved in 48% of breaches (DBIR 2026) [prior]. Vendor-caused claims are 14% of At-Bay's claims, averaging $145K [prior].
  - So 1.6% × 14% ≈ 0.22% a year of claims involve a vendor. The fight over which coverage pays changes the outcome in 10–40% of those, so 0.02–0.09% a year.
  - Severity is $25–150K. EV: 0.0005 × $60K ≈ **$25** (range $10–60).
- **Part (b).**
  - The October 20, 2025 AWS outage ran about 15 hours. It began with a race condition in DynamoDB's automated DNS management, inside AWS [snippet].
  - Today, exclusion 12's carve-back for dependent providers already saves that event. The risk appears only once T2-4 narrows the carve-back, so (b) is a required companion to T2-4.
  - For Cedar Ridge, which has no Coverage P, it is worth $0.
  - For P buyers: P-covered loss from outages over 8 hours is about $300–600 a year, and the DNS share is 20–30%, so about $50–150 [estimate].
- **Accumulation.** Part (b) keeps cloud outages inside P, so P needs its widespread-event cap.
- **Verdict.** Keep both parts.

### Tier B

**B1. Impersonation and deepfake response.**
- **Today.** Nothing is covered, because impersonation without a breach isn't an incident. Only the $2.5K pre-incident advice applies.
- **Evidence.**
  - The IRS and the Security Summit repeatedly warn tax professionals about impersonation and "new client" scams [prior].
  - Gartner found 62% of organizations saw a deepfake attack in the prior year [snippet]. That was a large-enterprise survey and counts attempts.
  - Coalition says deepfakes are still a small fraction of its claims [prior].
- **Frequency.** A response costing more than the $2.5K retention: 0.3–1% a year [estimate].
- **Severity.**
  - Takedowns: $1–5K.
  - A warning to about 2,800 clients: $2–5K.
  - PR and legal: $5–15K.
  - Total $5–25K, or $3–20K net of the retention.
- **EV.** 0.006 × $7K ≈ **$40** (range $15–80). No tail, because of the $25K cap.
- **Cost.** $40–100 including admin (0.7–1.8%). There is friction in defining an impersonation event and proving costs. Accumulation is low.
- **Verdict.** Make optional, at about $75. It fills a real tax-season gap, but a small one.

**B2. Executives' personal funds.**
- **Frequency.** Firm breach about 0.5–1% × attackers pivot to a partner's personal money with a real loss 2–5% ≈ 0.02–0.05% a year [estimate].
- **Severity.** Regulation E largely protects consumer accounts if the loss is reported fast, and homeowners identity-theft endorsements exist. Net loss is $0–25K, mostly $0–5K.
- **EV.** $2–5.
- **Side effects.** Every claim needs proof that the personal loss came from the firm breach. That invites disputes and padded claims.
- **Verdict.** Drop.

**B3. AI voluntary shutdown.**
- **Today.** Cedar Ridge uses Copilot for drafting and has no agent that acts without approval [prior]. Switching it off costs staff time, not income, and stays under the 8-hour wait.
- **EV.** $0–2.
- **The real value is elsewhere.** T2-5's routing treats a hijacked agent as a security failure and a malfunction as a system failure under the cap. That protects the insurer if one model-vendor update hits many insureds at once.
- **Verdict.** Drop the clause and keep T2-5.

**B4. Coinsurance only above the first $50K.**
- **Frequency.** The coinsurance applies in about 0.06% a year for Cedar Ridge (a lapsed test) and 0.25% for an insured without the backup credit (from A2).
- **Severity.** At most 20% × $50K = $10K.
- **EV.** $3–30.
- **Side effect.** It returns money on the small and mid-size losses the coinsurance exists to deter. That weakens the backup incentive where most ransomware claims sit: $168K average without BI [prior]. A2's backups-that-worked rule already fixes the genuinely unfair case.
- **Verdict.** Drop. Negative.

**B5. Define verified backups.**
- **Today.** The backup credit turns on a restore test within 12 months and an offline or immutable copy. The scope is vague: Cedar Ridge tested its file server, not Microsoft 365 [prior].
- **Frequency.** A fight over backup status: ransomware 0.25% × 20–30% ≈ 0.05–0.08% a year.
- **Severity.** The 20% coinsurance, $30–60K.
- **Claims EV.** About ±$10, because a precise list can cut either way.
- **The bigger value is before any loss.**
  - Only 54% of ransomware victims restored from backups in the Sophos 2025 survey, the lowest in six years [data].
  - At-Bay's ransomware claims average $510K with BI and $168K without [prior].
  - A precise standard targets the failure mode that turns the first into the second: an immutable copy, MFA on the backup console, and separate credentials.
- **Cost and risk.** No cost; it reduces loss. The risk is that more conditions give more ways to lose the credit after a loss.
- **Verdict.** Keep with change.
  - Put the checklist in the application and the evidence (T3-7), and test it at bind.
  - Keep the policy definition short and outcome-based.
  - Measure the 12 months from inception or from the incident, whichever helps the insured.

**B6. Warning and cure before a post-loss duty.**
- **Frequency.** Claim 1.6% × a cooperation or document dispute serious enough to threaten payment 1–2% ≈ 0.02–0.03% a year. B6 flips perhaps a third of those.
- **Severity.** $50–200K.
- **EV.** 0.0002 × $100K × 30% ≈ $5.
- **Side effect.** A 30-day cure step on each document request slows every claim.
- **Verdict.** Drop, or keep one sentence. Whether Colorado already requires prejudice is for the law report.

**B7. You need answer only what we asked.**
- **Today.** Honest mistakes only lead to re-rating, and rescission needs a knowing, intentional misstatement. *Travelers v. ICS* involved a question that was asked [prior], so B7 would not have helped there.
- **Frequency and severity.** 0.02–0.05% a year. At stake is $10–30K: a lost credit or an added coinsurance.
- **EV.** About $5.
- **Side effects.** Insureds have slightly less reason to volunteer bad news. It also pushes the insurer to ask better questions (T3-1), which is good.
- **Verdict.** Keep with change: one line in V.3, paired with T2-13.

**B8. Retention billed last, in six installments.**
- **Value.** Deferring $7.5K by about 3.5 months at 10% is about $220 per claim. At 1.6% a year, EV is about **$3**. For an $8.5M firm, $7.5K is not a cash crisis.
- **Cost.**
  - Bad debt of 5–10% of billed retentions: 1.6% × $7.5K × 7% ≈ $8, plus collection admin, so $5–15.
  - The insurer ends up collecting from a claimant right after a loss.
  - The insurer also pays the first-dollar vendor bills, so the insured has no reason to check them.
- **Verdict.** Drop. Negative. Handle hardship case by case in claims.

**B9. Security services with a no-forfeiture promise.**
- **The clause.** There is no service program today, and nothing says ignoring a service reduces cover, apart from the KEV notice. So the promise changes almost nothing: about $5 a year.
- **The services.**
  - At-Bay says no MDR customer filed an Akira claim in 2025, and its ransomware frequency is 7 times below the industry [snippet; marketing claim].
  - If services cut Cedar Ridge's claims by about 30% [estimate]:
    - the insured avoids 1.6% × 30% × about $25K of retention and uninsured costs ≈ **$120 a year**;
    - the insurer avoids 1.6% × 30% × $170K ≈ **$800 a year**.
- **Cost.** Alerts, scans and phishing training cost about $50–200 per policy [estimate]. MDR for about 70 endpoints costs about $10K+ a year [estimate], which is more than the premium, so it must be sold, not given.
- **Risks.** Liability if a service fails; widening of the scan promise (do T2-7 first).
- **Verdict.** Keep with change, as the hybrid in report 10.

**B10. Verified-framework tier.**
- **Outcome change.** None on claims, since it is never a condition.
- **Value to the insured.** A premium credit of perhaps 5–10% ($275–550) [estimate], and a shorter renewal.
- **Value to the insurer.** Better selection.
- **Risk.** An IT provider's attestation can be a rubber stamp. It also creates new misrepresentation arguments unless the V.3 protections cover it.
- **Verdict.** Make optional, as a rating-plan item that replaces the per-control credits (T2-16).

**B11. Earn credits mid-term.**
- **Frequency.** A firm adds a control mid-term (10–20%) × a claim in the rest of the term (about 0.8%) ≈ 0.1% a year.
- **Severity.** The retention difference, $2.5–5K, plus the 4-hour wait for MDR.
- **EV.** About $4. It gives a small nudge to adopt controls sooner.
- **Verdict.** Keep as one line. It mirrors the existing rule for losing a credit mid-term.

**B12. $0 retention on panel forensics and breach coach.**
- **Today.** Coverage A gives 72 hours and $25K at $0. A BEC mailbox review often runs 2–4 weeks, so the later costs fall under B with the $7.5K retention. Crisis response (forensics, notification and PR) is about half of SME incident costs [data: NetDiligence 2025].
- **Frequency.** Investigations running past 72 hours (1–1.5% a year) × ending with nothing to notify, so the retention sits on the forensics (about 60%) ≈ 0.7% a year [estimate].
- **Severity.** Up to $7.5K, average about $5K.
- **EV.** 0.007 × $5K ≈ **$35** (range $25–50). The cost is similar.
- **Verdict.** Drop. A simpler fix does the same job: let Coverage A's $25K run for about 14 days instead of 72 hours.

**B13. Policy at a glance.**
- It changes no loss.
- It delivers the plain-English notes the cover already promises, which is currently a failed cross-reference [prior].
- The only risk is contradicting the wording.
- **Verdict.** Keep, as documentation. Cosmetic.

**B14. Renewal "what changed" table.** No loss value. **Verdict:** take it out of the form and do it as a renewal practice.

**B15. Legal clock card.**
- The breach coach inside Coverage A already gives notice deadlines.
- Chance a card saves a missed deadline: 0.5% × 2–4% ≈ 0.01–0.02% a year. Late-notice penalties are about $10–50K, so **EV is $2–5**.
- A stale card can mislead.
- **Verdict.** Put it in the welcome pack, not the policy.

**B16. Publish claims results.**
- No value to the insured.
- Published misses against the service aims hand plaintiffs a yardstick under Colorado's unreasonable-delay statute [prior].
- **Verdict.** One rationale line at most.

### Tier C

**C1. Fast Downtime Payment.**
- **Today.**
  - A cloud failure without an attack is not covered, because Cedar Ridge didn't buy Coverage P.
  - Attacks are paid under D or E after 8 hours, with a firm 50% advance within 10 business days of confirming cover.
- **Cloud-trigger frequency.**
  - Parametrix counted 45 critical cloud interruptions in 2025, totaling 175 hours (about 4 hours each), and six events over 10 hours in 2024 [data, via snippet].
  - AWS us-east-1 has had roughly one event over 8 hours every two to three years [estimate]; the October 2025 one ran about 15 hours [snippet].
  - Through its tax, payroll and portal vendors, Cedar Ridge might see **0.2–0.4 qualifying events a year** [estimate].
- **Payout per event.**
  - The 8-hour threshold runs on the clock, and only business hours after it pay.
  - The October 2025 AWS event began about 1 a.m. Mountain time, so about 7 business hours would have paid, about $7K.
  - I use an average of about $4K. **Payout EV: $800–1,600 a year.**
- **Real loss.**
  - Cedar Ridge tolerates 1 day of downtime in tax season and 3 days otherwise [prior].
  - Most lost hours are deferred work. The true loss is maybe 20–40% of the payout, about $200–600 a year [estimate].
  - The outages that really hurt CPA firms ran for days: CCH malware in May 2019 (3–5 days; the IRS granted a 7-day extension) and Kronos payroll ransomware in December 2021 (several weeks) [snippet].
  - CCH Axcess logged 12 outages from February 2025 to date, and the ones reported ran about 30 minutes to 2 hours [snippet: StatusGator].
- **Timing value of the attack trigger.** $40K arriving about 4 weeks sooner than the V.7.4 advance, at 10%, is about $300. Times 0.25%, that is under $1 a year.
- **Cost.**
  - Technical premium ≈ payouts ÷ 0.6 ≈ **$1.3–2.7K**, or 25–50% of the premium.
  - Accumulation: one us-east-1 event triggers every CPA insured on the same software. For 5,000 insureds, $7K each is about $35M. That is more than the class's annual premium of 5,000 × $5.5K ≈ $27.5M [estimate].
- **Verdict.** Make optional, and don't offer it to the CPA class. For CPA firms, offer P with a 24-hour wait, which targets the multi-day events.

**C2. One limit reinstatement.**
- **Frequency.**
  - A first loss must use most of the $1M. Ransomware with recovery costs averages $961K (NetDiligence 2025) [prior], but claims over $1M are perhaps 1–3% of SME claims [estimate]. So 1.6% × 2% ≈ 0.03% a year.
  - An unrelated claim in the rest of that year is about 1.6%, so the joint chance is about 0.0005% a year.
- **Severity.** About $150K. **EV under $5.**
- **Comparison.** A $2M aggregate responds whenever a single loss exceeds $1M: about 0.02–0.05% a year × about $300K of excess ≈ $60–150 a year [estimate]. That is 10–30 times the protection.
- **Cost.** Reinsurers load reinstatements; perhaps 3–8% ($165–440) [estimate].
- **Verdict.** Drop. Make the $2M and $3M limit options real (README row 1) [prior].

**C3. AI regulatory defense.**
- Colorado SB 26-189 takes effect on January 1, 2027 [prior]. Enforcement is by the Attorney General (the law report should confirm).
- Cedar Ridge uses AI to draft, not to make consequential decisions about people [prior].
- **Frequency** 0.001–0.01% a year; **severity** $25–100K. **EV $1–5.**
- **Verdict.** Drop for now, and revisit when enforcement data exists.

**C4. $0 retention with qualifying MDR.**
- Cedar Ridge has no MDR, so it is worth $0 today.
- **For MDR buyers.** Claim frequency is about 1% a year [estimate: they are better risks] × $3.75–5K of retention saved ≈ **$40–50 a year**.
- **Where the value sits.** The loss reduction comes from MDR itself; the $0 retention is a sales hook.
- **Moral hazard.** Small: vendors bill without the insured checking.
- **Verdict.** Make optional. It replaces the halved retention rather than stacking on it (T2-16).

**C5. Goodwill payments to clients.**
- **Frequency.** A breach with notice: 0.4–0.6% a year.
- **Severity.** $10–25 × about 2,800 clients ≈ $30–70K of spending.
- **Why it adds little.**
  - US practice already covers credit monitoring for 24 months, and Coverage N covers lost profit.
  - Evidence that small gestures reduce churn or lawsuits is thin.
  - Paying for spending that happens only because it is covered is moral hazard.
  - Payments to potential class members could complicate a later settlement.
- **EV.** Payments of about $50–150 a year, but real value lower.
- **Verdict.** Drop.

**C6. Lookalike-domain client fraud.**
- **Today.** Invoice fraud is covered only if a security failure at the firm let criminals send the fake invoices.
- **Frequency.** In Coalition's data, 39% of funds-transfer-fraud claims had no confirmed email compromise [prior], so spoofing without a breach is common. For clients of a CPA firm this size paying a fake invoice: 0.3–1% a year [estimate].
- **Severity.** Diverted fees of $10–100K. The policy pays cost, not profit, so $7–70K. CPA firms often write these off to keep the client.
- **EV.** 0.005 × $15K ≈ **$60** (range $30–150).
- **Cost.** $100–200 (2–4%). Proving that a client paid a fake account with no breach is hard, and there is a collusion risk.
- **Verdict.** Make optional for invoice-heavy classes such as contractors and distributors. Low for CPA firms.

**C7. Risk classes.**
- No claim outcome changes.
- A shift toward eligibility means fewer firms insured and more control conditions in play after a loss.
- **Verdict.** Drop from this version. Keep it as an underwriting guideline.

**C8. Distribution ideas.**
- Not a wording question, and no protection for the insured.
- **Verdict.** One strategy line at most.

---

## 4. Ranked list, by utility

Order within each band is by expected value plus tail value, less insurer cost and friction. EV is to Cedar Ridge unless noted.

| Rank | ID | Utility | EV mid $/yr | Insurer cost mid | Why |
| --- | --- | --- | --- | --- | --- |
| 1 | A3 | **High** | 175 | $150–400 vs today | Closes the fraud paths a payroll firm actually hits; $200K+ tail |
| 2 | A2 | Medium | 14 (55 without the credit) | $15–55 | Converts a 20% cut into full payment when the gap didn't matter |
| 3 | A10 | Medium | 25 (+50–150 for P buyers) | $20–40 | Settles which coverage pays in vendor-side events; needed with T2-4 |
| 4 | B1 | Medium | 40 | $40–100 | Real tax-season event with no cover today; small dollars |
| 5 | B5 | Medium | ±10 on claims; larger prevention value | ~0 | Fewer backup fights; targets the $168K vs $510K difference |
| 6 | B9 | Medium (services) | ~5 clause; ~120 services | $50–200 | Services reduce frequency; the clause itself adds little |
| 7 | C6 | Low (CPA) | 60 | $100–200 | Real gap, but CPA fees are small and proof is hard |
| 8 | A5 | Low | 25 | ~0 | Tail value, but T2-1c does the real work |
| 9 | A7 | Low | 25 | $25–60 | Restates Coverage A; encourages early calls |
| 10 | B12 | Low | 35 | $25–60 | Overlaps Coverage A; stretching A's clock is simpler |
| 11 | C4 | Low | 0 (40–50 for MDR buyers) | $40–50 | A hook to sell MDR |
| 12 | A1 | Low | 15 | $0–15 | Reassurance; the dispute is theoretical |
| 13 | B7 | Low | 5 | ~$5 | One line; keeps underwriting honest |
| 14 | B6 | Low | 5 | $5–15 + delay | Slows every claim for a rare benefit |
| 15 | C1 | Low (CPA) | 200–600 real; 800–1,600 paid | $1.3–2.7K | Pays for deferrable downtime; tax-season accumulation |
| 16 | B11 | Low | 4 | ~$5 | Symmetry with the credit-loss rule |
| 17 | A6 | Low | 2–10 | $2–10 | Sweetener, not protection |
| 18 | B10 | Low | 0 on claims | 5–10% credit | A pricing tool, not protection |
| 19 | A4 | Low (insured) | about 0 | Saves leakage | Hygiene that protects the insurer's caps |
| 20 | C5 | Low | 50–150 spent; low value | 1–2% | Covered spending, not covered loss |
| 21 | C7 | Low | 0 | n/a | Underwriting redesign |
| 22 | B13 | Cosmetic | 0 | Drafting | Fixes the cover's promise |
| 23 | B15 | Cosmetic | 2–5 | Upkeep | The breach coach already does it |
| 24 | B14 | Cosmetic | 0 | Admin | Renewal practice |
| 25 | B16 | Cosmetic | 0 | Bad-faith evidence risk | Rationale line only |
| 26 | C8 | Cosmetic | 0 | n/a | Not a wording question |
| 27 | C3 | Cosmetic | 1–5 | ~$5 | Law not in force; no loss data |
| 28 | A8 | Cosmetic | <1 | ~0 | Arguably covered already |
| 29 | B3 | Cosmetic | 0–2 | ~0 | No agents at Cedar Ridge; T2-5 does the work |
| 30 | B2 | Cosmetic | 2–5 | Small + friction | Reg E and homeowners cover most of it; causation fights |
| 31 | A9 | Cosmetic | 1 | $2–5 | Pays ~15–20% of a rare day |
| 32 | C2 | Cosmetic | <5 | 3–8% | A $2M limit protects 10–30x more |
| 33 | B4 | **Negative** | 3–30 | 0.5–1% for insureds without the credit | Blunts the backup incentive where most claims sit |
| 34 | B8 | **Negative** | 3 | $5–15 + collections | Costs more than it gives; adversarial after a loss |

**Totals (mid values):**
- **Tier A:** about $300 a year, of which A3 is about $175.
- **Tier B:** about $120 a year, counting the B9 clause only.
- **Tier C:** about $70 a year in the core sense. This excludes C1's payouts and C5's spending.
- **All 34:** about $480 a year.

---

## 5. Data gaps and what to verify

**Gaps that change the ranking if they are wrong**
1. **CPA-class frequency.** The 1.5× class factor behind the 1.82% case is an assumption [prior]. There is no public CPA or payroll-firm claim frequency. Ask a reinsurer or a program administrator. A3's value scales directly with this figure.
2. **Who is deceived in fraud claims.** No dataset splits executive vs employee vs bank-deceived vs client-account losses. The 35–55% gap share in A3 is judgment. Coalition and At-Bay claims teams could answer this in one table.
3. **Payroll-diversion severity at bookkeeping and payroll firms.** None was found. I used $10–80K per event.
4. **Coinsurance application and disputes.** There is no data on how often ransomware coinsurance is applied or contested. The claim-denial figures I found are low-quality vendor blogs ("21% denied or partly denied in 2025"; "34% of denials for missing controls") [snippet]. They should not be cited.
5. **Ransom mitigation disputes (A1).** I found no US case or dataset on an insurer reducing BI for refusal to pay. The frequency is judgment.
6. **Litigation depth.** Duane Morris gives filing totals [data], but not the share of small-firm breaches that are sued, or how often depositions and mediations happen. A9 and A5 rest on judgment.
7. **Outage durations that matter to CPA firms.**
   - Parametrix gives cloud-level totals [data].
   - StatusGator shows CCH Axcess outages are short [snippet].
   - There is no distribution of outages over 8 hours by region during US business hours, and none for tax or payroll software. Gusto had a payroll-running outage in March 2026, duration unknown [snippet].
   - C1 pricing needs this.
8. **Deepfake and impersonation at SMBs.** Vendor figures (Gartner's 62%; "average $450K loss") come from enterprise surveys or unsourced pages [snippet]. For small firms there is only Coalition's "small fraction" [prior].
9. **Executives' personal-fund losses (B2).** No data.
10. **MDR effect.** At-Bay's "no MDR customer had an Akira claim" and "7× below industry" are marketing claims [snippet]. There is no controlled frequency comparison.
11. **Share of claims over $1M for firms under $25M (C2, limits).** Not found. I used 1–3%.
12. **Coalition H1 2026.** No frequency or severity update was found beyond the privacy-claims blog [prior].

**Verify before quoting**
- Duane Morris Data Breach Class Action Review 2026: the 1,822 filings figure and its definition of a filing.
- ITRC 2025 Annual Data Breach Report: 3,322 compromises.
- IRS / Security Summit: about 300 tax-professional data incidents in H1 2025, and about 200 by spring 2024.
- Parametrix Cloud Outage Risk Report 2025: 45 critical events and 175.3 hours; the 2024 "six events over 10 hours".
- AWS October 20, 2025: about 15 hours; root cause in DynamoDB's DNS automation (the AWS post-event summary).
- CCH / Wolters Kluwer: **May 2019**, 3–5 days, IRS 7-day extension (Accounting Today, 2019).
- Kronos (UKG) December 2021 ransomware outage: duration.
- CISA pre-ransomware notifications: "more than 4,300" and the "$9B prevented" claim.
- Sophos State of Ransomware 2025: 54% used backups; 49% paid; sample of 100–5,000 employees.
- Coveware Q2 2026: exfiltration-only payment rate of 15%. Coveware July 2026 post on re-extortion.
- AFP 2026 Payments Fraud and Control Survey: 76%, 48% (under $1B) and 74% BEC; the respondent profile.
- At-Bay: "twice as likely to be hit again within two years"; the MDR and Akira statements.
- NetDiligence 2025: the SME share of claims and the crisis-response share of costs.

**Sources searched (search-result level, September 27, 2026)**
- [Coalition 2026 Cyber Claims Report](https://www.coalitioninc.com/announcements/2026-cyber-claims-report)
- [At-Bay 2026 InsurSec key findings](https://www.at-bay.com/articles/insursec-report-2026-key-findings-cyber-risk/); [Insurance Business on At-Bay](https://www.insurancebusinessmag.com/us/news/cyber/one-ransomware-crew-now-drives-half-of-all-cyber-claims-atbay-573139.aspx)
- [NetDiligence 2025 study (PDF)](https://rsmus.com/content/dam/rsm/insights/services/risk-fraud-cybersecurity/1pdf/net-diligence-cyber-claims-study-2025-report.inline.pdf); [Carrier Management](https://www.carriermanagement.com/news/2025/09/25/279803.htm)
- [Duane Morris Data Breach Class Action Review 2026](https://blogs.duanemorris.com/classactiondefense/2026/02/03/hot-off-the-presses-the-duane-morris-data-breach-class-action-review-2026-and-the-duane-morris-privacy-class-action-review-2026/); [Duane Morris Class Action Review 2026](https://www.duanemorris.com/pressreleases/duane_morris_class_action_review_2026_comprehensive_analysis_class_action_litigation_0126.html)
- [ITRC 2025 Annual Data Breach Report](https://www.idtheftcenter.org/post/2025-annual-data-breach-report-record-number-compromises/)
- CPA-firm breach investigations: [Forrestall CPAs](https://www.classaction.org/data-breach-lawsuits/forrestall-cpas-august-2026); [MBE CPAs](https://www.classaction.org/data-breach-lawsuits/mbe-cpas-may-2025); [Schiff & Associates](https://colevannote.com/2026/03/20/schiff-associates-cpa-data-breach-investigation/)
- [CISA pre-ransomware notifications](https://www.cisa.gov/news-events/news/getting-ahead-ransomware-epidemic-cisas-pre-ransomware-notifications-help-organizations-stop-attacks); [Cybersecurity Dive](https://www.cybersecuritydive.com/news/cisa-ransomware-warning-program-key-employee-left/808589/)
- [Parametrix 2025 cloud outage findings (Business Insurance)](https://www.businessinsurance.com/cloud-services-see-decline-in-downtime-in-2025-parametrix/); [Reinsurance News](https://www.reinsurancene.ws/critical-cloud-outage-risk-remains-significant-despite-decline-in-occurrence-parametrix/); [Parametrix 2024 report](https://www.parametrixinsurance.com/in-the-news/2024-cloud-outage-risk-report)
- [AWS October 2025 outage analysis (ThousandEyes)](https://www.thousandeyes.com/blog/aws-outage-analysis-october-20-2025)
- [Microsoft Exchange Online outage, Aug–Sept 2026](https://cybersecuritynews.com/microsof-new-exchange-online/)
- [CCH Axcess outage history (StatusGator)](https://statusgator.com/services/cch-axcess/outage-history); [Wolters Kluwer CCH outage, 2019 (Accounting Today)](https://www.accountingtoday.com/news/the-wolters-kluwer-cch-outage-what-happened); [IRS extension (Graham Cluley)](https://grahamcluley.com/irs-extends-tax-filing-deadline-following-attack-on-wolters-kluwer-cch-cloud-accounting-service/)
- [Kronos outage (HR Dive)](https://www.hrdive.com/news/all-hands-on-deck-for-hr-teams-as-kronos-outage-drags-on/611811/)
- [IRS data theft information for tax professionals](https://www.irs.gov/individuals/data-theft-information-for-tax-professionals); [CPA Practice Advisor, Aug 2025](https://www.cpapracticeadvisor.com/2025/08/28/irs-reminds-tax-pros-to-guard-against-id-theft/168077/)
- [AFP 2026 Payments Fraud and Control Survey](https://www.financialprofessionals.org/about/learn-more/press-releases/Details/over-75-percent-of-us-firms-experienced-payments-fraud-in-2025-while-ai-adoption-for-fraud-mitigation-lags)
- [Sophos State of Ransomware 2025](https://www.sophos.com/en-us/press/press-releases/2025/06/nearly-half-companies-opt-pay-ransom-sophos-report-finds)
- [Coveware Q2 2026 (Veeam)](https://www.veeam.com/blog/cyber-extortion-payment-trends-q2-2026.html); [Coveware, July 2026](https://coveware.com/2026/07/adverse-cyber-extortions-are-more-common-than-commonly-advised/)
- Deepfake statistics (low quality): [Keepnet](https://keepnetlabs.com/blog/deepfake-statistics-and-trends); [Eftsure](https://www.eftsure.com/statistics/deepfake-statistics/)
- Claim-denial statistics (low quality, not to be cited): [ASI Networks](https://www.asi-networks.com/blog/why-cyber-insurance-claims-get-denied/); [Cloud Secure Tech](https://www.cloudsecuretech.com/insights/will-your-cyber-insurance-claim-pay-out/)
- BI claim timing (low quality): [Pierson Ferdinand](https://pierferd.com/news/business-interruption-claims-in-cyber-insurance); [Raizner Law](https://www.raiznerlaw.com/insights/how-long-does-a-business-interruption-insurance-claim-typically-take/)
