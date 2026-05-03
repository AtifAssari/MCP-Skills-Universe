---
title: 032-architecture-adr-non-functional-requirements
url: https://skills.sh/jabrena/cursor-rules-java/032-architecture-adr-non-functional-requirements
---

# 032-architecture-adr-non-functional-requirements

skills/jabrena/cursor-rules-java/032-architecture-adr-non-functional-requirements
032-architecture-adr-non-functional-requirements
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 032-architecture-adr-non-functional-requirements
SKILL.md
Create ADRs for Non-Functional Requirements

Guide stakeholders through a structured conversation to uncover and document architectural decisions for quality attributes using the ISO/IEC 25010:2023 quality model. This is an interactive SKILL. The ADR documents the outcome of the conversation, not the conversation itself. Act as an architecture consultant: challenge-first, consultative, adaptive.

What is covered in this Skill?

Challenge-first opening: ISO 25010:2023 quality characteristics (Functional Suitability, Performance Efficiency, Compatibility, Reliability, Security, Maintainability, Flexibility, Safety)
Understanding the challenge: drivers, constraints, system context
Quality-specific deep dive tailored to primary NFR category
Solution exploration and trade-off preferences
Decision synthesis and validation before ADR creation
ADR document generation with Quality Metrics & Success Criteria
Constraints

Use challenge-first, consultative discovery—ask 1-2 questions at a time, build on answers, tailor to NFR category. Only create ADR after thorough conversation and user confirmation.

MANDATORY: Run date before starting to get accurate timestamps for the ADR
MUST: Read the reference template fresh—do not use cached questions
MUST: Start with challenge-first opening (ISO 25010:2023 quality characteristics)
MUST: Ask one or two questions at a time; never all at once
MUST: Validate summary with user (Does this accurately capture your quality needs?) before proposing ADR creation
MUST: Wait for user to confirm proceed before generating the ADR
When to use this skill
Create ADR for Non-functional requirements
Document Non-functional requirements
Capture Non-functional requirements
Generate Non-functional requirements in an ADR
Workflow
Get current date

Run date before discovery and use it for ADR timestamps.

Read reference and open with quality challenge

Read references/032-architecture-adr-non-functional-requirements.md and begin with the challenge-first ISO 25010:2023 quality characteristics framing.

Run consultative NFR discovery

Ask one or two questions at a time to capture drivers, constraints, quality priorities, options, and trade-off preferences tailored to the primary NFR category.

Step constraints:

Never ask all discovery questions at once
Validate summary with user before proposing ADR generation
Generate ADR after explicit confirmation

Only after user confirms proceed, create the ADR including measurable Quality Metrics and Success Criteria.

Reference

For detailed guidance, examples, and constraints, see references/032-architecture-adr-non-functional-requirements.md.

Weekly Installs
56
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass