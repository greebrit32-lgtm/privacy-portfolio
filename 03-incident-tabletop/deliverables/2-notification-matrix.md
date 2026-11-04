# Breach Notification Requirements Matrix — Agarita Family Medicine

**Applies to:** a breach of unsecured protected health information (PHI) at Agarita Family Medicine *(fictional)*, a HIPAA covered entity in Texas

**Prepared by:** Brittany Green, Privacy Analyst · **Date:** 2026-11-03 · **Legal sources current as of:** 2026-11-03 ([register](../sources/source-register.md))

> _Independent educational exercise. Fictional organization. Not legal advice. Companion to the [playbook](1-incident-response-playbook.md)._

**Two laws, two starting points.** HIPAA deadlines run from **discovery**, the first day the breach is known or would have been known with reasonable diligence (45 CFR §164.404(a)(2) [S01]). Texas deadlines run from **the date the clinic "determines that the breach occurred"** (Tex. Bus. & Com. Code §521.053(b), (i) [S05, S06]). Health information is "sensitive personal information" under Texas law (§521.002(a)(2)(B) [S07; currency S04]), so a HIPAA breach at a Texas clinic also triggers Texas duties.

## 1. Matrix

| # | Notify | Trigger | Deadline | Method | Required content | Source |
|-------|----------|--------------|-------------------|------------------------|-----------------------|----------|
| N-1 | **Affected individuals** (HIPAA) | Breach of unsecured PHI | Without unreasonable delay; **≤ 60 calendar days after discovery** | First-class mail to last known address, or email if the individual agreed to electronic notice. May be sent in more than one mailing as information becomes available | (A) what happened, with breach and discovery dates; (B) types of PHI involved; (C) steps individuals should take; (D) what the clinic is doing to investigate, mitigate, and prevent; (E) contact procedures, including a toll-free number, email, website, or postal address. **Plain language** | §164.404(b)–(d) [S01] |
| N-1a | Substitute notice (HIPAA) | Contact info insufficient or out of date | Same as N-1 | **Under 10 people:** alternative written notice, phone, or other means. **10 or more:** a 90-day conspicuous home-page posting **or** major print/broadcast media where they likely live, **plus** a toll-free number active **≥ 90 days** | Whether the person's PHI may be included | §164.404(d)(2) [S01] |
| N-1b | Urgent notice (HIPAA, optional) | Possible imminent misuse | Additionally, as needed | Telephone or other means, **in addition to** written notice | — | §164.404(d)(3) [S01] |
| N-2 | **Affected Texas residents** (Texas) | Breach of system security involving sensitive personal information | Without unreasonable delay; **≤ 60th day after determining the breach occurred** (exceptions: law-enforcement delay; time needed to determine scope and restore the system) | Written notice to last known address; electronic notice; or substitute notice in limited cases (cost over $250,000, more than 500,000 people, or insufficient contact info) | **None specified** in §521.053 for individuals. The HIPAA N-1 letter is used | §521.053(b), (e), (f) [S05, S07; S04] |
| N-3 | **Texas Attorney General** | **250+ Texas residents** affected | As soon as practicable; **≤ 30th day after determining the breach occurred** | **Electronically**, using the form on the AG's website. The report may be an open record | (1) nature and circumstances; (2) number of Texas residents affected; (3) number already notified by mail or other direct method; (4) measures taken; (5) measures planned; (6) whether law enforcement is investigating | §521.053(i) [S06]; AG page [S08] |
| N-4 | **HHS (Secretary), 500+** | Breach of unsecured PHI involving **500 or more individuals** | **At the same time as** individual notice (N-1) | "In the manner specified on the HHS Web site" | As specified by the HHS web form | §164.408(b) [S01] |
| N-4a | **HHS (Secretary), under 500** | Fewer than 500 individuals | Log the breach; submit **≤ 60 days after the end of the calendar year** of discovery | HHS website | As specified by HHS | §164.408(c) [S01] |
| N-5 | **Prominent media outlets** | **More than 500 residents of one state** | Without unreasonable delay; **≤ 60 calendar days after discovery** | Media serving that state | Same content as N-1 | §164.406 [S01] |
| N-6 | **Nationwide consumer reporting agencies** | Clinic must notify **more than 10,000 persons at one time** (Texas) | Without unreasonable delay | — | "the timing, distribution, and content of the notices" | §521.053(h) [S07; S04] |
| N-7 | **Residents of other states** | Affected patients living outside Texas | Per that state's law, or under Texas §521.053(b) | — | — | §521.053(b-1) [S07; S04]. **Other states' laws not assessed** (scope) |

**Pausing the clocks:** a law-enforcement statement that notice would impede an investigation delays HIPAA notice for the period in a written statement, or up to 30 days for a documented oral statement (§164.412 [S01]). Texas allows delay while law enforcement determines that notice would impede a criminal investigation (§521.053(d) [S07; S04]).

**Business associates:** if the breach occurs at the MSP or the billing company, that business associate must notify the clinic within 60 days of *its* discovery, identifying affected individuals where possible and supplying the information needed for N-1 (§164.410 [S01]). The clinic's own clocks still apply to its notices.

## 2. Which rows apply? (thresholds at a glance)

| Affected individuals | N-1 / N-2 | N-3 AG | N-4 HHS | N-5 Media | N-6 CRAs |
|-----------------------------|---------------|----------|-----------------|---------------|-------------|
| 1–249 | ✔ | — | Annual log (N-4a) | — | — |
| 250–499 (Texas) | ✔ | ✔ | Annual log (N-4a) | — | — |
| 500 | ✔ | ✔ | ✔ at the same time | — (needs **more than** 500 in one state) | — |
| 501–10,000 (one state) | ✔ | ✔ | ✔ | ✔ | — |
| More than 10,000 | ✔ | ✔ | ✔ | ✔ | ✔ |

*Thresholds use different units: AG = Texas residents; media = residents of one state; HHS = total individuals; CRAs = persons notified at one time.*

## 3. Worked example (illustrative dates)
**Assume:** the ransom note is seen **Friday, January 15, 2027** (HIPAA discovery, Day 0). Forensics confirms data was copied on **Wednesday, January 20, 2027**, and the clinic determines a breach occurred that day (the Texas start date).

| Deadline | Rule | Date |
|---------------------------------------|---------------------------------|---------------------------|
| Texas Attorney General (N-3) | ≤ 30 days after Texas determination | **Fri, Feb 19, 2027** |
| *If Texas determination = discovery day* | *≤ 30 days after Jan 15* | *Sun, Feb 14, 2027* |
| Individuals (HIPAA, N-1); media (N-5); HHS 500+ (N-4) | ≤ 60 days after discovery | **Tue, Mar 16, 2027** |
| Individuals (Texas, N-2) | ≤ 60 days after Texas determination | Sun, Mar 21, 2027 (HIPAA's Mar 16 comes first) |
| HHS annual log if under 500 (N-4a) | ≤ 60 days after end of 2027 | Tue, Feb 29, 2028 |

**Takeaways:**
1. **The Texas Attorney General deadline comes first** (30 days), even though its clock may start later.
2. **HIPAA's 60 days runs from discovery**, so a slow investigation doesn't move it.
3. Neither law, as read, extends a deadline that falls on a weekend. Plan to file early.
4. **The 60 days are an outer limit:** both laws require notice "without unreasonable delay."

*(Dates computed with code and checked. Day counts start the day after the triggering date.)*

## 4. Not covered
- Other states' breach laws for non-Texas patients (N-7): identify them, then assess separately.
- Texas Health & Safety Code Ch. 181 (out of scope).
- Contract duties in business associate agreements (not public; would be checked in a real incident).

---
_Independent educational exercise. Fictional organization. Not legal advice._
