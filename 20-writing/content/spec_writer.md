---
title: spec-writer
url: https://skills.sh/jkappers/agent-skills/spec-writer
---

# spec-writer

skills/jkappers/agent-skills/spec-writer
spec-writer
Installation
$ npx skills add https://github.com/jkappers/agent-skills --skill spec-writer
SKILL.md
Spec Writing

Capture WHAT and WHY. Never prescribe HOW.

When invoked with arguments, write a spec for: $ARGUMENTS

Workflow
Gather context: Collect feature description, target users, problem statement, and constraints from user input or $ARGUMENTS. Ask clarifying questions for missing information.
Create directory: specs/feature-name/
Copy assets/spec.md to specs/feature-name/README.md
Complete every section from the Required Sections table below
Validate against the checklist before completing
Required Sections
Section	Content
Feature Overview	2-3 paragraphs: what, who, problem solved
Success Criteria	Measurable outcomes defining "done"
Design Goals	Primary (must) and secondary (nice to have)
User Experience	1-2 paragraphs: interaction, journey
Design Rationale	1-2 paragraphs: why this approach, trade-offs
Constraints/Assumptions	Technical constraints, business assumptions
Functional Requirements	FR-N format, max 6-8, with acceptance criteria
Edge Cases	Unusual inputs, failure scenarios
Acceptance Criteria
- [ ] Given [context], when [action], then [expected result]


Include 2-4 criteria per requirement: happy path + key failure cases.

Scope Check

More than 6-8 requirements = feature too large. Split: identify 3-4 core requirements, flag rest for separate spec in "Scope Notes" section.

Validation Checklist
 Single MVP focus (one deliverable)
 All requirements have testable criteria
 No TODO/TBD placeholders
 Edge cases documented
Exclusions

A spec defines WHAT to build, not HOW to build it. Exclude:

Implementation approach or technical strategy
Architecture diagrams
Code examples
Database schemas
API signatures
Technology or framework choices
Development estimates, timelines, or phase sections
Supporting Files
assets/spec.md - Spec template
references/spec-guide.md - Extended guidance on ADRs and archival
Weekly Installs
13
Repository
jkappers/agent-skills
First Seen
Feb 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass