---
title: adr
url: https://skills.sh/jellydn/my-ai-tools/adr
---

# adr

skills/jellydn/my-ai-tools/adr
adr
Installation
$ npx skills add https://github.com/jellydn/my-ai-tools --skill adr
SKILL.md
Architecture Decision Records (ADR)

Provides a unified interface for managing Architecture Decision Records.

Usage

/adr <ACTION> [ARGUMENTS]

Actions
init [DIRECTORY] - Initialize ADR directory structure
new - Create new ADR with given title
supersede - Create ADR that supersedes existing one
list - List all ADRs in the project
search - Search ADRs by content
view - View specific ADR
help - Show this help
What are ADRs?

Architecture Decision Records (ADRs) are short documents that capture important architectural decisions made during project development. They help teams:

Record the context and reasoning behind decisions
Track the evolution of architectural choices
Onboard new team members
Avoid revisiting already-settled decisions
ADR Structure

Each ADR typically contains:

Title: Brief description of the decision
Status: Proposed, Accepted, Deprecated, Superseded
Context: The situation requiring a decision
Decision: The chosen solution
Consequences: Positive and negative outcomes
ADR Template

A template is available at $SKILL_PATH/templates/adr-template.md:

# [NUMBER]. [TITLE]

Date: [DATE]

## Status

[Proposed | Accepted | Deprecated | Superseded by [ADR-NUMBER]]

## Context

[Describe the context and problem statement]

## Decision

[Describe the decision and solution]

## Consequences

### Positive
- [Positive outcome 1]
- [Positive outcome 2]

### Negative
- [Negative outcome 1]
- [Risk or trade-off]

ADR Directory Detection

Common ADR locations to check:

doc/adr/ (default)
docs/adr/
docs/architecture/decisions/
architecture/decisions/
Process Examples
Create new ADR:
/adr new "Use PostgreSQL for primary database"

List all ADRs:
/adr list

Search ADRs:
/adr search "database"

View specific ADR:
/adr view 5

Weekly Installs
28
Repository
jellydn/my-ai-tools
GitHub Stars
71
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass