# Tabletop Exercise Package — "Friday Night Lights Out"

**Organization:** Agarita Family Medicine *(fictional)* · **Exercise type:** discussion-based tabletop, ransomware with data-theft extortion
**Designed by:** Brittany Green (Privacy Analyst) with Claude (facilitator) · **Date designed:** 2026-11-03

> _Independent educational exercise. Fictional organization, people, and data. Not legal advice._

## Files in this package

| File | Audience | When to open |
|--------------------------------------------|----------------|----------------------------------------|
| `README.md` (this file) | Everyone | Before the exercise |
| [`participant-briefing.md`](participant-briefing.md) | Participants | Before the exercise |
| `facilitator-script.md` | **Facilitator only** | **Sealed.** Participants open it **after** the exercise (S7), for the after-action review |
| [`templates/`](templates/): [incident log](templates/incident-log.md), [4-factor worksheet](templates/four-factor-worksheet.md), [notification tracker](templates/notification-tracker.md), [holding statements](templates/holding-statement.md) | Participants | During the exercise |

## Purpose
Practice the clinic's [incident response playbook](../1-incident-response-playbook.md) and [notification matrix](../2-notification-matrix.md) under time pressure, with incomplete information, before a real incident happens.

## Objectives
By the end of the exercise, the team should have:

| # | Objective | Tests |
|-------|--------------------------------------------------------------------------|--------------------|
| O1 | Classified the incident and set the **discovery date** (the HIPAA clock) | Playbook §3, §4.1 |
| O2 | Coordinated containment, evidence, the insurer, law enforcement, and business associates | Playbook §4.2 |
| O3 | Made and **documented** a breach determination (4-factor assessment or presumption) | Playbook §5 |
| O4 | Identified **every** notification duty, recipient, and deadline | Playbook §6; Matrix |
| O5 | Kept communications consistent and accurate | Playbook §8 |
| O6 | Handled new problems that come up during the response | Playbook §3–§4 |

## Format and rules
- **Time is compressed.** About 60 minutes of play covers about 3 weeks of incident time. The facilitator announces each jump ("It is now Tuesday, Day 4…").
- **Injects:** the facilitator delivers new developments one at a time. After each, the Privacy Lead says what they would do and decide.
- **Asking questions:** participants may ask any role a question. The facilitator answers in character **only with facts that role would plausibly know at that moment.** If the answer isn't known yet, the answer is "unknown."
- **No-fault:** the goal is to find gaps in the plan, not to "win." Any answer can be explored.
- **Decisions are recorded** in the exercise record (`../4-exercise-record-and-breach-analysis.md`) with the time and reasoning.
- **Out of bounds:** technical hacking detail, negotiating with the attackers, and laws of states other than Texas (identify those residents, don't analyze their laws).

## Roles

| Role | Played by |
|----------------------------------------------------|------------------------------------------------|
| **Privacy Lead** (Privacy Analyst) | **Brittany.** Makes privacy and notification decisions |
| Incident Commander (IT Manager / Security Officer) | Facilitator, in character |
| Practice Administrator / Privacy Officer | Facilitator, in character |
| Medical Director | Facilitator, in character |
| MSP incident lead (business associate) | Facilitator, in character |
| Breach coach (outside counsel via the insurer) | Facilitator, in character |
| Others as needed (billing company, FBI, reporter, patient) | Facilitator, in character |
| **Facilitator** | **Claude.** Runs the clock, delivers injects, records decisions |

## After the exercise
1. The participant opens `facilitator-script.md` and compares the decisions with the hidden facts and the expected actions.
2. The breach risk assessment is finalized (S8), the notices are drafted (S9), and the after-action report is written (S10).
