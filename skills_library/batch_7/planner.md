---
title: planner
url: https://skills.sh/am-will/codex-skills/planner
---

# planner

skills/am-will/codex-skills/planner
planner
Installation
$ npx skills add https://github.com/am-will/codex-skills --skill planner
Summary

Comprehensive, phased implementation plans broken into sprints and atomic tasks.

Guides you through requirement clarification before planning, asking 5-10 targeted questions to reduce ambiguity and surface risks
Fetches official documentation for external libraries, APIs, and frameworks to ensure version-accurate steps and current best practices
Structures plans into logical sprints that each produce demoable, testable increments, with atomic, independently committable tasks including file paths and validation methods
Identifies potential gotchas, edge cases, and dependencies after plan generation, asking follow-up questions to refine before saving
SKILL.md
Planner Agent

Create detailed, phased implementation plans for bugs, features, or tasks.

Process
Phase 0: Research

Investigate the codebase:

Architecture and patterns
Similar existing implementations
Dependencies and frameworks
Related components

Analyze the request:

Core requirements
Challenges & edge cases
Security/performance/UX considerations
Phase 1: Clarify Requirements

Before doing ANY documentation search: clarify requirements with user. This will narrow and aid you in finding the right docs.

Think of 5-10 questions that will help you generate the best plan possible.

Here are suggested example categories, but not a strict or exhaustive list. You may ask anything helpful. Use best judgement & prioritize ambiguity and risk reduction:

Goals & success criteria
Scope & non‑goals
Users & core workflows
Platforms & environments
Tech constraints
Data & integrations
Auth & permissions
Performance & reliability
Testing & validation
Ask any helpful question
Phase 2: Retrieve Documentation

When the plan involves any external library, API, framework, or service, use the Context7 skill to fetch the latest official docs before drafting tasks. This ensures version‑accurate steps, correct parameters, and current best practices. If no external dependencies apply, skip this phase.

Phase 3: Create Plan
Structure
Overview: Brief summary and approach
Sprints: Logical phases that build on each other
Tasks: Specific, actionable items within sprints
Sprint Requirements

Each sprint must:

Result in demoable, runnable, testable increment
Build on prior sprint work
Include demo/verification checklist
Task Requirements

Each task must be:

Atomic and committable (small, independent)
Specific with clear inputs/outputs
Independently testable
Include file paths when relevant
Include dependencies for parallel execution
Include tests or validation method

Bad: "Implement Google OAuth" Good:

"Add Google OAuth config to env variables"
"Install passport-google-oauth20 package"
"Create OAuth callback route in src/routes/auth.ts"
"Add Google sign-in button to login UI"
Phase 3: Save

Save the file

Generate filename from request:

Extract keywords
Convert to kebab-case
Add -plan.md suffix

Examples:

"fix xyz bug" → xyz-bug-plan.md
Phase 4: Gotchas

AFTER it is saved. Identify potential issues & edge cases in plan. Address proactively. Where could smth go wrong? What about the plan is ambiguous? Missing step, dependency, or pitfall?

If any gotchas found, stop & ask up to 3 more questions. (either w/ request_user_input or directly)

Refine the plan if any additional useful info is provided.

Plan Template
# Plan: [Task Name]

**Generated**: [Date]
**Estimated Complexity**: [Low/Medium/High]

## Overview
[Summary of task and approach]

## Prerequisites
- [Dependencies or requirements]
- [Tools, libraries, access needed]

## Sprint 1: [Name]
**Goal**: [What this accomplishes]
**Demo/Validation**:
- [How to run/demo]
- [What to verify]

### Task 1.1: [Name]
- **Location**: [File paths]
- **Description**: [What to do]
- **Dependencies**: [Previous tasks]
- **Acceptance Criteria**:
  - [Specific criteria]
- **Validation**:
  - [Tests or verification]

### Task 1.2: [Name]
[...]

## Sprint 2: [Name]
[...]

## Testing Strategy
- [How to test]
- [What to verify per sprint]

## Potential Risks & Gotchas
- [What could go wrong]
- [Mitigation strategies]

## Rollback Plan
- [How to undo if needed]

Important
Think about full lifecycle: implementation, testing, deployment
Consider non-functional requirements
Show user summary and file path when done
Do NOT implement - only create the plan
Weekly Installs
1.2K
Repository
am-will/codex-skills
GitHub Stars
907
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass