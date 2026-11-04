# Session Log — Project 03

## S0 — 2026-11-03 — Plan approved ✅
**Done**
- Brittany chose **Scenario C**: a fictional Texas health clinic (HIPAA). Considered: A, Mesquite Lantern breach of the accepted warehouse risk R-13; B, Pecan Hollow ISD vendor breach. Reason: adds healthcare for a three-sector portfolio.
- Approved the 11-session plan and six deliverables (playbook, notification matrix, tabletop package, live exercise record and breach analysis, notification drafts, after-action report). Plan is in `README.md`.
- Scaffolded folders, source register, and study notes.

**Next step (S1):** Draft `scenario.md`: fictional clinic name (checked to avoid real clinics), size, services, patient population (types only), key systems and vendors (by role), and the incident type for the exercise (e.g., ransomware vs. misdirected records). Brittany picks.

**Open questions for Brittany**
- Incident type for the exercise (S1).
- Push: Project 03 commits stay local until Brittany OKs a push.

## S1 — 2026-11-03 — Scenario and fictional organization ✅
**Done**
- Brittany's decisions: incident = **ransomware** (with a claim that data was stolen first); clinic type = **family medicine** (all ages, including minors); name = **Agarita Family Medicine** (no match found in web searches on 2026-11-03; rejected "Coyote Ridge," which a correctional center and a veterinary clinic use).
- Drafted `scenario.md`: clinic profile (2 sites, 12 providers, about 18,000 patients incl. minors, a few out-of-state); systems and vendors by role (cloud EHR, **on-site file server with older SSN intake forms and lab PDFs**, workstations, email, MSP-managed backups with undocumented isolation, MSP / billing company as business associates, cyber insurer); incident premise (details deferred to S5); exercise roles (Brittany = privacy lead; Claude = facilitator); scope; review standards (named only).

**Next step (S2):** Legal and framework sources: HIPAA Breach Notification Rule (45 CFR Part 164 Subpart D) and Security Rule incident provisions (eCFR), HHS ransomware guidance and the HHS breach portal, Texas breach-notification law (Bus. & Com. Code Ch. 521) and Texas medical-records privacy law (Health & Safety Code Ch. 181), and NIST incident-handling guidance (SP 800-61, current revision). Check statute currency on official sites.

**Open questions for Brittany**
- Review `scenario.md`.
- Push on hold (1 commit ahead plus this one).

## S2 — 2026-11-03 — Legal and framework sources ✅
**Done**
- Registered S01–S09: HIPAA Breach Notification Rule (45 CFR 164 Subpart D) and Security Rule incident provisions (§§164.304, 164.308(a)(6)), from eCFR, current as of 2026-11-02 with no amendments in eCFR history since 2017 (so the proposed Security Rule overhaul is not in effect); the HHS Ransomware fact sheet (hhs.gov blocks downloads; read from an Internet Archive capture of 2026-10-26); Texas Bus. & Com. Code §§521.002/521.053 (codified, plus H.B. 4390 (2019), S.B. 768 (2023), a mirror); the Texas AG Data Breach Reporting page; and NIST SP 800-61 Rev. 3 (April 2025; CSF 2.0 profile).
- **Statute check (Brittany, official site):** §521.002 last amended 2009; §521.053 last amended 2023 (S.B. 768). Nothing later.
- **Decision (Brittany):** Texas Health & Safety Code Ch. 181 is out of scope (noted as related, not assessed).
- Study notes: HIPAA breach presumption and the 4 factors; HHS's ransomware position; the HIPAA vs. Texas notification clocks.

**Key points for S3–S4 (sourced)**
- Ransomware encryption of ePHI = "acquired," so a breach is presumed unless low probability is shown by the 4-factor assessment [S03; §164.402].
- HIPAA: individuals within 60 days of discovery (§164.404(b)); media if more than 500 residents of a state (§164.406); HHS at the same time as individual notice if 500+, else an annual log (§164.408); business associates notify the covered entity (§164.410); law-enforcement delay (§164.412).
- Texas: health information is sensitive personal information (§521.002(a)(2)(B)); individuals within 60 days of determining the breach (§521.053(b)); AG within 30 days if 250+ Texans, by electronic form (§521.053(i)); consumer reporting agencies if more than 10,000 notified (§521.053(h)); residents of other states may be notified under their own state's law (§521.053(b-1)).

**Next step (S3):** Incident response playbook: roles, severity levels, response phases mapped to NIST SP 800-61r3 / CSF 2.0 functions, and a breach-notification decision tree (HIPAA 4-factor plus Texas triggers).

**Open questions for Brittany**
- Push on hold.

## S3 — 2026-11-03 — Incident response playbook ✅
**Done**
- Read NIST SP 800-61r3's structure: CSF 2.0 Functions; Table 1 maps the old phases to Govern/Identify/Protect (preparation), Detect/Respond/Recover (response), and ID.IM (improvement).
- Wrote `deliverables/1-incident-response-playbook.md`: purpose and scope (§164.308(a)(6), §164.304); roles and contact tree (roles only); **severity levels SEV-1–4 (approved by Brittany)**; phases with checklists mapped to CSF categories (DE.CM/AE, RS.MA/AN/CO/MI, RC.RP/CO, ID.IM); HIPAA breach determination (presumption, 4 factors, HHS ransomware position, burden of proof §164.414); a **Mermaid decision tree** (rendered and checked in Chrome); a notification clock table (HIPAA individuals/HHS/media; Texas individuals/AG/CRAs; other states via §521.053(b-1)); records to keep; communication rules.
- Verified §164.412 (oral law-enforcement request: document it, delay ≤ 30 days) and §164.404(c)(2) (plain language) against the text.

**Next step (S4):** Notification requirements matrix (`deliverables/2-notification-matrix.md`): each obligation with trigger, recipient, deadline, method, required content, and source, plus a worked example of the clock for a Friday discovery.

**Open questions for Brittany**
- Push on hold.

## S4 — 2026-11-03 — Notification requirements matrix ✅
**Done**
- Read the remaining HIPAA text: §164.404(d) methods (first-class mail or agreed email; substitute notice for under 10 vs. 10+; urgent phone notice), §164.406(c) (media content = §164.404(c)), §164.410(c) (business associate content).
- Confirmed via S07 that Texas §521.053 lists **no content requirements for individual notices** (only the AG notice in (i)); (h) CRAs get "the timing, distribution, and content of the notices"; (b-1) other-state residents may be notified under their state's law or Texas (b).
- Wrote `deliverables/2-notification-matrix.md`: 10 rows (N-1 to N-7 incl. substitute and urgent notice, HHS 500+ vs. annual log), a threshold-at-a-glance table, and a **worked example** (discovery Fri 2027-01-15; Texas determination Wed 2027-01-20): Texas AG due **Feb 19** (comes first), HIPAA individuals/media/HHS due **Mar 16**, annual log Feb 29, 2028. Dates computed with code. PDF 4 pages.
- `tools/fit_tables.py` now sizes columns by mean cell length (median under-sized columns with a few long cells).

**Next step (S5):** Tabletop design: the incident storyline with a timed inject schedule (each inject: time, what the participants learn, the decision expected, the playbook/matrix section it tests), and hidden "ground truth" facts the facilitator reveals.

**Open questions for Brittany**
- Push on hold.
