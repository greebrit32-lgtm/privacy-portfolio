# 🔒 FACILITATOR SCRIPT — SEALED UNTIL AFTER THE EXERCISE (S7)

> **Brittany: do not open until the exercise is over.** It contains the hidden facts and twists.
>
> _Fictional organization, people, and data. Independent educational exercise. Not legal advice. Legal references point to the [source register](../../sources/source-register.md)._

---

## A. Ground truth (revealed only when asked or through injects)

| Fact | Truth | When it can be learned |
|----------------|---------------------------------------------------------------|--------------------|
| Initial access | Stolen password for the **MSP's remote-access tool** account (no multi-factor authentication) | Day 4, MSP/forensics |
| Attacker in network since | **Wed, Jan 6, 2027** (Day −9) | Day 4, forensics |
| Earlier warning sign | On **Tue, Jan 12** (Day −3), the MSP's endpoint tool flagged suspicious activity on the file server. An MSP technician **closed the ticket without escalating** it to the clinic | Day 4 if the Privacy Lead asks about earlier alerts; otherwise Day 7 (forensics report) |
| Data copied out | ~4.2 GB from three shared-drive folders: `Intake_Scans_2014-2019` (with SSNs), `Lab_Results`, `Billing_Exports` | Day 5, forensics (counsel-directed) |
| EHR (SYS-1) | **No evidence of access.** Cloud EHR logs are clean | Day 3, EHR vendor |
| Backups | On-site backups were on a network share and **were encrypted too**. An off-site copy dated **Tue, Jan 5** (before the intrusion) is clean. Restoring it loses 10 days of shared-drive files | Day 1, MSP |
| Workstations | 31 of 45 encrypted | Day 1 |
| Affected individuals (final count, Day 7) | **11,400 unique patients**: **11,050 Texas**, **210 Oklahoma**, **140 Louisiana**. Includes **2,900 minors**. SSNs for **3,800**. Out-of-date addresses for **620** | Day 7 |
| Employee data | One staff spreadsheet (out of scope; note only) | Day 5 |
| Leak site | Attackers post 5 sample lab-result PDFs on **Thu, Jan 21** (Day 6) | Day 6 |
| Law enforcement | FBI field office agent, contacted Day 1 | Day 2 (delay request) |

**Date reference:** Day 0 = Fri Jan 15, 2027. Day 1 Sat 1/16 · Day 2 Sun 1/17 · Day 3 Mon 1/18 · Day 4 Tue 1/19 · Day 5 Wed 1/20 · Day 6 Thu 1/21 · Day 7 Fri 1/22 · Day 10 Mon 1/25 · Day 12 Wed 1/27 · Day 14 Fri 1/29 · Day 20 Thu 2/4.

## B. Inject schedule (about 60 minutes)

| # | Play min | Incident time | Inject (read aloud) | Expected decisions / good practice | Tests |
|-------|-------|-------|----------------------------|---------------------------------------------------------|-------|
| **0** | 0 | Fri 1/15, 10:05 p.m. | Briefing situation. **"What do you do in the first hour?"** | Declare **SEV-1**. **Record discovery: Fri 1/15, 9:40 p.m.** (workforce knowledge). Isolate, don't wipe; preserve the ransom note and logs. Call the insurer hotline; activate the team; brief the Privacy Officer. Don't contact the attackers | O1, O2; Playbook §3, §4.1–4.2 |
| **1** | 6 | Sat 1/16, 9:00 a.m. | MSP: "On-site backups are encrypted too. We have an off-site copy from **Jan 5**. 31 of 45 workstations hit." The Medical Director asks: "Can we open Monday?" | Clinical decision belongs to the Medical Director (downtime procedures). Privacy Lead: confirm the off-site copy predates the intrusion before restoring; **evidence preserved before rebuild** | O2, O6 |
| **2** | 12 | Sun 1/17, 2:00 p.m. | **FBI agent (phone):** "Please hold off notifying patients for **two weeks**. It could tip off the group." | §164.412(b): an **oral** request must be **documented, including the official's identity**; delay **≤ 30 days** unless a **written** statement follows. Ask for it in writing. Calendar the end date. Note that Texas allows delay while law enforcement says notice would impede the investigation (§521.053(d)) | O2, O4; Matrix "pausing the clocks" |
| **3** | 18 | Mon 1/18, 11:30 a.m. | **Downtime problem:** a front-desk lead forwarded **12 patients'** lab results to her **personal Gmail** "to keep working." The EHR vendor reports **no evidence of EHR access**. | Treat Gmail as a **separate privacy incident** (SEV-3): retrieve, get written deletion attestation, document a 4-factor assessment (likely low probability if deleted and not further used; Brittany decides). Track separately (under 500 → annual HHS log if it is a breach) | O6, O3; Playbook §3, §5 |
| **4** | 24 | Tue 1/19, 4:00 p.m. | **Forensics (via counsel):** "Entry was through the **MSP's remote-access account**, no MFA. Attacker present since **Jan 6**." *(If the Privacy Lead asks about earlier alerts, reveal the **Jan 12 closed ticket**.)* **Billing company:** "Our SFTP drop folder is `Billing_Exports` on your server. Do **we** have to notify anyone?" | **Business associate dimension:** the MSP is a BA whose account was the entry point. Request its written incident report (§164.410). **Discovery-date discussion:** does the Jan 12 alert mean the breach "would have been known" earlier (§164.404(a)(2))? Note that MSP knowledge counts against the clinic only if the MSP acted as the clinic's *agent* (federal common law of agency); escalate to the breach coach and document the reasoning. To the billing company: the breach is at the clinic's system, so **the clinic notifies**; the billing company should preserve its records and cooperate | O1, O2, O3; Playbook §4.1–4.2 |
| **5** | 30 | Wed 1/20, 10:00 a.m. | **Forensics:** "Confirmed: ~4.2 GB copied from `Intake_Scans_2014-2019`, `Lab_Results`, `Billing_Exports`. Also one staff spreadsheet." | **Breach determination:** HIPAA presumption (and HHS's ransomware position) plus confirmed exfiltration means a **low probability can't be shown**. **Breach.** Record the **Texas determination date** (likely 1/20, or 1/15 if treated conservatively). **Texas AG deadline:** Feb 19 (from 1/20) or Feb 14 (from 1/15); file early | O3, O4; Playbook §5; Matrix §3 |
| **6** | 36 | Thu 1/21, 8:00 a.m. | **Leak site:** attackers post **5 sample lab-result PDFs** with patient names visible. | Confirms factor 3 ("actually acquired or viewed"). Accelerate notice ("without unreasonable delay"). Monitoring and takedown are counsel/insurer actions. Consider **urgent notice** to the 5 patients by phone (§164.404(d)(3)), subject to the FBI request (check whether it was ever put in writing) | O3, O4, O5 |
| **7** | 42 | Fri 1/22, 3:00 p.m. | **Final counts:** 11,400 patients (11,050 TX, 210 OK, 140 LA); 2,900 minors; SSNs for 3,800; **620** with outdated addresses. | **Which notices:** individuals (all); **Texas AG** (≥ 250 TX); **HHS** at the same time (≥ 500); **media in Texas** (more than 500 TX residents); **no media** for OK or LA (≤ 500 each); **consumer reporting agencies** (more than 10,000); **OK/LA residents:** their states' laws or Texas (b-1), *identify only*. **Substitute notice** for 620 (10 or more: 90-day web posting or major media, plus a toll-free number for 90 days). Minors: confirm with counsel how notices are addressed to parents or guardians (personal representative rules are not in this project's sources) | O4; Matrix §1–§2 |
| **8** | 48 | Mon 1/25, 9:00 a.m. | **Local reporter** calls the front desk: "Is it true patient records were hacked?" **FBI email:** "You may proceed with notifications." | Front desk refers the call to the Practice Administrator; **no speculation**; use the approved holding statement. FBI email ends any delay. Record it | O5, O2 |
| **9** | 54 | Wed 1/27, 1:00 p.m. | **Practice Administrator:** "The board is asking: if we **pay the ransom** and they delete the data, do we still have to notify?" | Notification doesn't depend on payment. HHS treats ransomware encryption as acquisition, and here data was **confirmed copied and partly posted**. Payment is a leadership/legal decision, outside the privacy determination. **Notify regardless** | O3, O5; Playbook §5 |
| **10** | 58 | Fri 1/29 | **Wrap-up:** "Walk me through your notification plan with dates." | A plan with dates: AG filing (before Feb 14/19); individual letters, HHS portal, and Texas media by **Mar 16** at the latest, but **as soon as possible**; CRA notice; substitute notice; call center | O4 |

## C. Answers in character (if asked)
- **Cyber insurer:** "We'll assign a breach coach and a forensics firm under counsel. Don't contact the threat actor."
- **EHR vendor (Day 3+):** "No anomalous access to your tenant in the past 30 days."
- **MSP (before Day 4):** "Still investigating." (After Day 4) "Our tech closed a Jan 12 alert as a false positive. We're reviewing it."
- **Medical Director:** decides clinic operations. Asks whether patients should be told anything Monday.
- **Practice Administrator:** wants a single holding statement by Monday morning.
- **Anything not in this script:** "Unknown at this time."

## D. Evaluation guide (for the after-action review)

| Objective | Met if… |
|-----------|-----------------------------------------------------------------------------------------|
| O1 | Discovery date recorded at the start (Fri 1/15, 9:40 p.m.); SEV-1; Jan 12 alert considered and documented |
| O2 | Insurer and counsel engaged early; evidence preserved; FBI oral request documented with identity and limits; BA (MSP) report requested |
| O3 | Breach determination documented with the 4 factors or the presumption; Gmail handled as a separate assessment |
| O4 | All applicable notices identified with correct thresholds and dates; substitute notice and CRAs caught; other-state residents identified |
| O5 | Single voice; no speculation to the reporter; ransom question answered without tying it to notification |
| O6 | Downtime workaround (Gmail) recognized as a new incident |

**Designed traps:** (1) the Jan 12 ticket and the discovery date; (2) the oral FBI request with no written follow-up; (3) the Gmail workaround; (4) "pay and they'll delete it"; (5) the thresholds (media per state; CRAs over 10,000; substitute notice at 10+); (6) the billing company asking whether *it* must notify.
