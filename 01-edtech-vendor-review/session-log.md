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

## S3 — 2026-11-03 — Collect vendor documents ✅
**Done**
- Registered 11 vendor documents (S01–S11), 1 signed agreement from the SDPC registry (S12), and 1 secondary trade-press source (S13). Dated text snapshots and SHA-256 fingerprints are in `sources/snapshots/2026-11-03/`.
- S12 (the Texas TX-NDPA signed with "Quizizz") is **not stored in the repo** because it contains signatories' personal data. It is registered by URL and fingerprint.

**Early observations to analyze in S8–S9 (facts only, no ratings yet)**
- Legacy question: S08 says "Data privacy and legal agreements remain in place. Quizizz Inc. is still the legal entity." S06 says Wayground "has signed off on the Texas Student Data Privacy Agreement" and links to S12, a TX-NDPA v1r6 with the provider named "Quizizz." The provider e-signature log is dated 06/11/2025, before the rebrand reported for 06/24/2025 (S13, secondary).
- AI question: S05 has a separate "AI service providers" table (Portkey, Microsoft Azure, Google Cloud, AWS). S01 mentions AI and LLMs. S10 describes the Wayground AI Chrome extension as teacher-only.
- S01 still links to `support.quizizz.com` URLs. One of them redirects to the Help Center home page instead of the subprocessor article.

**Addendum (same day):** Brittany decided to include the archived Quizizz-era versions. Added S14 (Quizizz Privacy Policy, effective 2024-12-10, captured 2025-06-03) and S15 (Quizizz Terms, updated 2024-03-01, captured 2025-05-30), which were the versions live when S12 was signed. Both already mention "Quizizz AI." S8 will compare S14 with S01 to see what changed about AI and student data after the rebrand.

**Next step (S4):** Collect the legal and benchmark sources: FERPA (34 CFR Part 99, esp. §99.31(a)(1)), COPPA Rule (16 CFR Part 312) and FTC guidance on schools, TEC Ch. 32 Subch. D, and the SDPC NDPA and TX-NDPA templates (blank, from SDPC/TXSPA). Fill in the study-note citations.

**Open questions for Brittany**
- Still open: repo license; checking the keychain for CJ's GitHub login before the first push.
