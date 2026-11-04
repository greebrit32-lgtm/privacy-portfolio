# Scenario — Agarita Family Medicine

> **FICTIONAL ORGANIZATION.** Agarita Family Medicine, its staff, patients, vendors, and the incident are invented for this exercise. Patients and records are described by **type** only. On 2026-11-03, web searches found no Texas clinic named "Agarita Family Medicine."

_Disclaimer: independent educational exercise. Fictional organization and data. Not legal advice._

## 1. Clinic profile (fictional)

| Item | Value |
|------|-------|
| Name | Agarita Family Medicine, P.A. |
| Location | Two clinic sites in Central Texas (generic; no real addresses) |
| Services | Family medicine for all ages: well visits, pediatrics, chronic care, minor procedures, in-house lab draws |
| Size | 12 providers; about 60 staff |
| Patients | About 18,000 active patients, **including minors**. Nearly all are Texas residents; a small number live in neighboring states |
| Privacy and security roles | The Practice Administrator is the designated Privacy Officer. The IT Manager is the designated Security Officer. **Brittany Green, Privacy Analyst**, supports both and leads privacy decisions during incidents |

## 2. Systems and vendors (described by role)

| ID | System / vendor | Role | Holds (types) |
|----|-----------------|------|---------------|
| SYS-1 | Cloud electronic health record (EHR) and patient portal | EHR vendor (business associate) | Full medical records, demographics, insurance, portal accounts |
| SYS-2 | **On-site file server** (shared drives) | Clinic-managed | Scanned intake forms (older ones include Social Security numbers), referral letters, lab result PDFs, billing exports, staff spreadsheets |
| SYS-3 | Staff workstations (about 45) | Clinic-managed | Cached documents, saved EHR sessions, email |
| SYS-4 | Email (cloud) | Email provider | Messages with attachments, including referrals and lab results |
| SYS-5 | Backups | Managed IT provider | Nightly copies of SYS-2. Retention and isolation **not documented** |
| VEN-1 | Managed IT service provider (MSP) | Business associate; remote access to SYS-2/SYS-3 | — |
| VEN-2 | Medical billing company | Business associate | Claims, insurance IDs, diagnosis and procedure codes |
| VEN-3 | Cyber insurance carrier | Provides a breach coach and forensics firm on notice | — |

**Data types on the file server (SYS-2):** patient names, dates of birth, addresses, phone numbers, insurance member IDs, Social Security numbers (older intake forms), diagnoses and lab results (in referral letters and lab PDFs), records of minors, and billing exports with diagnosis and procedure codes.

## 3. Incident premise (details are scripted in S5)
**Ransomware.** Late on a Friday, staff at one site see files they can't open and a ransom note on screen. The note claims the attackers have **copied** data before encrypting it and will publish it unless paid. The initial access route, what was copied, and whether backups survived are **unknown at the start**. Working those out is part of the exercise.

## 4. Exercise roles (fictional)

| Role | In the exercise |
|------|-----------------|
| Privacy Analyst (incident privacy lead) | **Brittany.** Makes the privacy and notification decisions in real time |
| Practice Administrator / Privacy Officer | Executive decisions, patient communications |
| IT Manager / Security Officer | Containment, technical facts |
| MSP incident lead (VEN-1) | Technical investigation; a business associate |
| Medical Director | Patient safety and clinical operations |
| Breach coach (outside counsel via VEN-3) | Legal privilege, regulator strategy |
| Facilitator | **Claude.** Runs the clock, delivers injects, records decisions |

## 5. Out of scope
- Employee personal data (noted if the scenario surfaces it, not analyzed)
- Paying or negotiating the ransom (noted as a business decision for leadership; not analyzed)
- Technical forensics beyond what the injects reveal
- Laws of states other than Texas, beyond identifying which affected residents live elsewhere

## 6. Review standards
Named here only. Each will be registered with a URL and access date in S2.
- **HIPAA Breach Notification Rule** and related HHS guidance (including guidance on ransomware)
- **HIPAA Security Rule**, for incident response requirements
- **Texas breach-notification law** and **Texas medical-records privacy law**
- **NIST incident-handling guidance** as the process framework
