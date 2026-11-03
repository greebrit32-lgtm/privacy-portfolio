# Session Log — Project 02

## S0 — 2026-11-03 — Plan approved ✅
**Done**
- Brittany chose **Scenario C**: a fictional Texas company launching a consumer mobile app with location data and ad targeting. (Considered: A, PHISD AI tutor, which keeps the portfolio in one sector; B, health clinic portal / HIPAA.)
- Approved the 11-session plan and four deliverables (data inventory .xlsx, Mermaid data-flow map, PIA report, 1-page executive summary). Plan is in `README.md`.
- Added a CLAUDE.md data rule: inventories and maps list data **types**, never sample records.

**Next step (S1):** Draft `scenario.md`. Fictional company name (checked against Texas business records and web search, so it doesn't match a real company), what the app does, users (adults only, or teens too?), launch context, and which features are in scope.

**Open questions for Brittany**
- App concept. Ideas to pick from in S1: a local-events finder, a fitness/running app, a rewards app for Texas small businesses.
- Will the app allow users under 18? Under 13? This changes which laws apply.

## S1 — 2026-11-03 — Scenario and fictional organization ✅
**Done**
- Brittany's decisions: app concept = **local-events finder**; users = **adults 18+ only**; name = **Mesquite Lantern Co. / "Lantern Local"** (web searches on 2026-11-03 found no exact matches; rejected "Caliche Labs" (several real "Caliche" businesses in Texas) and "Nearbuzz" (close to existing apps NearestBuzz and NearBuz)). Project 02 commits stay local for now (push on hold).
- Drafted `scenario.md`: company profile, request, users, 10 planned features (F-1 to F-10) listing data **types** only, third parties by role, scope limits, review standards (named only), and roles.
- Set up `study-notes.md` (two placeholders to cite in S2), `sources/source-register.md`, and folders.

**Next step (S2):** Collect the legal and framework sources: the Texas Data Privacy and Security Act (official statute text; sections on sensitive data, consumer rights, data protection assessments, and the sale of data / targeted advertising), FTC Act §5 and FTC guidance and actions on location data, a FIPPs source, and a public PIA template to benchmark the report structure. Register each one and fill in the study notes.

**Open questions for Brittany**
- Review `scenario.md`. Are the features right? F-3 (background location) and F-8 (audience segments for advertisers) were included deliberately to give the PIA real trade-offs.
- Which PIA template to benchmark (options in S2).

## S2 — 2026-11-03 — Legal and framework sources ✅
**Done**
- Registered S01–S07: TDPSA as enacted (H.B. 4, 88R; effective 2024-07-01, §541.055(e) 2025-01-01), the codified Ch. 541 URL (amendments pending manual check), 15 U.S.C. §45 (govinfo 2024 ed.), FTC X-Mode (proposed, 2024-01-09) and InMarket (proposed 2024-01-18; final 2024-05-01) press releases, and the Federal Privacy Council FIPPs resource (9 principles). Snapshots saved for S01, S03, S07. FTC pages could not be downloaded (site blocks it) and were read via the fetch tool.
- **Brittany's decisions:** (1) assume the full TDPSA applies (Mesquite Lantern is not an SBA small business; stated as an assumption in scenario §5); (2) structure the PIA on the §541.105(b) assessment elements, with the 9 FIPPs as the risk lens.
- Study notes: filled in citations for the PIA/assessment and precise-geolocation rows; added FTC §5 unfairness and the narrow TDPSA "targeted advertising" definition.

**Key legal points for later sessions (sourced)**
- Precise geolocation is sensitive data (§541.001(29)(D)), and processing it requires consent (§541.101(b)(4)). Consent excludes acceptance of general terms (§541.001(6)).
- An assessment is required for targeted advertising, sale, profiling with risk, and sensitive data (§541.105(a)(1)–(5)).
- Ads based on activity within the company's own app are not "targeted advertising" (§541.001(31)(A)(i)).
- InMarket (S05–S06): own apps described location use for app features, then used it for advertising and audience segments. The order required informed consent.

**Next step (S3):** System description: for each feature F-1 to F-10, describe the data collected, when, from whom, why, which system and third party receive it, and retention. Write it as the product team's design (fictional), ready for the inventory.

**Open questions for Brittany**
- **5-minute manual check:** open https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm and note any "Amended by" lines under §§541.001–541.205, especially 2025 changes (S02).
- Push of Project 02 commits: still on hold.

## S3 — 2026-11-03 — System description ✅
**Done**
- Drafted `working/system-description.md`, the fictional product team's pre-review design: 12 systems and recipients (SYS-1–6, TP-1–6), 23 data-element **types** (DE-01–DE-23), and a feature-by-feature table (what is collected and when, purpose, destination, proposed retention, notice/choice as designed).
- Flagged 8 design choices for the PIA: background location on by default plus 24-month history; sensitive event categories (faith, LGBTQ+, politics, health support) flowing into check-ins, profiles, and segments; audience segments sold to advertisers as "anonymous" hashed IDs; single terms checkbox and pre-checked marketing; SDK data flows with retention not reviewed; self-declared age gate; no deletion for check-ins and downstream copies; opt-out only through a web form.

**Next step (S4):** Build `tools/build_inventory.py`, reusing the build-from-Markdown pattern of `build_questionnaire.py`. It reads the system description, generates `deliverables/1-data-inventory.xlsx` (one row per data element: type, source, feature, purpose, systems/recipients, retention, sensitivity, TDPSA category, legal basis/consent, notes), and leaves the analyst columns blank for S5.

**Open questions for Brittany**
- Review the flagged design choices. Any to add or remove? (It's fictional, so these are teaching choices.)
- Still pending: manual check of Ch. 541 "Amended by" lines (S02); push on hold.

## S4 — 2026-11-03 — Data inventory generator ✅
**Done**
- Made recipients explicit in `working/system-description.md`: new "Systems and recipients" column per data element (so the data map shows only real flows, e.g., card data → payment processor only). Added **DE-24 coarse location** (derived; sent to the ad network in F-7 and used in F-8 segments).
- Wrote `tools/build_inventory.py` (reuses the Project 01 helpers). It builds `deliverables/1-data-inventory.xlsx` with these sheets: Instructions; Inventory (24 rows: design columns from the system description plus 6 yellow analyst columns with Sensitivity / TDPSA-category dropdowns); **Data x Recipients** matrix (24 × 12, third-party cells shaded); Features; Systems & Recipients; Sources.
- Validation: the build stops on unknown recipients, features, or data IDs, or on invalid dropdown values (tested). Expands ID ranges like "DE-01–06" (a bug caught in testing: DE-03–06 were initially unlinked).
- CLAUDE.md output formats now mention the inventory builder.

**Next step (S5):** Fill in `working/inventory-notes.md` (analyst columns for DE-01–DE-24): sensitivity, TDPSA category, §541.105 trigger(s), consent/legal basis, FIPPs concerns, notes. All cited to S01–S07. Sensitivity calls are **PROPOSED — Brittany to decide**.

**Open questions for Brittany**
- Still pending: manual check of Ch. 541 "Amended by" lines (S02); push on hold.

## S5 — 2026-11-03 — Data inventory filled in ✅ (sensitivity PROPOSED)
**Done**
- Read the remaining TDPSA text needed for citations: consent (incl. exclusions for general terms and dark patterns), sale exclusions, targeted-advertising exclusions, pseudonymous data, opt-out rights §541.051(b)(5), privacy notice §541.102 (incl. the required "NOTICE: We may sell your sensitive personal data."), processor contracts §541.104, deidentified/pseudonymous data §541.106.
- Wrote `working/inventory-notes.md`: 24 analyst rows (sensitivity, TDPSA category, §541.105 triggers, consent/legal basis, FIPPs, notes), each cited to S01/S05–S07. Rebuilt the .xlsx.
- Proposed result: **8 High / 10 Medium / 6 Low** sensitivity. **7 types are Texas "sensitive data"**: precise location (DE-07, DE-08), location history (DE-09), interests/inferences/check-ins/segments that can reveal religion or sexuality (DE-11, DE-12, DE-14, DE-21).
- Flagged for S7: default-on background location vs. the "no dark patterns" consent definition; pre-checked marketing box; 24-month location history; segments described as "anonymous" but device-linked (§541.001(12)); organizer marketing use beyond the §541.001(28)(B) sale exclusion; coarse-location precision vs. the 1,750-ft definition; self-declared age gate.

**Next step (S6):** Data-flow map (Mermaid) built from the Data x Recipients matrix: users → app → Mesquite Lantern systems → processors vs. third parties, with sensitive flows highlighted. Must render on GitHub, plus a PDF.

**Open questions for Brittany**
- Sensitivity scale and calls (asked at the end of S5).
- Still pending: manual check of Ch. 541 "Amended by" lines; push on hold.
