---
title: specification-writing
url: https://skills.sh/epicenterhq/epicenter/specification-writing
---

# specification-writing

skills/epicenterhq/epicenter/specification-writing
specification-writing
Installation
$ npx skills add https://github.com/epicenterhq/epicenter --skill specification-writing
SKILL.md
Specification Writing

Follow writing-voice for prose sections.

A specification gives an agent (or human) the context they need to implement a feature autonomously. The goal is NOT to describe everything exhaustively; it's to provide enough initial context that the implementer can do their own research and make informed decisions.

Note: This guide uses [PLACEHOLDER] markers for content you must fill in. Code blocks show templates; replace all bracketed content with your feature's details.

When to Apply This Skill

Use this pattern when you need to:

Plan a feature with a spec that enables autonomous implementation.
Document research findings, trade-offs, and design rationale.
Define phased implementation tasks with trackable checkboxes.
Capture open questions and recommendations without over-prescribing.
Lay out architecture with tables/diagrams instead of wall-of-prose plans.
The Core Philosophy

Specs should:

Provide context, not instructions: Give the "why" and "what", let the implementer figure out "how"
Document research, not conclusions: Show what was explored, what exists, what doesn't
Leave questions open: The Open Questions section is a feature, not a bug
Enable autonomous implementation: An agent reading this should spawn sub-agents to verify and extend

A good spec is a launching pad, not a script to follow.

Document Structure
Header (Required)
# [Feature Name]

**Date**: [YYYY-MM-DD]
**Status**: Draft | In Progress | Implemented
**Author**: [Name or AI-assisted]
**Branch**: [optional: feat/feature-name if work has started]

Overview

One paragraph max. Describe what the feature does. Don't sell it.

## Overview

[One to two sentences describing what this feature adds or changes and what it enables. Be specific about the capability, not vague about benefits.]

Motivation

Structure as Current State → Problems → Desired State.

## Motivation

### Current State

[Show actual code or configuration demonstrating how things work TODAY. Use real code blocks, not prose descriptions.]

This creates problems:

1. **[Problem Title]**: [Specific explanation of what breaks or is painful]
2. **[Problem Title]**: [Specific explanation of what breaks or is painful]

### Desired State

[Brief description of what the target looks like. Can include a code snippet showing the ideal API or structure.]

Research Findings

This is where specs shine. Document what you FOUND, not what you assumed.

## Research Findings

### [Topic Researched]

[Description of what you investigated and methodology]

| [Category]    | [Dimension 1]  | [Dimension 2]    |
| ------------- | -------------- | ---------------- |
| [Project/Lib] | [What they do] | [Their approach] |
| [Project/Lib] | [What they do] | [Their approach] |

**Key finding**: [Your main discovery—could be that no standard exists, or that everyone does X]

**Implication**: [What this means for your design decisions]


Include:

What similar projects do (comparison tables)
What you searched for but didn't find ("No Established Pattern Exists")
Links or references to documentation you consulted
Design Decisions

Use a table for traceability. Every decision should have a rationale.

## Design Decisions

| Decision            | Choice           | Rationale                       |
| ------------------- | ---------------- | ------------------------------- |
| [Decision point]    | [What you chose] | [Why this over alternatives]    |
| [Decision point]    | [What you chose] | [Why this over alternatives]    |
| [Deferred decision] | Deferred         | [Why it's out of scope for now] |

Architecture

Diagrams over prose. Show relationships visually with ASCII art.

## Architecture

[Describe what the diagram shows]


┌─────────────────────────────────────────┐ │ [Component Name] │ │ ├── [field]: [type or value] │ │ └── [field]: [type or value] │ └─────────────────────────────────────────┘ │ ▼ [relationship label] ┌─────────────────────────────────────────┐ │ [Component Name] │ └─────────────────────────────────────────┘

For multi-step flows:

STEP 1: [Step name] ──────────────────── [What happens in this step]

STEP 2: [Step name] ──────────────────── [What happens in this step]

Implementation Plan

Break into phases. Use checkboxes for tracking. Phase 1 should be detailed; later phases can be rougher (the implementer will flesh them out).

## Implementation Plan

### Phase 1: [Phase Name]

- [ ] **1.1** [Specific, atomic task]
- [ ] **1.2** [Specific, atomic task]
- [ ] **1.3** [Specific, atomic task]

### Phase 2: [Phase Name]

- [ ] **2.1** [Higher-level task—implementer will break down]
- [ ] **2.2** [Higher-level task]

Edge Cases

List scenarios that might break assumptions or need special handling.

## Edge Cases

### [Scenario Name]

1. [Initial condition]
2. [What happens]
3. [Expected outcome or "See Open Questions"]

### [Scenario Name]

1. [Initial condition]
2. [What happens]
3. [Expected outcome]

Open Questions

This section signals "you decide this" to the implementer. Include your recommendation but don't close the question.

## Open Questions

1. **[Question about an unresolved design decision]**
   - Options: (a) [Option A], (b) [Option B], (c) [Option C]
   - **Recommendation**: [Your suggestion and why, but explicitly leave it open]

2. **[Another unresolved question]**
   - [Context about why this is uncertain]
   - **Recommendation**: [Suggestion or "Defer until X"]

Success Criteria

How do we know this is done? Checkboxes for verification.

## Success Criteria

- [ ] [Specific, verifiable outcome]
- [ ] [Specific, verifiable outcome]
- [ ] [Tests pass / build succeeds / docs updated]

References

Files that will be touched or consulted.

## References

- `[path/to/file.ts]` - [Why this file is relevant]
- `[path/to/pattern.ts]` - [Pattern to follow or reference]

Good vs Bad Specs
Good Spec Characteristics
Research is documented: Shows what was explored, not just conclusions
Decisions have rationale: Every choice has a "why" in a table
Questions are left open: Implementer has room to decide
Code shows current state: Not described abstractly
Architecture is visual: ASCII diagrams over prose
Phases are actionable: Checkboxes that can be tracked
Bad Spec Characteristics
Prescriptive step-by-step: Reads like a tutorial, no room for autonomy
Assumes without research: "We'll use X" without exploring alternatives
Closes all questions: No Open Questions section
Abstract descriptions: "The system will handle Y" without showing code
Wall of prose: No tables, no diagrams, no structure
Writing for Agent Implementers

When an agent reads your spec, they should:

Understand the problem from Motivation section
Know what's been explored from Research Findings
See the proposed direction from Design Decisions
Have a starting point from Implementation Plan Phase 1
Know what to investigate further from Open Questions

The agent will then:

Spawn sub-agents to verify your research
Explore the Open Questions you left
Flesh out later phases of the implementation plan
Make decisions where you left room

If your spec is too prescriptive, the agent will blindly follow it. If it's too vague, the agent will flounder. The sweet spot is: enough context to start, enough openness to own the implementation.

Quick Reference Checklist
- [ ] Header (Date, Status, Author)
- [ ] Overview (1-2 sentences)
- [ ] Motivation
  - [ ] Current State (with code)
  - [ ] Problems (numbered)
  - [ ] Desired State
- [ ] Research Findings
  - [ ] Comparison tables
  - [ ] Key findings
  - [ ] Implications
- [ ] Design Decisions (table with rationale)
- [ ] Architecture (ASCII diagrams)
- [ ] Implementation Plan (phased checkboxes)
- [ ] Edge Cases
- [ ] Open Questions (with recommendations)
- [ ] Success Criteria
- [ ] References


Not every spec needs every section. A small feature might skip Research Findings. A migration spec might focus heavily on Edge Cases. Use judgment.

Weekly Installs
72
Repository
epicenterhq/epicenter
GitHub Stars
4.5K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass