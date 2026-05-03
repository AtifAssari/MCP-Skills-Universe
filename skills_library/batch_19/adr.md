---
title: adr
url: https://skills.sh/ncklrs/startup-os-skills/adr
---

# adr

skills/ncklrs/startup-os-skills/adr
adr
Installation
$ npx skills add https://github.com/ncklrs/startup-os-skills --skill adr
SKILL.md
Architecture Decision Records

Expert guidance for creating and managing Architecture Decision Records based on Olaf Zimmermann's research and the MADR (Markdown Architectural Decision Records) methodology.

How This Skill Works

When invoked, this skill guides you through the full ADR lifecycle:

Readiness assessment — Evaluate whether a decision is ready to be recorded (START criteria)
Creation — Write well-structured ADRs using the MADR template with anti-pattern avoidance
Quality evaluation — Check completeness using the ECADR "Definition of Done" criteria
Lifecycle management — Maintain ADR logs, supersede outdated records, track decision status
Core Philosophy

"Don't decide too early, this harms flexibility. Don't decide too late either."

ADRs function as decision journals — not blueprints or policies. They capture the rationale behind architecturally significant choices: the problem context, the alternatives considered, the criteria applied, and the consequences accepted. Good ADRs are executive summaries that balance tradeoffs, not sales pitches for a predetermined outcome.

When to Use This Skill
Creating a new ADR for an architectural decision
Evaluating whether a decision is ready to be recorded
Reviewing an existing ADR for completeness and quality
Writing or customizing a MADR template for a project
Assessing whether a requirement is architecturally significant
Managing an ADR log (superseding, deprecating, linking decisions)
Training teams on ADR best practices
Command Modes
Argument	Action
create	Walk through creating a new ADR interactively
review	Evaluate an existing ADR against quality criteria
check-ready	Assess decision readiness using START criteria
check-done	Assess ADR completeness using ECADR criteria
template	Output a blank MADR template ready to fill in
list	Help organize and maintain an ADR log
(no args)	General ADR guidance based on context
The MADR Template (Quick Reference)
# ADR-NNNN: [Short Title Describing Decision]

## Status
[proposed | accepted | deprecated | superseded by ADR-XXXX]

## Date
YYYY-MM-DD

## Decision Makers
[Who made or approved this decision]

## Context and Problem Statement
[1-3 paragraphs: What is the issue? Why does it matter?
Frame as a question when possible.]

## Decision Drivers
- [Driver 1: quality attribute, business constraint, or technical concern]
- [Driver 2]
- [Driver 3]

## Considered Options
1. [Option A — the chosen option]
2. [Option B]
3. [Option C]

## Decision Outcome
Chosen option: "[Option A]", because [justification referencing decision drivers].

### Consequences
- Good, because [positive consequence]
- Good, because [another benefit]
- Bad, because [accepted tradeoff]
- Bad, because [known limitation]

## Pros and Cons of Options

### Option A
- Good, because [advantage]
- Bad, because [disadvantage]

### Option B
- Good, because [advantage]
- Bad, because [disadvantage]

### Option C
- Good, because [advantage]
- Bad, because [disadvantage]

## Validation
[How will we verify this decision works? Code review, design review,
architectural fitness function, spike, etc.]

## More Information
[Links to related ADRs, RFCs, spikes, or external references.
Note confidence level and planned review date.]

Key Frameworks
START — Definition of Ready

Before writing an ADR, confirm all five criteria:

Stakeholders known and available
Timing is the Most Responsible Moment
Alternatives identified (minimum two)
Requirements and context documented
Template selected and instantiated
ECADR — Definition of Done

Before marking an ADR as accepted, confirm all five criteria:

Evidence that the design will work
Criteria applied to compare at least two alternatives
Agreement from relevant stakeholders
Documentation captured and shared
Realization and review plan scheduled
ASR Test — Architectural Significance

A requirement warrants an ADR when it scores on these criteria:

High business impact or risk
Critical stakeholder concern
Quality-of-service deviation from current architecture
External dependency that is unpredictable or uncontrollable
Cross-cutting concern affecting multiple components
First-of-a-kind implementation for the team
Historical precedent of causing problems
What This Skill Provides
Readiness assessment using START criteria with checklists
MADR template generation (full and minimal variants)
Anti-pattern detection in draft ADRs (11 known anti-patterns)
Quality evaluation using ECADR Definition of Done
Architectural significance assessment for prioritizing decisions
Lifecycle guidance for maintaining ADR logs over time
Weekly Installs
55
Repository
ncklrs/startup-os-skills
GitHub Stars
18
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass