# Privacy Impact Assessment: Lantern Local

**Organization:** Mesquite Lantern Co. *(fictional)* · **Product:** Lantern Local mobile app *(fictional)*
**Prepared for:** General Counsel · **Prepared by:** Brittany Green, Privacy Analyst
**Date:** 2026-11-03 · **Legal sources current as of:** 2026-11-03 ([source register](../sources/source-register.md))
**Status:** FINAL (analyst recommendation). Ratings and decisions by Brittany Green.

> _Independent educational exercise. Mesquite Lantern Co., Lantern Local, and all data are fictional; data is described by type only. Not legal advice._

---

## 1. Summary and recommendation

Lantern Local is a free, ad-supported events app that the company plans to launch in four Texas metro areas for adults 18+. As designed, it collects **precise location in the foreground and background**, builds **interest profiles**, records **check-ins**, and shares data with an **ad network, advertisers, and event organizers**.

The design triggers a data protection assessment under Texas law on several grounds: it processes **sensitive data** (precise geolocation, and categories revealing religion or sexuality), and, as designed, **targeted advertising** and **sale of personal data** (Tex. Bus. & Com. Code §541.105(a)(1), (2), (4) [S01]). This report is that assessment.

**Findings:** 14 risks were identified. As designed, **8 are High, 4 Medium, and 2 Low.** Most High risks share one root cause: **location and sensitive interests collected to find events are reused for advertising.**

**Recommendation: LAUNCH WITH CONDITIONS.** Approve launch once the four design changes (D-1–D-4) and the supporting mitigations in Section 6 are built and verified. With them, residual risk is **0 High, 3 Medium, 11 Low.** The three Medium risks are accepted with monitoring and a re-review in six months (Section 7).

| Design change | Effect |
|------------------------------------------------------------|----------------------------------------|
| **D-1** Contextual ads only; no audience-segment sales; aggregate reports to advertisers | Location and sensitive data no longer feed advertising |
| **D-2** Background alerts off by default, with a specific opt-in and geofencing near saved events | Background location only with real consent |
| **D-3** Raw precise location kept 7 days, then coarsened | Location trail no longer kept for 24 months |
| **D-4** Sensitive event categories are search-only unless the user opts in | Faith, LGBTQ+, political, and health categories stay out of profiles |

## 2. Scope, method, and sources

- **In scope:** features F-1 to F-10 as submitted by Product and Engineering ([system description](../working/system-description.md)); users 18+ in Texas ([scenario](../scenario.md)).
- **Standards:**
  - Texas Data Privacy and Security Act, Tex. Bus. & Com. Code Ch. 541, as enacted [S01], with the 2025 amendment to §541.104(a) [S08]. Brittany checked the official site on 2026-11-03: no other section has been amended [S02].
  - FTC Act §5 [S03]; FTC location-data actions as illustrations [S04–S06].
  - The nine FIPPs [S07] as the risk lens.
- **Assumption:** Mesquite Lantern is not an SBA small business, so Chapter 541 applies in full (§541.002(a)(3) [S01]; scenario §5).
- **Method:** data inventory (24 data types) → data-flow map (15 flows) → risk identification (14 risks) → likelihood × impact ratings (3×3) → design decisions → residual ratings.
- **Also assessed:** the Texas Responsible Artificial Intelligence Governance Act (H.B. 149, eff. 2026-01-01) [S08], section by section ([assessment](../working/traiga-assessment.md)).
- **Out of scope:** users outside Texas; laws specific to minors; security testing; contract negotiation.

## 3. The system as designed

**Deliverables:** [data inventory (.xlsx)](1-data-inventory.xlsx) · [data-flow map](2-data-flow-map.md)

- **24 data types.** **7 are Texas "sensitive data"** (§541.001(29) [S01]): foreground and background precise location (DE-07, DE-08), location history (DE-09), and interests, inferred profile, check-ins, and audience segments that can reveal religion or sexuality (DE-11, DE-12, DE-14, DE-21).
- **15 data flows, 10 carrying sensitive data.** Sensitive data leaves the company on three flows: recommendation engine → **ad network** (profile, coarse location); organizer portal → **event organizers** (check-ins); advertiser portal → **advertisers** (profiles, segments).
- **Recipients:** two processors (push service, payment processor); three independent third parties (ad network, organizers, advertisers); and an analytics SDK whose role was not stated.

## 4. Data protection assessment (Tex. Bus. & Com. Code §541.105)

**Why an assessment is required (§541.105(a) [S01]):**

| Trigger | Present in the design? |
|--------------------------|--------------------------------------------------------------------------|
| (1) Targeted advertising | **Possibly.** Depends on whether the ad network uses cross-app data (§541.001(31)). Removed by D-1 (contextual ads). |
| (2) Sale of personal data | **Yes, as designed.** Audience segments provided to advertisers (F-8). Removed by D-1. |
| (3) Profiling with foreseeable risk | **Yes.** Inferred interests built from location and sensitive categories (F-4). Reduced by D-3 and D-4. |
| (4) Sensitive data | **Yes.** Precise geolocation; sensitive categories. **Remains after changes, with consent.** |
| (5) Other heightened risk | **Yes.** Continuous background location (F-3). Reduced by D-2. |

**Weighing benefits against risks (§541.105(b)(1)):**
- **Benefits:**
  - Consumers find relevant local events for free.
  - Local businesses and organizers reach nearby audiences.
  - Ticketing and check-ins support attendance.
  - The company earns revenue to keep the service free.
- **Risks:** As designed, the processing exposes where people are, when, and which faith, LGBTQ+, political, or health events they attend, and passes some of this to parties outside the company's control (Section 5).
- **Weighing:** The benefits depend on knowing roughly where a user is and what they like. They do **not** depend on continuous background tracking, a 24-month location trail, sensitive categories in profiles, or selling segments. With D-1–D-4, the core benefits remain and the highest-impact processing is removed or placed under specific consent.

**Factors the assessment must consider (§541.105(b)(2)):**

| Factor | Assessment |
|---------------|-------------------------------------------------------------------------------------|
| (A) Use of de-identified data | The design calls segments "anonymous," but they use hashed device advertising IDs. Texas excludes device-linkable data from "deidentified" (§541.001(12)), so they are personal data. D-1 replaces segments with aggregate reports. Any data the company describes as de-identified must meet §541.106(a): reasonable measures, a public commitment not to re-identify, and contracts. |
| (B) Reasonable expectations of consumers | Users of an events app expect location to be used to find nearby events. They are unlikely to expect collection every 15 minutes with the app closed, a two-year location history, or their attendance at faith or LGBTQ+ events shaping ads and advertiser segments. The FTC's InMarket matter involved location requested for app features and also used for advertising [S05, S06]. |
| (C) Context of the processing | A consumer entertainment app, adults 18+, Texas only. Location is precise, and event categories can reveal protected traits. Data reaches three kinds of independent third parties. |
| (D) Relationship between the controller and the consumer | Direct, account-based, and free to the user. Users have little ability to see or control downstream sharing in the design as submitted (single web-form opt-out, R-08). |

## 5. Risks

Full detail with citations is in the [risk register](../working/risk-register.md). Ratings use the 3×3 likelihood × impact method.

| ID | Risk | Inherent | Change(s) | Residual |
|-------|--------------------------------------------------------------|----------|-----------|----------|
| R-01 | Background location on by default during onboarding | **High** | D-2 | **Medium** |
| R-02 | Location reused for profiling, ads, and segments beyond the prompt's purpose (§541.101(b)(1)) | **High** | D-1 | Low |
| R-03 | 24-month precise location history (§541.101(a)(1)) | **High** | D-3 | **Medium** |
| R-04 | Sensitive event categories in profiles, check-ins, and segments (§541.001(29)(A); §541.101(b)(4)) | **High** | D-1, D-4 | Low |
| R-05 | Audience segments sold as "anonymous" (§541.001(12), (28); §541.102(b)) | **High** | D-1 | Low |
| R-06 | Ad network SDK receives profile, coarse location, device IDs (§541.001(21), (31)) | **High** | D-1 | Low |
| R-07 | Single terms checkbox; pre-checked marketing box (§541.001(6)(A), (6)(C)) | **High** | Consent and notice | Low |
| R-08 | Requests and opt-outs only through one web form (§541.055(a), (e)) | **High** | Rights | Low |
| R-09 | Organizers' marketing use of attendee data (§541.001(28)(B)) | Medium | Organizers | Low |
| R-10 | Analytics SDK role and vendor contracts not established (§541.104 [S01, S08]) | Medium | Vendors | Low |
| R-11 | Deletion requests can't fully be honored (§541.051(b)(3)) | Medium | Deletion | Low |
| R-12 | Self-declared age gate | Low | Age | Low |
| R-13 | Concentrated sensitive data in the data warehouse (§541.101(a)(2)) | Medium | D-3, Warehouse | **Medium** |
| R-14 | Recommendation engine likely a regulated "artificial intelligence system"; AI documentation not prepared (§551.001(1); §552.103(b) [S08]) | Low | AI record | Low |
| | **Totals** | **8 H / 4 M / 2 L** | | **0 H / 3 M / 11 L** |

## 6. Conditions for launch

**Design changes (all required):** D-1, D-2, D-3, D-4 (Section 1).

**Supporting mitigations (all required):**
1. **Consent and notice:** separate, unchecked opt-ins (marketing; background location); just-in-time explanations at each collection point. A privacy notice meeting §541.102(a): categories, purposes, rights, the appeal process, third-party sharing, and request methods.
2. **Consumer rights:** in-app privacy settings (access, delete, export, opt-outs) plus an email address (§541.055(a)); honor device-level opt-out signals (§541.055(e)); a request log with the 45-day response clock (§541.052(b)).
3. **Organizers:** share only what ticket fulfillment needs; attendee opt-in for organizer marketing; no check-ins for sensitive categories; contract limits on use and retention.
4. **Vendors:** processor contracts with the §541.104(b) terms for analytics, push, and payment providers. Analytics configured so the provider does not use data for its own purposes. An ad network contract limiting use; SDK set up without the device advertising ID.
5. **Deletion:** users can delete check-ins (only badge counts kept); deletion and retention terms flowed down to partners.
6. **Age screen:** neutral date-of-birth screen; block re-entry after a failed attempt; a process for responding when the company learns a user is a minor.
7. **AI system record (R-14):** a short record for the recommendation engine covering the items the Attorney General may request (purpose, training data, inputs, outputs, metrics, limitations, monitoring; §552.103(b) [S08]); add the §541.104(a)(2) AI-security assistance term to processor contracts.
8. **Data warehouse:** only aggregated or coarse data in SYS-4; Security to confirm access controls, logging, and encryption.

**Verification before launch:** the privacy analyst reviews the built onboarding and consent screens, privacy settings, ad SDK configuration, retention jobs, and signed vendor contracts against this list.

## 7. Residual risk and monitoring

| Residual Medium risk | Why it remains | Owner / monitoring |
|---------------------|--------------------------------|-----------------------------------------------|
| R-01 Background location (opt-in) | Precise location is still collected from users who opt in | Product: track opt-in rate and alert volume; re-review if collection changes |
| R-03 7-day raw location | Sensitive while it exists | Engineering: confirm the deletion job runs; quarterly check |
| R-13 Warehouse security | Controls are outside this PIA's scope | Security: confirm controls before launch |

**Re-review:** six months after launch, or sooner on any material change, such as new data uses, new recipients, targeted advertising, or a change in user ages. Texas requires a documented assessment of each processing activity listed in §541.105(a), so any new activity of that kind needs its own assessment.

## 8. Open items and scope notes
- **Texas Responsible Artificial Intelligence Governance Act (H.B. 149, eff. 2026-01-01) [S08]: assessed** ([detail](../working/traiga-assessment.md)).
  - **Applies:** Mesquite Lantern conducts business in Texas (§551.002), and the recommendation engine likely meets the "artificial intelligence system" definition (§551.001(1)).
  - **Not applicable:** the consumer-disclosure duty in §552.051(b), social scoring (§552.053), and biometric identification (§552.054) are stated for governmental entities.
  - **Intent-based prohibitions** that bind any person (manipulation, §552.052; constitutional rights, §552.055; unlawful discrimination, §552.056, where "disparate impact is not sufficient by itself"; sexual content, §552.057) are not implicated by the design.
  - **Enforcement:** by the Attorney General only, with a 60-day cure period (§§552.101, .104). Resulting risk: R-14 (Low).
  - **Legal currency:** Brittany checked the official site on 2026-11-03. Chapters 551–552 show only "Added by Acts 2025" (H.B. 149), with no later amendments.
- **Laws specific to minors and children's privacy:** not assessed (18+ product; see R-12).
- **Users outside Texas:** other states' laws not assessed. Re-review before expanding.
- **Documentation:** under §541.105(c)–(d) [S01], the Attorney General may request this assessment through a civil investigative demand, and it is confidential. Keep a dated copy with this PIA's decisions.

## 9. Sign-off

| Role | Name | Decision | Date |
|-------------------|--------------------------|--------------------------------------------------|-------|
| Privacy Analyst | Brittany Green | Recommends launch with conditions (Sections 6–7) | 2026-11-03 |
| General Counsel | *(fictional; pending)* | ☐ Approve with conditions ☐ Approve with changes ☐ Do not approve | |
| Head of Product | *(fictional; pending)* | ☐ Accepts conditions D-1–D-4 and mitigations | |

---
_Independent educational exercise. Fictional organization, product, and data. Prepared from public legal sources accessed 2026-11-03. Not legal advice._
