# Questionnaire and Scoring Rubric — Design

**Status:** APPROVED by Brittany, 2026-11-03 (S6). Once approved, `tools/build_questionnaire.py` builds this into `deliverables/1-vendor-questionnaire.xlsx` (S7).

_Disclaimer: independent educational exercise, based only on public documents. Not legal advice. Not affiliated with or endorsed by Wayground._

## How the questionnaire works

A real vendor questionnaire is usually sent to the vendor to fill out. In this project **the vendor never answers it**. The analyst answers each question from the vendor's **public documents only**, and cites the source ID and section for every answer. When the documents are silent, the answer is **"Not found in public documentation."** That is a finding about the documents, not about the vendor's actual practices. A district would then send those items to the vendor as follow-up questions.

Each question maps to one requirement in [`requirements-matrix.md`](requirements-matrix.md) (same ID).

## Score levels (approved)

| Code | Level | Meaning | Points |
|------|-------|---------|--------|
| **A** | Addressed | The documents explicitly cover every element of the requirement in terms consistent with it. | 2 |
| **P** | Partially addressed | The documents cover some elements, or use qualified or general language (e.g., "may," "reasonable," no timeframe). | 1 |
| **D** | Addressed differently | The documents speak to the topic but state something different from the requirement (e.g., a 90-day deletion window against a 60-day requirement). | 1 |
| **NF** | Not found in public documentation | No public document in the source register addresses it. | 0 |
| **N/A** | Not applicable | The requirement doesn't apply given the scenario (e.g., a feature the district will not use). The reason must be stated. | excluded |

Why "D" is separate from "P": "partially" means some elements are missing. "Differently" means the vendor made a clear statement that doesn't match the requirement. They lead to different follow-ups. P calls for a clarifying question, and D calls for a contract term. Both earn 1 point. The difference shows in the label, not the number.

## Weighting (approved)

Weight is set by **basis type** from the matrix, so a gap relative to law counts more than a gap relative to a model contract:

| Basis type | Weight |
|------------|--------|
| Law | 3 |
| Guidance | 2 |
| Contract benchmark | 2 |
| Law + benchmark | 3 |
| Benchmark + law | 3 |
| Law (definition) | 1 |
| Law (district duty) | 1 (the duty falls on the district, so vendor documents only support it) |
| Law (COPPA scope) | 3 |
| Derived | 2 |

**Domain score** = points earned ÷ points possible (weighted), shown as a percentage.
**No single overall grade** is proposed, because one number hides where the gaps are. The memo reports domain scores and the top findings.

**The score is not the risk rating.** The score measures how fully the documents cover each requirement. The risk rating (S10) weighs likelihood and impact for the district, and Brittany assigns it. A low-scoring item can be low risk, and a single NF item can be high risk.

## Answer columns (for the .xlsx)

| Column | Filled in | Content |
|--------|-----------|---------|
| ID | S7 | D1.1 … D12.4 |
| Domain | S7 | |
| Question | S7 | From the list below |
| Basis / citation | S7 | From the matrix |
| Basis type, Weight | S7 | |
| What the public documents say | S8–S9 | Short quote or paraphrase |
| Source ID + section | S8–S9 | e.g., "S01 §4" |
| Score (A/P/D/NF/N/A) | S8–S9 | PROPOSED until Brittany confirms |
| Points, Weighted points | auto | Formula |
| Follow-up question for vendor | S8–S9 | What a district would ask |
| Notes | any | e.g., S14 vs. S01 change |

## Questions (41)

### D1. Applicability and roles
- **D1.1** Do the documents describe the vendor acting on the school's behalf under the school's control of student records (e.g., as a "school official" under FERPA), and do they commit to FERPA redisclosure limits?
- **D1.2** Do the documents describe the service as designed and marketed for K–12 school use (Texas "operator")?
- **D1.3** Do the documents identify the legal entity, the products covered, and the products excluded?

### D2. Data collection and minimization
- **D2.1** Do the documents state that children are not required to provide more personal information than reasonably necessary to take part?
- **D2.2** Do the documents list the categories of student data collected (a data schedule)?
- **D2.3** Which Texas "covered information" categories do the documents say are collected (identifiers, voice, location, search activity, etc.)?

### D3. Use limitations
- **D3.1** Do the documents limit the use of student data to providing the service, or to what the school instructs?
- **D3.2** Do the documents limit uses of student data to school purposes, and how do they describe use for "improving" the service?
- **D3.3** Do the documents prohibit redisclosure of student data except as permitted?

### D4. Advertising, profiling, and sale
- **D4.1** Do the documents prohibit targeted advertising to students based on data from school use?
- **D4.2** Do the documents prohibit building student profiles except for a school purpose?
- **D4.3** Do the documents prohibit selling or renting student data, and address what happens in a merger or acquisition?
- **D4.4** Where the school provides COPPA consent, do the documents limit use to the school's benefit with no other commercial purpose?

### D5. Subprocessors and third-party disclosure
- **D5.1** Do the documents state that third parties receiving student data are contractually limited to providing the service and must protect the data?
- **D5.2** Do the documents state that the vendor obtains written security assurances from service providers that handle children's data?
- **D5.3** Do the documents state that subprocessor agreements are at least as protective as the vendor's own commitments, and prohibit sale?
- **D5.4** Is there a current public subprocessor list showing which providers process student data, and do the policy's links to it work?

### D6. AI features, model training, and de-identified data
- **D6.1** Do the documents identify the AI features and say whether students, teachers, or both use them?
- **D6.2** Do the documents say whether student data is sent to AI providers, and name them?
- **D6.3** Do the documents say whether student data is used to train or improve AI models, and whether that data is identifiable or de-identified?
- **D6.4** Do the documents prohibit re-identifying de-identified data and limit its transfer?
- **D6.5** Do the documents say whether AI providers are bound by the same terms (no training on school data, no retention beyond the service)?

### D7. Security program
- **D7.1** Do the documents describe reasonable security practices for student data?
- **D7.2** Do the documents describe a written information security program, with a coordinator, annual risk assessments, and safeguards?
- **D7.3** Do the documents name a recognized security framework or certification, and describe audits?

### D8. Breach notification
- **D8.1** Do the documents commit to notifying the school within a stated time after a breach (benchmark: 72 hours), with stated content?
- **D8.2** Do the documents address reimbursement of the school's breach-related costs?

### D9. Retention and deletion
- **D9.1** Do the documents include a written retention policy for children's data that states purposes, business need, and a deletion timeframe?
- **D9.2** Do the documents commit to deleting student data within 60 days of a district request?
- **D9.3** Do the documents commit to disposing of student data within 60 days of termination?

### D10. Parent and student rights
- **D10.1** Do the documents explain how parents can access student records, including routing requests through the school?
- **D10.2** Do the documents let parents review, stop further use of, and delete their child's information?
- **D10.3** Do the documents commit the vendor to helping the school respond to access requests?

### D11. COPPA consent model
- **D11.1** Do the documents explain how verifiable parental consent is obtained, including for material changes?
- **D11.2** Do the documents offer separate consent for disclosure to third parties where it is not integral to the service?
- **D11.3** If the vendor relies on school authorization, do the documents limit it to educational use, give the school notice, and let the school review and delete?
- **D11.4** Do the documents direct schools or districts, rather than individual teachers, to make the consent decision?

### D12. Agreements, change, and legacy coverage
- **D12.1** Do the documents say that a signed DPA takes priority over the terms of service?
- **D12.2** Do the documents say agreements bind successors, with notice to schools if control changes?
- **D12.3** Do the documents say whether agreements signed under the Quizizz name cover current services, including AI features and later policy changes?
- **D12.4** Do the documents explain how schools are notified of material policy changes?

## Decisions (Brittany, 2026-11-03)
1. **Score levels:** 5 levels approved: A (2) / P (1) / D (1) / NF (0) / N/A (excluded).
2. **Weighting:** by basis type, as in the table above.
3. **Reporting:** domain percentages only. No overall score.

Individual question scores entered in S8–S9 remain **PROPOSED** until Brittany confirms them.
