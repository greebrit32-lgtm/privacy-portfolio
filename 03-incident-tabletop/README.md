# Project 03 — Incident Response Tabletop

**Scenario (chosen 2026-11-03):** A **fictional** Texas health clinic has a privacy incident (e.g., ransomware or misdirected records). As the clinic's privacy analyst, I prepare the incident response playbook, work out who must be notified and by when, design a tabletop exercise, **run it live** (Claude facilitates and delivers injects; I make the decisions), and write the breach analysis, draft notices, and after-action report. The clinic, its patients, and all data are invented. The profile is drafted in S1 (`scenario.md`).

**Measured against (named only; sourced in S2):** the HIPAA Breach Notification Rule and related HHS guidance, Texas breach-notification and medical-records privacy law, and NIST incident-handling guidance as the process framework.

**Status:** Planned. Plan approved 2026-11-03. Not started.

## Deliverables
1. `deliverables/1-incident-response-playbook.md`: roles, severity levels, response phases, and a breach-notification decision tree
2. `deliverables/2-notification-matrix.md` (and .xlsx if useful): for each law, the trigger, deadline, recipients, and required content
3. `deliverables/3-tabletop-package/`: scenario story, timed injects, facilitator guide, participant materials
4. `deliverables/4-exercise-record-and-breach-analysis.md`: decisions made during the live exercise, plus the formal breach risk assessment and notification decision
5. `deliverables/5-notification-drafts/`: draft notices to individuals and regulators, with the required content elements
6. `deliverables/6-after-action-report.md`: what went well, gaps, and an improvement plan

## Session plan
| # | Session | Time | Stopping point |
|---|---------|------|----------------|
| S1 | Scenario and fictional organization | 30m | `scenario.md` committed |
| S2 | Legal and framework sources | 45–60m | Sources registered; statute currency checked |
| S3 | Incident response playbook | 60m | Playbook drafted |
| S4 | Notification requirements matrix | 45–60m | Matrix complete |
| S5 | Tabletop design: story, timeline, injects | 45m | Injects drafted |
| S6 | Facilitator guide and participant materials | 45m | Package ready |
| S7 | **Run the tabletop live** (Brittany decides) | 60m | Exercise record captured |
| S8 | Breach risk assessment and notification decision | 45m | Decision documented |
| S9 | Notification letter drafts | 45m | Drafts complete |
| S10 | After-action report and improvement plan | 45m | AAR final |
| S11 | Citation audit, polish, publish | 45m | Project 03 published |

## Carried over from Projects 01–02
Same working rules (see the repo's `CLAUDE.md`): fictional organization and data (patients described by **type** only; any example is obviously synthetic, e.g., "Patient A"), every legal claim cited to a source ID and section, statute currency checked on official sites, neutral wording, and Brittany makes the judgment calls. Reused: the source register format, `tools/export_pdf.sh`, `tools/fit_tables.py`, and the 3×3 risk method where useful.

_Disclaimer: independent educational exercise. Fictional organization and data. Not legal advice._
