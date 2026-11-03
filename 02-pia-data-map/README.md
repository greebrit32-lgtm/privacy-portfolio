# Project 02 — Privacy Impact Assessment & Data Map

**Scenario (chosen 2026-11-03):** A **fictional** Texas company is launching a consumer mobile app that uses location data and ad targeting. Acting as the company's privacy analyst, I map the app's personal data and assess its privacy risks **before launch**. The company, app, and all data are invented. The profile is drafted in S1 (`scenario.md`).

**Measured against (named only; sourced in S2):** the Texas Data Privacy and Security Act, Section 5 of the FTC Act (unfair or deceptive practices) and related FTC guidance, and the Fair Information Practice Principles (FIPPs). The report is structured on the Texas data protection assessment elements (§541.105(b)), with the nine FIPPs as the risk lens.

**Status:** Planned. Plan approved 2026-11-03. Not started.

## Deliverables
1. `deliverables/1-data-inventory.xlsx`: every personal-data element with source, purpose, legal basis, system, recipients, retention, and sensitivity (generated from Markdown, as in Project 01)
2. `deliverables/2-data-flow-map.md`: data-flow diagram in Mermaid (renders on GitHub), plus a PDF
3. `deliverables/3-pia-report.md`: system description, risks against FIPPs and the law, mitigations, residual risk ratings, and sign-off recommendation
4. `deliverables/4-executive-summary.md`: one page for the decision-maker

## Session plan
| # | Session | Time | Stopping point |
|---|---------|------|----------------|
| S1 | Scenario and fictional organization profile | 30m | `scenario.md` committed |
| S2 | Legal and framework sources | 45–60m | Sources registered |
| S3 | System description: features, users, data collection points | 45m | System description drafted |
| S4 | Data inventory part 1: .xlsx generator (reuses the Project 01 pattern) | 45m | Blank inventory committed |
| S5 | Data inventory part 2: fill in | 60m | Inventory complete |
| S6 | Data-flow map (Mermaid) | 45m | Diagram renders on GitHub |
| S7 | Risk identification against FIPPs and the law | 60m | Risk list drafted |
| S8 | Risk ratings and mitigations (Brittany rates; 3×3 method) | 45m | Ratings decided |
| S9 | PIA report draft | 60m | Report drafted |
| S10 | Executive summary and PDF exports | 45m | Summary final, 1 page |
| S11 | Citation audit, polish, publish | 45m | Project 02 published |

## Carried over from Project 01
Same working rules (see the repo's `CLAUDE.md`): fictional data only, every legal claim cited to a source ID and section, neutral wording, and Brittany makes the judgment calls. Reused: the source register format, `tools/export_pdf.sh`, the 3×3 likelihood × impact method, and the build-from-Markdown approach.

_Disclaimer: independent educational exercise. Fictional organization and data. Not legal advice._
