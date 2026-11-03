# Scenario — Mesquite Lantern Co. and the "Lantern Local" app

> **FICTIONAL ORGANIZATION AND PRODUCT.** Mesquite Lantern Co. and the Lantern Local app are invented for this exercise. Every detail (company, people, features, vendors, numbers) is made up. On 2026-11-03, web searches found no existing company named "Mesquite Lantern" and no app named "Lantern Local."

_Disclaimer: independent educational exercise. Fictional organization and data. Not legal advice._

## 1. Company profile (fictional)

| Item | Value |
|------|-------|
| Company | Mesquite Lantern Co. (privately held startup) |
| Headquarters | Texas (generic; no real address) |
| Size | About 40 employees |
| Product | **Lantern Local**, a free mobile app (iOS and Android) for finding local events |
| Business model | Free to users. Revenue from **in-app ads** sold to local businesses and from a share of ticket sales |
| Launch plan | Texas launch in four metro areas (Austin, Dallas–Fort Worth, Houston, San Antonio), with about 100,000 users expected in year one |
| Privacy function | One privacy analyst (my role), reporting to the General Counsel. No dedicated privacy team yet |

## 2. The request

The product team plans to launch Lantern Local next quarter. The General Counsel requires a **privacy impact assessment (PIA)** before launch and has asked the privacy analyst for:

1. A **data inventory** of all personal data the app collects, creates, or shares
2. A **data-flow map** showing where that data goes
3. A **PIA report** with risks, mitigations, residual risk ratings, and a launch recommendation
4. A **one-page summary** for the leadership team

## 3. Users

| User group | In scope? | Notes |
|------------|-----------|-------|
| Adults 18+ in Texas | **Yes** | The only intended users |
| Under 18 | **No, by design** | The app is 18+. **How the age limit is enforced is part of the review.** |
| Users outside Texas | Out of scope for this PIA | The launch is Texas-only. The PIA notes this as a scope limit. |
| Business advertisers | Yes, as recipients of data | Local businesses that buy ads |
| Event organizers | Yes, as recipients of data | Venues and promoters who list events |

## 4. Planned features (product team's design, before privacy review)

| # | Feature | What it does | Personal data involved (types) |
|---|---------|--------------|--------------------------------|
| F-1 | Account sign-up | Email or "Sign in with Google/Apple" | Name, email, account ID, date of birth (age gate) |
| F-2 | Events near me | Shows events near the user's current location | **Precise geolocation** (foreground) |
| F-3 | "Heads-up" alerts | Notifies users when they're near an event they might like, even when the app is closed | **Precise geolocation in the background**, push token |
| F-4 | Interest profile | Learns what users like from taps, saves, and check-ins | Interests and inferred preferences, activity history |
| F-5 | Check-ins | Users check in at events to earn badges | Attendance history (places and times) |
| F-6 | Tickets | Buy tickets in the app through a third-party payment processor | Purchase history, payment handled by the processor |
| F-7 | Local ads | Ads from local businesses, targeted by location and interests | Location, interests, device advertising ID |
| F-8 | Audience insights for advertisers | Advertisers get reports on who saw or acted on their ads, and the product team wants to offer **audience segments** (e.g., "live-music fans near downtown Austin") | Aggregated or segmented user data |
| F-9 | Analytics and crash reporting | Third-party software development kits (SDKs) inside the app | Device data, app usage events, IP address |
| F-10 | Share with organizers | Organizers see who bought tickets or checked in | Name, email, attendance |

**Third parties (fictional, described by role only):** a cloud hosting provider, a payment processor, an analytics SDK provider, an advertising network, a push-notification service, and event organizers.

## 5. Stated assumptions (Brittany, 2026-11-03)
- **Texas Data Privacy and Security Act applies in full.** For this exercise, Mesquite Lantern Co. is assumed **not** to qualify as a small business under U.S. Small Business Administration definitions, so the exemption in Tex. Bus. & Com. Code §541.002(a)(3) [S01] does not apply. SBA size standards were not analyzed. (If it did qualify, §541.107 would still require consent before selling sensitive data [S01].)
- **Report structure:** the PIA follows the data protection assessment elements in §541.105(b) [S01] (benefits vs. risks, de-identified data, consumer expectations, context, relationship). The nine FIPPs [S07] are the risk lens.

## 6. Out of scope
- Users outside Texas, and laws of other states (noted as a limit)
- Employee data and internal HR systems
- Detailed security testing (the PIA records security controls as described by engineering)
- Contract negotiation with vendors (the PIA recommends terms only)

## 7. Review standards
Named here only. Each will be registered with a URL and access date in S2.
- **Texas Data Privacy and Security Act** (Texas consumer privacy law)
- **FTC Act Section 5** (unfair or deceptive practices) and FTC guidance on location data and advertising
- **Fair Information Practice Principles (FIPPs)**
- **Report structure:** Tex. Bus. & Com. Code §541.105(b) data protection assessment elements (decided S2; see §5)

## 8. Roles

| Role | Who | Responsibility |
|------|-----|----------------|
| Privacy analyst | Brittany Green, playing the Mesquite Lantern analyst | Maps the data, assesses the risks, and makes the calls on risk ratings and the launch recommendation |
| General Counsel | Fictional; receives the PIA | Makes the company's launch decision |
| Product and Engineering | Fictional; provide feature details | Answer questions about how features work |
| Drafting support | Claude (AI assistant) | Drafts options and explanations. Ratings stay marked "PROPOSED" until Brittany confirms them. |
