---
title: prd
url: https://skills.sh/scando1993/sugar/prd
---

# prd

skills/scando1993/sugar/prd
prd
Installation
$ npx skills add https://github.com/scando1993/sugar --skill prd
SKILL.md
PRD Generator

Create detailed Product Requirements Documents that are clear, actionable, and suitable for implementation by AI agents or junior developers.

The Job
Receive a feature description from the user
Ask 3-5 essential clarifying questions (with lettered options for quick responses like "1A, 2C, 3B")
Generate a structured PRD based on answers
Save to tasks/prd-[feature-name].md

Do NOT implement anything. Just document requirements.

Clarifying Questions

Ask only critical questions where the initial prompt is ambiguous:

1. What is the primary goal of this feature?
   A. Option one
   B. Option two
   C. Other: [please specify]

2. Who is the target user?
   A. New users only
   B. All users
   C. Admin users

PRD Structure
1. Introduction/Overview

Brief description of the feature and the problem it solves.

2. Goals

Specific, measurable objectives (bullet list).

3. User Stories

Each story needs:

Title: Short descriptive name
Description: "As a [user], I want [feature] so that [benefit]"
Acceptance Criteria: Verifiable checklist (not vague)

Format:

### US-001: [Title]
**Description:** As a [user], I want [feature] so that [benefit].

**Acceptance Criteria:**
- [ ] Specific verifiable criterion
- [ ] Another criterion
- [ ] Typecheck/lint passes


Each story must be completable in one focused AI agent pass. If too big, split it.

4. Functional Requirements

Numbered: "FR-1: The system must allow users to..."

5. Non-Goals (Out of Scope)

What this feature will NOT include.

6. Technical Considerations (Optional)

Known constraints, dependencies, integration points.

7. Success Metrics

How success is measured.

8. Open Questions

Remaining unknowns.

Story Sizing (Critical)

Right-sized:

Add a database column and migration
Add a UI component to an existing page
Update a server action with new logic

Too big (split these):

"Build the entire dashboard"
"Add authentication"
"Refactor the API"

Rule of thumb: If you cannot describe the change in 2-3 sentences, it is too big.

Output
Format: Markdown
Location: tasks/prd-[feature-name].md
Weekly Installs
11
Repository
scando1993/sugar
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass