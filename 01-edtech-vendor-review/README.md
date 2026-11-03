# Project 01 — EdTech Vendor Privacy Review: Wayground (formerly Quizizz)

**Scenario:** I'm a privacy analyst at a fictional Texas school district, Pecan Hollow ISD (PK–12, about 12,000 students; see [scenario.md](scenario.md)). Teachers want to use Wayground, a classroom quiz, lesson, and AI platform, district-wide. Before that can happen, the district needs a privacy review. I reviewed Wayground using **only its public documents**.

**Measured against:** FERPA (including the school-official exception), COPPA (including the 2025 rule amendments), Texas Education Code §§32.151–.157, FTC and Department of Education guidance, and the Student Data Privacy Consortium (SDPC) National Data Privacy Agreement.

**Status:** Complete (November 2026). The recommendation is **conditional approval, phased**.

## Start here

| If you have… | Read |
|---|---|
| 2 minutes | [**Memo to the District Privacy Officer**](deliverables/3-privacy-officer-memo.md) (2 pages; [PDF](deliverables/pdf/3-privacy-officer-memo.pdf)) |
| 10 minutes | [**Risk assessment**](deliverables/2-risk-assessment.md): 9 findings with risk ratings ([PDF](deliverables/pdf/2-risk-assessment.pdf)) |
| The full picture | [**Vendor questionnaire (.xlsx)**](deliverables/1-vendor-questionnaire.xlsx): 41 questions, each answered from public documents with source, score, and vendor follow-up |

## What I found

- **Most protections come from the contract, not the privacy policy.** Wayground offers Texas districts a signed state data privacy agreement (TX-NDPA). It provides FERPA school-official status, 72-hour breach notice, breach-cost reimbursement, and 60-day deletion. The privacy policy alone does not.
- **The AI question.** The policy's AI section is unchanged from the pre-rebrand (Quizizz) version. It says no personal data goes to AI platforms, while Wayground's AI deployment guide describes an extension that reads student names and submissions for grading.
- **The legacy question.** The Texas agreement was signed as "Quizizz" in June 2025, before the AI launch, and its list of covered products is illegible in the public copy. Whether it covers the newer AI features is not found in public documentation.

## How the work was done

1. **Sources** ([register](sources/source-register.md)): 25 sources, each with URL, version date, and access date, plus dated text snapshots and fingerprints. That includes archived Quizizz-era policies from the Internet Archive and the signed Texas agreement from the SDPC registry.
2. **Requirements** ([matrix](working/requirements-matrix.md)): 41 requirements in 12 domains. Each one is labeled **Law**, **Guidance**, **Contract benchmark**, or **Derived**, so legal requirements aren't confused with contract norms.
3. **Rubric** ([design](working/questionnaire-rubric.md)): five score levels, weighted by how binding the requirement is. Scores are reported per domain only, with no single overall grade.
4. **Evidence** ([notes](working/evidence-notes.md)): a quote or paraphrase, source, and section for every answer, plus the result if only the privacy policy is considered.
5. **Risk** ([assessment](deliverables/2-risk-assessment.md)): findings grouped from the gaps and rated by likelihood × impact. **Scores and risk ratings are separate.** A domain can score 100% and still carry a High risk.
6. **Recommendation** ([memo](deliverables/3-privacy-officer-memo.md)): conditions mapped to each finding.

The spreadsheet is generated from the Markdown files by [`tools/build_questionnaire.py`](../tools/build_questionnaire.py), so the questions, evidence, and scores live in one place.

## Ground rules I followed

- **Public information and fictional data only.** No real student or district data. The district is fictional, and I checked its name against Texas district lists.
- **Every factual claim is cited** to a source ID and section. Where the documents are silent, the answer reads "Not found in public documentation." I didn't infer.
- **Neutral wording.** Findings describe what the documents say or don't say. They are not conclusions about the vendor's practices or legal compliance.
- **Privacy in my own work.** The signed agreement contains signatories' names, emails, and IP addresses, so I cited it by link and fingerprint instead of republishing it. Copyrighted model contracts are handled the same way.
- **Division of labor.** An AI assistant (Claude) helped collect sources and draft. I made the judgment calls: scope, every score, every risk rating, and the final recommendation. The [session log](session-log.md) records each decision.

## How it was scheduled

Twelve sessions of 30–60 minutes. Each one had one goal and ended with a commit and a [log entry](session-log.md).

| # | Session | # | Session |
|---|---------|---|---------|
| S1 | Repo scaffold and tooling | S7 | Build the .xlsx |
| S2 | Fictional district and scope | S8 | Evidence pass, domains 1–6 |
| S3 | Collect vendor documents | S9 | Evidence pass, domains 7–12, and scoring |
| S4 | Collect legal and benchmark sources | S10 | Risk assessment and findings |
| S5 | Requirements matrix | S11 | 2-page memo |
| S6 | Questionnaire and rubric design | S12 | Citation audit, polish, publish |

## Project files

| Folder | Contents |
|--------|----------|
| [`deliverables/`](deliverables/) | Questionnaire (.xlsx), risk assessment, memo, and PDFs |
| [`working/`](working/) | Requirements matrix, rubric, and evidence notes |
| [`sources/`](sources/) | Source register and dated snapshots |
| [`scenario.md`](scenario.md) | Fictional district profile and scope |
| [`study-notes.md`](study-notes.md) | CIPP/US concepts that came up, tagged by topic |
| [`session-log.md`](session-log.md) | Session-by-session log: done, next step, decisions |

_Disclaimer: independent educational exercise, based only on public documents. Not legal advice. Not affiliated with or endorsed by Wayground. Pecan Hollow ISD is fictional._
