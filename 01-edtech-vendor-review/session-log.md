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

## S4 — 2026-11-03 — Collect legal and benchmark sources ✅
**Done**
- Registered S16–S23: FERPA regulations (eCFR), the COPPA Rule (eCFR), the FTC's 2025 COPPA amendments (90 FR 16918, effective 2025-06-23), the FTC COPPA FAQ §N (schools), Tex. Educ. Code Ch. 32 Subch. D (codified URL plus enacted HB 2087), ED/PTAC 2014 online-services guidance, and the SDPC NDPA v2.2. TX-NDPA v1r6 text = S12.
- Saved snapshots for public-domain government texts. The copyrighted NDPA (S23) is registered by URL and fingerprint only.
- Filled in the study-note citations for COPPA (child under 13, school consent via FTC guidance) and FERPA (school-official exception, three conditions). Added a note on regulation vs. guidance.

**Worth noting for later sessions**
- The COPPA amendments took effect 2025-06-23, twelve days after the Quizizz e-signature on S12 (06/11/2025).
- The NDPA v2.2 benchmark contains no AI-specific terms.
- TX-NDPA v1r6 and the national NDPA v2.2 are different versions.

**Next step (S5):** Draft the requirements matrix: about 12 review domains (e.g., data collection and minimization, use limits, advertising and profiling, AI and model training, subprocessors, security, breach notice, retention and deletion, parent and student rights, COPPA consent, school-official/direct control, legacy agreement coverage). Each requirement cites S16–S23.

**Open questions for Brittany**
- ~~Texas statute history~~ **Resolved 2026-11-03:** Brittany checked the official site. §§32.151–.157 have no amendments since H.B. 2087 (2017), including none from 2025. Cite as: Tex. Educ. Code §§32.151–.157 [S20], text as enacted [S21].
- Retry the Internet Archive snapshot of the FTC FAQ (S19) later. It was rate-limited today.
- Still open: repo license; check the keychain for CJ's GitHub login before the first push.

## S5 — 2026-11-03 — Requirements matrix (draft) ✅
**Done**
- Drafted `working/requirements-matrix.md`: 12 domains and 42 requirements, each citing a specific clause (FERPA, COPPA, Tex. Educ. Code §§32.151–.156, FTC FAQ §N, NDPA v2.2) and labeled by basis type (Law / Guidance / Contract benchmark / Derived).
- Verified from S18: COPPA amendments effective 2025-06-23, **compliance date 2026-04-22**. The FTC did **not** finalize the ed-tech/school-authorization provisions and continues to rely on existing guidance.
- Read each cited clause in the source text before citing it. S12 (scanned) references are marked "as viewed," with exhibit headings to confirm in S8.

**Next step (S6):** Design the questionnaire and scoring rubric: turn each requirement into a question, define the score levels (e.g., Addressed / Partially / Not addressed / Not found in public documentation), and decide weighting. Brittany approves the rubric.

**Open questions for Brittany** (see the end of the matrix)
- Domain count and merges; framing of D6 (AI) as "Derived"; whether to add Texas breach-notice law (Bus. & Com. Code §521.053); confirm PPRA stays out of scope.
- Still open: retry the FTC FAQ snapshot; repo license; check the keychain for CJ's GitHub login before the first push.

## S6 — 2026-11-03 — Questionnaire and rubric design ✅
**Done**
- Recorded the S5 scope decisions in the matrix: 12 domains confirmed; D6 (AI) labeled Derived; Texas general breach law and PPRA out of scope (D8.3 removed, leaving **41 requirements**).
- Drafted `working/questionnaire-rubric.md`: 41 questions, one per requirement, answered from public documents only. It also defines the answer columns for the .xlsx.
- **Rubric approved by Brittany:** 5 score levels (A 2 / P 1 / D 1 / NF 0 / N/A excluded); weights by basis type (Law 3; Guidance, Benchmark, and Derived 2; definition and district-duty items 1); domain percentages only, with no overall grade. Score ≠ risk rating (S10).

**Next step (S7):** Write `tools/build_questionnaire.py` (openpyxl) to build `deliverables/1-vendor-questionnaire.xlsx` from the matrix and the rubric. Sheets: Instructions, Questionnaire (41 rows, score dropdown, point formulas), Domain Scores (formulas), Rubric, Sources. Blank answers.

**Open questions for Brittany**
- None new. Still open: retry the FTC FAQ snapshot; repo license; check the keychain for CJ's GitHub login before the first push.

## S7 — 2026-11-03 — Build the questionnaire .xlsx ✅
**Done**
- Wrote `tools/build_questionnaire.py`. It reads the matrix, the rubric, and the source register (Markdown is the single source of truth) and builds `deliverables/1-vendor-questionnaire.xlsx`.
  - Sheets: Instructions (with disclaimer), Questionnaire (41 rows; Score and Score-status dropdowns; point formulas; yellow answer columns), Domain Scores (formulas; % per domain; no overall score), Rubric, Sources (24).
  - The build fails with a clear message if a requirement has no question or a basis type has no weight.
  - Rebuilding keeps any answers already entered (matched by question ID).
- **Verified:** filled a scratch copy with sample scores and recalculated it in Numbers. Results matched the hand calculation (D1 = 9/16 = 56%; N/A excluded in D2 → 4/6 = 67%; unscored domain shows "not yet scored"). Rebuild carry-over was tested, then the deliverable was rebuilt blank.

**Next step (S8):** Evidence pass, domains D1–D6. For each question: quote or paraphrase what the public documents say, cite source + section, propose a score (PROPOSED), and draft the vendor follow-up. Includes the S14-vs-S01 comparison (Quizizz-era vs. current policy) for AI and legacy coverage, and mapping S12 clause numbers by hand.

**Open questions for Brittany**
- None new. Still open: retry the FTC FAQ snapshot; repo license; check the keychain for CJ's GitHub login before the first push.

## S8 — 2026-11-03 — Evidence pass, D1–D6 ✅ (scores PROPOSED)
**Done**
- Read the full current policy (S01) and compared key sentences with the Quizizz-era policy (S14). Read the AI pages (S10, S11), the subprocessor list (S05), the agreements page (S06), the rebrand article (S08), and the terms (S02). Mapped the scanned TX-NDPA (S12) clauses by hand.
- Added **S25**: the vendor's DBA letter dated 2025-06-05, linked from S08.
- Wrote `working/evidence-notes.md`: 22 evidence rows (D1.1–D6.5), key observations, and an S12 clause map. All scores are **PROPOSED**.
- Updated `tools/build_questionnaire.py` to load evidence-notes.md (Markdown wins over the workbook) and validate scores. Rebuilt the .xlsx.

**Key observations (facts only)**
1. The S01 §5.2 AI text matches S14 (effective 2024-12-10). New since then: the ISO 27001 and SOC 2 Type II references.
2. AI provider names differ across S01, S05, S10, and S11 (OpenAI/Anthropic; Portkey/Azure/GCP/AWS; GPT-5; Pangram).
3. S01 says no personal data goes to AI platforms. S10 says the AI extension reads rosters and student submissions (deleted within 72 hours). The documents don't reconcile these.
4. S12 Exhibit A (products covered) is blank or illegible in the public scan. Exhibit B as executed doesn't check "Student work" or "Student Name."

**Proposed domain scores (if all PROPOSED scores are accepted):** D1 100%, D2 83%, D3 69%, D4 91%, D5 65%, D6 70%.

**Next step (S9):** Evidence pass D7–D12 (S12 Art. V, Exhibits F–G; breach, retention, rights, COPPA consent, agreements/legacy). Then Brittany confirms or changes all scores.

**Open questions for Brittany**
- ~~Scoring frame~~ **Decided:** include the TX-NDPA terms available via Exhibit E. Record "Policy only" in Notes.
- ~~D6.2~~ **Decided:** P.
- Review the 22 PROPOSED scores (in `working/evidence-notes.md` or the .xlsx).
- Still open: retry the FTC FAQ snapshot; repo license; check the keychain for CJ's GitHub login before the first push.

## S9 — 2026-11-03 — Evidence pass, D7–D12 ✅ (scores PROPOSED)
**Done**
- Read the remaining TX-NDPA (S12) pages: Art. V (security, audits, 72-hour breach notice), Art. VI–VII (general offer, termination, priority of agreements, successors), Exhibit E (general offer and withdrawal terms), and the Texas addendum (p. 21–22). Clause map extended.
- Added 19 evidence rows (D7.1–D12.4) and observations 7–9 to `working/evidence-notes.md`. **All 41 questions now have evidence.** Rebuilt the .xlsx.
- Verified domain scores by recalculating the workbook in Numbers.

**Proposed domain scores (all PROPOSED):** D1 100% · D2 83% · D3 69% · D4 91% · D5 65% · D6 70% · D7 81% · D8 100% · D9 69% · D10 100% · D11 65% · D12 75%.

**New observations (facts only)**
- Exhibit E lets the provider withdraw the offer on a "material change in the services and products" or three years after signing (06/11/2025). A subscribing district is bound for the term of the originating DPA, which isn't visible.
- The Texas addendum extends DPA protections to "all data provided to or collected by the Provider."
- No written retention policy for children's data with deletion timeframes found (COPPA §312.10 compliance date 2026-04-22). TX-NDPA v1r6 gives no post-termination deadline.
- Many protections exist **only** in the TX-NDPA (breach 72 hours and reimbursement, 60-day deletion on request, DPA priority, 45-day access support). Policy-only results are recorded in Notes.

**Next step (S10):** Brittany confirms or changes the 41 scores. Then draft the risk assessment and findings table (`deliverables/2-risk-assessment.md`): select findings from P/D/NF items, write requirement / what the docs say / gap / recommendation, and Brittany assigns risk ratings.

**Open questions for Brittany**
- ~~D12.4~~ **Decided: D.**
- ~~Score review~~ **All 41 scores confirmed by Brittany (2026-11-03).**
- Still open: retry the FTC FAQ snapshot; repo license; check the keychain for CJ's GitHub login before the first push.

## S10 — 2026-11-03 — Risk assessment and findings table ✅
**Done**
- Recorded Brittany's decisions from the end of S9: D12.4 = D; all 41 questionnaire scores confirmed. Deliverable 1 is complete.
- Drafted `deliverables/2-risk-assessment.md`: summary, method, a 9-finding table, and finding details (requirement / what the docs say / gap / recommendation), all cited and in neutral wording (checked for "violates," "fails," "illegal").
- **Brittany approved** the 3×3 likelihood × impact method and assigned the ratings: **High** for F1 (AI data flows), F2 (TX-NDPA coverage of AI features), F3 (protections only in the DPA; teacher self-sign-up), and F4 (COPPA consent model). **Medium** for F5 (provider lists), F6 (retention), and F7 (material changes). **Low** for F8 (develop new services) and F9 (security program elements).
- Study note added: risk = likelihood × impact; score ≠ risk.

**Next step (S11):** Write the 2-page memo to the District Privacy Officer (`deliverables/3-privacy-officer-memo.md`): summary, top risks (F1–F4), contract terms to require, and a recommendation. **Brittany decides approve / conditionally approve / reject.** Export to PDF and check it is 2 pages.

**Open questions for Brittany**
- The recommendation decision (S11).
- Still open: retry the FTC FAQ snapshot; repo license; check the keychain for CJ's GitHub login before the first push.

## S11 — 2026-11-03 — 2-page memo ✅
**Done**
- **Brittany's decision: CONDITIONAL APPROVAL, PHASED.** Core features are approved after the Phase 1 conditions (sign TX-NDPA via Exhibit E unaltered; updated Exhibit A incl. AI; district-level control; COPPA consent approach; disposal deadline). AI features using student work or names are held until Phase 2 conditions are met (AI data-flow description; complete subprocessor list; DPA prevails over policy changes).
- Wrote `deliverables/3-privacy-officer-memo.md`: recommendation and rationale, summary, top risks F1–F4, eight conditions mapped to findings, and next steps. Neutral wording checked.
- PDF export `deliverables/pdf/3-privacy-officer-memo.pdf` = **2 pages** (verified visually). First draft was 3 pages; fixed by tightening the text and setting table column widths (pandoc sizes columns from the separator-row dashes).

**Next step (S12):** Polish and publish prep: audit every vendor/legal claim in the deliverables against the register (source ID + section); check disclaimers on every deliverable; export the risk assessment PDF; update the project README and the portfolio landing page; write the README "how to read this project" guide; final review by Brittany. Decide the license and GitHub account; check the keychain for CJ's login. **Push only with Brittany's OK.**

**Open questions for Brittany**
- License (CC BY 4.0 suggested); GitHub repo name and visibility; retry the FTC FAQ snapshot (S19).

## S12 — 2026-11-03 — Citation audit, polish, publish prep ✅ (publish pending Brittany's OK)
**Done**
- **Citation audit:** every source ID used in the deliverables exists in the register. Of 199 quoted phrases, 156 match the snapshot text exactly, 31 are from the scanned TX-NDPA (S12; transcribed from page images), and 12 flagged items were checked by hand (S12 quotes, one label, one nested-quote style). Result: no unsupported quotations.
- **Disclaimers:** present in every Markdown file in the project and in the .xlsx Instructions sheet.
- **PDFs:** risk assessment exported (7 pages; findings-table column widths fixed). Memo PDF is 2 pages (S11).
- **READMEs:** project README rewritten as a "start here" guide (findings, method, ground rules, AI-assistance disclosure, session plan). Landing page updated: Project 01 Complete; "Skills demonstrated" filled in.
- **Pre-publish privacy scan:** no signatory names, emails, or IPs from S12; no CJ email; no employer references in tracked files or the .xlsx. Git history author = noreply address only.
- **Keychain check:** the saved github.com credential is account ID 285196955 = Brittany (greebrit32-lgtm), not CJ. `gh` is logged in as greebrit32-lgtm.

**Open questions for Brittany**
- ~~F1 likelihood~~ **Decided: High** (rating unchanged: High).
- ~~License / repo / push~~ **Decided:** CC BY 4.0; public repo `greebrit32-lgtm/privacy-portfolio`; Brittany approved creating it and pushing (2026-11-03).
- Retry the FTC FAQ snapshot (S19) later. Optional.
