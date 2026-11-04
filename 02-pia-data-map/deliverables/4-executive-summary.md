# Lantern Local — Privacy Review: Executive Summary

**To:** Leadership team, Mesquite Lantern Co. *(fictional)* · **From:** Brittany Green, Privacy Analyst · **Date:** November 3, 2026 · **Decision needed:** approve launch with the conditions below

*Detail: [PIA report](3-pia-report.md) · [data inventory](1-data-inventory.xlsx) · [data-flow map](2-data-flow-map.md). Fictional company and data; independent educational exercise; not legal advice.*

**Recommendation: LAUNCH WITH CONDITIONS.** Launch once four design changes and supporting safeguards are built and verified. They cut privacy risk from **8 High to 0 High** and keep the app's core value: finding local events.

## Why changes are needed
Texas law treats **precise location** and data revealing **religion, sexuality, or health** as "sensitive data." Processing it requires the user's specific **consent**, and accepting general terms doesn't count (Tex. Bus. & Com. Code §541.001(6), (29); §541.101(b)(4)). As designed, the app tracks location in the background by default, keeps a two-year location trail, puts faith and LGBTQ+ interests into profiles, and **sells device-linked audience segments labeled "anonymous."** The FTC has acted against similar location-for-advertising practices (InMarket, 2024).

## The four changes

| ID | Change | Business trade-off |
|-------|--------------------------------------------------|----------------------------------------------|
| **D-1** | **Contextual ads only.** No audience-segment sales; advertisers get aggregate performance reports | Lower ad revenue per user. Removes the biggest legal and reputational exposure |
| **D-2** | **Background alerts off by default**, specific opt-in, alerts only near saved events | Fewer alert users at launch. Opt-ins are real and defensible |
| **D-3** | **Keep raw location 7 days** (not 24 months), then coarsen | Slightly less recommendation history. Much smaller breach impact |
| **D-4** | **Sensitive categories search-only** unless the user opts in | Minimal. Those categories stay browsable |

**Also required:** unchecked, separate opt-ins; in-app privacy settings plus email requests; honor device opt-out signals; processor contracts (analytics, push, payments); attendee opt-in before organizer marketing; deletable check-ins; a better age screen; and an AI system record for the recommendation engine (Texas AI Governance Act, eff. 2026-01-01).

## Remaining risk (accepted with monitoring)
**3 Medium:** opt-in background location (R-01), 7-day location retention (R-03), and data-warehouse security, which Security must confirm (R-13). **11 Low.** Re-review six months after launch or on any material change.

**Next steps:** (1) Product and Engineering build D-1–D-4 and the safeguards; (2) Legal executes vendor contracts; (3) the privacy analyst verifies the build against the PIA checklist; (4) launch.
