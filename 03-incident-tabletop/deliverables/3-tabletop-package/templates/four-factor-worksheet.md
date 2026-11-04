# HIPAA Breach Risk Assessment — Four-Factor Worksheet (Template)

**Incident ID:** ________ · **Prepared by:** ________ · **Date:** ________ · **Approved by (Privacy Officer):** ________

> _Template from an independent educational exercise. Not legal advice. Sources: 45 CFR §164.402 [S01]; HHS Ransomware Fact Sheet [S03]._

## Step 1. Is this a possible breach?
| Question | Answer | Notes |
|----------|--------|-------|
| Does the incident involve protected health information (PHI)? | ☐ Yes ☐ No | |
| Was it a use or disclosure **not permitted** by the Privacy Rule? | ☐ Yes ☐ No | |
| Does an **exception** apply (§164.402(1)(i)–(iii): good-faith workforce access; inadvertent disclosure between authorized persons; recipient couldn't reasonably retain it)? | ☐ Yes ☐ No | |
| Was the PHI **"secured"** (rendered unusable, unreadable, or indecipherable per HHS guidance, e.g., properly encrypted with the key not compromised)? | ☐ Yes ☐ No | |
| **Ransomware?** HHS treats ePHI encrypted by ransomware as "acquired," so a breach is **presumed** unless low probability is shown [S03, Q6]. | ☐ Yes ☐ No | |

If PHI is involved, the use or disclosure was impermissible, no exception applies, and the PHI was unsecured, **a breach is presumed** unless Step 2 shows a low probability of compromise (§164.402(2)).

## Step 2. Four factors (§164.402(2)(i)–(iv))

| Factor | Evidence | Points toward low probability? |
|--------|----------|--------------------------------|
| **(i) Nature and extent of the PHI:** types of identifiers (names, SSNs, dates of birth, diagnoses, lab results, insurance IDs), sensitivity, likelihood of re-identification | | ☐ Yes ☐ No ☐ Unclear |
| **(ii) The unauthorized person** who used the PHI or received it (e.g., a known workforce member vs. a criminal actor) | | ☐ Yes ☐ No ☐ Unclear |
| **(iii) Whether the PHI was actually acquired or viewed** (forensic evidence; exfiltration; publication) | | ☐ Yes ☐ No ☐ Unclear |
| **(iv) Extent of mitigation** (retrieval, deletion attestation, assurances) | | ☐ Yes ☐ No ☐ Unclear |

## Step 3. Conclusion
☐ **Low probability of compromise demonstrated.** Not a breach. Keep this worksheet (burden of proof, §164.414).
☐ **Breach.** Notify per the [notification matrix](../../2-notification-matrix.md).

**Reasoning (plain language):**

**Affected individuals:** total ____ · by state: TX ____ / other ____ · minors ____ · contact info unusable ____

**Texas:** does the data include "sensitive personal information" (incl. health information, §521.002(a)(2)(B))? ☐ Yes ☐ No · Texas determination date: ________
