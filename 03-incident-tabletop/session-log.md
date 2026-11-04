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
