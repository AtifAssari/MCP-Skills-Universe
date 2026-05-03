---
rating: ⭐⭐⭐
title: product-specs-writer
url: https://skills.sh/ncklrs/startup-os-skills/product-specs-writer
---

# product-specs-writer

skills/ncklrs/startup-os-skills/product-specs-writer
product-specs-writer
Installation
$ npx skills add https://github.com/ncklrs/startup-os-skills --skill product-specs-writer
SKILL.md
Product Specs Writer

Comprehensive product documentation expertise — from strategic PRDs to implementation-ready specifications that engineering teams can actually build from.

Philosophy

Great product specs bridge the gap between vision and execution. They're not bureaucratic documents; they're communication tools that align teams and prevent expensive misunderstandings.

The best product specifications:

Start with the why — Context before requirements
Are testable — Every requirement has clear acceptance criteria
Anticipate questions — Edge cases, errors, and constraints documented upfront
Evolve with the product — Living documents, not static artifacts
Respect the reader — Engineers, designers, and stakeholders can all understand them
How This Skill Works

When invoked, apply the guidelines in rules/ organized by:

prd-* — Product Requirements Documents, vision, scope
stories-* — User stories, personas, jobs-to-be-done
criteria-* — Acceptance criteria, definition of done
technical-* — Technical specifications, architecture decisions
api-* — API specifications, contracts, versioning
edge-* — Edge cases, error handling, failure modes
design-* — Design handoff, component specs, interactions
rollout-* — Feature flags, rollout plans, experiments
metrics-* — Success metrics, KPIs, measurement plans
maintenance-* — Documentation lifecycle, versioning, deprecation
Core Frameworks
Specification Hierarchy
┌─────────────────────────────────────────┐
│              VISION                     │  ← Why are we building this?
│         (Problem & Opportunity)         │
├─────────────────────────────────────────┤
│               PRD                       │  ← What are we building?
│      (Requirements & Constraints)       │
├─────────────────────────────────────────┤
│          USER STORIES                   │  ← Who benefits and how?
│       (Personas & Journeys)             │
├─────────────────────────────────────────┤
│      ACCEPTANCE CRITERIA                │  ← How do we know it's done?
│      (Testable Conditions)              │
├─────────────────────────────────────────┤
│      TECHNICAL SPECS                    │  ← How do we build it?
│   (Architecture & Implementation)       │
└─────────────────────────────────────────┘

Document Types by Audience
Document	Primary Audience	Purpose	Update Frequency
PRD	Leadership, PM, Design	Align on what and why	Per milestone
User Stories	Engineering, QA	Define scope and value	Per sprint
Acceptance Criteria	QA, Engineering	Define done	Per story
Technical Spec	Engineering	Define how	Per feature
API Spec	Frontend, External devs	Define contracts	Per version
Design Handoff	Engineering	Define UI/UX	Per component
Rollout Plan	Engineering, Ops	Define deployment	Per release
Success Metrics	Leadership, Data	Define success	Per quarter
The INVEST Criteria (User Stories)
Criteria	Question	Example
Independent	Can it be built alone?	No dependencies on unfinished stories
Negotiable	Is scope flexible?	Details can be refined with engineering
Valuable	Does user benefit?	Clear value proposition stated
Estimable	Can we size it?	Enough detail to estimate effort
Small	Fits in a sprint?	Can be completed in 1-5 days
Testable	Can we verify it?	Has clear acceptance criteria
Specification Completeness Checklist
PRD Completeness:
├── Problem Statement         □ Clearly defined user pain
├── Success Metrics          □ Measurable outcomes defined
├── User Stories             □ All personas covered
├── Scope                    □ In-scope and out-of-scope clear
├── Constraints              □ Technical and business limits stated
├── Dependencies             □ External dependencies identified
├── Risks                    □ Known risks and mitigations
├── Timeline                 □ Milestones and deadlines set
└── Open Questions           □ Unknowns explicitly listed

Technical Spec Completeness:
├── Architecture             □ System design documented
├── Data Model               □ Schema and relationships defined
├── API Contracts            □ Endpoints and payloads specified
├── Edge Cases               □ Failure modes documented
├── Security                 □ Auth, encryption, compliance covered
├── Performance              □ SLAs and benchmarks defined
├── Monitoring               □ Observability strategy clear
└── Rollback Plan            □ Recovery procedures documented

Error Handling Taxonomy
Error Type	Example	Documentation Required
Validation	Invalid email format	Error message, field highlighting
Authorization	User lacks permission	Error state, escalation path
Resource	Item not found	Empty state, recovery action
System	Database timeout	Retry strategy, user feedback
Business Logic	Insufficient balance	Error explanation, next steps
External	Third-party API down	Fallback behavior, degraded mode
Specification Templates
Minimal PRD Structure
# Feature: [Name]

## Problem
What user problem are we solving?

## Solution
High-level approach (1-2 paragraphs)

## Success Metrics
- Primary: [Metric] from X to Y
- Secondary: [Metric] from X to Y

## User Stories
- As a [user], I want [goal] so that [benefit]

## Scope
**In scope:** [List]
**Out of scope:** [List]

## Open Questions
- [ ] Question 1
- [ ] Question 2

User Story Template
**As a** [persona/user type]
**I want** [capability/action]
**So that** [benefit/value]

**Acceptance Criteria:**
- Given [context], when [action], then [result]
- Given [context], when [action], then [result]

**Edge Cases:**
- What if [edge case]? Then [behavior]

**Out of Scope:**
- [Explicit exclusion]

Anti-Patterns
Spec by committee — Over-collaboration produces vague documents
Premature optimization — Specifying implementation details too early
Missing the why — Requirements without context for decisions
Kitchen sink scope — Trying to solve everything in one release
One-way documentation — Specs that don't get updated as learnings emerge
Assumption blindness — Not documenting implicit assumptions
Designer/Engineer telephone — No direct communication, only docs
Success theater — Metrics chosen because they're easy, not meaningful
Spec as contract — Treating specs as unchangeable legal documents
Documentation debt — Outdated specs worse than no specs
Weekly Installs
85
Repository
ncklrs/startup-os-skills
GitHub Stars
18
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass