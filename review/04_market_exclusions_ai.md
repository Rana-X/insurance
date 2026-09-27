# 04: Market economics, exclusion trends and AI: stress test of the Harborline SMB cyber policy

As of 2026-09-27. Analyst lens: traditional carriers, reinsurance and wording trends. Builds on round 1 (`ctx/round1_findings.md`) and does not repeat it, except where new evidence changes a round-1 point.

## 0. Method and evidence labels

- **WebSearch:** 22 of 22 searches used.
- **WebFetch:** every attempt was egress-blocked: content.naic.org, claimsjournal.com, beinsure.com, munichre.com, lmalloyds.com, westchester.com and herodevs.com. No blocked domain was retried. **So all web evidence below is "search-snippet" level**, meaning search-engine summaries of the page. Figures can be paraphrased or merged by the summarizer.
- Labels used:
  - **[S]**: search snippet, source named.
  - **[S-low]**: search snippet from an aggregator, blog or vendor. Treat as a lead, not a fact.
  - **[CAT]**: row in the local catalog (`/home/user/insurance/catalog/cyber_policies.csv`). This is metadata only; the document was not opened.
  - **[CTX]**: Harborline package files.
  - **[AK]**: analyst background knowledge, not re-verified in this pass. Flagged wherever it matters.
- Nothing here invents a clause number, date or figure. Where a snippet conflicts with another source, both are shown.

---

## Top findings (read this first)

1. **The market is soft and reinsurance is cheap.**
   - Rates: Marsh Q2 2026 shows US cyber rates down 2% (same as Q1; falling since Q2 2023), and global cyber down 4% (12th straight quarterly decline). CIAB Q2 2026 shows cyber down 3.2% on average (9th straight quarter). July 2026 cyber reinsurance renewals were down 10–20%, with lower attachment points. [S]
   - **Correction to round 1 / Claim Ledger C17:** a cyber-specific US figure (−2%) now exists in Marsh's Q2 2026 index. The rationale can say "U.S. cyber rates fell 2% in Q2 2026 (Marsh)", attributed.
2. **Loss ratios are rising while prices fall.**
   - 2025 US cyber loss ratio (direct loss plus DCC) was about 53%, up almost 6 points, and above 50 for the first time since the COVID-era ransomware spike (AM Best, via snippet).
   - Surplus lines now write **nearly two-thirds** of US cyber premium, at a loss ratio near 56. Admitted business ran at **50.2**. [S]
   - This helps the admitted case, but a new entrant is buying into falling price adequacy.
3. **Every systemic loss realized so far has been a non-malicious outage.** CrowdStrike 2024 insured-loss estimates ran $300M–$1.5B. CyberCube put the AWS October 2025 outage at $38M–$581M, clustered at the low end. JLR 2025 was a £1.9bn economic event with essentially no insurance recovery. [S] This supports Harborline's instinct to sublimit system failure. However, **Harborline leaks system-failure exposure at full limits in two places**: Coverage F restoration, and the AI-agent trigger (see 5.3 and 5.5).
4. **The war exclusion is structurally aligned with LMA5567/Beazley E15626 and meets the Lloyd's Y5381 criteria on its face.** It still needs four drafting fixes before reinsurer review (5.1):
   - an explicit "cyber operation in the course of war" limb;
   - a check for the LMA "retaliatory operations between specified states" limb [AK, verify];
   - a cloud "physically located" tie-breaker;
   - an impact threshold that drops LMA's "functioning of the state" qualifier and is therefore broader than LMA.
   The no-repayment, keep-paying-pending-attribution promise may sit net of reinsurance.
5. **The infrastructure exclusion's dependent-provider carve-back is too wide.** A power utility, ISP or DNS/CDN provider with a written or click-through agreement is a "dependent provider". So a cyberattack on a utility or telecom is carved back into Coverage E, which is the accumulation the exclusion exists to stop (5.2).
6. **The KEV 20% coinsurance is a defensible, more transparent alternative to Chubb's Neglected Software Exploit (NSE) endorsement.** Chubb's NSE gives 45 days of full cover, then gradually shifts risk to the insured. Harborline's rule has three weaknesses:
   - it jumps straight to 20% instead of stepping up;
   - it never escalates for long neglect;
   - it **conflicts with Harborline's own "what our scan saw, we accept" estoppel** (Section V.3.4).
7. **The affirmative AI clause is now market-standard, not market-leading.**
   - Coalition added it in 2024–25. Beazley confirmed affirmative AI cyber cover and launched AI Voluntary Shutdown and AI Regulatory Defence & Penalties endorsements (September 17–24, 2026). CFC added affirmative AI cover (September 2026). [S]
   - "AI agent exceeding its authority" as a security failure is genuinely ahead of the market; no competitor definition was found. But it is under-engineered: it bypasses the $250K system-failure sublimit, turns on prompt text ("written instructions"), and has no event aggregation.
8. **AI exclusions are spreading in general liability and management liability, not in cyber.**
   - ISO CG 40 47 / CG 40 48 / CG 35 08 (01 26) are **optional** GL endorsements (Gallagher, via snippet).
   - Berkley's absolute AI exclusion is PC 51380 00 in D&O/E&O/fiduciary. [S]
   - No major carrier with an absolute AI exclusion in standalone cyber was found in this pass.
   - Harborline's rationale wording ("on general liability forms since January 2026") overstates adoption and should read "available as optional ISO endorsements since January 2026".
9. **Admitted paper is sensible for a $1M–$50M SMB launch, with conditions:**
   - roll out state by state;
   - get quota-share or fronting capacity;
   - accept slower rate moves in a soft market;
   - expect form review of the novel clauses: KEV coinsurance, estoppel, attribution, arbitration, AI agent.

---

## 1. Market structure and economics, 2025–2026

### 1.1 US premium, loss ratios, admitted vs surplus lines

| Metric | Figure | Source / label | Note |
|---|---|---|---|
| 2024 US cyber direct written premium (DWP) including alien surplus lines | $9.14B, down 7.11% from $9.84B (2023); "first premium decline in the market's history" | NAIC 2025 Report on the Cybersecurity Insurance Market [S] | Report PDF was blocked; snippet only |
| 2024 DWP by US-domiciled insurers | $7.08B | NAIC 2025 report [S] | Consistent with AM Best's statutory figure below |
| 2024 AM Best US cyber DPW | $7.075B, −2.3%; loss ratio 48.8% vs 41.6% (2023) | AM Best Market Segment Report (Business Wire, June 23, 2025) [S] | WTW also cites DWP −2.3% in 2024 [S] |
| 2024 "combined loss ratio" | 47% ("third consecutive year of profitable results") | Snippet attributed to NAIC report or an aggregator [S-low] | Conflicts with AM Best's 48.8%. Definitions differ (direct loss vs loss plus DCC; alien surplus lines in or out) |
| 2024 claims | ~50,000 claims filed, +40% year on year | NAIC-report snippet [S] | |
| 2024 premium by policy type (reclassified) | Primary 65%, excess 31%, endorsement 4% | NAIC-report snippet [S] | |
| **2025 premium growth** | Fitch: US cyber "swung to 7% written premium growth in 2025" | The Insurer, June 3, 2026 [S] | Another snippet says "nearly 11%". A Claims Journal headline (June 30, 2026) reads "Flat Premium". **Unresolved.** Bases likely differ (standalone vs total; AM Best vs Fitch) |
| **2025 loss ratio** | Direct loss plus DCC rose "almost 6 percentage points to 53%"; first time over 50 since the COVID-era ransomware spike | AM Best via Claims Journal, June 30, 2026 [S] | More third-party claims drove the rise (headline) |
| **Admitted vs surplus lines (2025)** | Surplus lines "nearly two-thirds of all cyber insurance premium", loss ratio "nearly 56"; admitted loss ratio 50.2 | Same AM Best coverage [S] | Key input for the admitted decision (5.6) |
| Policies in force (2025) | +34% | Same snippet cluster [S] | Unit growth far outpaces premium growth, so average premium is falling |
| Top writers (2025 standalone) | Beazley USA No. 2 with $493.9M DPW, up from No. 10 | AM Best, Best's Rankings [S] | |
| NAIC 2026 report (2025 data) | Not found in search | n/a | Treat any "2026 NAIC" figure as unverified |
| Global market | ~US$15bn (2025); ~US$28bn forecast by 2030 | Munich Re, *Cyber Insurance: Risks and Trends 2026* [S] | Page blocked. Main loss drivers: ransomware, data breach, BEC, DDoS |
| S&P | *Cyber Insurance Market Outlook 2026: Resilient Earnings, Tougher Competition, Pockets of Growth* | S&P Global Ratings [S, title only] | No figures captured |

**Read-across:** the US market is growing in units (SMB-led) and shrinking or flat in rate. Loss ratios have risen two years running (roughly 41.6 → ~48 → ~53), from lower rates and more third-party and privacy claims. That fits the At-Bay and Coalition privacy-claims data already in Harborline's sources. Harborline's "priced near the upper market" stance (rationale) is coherent against this backdrop. Its illustrative premium is still not actuarially grounded, as round 1 found.

### 1.2 Rate trends through Q2/Q3 2026

| Source | Period | Cyber rate signal | Label |
|---|---|---|---|
| Marsh Global Insurance Market Index | Q2 2026 (released July 2026) | Global cyber −4% (12th consecutive quarterly decline; Q1 was −5%). **US cyber −2%, same as Q1; US cyber falling since Q2 2023.** Regional range: IMEA −14% to US −2% (LAC −10%). Global composite −6% | [S] Marsh press release; Insurance Journal July 23, 2026 |
| CIAB P&C Market Survey | Q2 2026 | Cyber premiums −3.2% on average; 9th consecutive quarter of decreases | [S] CIAB / Insurance Journal Aug 20, 2026 |
| WTW Insurance Marketplace Realities 2026 (Oct 2025) and Spring Update (May 2026) | 2025–H1 2026 | Flat primary and excess renewals; ample capacity; "early indicators in 2026 point to a deceleration in the rate of market softening" | [S] |
| Amwins *State of the Market: 2026 Outlook* | 2026 | Renewals level or below expiring; capacity from new entrants and expanding carriers, "including limits up to $10 million"; tighter terms for SAM and cyber-adjacent exposures | [S] |
| Aon, Gallagher | 2026 | No cyber rate figure retrieved in this pass | Gap |
| Q3 2026 indices | n/a | Not yet found (Marsh Q3 not surfaced) | Gap |

### 1.3 SMB penetration and take-up (low-quality evidence; surveys conflict)

| Claim | Source | Label |
|---|---|---|
| 10–20% of small businesses and 5–10% of micro-enterprises have cyber insurance | Swiss Re estimate quoted by an aggregator | [S-low] |
| 70% of businesses say they buy cyber insurance (highest since the index turned cyber-focused in 2018) | Travelers Risk Index (Claims Journal, Sept 23, 2026) | [S] (includes embedded/BOP cover; self-reported) |
| ~71% SME uptake "helped by bundled cyber clauses in commercial policies" | Hiscox 2025 SME survey, via aggregator | [S-low] |
| UK small businesses with cyber insurance: 62%, up from 49% in 2024 | aggregator | [S-low] |
| SMBs carry the greatest uninsured cyber risk globally | Munich Re (Global Cyber Risk and Insurance Survey 2026 exists; not read) | [S] |

Takeaway: "has cyber" survey numbers (60–70%) largely count BOP-embedded, low-limit cover such as HSB Cyber Suite. **Standalone** SMB penetration is much lower; the 10–20% estimate is the only standalone-style figure found, and it is low quality. For Harborline, the addressable market is mostly SMBs with embedded sublimits (often $50K–$100K [AK]) who need a real standalone limit. That supports the "core that can't be forgotten" design.

### 1.4 Reinsurance and cat-bond capacity

| Item | Finding | Label |
|---|---|---|
| July 1, 2026 cyber reinsurance renewals | Reductions of 10–20%. Brokers: 15–20% on best programs; reinsurers: 10–15%. Attachment points moving lower | The Insurer (June 17, 2026); Guy Carpenter "July 1, 2026 reinsurance renewals: cyber" (title); Lockton July 2026 [S] |
| January 1, 2026 | "Cyber aggregate excess-of-loss rates fell by 32%" | [S-low]: attribution unclear (possibly a Guy Carpenter renewal report) |
| Cat bond market overall | Record ~$65.6bn outstanding at end Q2 2026; H1 2026 issuance a record $17.3bn (AM Best) | Artemis Q2 2026 report; The Insurer Aug 27, 2026 [S] |
| Cyber cat bonds | Cyber share "just 0.19% of new issuance year-to-date in 2026"; "no 144A cyber catastrophe bonds in 2026 so far" | Artemis [S] |
| Conflicting item | Hannover Re parametric cyber cat bond "Series 2026-1" of $300M, described as "the biggest cyber catastrophe bond so far" | [S]. **Conflicts** with "no 144A cyber cat bonds in 2026"; it may be a private or non-144A deal or mis-dated. Unresolved |
| Outlook | "Cyber ILS primed for future growth if traditional capacity constraints emerge" (S&P) | Artemis [S] |

**Read-across for Harborline:** 2026 is a good year to buy a quota share for a new admitted book, because capacity is abundant and cedants have leverage. But quota-share reinsurers will require the original form's war, infrastructure and systemic language to be **at least as broad as the treaty's**. Anything Harborline grants beyond the treaty (pending-attribution payments, carve-backs, AI-agent triggers) is paid net unless the treaty expressly follows it.

### 1.5 Systemic events and insured-loss estimates

| Event | Insured-loss estimate | Source | Label |
|---|---|---|---|
| CrowdStrike faulty update, July 2024 | CyberCube $400M–$1.5B. Guy Carpenter $300M–$1B ("kitty cat"). Parametrix: insurers pay $540M–$1.08B of $5.4B Fortune 500 direct losses; cyber insurance covers ~10–20% because of large retentions and limits | Insurance Journal (Jul 25 and Aug 2, 2024); Cybersecurity Dive; Fortune/Axios [S] | [S] |
| AWS us-east-1 outage ("Amazonk"), October 2025 | CyberCube preliminary $38M–$581M, most outcomes near the low end (Insurance Journal headline: "likely about $40M"); loss-ratio impact "low- to mid-single digits"; >2,000 large organizations and ~70,000 in total affected | CyberCube; Insurance Journal Oct 27, 2025; Reinsurance News [S] | [S] |
| Jaguar Land Rover, September 2025 | Cyber Monitoring Centre (CMC) **Category 3 systemic event**; ~£1.9bn (modelled £1.6–2.1bn); >5,000 organizations. Press reports say JLR had not completed its cyber placement, so there was little or no insured recovery | CMC statement Oct 22, 2025; Reinsurance News; Insurance Times [S] | [S]; the "£260m running total by Feb 2026, none insured" snippet is [S-low] |
| Other late-2025 outages | Lockton, "Recent outages shine spotlight on systemic cyber risks" (Dec 2025); Amwins, "AWS Outage: Market Impacts and Coverage Implications" | [S, titles] | |
| Modelling | CyberCube (event estimates above), Guy Carpenter, Gen Re ("The CrowdStrike Incident: A Wake-Up Call for Insurers?", Feb 2025). Munich Re: the "lion's share" of insurable cyber risk remains uninsured | [S] | |

**Key point:** the realized "cyber cats" have been **non-malicious outages** (system failure and dependent system failure) with modest insured losses. They were modest because of waiting periods, retentions and sublimits, not because exposure was small. The malicious systemic tail (NotPetya-type, state-backed) remains modelled rather than realized. That is exactly the split Harborline draws: war exclusion for the malicious tail, sublimits for outages. The design logic is sound; the leaks are in execution (Section 5).

---

## 2. Traditional carriers' SMB cyber products and wording trends

| Carrier | SMB product / channel | Relevant wording features found | Latest public form (catalog) | Label |
|---|---|---|---|---|
| **Chubb** | Cyber ERM small business; digital small commercial (appetite guide); BOP optional cyber | **Neglected Software Exploit (NSE):** "provid[es] full coverage for 45 days, and then for software that remains unpatched beyond 45 days, gradually re-weights risk sharing between the Insured and Insurer as time passes" (Chubb). One snippet shows an illustrative schedule: **0–45 days 0%, 46–90 days 0%, 91–180 days 5%, 181–365 days 10%, 366+ days 25%** coinsurance. **Widespread Event endorsement** (US form **PF-54815 (06/21)**, on the LMA clause list): separate limit, retention and coinsurance for Widespread Severe Vulnerability Exploit, Widespread Severe Zero-Day Exploit, Widespread Software Supply Chain Exploit and All Other Widespread Events. Chubb likens this to flood or quake handling in property | PF-48169 (02/19) small-business specimen; AU ERM V2.2 E13 Widespread Event [CAT] | NSE description [S] (Chubb pages). **The schedule is [S-low]:** the search summary's percentages may be one illustrative schedule, and the 46–90-day "0%" row sits oddly with "gradually re-weights" after day 45. Actual percentages are set per policy. Per my recollection [AK, verify], the NSE clock runs from CVE publication or patch availability, not insurer notice |
| **Beazley** | BBR / Full Spectrum Cyber; myBeazley small business | BBR 5.0 (70% hammer; bricking, reputation, proof-of-loss, cryptojacking; system failure in data recovery); **War and Cyber War Exclusion E15626** (physical-force war; major detrimental impact; essential services; bystander carve-back; no attribution mechanism per [CTX] C14). **Sept 2026: confirmed affirmative AI cover in cyber and tech E&O (Sept 17–18); launched "AI Voluntary Shutdown" and "AI Regulatory Defence & Penalties" endorsements (Sept 24)** | BBR 5.0 specimen F00653 (02/2025); BZCBR184_04/25 enhancements [CAT] | AI launches [S] (Insurance Journal Sept 17 and 25; The Insurer Sept 18 and 24, 2026). Round 1 already flagged the July 2025 vs 04/2025 date mismatch; the catalog shows the F00653 specimen as 02/2025 |
| **Travelers** (incl. Corvus) | CyberRisk; CyberFirst; BOP cyber endorsements; Corvus Smart Cyber | MFA attestation as an application artifact; *Travelers v. ICS* (2022) rescission over MFA | CYB-16001 CW coverage form (edition unverified); MFA attestation **CYB-14306 (2023-03)** [CAT] | Detailed 2026 MFA requirements not retrieved [gap] |
| **Hiscox** | CyberClear (US admitted) | Bundled SMB policy (breach, extortion, BI) | Admitted Cyber Coverage Part **CYBCL-CYB P0001A CW (10/2019)** [CAT] | Product description [S] |
| **The Hartford** | CyberChoice First Response (BOP/Spectrum add-on), CyberChoice Professional | Expanded CyberChoice First Response to small businesses nationwide except Alaska, Louisiana and Vermont | Product pages [CAT] | [S] (Insurance Business; date not captured) |
| **CNA** | EPS Plus | "CNA EPS Plus Policy Cyber War Exclusion" is on the LMA's **Cyber War Clauses list (October 2025)**. Evidence that a US admitted major has a named cyber-war clause catalogued against Lloyd's criteria | n/a | [S] (LMA list title and row) |
| **AXA XL** | CyberRiskConnect | "Generative AI cyber endorsement" cited as an example of affirmative AI | TRD 050 0619 (06/2019) [CAT] | [S-low] (via arXiv summary; date not verified) |
| **Tokio Marine HCC** | NetGuard Plus (NAS); SMB online flow up to $100M revenue | Base form includes dependent system failure, bricking, cyber crime, non-physical BI | NGP 1000 (04/2020) specimen; NGP-RNA (08/2025) renewal application; broad-appetite sheet (12/2025) [CAT] | Catalog notes only |
| **HSB (Munich Re)** | **Cyber Suite**, BOP-embedded and sold through mutuals and regionals (Erie, GNY, Heartland, Wilmington, Cal Mutual) | Low sublimit embedded model; Cyber Suite 2.0 (brochure 10/2025) | CSC 02-2025 coverage form (Heartland); Cyber Suite 2.0 brochure [CAT] | Not opened |
| **Crum & Forster** | Simple Cyber (+ MCM for professional services) | Simple, short-form SMB wording | **Simple Cyber Version 6.0 (2025-09-04)**; MCM v6 [CAT] | Not opened |
| **Munich Re** | HSB Total Cyber; **aiSure** (AI performance guarantee) | See Section 4 | HSB Total Cyber specimen 2021 [CAT] | [S] |

**Wording trends seen across traditional carriers:**
- systemic-event carve-outs with separate limits and coinsurance (Chubb Widespread Event);
- patch-hygiene risk sharing (Chubb NSE) and end-of-life software scrutiny (a HeroDevs blog title, "What's Excluded in 2026" [S-low]);
- modern cyber-war clauses catalogued by the LMA (Beazley E15626, CNA EPS Plus);
- system-failure cover in base forms but often sublimited, especially dependent system failure;
- in September 2026, a wave of affirmative AI cover (Beazley, CFC) following Coalition.
- BOP-embedded cyber (HSB Cyber Suite, Hartford, Travelers) remains the main SMB "penetration" channel.

---

## 3. Exclusion trends

### 3.1 War and state-backed cyber

| Item | Finding | Label |
|---|---|---|
| Lloyd's Market Bulletin **Y5381** (16 Aug 2022) | All standalone cyber-attack policies (risk codes CY, CZ) must carry a state-backed cyber-attack exclusion on placement or renewal from **31 March 2023** | DAC Beachcroft; Lloyd's PDF (title) [S] |
| LMA model clauses **LMA5564–LMA5567** | Four tiers. LMA5564 is strictest (excludes war and any cyber operation). LMA5567 carve-back: exclusion "does not apply to the direct or indirect effect of a cyber operation on a computer system used by the insured or its third party service providers that is not physically located in an impacted state" | DAC Beachcroft [S] |
| **A and B variants** (LMA5564A/B–5567A/B) | "Two sets of four model clauses." One blog says A versions carry explicit attribution language and B versions drop it; that characterization is **[S-low]**. Another snippet: LMA5567A "is careful to state that the insurer's burden of proof remains unchanged" while obliging parties to consider "objectively reasonable evidence" | DAC Beachcroft (two sets) [S]; Cyber Insurance Academy blog [S-low] |
| Attribution mechanics | Primary, but not exclusive, factor: attribution by the government of the state where the affected computer system is **physically located**. If that government fails to attribute or takes an unreasonable time, the insurer must prove attribution by other available evidence | Aggregated legal commentary [S] |
| "Major detrimental impact" | Operationalized through "impacted state": major detrimental impact on the **functioning of a state** through disruption of an **essential service**, or on its security or defence | [S] |
| Later Lloyd's bulletin **Y5433** ("State backed cyber attack wordings") | Acknowledges progress since Y5381 | Lloyd's PDF title [S]; date not captured |
| Lloyd's "types" | "Type 7 clauses must not be used from 1 January 2025 for reinsurance business, and the use of Type 4 clauses for policies incepted from 1 January 2025 will not be permitted for Lloyd's syndicates" | DAC Beachcroft [S]; the type taxonomy was not opened |
| Treaty clauses | LMA published model state-backed cyber war exclusion clauses **for cyber treaty reinsurance** | DAC Beachcroft title [S]; clause numbers not captured |
| LMA clause registry | LMA "Cyber War Clauses" lists (Sept 2025, Oct 2025) catalogue market clauses such as the Marsh Type 5 War Exclusion and the CNA EPS Plus Cyber War Exclusion, and host Beazley E15626 and Chubb PF-54815 | [S] |
| US adoption | Mixed. Modern clauses: Beazley, CNA, and the Chubb family (Widespread Event separately). Legacy "hostilities / warlike operations" wording is still in At-Bay AB-CYB-001.2 and Coalition's 2025–26 issued policy | [S] + [CTX] (checked in round 0) |
| Case law | *Merck v. ACE*, 475 N.J. Super. 420 (App. Div. 2023): legacy war wording did not reach NotPetya. [AK] The case settled in early 2024 before the NJ Supreme Court ruled | [CTX] + [AK] |

### 3.2 Infrastructure and utility

Market-typical cyber wordings exclude power, utility, telecom and core-internet failures that the insured does not control. They usually treat **cloud and IT service providers as dependent providers** rather than infrastructure. [S] (Reed Smith; Seedpod summaries). Contingent BI for non-attack outages usually needs a specific endorsement. [S]

Coalition's third-party mechanical-failure exclusion carves back provider security failures [CTX]. Harborline extends that carve-back to system failures.

### 3.3 Widespread-event and system-failure treatment

- Chubb Widespread Event: a separate limit, retention and coinsurance per systemic peril. [S]
- "A small number of insurers" have drafted widespread-event language that "may be used more widely." [S]
- Full limits are typical for security-failure dependent BI; **sublimits persist for system-failure dependent BI**. [S] A 2026 claim of "aggressive" dependent-BI sublimits is [S-low].
- Some carriers limit dependent businesses to those **under contract** with the insured. [S] Harborline adopts this, but "click-through" terms make it near-universal.

### 3.4 Neglected software and failure to maintain

- Chubb NSE is the reference design (3.x above).
- Failure-to-maintain and end-of-life-software exclusions persist in parts of the market. [S-low]
- Insurtech forms (Coalition, At-Bay) use scanning and contingency conditions [CTX].

### 3.5 BIPA and wrongful collection

Wrongful-collection and biometric exclusions are now standard, with pixel/CIPA cover sold separately. Harborline's structure matches (Coverage Q; exclusion 10 with a breach carve-back).

- [AK] Illinois amended BIPA in 2024 so damages accrue per person rather than per scan. This reduces, but does not remove, severity.
- SB 690 status is covered in round 1.

### 3.6 UDAP in cyber liability

- Round 1 flagged that Harborline's exclusion IV.2.8 carves back UDAP only for regulatory proceedings.
- [AK] Market wordings typically exclude antitrust and unfair competition. Where they exclude "unfair or deceptive trade practices", they commonly carve back claims arising from a privacy event or security failure, including private actions pleading state UDAP/UCL.
- Evidence level is analyst knowledge only; no 2025–26 form was opened in this pass. The direction of round 1's fix is consistent with market practice.

### 3.7 Contractual liability and betterment

- Contract-liability carve-backs for data-security duties, PCI assessments and liability-absent-contract are market-standard. Harborline matches [CTX].
- Betterment: Coalition pays 25% betterment [CTX C11]; BBR 5.0 has security-improvement features [CTX]. Harborline's Coverage G ($25K, incident-team-recommended, 90 days) is on the conservative side and priceable.

---

## 4. AI and insurance

### 4.1 ISO generative-AI GL exclusions

- Three forms, **01 26 edition**, effective **January 1, 2026**:
  - **CG 40 47**: Coverage A and B.
  - **CG 40 48**: Coverage B (personal and advertising injury) only.
  - **CG 35 08**: Products/Completed Operations coverage part, Section I bodily injury and property damage.
- **All are optional**; "they do not attach automatically." [S] (Gallagher; Independent Agent; Testudo glossary)
- Adoption: "several carriers adopted them within weeks" [S-low]. A claim that they are "now the default for 70% of the U.S. market" is **[S-low], unsupported: do not use.**
- **Harborline fix:** rationale "Regulatory status" and "Exclusions" rows say "on general liability forms since January 2026". Change to "available as optional ISO endorsements since January 2026; adoption varies by carrier".

### 4.2 Absolute AI exclusions

- **W.R. Berkley:** "Artificial Intelligence Exclusion (Absolute)", form **PC 51380 00** (edition shown in the snippet as **06-24**; the task brief says 2025, so verify). Used on D&O, E&O and fiduciary. It removes cover for "any actual or alleged use, deployment, or development of Artificial Intelligence." [S] (Hunton Andrews Kurth blog; National Law Review)
- Hamilton Select reportedly has comparable language. [S-low]
- A snippet claims "Berkshire Hathaway, Chubb, and Travelers secured state regulator approval to strip AI-related damages from corporate policies entirely". **[S-low], unverified; do not cite.**
- **Cyber lines:** "most carriers there are affirming coverage for AI-driven attacks." [S] A claim that "42% of companies already carry AI-related exclusions somewhere in their cyber policies" is [S-low]; source survey unidentified.
- **No major standalone cyber carrier with an absolute AI exclusion was found in this pass.** That is absence of evidence from 22 searches, not proof.

### 4.3 Affirmative AI in cyber

| Carrier | What | Date | Label |
|---|---|---|---|
| Coalition | Affirmative AI Endorsement for US surplus and Canada cyber. "AI security event" treated as a security failure; funds-transfer-fraud triggers extended to deepfake instructions | Endorsement March 2024; built into the Active Cyber Policy April 2025 | [S] (Coalition announcement + secondary) |
| Coalition | Deepfake Response Endorsement: forensic analysis, legal takedown, crisis communications | Announced Dec 9, 2025 | [S] |
| Beazley | Confirmed affirmative AI cover in cyber and tech E&O | Sept 17–18, 2026 | [S] |
| Beazley | "AI Voluntary Shutdown" (described as industry-first: suspending the insured's own malfunctioning AI) and "AI Regulatory Defence & Penalties" (the insured's own unintentional AI misuse) | Sept 24, 2026 | [S] |
| CFC | Affirmative AI cover within an FI suite upgrade | Sept 2026 (Insurance Journal, Sept 17) | [S] |
| AXA XL | Generative AI cyber endorsement | Date not verified | [S-low] |

**Deepfakes** are generally handled inside social-engineering / funds-transfer-fraud sublimits. Harborline's rationale cites $100K–$250K as common [CTX]. Coalition extends triggers to deepfakes. Harborline covers deepfakes through any channel, including phone, video and letter, within Coverage H at $250K. That is broader than Coalition's "electronic means" [CTX].

### 4.4 AI-specific insurance

| Provider | Product | Facts found | Label |
|---|---|---|---|
| Armilla + Chaucer (Lloyd's) | Affirmative AI liability | Launched April 30, 2025 (PR Newswire). "Vanguard AI" coordinated structure (Feb 10, 2026) pairs dedicated AI aggregate limits (reported as $25M+ per organization) with cyber limits (reported as $10M), using predefined allocation rules for mixed cyber/AI losses | Launch [S]; Vanguard limits [S-low] |
| Munich Re | aiSure | Performance guarantee: pays if a model misses a specified accuracy benchmark; operating since 2018 | [S] |
| AIUC | AIUC-1 standard + audits + insurance for AI-agent failures | Launched from stealth July 2025 with a $15M seed. Six pillars (data/privacy, security, safety, reliability, accountability, societal). Reported: ElevenLabs first AIUC-1-structured AI-agent policy (Feb 2026); Schellman first accredited auditor (Feb 2026) | [S] / [S-low] |
| Testudo | AI liability MGA | Conflicting dates: platform launch June 18, 2025; underwriting start Oct 31, 2025; "MGA launched January 2026"; capacity $9.25M per insured with Atrium and QBE (Feb 2026) | [S-low] |

### 4.5 AI agents and agentic AI in wordings

- No carrier wording that defines "AI agent" or agent-exceeding-authority was found; Harborline's own check found none either [CTX].
- Commentary describes agent actions as a "coverage vacuum" discovered at claim time, and says "a handful of carriers" offer add-ons covering agent actions, hallucination liability and prompt injection. [S-low]
- Academic work: arXiv 2605.18784 ("Insurability Frontier of AI Risk") and arXiv 2606.05449 ("Insurance of Agentic AI"). [S, titles]
- Beazley's AI Voluntary Shutdown is the closest carrier analogue: first-party cost of switching off the insured's own misbehaving AI.

### 4.6 Regulators

- The **NAIC Model Bulletin on the Use of AI Systems by Insurers** (adopted Dec 2023) governs **insurers' own** AI use (underwriting, claims), not coverage of AI.
  - Adoption: "24 states and DC" by the Spring 2026 National Meeting; another source says 25 by July 29, 2026.
  - A **12-state pilot of the NAIC AI Systems Evaluation Tool** ran in 2026, with an updated version targeted for the Fall 2026 National Meeting. [S]
- Relevance to Harborline: the pre-issue security scan, scan-based credits and any automated triage fall under insurer AI governance expectations in adopting states.
  - [AK] Colorado also runs its own insurer AI/external-data regime (SB21-169). Colorado SB 26-189 (effective Jan 1, 2027) governs insureds' AI use [CTX].
- No regulator guidance on AI **exclusions** in cyber was found.

---

## 5. Implications for Harborline, item by item

### Summary scorecard

| # | Design choice | Verdict | Priority fix |
|---|---|---|---|
| 5.1 | War / state-backed cyber exclusion | **Aligned in architecture; 4 drafting gaps; reinsurance recoverability risk** | Add "cyber operation in the course of war" limb; verify the "retaliatory operations" limb; cloud location tie-breaker; restore the "functioning of the state" qualifier; cap or align pending-attribution spend with the treaty |
| 5.2 | Infrastructure exclusion + dependent-provider carve-back | **Sound concept; carve-back too wide** | Define "infrastructure provider" and remove it from "dependent provider" (or from the carve-back) |
| 5.3 | $250K system-failure sublimit, optional dependent system failure | **Consistent with market and reinsurer appetite; two leaks** | Apply the $250K to Coverage F (and N) when caused by system failure; add a widespread-event aggregate |
| 5.4 | KEV 20% coinsurance after 45 days' notice | **Reasonable, more transparent than Chubb NSE; internal conflict** | Carve out the KEV rule from scan estoppel V.3.4; consider graduated steps; tie notice delivery to the "security contacts" duty |
| 5.5 | Affirmative AI + AI-agent trigger | **AI clause: market-standard. Agent trigger: market-leading but under-engineered** | Sublimit agent-only events; define "written instructions"; route agent-initiated payments; add widespread aggregation |
| 5.6 | Admitted paper | **Sensible for the SMB launch, with a phased plan** | State-by-state filing plan; quota share or fronting; consider surplus lines for the $25–50M band or tech classes |

### 5.1 War exclusion (Section IV, exclusion 15)

**What aligns** (with LMA5567 and Beazley E15626 as described in [S] and [CTX]):

| Element | Harborline | LMA5567 / E15626 / Y5381 | Match? |
|---|---|---|---|
| War | Physical force by one state against another; civil war, rebellion, insurrection, military takeover | Physical-force war definition (E15626 [CTX]; LMA [AK]) | Yes |
| State-backed cyber operation | By, at the direction of, or under the control of a state | Same concept | Yes |
| Threshold | "Major detrimental impact" on another state's security or defence, or on its essential services | Impacted state: major detrimental impact on **the functioning of a state** through disruption of an essential service, or on its security or defence [S] | **Partial.** Harborline drops "functioning of the state" (see gap 3) |
| Essential services | Financial, health, utility, emergency, food, energy, transportation | LMA illustrative list: financial institutions and market infrastructure, health, utilities [AK] | Broader list; acceptable if kept illustrative |
| Bystander carve-back | Your systems or a dependent provider's systems outside the impacted state | "Computer system used by the insured or its third party service providers that is not physically located in an impacted state" [S] | Yes |
| Attribution | Government of the state where affected systems are located; objectively reasonable evidence meanwhile | Same primary-but-not-exclusive rule; insurer proves attribution if the government is silent or slow [S] | Yes |
| Burden | Insurer | LMA5567A: insurer's burden "remains unchanged" [S-low] | Yes |
| Help pending attribution; no clawback | Coverage A, breach response and defense continue; no repayment | Not in LMA models | **Beyond market** (see gap 5) |
| Terrorism / state-linked crime carve-back | Expressly covered unless (a) or (b) applies | LMA models are silent; consistent in effect | Yes (Coalition-style clarity) |

**Y5381 criteria** (as summarized in [CTX] and [S]: exclude war; exclude state-backed attacks that significantly impair a state; clarify bystanders; set an attribution basis): **met on the face of the wording.** Y5381 binds Lloyd's syndicates, not a US admitted insurer. It matters because Lloyd's and London reinsurers, and LMA treaty clauses, carry the same expectations upstream.

**Gaps to fix before reinsurer review:**

1. **No explicit "cyber operation carried out as part of a war" limb.** Harborline's (a) excludes "war", and the causal link ("arising from") would have to do the work. After *Merck*, do not rely on causation language. Add "(a) war, or a cyber operation carried out as part of a war". [AK: the LMA models state this separately.]
2. **Retaliatory operations between major states.** [AK, verify against LMA text] LMA5565–5567 also exclude retaliatory cyber operations between specified states (a named list of major powers). If the quota-share treaty imports LMA5567, Harborline's form is narrower than the treaty, and those losses are net. Either add the limb or get the treaty to follow Harborline's form.
3. **Impact threshold drift.** Harborline triggers on impact "on its essential services". LMA requires major detrimental impact on the **functioning of the state** *due to* disruption of an essential service. Harborline's text is arguably **broader** (insurer-favorable), which undercuts the rationale's "insured-friendly modern wording" claim. Restore "on the functioning of that state due to disruption of the availability, integrity or delivery of an essential service", or on its security or defence.
4. **"Where your affected computer systems are located" for cloud accounts.** Harborline's *computer systems* include cloud accounts the insured administers, whose data centers may sit abroad. LMA uses "physically located". Add a tie-breaker, e.g. "for cloud accounts, the location of the data center hosting the affected data or, if unknown, the named insured's principal office". Otherwise the bystander carve-back and the attribution rule are both indeterminate for a typical Microsoft 365 SMB.
5. **Pending-attribution payments with no clawback** (IV.15.5). This is good for insureds and rare in the market. If the treaty excludes the same event, those payments are **not reinsured**, and a NotPetya-type event hits every insured at once. Options:
   - cap pre-attribution spend (e.g., Coverage A plus a fixed amount per insured);
   - negotiate express treaty follow-the-settlements for this clause;
   - keep the no-clawback promise but make it subject to an event aggregate.
6. **Minor:** "another state" should be defined as a state other than the state carrying out the operation, as the LMA "impacted state" concept does.

**Bottom line:** Harborline's war exclusion is closer to LMA5567 than At-Bay's or Coalition's legacy wording [CTX], and it adds an attribution clause that Beazley's E15626 lacks. It is reinsurable in principle. Fix gaps 1–4 and price gap 5 before calling it "reinsurer-reviewed".

### 5.2 Infrastructure exclusion (IV.2.12) with dependent-provider carve-back

- **Concept:** excluding power, utilities, telecoms, satellites and core internet (DNS) that the insured does not operate is market-standard, as is covering contracted IT and cloud providers under dependent BI. [S] Coalition carves back provider security failures [CTX]. Harborline's extension of the carve-back to system failures (Coverage P) is logical because P is optional and priced.
- **Problem:** "Dependent provider" means **any** business providing services under a written or electronic agreement, including accepted online terms. An electric utility, an ISP or telecom carrier, a DNS or CDN provider with click-through terms: **all are dependent providers.** Exclusion 12's carve-back ("does not apply to a security failure ... at a dependent provider under Coverage E") therefore reinstates cover for:
  - a ransomware attack on the regional power utility that blacks out the insured;
  - a compromise of a national telecom or ISP;
  - an attack on a managed DNS provider.
  These are the correlated, portfolio-wide events the exclusion exists to remove. (For P, the *system failure* definition already carves out power, utility, telecom and internet failure, so the leak is mainly Coverage E.)
- **Fix:** define "infrastructure provider" (electricity, gas, water, telecommunications carriers, internet backbone and exchange points, DNS root/TLD operators, satellite operators). Exclude infrastructure providers from "dependent provider", or limit the carve-back to "IT, cloud, software and business-process providers". Optionally keep a small, priced sublimit for security failures at infrastructure providers. Cloud hyperscalers should stay dependent providers; that is the market norm and what SMBs expect.

### 5.3 $250K system-failure sublimit in core; dependent system failure optional

- **Consistent with the market:** full limits for security-failure BI; sublimits persist for system failure and especially dependent system failure. [S] Chubb separates widespread perils. [S] Realized systemic losses were system-failure driven (CrowdStrike, AWS). [S] Reinsurers price this as the main modelled accumulation (CyberCube estimates) [S]. For a new admitted carrier, core system failure at $250K with an 8-hour wait, plus dependent system failure as a priced option, is a **defensible middle**: narrower than Coalition (full limit [CTX]) and broader than startup forms (Vouch optional [CTX]).
- **Leak 1: Coverage F restoration at full limit for system failure.** Coverage F pays restoration costs "because of a security failure or system failure" at $1,000,000. A CrowdStrike-type faulty vendor update is the insured's own **system failure**. The BI part is capped at $250K, but endpoint re-imaging, data recreation and IT labor fall under F at full limit across every affected insured. Apply the $250K system-failure sublimit to D **and F** combined (or a separate F sublimit).
- **Leak 2: the AI-agent trigger.** An AI agent that "exceeds its authority" is a **security failure**. An agent malfunction therefore reaches full-limit BI ($1M in D), F and liability, bypassing the $250K system-failure cap that would apply to the same outage caused by a "programming error" (see 5.5).
- **No widespread-event aggregate.** Harborline's only widespread-event language is in *business income loss* (no profit from competitors' harm). Consider:
  - an annual widespread-event sublimit on D (system failure), E and F;
  - or, at minimum, a portfolio event limit in the treaty;
  - and documenting a CrowdStrike/AWS-scenario PML in the filing memorandum.
- **Waiting period.** The rationale cut system-failure waiting from 12 to 8 hours to match Coalition and Vouch [CTX]. For a correlated vendor-update event, most SMB recoveries run 1–3 days [AK], so 8 hours lets most of those claims through. Keep 8 hours only if the aggregate above is added; otherwise 12 hours is a cheap accumulation dampener.

### 5.4 KEV 20% coinsurance after 45 days' written notice vs Chubb NSE

| Feature | Chubb NSE | Harborline III.1.7 |
|---|---|---|
| Scope | Exploits of known, published software vulnerabilities (CVE-based [AK]) | Only CISA KEV-listed vulnerabilities that **Harborline notified in writing** |
| Clock | 45 days of full coverage, then graduated risk sharing [S]. Start point: publication or patch availability [AK, verify] | 45 days **after Harborline's notice** |
| Shape | Graduated; illustrative schedule 0% → 5% → 10% → 25% [S-low] | Flat 20% cliff at day 46, never escalates |
| Insured awareness | Insured must track patches itself | Only what the insurer told them |
| Burden | Insurer shows the exploit was of a neglected vulnerability | Insurer must show the incident was "caused" by that KEV item |

**Assessment:** Harborline's rule is **more insured-friendly and more transparent**. It suits a no-IT-staff SMB and is easier to defend in admitted form review, since it is disclosed and conditioned on notice. It keeps the policy's "security lapses don't void coverage" promise honest. Issues:

1. **Conflict with scan estoppel (V.3.4):** "We will not deny or **reduce** coverage ... because of any condition that our pre-issue security scan showed, or should have shown." A KEV found in the pre-issue scan and then notified is arguably shielded, because coinsurance *reduces* coverage. Add "except as provided in Section III, part 1.7, after written notice".
2. **Cliff vs slope:** 20% at day 46 is harsher early than Chubb's illustrative schedule and softer for year-long neglect. Consider 10% (46–90 days after notice), 20% (91–180) and 30% (180+). Or apply a higher step for KEV entries flagged as used in ransomware campaigns [AK: KEV carries such a flag]. That matches the At-Bay 2026 finding that 87% of ransomware entry was via remote access [CTX].
3. **Notice mechanics:** make delivery to the "security contacts" (already a claim-free condition, V.6.1) the notice address, with deemed receipt. Otherwise every coinsurance dispute becomes a notice dispute.
4. **Consistency:** "This is the only way patching affects your coverage" (III.1.7) sits awkwardly with the claim-free reduction's "fix critical issues within 30 days" (V.6.1), which also ties a benefit to patching. Say "the only way patching affects what we pay on a claim".
5. **Operational commitment:** the rule only works if Harborline runs continuous external scanning and KEV matching for every insured. That is a real cost line and should be in the rationale's "what I'd do with more time" or pricing notes.

### 5.5 Affirmative AI clause + "AI agent exceeding authority" in *security failure*

- **The affirmative clause is market-standard**, not market-leading, as of September 2026: Coalition (2024/25), Beazley (Sept 17–24, 2026), CFC (Sept 2026), AXA XL. [S] Update the rationale's market benchmark, which lists only Coalition. The clause is still valuable as a contrast with GL (ISO optional exclusions) and D&O/E&O (Berkley absolute). AI-created media content under Coverage L is a real gap-filler.
- **The AI-agent trigger is ahead of the market.** No competitor definition was found; Beazley's AI Voluntary Shutdown is the nearest analogue. Risks:
  1. **Sublimit arbitrage:** outages caused by an agent "exceeding authority" are *security failures* (full $1M BI after 8 hours). The same outage from a "programming error" is a *system failure* ($250K). Expect claims framing. Fix: when an AI-agent event involves no unauthorized third party, apply the system-failure sublimit (or a dedicated AI-agent sublimit) to D and F.
  2. **"Written instructions" = prompts?** If a system prompt or policy document counts as "written instructions", coverage turns on prompt text. Broad technical permissions plus narrow prose instructions would maximize cover (moral hazard). Define authority by **configured permissions** only, or require instructions in a governance document existing before the incident.
  3. **Money movement:** an agent that pays a fake invoice after prompt injection is not an *employee* acting on a *fraudulent instruction*. Whether it is *computer fraud* ("someone's unauthorized entry into, or use of") is arguable. Say expressly whether agent-executed payments fall under Coverage H (and its sublimit) or not. Otherwise the $250K fraud sublimit can be sidestepped through B, D or I framing.
  4. **Accumulation:** a compromised or faulty agent platform update, or a prompt-injection campaign, is a widespread event. Include it in the widespread-event aggregate recommended in 5.3.
  5. **Uncovered AI regulatory exposure:** Coverage J needs a security failure or privacy event. Beazley now sells AI regulatory defence and penalties. With Colorado SB 26-189 effective Jan 1, 2027 [CTX], an optional "AI regulatory" coverage would be a natural Part 2 addition later. For now, state the gap plainly in the rationale.
  6. **Underwriting:** add two application questions: agent inventory, and least-privilege/logging for agents. Condition the agent trigger on logging existing, so "exceeded its authority" can be proven.
- **Verdict:** keep both, but label the agent trigger as a deliberate, sublimited innovation rather than a full-limit promise. As drafted, it is the largest unpriced exposure in the form after the utility carve-back.

### 5.6 Admitted paper for an SMB cyber launch in 2026

**For:**
- SMB buyers ($1M–$50M revenue) mostly buy through retail agents or direct, and the admitted market dominates SMB and BOP-embedded cover.
- Admitted business ran a **better loss ratio (50.2 vs ~56 for surplus lines)** in 2025. [S]
- Guaranty-fund protection, no surplus-lines tax or diligent-search friction, and consistency with Harborline's regulatory-style promises (service standards, cancellation limits, honest-mistake rule).
- TRIA offer mechanics and state amendatory endorsements are already contemplated [CTX].

**Against / conditions:**
- **Speed and flexibility:** surplus lines hold about two-thirds of premium because freedom of rate and form lets carriers move with the cycle. [S] In a market with rates at −2% to −3% (Marsh/CIAB) and softening slowing (WTW), an admitted filer cannot re-price quickly either way. State filing timelines vary [AK].
- **Form review of novel clauses:** KEV coinsurance tied to insurer notice, scan estoppel, attribution rules, arbitration at the insured's option, the 70% hammer and the AI-agent definition will each draw questions. Budget for state variations beyond the Colorado amendatory form.
- **Capacity and rating:** a new admitted carrier needs a financial-strength rating agents will accept [AK] or a fronting arrangement, plus a quota share. 2026 reinsurance terms (−10–20% in July; ample capacity) make this feasible now. [S]
- **Competitive set:** admitted SMB is crowded with low-price BOP-embedded products (HSB Cyber Suite, Hartford, Travelers) [CAT]/[S]. Standalone SMB leaders (Coalition, At-Bay) run surplus-lines forms, with some admitted variants [CTX].

**Recommendation:**
- Launch admitted for the core $1M–$25M band in a first wave of states (Colorado plus file-and-use states).
- Keep an E&S or fronted option for $25M–$50M, tech-heavy or high-hazard classes.
- Say in the memo that admitted status is a deliberate trade: slower pricing moves in exchange for trust and consumer protection. The QR steel-man already says this; the new AM Best admitted vs surplus-lines loss-ratio data strengthens it.

---

## 6. Corrections and additions for the Harborline package (new in this round)

1. Rationale "What we changed", Premium row, and Claim Ledger C17: Marsh Q2 2026 **does** report a US cyber figure (−2%, same as Q1). Replace "a cyber-specific figure was not verified" with the attributed figure. Label it search-snippet unless the press release is reopened.
2. Rationale "Regulatory status" and "Exclusions" rows: ISO CG 40 47 / CG 40 48 / CG 35 08 are **optional** endorsements (01 26 edition), not "on general liability forms".
3. Rationale market benchmark and "AI clause" row: add Beazley (affirmative AI cyber, Sept 2026, plus AI Voluntary Shutdown and AI Regulatory Defence & Penalties endorsements) and CFC. "No competitor wording found" should be limited to the AI-agent *definition*.
4. Rationale Summary item 4 and trade-offs ("stayed cautious on systemic risks"): not fully true until the Coverage F system-failure leak, the utility/telecom carve-back and the AI-agent full-limit trigger are fixed.
5. War wording: fix gaps 1–4 in 5.1. Add the pending-attribution treaty point to "Still needs counsel or actuarial review".
6. Scan estoppel V.3.4 vs KEV rule III.1.7: add the carve-out.
7. Optional: cite the AM Best 2025 admitted vs surplus-lines loss ratios in the admitted-paper steel-man, and the Chubb Widespread Event endorsement (PF-54815 (06/21)) as the market reference for a widespread-event aggregate.

## 7. Open gaps (not resolved in this pass)

- Exact Chubb NSE percentages and clock start. The snippet schedule is low-confidence; confirm from a Chubb PF form.
- Whether LMA5565–5567 contain the "retaliatory operations between specified states" limb, and the A/B variant difference (blog-level only).
- NAIC 2026 report (2025 data); Aon and Gallagher 2026 cyber rate figures; Q3 2026 indices.
- 2025 premium growth: Fitch +7% vs "nearly 11%" vs a "flat premium" headline.
- Hannover Re 2026 cyber cat bond vs "no 144A cyber cat bonds in 2026".
- Current Travelers MFA requirements; current Hiscox and CNA SMB forms (catalog forms are 2019–2020 editions).
- Berkley PC 51380 edition date (06-24 per snippet vs 2025 per brief).

## 8. Sources (URLs as returned by search; all search-snippet level unless marked)

**Market and economics**
- NAIC 2025 Report on the Cybersecurity Insurance Market: https://content.naic.org/sites/default/files/inline-files/2025_Cybersecurity_Insurance%20Report.pdf (fetch blocked)
- Fitch 2025 growth (The Insurer, Jun 3, 2026): https://www.theinsurer.com/cyber-risk/news/fitch-us-cyber-insurance-market-swung-to-7-written-premium-growth-in-2025-2026-06-03/
- AM Best 2025 results (Claims Journal, Jun 30, 2026): https://www.claimsjournal.com/news/national/2026/06/30/338540.htm (fetch blocked)
- AM Best rankings (Beazley No. 2): https://news.ambest.com/newscontent.aspx?refnum=275075&altsrc=175
- AM Best 2024 segment report: https://www.businesswire.com/news/home/20250623167339/en/Bests-Market-Segment-Report-2024-Pricing-Cuts-in-U.S.-Cyber-Generated-First-Ever-Reduction-in-Direct-Premiums-Written
- Marsh Q2 2026 GIMI: https://www.marsh.com/en/corp/about/news/global-commercial-insurance-falls-6-percent-q2-2026.html ; https://www.insurancejournal.com/news/national/2026/07/23/878716.htm
- CIAB Q2 2026: https://www.ciab.com/resources/q2-2026-pc-market-survey ; https://www.insurancejournal.com/news/national/2026/08/20/882240.htm
- WTW IMR 2026 Cyber: https://www.wtwco.com/en-us/insights/2025/10/insurance-marketplace-realities-2026-cyber-risk ; Spring update: https://www.wtwco.com/en-us/insights/2026/05/insurance-marketplace-realities-2026-spring-update
- Amwins 2026 Outlook: https://www.amwins.com/resources-and-insights/market-insights/article/state-of-the-market-2026-outlook ; AWS outage note: https://www.amwins.com/resources-and-insights/market-insights/article/aws-outage--market-impacts-and-coverage-implications
- Munich Re Risks and Trends 2026: https://www.munichre.com/en/insights/cyber/cyber-insurance-risks-and-trends-2026.html (fetch blocked); Global Cyber Risk and Insurance Survey 2026: https://www.munichre.com/en/insights/cyber/global-cyber-risk-and-insurance-survey-2026.html
- S&P Outlook 2026: https://www.spglobal.com/ratings/en/regulatory/article/cyber-insurance-market-outlook-2026-resilient-earnings-tougher-competition-pockets-of-growth-s101658506
- Travelers Risk Index (Sept 23, 2026): https://www.claimsjournal.com/news/national/2026/09/23/340321.htm
- SMB take-up aggregator ([S-low]): https://app.stationx.net/articles/small-business-cybersecurity-statistics

**Reinsurance and cat bonds**
- The Insurer, July renewals: https://www.theinsurer.com/cyber-risk/news/cyber-reinsurance-rates-fall-by-as-much-as-20-at-july-renewals-aggregate-2026-06-17/
- Guy Carpenter July 1, 2026 cyber: https://www.guycarp.com/insights/2026/07/July-1-renewals-cyber.html
- Lockton July 2026 cyber: https://insights.lockton.com/lockton-market-update/july-2026/cyber
- Artemis Q2 2026 report: https://www.artemis.bm/wp-content/uploads/2026/07/catastrophe-bond-ils-market-report-q2-2026.pdf ; cyber cat bond topic: https://www.artemis.bm/news/topic/cyber-cat-bond/ ; S&P on cyber ILS: https://www.artemis.bm/news/cyber-ils-primed-for-future-growth-if-traditional-capacity-constraints-emerge-sp/
- The Insurer, H1 2026 cat bonds: https://www.theinsurer.com/ti/reinsurancemonth/cat-bond-issuance-for-h1-2026-hits-record-173-billion-am-best-2026-08-27/

**Systemic events**
- CrowdStrike: https://www.insurancejournal.com/news/national/2024/07/25/785484.htm ; https://www.insurancejournal.com/news/national/2024/08/02/786766.htm ; https://www.cybersecuritydive.com/news/crowdstrike-cost-fortune-500-losses-cyber-insurance/722396/
- AWS Oct 2025: https://www.cybcube.com/news/insurance-loss-estimate-for-aws-amazonk-outage ; https://www.insurancejournal.com/news/national/2025/10/27/845197.htm
- JLR/CMC: https://cybermonitoringcentre.com/2025/10/22/cyber-monitoring-centre-statement-on-the-jaguar-land-rovercyber-incident-october-2025/ ; https://www.insurancetimes.co.uk/news/fca-warns-of-massive-underinsurance-after-jaguar-land-rover-cyber-shock/1456713.article
- Gen Re: https://www.genre.com/us/knowledge/publications/2025/february/the-crowdstrike-incident-a-wake-up-call-for-insurers-en
- Lockton Dec 2025: https://insights.lockton.com/lockton-market-update/december-2025/recent-outages-shine-spotlight-on-systemic-cyber-risks

**Wordings and exclusions**
- Chubb systemic events paper: https://www.chubb.com/content/dam/chubb-sites/chubb-com/us-en/business-insurance/products/cyber/documents/chubb_insuring_systemic_cyber_events_final.pdf ; HK article: https://www.chubb.com/hk-en/articles/business/a-better-way-to-define-and-insure-systemic-cyber-events.html
- Chubb Widespread Event Endorsement PF-54815 (06/21) (US): https://lmalloyds.com/wp-content/uploads/2025/09/PF-54815-06-21-Widespread-Event-Endorsement-US.pdf (fetch blocked)
- Chubb Cyber ERM factsheet (APAC): https://www.chubb.com/content/dam/chubb-sites/chubb/apac/document/products/Cyber%20ERM%20Factsheet%20Version2-2.pdf
- Westchester systemic-risk FAQ (Oct 2021): https://www.westchester.com/content/dam/chubb-sites/westchester/us-en/documents/Westchester_CyberSystemicRiskProductUpdate.pdf (fetch blocked)
- LMA cyber war clauses page: https://lmalloyds.com/specialist-areas/underwriting/wordings/cyber-war-clauses/ ; lists: https://lmalloyds.com/wp-content/uploads/2025/10/Cyber-War-Clauses-October-2025.pdf ; https://lmalloyds.com/wp-content/uploads/2025/09/Cyber-War-Clauses.pdf
- Lloyd's Y5381: https://assets.lloyds.com/media/35926dc8-c885-497b-aed8-6d2f87c1415d/Y5381%20Market%20Bulletin%20-%20Cyber-attack%20exclusions.pdf ; Y5433: https://assets.lloyds.com/media/6715b794-2ffd-40f7-b1c5-bcc02ca2e29b/Y5433%20-%20State%20backed%20cyber%20attack%20wordings.pdf
- DAC Beachcroft overview: https://www.dacbeachcroft.com/en/What-we-think/War-exclusions-in-cyber-policies-an-overview ; treaty clauses: https://www.dacbeachcroft.com/en/What-we-think/LMA-publishes-model-state-backed-cyber-war-exclusion-clauses-for-cyber-treaty-reinsurance
- LMA5567A/B blog ([S-low]): https://www.cyberinsuranceacademy.com/blog/guides/lma5567a-b-lloyds-cyber-war-exclusions-2026/
- Exclusions commentary: https://www.reedsmith.com/articles/cyber-insurance-claims/navigating-common-exclusions-in-cyber-policies/ ; https://www.insurancethoughtleadership.com/cyber/cyber-insurance-exclusions-expect-2026 ([S-low])

**AI**
- ISO forms (Gallagher): https://www.ajg.com/news-and-insights/iso-introduces-generative-ai-exclusion-in-commercial-general-liability-policies/ ; Independent Agent: https://www.independentagent.com/vu_resource/verisk-to-roll-out-new-general-liability-exclusions-for-generative-ai-exposures/
- Berkley absolute AI exclusion: https://www.hunton.com/hunton-insurance-recovery-blog/the-continued-proliferation-of-ai-exclusions ; https://natlawreview.com/article/continued-proliferation-ai-exclusions
- Coalition Affirmative AI: https://www.coalitioninc.com/announcements/coalition-adds-new-affirmative-ai-endorsement-to-cyber-policies ; https://www.coalitioninc.com/ai-coverage
- Beazley AI (Sept 2026): https://www.theinsurer.com/cyber-risk/news/beazley-confirms-ai-related-cover-in-cyber-tech-eo-policies-2026-09-18/ ; https://www.theinsurer.com/cyber-risk/news/beazley-launches-cyber-cover-for-ai-shutdowns-and-regulatory-risks-2026-09-24/ ; https://www.insurancejournal.com/news/national/2026/09/25/886788.htm ; CFC: https://www.insurancejournal.com/news/national/2026/09/17/885463.htm
- Armilla/Chaucer: https://www.prnewswire.com/news-releases/armilla-launches-affirmative-ai-liability-insurance-with-lloyds-underwriter-chaucer-302442586.html
- AIUC: https://aiuc.com/updates/introducing-aiuc-1
- Agentic AI research: https://arxiv.org/html/2606.05449v1 ; https://arxiv.org/pdf/2605.18784
- NAIC AI bulletin adoption map: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf ; aggregator ([S-low]): https://actuary.info/insights/ai-regulation-insurance-naic-2026

**Carriers**
- The Hartford expansion: https://www.insurancebusinessmag.com/us/news/cyber/the-hartford-expands-cyber-coverage-for-small-businesses-550562.aspx
- Local catalog rows [CAT]: `/home/user/insurance/catalog/cyber_policies.csv` (Chubb PF-48169; Beazley F00653; Travelers CYB-14306; Hiscox CYBCL-CYB P0001A CW; AXA XL TRD 050 0619; TMHCC NGP 1000 / NGP-RNA 08/2025; HSB CSC 02-2025; C&F Simple Cyber v6.0)
