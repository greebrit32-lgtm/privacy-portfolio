# System Description — Lantern Local (as designed by the product team, pre-review)

**Status:** DRAFT (S3, 2026-11-03). This is the **fictional** product team's design as submitted for privacy review. It describes what the team *plans*, including choices the PIA may recommend changing. Nothing here is a finding.

_Fictional company, product, vendors, and data. Data is described by **type** only. Not legal advice._

## 1. Systems

| ID | System | Operated by | Notes |
|----|--------|-------------|-------|
| SYS-1 | Lantern Local mobile app (iOS, Android) | Mesquite Lantern | Collects user input and device signals |
| SYS-2 | Lantern API and user database | Mesquite Lantern, hosted by a **cloud hosting provider** (processor) | Accounts, preferences, check-ins, location history |
| SYS-3 | Recommendation engine | Mesquite Lantern | Builds the interest profile from activity and location |
| SYS-4 | Data warehouse | Mesquite Lantern, on the cloud host | Copies of app data for analytics and the advertiser reports |
| SYS-5 | Advertiser portal | Mesquite Lantern | Local businesses buy ads, view reports, and (as planned) buy **audience segments** |
| SYS-6 | Organizer portal | Mesquite Lantern | Event organizers list events and see ticket buyers and check-ins |
| TP-1 | Analytics and crash-reporting SDK | Third-party **analytics provider** | Embedded in the app |
| TP-2 | Advertising SDK and ad network | Third-party **advertising network** | Embedded in the app. Serves ads, measures clicks, and uses the device advertising ID |
| TP-3 | Push-notification service | Third-party **push provider** (processor) | Delivers alerts |
| TP-4 | Payment processor | Third-party **payment processor** | Handles card data. Mesquite Lantern receives a payment token and receipt |
| TP-5 | Event organizers | Independent businesses | Receive ticket-buyer and check-in data |
| TP-6 | Advertisers | Independent local businesses | Receive ad reports and (as planned) audience segments |

## 2. Data elements (types)

| ID | Data element (type) | Source | Collected by feature | Systems and recipients |
|----|---------------------|--------|----------------------|------------------------|
| DE-01 | Name | User | F-1 | SYS-1, SYS-2, SYS-4, SYS-6, TP-5 |
| DE-02 | Email address | User or sign-in provider | F-1 | SYS-1, SYS-2, SYS-4, SYS-6, TP-5 |
| DE-03 | Account ID (internal) | Generated | F-1 | SYS-2, SYS-3, SYS-4, TP-1 |
| DE-04 | Date of birth | User (self-declared) | F-1 (age gate) | SYS-1, SYS-2 |
| DE-05 | Sign-in provider identifier (Google/Apple) | Sign-in provider | F-1 | SYS-2 |
| DE-06 | Password (stored hashed) | User | F-1 | SYS-2 |
| DE-07 | Precise geolocation, **foreground** | Device GPS | F-2 | SYS-1, SYS-2, SYS-3, SYS-4 |
| DE-08 | Precise geolocation, **background** (every 15 minutes) | Device GPS | F-3 | SYS-1, SYS-2, SYS-3, SYS-4 |
| DE-09 | Location history (stored trail of DE-07/DE-08) | Derived | F-2, F-3, F-4 | SYS-2, SYS-3, SYS-4 |
| DE-10 | Push-notification token | Device | F-3 | SYS-2, TP-3 |
| DE-11 | Selected interests (e.g., live music, food, sports) | User | F-4 | SYS-2, SYS-3, SYS-4 |
| DE-12 | **Inferred interests and profile** | Derived (SYS-3) | F-4, F-7, F-8 | SYS-3, SYS-4, SYS-5, TP-2, TP-6 |
| DE-13 | In-app activity (views, taps, saves, searches) | App (SYS-1, TP-1) | F-4, F-9 | SYS-1, SYS-3, SYS-4, TP-1 |
| DE-14 | Check-in / attendance history (event, place, time) | User action plus location | F-5 | SYS-2, SYS-3, SYS-4, SYS-6, TP-5 |
| DE-15 | Ticket purchase history | User action | F-6 | SYS-2, SYS-4, SYS-6, TP-4, TP-5 |
| DE-16 | Payment card data | User → TP-4 only | F-6 | TP-4 |
| DE-17 | Device advertising ID | Device | F-7, F-9 | SYS-1, SYS-4, TP-1, TP-2, TP-6 |
| DE-18 | Device information (model, OS, app version) | Device | F-9 | SYS-2, TP-1, TP-2 |
| DE-19 | IP address | Network | F-9 (and all requests) | SYS-2, TP-1, TP-2 |
| DE-20 | Crash and diagnostic logs | Device | F-9 | TP-1 |
| DE-21 | Audience segment membership | Derived (SYS-4) | F-8 | SYS-4, SYS-5, TP-6 |
| DE-22 | Ad interaction data (impressions, clicks) | TP-2 | F-7, F-8 | SYS-4, SYS-5, TP-2 |
| DE-23 | Permission and preference records (location permission state, marketing opt-in, ad-tracking choice) | Device / user | F-1, F-2, F-3, F-7 | SYS-1, SYS-2 |
| DE-24 | Coarse location (neighborhood or metro area, derived from DE-07/DE-08) | Derived (SYS-3) | F-7, F-8 | SYS-3, SYS-4, SYS-5, TP-2 |

**Event categories (design detail):** events are tagged with categories including *Faith & Spirituality*, *Pride & LGBTQ+*, *Community & Politics*, and *Health & Wellness Support Groups*, alongside music, food, and sports. Check-ins (DE-14) and inferred interests (DE-12) inherit these categories.

## 3. Feature-by-feature design

| Feature | What is collected, and when | Purpose (as stated by product team) | Where it goes | Retention (as proposed) | Notice / choice (as designed) |
|---------|-----------------------------|-------------------------------------|---------------|-------------------------|-------------------------------|
| **F-1 Account sign-up** | DE-01–06, DE-23 at sign-up | Create an account; keep under-18 users out | SYS-2 | Until account deletion | One screen: enter date of birth (under 18 blocked); one checkbox, "I agree to the Terms and Privacy Policy"; **marketing email box pre-checked** |
| **F-2 Events near me** | DE-07 each time the app is opened; stored to DE-09 | Show nearby events | SYS-1 → SYS-2 → SYS-3, SYS-4 | **Location history kept 24 months** "to improve recommendations" | OS prompt "Allow while using the app" on first open |
| **F-3 Heads-up alerts** | DE-08 every 15 minutes, app closed; DE-10 | Alert users near events they might like | SYS-2 → SYS-3; TP-3 gets token and message | Same as DE-09 (24 months) | Onboarding screen 3: "Get alerts about events near you" → OS "Always allow" prompt. **On by default in the onboarding flow** |
| **F-4 Interest profile** | DE-11, DE-12, DE-13, DE-09 continuously | Personalize recommendations | SYS-3, SYS-4 | Profile kept while the account exists; rebuilt nightly | Described in the privacy policy only |
| **F-5 Check-ins** | DE-14 when the user taps "Check in" (location verified) | Badges and streaks | SYS-2, SYS-4; shared with organizer (F-10) | **No deletion planned** (badges are permanent) | In-app button |
| **F-6 Tickets** | DE-15; DE-16 goes to TP-4 only | Sell tickets; revenue share | SYS-2; TP-4; organizer (F-10) | 7 years (accounting) | Checkout screen; processor's terms linked |
| **F-7 Local ads** | DE-17, DE-22; ad requests include DE-12 interest categories and **DE-24 coarse location** (derived from DE-07/08) | Show relevant local ads; ad revenue | TP-2 (ad network, embedded SDK) | Per ad-network terms (not reviewed) | iOS ad-tracking prompt (Apple requirement); on Android, no in-app prompt. Privacy policy says ads are "personalized" |
| **F-8 Audience insights** | DE-21 built from DE-09, DE-12, DE-14, DE-24 | Advertiser reports; **sell audience segments** such as "live-music fans near downtown Austin" | SYS-4 → SYS-5 → TP-6 (advertisers) | Segments refreshed weekly; advertisers keep what they download | Not described to users yet. Product team considers segments "anonymous" because they contain hashed advertising IDs instead of names |
| **F-9 Analytics and crash reporting** | DE-13, DE-17, DE-18, DE-19, DE-20 | Product analytics, debugging | TP-1 (SDK) | Analytics provider default (not reviewed) | Privacy policy only |
| **F-10 Share with organizers** | DE-01, DE-02, DE-14, DE-15 for that organizer's events | Let organizers manage attendance and market future events | SYS-6 → TP-5 | Organizers keep data under their own policies | Privacy policy says data is shared "with event partners" |

## 4. Design choices flagged for the PIA
These are the product team's choices most likely to drive findings. They are listed here so the inventory and risk sessions examine them. No conclusions yet.

1. **Background location (F-3) on by default**, collected every 15 minutes, and stored as a 24-month location history (DE-09).
2. **Sensitive event categories** (faith, LGBTQ+, politics, health support) flow into check-ins, inferred interests, and audience segments.
3. **Audience segments sold to advertisers (F-8)**, described internally as "anonymous" because they use hashed advertising IDs.
4. **Single "agree to Terms and Privacy Policy" checkbox** at sign-up. Marketing opt-in pre-checked.
5. **Ad network and analytics SDKs** receive location-derived data and device IDs. Their retention and onward use were not reviewed.
6. **Age gate** relies on a self-declared date of birth.
7. **No deletion** for check-in history. Organizers and advertisers keep downloaded data under their own policies.
8. **Opt-out of targeted ads / sale:** only a web form linked from the privacy policy. No in-app setting at launch.
