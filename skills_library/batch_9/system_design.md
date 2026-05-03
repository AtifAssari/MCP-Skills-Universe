---
title: system-design
url: https://skills.sh/s-hiraoku/synapse-a2a/system-design
---

# system-design

skills/s-hiraoku/synapse-a2a/system-design
system-design
Installation
$ npx skills add https://github.com/s-hiraoku/synapse-a2a --skill system-design
SKILL.md
System Design

Guide architectural decisions and produce structured design artifacts.

When to Use
Designing a new system or major feature from scratch
Evaluating trade-offs between architectural approaches
Creating Architecture Decision Records (ADRs)
Reviewing existing architecture for scalability, reliability, or maintainability concerns
Decomposing a monolith or planning a migration
Workflow
Step 1: Clarify Requirements

Before designing, gather:

Functional requirements - What must the system do?
Non-functional requirements - Performance, availability, security, cost constraints
Scope boundaries - What is explicitly out of scope?
Existing constraints - Current tech stack, team skills, timeline

Ask the user to clarify any ambiguous requirements before proceeding.

Step 2: Identify Components

Break the system into components:

Data stores - What data exists? How is it accessed?
Services / modules - What are the logical units of work?
Interfaces - How do components communicate? (API, events, shared DB, files)
External dependencies - Third-party services, APIs, infrastructure
Step 3: Evaluate Alternatives

For each significant decision, document at least 2 options:

Criterion	Option A	Option B
Complexity	...	...
Scalability	...	...
Operational cost	...	...
Team familiarity	...	...

Recommend one option with clear reasoning.

Step 4: Produce Design Artifact

Output a structured design document:

# Design: <Title>

## Context
[Problem statement and motivation]

## Requirements
- Functional: ...
- Non-functional: ...

## Architecture
[Component diagram or description]

## Key Decisions
| Decision | Choice | Rationale |
|----------|--------|-----------|
| ... | ... | ... |

## Data Model
[Schema or entity relationships]

## API Surface
[Key endpoints or interfaces]

## Risks & Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
| ... | ... | ... |

## Open Questions
- ...

Step 5: Review Checklist

Before finalizing, verify:

 Single responsibility per component
 No circular dependencies between modules
 Failure modes identified and handled
 Data consistency model is explicit (strong vs eventual)
 Security boundaries are defined
 Observability points (logging, metrics, tracing) are planned
Principles
Start simple - Add complexity only when requirements demand it
Make trade-offs explicit - Every choice has a cost; document it
Design for change - Interfaces should be stable; implementations should be replaceable
Separate concerns - Data, logic, and presentation should not be entangled
Fail gracefully - Design for partial failures, not just the happy path
Weekly Installs
82
Repository
s-hiraoku/synapse-a2a
GitHub Stars
4
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass