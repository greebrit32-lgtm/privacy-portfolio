# MEMORANDUM

| | |
|--------|------------------------------------------------------------------------|
| **To** | District Privacy Officer, Pecan Hollow ISD *(fictional district)* |
| **From** | Brittany Green, Privacy Analyst |
| **Date** | November 3, 2026 |
| **Re** | Privacy review of Wayground (formerly Quizizz): recommendation |

**Recommendation: CONDITIONAL APPROVAL, PHASED.** Approve core quiz and lesson features once the Phase 1 conditions below are met. Hold AI features that use student work or names until the vendor documents how they handle that data. Approval as-is isn't supported (four High risks; key protections are in a contract not yet signed). Rejection isn't necessary: each High risk can be addressed by contract and district process, and because teachers can self-sign-up (F3), rejection without enforcement could leave *less* control than a signed DPA.

## 1. Summary

Teachers have asked to use Wayground district-wide (PK–12, about 12,000 students). I reviewed Wayground's public documents, including the Texas data privacy agreement it offers districts, against FERPA, COPPA, Texas Education Code §§32.151–.157, and the national SDPC agreement. All 41 questionnaire items have evidence and confirmed scores. Domain coverage ranges from 65% to 100%.

Most requirements are addressed. Most of the strongest protections come from the **Texas Student Data Privacy Agreement (TX-NDPA)**, which the district adopts by signing Exhibit E, and not from the privacy policy. Those protections are FERPA school-official status, 72-hour breach notice, breach-cost reimbursement, deletion within 60 days of a district request, and the DPA overriding the terms of service. The open issues involve the AI features and whether that agreement, signed as "Quizizz" in June 2025, covers them.

## 2. Top risks

| # | Risk | Rating |
|----|------------------------------------------------------------------------------------------|--------|
| F1 | **AI handling of student data is described differently across documents.** The policy says no personal data goes to AI platforms. The AI guide says the AI extension reads student names and submissions for grading and deletes submissions within 72 hours. | High |
| F2 | **Agreement coverage of AI features is not confirmed.** The Texas agreement was signed 06/11/2025, before the AI launch. Its covered-products list (Exhibit A) is illegible in the public copy, and the vendor may withdraw the offer after a material change in services. | High |
| F3 | **Protections depend on the DPA, and teachers can start without one.** The policy alone has no 72-hour breach notice, no district deletion deadline, and no school-official terms. Teachers can install the AI extension themselves. | High |
| F4 | **The COPPA consent model for students under 13 is not described.** Teachers are "requested to get parental consent," and the terms say Wayground does not require parental consent for under-13 users. | High |

Medium: provider lists differ across documents (F5); no written retention schedule for children's data (F6); material changes use notice plus continued use (F7). Low: F8, F9.

## 3. Conditions and contract terms to require

**Phase 1, core features:**

1. **Sign the TX-NDPA via Exhibit E unaltered**, and confirm in writing that the General Offer is still in effect. *(F2, F3)*
2. **Get an updated Exhibit A** listing every product used, including Wayground AI, and confirm that the "LEA Data" definition covers data processed by AI features. *(F2)*
3. **District-level control only:** no teacher self-sign-up or rostering until the DPA is executed. Ask whether sign-ups under district domains can be restricted. *(F3)*
4. **Settle the COPPA consent approach** for PK–5 rosters, and get written confirmation that under-13 data is used only for the school's benefit, with no other commercial purpose. *(F4)*
5. **Set a disposal deadline:** Exhibit D with 60-day disposal at contract end, plus the vendor's written retention policy for children's data. *(F6)*

**Phase 2, AI features using student work or names:**

6. **Get a written AI data-flow description** for each feature (inputs, providers, retention, de-identification), attached to the DPA. *(F1)*
7. **Get a complete subprocessor list** including AI gateway, model, and integrity providers, with change notice and no-training, zero-retention, and no-sale terms for each. *(F5)*
8. **Confirm the DPA prevails over later policy changes**, and describe how new consent is obtained for material changes affecting students under 13. *(F7)*

## 4. Next steps

If you agree: (1) I send the vendor the questionnaire follow-up questions and request the SOC 2 Type II report and ISO 27001 scope under NDA *(F9)*; (2) Wayground stays off the approved list until condition 1 is met; (3) teachers are told not to roster students yet. Reassess Phase 2 when the vendor responds. *Supporting documents: questionnaire (41 items), risk assessment (9 findings), and source register (S01–S25, accessed 2026-11-03).*

---
*Independent educational exercise based only on public documents. Not legal advice. Not affiliated with or endorsed by Wayground. Pecan Hollow ISD is fictional.*
