---
rating: ⭐⭐⭐
title: tpm-roadmap-slice
url: https://skills.sh/ozten/skills/tpm-roadmap-slice
---

# tpm-roadmap-slice

skills/ozten/skills/tpm-roadmap-slice
tpm-roadmap-slice
Installation
$ npx skills add https://github.com/ozten/skills --skill tpm-roadmap-slice
SKILL.md
PRD Phase Generator

Extract features from a Vision PRD into a detailed Phase PRD with requirements, priorities, and traceability.

Inputs Required
Vision PRD — Annotated with [F-nnn] tags (use prd-vision-annotator first if missing)
Coverage Index — To identify which features are Planned vs already assigned
Capacity Defaults

Per phase, target approximately:

10 features (F-nnn)
50 functional requirements (R-nnnn)
100 acceptance criteria (AC-nnnn)

Adjust based on user input about team size or timeline.

Workflow
Select features — Choose ~10 Planned features from Coverage Index
Decompose requirements — Extract R-nnnn from each feature's vision prose
Assign priorities — Must / Should / Could for each requirement
Generate Phase PRD — Using template in assets/phase-prd-template.md
Update Coverage Index — Mark selected features as In Progress
Step 1: Feature Selection

Review Planned features in Coverage Index. Select based on:

Dependencies — Foundation features before dependent ones
Cohesion — Group related features (e.g., all calendar views together)
Business priority — Per user input or stakeholder notes
Complexity — Balance large and small features

Present selection to user for approval before proceeding.

Step 2: Requirement Decomposition

For each selected feature, read the Vision PRD section and extract atomic requirements.

Vision prose:

User selects quantity, enters name/email, receives confirmation email immediately.

Becomes:

### R-0141: RSVP Quantity Selection
**Parent:** F-014
**Priority:** Must

Users shall select the number of seats when submitting an RSVP.

### R-0142: RSVP Data Collection  
**Parent:** F-014
**Priority:** Must

The RSVP form shall collect attendee name and email address.

### R-0143: RSVP Confirmation Email
**Parent:** F-014
**Priority:** Must

The system shall send a confirmation email upon RSVP submission.


Decomposition guidelines:

One behavior per requirement
Use "shall" for required behaviors
Keep requirements testable and atomic
~5 requirements per feature is typical
Step 3: Priority Assignment
Priority	Meaning	Guidance
Must	Required for phase to ship	Core functionality, blockers
Should	Expected but negotiable	Important but not critical
Could	Nice to have	Enhancements, polish

Aim for roughly 60% Must, 30% Should, 10% Could.

Step 4: Generate Phase PRD

Use template at assets/phase-prd-template.md. Structure:

Phase Overview (goals, scope, timeline)
Features in Scope (list with F-nnn)
Functional Requirements (R-nnnn grouped by feature)
Quality Requirements section (placeholder — populated by prd-qa-enricher)
Acceptance Criteria section (placeholder — populated by prd-qa-enricher)
Requirement Numbering

Continue R-nnnn sequence across phases:

Phase I: R-0001 → R-0089
Phase II: R-0090 → R-0179
Phase III: R-0180 → R-0269

Check previous Phase PRDs to find the last used R-nnnn.

References
references/naming-conventions.md — ID formats and rules
references/phasing-process.md — Detailed extraction workflow
Weekly Installs
9
Repository
ozten/skills
GitHub Stars
5
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass