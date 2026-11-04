# Risk Register — Lantern Local PIA (S7)

**Status:** Risks identified (S7). **Ratings, mitigations, and residual ratings decided by Brittany Green, 2026-11-03 (S8)**. See the end of this file.

_Fictional company, product, and data. Not legal advice._

## Method
- Each feature and flow in the [system description](system-description.md), [inventory](../deliverables/1-data-inventory.xlsx), and [data-flow map](../deliverables/2-data-flow-map.md) was checked against:
  - the **Texas Data Privacy and Security Act**, Tex. Bus. & Com. Code Ch. 541, as enacted [S01];
  - **FTC Act §5** [S03], with the FTC's location-data actions [S04–S06] as illustrations;
  - the nine **FIPPs** [S07].
- **Wording:** each risk states the design as submitted, the requirement, and the *gap relative to* that requirement. FTC press releases describe allegations and orders in other cases. They are cited as illustrations of regulator focus, not as rules that bind Mesquite Lantern.
- **§541.105(b) factors** (benefits, de-identified data, consumer expectations, context, relationship) are noted where they bear on a risk. The full benefit–risk weighing is in the PIA report (S9).

## Summary

| ID | Risk | Features / data | FIPPs |
|----|------|-----------------|-------|
| R-01 | Background location collected by default during onboarding | F-3; DE-08, DE-09 | Individual Participation; Minimization |
| R-02 | Location used for profiling, ads, and segments beyond the purpose shown in the location prompt | F-2–F-4, F-7, F-8; DE-07–09, DE-12, DE-21, DE-24 | Purpose Specification and Use Limitation; Transparency |
| R-03 | 24-month precise location history | F-2, F-3; DE-09 | Minimization; Security |
| R-04 | Sensitive event categories flow into profiles, check-ins, and segments without specific consent | F-4, F-5, F-8; DE-11, DE-12, DE-14, DE-21 | Individual Participation; Purpose Specification and Use Limitation |
| R-05 | Audience segments provided to advertisers described as "anonymous" | F-8; DE-17, DE-21 | Transparency; Accountability; Individual Participation |
| R-06 | Ad network SDK receives profile, coarse location, and device IDs | F-7; DE-12, DE-17, DE-24; flows SYS-1→TP-2, SYS-3→TP-2 | Transparency; Individual Participation; Minimization |
| R-07 | Sign-up relies on a single terms checkbox and a pre-checked marketing box | F-1; DE-02, DE-23 | Individual Participation; Transparency |
| R-08 | Consumer requests and opt-outs only through one web form | All; §541.051 rights | Individual Participation; Access and Amendment |
| R-09 | Organizers receive attendee data and use it for their own marketing | F-10; DE-01, DE-02, DE-14, DE-15; flow SYS-6→TP-5 | Purpose Specification and Use Limitation; Transparency |
| R-10 | Analytics SDK's role is not established; vendor contracts not reviewed | F-9; TP-1 (also TP-2–TP-4) | Accountability; Security |
| R-11 | Deletion requests can't fully be honored (check-ins kept forever; downstream copies) | F-5, F-8, F-10; DE-14, DE-21; TP-1, TP-2, TP-5, TP-6 | Individual Participation; Minimization |
| R-12 | Age limit relies on a self-declared date of birth | F-1; DE-04 | Quality and Integrity |
| R-13 | Security of concentrated location and profile data in the data warehouse | SYS-2, SYS-4; DE-09, DE-12, DE-14 | Security |

---

## Risk details

### R-01. Background location collected by default during onboarding
- **Design:** Onboarding screen 3 ("Get alerts about events near you") leads to the OS "Always allow" prompt. Background location is **on by default** in that flow and is collected every 15 minutes with the app closed (F-3; DE-08).
- **Requirement:**
  - Processing sensitive data requires consent (§541.101(b)(4) [S01]). Precise geolocation is sensitive data (§541.001(21), (29)(D)).
  - "Consent" must be "freely given, specific, informed, and unambiguous" and excludes "agreement obtained through the use of dark patterns" (§541.001(6), (6)(C)).
  - A "dark pattern" is an interface "designed or manipulated with the effect of substantially subverting or impairing user autonomy, decision-making, or choice" (§541.001(10)).
- **Gap:** A default-on setting inside onboarding, framed only around alerts, is a gap relative to the consent definition. Whether it is a dark pattern depends on the final screen design.
- **Expectations / context (§541.105(b)(2)(B)–(C)):** Users of an events app may not expect location to be collected every 15 minutes while the app is closed.
- **Illustration:** In the FTC's InMarket matter, the FTC alleged location was requested for app features and also used for advertising. The order required informed consent [S05, S06].
- **Mitigation options (for S8):** make F-3 off by default with a separate, specific opt-in; collect only near saved events (geofences) rather than every 15 minutes; offer a "while using" mode.

### R-02. Location used beyond the purpose shown in the location prompt
- **Design:** The OS prompts describe finding events and getting alerts (F-2, F-3). The same location data also builds the interest profile (F-4), feeds coarse location to the ad network (F-7), and builds advertiser segments (F-8).
- **Requirement:** A controller may not process personal data "for a purpose that is neither reasonably necessary to nor compatible with the disclosed purpose … unless the controller obtains the consumer's consent" (§541.101(b)(1) [S01]). Sensitive data needs consent (§541.101(b)(4)). The privacy notice must state purposes (§541.102(a)(2)).
- **Gap:** The design discloses advertising and profiling uses of location only in the privacy policy. That is a gap relative to purpose-specific consent for sensitive data.
- **Illustration:** InMarket and X-Mode both involved location data used or sold for advertising without users being "fully informed" [S04, S05].
- **Mitigation options:** a separate opt-in for using location for ads and personalization; keep event-finding location separate from advertising; describe each use at the point of collection.

### R-03. 24-month precise location history
- **Design:** DE-09 stores a trail of foreground and background locations for **24 months** "to improve recommendations."
- **Requirement:** Collection limited to what is "adequate, relevant, and reasonably necessary" for the disclosed purposes (§541.101(a)(1) [S01]). Security appropriate to "the volume and nature" of the data (§541.101(a)(2)).
- **Gap:** The design gives no reason why 24 months of precise location is needed for event recommendations. That is a gap relative to the minimization standard. A long, precise trail can reveal home, work, and places visited.
- **Mitigation options:** shorten retention (for example, days for raw points); convert to coarse location or interest signals and delete raw points; no history at all for F-2.

### R-04. Sensitive event categories flow into profiles, check-ins, and segments
- **Design:** Event categories include *Faith & Spirituality*, *Pride & LGBTQ+*, *Community & Politics*, and *Health & Wellness Support Groups*. These flow into selected interests (DE-11), inferred interests (DE-12), check-ins (DE-14), and audience segments (DE-21).
- **Requirement:** "Sensitive data" includes personal data "revealing … religious beliefs, mental or physical health diagnosis, sexuality" (§541.001(29)(A) [S01]). Processing it requires consent (§541.101(b)(4)). Profiling with a foreseeable risk of injury or intrusion requires an assessment (§541.105(a)(3)).
- **Gap:** The design has no specific consent for sensitive categories and uses them in advertising segments. That is a gap relative to §541.101(b)(4).
- **Illustration:** According to the FTC's release, the InMarket proposed order bars products that categorize or target consumers based on sensitive location data, and the FTC described segments such as "Christian church goers" [S05].
- **Mitigation options:** exclude sensitive categories from profiling and segments entirely; keep them for event search only (not stored to the profile); a specific opt-in if they are stored.

### R-05. Audience segments provided to advertisers described as "anonymous"
- **Design:** F-8 offers advertisers segments (e.g., "live-music fans near downtown Austin") containing **hashed device advertising IDs**. The product team calls them "anonymous." Not yet described to users.
- **Requirement:**
  - Disclosure to a third party for value is a "sale" (§541.001(28) [S01]).
  - "Deidentified data" excludes data that can be linked to "a device linked to that individual" (§541.001(12)).
  - Selling sensitive data requires consent (§541.101(b)(4)), the notice "NOTICE: We may sell your sensitive personal data." (§541.102(b)), a disclosure and opt-out method (§541.103), and an opt-out right (§541.051(b)(5)(B)).
  - Calling data "deidentified" brings obligations: reasonable measures, a public commitment not to re-identify, and contractual flow-down (§541.106(a)).
- **Gap:** Hashed advertising IDs identify a device for targeting, so the segments are personal data (and sensitive data where built from location or sensitive categories). Describing them as "anonymous" is a gap relative to §541.001(12). If made in a public statement, it could raise FTC §5 deception concerns [S03].
- **Illustration:** InMarket sorted consumers into audience segments from location histories [S05].
- **Mitigation options:** drop segment sales; offer aggregate reports only (performance measurement is excluded from "targeted advertising," §541.001(31)(B)); if kept, exclude sensitive data, obtain consent, post the §541.102(b) notice, and sign contracts limiting advertiser use.

### R-06. Ad network SDK receives profile, coarse location, and device IDs
- **Design:** The ad SDK (TP-2) gets the device advertising ID from the app. The recommendation engine sends interest categories (including sensitive ones) and "coarse location" with ad requests. Retention and onward use by the ad network were not reviewed. Android has no in-app ad-tracking prompt.
- **Requirement:**
  - "Targeted advertising" covers ads selected from activity "over time and across nonaffiliated websites or online applications," but excludes ads based only on the controller's own app (§541.001(31) [S01]).
  - If F-7 is targeted advertising: assessment (§541.105(a)(1)), disclosure and opt-out (§541.103), and the opt-out right (§541.051(b)(5)(A)).
  - "Precise geolocation" is within 1,750 feet (§541.001(21)).
- **Gap:** The design doesn't establish whether the ad network uses cross-app data (which decides whether F-7 is "targeted advertising"), how coarse "coarse location" is, or the ad network's role and retention. Sensitive interest categories are sent to an independent third party.
- **Mitigation options:** contextual ads only (based on the event being viewed); strip sensitive categories from ad requests; set coarse location to metro level, well beyond 1,750 feet; contract terms limiting the ad network's use; honor platform and device opt-out signals (see R-08).

### R-07. Sign-up relies on a single terms checkbox and a pre-checked marketing box
- **Design:** One checkbox: "I agree to the Terms and Privacy Policy." The marketing email opt-in is **pre-checked** (F-1).
- **Requirement:** Consent excludes "acceptance of a general or broad terms of use or similar document" (§541.001(6)(A) [S01]) and agreement obtained through dark patterns (§541.001(6)(C), (10)).
- **Gap:** The terms checkbox can't serve as consent for sensitive data (R-01, R-02, R-04). The pre-checked box is a gap relative to the dark-pattern exclusion. (Email marketing law beyond Ch. 541 is out of scope.)
- **Mitigation options:** separate, unchecked opt-ins for marketing; just-in-time consent for each sensitive use; a privacy notice that meets §541.102(a).

### R-08. Consumer requests and opt-outs only through one web form
- **Design:** Opt-out of targeted ads and sale is only a web form linked from the privacy policy. There is no in-app setting at launch.
- **Requirement:**
  - Consumers have rights to access, correct, delete, port, and opt out (§541.051(b) [S01]).
  - Controllers must provide "two or more secure and reliable methods" that account for "the ways in which consumers normally interact with the controller" (§541.055(a)).
  - Opt-outs via an authorized agent, including "a global setting on an electronic device," must be honored when verifiable (§541.055(e); effective 2025-01-01).
  - Response within 45 days (§541.052(b)).
- **Gap:** One web-only method for an app-first product is a gap relative to §541.055(a). The design has no plan for device-level opt-out signals (§541.055(e)).
- **Mitigation options:** in-app privacy settings (opt-outs, deletion, export) plus an email address; honor device-level signals; a request log with the 45-day clock.

### R-09. Organizers receive attendee data and use it for their own marketing
- **Design:** Organizers (TP-5) get name, email, check-ins, and ticket purchases for their events, "to manage attendance and market future events," and keep it under their own policies.
- **Requirement:** Disclosure to a third party "for purposes of providing a product or service requested by the consumer" is excluded from "sale" (§541.001(28)(B) [S01]). Other uses must be compatible with the disclosed purpose or have consent (§541.101(b)(1)). Check-ins can be sensitive data (§541.001(29)(A)), which requires consent (§541.101(b)(4)).
- **Gap:** Sharing to fulfill tickets fits the exclusion. Sharing so organizers can market to attendees, plus check-ins at sensitive-category events, goes beyond it. Whether organizers give "valuable consideration" (the sale definition) depends on the revenue-share arrangement, which isn't specified.
- **Mitigation options:** share only what ticket fulfillment needs; get an attendee opt-in for organizer marketing; don't share check-ins for sensitive categories; organizer contract terms limiting use.

### R-10. Analytics SDK's role is not established; vendor contracts not reviewed
- **Design:** The analytics SDK (TP-1) gets account ID, activity, device IDs, IP address, and crash logs directly from the app. Its role (processor or third party) and retention aren't stated. Contracts with TP-1 through TP-4 weren't reviewed.
- **Requirement:** A processor acts "on behalf of a controller" (§541.001(23) [S01]) under a contract with instructions, purpose, data types, duration, confidentiality, deletion or return, and assessment support (§541.104(a)–(b)). §541.104(a)(2) was amended effective 2026-01-01 to add assistance with security for data processed by an "artificial intelligence system" [S08]. A third-party recipient may make the disclosure a "sale" if there's consideration (§541.001(28)).
- **Gap:** Without a defined role and contract, the company can't show that TP-1's use is limited to its instructions. That is a gap relative to §541.104(b).
- **Mitigation options:** choose analytics configured as a processor (no use for its own purposes) and sign §541.104(b) terms; minimize identifiers sent; review TP-2–TP-4 contracts too.

### R-11. Deletion requests can't fully be honored
- **Design:** Check-in history is never deleted (badges are permanent). Advertisers and organizers keep downloaded data. Ad network and analytics retention weren't reviewed.
- **Requirement:** Right to "delete personal data provided by or obtained about the consumer" (§541.051(b)(3) [S01]). Processors must delete or return data at the controller's direction (§541.104(b)(6)(B)). FIPPs Minimization [S07].
- **Gap:** The design has no deletion path for check-ins or for data already passed to third parties. That is a gap relative to the deletion right.
- **Mitigation options:** let users delete check-ins (or keep only badge counts); retention limits and deletion obligations in partner contracts; share less with third parties to begin with.

### R-12. Age limit relies on a self-declared date of birth
- **Design:** Users enter a date of birth, and under-18 entries are blocked (F-1).
- **Requirement:** Personal data "collected from a known child" (under 13) is sensitive data (§541.001(5), (29)(C) [S01]). FIPPs Quality and Integrity [S07]. Laws specific to minors and children's privacy are **not in this project's source register**, so they aren't assessed here (scope note).
- **Gap:** A self-declared age gate gives limited assurance that the 18+ limit holds.
- **Mitigation options:** a neutral age screen (no hints about the cutoff); block re-entry after a failed attempt; respond if the company gains actual knowledge that a user is a minor; add a review of laws on minors to scope if the user base changes.

### R-13. Security of concentrated location and profile data
- **Design:** The data warehouse (SYS-4) holds copies of location history, profiles, check-ins, and segments for analytics and advertiser reports.
- **Requirement:** "Reasonable administrative, technical, and physical data security practices that are appropriate to the volume and nature of the personal data" (§541.101(a)(2) [S01]). FIPPs Security [S07].
- **Gap:** Security controls for SYS-4 are outside this PIA's scope (scenario §6). This risk records that the warehouse concentrates the most sensitive data in the system, so its controls need confirming.
- **Mitigation options:** keep only aggregated or coarse data in the warehouse; access controls and logging; encryption; retention limits matching R-03.

## Notes for S8
- **Most risks share a root cause:** location and sensitive categories are reused for advertising (R-02, R-04, R-05, R-06). A design change, such as separating event-finding from advertising, could address several at once.
- Benefits to weigh (§541.105(b)(1)), for the S9 report: finding relevant local events, small-business revenue, and a free service for users.

---

## Ratings and mitigations (decided by Brittany, 2026-11-03)

**Method:** 3×3 likelihood × impact, the same matrix as Project 01 (High×High/Medium → High; Medium×Medium → Medium; Low×High → Medium; Low×Medium/Low → Low). **Inherent** = the design as submitted. **Residual** = after the chosen mitigations are implemented.

### Design decisions
| # | Decision | Chosen option | Risks addressed |
|---|----------|---------------|-----------------|
| D-1 | Advertising model | **Contextual ads only.** Ads are based on the event or page being viewed. **No audience segment sales.** Advertisers get aggregate performance reports only (measurement is excluded from "targeted advertising," §541.001(31)(B) [S01]). Location and sensitive categories never feed advertising. Ad SDK configured without the device advertising ID. | R-02, R-04, R-05, R-06 |
| D-2 | Background alerts (F-3) | **Off by default; separate, specific opt-in; geofenced** alerts near events the user saved, replacing collection every 15 minutes | R-01 |
| D-3 | Raw precise location retention | **7 days**, then delete raw points and keep only coarse or interest signals | R-03, R-13 |
| D-4 | Sensitive event categories | **Search-only.** Users can browse them, but they are never stored in the profile or check-in history unless the user explicitly opts in | R-04 |

### Supporting mitigations (recommended with the decisions)
- **Consent and notice (R-07):** separate, unchecked opt-ins (marketing, background location); just-in-time explanations at each collection point; a privacy notice meeting §541.102(a).
- **Rights (R-08):** in-app privacy settings (opt-outs, deletion, export) plus an email address (§541.055(a)); honor device-level opt-out signals (§541.055(e)); track the 45-day response clock (§541.052(b)).
- **Organizers (R-09):** share only what ticket fulfillment needs (§541.001(28)(B)); attendee opt-in for organizer marketing; no check-ins for sensitive categories; contract use limits.
- **Vendors (R-10):** analytics configured as a processor, with §541.104(b) contract terms for TP-1, TP-3, TP-4; ad network contract limiting use.
- **Deletion (R-11):** user-deletable check-ins (keep only badge counts); deletion and retention terms in partner contracts.
- **Age (R-12):** neutral age screen, block re-entry after a failed attempt, a process for when the company learns a user is a minor.
- **Warehouse (R-13):** keep only aggregated or coarse data in SYS-4; confirm access controls, logging, and encryption (outside this PIA's scope).

### Ratings

| ID | Risk | Inherent L | Inherent I | **Inherent** | Mitigation | Residual L | Residual I | **Residual** |
|----|------|-----------|-----------|--------------|------------|-----------|-----------|--------------|
| R-01 | Background location on by default | High | High | **High** | D-2 | Low | High | **Medium** |
| R-02 | Location reused beyond the prompt's purpose | High | High | **High** | D-1 | Low | Medium | **Low** |
| R-03 | 24-month location history | High | High | **High** | D-3 | Low | High | **Medium** |
| R-04 | Sensitive categories in profiles and segments | Medium | High | **High** | D-1, D-4 | Low | Medium | **Low** |
| R-05 | "Anonymous" segments sold to advertisers | High | High | **High** | D-1 | Low | Low | **Low** |
| R-06 | Ad network receives profile, location, IDs | Medium | High | **High** | D-1 | Low | Medium | **Low** |
| R-07 | Terms checkbox; pre-checked marketing | High | Medium | **High** | Consent and notice | Low | Medium | **Low** |
| R-08 | One web-form opt-out | High | Medium | **High** | Rights | Low | Medium | **Low** |
| R-09 | Organizer marketing use | Medium | Medium | **Medium** | Organizers | Low | Medium | **Low** |
| R-10 | Analytics role and contracts | Medium | Medium | **Medium** | Vendors | Low | Medium | **Low** |
| R-11 | Deletion gaps | Medium | Medium | **Medium** | Deletion | Low | Medium | **Low** |
| R-12 | Self-declared age gate | Low | Medium | **Low** | Age | Low | Low | **Low** |
| R-13 | Warehouse security | Low | High | **Medium** | D-3, Warehouse | Low | High | **Medium** |

**Totals:** inherent 8 High / 4 Medium / 1 Low → residual **0 High / 3 Medium / 10 Low**. The three remaining Medium risks involve sensitive data that is still collected with consent (R-01, R-03) or controls outside this PIA's scope (R-13).
