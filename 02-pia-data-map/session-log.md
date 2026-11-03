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
