# Participant Briefing — "Friday Night Lights Out"

> _Fictional organization, people, and data. Independent educational exercise. Not legal advice._

## Starting situation (what everyone knows at the start)

**Friday, January 15, 2027, 9:40 p.m.** A medical assistant finishing late charting at the clinic's main site can't open files on the shared drive. Every file now ends in an unfamiliar extension. A text file appears on the desktop of several workstations:

> *"Your network has been encrypted. We have downloaded your patients' files. If you do not contact us within 72 hours, your data will be published on our site."*

The medical assistant calls the IT Manager's cell phone at **9:52 p.m.** The IT Manager, now acting as **Incident Commander**, calls you, the Privacy Lead, at **10:05 p.m.** Clinic hours resume **Monday at 8:00 a.m.**, and the schedule has about 140 appointments.

## What each role knows at the start

| Role | Knows | Doesn't know yet |
|-------------------------|------------------------------------------------------|----------------------|
| Incident Commander (IT Manager) | Files on the shared drive (SYS-2) and at least some workstations (SYS-3) are encrypted. The ransom note claims data was downloaded | How the attackers got in; which systems are affected; whether data was really taken; whether backups are usable |
| Privacy Lead (you) | Everything in this briefing, the [playbook](../1-incident-response-playbook.md), and the [matrix](../2-notification-matrix.md) | Everything else |
| Practice Administrator / Privacy Officer | Has been told only "IT problem at the main site." Not yet briefed on the note | — |
| Medical Director | Not yet contacted | — |
| MSP incident lead | Not yet contacted. The MSP manages backups and has remote access to the server | — |
| Cyber insurer / breach coach | Not yet contacted | — |

## Reference facts (from the clinic's scenario)
- **About 18,000 active patients, including minors.** Nearly all are Texas residents; a small number live in neighboring states.
- **The shared drive (SYS-2) holds:** scanned intake forms (older ones include Social Security numbers), referral letters, lab result PDFs, billing exports, and staff spreadsheets.
- **The cloud EHR (SYS-1)** is run by a vendor (a business associate). Its status is not yet known.
- **Backups (SYS-5)** are run by the MSP. Isolation is **not documented**.
- **Business associates:** the MSP (VEN-1) and the billing company (VEN-2). **Cyber insurance** with a 24/7 hotline (VEN-3).

## Your first decision
When the exercise begins, the facilitator will ask what you do in the first hour. You may ask any role questions first.
