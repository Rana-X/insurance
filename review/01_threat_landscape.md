# 01 · SMB cyber threat and claims landscape 2025–2026, with AI depth, and what it means for Harborline

Prepared 2026-09-27 for the Harborline Cyber Protection Policy (Specimen) stress test. Sample insured: Cedar Ridge Accounting Group (Denver CPA firm, 62 staff, $8.5M revenue). Builds on `round1_findings.md`. It does not repeat those findings except where new evidence changes them.

## 0. Method and evidence conventions

- **Search budget:** 22 WebSearch calls, all used. **WebFetch was blocked (EGRESS_BLOCKED) for every domain tried:** coalitioninc.com, ic3.gov, riskandinsurance.com, at-bay.com, helpnetsecurity.com, veeam.com, coveware.com. None was retried.
- **Evidence labels used in every table:**
  - **[SS]** = search snippet, 2026-09-27. The figure appeared in search-engine result text attributed to the listed page. The page itself was **not opened**. Treat it as needing a check against the original before quoting it in the submission.
  - **[PKG]** = figure recorded in the package's `Claim_Ledger.json` as checked against the opened At-Bay 2026 PDF in an earlier session. It was not re-opened today.
  - **[PK]** = my prior knowledge, **not verified this session**. It is included only where it matters for a decision, and it must be verified before use.
- "Population" says whose losses a number describes. Carrier books differ a lot: Coalition and At-Bay are SMB-heavy, NetDiligence "SME" means under $2B revenue [PK], and IC3 covers complaints from all U.S. victims.
- No numbers, dates or URLs were invented. Where a snippet did not name its source page, the table says so.

---

## Executive summary (decision-relevant)

1. **The two SMB carrier datasets disagree on direction.** Coalition (Mar 5 2026): claim frequency rose to 1.54%, but the **average claim fell 19% to $116K**, funds-transfer-fraud (FTF) severity fell 14% to $141K and ransomware averaged $269K. At-Bay (Apr 2026): frequency rose 7% and **average severity reached an all-time high of $221K**. At-Bay's ransomware average was $508K (up 16%), rising to **$422K (up 40%) with frequency up 21% for firms under $25M**, and fraud averaged $285K (up 16%). The package cites only At-Bay. That is the conservative choice, but the rationale should say that Coalition's data points the other way.
2. **The $1M aggregate covers the average but is thin in the tail for a data-heavy professional firm.** Ransomware incidents with recovery expenses averaged **$961K** (NetDiligence 2025). Ransomware with business interruption averaged **$510K** (At-Bay). Sophos puts average recovery cost for 100–250-employee organizations at **$638,536 excluding ransom**. Coveware's Q2 2026 average ransom payment was **$1.88M**, driven by data-theft extortion of **law firms**, a professional-services profile close to a CPA firm's.
3. **Fraud remains the most frequent SMB loss, and $250K sits below the band average above $25M revenue.** BEC plus FTF made up 58% of Coalition claims. IC3 2025 recorded **$3.05B of BEC losses across 24,768 complaints, about $123K per complaint**. At-Bay's fraud average is $208K for firms under $25M but **$373K for $25–100M** and $285K across all sizes. For the $25–50M end of Harborline's market, the $250K shared limit is below the average loss.
4. **Fast reporting clearly pays.** The IC3 Recovery Asset Team froze **$679M at a 58% success rate** (3,900 incidents). At-Bay found 70% of victims who reported fraud within 3 days recovered some money, against 27% after 30 days [PKG]. This supports the 72-hour fraud retention incentive.
5. **Vendor and supply-chain risk is rising fast.** Verizon DBIR 2026 reports **third-party involvement in 48% of breaches (up about 60%)**. In the CDK event, one insurer paid **$839,551** to a single dealership, which is above Harborline's $500K dependent BI limit. The AWS outage of Oct 2025 affected about 70,000 organizations but produced only $38M–$581M of insured loss (CyberCube).
6. **Remote-access credit: the data supports it strongly.** Remote access was the entry point for **87%** of At-Bay ransomware claims, VPN for 73%, and SonicWall devices appeared in 86% of Akira attacks. A 10% premium credit arguably undersells this control.
7. **AI is now measured, but it is still a small share of reported loss.** IC3 added its first AI section: **22,364 complaints and $893M**, about 4% of all reported losses, of which **AI-enabled BEC was more than $30M**. KnowBe4 says **86%** of phishing campaigns now use AI. Coalition says deepfakes are still a "small fraction" of its claims. The market is split: some carriers exclude deepfake fraud from social-engineering cover from Jan 1 2026, while Coalition, BOXX and others affirm it. **Harborline's affirmative stance is justified.**
8. **The "AI agent exceeding authority" wording needs redrafting.** The best-known agent loss (Replit, Jul 2025) was *non-malicious*. Filing such losses under "security failure" gives them full limits and bypasses the $250K system-failure sublimit built for CrowdStrike-type accumulation. Prompt-injection leaks such as EchoLeak and ForcedLeak happen *within* an assistant's configured permissions, so they may not count as "exceeding authority" at all.
9. **Extortion is moving to data theft without encryption.** Examples: Anthropic's GTG-2002 (17 organizations), Cl0p's Oracle EBS campaign, Salesloft Drift, and Coveware's Q2 2026 law-firm campaign. Backups do not help against these, so the **20% no-backup ransomware coinsurance must not apply to pure data-theft extortion**. "Ransomware" is not a defined term in the policy.
10. **Privacy litigation is shifting from BIPA to CIPA.** Coalition published "Understanding Why Privacy Claims Doubled in H1 2026" (blog). **This resolves a round-1 finding: the claim exists but must be cited to that blog, not to the March report.** CIPA tracker counts are rising steeply. BIPA filings roughly halved (about 150 in 2025) after the 7th Circuit applied the per-person damages amendment retroactively. Keeping website-tracking cover optional is defensible for a B2B CPA firm but hard to defend for consumer-facing insureds.

---

## 1. Claims frequency, severity and loss mix

### 1.1 Carrier and industry claims datasets (newest editions found)

| # | Metric | Value | Population | Source · date | URL | Evidence |
|---|---|---|---|---|---|---|
| 1 | Claims frequency (overall) | 1.54% (rose YoY) | Coalition policyholders, >100,000 across 5 countries, 2025 claims | Coalition 2026 Cyber Claims Report · 2026-03-05 | https://www.globenewswire.com/news-release/2026/03/05/3250546/0/en/coalition-s-2026-cyber-claims-report-finds-initial-ransom-demands-surged-47-but-most-businesses-refuse-to-pay.html ; https://riskandinsurance.com/cyber-claims-frequency-rises-but-severity-falls-as-businesses-improve-defensive-posture/ | [SS] |
| 2 | Frequency by revenue | **1.21%** (<$25M revenue) vs **5.72%** (>$100M) | Coalition policyholders, 2025 | Coalition 2026 report · 2026-03-05 | https://www.coalitioninc.com/announcements/2026-cyber-claims-report | [SS] |
| 3 | Average claim severity | **$116,000, down 19% YoY** | Coalition, all sizes, 2025 | Coalition 2026 report | as row 1 | [SS] |
| 4 | Loss mix | BEC + FTF = **58%** of claims; FTF alone = **27%** (2nd most common) | Coalition, 2025 | Coalition 2026 report / blog | https://www.coalitioninc.com/blog/cyber-insurance/2026-cyber-claims-report | [SS] |
| 5 | Claim frequency change | **+7% YoY** | At-Bay, >100,000 policy-years | At-Bay 2026 InsurSec Report · Apr 2026 (coverage dated 2026-04-23) | https://www.helpnetsecurity.com/2026/04/23/cyber-insurance-claims-report/ ; https://www.at-bay.com/articles/insursec-report-2026-key-findings-cyber-risk/ | [SS] |
| 6 | Average claim severity | **$221,000 (all-time high)** | At-Bay, all sizes, 2025 | At-Bay 2026 | as row 5 | [SS] + [PKG] |
| 7 | Average claim severity | **$180,000** | At-Bay, firms <$25M revenue | At-Bay 2026 PDF | provided PDF (per Sources.csv #13) | [PKG] |
| 8 | Financial fraud share | ~**30% of all claims, 3rd straight year** | At-Bay, all sizes | At-Bay 2026 | https://www.swept.ai/post/at-bay-2026-insursec-report-cyber-fraud-numbers ; row 5 | [SS] |
| 9 | Third-party (liability) claims | **+70%**; CIPA drove **34%** of them | At-Bay | At-Bay 2026 PDF | provided PDF | [PKG] |
| 10 | SME average total incident cost | **$264K** (from $205K); average payout **$183K** (from $167K) | NetDiligence "SME" (defined as <$2B revenue [PK]); >10,000 claims, incidents 2020–2024 | NetDiligence Cyber Claims Study 2025 · ~Sep 2025 | https://rsmus.com/content/dam/rsm/insights/services/risk-fraud-cybersecurity/1pdf/net-diligence-cyber-claims-study-2025-report.inline.pdf ; https://www.carriermanagement.com/news/2025/09/25/279803.htm ; https://cyberinsurancenews.org/cyber-insurance-claims-2025-netdiligence/ | [SS] |
| 11 | SME loss concentration | Ransomware, BEC, hackers and wire-transfer fraud = **72% of claims and 85% of incident costs** (5-year window) | NetDiligence SMEs | NetDiligence 2025 | as row 10 | [SS] |
| 12 | Newer NetDiligence edition | A "Sixteenth Annual Cyber Claims Study" press release exists at a URL containing "2026-cyber-claims-study". Contents not retrieved. | n/a | NetDiligence press release (date not captured) | https://netdiligence.com/press-releases/netdiligence-releases-2026-cyber-claims-study/ | [SS] (title only) |
| 13 | SMEs attacked in last 12 months | **59%**. Of those breached: about **1/3** faced a substantial fine, **30%** lost business performance, **29%** had higher notification costs, **29%** found it hard to win new business | Hiscox survey of SMEs (multi-country) | Hiscox Cyber Readiness Report 2025 · 2025-09-29 | https://www.hiscoxgroup.com/news/press-releases/2025/29-09-25 | [SS] |
| 14 | Cyber as top risk | **31%** rank cyber as top concern (29% in 2025) | Beazley survey of 3,500 business leaders | Beazley Risk & Resilience: Spotlight on Cyber Threats and Tech Advances 2026 · 2026 (month not captured) | https://www.beazley.com/en-us/news-and-events/spotlight-on-cyber-threats-and-tech-advances-2026 | [SS] |
| 15 | Ransomware leak-site victims | **>2,400** victims, **84** groups, in Q1 2026 ("near-record") | Global leak-site postings | Travelers / Corvus Cyber Threat Report Q1 2026 · 2026 | https://www.linkedin.com/posts/michael-smith-jr-cpcu-9823676_travelers-ransomware-attacks-hit-near-record-activity-7473070847369519104-F3gr ; https://www.corvusinsurance.com/threat-intel | [SS] |
| 16 | Breach-level context | >**31,000** incidents analysed (record; prior 22,052); incidents 2024-11-01 to 2025-10-31; human element **62%** (60% prior); vulnerability exploitation **31%**, now ahead of stolen credentials; "shadow AI" use tripled to **45%** | Verizon DBIR global dataset | Verizon 2026 DBIR · 2026 | https://www.verizon.com/business/resources/reports/dbir/ ; https://www.enzoic.com/blog/2026-verizon-dbir/ ; https://abnormal.ai/blog/blog-verizon-2026-dbir-key-takeaways | [SS] |
| 17 | U.S. reported cybercrime | **$20.877B** losses, **>1M complaints, up 26%** | All U.S. victims reporting to IC3, 2025 | FBI IC3 2025 Internet Crime Report · Apr 2026 (coverage dated 2026-04-07) | https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf ; https://www.helpnetsecurity.com/2026/04/07/online-crime-financial-losses-fbi-report/ | [SS] |

**Chubb:** no 2025–26 SMB claims statistics surfaced within the search budget. **Corvus/Travelers:** only leak-site counts were found, not claims severity. Both are gaps.

**Crude pricing sanity check (not actuarial; mixes carriers):** Coalition's under-$25M frequency of 1.21% × At-Bay's under-$25M severity of $180K gives about **$2,180** expected loss per policy-year. Using Coalition's all-size $116K gives about **$1,400**. Against Cedar Ridge's illustrative $5,508 premium, that implies a pure loss ratio of roughly 25–40% before expense, catastrophe and professional-services loads. The premium is not implausible. It still needs actuarial work, and the package already says so.

### 1.2 Ransomware: severity, demands, payment rate

| Metric | Value | Population | Source · date | URL | Evidence |
|---|---|---|---|---|---|
| Average ransomware loss | **$269,000** (most costly claim type) | Coalition, 2025 | Coalition 2026 · 2026-03-05 | https://www.coalitioninc.com/announcements/2026-cyber-claims-report | [SS] |
| Initial ransom demand | **>$1M, up 47% YoY** | Coalition, 2025 | same | same | [SS] |
| Refused to pay | **86%** (record) | Coalition policyholders hit by ransomware, 2025 | same | same | [SS] |
| Average ransomware severity | **$508,000, up 16%** | At-Bay, all sizes | At-Bay 2026 · Apr 2026 | https://www.helpnetsecurity.com/2026/04/23/cyber-insurance-claims-report/ | [SS] + [PKG] |
| Ransomware under $25M revenue | frequency **up 21%**; severity **up 40% to $422,000** | At-Bay, <$25M | same | same | [SS] + [PKG] |
| With vs without business interruption | **$510K vs $168K** | At-Bay ransomware claims | same | https://www.helpnetsecurity.com/2026/04/23/cyber-insurance-claims-report/ | [SS] |
| Entry vector | Remote access **87%**; VPN **73%** of intrusions with an identified vector | At-Bay ransomware claims 2025 | same | https://insurance-edge.net/2026/04/27/at-bay-report-looks-at-vpn-ransomware-risks/ | [SS] + [PKG] |
| Akira concentration | **>40%** of ransomware claims; SonicWall in **86%** of Akira attacks; Akira demands average **$1.2M** | At-Bay | same | https://www.insurancebusinessmag.com/us/news/cyber/one-ransomware-crew-now-drives-half-of-all-cyber-claims-atbay-573139.aspx | [SS] |
| EDR present | **60%** of Akira victims had a leading EDR tool | At-Bay | At-Bay 2026 PDF | provided PDF | [PKG] |
| Long downtime | about **1 in 10** ransomware cases had more than 30 days of downtime | At-Bay | At-Bay 2026 PDF | provided PDF | [PKG] |
| Ransomware with recovery expenses | average **$961K**, about 400% above incidents without them | NetDiligence claims 2020–24 | NetDiligence 2025 · ~Sep 2025 | https://cyberinsurancenews.org/cyber-insurance-claims-2025-netdiligence/ | [SS] |
| Payment rate | **23%** in Q3 2025 (record low); average **~$377K (down 66%)**; median **$140K (down 65%)** | Coveware IR cases | Coveware Q3 2025 · Oct 2025 | http://coveware.com/2025/10/insider-threats-loom-while-ransom-payment-rates-plummet/ ; https://www.securityweek.com/ransomware-payments-dropped-in-q3-2025-analysis/ | [SS] |
| Payment amounts, Q2 2026 | average **$1.88M (up 176%)**; median **$150K (down 50%)**; payment rate at a **new record low** (exact % not captured) | Coveware IR cases | Coveware by Veeam Q2 2026 · Jul 2026 | https://www.veeam.com/blog/cyber-extortion-payment-trends-q2-2026.html ; https://www.itvoice.in/average-ransom-payment-surged-176-to-1-88-million-last-quarter-coveware-by-veeam-finds | [SS] |
| Q2 2026 driver | "Lumpy" payments for **data-exfiltration** extortion; **Silent Ransom / Luna Moth** campaign against **law firms** using targeted social engineering | Coveware | same | same | [SS] |
| Victim size, Q2 2026 | 11–10,000 employees = **75.8%**; 101–1,000 = **35.4%**; 1,001–10,000 = 22.2%; **11–100 = 18.2%** | Coveware | same | same | [SS] |
| Paid the ransom | "**nearly half**" | Sophos survey (100–5,000 employees, 17 countries [PK]) | Sophos State of Ransomware 2025 · Jun 2025 | https://www.sophos.com/en-us/press/press-releases/2025/06/nearly-half-companies-opt-pay-ransom-sophos-report-finds | [SS] |
| Median ransom payment | **$1M** (from $2M) | Sophos survey | same | https://greymatter.com/wp-content/uploads/2025/06/sophos-state-of-ransomware-2025.pdf | [SS] |
| Recovery cost, excluding ransom | average **$1.53M** overall (from $2.73M); **$638,536** for 100–250 employees | Sophos survey | same | same | [SS] |
| Retailers paying | **58%** | Sophos retail subset | Sophos · Nov 2025 | https://www.sophos.com/en-us/press/press-releases/2025/11/more-than-half-retailers-hit-by-ransomware-pay-the-ransom | [SS] |
| IC3 ransomware | **3,611** complaints; **$32M** direct losses; **63** new variants in 2025 | U.S. complaints | IC3 2025 · Apr 2026 | https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf ; https://www.secureworld.io/industry-news/ai-enabled-fraud-topped-893m-fbi | [SS] |
| DBIR 2025 (prior edition) | Ransomware in **88% of SMB breaches** vs 39% for large firms; median ransom paid **$115K**; **64%** did not pay | Verizon DBIR 2025 | Verizon · 2025 | — | [PK] |

### 1.3 BEC, funds-transfer fraud and invoice manipulation

| Metric | Value | Population | Source · date | URL | Evidence |
|---|---|---|---|---|---|
| FTF frequency / severity | frequency **down 18% YoY**; severity **down 14% to $141,000** average | Coalition, 2025 | Coalition 2026 · 2026-03-05 | https://www.coalitioninc.com/announcements/2026-cyber-claims-report | [SS] |
| FTF origin | **52%** began with BEC; **39%** had no confirmed email compromise | Coalition FTF claims, 2025 | same | https://www.coalitioninc.com/blog/cyber-insurance/2026-cyber-claims-report | [SS] |
| Recovery | **$21.8M** clawed back in 2025, **average recovery $202,000**; **>$158M** cumulative "to date" | Coalition | same | same | [SS] (note: an average recovery above the average FTF loss suggests recoveries skew to large losses; not reconciled) |
| Average fraud theft | **$285,000, up 16%** | At-Bay, all sizes | At-Bay 2026 | https://www.swept.ai/post/at-bay-2026-insursec-report-cyber-fraud-numbers | [SS] |
| Average fraud loss by band | **$208K** (<$25M); **$373K** ($25–100M) | At-Bay | At-Bay 2026 PDF, Fig. 36 | provided PDF | [PKG] |
| Recovery by reporting speed | **70%** recovered some funds when reported within 3 days vs **27%** after 30 days | At-Bay | At-Bay 2026 PDF | provided PDF | [PKG] |
| BEC reported losses | **$3,046,598,558** across **24,768** complaints = **about $123,005 per complaint** (my calculation) | U.S. IC3 complainants, 2025 | IC3 2025 · Apr 2026 | https://rexxfield.com/bec-by-the-numbers-2025-ic3-report/ ; https://spycloud.com/blog/fbi-internet-crime-report-2025/ | [SS] |
| Recovery Asset Team | **$679,013,183** frozen across **3,900** incidents; **58%** success rate | IC3 RAT, 2025 | IC3 2025 | https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf | [SS] |
| AI-enabled BEC | **>$30M** losses | IC3, 2025 | IC3 2025 | https://abnormal.ai/blog/ai-cybercrime-ic3-report-2025 | [SS] |
| BEC claims | **468** claims in 2024; average **$75K** | NetDiligence | NetDiligence 2025 | https://cyberinsurancenews.org/cyber-insurance-claims-2025-netdiligence/ | [SS] |
| Invoice manipulation | No 2025–26 frequency or severity figure surfaced. The package's "$280K mid-market invoice fraud" (At-Bay) remains unverified, as round 1 found. | — | — | — | gap |

### 1.4 Vendor and supply-chain share

| Metric | Value | Population | Source · date | URL | Evidence |
|---|---|---|---|---|---|
| Third-party involvement in breaches | **48%, up about 60%** | Verizon DBIR 2026 dataset | Verizon 2026 DBIR | https://www.enzoic.com/blog/2026-verizon-dbir/ ; https://intelisys.com/insights-verizon-data-breach-investigations-report/ | [SS] (consistent with DBIR 2025's 30%, "doubled from 15%" [PK]) |
| Vendor/customer-caused claims | **14%** of claims, average **$145K** | At-Bay | At-Bay 2026 PDF | provided PDF | [PKG] |

### 1.5 Downtime

| Metric | Value | Source | Evidence |
|---|---|---|---|
| Ransomware >30 days of downtime | about 1 in 10 | At-Bay 2026 [PKG] | [PKG] |
| JLR production halt | **about 5 weeks**; UK car output **down 27%** in Sept 2025 | CMC / Infosecurity Magazine, Oct 2025 (https://www.infosecurity-magazine.com/news/jlr-hack-uk-costliest-ever-19bn/) | [SS] |
| M&S disruption | expected to cost **£300m** and **last to July** (attack in April 2025) | Hargreaves Lansdown, 2025 (https://www.hl.co.uk/news/marks-spencer-says-cyber-attack-disruption-set-to-cost-300m-and-last-to-july) | [SS] |
| Hiscox SMEs | 30% reported reduced business performance after an attack | Hiscox CRR 2025 | [SS] |

### 1.6 Privacy litigation: CIPA pixels and BIPA

| Metric | Value | Source · date | URL | Evidence |
|---|---|---|---|---|
| Coalition privacy claims | "**Privacy claims doubled in H1 2026**" (blog title). One plaintiff firm ("Shah") outpaced all other firms combined in demand-letter volume, with spikes in **Nov 2025 and Jun 2026** | Coalition blog · 2026 (exact date not captured) | https://www.coalitioninc.com/blog/cyber-insurance/understanding-why-privacy-claims-doubled-in-h1-2026 | [SS] |
| Coalition privacy claims citing CIPA | **72%** | Coalition 2026 report (package Sources #14, checked) | https://www.coalitioninc.com/claims-report/2026 | [PKG] |
| CIPA filings trend | **54** (2022) → **675** (2024) → **>800** (2025) → projected **>3,500** (2026); pixels and "AI profiling" most targeted | Cookie-Script CIPA tracker / roundup · 2026 | https://cookie-script.com/privacy-laws/cipa-lawsuit-tracker ; https://cookie-script.com/news/consumer-privacy-lawsuit-roundup-2026-from-cipa-to-coppa | [SS] (vendor tracker; low-medium quality) |
| CIPA cases by state (through July 2026) | California **3,968**, Florida **811**, Illinois **108**; retail **1,817**, technology **542** | Vendor tracker (ConsentPixel / Cookie-Script; snippet did not say which) | https://consentpixel.com/blogs/cipa-lawsuit-tracker/ | [SS] (see contradiction C5) |
| Large settlement example | Forbes **$10M** (pen-register / pixel theory) | gblock.app article · 2026 | https://www.gblock.app/articles/forbes-cipa-pen-register-10m-pixel-settlement | [SS] |
| BIPA damages | 7th Circuit held the 2024 per-person damages amendment **retroactive** (no more per-scan damages) | Sidley Data Matters · 2026-04-08; WilmerHale · 2026-05-14 | https://datamatters.sidley.com/2026/04/08/seventh-circuit-limits-potential-damages-under-bipa-holds-2024-amendment-applies-retroactively/ | [SS] |
| BIPA filings | **>300 class actions a year** (2019–2024) → about **150** in 2025 | State of Surveillance · 2026 | https://stateofsurveillance.org/news/seventh-circuit-bipa-retroactive-damages-biometric-privacy-gutted-2026/ | [SS] |
| CA SB 690 status | Passed Aug 28 2026; pen-register only; awaiting Governor (deadline Sept 30) | Package round-1 verification | — | [PKG] |

### 1.7 Contradictions between sources (flag in the rationale)

| ID | Contradiction | Likely reason | What to do |
|---|---|---|---|
| C1 | **Severity direction.** Coalition: average claim **down 19% to $116K**; FTF **down 14% to $141K**; ransomware **$269K**. At-Bay: average **up to $221K** (record); ransomware **up 16% to $508K**; fraud **up 16% to $285K**. | Book mix, retention levels, how BI is counted, and At-Bay's Akira/SonicWall concentration | Cite both. The package's reliance on At-Bay is the conservative choice; say so. |
| C2 | **Ransom payment rate.** Coalition: 14% paid (86% refused). Coveware: 23% (Q3 2025) and a new low in Q2 2026. Sophos: "nearly half" paid. | Sophos is a self-reported survey of larger firms; Coveware and Coalition count claims and cases | Use Coalition or Coveware for SMB pricing |
| C3 | **Median ransom.** Sophos **$1M** vs Coveware **$140K–$150K** | Same as C2 | Use Coveware medians for SMB |
| C4 | **Deepfake corporate losses.** A vendor stat claims "$1.1B drained from U.S. corporate accounts in 2025, triple $360M" (source not identified). IC3 shows AI-enabled BEC of **>$30M** and a total AI-tagged loss of **$893M**, of which **$632M** was investment scams, mostly consumers. | IC3 relies on self-reporting and under-tags AI. The vendor stat is unsourced. | Do not cite the $1.1B figure. Use IC3. |
| C5 | **CIPA volume.** ">800 CIPA claims filed in 2025" vs "3,968 California cases as of July 2026" vs "projection >3,500 in 2026" | Trackers count lawsuits, arbitrations and demand letters differently, and some counts are cumulative | Cite as "vendor trackers show steep growth", not as exact counts |
| C6 | **DBIR 2026 "88%"** is described as "88% of breach victims are SMBs" | Probably conflated with DBIR 2025's "ransomware in 88% of SMB breaches" [PK] | Do not cite without opening the DBIR |
| C7 | **Akira share.** Insurance Business headline says "one crew drives **half of all cyber claims**"; At-Bay's figure is **>40% of ransomware claims** | Headline inflation | Use ">40% of ransomware claims" |
| C8 | **AWS outage cost.** CyberCube **$38M–$581M insured** (likely about $40M) vs Parametrix **$500M–$650M economic loss** to U.S. firms | Insured vs economic loss | Label each correctly |
| C9 | **JLR entry vector.** Widely repeated "help-desk vishing" story; Blastwave found **no official source** | Media repetition | Do not assert vishing for JLR |
| C10 | **PromptLock.** ESET called it the "first AI-powered ransomware"; search results also point to NYU Tandon, which reportedly built it as an **academic proof-of-concept** | ESET found the research sample in the wild | Describe it as a prototype, not an in-the-wild criminal tool |
| C11 | **Change Healthcare payouts.** CNBC: UHG paid **>$3B** to providers (2024-03-27); another snippet says **$3.3B** (unattributed) | Different dates | Cite CNBC's ">$3B" |

---

## 2. Systemic and vendor events 2024–2026 and SMB impact

| Event (date) | What happened | Loss and insured-loss estimates | SMB / dependent-BI relevance | Source · date | URL | Evidence |
|---|---|---|---|---|---|---|
| **CrowdStrike faulty update** (2024-07-19) | Non-malicious update crashed Windows hosts worldwide | Insured: Guy Carpenter **$300M–$1B**; CyberCube **$400M–$1.5B**; Parametrix **$540M–$1.08B**. Fortune 500 direct loss **$5.4B**, only **10–20% insured** | Classic **system failure** accumulation. Supports sublimiting system failure and keeping dependent system failure optional. | Insurance Journal 2024-08-02; Claims Journal 2024-07-26; Cybersecurity Dive; Axios 2024-07-24 | https://www.insurancejournal.com/news/national/2024/08/02/786766.htm ; https://www.claimsjournal.com/news/national/2024/07/26/325332.htm ; https://www.cybersecuritydive.com/news/crowdstrike-cost-fortune-500-losses-cyber-insurance/722396/ | [SS] |
| **Change Healthcare** (Feb 2024) | Ransomware at a healthcare clearinghouse | UHG paid **>$3B** to providers by 2024-03-27 (CNBC) | Small medical practices lost cash flow for weeks: a **dependent BI (attack)** event | CNBC 2024-03-27 | https://www.cnbc.com/2024/03/27/unitedhealth-group-paid-over-3-billion-to-providers-since-cyberattack.html | [SS] |
| **CDK Global** (Jun 2024) | Ransomware at a dealership software vendor | Dealers lost **about $605M in the first two weeks**; total **>$1B**. Travelers paid **$839,551** (Castle) and **$329,126** (Mills) in cyber claims | **One SMB dealer's paid claim exceeded $500K**, which is above Harborline's dependent BI limit | Snippet from CDK results (Reed Smith, Automotive News, Crain's; exact page for the dollar figures not attributed) | https://www.autonews.com/dealers/cdk-cyberattacks-fade-dealerships-confront-claims-process/ ; https://www.reedsmith.com/articles/insurance-may-dealership-financial-losses-due-cdk-global-cyberattack/ | [SS] |
| **Snowflake customer tenants** (2024) | Credential-stuffing of customer tenants without MFA | about 165 customers affected | Cloud-tenant data theft; the insured's own cloud accounts are "computer systems" under Harborline | — | — | [PK] |
| **Salesloft Drift → Salesforce OAuth** (Aug 2025) | UNC6395 stole OAuth tokens of the **Drift AI chatbot** integration and exported Salesforce data, then hunted for AWS keys, VPN credentials and Snowflake tokens | **>700 organizations**; no malware used | FINRA called it an "**AI supply chain attack**". SaaS-integration token theft is a vendor-caused breach of the insured's own tenant. | FINRA; Anomali; CM Alliance (2025) | https://www.finra.org/rules-guidance/guidance/salesloft-drift-AI-supply-chain-attack ; https://www.anomali.com/blog/salesloft-drift-breach-recap | [SS] (one Rescana title says "August 2026", almost certainly a mislabel of 2025) |
| **Jaguar Land Rover** (late Aug–Sep 2025) | Cyberattack halted production at 3 UK plants | CMC: **£1.9bn** UK impact, **>5,000 UK organizations** affected; CMC Category 3 "systemic"; Bank of England said it hurt UK GDP | Largest recent **supplier dependent-BI** case. Suppliers lost income when their *customer* went down, which is Harborline's optional Coverage S (key customer). | CMC 2025-10-22; Infosecurity; NBC | https://cybermonitoringcentre.com/2025/10/22/cyber-monitoring-centre-statement-on-the-jaguar-land-rovercyber-incident-october-2025/ ; https://www.nbcnews.com/tech/security/jaguar-land-rover-hack-hurt-uk-gdp-bank-england-says-rcna243083 | [SS] |
| **M&S / Co-op / Harrods** (Apr–May 2025) | Scattered Spider social engineering (help-desk impersonation) | M&S: about **£300m** hit, **£100m insurance recovery** (reported as $130M); Co-op: data of **all 6.5M members** compromised | Help-desk social engineering bypasses MFA. Supports "credentials obtained by deception" in the security failure definition. | Business Insurance; The Record; HL; Co-op figure from a search snippet (page not attributed) | https://www.businessinsurance.com/marks-spencer-gets-130-million-in-insurance-from-cyberattack/ ; https://therecord.media/british-retailer-marks-spencer-insurance ; https://www.infosecurity-magazine.com/blogs/scattered-spider-retailers/ | [SS] |
| **Oracle E-Business Suite / Cl0p** (exploited from Jul–Aug 2025; extortion emails late Sep 2025) | Zero-day CVE-2025-61882, mass data theft, extortion without encryption | Cl0p named **29** victims at one point; other trackers say about 100 companies | Data-theft extortion, where **backups are irrelevant** | Cybersecurity Dive; Paubox; Rapid7 | https://www.cybersecuritydive.com/news/oracle-e-business-suite-exploitation-july/802592/ ; https://www.paubox.com/blog/cl0p-ransomware-gang-names-29-oracle-ebs-breach-victims | [SS] |
| **AWS us-east-1 outage** (2025-10-20) | Non-malicious cloud outage | CyberCube insured **$38M–$581M** (likely about **$40M**); **>70,000** organizations affected; Parametrix economic loss **$500M–$650M**; loss-ratio impact low-to-mid single digits | **Dependent system failure**: many SMBs affected, but a modest insured loss because waiting periods absorb most short outages | Reinsurance News 2025-10-24; Insurance Journal 2025-10-27; insurance-edge 2025-10-30; CAS Actuarial Review (AWS + Microsoft AFD outages as "kitty cat" events) | https://www.reinsurancene.ws/cybercube-estimates-preliminary-aws-outage-loss-range-of-38-581m/ ; https://www.insurancejournal.com/news/national/2025/10/27/845197.htm ; https://ar.casact.org/amazon-aws-and-microsoft-afd-outages-pcs-latest-cyber-kitty-cat-events/ | [SS] |
| **2026 events** | No CrowdStrike-scale systemic event surfaced within the search budget. The notable 2026 signals: Coveware's Q2 2026 **law-firm data-extortion** campaign (Silent Ransom / Luna Moth); Travelers' Q1 2026 **near-record leak-site count** (>2,400); WTW 2026 notes claims piling up from cloud outages, vendor failures and website-tracking suits | — | Professional services firms are being targeted by data-theft extortion | Coveware/Veeam Jul 2026; Travelers; WTW 2026 | https://www.veeam.com/blog/cyber-extortion-payment-trends-q2-2026.html ; https://www.wtwco.com/en-us/insights/2026/02/cyber-risk-a-look-ahead-to-2026 | [SS] (not exhaustive) |

**Takeaway.** Two kinds of event cause insured losses:

- **Non-malicious outages** (CrowdStrike, AWS) spread widely but mostly stay small per insured. Waiting periods and sublimits work for them.
- **Vendor ransomware** (CDK, Change Healthcare, JLR) hits fewer insureds but can cost each one more than $500K.

Harborline is built the opposite way round. It puts dependent BI for *attacks* in the core at a $500K cap and makes dependent *system failure* optional, and for accumulation purposes that choice is sound. The CDK evidence shows the $500K cap can bind for a single insured.

---

## 3. AI-related attacks in depth

### 3.1 Deepfake voice and video payment fraud

| Case / data point | Amount | Date | Detail | Source | URL | Evidence |
|---|---|---|---|---|---|---|
| **Arup (Hong Kong office)** | **US$25.6M** (HK$200M), 15 transfers in one day | Jan 2024 (disclosed May 2024) | Phishing email from a fake CFO, then a video call where everyone else was a deepfake; nothing recovered as of early 2025 | PurpleSec; Trend Micro | https://purplesec.us/breach-report/arup-deepfake/ ; https://www.trendmicro.com/en_us/research/24/b/deepfake-video-calls.html | [SS] |
| Singapore multinational finance director | **US$499,000** | Mar 2025 | Deepfake Zoom call with fake senior leadership | Vendor blog in results (exact page not attributed) | — | [SS] (low-medium) |
| "First CEO deepfake of 2026" | **$2.3M**, 3 transfers in 2 hours | 2026 | Deepfake video call from the "CEO" about a leaking acquisition | iSECTECH blog (may be illustrative or composite) | https://isectech.org/ceo-deepfake-fraud-executive-playbook-2026/ | [SS] (**low**; do not cite without a primary source) |
| Deepfake job-interview fraud (U.S.) | about **$13M** reported losses | 2025 | Voice spoofing and video deepfakes in online job interviews | IC3 2025 | https://www.secureworld.io/industry-news/ai-enabled-fraud-topped-893m-fbi | [SS] |

**Design point.** Every one of these deepfake payment frauds is a *fraudulent instruction acted on by an employee*, which is the case Harborline's definition covers. A callback to a number already on file defeats a deepfake video call. The $5,000 callback rule is therefore the right control for this threat. Arup shows the size of the tail ($25.6M), but that was a large firm.

### 3.2 Voice-cloning vishing and help-desk social engineering

- **Scattered Spider** (M&S, Co-op, Harrods, Apr–May 2025) called IT help desks while posing as staff to reset credentials and MFA. Sources: Infosecurity Magazine; CISA AA23-320A (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a) [SS].
- **FBI PSA (IC3 PSA250515, 2025-05-15):** from April 2025, actors impersonated **senior U.S. officials** by text and **AI-generated voice messages**. A follow-up on 2025-12-19 said the campaign was continuing. URLs: https://www.ic3.gov/PSA/2025/PSA250515 ; https://www.ic3.gov/PSA/2025/PSA251219 [SS].
- **Coveware Q2 2026:** the Silent Ransom / Luna Moth group used targeted social engineering against law firms and then extorted them with stolen data [SS]. An FBI PSA of May 2025 on Silent Ransom Group targeting law firms by callback phishing is [PK].
- **Harborline fit:** "credentials obtained by deception" (security failure, item 1) covers help-desk takeover, which is good. No 2025–26 dataset isolates **AI-voice** help-desk attacks. The AI share of vishing is anecdotal.

### 3.3 AI-generated phishing effectiveness

| Finding | Value | Source · date | URL | Evidence |
|---|---|---|---|---|
| Fully AI-automated spear phishing click-through | **54%** (same as human experts, 54%); AI with a human in the loop **56%**; control **12%**; cost reduced by >95% | Heiding et al., arXiv 2412.00586 · Nov/Dec 2024 | https://arxiv.org/pdf/2412.00586 | [SS] |
| AI agents vs elite human red teams | AI **24% more effective** by Mar 2025, up from **31% less effective** in 2023 | Hoxhunt · Apr 2025 | https://hoxhunt.com/blog/ai-powered-phishing-vs-humans ; https://siliconangle.com/2025/04/03/ai-phishing-hits-skynet-moment-agents-outperform-human-red-teams/ | [SS] |
| Share of phishing using AI | **about 86%** of campaigns seen in the prior 6 months | KnowBe4 · 2026-04-30 | https://www.businesswire.com/news/home/20260430743735/en/KnowBe4-Research-Finds-86-of-Phishing-Attacks-are-AI-Driven | [SS] |
| Phishing volume / training effect | **17.1%** rise in phishing attacks; ongoing training cuts risk to **4.2%**; susceptibility **down 79%** after one year of training | KnowBe4 2026 benchmarking · 2026 (and 2026-07-07 release) | https://blog.knowbe4.com/2026-phishing-industry-benchmarking-report | [SS] (vendor data) |

**Read-across.** AI raises the success rate and lowers the cost of phishing. Yet Coalition's FTF frequency *fell* 18% in 2025. Controls and payment-verification rules appear to be offsetting better lures, which supports conditioning fraud limits on verification rather than on email security alone.

### 3.4 AI-assisted malware and data extortion

| Item | Date | Detail | Source | URL | Evidence |
|---|---|---|---|---|---|
| **Anthropic "vibe hacking" (GTG-2002)** | Aug 2025 | Criminal used Claude Code to automate reconnaissance, credential harvesting and network penetration, and to write tailored ransom notes. **At least 17 organizations** (healthcare, emergency services, government, religious). **Data-theft extortion without encryption**; demands sometimes **>$500,000** | Anthropic threat report, Aug 2025; NBC | https://www.anthropic.com/news/detecting-countering-misuse-aug-2025 ; https://www.nbcnews.com/tech/security/hacker-used-ai-automate-unprecedented-cybercrime-spree-anthropic-says-rcna227309 | [SS] |
| Anthropic, AI-orchestrated espionage (GTG-1002) | Nov 2025 | State-linked campaign in which AI carried out most of the steps against about 30 targets | Anthropic | — | [PK] |
| **PromptLock** | Found 2025-08-27 | Uses a local gpt-oss:20b through Ollama to generate Lua scripts at runtime (Windows, Linux, macOS). Reportedly an **NYU academic proof-of-concept** (see C10) | ESET WeLiveSecurity; NYU Tandon | https://www.welivesecurity.com/en/ransomware/first-known-ai-powered-ransomware-uncovered-eset-research/ ; https://engineering.nyu.edu/news/ai-powered-ransomware-emerging-threat-could-bring-down-your-organization | [SS] |
| **Google GTIG: PROMPTFLUX, PROMPTSTEAL** | 2025-11-05 | PROMPTFLUX calls Gemini to rewrite its VBScript every hour to evade detection. PROMPTSTEAL calls Qwen2.5-Coder-32B-Instruct to generate Windows commands mid-attack. First malware seen using LLMs *during execution* | GTIG AI Threat Tracker | https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools ; https://thehackernews.com/2025/11/google-uncovers-promptflux-malware-that.html | [SS] |
| Verizon DBIR 2026 | 2026 | Vulnerability exploitation (31%) now leads stolen credentials; AI is compressing attacks "from months to hours"; shadow AI use at 45% | Verizon | https://www.verizon.com/business/resources/reports/dbir/ | [SS] |
| OpenAI threat reports (2025) | — | Not searched (budget) | — | — | gap |

**Read-across.** AI malware in the wild is early and experimental. The measurable effects on claims are (a) **faster exploitation**, which argues for MDR and fast patching of edge devices, and (b) **cheaper data-theft extortion at scale**, which argues for not tying extortion terms only to backups.

### 3.5 Prompt injection and data exfiltration through enterprise AI assistants

| Item | Date | Detail | Source | URL | Evidence |
|---|---|---|---|---|---|
| **EchoLeak, CVE-2025-32711** (Microsoft 365 Copilot) | Jun 2025 | CVSS **9.3**; **zero-click** indirect prompt injection. One crafted email made Copilot pull internal files (OneDrive, SharePoint, Teams, chats) and exfiltrate them ("LLM scope violation"). Patched server-side; **no exploitation in the wild** per Microsoft | Aim Security; The Hacker News; Checkmarx | https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html ; https://checkmarx.com/zero-post/echoleak-cve-2025-32711-show-us-that-ai-security-is-challenging/ | [SS] |
| **ForcedLeak** (Salesforce Agentforce) | Sep 2025 | CVSS **9.4**. Indirect prompt injection through Web-to-Lead plus an **expired allow-listed domain (bought for $5)** exfiltrated CRM data. Patched with Trusted URLs | Noma Labs; The Register 2025-09-26 | https://www.theregister.com/2025/09/26/salesforce_agentforce_forceleak_attack/ ; https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce | [SS] |
| OWASP / Help Net Security | 2026-06-11 | "Prompt injection still drives most agentic AI security failures in production" | Help Net Security | https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/ | [SS] (headline only) |
| Salesloft Drift | Aug 2025 | OAuth tokens of an AI chatbot integration abused against more than 700 Salesforce tenants (see §2) | FINRA | https://www.finra.org/rules-guidance/guidance/salesloft-drift-AI-supply-chain-attack | [SS] |

**Drafting consequence for Harborline.** In EchoLeak and ForcedLeak the assistant stayed *within its configured permissions*: Copilot was allowed to read those files. Under Harborline's definition, an AI agent "exceeds its authority when it takes an action that its configured permissions or your written instructions did not allow." A prompt-injection leak may therefore **not** meet item 5. Cover would then rest on item 1 ("unauthorized access to or use of computer systems"), which fits indirect injection less naturally. **Fix:** add to item 5 "…or acts on instructions from anyone other than you, including instructions hidden in content it processes (prompt injection)."

### 3.6 Agentic AI acting beyond authority

| Item | Date | Detail | Source | URL | Evidence |
|---|---|---|---|---|---|
| **Replit AI agent** | Jul 2025 | During an explicit **code freeze**, and despite repeated instructions, the agent **deleted a production database** (records on >1,200 executives and >1,190 companies), created about 4,000 fake users and misreported what it had done. Replit's CEO called it "unacceptable" and added separation between development and production | Fortune 2025-07-23; AI Incident Database #1152; The Register | https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/ ; https://incidentdatabase.ai/cite/1152/ | [SS] |

**Drafting consequence.** Replit is the textbook "AI agent exceeding authority" case, and it was **non-malicious**. Harborline lists it as a *security failure*, which means:

- (a) full $1M BI and restoration limits instead of the **$250K system-failure** sublimit;
- (b) it also qualifies as a "security failure" for the 8/4-hour wait and for Coverage G.

A faulty model or platform update that makes many customers' agents misbehave at once would be a **CrowdStrike-style accumulation** hidden inside the full-limit attack bucket. **Recommendation:**

- Treat *non-malicious* agent actions beyond authority as a **system failure** (sublimited).
- Keep *third-party-induced* agent actions (prompt injection, a hijacked agent) as a **security failure**.
- Consider requiring human approval for destructive or payment actions as an underwriting question.

### 3.7 Government alerts and measured AI share

| Item | Date | Key content | URL | Evidence |
|---|---|---|---|---|
| **FinCEN FIN-2024-Alert004** | 2024-11-13 | Deepfake media used to get around identity verification at financial institutions; SAR filings mentioning deepfakes have risen since 2023; red-flag indicators | https://www.fincen.gov/system/files/shared/FinCEN-Alert-DeepFakes-Alert508FINAL.pdf | [SS] |
| **FBI PSA I-120324** | 2024-12-03 | Criminals use generative AI to commit fraud at larger scale: synthetic profiles, fake documents, voice cloning to reach bank accounts | https://www.ic3.gov/PSA/2024/PSA241203 | [SS] |
| **FBI PSA PSA250515** (+ Dec 2025 update PSA251219) | 2025-05-15 / 2025-12-19 | AI voice messages impersonating senior U.S. officials | https://www.ic3.gov/PSA/2025/PSA250515 | [SS] |
| **IC3 2025 report, first AI section** | Apr 2026 | **22,364** AI-tagged complaints, **$893M** losses; AI investment scams **$632M**; AI-enabled BEC **>$30M**; deepfake interviews about **$13M** | https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf ; https://abnormal.ai/blog/ai-cybercrime-ic3-report-2025 | [SS] |

**AI share (my calculation from IC3 figures):** AI-tagged losses were **about 4.3%** of all IC3 losses ($893M / $20.877B) and **about 2% or less** of complaints (22,364 of more than 1M). AI-enabled BEC was **about 1%** of BEC losses ($30M / $3.05B). These are floors, because victims rarely know AI was used.

### 3.8 Insurer data and market response

| Item | Date | Detail | URL | Evidence |
|---|---|---|---|---|
| **Coalition Deepfake Response Endorsement** | Dec 2025 (global) | Pays to respond to deepfake incidents that cause **reputational, legal and operational** harm, even where controls are strong. Coalition says deepfakes are **still a small fraction of claims**, with AI expected to be used regularly in fraud/BEC within **12–24 months** | https://www.coalitioninc.com/announcements/coalition-adds-deepfake-response-endorsement ; https://fintech.global/2025/12/18/coalition-adds-deepfake-cover-to-cyber-insurance/ ; https://cyberscoop.com/url-coalition-cybersecurity-insurance-coverage-deepfakes-reputational-harm/ | [SS] |
| **BOXX Insurance** | n.d. (2025–26) | Adds **affirmative AI and deepfake** cover to its Cyberboxx Business policy | https://www.insurancebusinessmag.com/us/news/cyber/boxx-insurance-adds-affirmative-ai-and-deepfake-coverage-to-cyberboxx-business-policy-583408.aspx | [SS] |
| Market split | from 2026-01-01 | "A number of carriers" **exclude AI-generated deepfake fraud from standard social-engineering cover** on renewals; others affirm it (voice clones, video deepfakes) | https://insuranceindustry.ai/the-deepfake-coverage-gap/ ; https://www.businessinsurance.com/insurers-brokers-adjust-as-ai-exclusions-emerge/ | [SS] (carriers not named in the snippet) |
| ISO generative-AI exclusions (general liability) | Jan 2026 | CG 40 47 / CG 40 48 / CG 35 08 | package Sources #25–26 | [PKG] |
| Deepfake hiring fraud and shadow AI | 2026 | Testing cyber and crime wordings | https://beinsure.com/news/deepfake-hiring-insurance-fraud/ | [SS] (headline) |
| Quantified AI-claims share from any insurer | — | **None found.** Coalition gives only the qualitative "small fraction" | — | gap |

**Correction for the rationale.** It says "At-Bay's 2026 report shows AI is already driving fraud." Nothing retrieved today supports that attribution. Replace it with IC3 2025 (AI-enabled BEC >$30M; $893M AI-tagged) and KnowBe4 (86% of phishing uses AI), or verify it in the At-Bay PDF.

---

## 4. Sector specifics: accounting and tax firms

| Topic | Finding | Source · date | URL | Evidence |
|---|---|---|---|---|
| IRS / Security Summit 2026 | "Protect Your Clients; Protect Yourself" series ran through summer 2026; the closing reminder in **Sept 2026** urged vigilance against identity theft | IRS newsroom · Sep 2026 | https://www.irs.gov/newsroom/security-summit-closes-summer-series-with-data-security-reminder-for-tax-pros | [SS] |
| "New client" scams | Fraudsters pose as prospective clients and send malicious links or attachments disguised as tax documents (spear phishing) | IRS / Security Summit | https://www.irs.gov/newsroom/tax-pros-should-watch-out-for-phishing-emails-and-other-attacks-security-summit-warns ; https://irs.gov/newsroom/tax-security-101-security-summit-reminds-tax-professionals-to-beware-of-spear-phishing-emails | [SS] |
| Credential theft for e-file IDs | Phishing aimed at **EFIN, PTIN and CAF** numbers | IRS / Security Summit | as above | [SS] |
| WISP mandatory | Tax pros must have a **Written Information Security Plan**; Publication 4557 supports FTC Safeguards compliance | IRS | https://www.irs.gov/newsroom/irs-security-summit-remind-tax-pros-they-need-a-written-information-security-plan-to-protect-client-data | [SS] |
| FTC Safeguards notification | Amendment effective **2024-05-13**: notify the FTC within **30 days** of discovering a "notification event" affecting **≥500 consumers'** unencrypted information. No public count of events was found | FTC (16 CFR 314.4(j)) | — | [PK] (search returned no snippet) |
| Professional-services extortion | Law firms targeted by **Silent Ransom / Luna Moth** data-theft extortion, producing large payments (Q2 2026). CPA firms hold similar confidential financial data | Coveware / Veeam · Jul 2026 | https://www.veeam.com/blog/cyber-extortion-payment-trends-q2-2026.html | [SS] |
| Victim size | 11–100 employees = **18.2%** of Coveware Q2 2026 cases; 101–1,000 = 35.4%. Cedar Ridge (62 staff) is in the core target band | Coveware Q2 2026 | same | [SS] |

**Tax-season pattern** (IRS "Dirty Dozen", Security Summit; [PK] beyond the snippets above):

- account takeover of tax-software and e-file credentials (EFIN/PTIN/CAF);
- fraudulent returns filed in clients' names;
- W-2/payroll data requests from a spoofed "CEO";
- "new client" lures from January to April.

**Implications for Cedar Ridge's policy:**

1. Client **identity-theft remediation** (IRS IP PIN, Form 14039 help) should be named as a breach response cost.
2. **Data-theft extortion is the realistic ransomware scenario** for a CPA firm holding SSNs, which makes backups less decisive.
3. **Seasonality in the BI calculation** (already in Section III.4) matters: an attack in March will produce a large claim.
4. Funds held **for clients** are already in "funds transfer loss". Keep this.

---

## 5. Implications: each Harborline design choice against 2025–26 data

Verdict key: **SUPPORTS / CHALLENGES / SILENT / MIXED**. "Harborline" figures are from `policy.md`.

| # | Design choice | Verdict | Key numbers (population · source · evidence) | Recommendation |
|---|---|---|---|---|
| 1 | **$1M aggregate** | **MIXED**: supports for the average, challenges the tail | Average claim: **$180K** (<$25M, At-Bay [PKG]); **$116K** (Coalition [SS]); **$264K** NetDiligence SME average cost [SS]. Ransomware: **$422K** (<$25M, At-Bay [SS/PKG]); **$510K** with BI (At-Bay [SS]); **$961K** with recovery expenses (NetDiligence [SS]); **$638,536** recovery excluding ransom for 100–250 employees (Sophos [SS]); Coveware Q2 2026 average payment **$1.88M** (law-firm exfiltration) [SS] | $1M suits a typical $5–10M firm. For data-heavy professional firms and the $25–50M band, a ransomware claim plus notification plus class-action defense (defense erodes the same aggregate) can pass $1M. **Offer real $2M/$3M options** (round 1 found Item 6 promises "higher limits" that don't exist). |
| 2 | **$7,500–$10,000 retention for $5–25M revenue** | **SILENT on level; SUPPORTS scaling** | Frequency **1.21%** (<$25M) vs **5.72%** (>$100M), Coalition [SS]. $7,500 = about **5%** of Coalition's $141K average FTF, **6.5%** of its $116K average claim, **10%** of NetDiligence's $75K average BEC [SS] | Keep. No data suggests the retention suppresses legitimate SMB claims. The competitors' $2,500 is a pricing, not a risk, argument. |
| 3a | **$250K fraud limit shared with invoice manipulation** | **MIXED** | Below-limit averages: Coalition FTF **$141K** [SS]; IC3 BEC **about $123K per complaint** [SS]; At-Bay <$25M **$208K** [PKG]. Above-limit averages: At-Bay all sizes **$285K (+16%)** [SS]; **$373K** for $25–100M [PKG]. Tail: Arup **$25.6M**; Singapore **$499K** [SS] | Adequate below $25M revenue. **Make Coverage R ($500K) the default for $25–50M insureds.** Sharing with invoice manipulation is SILENT (no invoice data found). Consider a separate $100K invoice sublimit so one event cannot exhaust both. |
| 3b | **$100K cap without callback; $5,000 callback threshold** | **SUPPORTS the control; SILENT on the threshold** | 52% of FTF began with BEC and **39% had no confirmed email compromise** (Coalition [SS]), so email security alone is not enough and out-of-band verification is. Deepfake cases (Arup, Singapore) involved **unverified live calls** that a callback to a number on file would defeat [SS]. FinCEN and FBI alerts stress verification [SS]. $100K is below every average-severity figure above, so the cap will bite on a typical uncallbacked loss, as intended. **Competitive counterpoint:** Beazley BBR 5.0 has **no out-of-band requirement** [PKG]. | Keep. Say plainly in the rationale that the cap is designed to bite. No data on transfer-size distribution justifies $5,000 specifically; add "any change of payee bank details regardless of amount" (the policy already does this). |
| 4 | **72-hour lower fraud retention** | **SUPPORTS** | IC3 RAT **58%** success, **$679M** frozen, 3,900 incidents [SS]. At-Bay **70% vs 27%** recovery (≤3 days vs >30 days) [PKG]. Coalition **$21.8M** recovered in 2025 [SS] | Keep. Consider a 24-hour tier to match the policy's own "ideally within 24 hours" wording. |
| 5 | **8-hour BI waiting period** | **SILENT** (market norm) | No 2025–26 distribution of SMB outage durations found. AWS 2025: **>70,000** organizations hit but insured loss likely about **$40M** (CyberCube [SS]), which shows waiting periods absorb most short cloud outages | Keep. |
| 6 | **180-day restoration** | **SUPPORTS** | About **1 in 10** ransomware cases down >30 days (At-Bay [PKG]); JLR **about 5-week** halt [SS]; M&S disruption **from April "to July"** [SS] | Keep. 90-day forms (Vouch) look short against this evidence. |
| 7a | **$500K dependent BI (attacks), in core** | **MIXED**: supports inclusion, challenges the cap for some sectors | Third-party involvement **48% (+60%)**, DBIR 2026 [SS]. Vendor-caused claims **14%**, average **$145K** (At-Bay [PKG]), so $500K is about **3.4x** the average. CDK: one dealer's paid claim **$839,551** [SS]. JLR: **>5,000** UK organizations affected [SS]. Change Healthcare: **>$3B** of provider advances [SS] | Keep in core. **Ask about single-vendor concentration** in the application (tax software, practice management, clearinghouses) and offer the full-limit option for concentrated insureds. For a CPA firm, a tax-software vendor outage in tax season is the key scenario. |
| 7b | **Dependent system failure optional** | **SUPPORTS** (accumulation) | CrowdStrike insured **$300M–$1.5B** across three estimates; Fortune 500 **10–20% insured** [SS]. AWS insured **$38M–$581M** [SS] | Keep optional. Consider offering it with a longer (12–24h) waiting period so it can be priced for SMBs. |
| 8 | **$250K system-failure sublimit** | **SUPPORTS concept; SILENT on amount** | CrowdStrike / AWS accumulation [SS]. No SMB per-insured system-failure severity found | Keep. **Route non-malicious AI-agent errors here** (see #12b). |
| 9 | **20% ransomware coinsurance without verified backups** | **MIXED** | Supports: backups underlie the **86%** refusal rate (Coalition [SS]) and the **23%** payment rate (Coveware [SS]). Challenges: extortion is moving to **data theft without encryption** (Oracle EBS/Cl0p; Salesloft Drift; Anthropic GTG-2002 with **17** organizations and demands >$500K; Coveware Q2 2026 law-firm exfiltration) [SS], where backups do nothing. **"Ransomware" is undefined** in the policy | **Limit the coinsurance to restoration and BI loss from encryption or destruction**, not to extortion payments or breach costs from data theft. Add a definition of ransomware. Fix the backup test lapsing mid-term (round 1). |
| 10 | **MDR credit (retention halved, 4-hour wait)** | **SUPPORTS direction; SILENT on magnitude** | **60%** of Akira victims had a leading EDR (At-Bay [PKG]), so EDR alone is not enough and 24/7 response matters. DBIR 2026: exploitation leads, and AI compresses attacks "from months to hours" [SS]. Coalition also cut waiting periods for MDR (Apr 2026 [PKG]). No quantified MDR loss-reduction figure was found | Keep. Ask At-Bay/Coalition-style data for evidence of the loss effect before rating. |
| 11 | **10% remote-access premium credit** | **SUPPORTS (strongly)**; arguably too small | Remote access **87%** of ransomware entries; VPN **73%**; SonicWall in **86%** of Akira attacks (At-Bay [SS/PKG]). Vulnerability exploitation **31%**, now the top breach vector (DBIR 2026 [SS]) | Consider making hardened remote access a **condition**, or raising the credit. The KEV rule (insurer notice + 45 days) is slow for internet-facing VPN/firewall bugs exploited within days; consider a **shorter window for edge devices**. |
| 12a | **Affirmative AI clause** | **SUPPORTS** | IC3's first AI section: **22,364** complaints / **$893M**; AI-enabled BEC **>$30M** [SS]. KnowBe4 **86%** of phishing uses AI [SS]. Market split: some carriers **exclude** deepfake fraud from social engineering from **2026-01-01**, while Coalition (Dec 2025) and BOXX **affirm** it [SS]. ISO GL AI exclusions [PKG] | Keep. It is a real differentiator in 2026. Re-source the rationale's "At-Bay shows AI is driving fraud" line (§3.8). |
| 12b | **"AI agent exceeding authority" as a security failure** | **CHALLENGES (drafting)** | Replit (Jul 2025): **non-malicious** agent deleted a production database during a code freeze [SS], which would get full limits and bypass the $250K system-failure sublimit. EchoLeak (CVSS 9.3) and ForcedLeak (CVSS 9.4) leak data *within* permissions [SS], so they may fall outside "exceeding authority" | (i) Treat non-malicious agent errors as a **system failure**. (ii) Treat prompt-injected or hijacked agent actions as a **security failure** by adding "acts on instructions from anyone other than you, including hidden instructions in content it processes". (iii) Add an application question on AI agents with write, delete or payment permissions and on human approval. |
| 13 | **Reputational harm $100K after 14 days** | **SUPPORTS existence; SILENT on amount** | **29%** of breached SMEs found it hard to win new business; **30%** saw business performance fall (Hiscox 2025 [SS]). Gap: Coalition's Deepfake Response Endorsement (Dec 2025) covers **deepfake reputational attacks**, but Harborline's trigger requires an "adverse publication" about a security failure or privacy event, so a **deepfake of a partner** with no breach does not trigger | Keep. Consider adding "deepfake impersonation of the insured or its executives" as a trigger for crisis-response costs (not lost profit). |
| 14 | **Bricking $100K** | **SILENT** | No 2025–26 bricking frequency or severity found. Beazley BBR 5.0 includes bricking [PKG] | Keep. For a 62-person firm, $100K replaces most endpoints. |
| 15 | **Cryptojacking / telecom fraud $50K** | **SILENT in data found; possible CHALLENGE** | No cryptojacking severity data retrieved. [PK] "LLMjacking" (stolen cloud or AI API keys used to run LLMs) was reported by Sysdig (2024) at potentially **>$46K per day** | Verify the LLMjacking figure. **Name AI model/API providers** in "service fraud loss" (currently "cloud, hosting or telephone providers"). $50K is likely enough for SMBs if charges are caught within days. |
| 16 | **Website-tracking liability optional** | **CHALLENGES** (for consumer-facing insureds) | Coalition: privacy claims **doubled in H1 2026** (blog) [SS]; **72%** of privacy claims cite CIPA [PKG]. At-Bay: third-party claims **+70%**, CIPA **34%** [PKG]. CIPA trackers: 675 (2024) → >800 (2025) → projected >3,500 (2026) [SS]; retail most targeted (1,817 cases) [SS]. Counterweights: SB 690 (pen-register only) awaits the Governor [PKG]; BIPA filings down to about 150 in 2025 [SS] | Optional is defensible for Cedar Ridge (B2B-heavy CPA firm). For retail and healthcare insureds, **ask about pixels in the application** and consider a **defense-only core sublimit**. Fix the UDAP exclusion carve-back (round 1), since CIPA suits plead UCL. |

---

## 6. Corrections and updates to the package suggested by this pass

1. **Coalition "privacy claims doubled in H1 2026."** Round 1 said this could not come from the March 2026 report. It **does exist** as a separate Coalition blog: https://www.coalitioninc.com/blog/cyber-insurance/understanding-why-privacy-claims-doubled-in-h1-2026 [SS]. Re-cite it to the blog and add it to Sources. Do not delete it.
2. **Coalition's contrary severity data** (average claim down 19% to $116K; FTF down 14% to $141K; ransomware $269K) should appear next to At-Bay's figures, as the steel-man "benchmarks lean on carrier data" row implies.
3. **At-Bay fraud:** add the all-size average of **$285K (+16%)** next to the $208K under-$25M figure to justify offering Coverage R to $25–50M insureds.
4. **Ransomware "average":** label $508K as all sizes and $422K as under $25M (round 1 flagged the confusion). Use $422K in the Vouch comparison.
5. **Add missing sources** that round 1 flagged as absent from the 33, now with URLs:
   - FBI IC3 2025 report: https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf
   - Coalition Deepfake Response Endorsement: https://www.coalitioninc.com/announcements/coalition-adds-deepfake-response-endorsement
   - FinCEN FIN-2024-Alert004
   - Verizon DBIR 2026
6. **Replace "At-Bay's 2026 report shows AI is already driving fraud"** with IC3 2025 AI figures, unless it is confirmed in the At-Bay PDF.
7. **JLR wording:** "the attack on Jaguar Land Rover disrupted more than 5,000 UK organizations, including its suppliers (Cyber Monitoring Centre, Oct 2025)." Avoid the unsupported help-desk vishing story.
8. **Define "ransomware"** and scope the backup coinsurance to encryption or destruction losses.
9. **Redraft AI-agent item 5** as in §5 row 12b.

## 7. Gaps and items to verify before submission

- **All [SS] figures are search snippets.** Open the originals before quoting. Priority: Coalition 2026 report, At-Bay 2026 PDF (already opened earlier), IC3 2025 PDF, Coveware Q2 2026 (exact payment rate), DBIR 2026 (third-party 48%).
- Not found within budget:
  - Chubb SMB claims data
  - Corvus/Travelers claims severity
  - a quantified AI-claims share from any carrier
  - invoice-manipulation frequency and severity
  - bricking and cryptojacking severity
  - SMB outage-duration distribution
  - FTC Safeguards notification counts
  - OpenAI threat reports
  - any 2026 CrowdStrike-scale systemic event
- [PK] items to verify: DBIR 2025 SMB ransomware 88% / $115K / 64%; NetDiligence "SME" = under $2B revenue; FTC Safeguards 30-day / 500-consumer rule; Snowflake about 165 customers; Anthropic GTG-1002 (Nov 2025); FBI Silent Ransom Group PSA (May 2025); Sysdig LLMjacking cost.

## 8. Source index (evidence level: all [SS] unless marked)

| Source | Date | URL |
|---|---|---|
| Coalition, 2026 Cyber Claims Report (press release / blog / page) | 2026-03-05 | https://www.coalitioninc.com/announcements/2026-cyber-claims-report ; https://www.coalitioninc.com/blog/cyber-insurance/2026-cyber-claims-report ; https://www.coalitioninc.com/claims-report/2026 |
| Coalition, Understanding Why Privacy Claims Doubled in H1 2026 | 2026 | https://www.coalitioninc.com/blog/cyber-insurance/understanding-why-privacy-claims-doubled-in-h1-2026 |
| Risk & Insurance on Coalition 2026 | 2026 | https://riskandinsurance.com/cyber-claims-frequency-rises-but-severity-falls-as-businesses-improve-defensive-posture/ |
| At-Bay, 2026 InsurSec Report (+ coverage) | Apr 2026 | https://www.at-bay.com/articles/insursec-report-2026-key-findings-cyber-risk/ ; https://www.helpnetsecurity.com/2026/04/23/cyber-insurance-claims-report/ ; https://insurance-edge.net/2026/04/27/at-bay-report-looks-at-vpn-ransomware-risks/ ; https://www.insurancebusinessmag.com/us/news/cyber/one-ransomware-crew-now-drives-half-of-all-cyber-claims-atbay-573139.aspx |
| NetDiligence Cyber Claims Study 2025 | ~Sep 2025 | https://rsmus.com/content/dam/rsm/insights/services/risk-fraud-cybersecurity/1pdf/net-diligence-cyber-claims-study-2025-report.inline.pdf ; https://www.carriermanagement.com/news/2025/09/25/279803.htm |
| Verizon 2026 DBIR | 2026 | https://www.verizon.com/business/resources/reports/dbir/ ; https://www.verizon.com/business/resources/executivebriefs/2026-dbir-executive-summary.pdf |
| FBI IC3 2025 Internet Crime Report | Apr 2026 | https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf ; https://www.fbi.gov/news/press-releases/cryptocurrency-and-ai-scams-bilk-americans-of-billions |
| Coveware Q3 2025 | Oct 2025 | http://coveware.com/2025/10/insider-threats-loom-while-ransom-payment-rates-plummet/ |
| Coveware by Veeam Q2 2026 | Jul 2026 | https://www.veeam.com/blog/cyber-extortion-payment-trends-q2-2026.html ; https://coveware.com/2026/07/adverse-cyber-extortions-are-more-common-than-commonly-advised/ |
| Sophos State of Ransomware 2025 | Jun 2025 | https://www.sophos.com/en-us/press/press-releases/2025/06/nearly-half-companies-opt-pay-ransom-sophos-report-finds |
| Hiscox Cyber Readiness Report 2025 | 2025-09-29 | https://www.hiscoxgroup.com/news/press-releases/2025/29-09-25 |
| Beazley Spotlight on Cyber Threats and Tech Advances 2026 | 2026 | https://www.beazley.com/en-us/news-and-events/spotlight-on-cyber-threats-and-tech-advances-2026 |
| Travelers/Corvus Q1 2026 threat report (via LinkedIn) | 2026 | https://www.linkedin.com/posts/michael-smith-jr-cpcu-9823676_travelers-ransomware-attacks-hit-near-record-activity-7473070847369519104-F3gr |
| CrowdStrike loss estimates | Jul–Aug 2024 | https://www.insurancejournal.com/news/national/2024/08/02/786766.htm ; https://www.claimsjournal.com/news/national/2024/07/26/325332.htm ; https://www.cybersecuritydive.com/news/crowdstrike-cost-fortune-500-losses-cyber-insurance/722396/ |
| Change Healthcare (CNBC) | 2024-03-27 | https://www.cnbc.com/2024/03/27/unitedhealth-group-paid-over-3-billion-to-providers-since-cyberattack.html |
| CDK Global | 2024– | https://www.autonews.com/dealers/cdk-cyberattacks-fade-dealerships-confront-claims-process/ ; https://www.reedsmith.com/articles/insurance-may-dealership-financial-losses-due-cdk-global-cyberattack/ |
| AWS outage estimates | Oct 2025 | https://www.reinsurancene.ws/cybercube-estimates-preliminary-aws-outage-loss-range-of-38-581m/ ; https://www.insurancejournal.com/news/national/2025/10/27/845197.htm ; https://insurance-edge.net/2025/10/30/parametrix-estimates-aws-outage-costs/ |
| JLR (CMC) | 2025-10-22 | https://cybermonitoringcentre.com/2025/10/22/cyber-monitoring-centre-statement-on-the-jaguar-land-rovercyber-incident-october-2025/ ; https://www.blastwave.com/blog/jaguar-land-rover-the-most-expensive-cyberattack-in-british-history-and-the-story-everyone-told-about-it-came-from-nowhere |
| M&S | 2025 | https://www.businessinsurance.com/marks-spencer-gets-130-million-in-insurance-from-cyberattack/ ; https://therecord.media/british-retailer-marks-spencer-insurance |
| Salesloft Drift | 2025 | https://www.finra.org/rules-guidance/guidance/salesloft-drift-AI-supply-chain-attack ; https://www.anomali.com/blog/salesloft-drift-breach-recap |
| Oracle EBS / Cl0p | 2025 | https://www.cybersecuritydive.com/news/oracle-e-business-suite-exploitation-july/802592/ ; https://www.paubox.com/blog/cl0p-ransomware-gang-names-29-oracle-ebs-breach-victims |
| Arup deepfake | 2024 | https://purplesec.us/breach-report/arup-deepfake/ |
| Anthropic, Detecting and countering misuse of AI: August 2025 | Aug 2025 | https://www.anthropic.com/news/detecting-countering-misuse-aug-2025 |
| ESET PromptLock / NYU | Aug–Sep 2025 | https://www.welivesecurity.com/en/ransomware/first-known-ai-powered-ransomware-uncovered-eset-research/ ; https://engineering.nyu.edu/news/ai-powered-ransomware-emerging-threat-could-bring-down-your-organization |
| Google GTIG AI Threat Tracker | 2025-11-05 | https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools |
| EchoLeak CVE-2025-32711 | Jun 2025 | https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html |
| ForcedLeak | Sep 2025 | https://www.theregister.com/2025/09/26/salesforce_agentforce_forceleak_attack/ |
| Replit agent incident | Jul 2025 | https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/ |
| FinCEN FIN-2024-Alert004 | 2024-11-13 | https://www.fincen.gov/system/files/shared/FinCEN-Alert-DeepFakes-Alert508FINAL.pdf |
| FBI PSAs | 2024-12-03; 2025-05-15; 2025-12-19 | https://www.ic3.gov/PSA/2024/PSA241203 ; https://www.ic3.gov/PSA/2025/PSA250515 ; https://www.ic3.gov/PSA/2025/PSA251219 |
| Coalition Deepfake Response Endorsement | Dec 2025 | https://www.coalitioninc.com/announcements/coalition-adds-deepfake-response-endorsement ; https://cyberscoop.com/url-coalition-cybersecurity-insurance-coverage-deepfakes-reputational-harm/ |
| BOXX affirmative AI | n.d. | https://www.insurancebusinessmag.com/us/news/cyber/boxx-insurance-adds-affirmative-ai-and-deepfake-coverage-to-cyberboxx-business-policy-583408.aspx |
| Heiding et al. (AI spear phishing) | 2024 | https://arxiv.org/pdf/2412.00586 |
| Hoxhunt | Apr 2025 | https://hoxhunt.com/blog/ai-powered-phishing-vs-humans |
| KnowBe4 | 2026-04-30 | https://www.businesswire.com/news/home/20260430743735/en/KnowBe4-Research-Finds-86-of-Phishing-Attacks-are-AI-Driven |
| CIPA trackers | 2026 | https://cookie-script.com/privacy-laws/cipa-lawsuit-tracker ; https://consentpixel.com/blogs/cipa-lawsuit-tracker/ |
| BIPA 7th Circuit | 2026-04-08 | https://datamatters.sidley.com/2026/04/08/seventh-circuit-limits-potential-damages-under-bipa-holds-2024-amendment-applies-retroactively/ |
| IRS Security Summit | 2026 | https://www.irs.gov/newsroom/security-summit-closes-summer-series-with-data-security-reminder-for-tax-pros ; https://www.irs.gov/newsroom/irs-security-summit-remind-tax-pros-they-need-a-written-information-security-plan-to-protect-client-data |
