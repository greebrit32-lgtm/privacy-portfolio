# Session Log — Project 01

## S1 — 2026-11-02 — Repo scaffold and tooling ✅
**Done**
- Created the repo structure, `CLAUDE.md` working rules, portfolio landing page, project README with the 12-session plan, source register, and study notes template.
- Tooling: `.venv` with openpyxl 3.1.5. pandoc 3.13 installed via Homebrew.
- `tools/export_pdf.sh` (pandoc → HTML → headless Chrome → PDF, with page count). Tested on the project README, and it rendered cleanly.

**Next step (S2):** Draft `scenario.md`, the fictional Texas ISD profile: name, size, grades, ages, the Wayground use case, data shared, and in-scope account types.

**Open questions for Brittany**
- Fictional district name and size (Claude can suggest names checked as not real).
- License for the public repo (CC BY 4.0 suggested), or none.
- Which GitHub account will host the repo (no remote yet; nothing pushed).

## S2 — 2026-11-03 — Fictional district and scope ✅
**Done**
- Chose the fictional district name **Pecan Hollow ISD**. On 2026-11-03 it was checked against Wikipedia's Texas district list and a web search, with no match. Rejected Cedar Prairie (too close to Cedar Hill and Grand Prairie ISDs) and Bluebonnet Ridge (too close to Blue Ridge ISD).
- Drafted `scenario.md`: district profile, the request, users in scope by age, the data the district expects to share, features in scope (including the AI features and legacy Quizizz documents), out of scope, review standards, and roles.
- Added two study-note placeholders (COPPA school authorization; FERPA school-official exception) to fill in with citations in S4.
- Repo housekeeping: the commit email was set to CJ's address from when the computer was set up. Changed it to Brittany's GitHub noreply address and rewrote the S1 commit author. Nothing had been pushed.

**Next step (S3):** Collect the vendor's public documents (privacy policy, terms, student privacy pages, trust/security pages, AI feature pages, and any Quizizz-era documents or signed agreements in public registries). Record each one in `sources/source-register.md` with its URL, last-updated date, and access date, and save a dated snapshot.

**Open questions for Brittany**
- Review `scenario.md`. Are the size and grade span (about 12,000 students, PK–12) OK?
- License for the public repo (CC BY 4.0 suggested), or none. Still open from S1.
- Before the first push (S12): check that the Mac keychain doesn't still hold CJ's GitHub login, so pushes go through `greebrit32-lgtm`.
