# Vendor Privacy Risk Assessment: Wayground (formerly Quizizz)

**Prepared for:** District Privacy Officer, Pecan Hollow ISD (**fictional district**)
**Prepared by:** Brittany Green, Privacy Analyst (portfolio exercise)
**Review date:** 2026-11-03 · **Documents reviewed as of:** 2026-11-03 (source register: [S01–S25](../sources/source-register.md))
**Status:** FINAL. Risk ratings assigned by Brittany Green, 2026-11-03.

> _Independent educational exercise, based only on public documents. Not legal advice. Not affiliated with or endorsed by Wayground. Pecan Hollow ISD is a fictional district._

---

## 1. Summary

Pecan Hollow ISD (PK–12, about 12,000 students) is considering district-wide classroom use of Wayground, including its AI features ([scenario](../scenario.md)). This assessment compares Wayground's public documents against FERPA, COPPA, Texas Education Code §§32.151–.157, FTC and Department of Education guidance, and the SDPC National Data Privacy Agreement (NDPA). Results are recorded in the [questionnaire](1-vendor-questionnaire.xlsx) (41 questions, all scores confirmed).

**Overall picture.** Wayground's public documents address most requirements. The strongest protections, including 72-hour breach notice, breach-cost reimbursement, 60-day deletion on request, school-official status, and the DPA prevailing over the terms of service, come from the **Texas Student Data Privacy Agreement (TX-NDPA v1r6)** that Wayground offers to Texas districts through Exhibit E [S06; S12]. They do not come from the privacy policy. The main open questions concern (1) how the AI features handle student data, and (2) whether that agreement, signed as "Quizizz" in June 2025, covers features added since.

**Domain coverage (weighted; scores confirmed):**

| Domain | Score | Domain | Score |
|--------|-------|--------|-------|
| D1 Applicability and roles | 100% | D7 Security program | 81% |
| D2 Data collection and minimization | 83% | D8 Breach notification | 100% |
| D3 Use limitations | 69% | D9 Retention and deletion | 69% |
| D4 Advertising, profiling, and sale | 91% | D10 Parent and student rights | 100% |
| D5 Subprocessors and third parties | 65% | D11 COPPA consent model | 65% |
| D6 AI features and model training | 70% | D12 Agreements and legacy coverage | 75% |

Scores measure how fully the public documents address each requirement, assuming the district signs the TX-NDPA via Exhibit E. **Scores are not risk ratings.** Risk ratings (Section 3) weigh likelihood and impact for this district.

## 2. Method

- **Evidence:** vendor documents and agreements saved on 2026-11-03 (S01–S15, S25), compared with legal and benchmark sources (S16–S24). The requirements are in the [requirements matrix](../working/requirements-matrix.md), and quotes and citations are in the [evidence notes](../working/evidence-notes.md).
- **Findings** group related questionnaire items scored P (partially addressed) or D (addressed differently). Items scored A where the protection exists **only** in the TX-NDPA are grouped into Finding F3.
- **Risk rating** = likelihood × impact, on a 3 × 3 scale (method approved 2026-11-03):

| | **Impact: Low** | **Impact: Medium** | **Impact: High** |
|---|---|---|---|
| **Likelihood: High** | Medium | High | High |
| **Likelihood: Medium** | Low | Medium | High |
| **Likelihood: Low** | Low | Low | Medium |

  - *Likelihood:* how likely the gap is to affect PHISD student data, given the planned use (district-wide, PK–12, AI features in scope).
  - *Impact:* how serious the effect would be: sensitivity and volume of data, age of students, and whether the district can detect or correct it.
- **Wording:** findings describe what the documents say or do not say. They are not conclusions about the vendor's actual practices or legal compliance.

## 3. Findings table

| ID | Finding | Requirement (basis) | Questionnaire items | Likelihood | Impact | Risk rating |
|---|------------------------------|--------------------------|-------------------|---------|-------|-------|
| F1 | Public documents describe AI handling of student data differently | Use, disclosure, and subprocessor transparency (derived from FERPA §99.33, Tex. Educ. Code §32.153, NDPA §2.3, §4.2) | D6.1, D6.2, D2.2 | Medium–High | High | **High** |
| F2 | TX-NDPA coverage of post-2025 AI features not confirmed | DPA scope and products covered (NDPA §1.2, Exh. A; TX-NDPA Exh. E) | D12.3, D3.1 | Medium | High | **High** |
| F3 | Key protections exist only in the DPA; teachers can start without one | FERPA school-official exception §99.31(a)(1)(i)(B); FTC COPPA FAQ §N.3 | D11.4; policy-only results for D1.1, D3.3, D4.2, D6.4, D8.1, D8.2, D9.2, D10.3, D12.1 | High | High | **High** |
| F4 | COPPA consent model for rostered students under 13 not described | 16 CFR §312.5; FTC COPPA FAQ §N.1–N.2 | D11.1, D11.3, D4.4 | Medium | High | **High** |
| F5 | AI and integrity providers listed differently across documents; subprocessor terms partial | 16 CFR §312.8(c); Tex. Educ. Code §32.153(d); NDPA §2.3 | D5.4, D6.5, D5.3, D5.2 | Medium | Medium | **Medium** |
| F6 | No written retention schedule for children's data; no post-termination deadline | 16 CFR §312.10; NDPA §4.6 | D9.1, D9.3 | High | Medium | **Medium** |
| F7 | Material policy changes use notice plus continued use | 16 CFR §312.5(a)(1) | D12.4 | Medium | Medium | **Medium** |
| F8 | Policy permits use to "develop new services" | NDPA §4.2; Tex. Educ. Code §32.153 | D3.1, D3.2 | Low | Medium | **Low** |
| F9 | Security program elements required by the 2025 COPPA amendments not described | 16 CFR §312.8(b) | D7.2 | Low | Medium | **Low** |

## 4. Findings in detail

### F1. Public documents describe AI handling of student data differently — High
- **Requirement:** The district needs to know what student data its vendors disclose, to whom, and for what purpose, in order to keep FERPA "direct control" and apply Texas §32.153 use limits (requirement D6.2, *derived*).
- **What the documents say:**
  - The privacy policy says Wayground "does NOT use AI platforms or sites for any personal data … and we do not transmit any personal data in connection with those uses," and that AI data is "educational materials produced by our users" [S01 §5.2]. Its Canada section lists "not uploading personal information to our AI providers" [S01 §15.2(e)].
  - The AI deployment guide says the Wayground AI extension reads Google Classroom rosters ("Showing student names") and "student submissions" ("Reading work for grading and feedback"). It says "student submission content" is "deleted within 72 hours of processing" [S10].
  - The product page says the AI will "analyze student responses" [S11].
  - The TX-NDPA data schedule, as executed, does not check "Student work" or "Student Name" [S12 Exh. B pp. 12–14].
- **Gap:** The documents do not explain how these statements relate. For example, they don't say whether submissions are de-identified before AI processing, or which provider processes them.
- **Why it matters:** Student work and names from PK–12 classes would be among the most sensitive data the district shares. The district can't confirm the extension's data flow from the public record.
- **Recommendation:** Before approving AI features for use with student work, require a written description of each AI feature's data inputs, the providers involved, and retention, and attach it to the DPA (Exhibit A/B). Until then, limit use to AI features that don't take student data as input.

### F2. TX-NDPA coverage of post-2025 AI features not confirmed — High
- **Requirement:** A DPA protects the data and services it covers. NDPA §1.2 and Exhibit A list the covered products. The TX-NDPA limits use to the "Services outlined in Exhibit 'A'" [S12 Art. IV §2].
- **What the documents say:**
  - Wayground's Texas offer is a TX-NDPA v1r6 signed by "Quizizz" on 06/11/2025 [S12 p. 3, p. 19]. That is before the rebrand and AI features were announced on 06/24/2025 (secondary source [S13]).
  - Wayground states "any contracts signed with Quizizz Inc. remain valid" [S08]. The DBA letter confirms Quizizz Inc. remains the legal entity [S25].
  - **Exhibit A is blank or illegible in the public copy** [S12 pp. 10–11].
  - The provider "may withdraw the General Offer" upon "a material change in the services and products" or three years after signing [S12 p. 19].
  - The Texas addendum extends protections "to all data provided to or collected by the Provider" [S12 p. 21 ¶1].
  - The policy's AI section is unchanged from the Quizizz-era policy effective 2024-12-10 [S01 §5.2; S14 §5.2].
- **Gap:** Whether the TX-NDPA covers the Wayground AI extension and other features added after June 2025: **Not found in public documentation.**
- **Recommendation:** Before signing Exhibit E, obtain written confirmation that the General Offer is still in effect and covers all current products, and get an updated Exhibit A that names the AI features. Confirm that the Texas addendum's "LEA Data" definition applies to data processed by AI features.

### F3. Key protections exist only in the DPA; teachers can start without one — High
- **Requirement:** For FERPA's school-official exception, the vendor must be under the district's "direct control" [34 CFR §99.31(a)(1)(i)(B)(2)]. FTC guidance recommends the district, not individual teachers, decide on a service's information practices [FTC COPPA FAQ §N.3, S19].
- **What the documents say:**
  - With the TX-NDPA, the district gets school-official status and direct control [S12 Art. I §1; p. 21 ¶3], 72-hour breach notice [Art. V §4], breach-cost reimbursement [p. 22 ¶6], 60-day deletion on request [Art. IV §6], DPA precedence over the ToS and policies [Art. VII §3], and 45-day support for access requests [Art. II §2].
  - Without it, the policy and terms alone don't include those terms. The ToS calls itself "the entire agreement" and doesn't mention DPAs [S02].
  - Teachers "can install [the AI extension] themselves" on a personal device [S10]. Teachers and schools are "requested to get parental consent" for rostered students [S01 §5.6].
- **Gap:** The protections depend on the district signing Exhibit E and controlling who signs up. The public documents describe no district-level control over teacher self-sign-up.
- **Recommendation:** Sign the TX-NDPA via Exhibit E before any classroom use. Until it is in place, add Wayground to the not-yet-approved list and tell teachers not to roster students. Ask the vendor whether it can restrict sign-ups under district domains to the district-approved configuration.

### F4. COPPA consent model for rostered students under 13 not described — High
- **Requirement:** Verifiable parental consent before collecting children's personal information, including consent to material changes [16 CFR §312.5(a)(1)]. A school may consent in a parent's place only for the school's benefit, with direct notice, and with the ability to review and delete [FTC COPPA FAQ §N.1–N.2, S19]. In 2025 the FTC kept relying on this guidance instead of codifying it [S18 at 16918].
- **What the documents say:**
  - "As necessary, Wayground ensures that there is verifiable parental consent" [S01 §2].
  - Teachers and schools "are requested to get parental consent," and a template is provided [S01 §5.6].
  - The terms say that for children under 13 Wayground "does not require Wayground to obtain parental consent" [S02 "Eligibility"].
  - No document states that the vendor relies on school authorization. TX-NDPA v1r6 as viewed has no COPPA school-consent clause.
- **Gap:** The documents don't say which consent model applies when the district rosters PK–5 students, or who is responsible for obtaining consent.
- **Recommendation:** Decide the district's consent approach (district-collected parental consent, or school authorization under FTC guidance) before rollout. Require the vendor to confirm in writing that data from students under 13 is used only for the school's benefit and for no other commercial purpose.

### F5. AI and integrity providers listed differently across documents; subprocessor terms partial — Medium
- **Requirement:** Written assurances from service providers [16 CFR §312.8(c)], contracts limiting third-party use [Tex. Educ. Code §32.153(d)], and subprocessor agreements at least as protective as the DPA, including no sale [NDPA §2.3].
- **What the documents say:**
  - The policy names "OpenAI, Anthropic or others" [S01 §5.2].
  - The subprocessor list's AI table names Portkey, Microsoft Azure, Google Cloud Platform, and AWS, with no "processes student data" column [S05].
  - The product page cites GPT-5 [S11], and the AI guide names Pangram [S10]. Pangram, OpenAI, and Anthropic are not in S05.
  - The policy links to a legacy URL that redirects to the help center home page [S01 §5.1; register notes].
  - "Zero data retention" with AI providers appears in the Canada section [S01 §15.2(d)].
  - Neither the policy nor the TX-NDPA v1r6 states a no-sale term for subprocessors [S01 §5.3; S12 Art. II §5].
- **Gap:** The district can't build a complete list of who receives student data from the public documents.
- **Recommendation:** Require a complete, current subprocessor list, including AI gateway, model, and integrity providers, with whether each processes student data. Require notice of changes, and confirmation that no-training, zero-retention, and no-sale terms apply to each.

### F6. No written retention schedule for children's data; no post-termination deadline — Medium
- **Requirement:** A written retention policy for children's data stating purposes, business need, and a deletion timeframe, included in the online notice [16 CFR §312.10; compliance date 2026-04-22, S18]. Disposal within 60 days of termination [NDPA v2.2 §4.6].
- **What the documents say:**
  - Data is kept "as long as your account is active or as needed." Inactive accounts may be deleted "normally not sooner than one year" [S01 §4].
  - The TX-NDPA requires disposal on termination "after providing the LEA with reasonable prior notice," with no number of days [S12 Art. IV §6].
- **Gap:** No deletion timeframe for children's data is stated in the public documents, and the TX-NDPA v1r6 sets no deadline after termination.
- **Recommendation:** Request the written retention policy. In the DPA (Exhibit D, Directive for Disposition), set a disposal deadline (60 days) at the end of each school year or contract.

### F7. Material policy changes use notice plus continued use — Medium
- **Requirement:** Consent to "any material change in the collection, use, or disclosure practices to which the parent has previously consented" [16 CFR §312.5(a)(1)].
- **What the documents say:** Material changes are announced "by email or other publicly available notice … before the change becomes effective," and "continued use … constitutes your acceptance" [S01 §9; S02]. The TX-NDPA can be amended only "with the signed written consent of both Parties" [S12 Art. VII §4].
- **Gap:** For data covered by COPPA, the documents describe notice, not new consent.
- **Recommendation:** Confirm in the DPA that its terms prevail over later policy changes (TX-NDPA Art. VII §3). Ask how new consent is obtained for material changes affecting students under 13.

### F8. Policy permits use to "develop new services" — Low
- **Requirement:** Use limited to the contracted services [NDPA §4.2; S12 Art. IV §2]. Texas permits use to maintain, develop, support, improve, or diagnose the operator's service [Tex. Educ. Code §32.153(e)].
- **What the documents say:** Data is used to "improve and develop and enhance the services … [and] develop new services" [S01 §7.1]. "Aggregated demographic and activity data may be used for research purposes" [S01 §3.3]. Wayground does "not repurpose student data … without express consent … or all data anonymized" [S01 §7.3].
- **Gap:** The policy doesn't say whether "develop new services" applies to student data. With the TX-NDPA, use is limited to Exhibit A services, but Exhibit A is not legible in the public copy (see F2).
- **Recommendation:** Confirm in the DPA that student data is not used to develop new services except in de-identified form under TX-NDPA Art. IV §5.

### F9. Security program elements required by the 2025 COPPA amendments not described — Low
- **Requirement:** A written information security program with a designated coordinator, at least annual risk assessments, and safeguards [16 CFR §312.8(b); compliance date 2026-04-22].
- **What the documents say:** The policy describes a "comprehensive security program" [S01 §12.1]. Wayground holds ISO/IEC 27001:2022 certification with internal and external audits [S09] and has completed a SOC 2 Type II examination [S01 §12.1]. The TX-NDPA requires a cybersecurity framework (NIST CSF, ISO 27000 marked) and an audit right [S12 Art. V §2–§3, p. 20].
- **Gap:** A designated coordinator and annual risk assessments are not described in public documents.
- **Recommendation:** Request the SOC 2 Type II report and ISO certificate scope under NDA, and confirm the §312.8(b) elements.

## 5. What this assessment does not cover
- Anything not in public documents, such as actual vendor practices, non-public contracts, or the technical behavior of the product. Out of scope by design ([scenario](../scenario.md) §6).
- Texas general breach-notification law and PPRA (scope decisions, 2026-11-03).
- Legal conclusions. This is a documentation review.

---
_Prepared as an independent educational exercise based only on public documents (accessed 2026-11-03). Not legal advice. Not affiliated with or endorsed by Wayground. All organizations other than the named vendor are fictional._
