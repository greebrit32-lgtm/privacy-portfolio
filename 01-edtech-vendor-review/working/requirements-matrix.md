# Requirements Matrix — Wayground Review (Pecan Hollow ISD, fictional)

**Status:** DRAFT (S5, 2026-11-03). Domains and requirements were drafted by Claude for Brittany to review. Nothing here is a finding or a rating. This matrix defines *what we measure against*. Vendor evidence is collected in S8–S9.

_Disclaimer: independent educational exercise, based only on public documents. Not legal advice. Not affiliated with or endorsed by Wayground._

## How to read this

- **Basis type** tells you how much weight a requirement carries:
  - **Law**: statute or regulation (S16, S17, S20/S21). A gap here is a gap relative to a legal requirement.
  - **Guidance**: agency interpretation (S19, S22). It shows how regulators read the law, but it is not binding text.
  - **Contract benchmark**: model DPA terms (S23 NDPA v2.2; S12 TX-NDPA v1r6). Not law. These are what districts commonly require in contracts.
  - **Derived**: no source states this directly. It applies the requirements above to a new situation (AI), and it is labeled so readers can see that.
- **Vendor sources** lists where to look in S8–S9 (S01 current policy, S14 Quizizz-era policy, etc.).
- **TX-NDPA (S12):** a scanned document with no text layer. Its clause numbers will be mapped by hand in S8. Until then, the NDPA v2.2 (S23) clause is listed as the benchmark, and S12 is assumed to follow the same structure **only after it is checked**.

## Key context from the sources

- COPPA's school-consent model exists only in FTC guidance (S19 §N). The 2025 amendments did **not** finalize the proposed ed-tech and school provisions. The FTC "will continue to enforce COPPA in the ed tech context consistent with its existing guidance" (S18, 90 FR 16918 at 16918).
- 2025 COPPA amendments: effective 2025-06-23. Compliance date **2026-04-22** for most provisions (S18, DATES).
- Texas Subch. D is unamended since 2017 (S20, verified 2026-11-03), so its text is as enacted in S21.
- The NDPA v2.2 (S23) contains no AI-specific terms. AI requirements (Domain 6) are **derived**.

---

## Domains and requirements

### D1. Applicability and roles
| Req | Requirement (plain language) | Basis | Type | Vendor sources to check |
|-----|------------------------------|-------|------|-------------------------|
| D1.1 | For a vendor to receive education records without parental consent as a "school official," it must perform a service the district would otherwise use employees for, be under the district's **direct control** over use and maintenance of records, and follow redisclosure limits. | 34 CFR §99.31(a)(1)(i)(B)(1)–(3) [S16] | Law | S01, S02, S12 |
| D1.2 | A vendor is a Texas "operator" if it has actual knowledge its service is used primarily for, and was designed and marketed for, a school purpose. | Tex. Educ. Code §32.151(3) [S20, S21] | Law | S01, S11 (marketing) |
| D1.3 | Who the vendor says it is: legal entity, product names, and which products each document covers. | NDPA v2.2 §1.2, Exhibit A [S23] | Contract benchmark | S01 (scope paragraph), S08, S14 |

### D2. Data collection and minimization
| Req | Requirement | Basis | Type | Vendor sources |
|-----|-------------|-------|------|----------------|
| D2.1 | The vendor may not require a child to disclose more personal information than is reasonably necessary to participate in an activity. | 16 CFR §312.7 [S17] | Law | S01 §3, §6 |
| D2.2 | The categories of student data collected are listed (a data schedule). | NDPA v2.2 §1.3, Exhibit B [S23] | Contract benchmark | S01 §3, S12 Exhibit B |
| D2.3 | The vendor's collection is compared against Texas "covered information" (which includes student identifiers, search activity, voice recordings, and geolocation, among others). | §32.151(1) [S21] | Law (definition) | S01 §3 |

### D3. Use limitations
| Req | Requirement | Basis | Type | Vendor sources |
|-----|-------------|-------|------|----------------|
| D3.1 | Student data is used only to provide the contracted services or as the district instructs. | NDPA v2.2 §4.2 [S23] | Contract benchmark | S01, S02, S12 |
| D3.2 | Covered information may be used or disclosed only for the purposes listed in §32.153(a), including furthering a school purpose. Note: §32.153(e) also permits use for "maintaining, developing, supporting, improving, or diagnosing" the operator's service. | §32.153(a), (e) [S21] | Law | S01 §5 |
| D3.3 | A school official may not redisclose education-record PII without consent except as FERPA permits. | 34 CFR §99.33(a) [S16] | Law | S01 §5 |

### D4. Advertising, profiling, and sale
| Req | Requirement | Basis | Type | Vendor sources |
|-----|-------------|-------|------|----------------|
| D4.1 | No targeted advertising based on information acquired through school use. | §32.152(a)(1) [S21]; NDPA v2.2 §4.7(a) [S23] | Law + benchmark | S01 (principles; §1) |
| D4.2 | No student profile except for a school purpose. | §32.152(a)(2) [S21]; NDPA v2.2 §4.7(b) [S23] | Law + benchmark | S01 |
| D4.3 | No sale or rental of covered information (merger/acquisition exception, §32.152(c)(1)). | §32.152(a)(3), (c) [S21]; NDPA v2.2 §4.4 [S23] | Law + benchmark | S01, S04 |
| D4.4 | If the vendor relies on school consent under COPPA, the data is used only for the school's benefit and "for no other commercial purpose." | FTC COPPA FAQ §N.2 [S19] | Guidance | S01 §2 |

### D5. Subprocessors and third-party disclosure
| Req | Requirement | Basis | Type | Vendor sources |
|-----|-------------|-------|------|----------------|
| D5.1 | Third parties receiving covered information are under contract to use it only for the contracted school-purpose service and to protect it. | §32.153(d) [S21] | Law | S05, S01 §5 |
| D5.2 | Before releasing children's information to service providers, the vendor confirms they can protect it and gets written assurances. | 16 CFR §312.8(c) [S17] | Law | S05, S01 §5 |
| D5.3 | The vendor has subprocessor agreements at least as protective as the DPA, prohibiting sale. | NDPA v2.2 §2.3 [S23] | Contract benchmark | S05, S12 |
| D5.4 | A current, public list of subprocessors, including whether each one processes student data. | Derived from D5.1–D5.3 (transparency needed to verify them) | Derived | S05 (current), S01 link to legacy URL |

### D6. AI features, model training, and de-identified data
_No source in the register contains an AI-specific requirement. Each row applies the cited general requirement to AI features. **Derived**: Brittany to confirm the framing._

| Req | Requirement | Basis applied | Type | Vendor sources |
|-----|-------------|---------------|------|----------------|
| D6.1 | The documents say which AI features exist and whether students, teachers, or both use them. | D1.3; NDPA v2.2 Exhibit A [S23] | Derived | S10, S11, S01 |
| D6.2 | The documents say whether student data (prompts, responses, work) is sent to AI providers, and which ones. | D5.1–D5.3 | Derived | S05 (AI table), S01 |
| D6.3 | The documents say whether student data is used to **train or improve AI models**, and whether that data is identifiable or de-identified. | D3.1–D3.2; §32.153(e), §32.154(1)(A), (2) [S21]; NDPA v2.2 §4.5 [S23] | Derived | S01, S05, S14 vs. S01 |
| D6.4 | Use of de-identified data: no re-identification attempts, and limits on transfer to third parties other than subprocessors. | NDPA v2.2 §4.5 [S23] | Contract benchmark | S01 |
| D6.5 | Whether AI providers are bound by the same terms (no training on district data, no retention beyond the service). | D5.2–D5.3 | Derived | S05 |

### D7. Security program
| Req | Requirement | Basis | Type | Vendor sources |
|-----|-------------|-------|------|----------------|
| D7.1 | Reasonable security procedures and practices that protect covered information. | §32.155 [S21] | Law | S09, S01 |
| D7.2 | A **written** information security program with a designated coordinator, annual risk assessments, and safeguards (2025 amendment). | 16 CFR §312.8(b) [S17]; compliance date 2026-04-22 [S18] | Law | S01, S09 |
| D7.3 | Security aligned to a recognized framework (e.g., NIST CSF, ISO 27001), plus security audits. | NDPA v2.2 §5.2–5.3, Exhibit F [S23]; S12 p. 20 ("Cybersecurity Frameworks" table, as viewed; exhibit letter to confirm in S8) | Contract benchmark | S09, S12 |

### D8. Breach notification
| Req | Requirement | Basis | Type | Vendor sources |
|-----|-------------|-------|------|----------------|
| D8.1 | Notify the district within **72 hours** of confirming a breach, with the minimum content listed. | NDPA v2.2 §5.4 [S23] | Contract benchmark | S01, S02, S12 |
| D8.2 | Reimburse the district's breach-related costs (Texas addendum). | S12 p. 22 ¶6 "Reimbursement of Expenses Associated with Security Breach" (as viewed; exhibit heading to confirm in S8) | Contract benchmark | S12 |
| D8.3 | Statutory breach notice under Texas general law. | Not in current source register. **Open:** add Tex. Bus. & Com. Code §521.053 as a source, or keep it out of scope? | — | — |

### D9. Retention and deletion
| Req | Requirement | Basis | Type | Vendor sources |
|-----|-------------|-------|------|----------------|
| D9.1 | Keep children's data only as long as reasonably necessary, never indefinitely, and publish a **written retention policy** stating purposes, business need, and deletion timeframe. | 16 CFR §312.10 [S17]; compliance date 2026-04-22 [S18] | Law | S01 §4 |
| D9.2 | Delete a student's covered information within **60 days** of a district request (or as the contract specifies). | §32.156 [S21] | Law | S01 §4, S06 |
| D9.3 | Dispose of student data within 60 days of a request or of termination. | NDPA v2.2 §4.6 [S23] | Contract benchmark | S01 §4, S12 |

### D10. Parent and student rights
| Req | Requirement | Basis | Type | Vendor sources |
|-----|-------------|-------|------|----------------|
| D10.1 | Parents can inspect and review education records (through the district). | 34 CFR §99.10 [S16] | Law (district duty) | S01 §2 |
| D10.2 | On a parent's request, the operator describes the data collected from the child and lets the parent review it, refuse further use, and have it deleted. | 16 CFR §312.6 [S17] | Law | S01 §2 |
| D10.3 | The vendor helps the district respond to parent and student access requests. | NDPA v2.2 §2.2 [S23] | Contract benchmark | S01, S12 |

### D11. COPPA consent model
| Req | Requirement | Basis | Type | Vendor sources |
|-----|-------------|-------|------|----------------|
| D11.1 | Verifiable parental consent before collecting from children, including for **material changes** in practices. | 16 CFR §312.5(a)(1) [S17] | Law | S01 §2 |
| D11.2 | Separate consent for disclosure to third parties unless it is integral to the service (2025 amendment). | 16 CFR §312.5(a)(2) [S17] | Law | S01 §2, §5 |
| D11.3 | If relying on school authorization: limited to the educational context, direct notice to the school, and the school can review and delete. | FTC COPPA FAQ §N.1 [S19] | Guidance | S01 §2 |
| D11.4 | The decision is made by the district or school, not individual teachers. | FTC COPPA FAQ §N.3 [S19]; S22 | Guidance | S10 (teacher self-install), S06 |

### D12. Agreements, change, and legacy coverage
| Req | Requirement | Basis | Type | Vendor sources |
|-----|-------------|-------|------|----------------|
| D12.1 | A DPA or contract governs student data and takes priority over conflicting terms of service. | NDPA v2.2 "Priority of Agreements" [S23] | Contract benchmark | S02, S06, S12 |
| D12.2 | Agreements bind successors in a change of control, with notice to the district. | NDPA v2.2 "Successors Bound" [S23]; §32.152(c)(1) [S21] | Benchmark + law | S08 |
| D12.3 | **Legacy coverage:** whether agreements signed as "Quizizz" (S12, signed 06/11/2025) cover the services as they exist now, including AI features and policy revisions made after signing. | D12.1–D12.2; Exhibit E rule that the DPA must be unaltered (S12 p. 22 ¶7) | Derived | S08, S06, S12, S14 vs. S01 |
| D12.4 | How the vendor notifies districts of material policy changes. | 16 CFR §312.5(a)(1) (material change) [S17] | Law (COPPA scope) | S01, S02, S14 |

---

## Open questions for Brittany
1. **Domain count:** there are 12. Merge, split, or drop any? (For example, D8 Breach could merge into D7 Security.)
2. **D6 (AI) is labeled "Derived."** Is that the right framing for a public portfolio, or should AI requirements be presented as best practice with sources added later (e.g., ED or FTC AI guidance)?
3. **D8.3:** add Texas breach-notification law (Bus. & Com. Code §521.053) to scope, or leave it out to keep the project small?
4. **PPRA** (named in the NDPA recitals) is not in scope. Confirm that it stays out.
