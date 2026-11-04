# Texas Responsible Artificial Intelligence Governance Act — Applicability to Lantern Local (S9b)

**Status:** FINAL (2026-11-03). Section-by-section reading of H.B. 149 as enacted [S08]. **R-14 rated Low (inherent and residual) by Brittany.**
**Legal currency:** H.B. 149 takes effect January 1, 2026 [S08]. Brittany checked the official site on 2026-11-03: Chapters 551–552 show only "Added by Acts 2025" (H.B. 149), with no later amendments.

_Fictional company and product. Not legal advice._

## 1. Does the Act apply to Mesquite Lantern?
- **Who it covers:** a person who "(1) promotes, advertises, or conducts business in this state; (2) produces a product or service used by residents of this state; or (3) develops or deploys an artificial intelligence system in this state" (§551.002 [S08]). Mesquite Lantern meets (1) and (2).
- **Is the recommendation engine an "artificial intelligence system"?** The Act defines it as "any machine-based system that, for any explicit or implicit objective, infers from the inputs the system receives how to generate outputs, including content, decisions, predictions, or recommendations, that can influence physical or virtual environments" (§551.001(1) [S08]). SYS-3 infers interests from activity and location and outputs event recommendations (system description F-4). **It likely meets the definition.**
- **Roles:** Mesquite Lantern builds SYS-3 and uses it in Texas, so it is both a "developer" and a "deployer" (§552.001(1)–(2) [S08]).

## 2. Section-by-section

| Section | Who it binds | What it requires or prohibits | Applies to Lantern Local? |
|---------|--------------|-------------------------------|---------------------------|
| §552.051(b)–(e) Disclosure to consumers | "A governmental agency" | Disclose that a consumer is interacting with an AI system; clear, plain language, no dark patterns | **No.** The duty in (b) is stated for governmental agencies. |
| §552.051(f) Health care | Providers of health care services | Disclose AI use in health care | **No.** Not a health care service. |
| §552.052 Manipulation of human behavior | "A person" | May not develop or deploy AI "in a manner that intentionally aims to incite or encourage" self-harm, harm to others, or criminal activity | **Applies, but the design does not implicate it.** Event recommendations have no such aim. |
| §552.053 Social scoring | "A governmental entity" | Prohibits social scoring | **No.** |
| §552.054 Biometric data | "A governmental entity" | Prohibits certain biometric identification | **No.** Lantern Local collects no biometric data. |
| §552.055 Constitutional protection | "A person" | May not develop or deploy AI "with the sole intent" to infringe constitutional rights | **Applies, but the design does not implicate it.** |
| §552.056 Unlawful discrimination | "A person" | May not develop or deploy AI "with the intent to unlawfully discriminate against a protected class." "Disparate impact is not sufficient by itself to demonstrate an intent to discriminate" (c). Protected classes include religion and sex (a)(3) | **Applies.** The design has no discriminatory intent. As designed, though, the engine inferred religion- and LGBTQ+-related interests (R-04). D-1 and D-4 remove those from profiles and advertising. |
| §552.057 Sexual content; minors | "A person" | Prohibits certain sexual content and child-imitating sexual chat | **No.** No such functionality. |
| §552.101–.105 Enforcement | Attorney General | Exclusive AG enforcement; no private right of action (§552.101). Complaint portal (§552.102). Civil investigative demand (§552.103). **60-day notice and cure period** (§552.104). Civil penalties: $10,000–$12,000 per curable violation, $80,000–$200,000 per uncurable violation, $2,000–$40,000 per day for continued violations (§552.105(a)). Rebuttable presumption of reasonable care (§552.105(c)) | Applies if a violation is alleged |
| §541.104(a)(2), as amended | Processors under the TDPSA | Assist the controller with security of personal data "collected, stored, and processed by an artificial intelligence system" | **Yes.** Processors handling SYS-3 data (e.g., the cloud host). |
| Ch. 553 Sandbox; Ch. 554 Council | Program and state council | Optional sandbox participation; state council | Not required. Not assessed further. |

## 3. What the Attorney General can request
After a complaint, the Attorney General may request, through a civil investigative demand (§552.103(b) [S08]): "(1) a high-level description of the purpose, intended use, deployment context, and associated benefits"; "(2) a description of the type of data used to program or train" the system; "(3) … the categories of data processed as inputs"; "(4) … the outputs"; "(5) any metrics the person uses to evaluate the performance"; "(6) any known limitations"; "(7) … the post-deployment monitoring and user safeguards"; and "(8) any other relevant documentation."

**Observation:** the design submitted for review includes no AI system documentation for SYS-3 covering these items.

## 4. Resulting risk (added to the risk register)

**R-14. Recommendation engine is likely a regulated "artificial intelligence system," and the documentation the AG may request is not prepared**
- **Requirement:** §551.001(1), §551.002, §552.103(b), §541.104(a)(2) as amended [S08].
- **Gap:** No AI system documentation for SYS-3. Processor contracts don't yet address assistance with AI-system data security.
- **Mitigation options:**
  - a short "AI system record" for SYS-3 covering the §552.103(b) items (purpose, training data, inputs, outputs, metrics, limitations, monitoring);
  - confirm SYS-3 does not use protected-class attributes (this follows from D-4);
  - add the §541.104(a)(2) assistance term to processor contracts;
  - monitor Attorney General guidance.
- **Rating (Brittany, 2026-11-03):** Likelihood **Low** (the Act's private-sector prohibitions are intent-based, and the design has no such aim) × Impact **Medium** (investigation burden; penalties if a violation were found) → **Low**. With mitigations, residual **Low**.
