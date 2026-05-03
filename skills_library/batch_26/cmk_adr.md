---
title: cmk:adr
url: https://skills.sh/commandosslabs/ai-devkit/cmk:adr
---

# cmk:adr

skills/commandosslabs/ai-devkit/cmk:adr
cmk:adr
Installation
$ npx skills add https://github.com/commandosslabs/ai-devkit --skill cmk:adr
SKILL.md
ADR
Intents
We decided to use event sourcing over CRUD for the audit trail — record that as an ADR

Record an ADR: chose Redis over Memcached for session caching because of pub/sub support

Update ADR-0003 — we revisited the decision and switched from REST to gRPC

Document why we chose Kafka over RabbitMQ

What architecture decisions have we recorded?

References

Read references/adr-conventions.md for placement rules and references/adr-template.md for section structure.

Scope

ADRs are for system-level decisions that affect multiple features or core architecture. Feature-scoped decisions belong in the feature spec.md under Technical Decisions.

Workflow: Create
Gather decision context from conversation/docs/links.
Validate scope is system-wide (not feature-scoped).
Place at the repository's existing ADR path, or fallback: docs/adrs/{NNNN}-{decision-title}.md. Determine {NNNN} by scanning existing ADRs and incrementing (start at 0001 if none exist).
Fill template from references/adr-template.md (or local template if present).
Set status to proposed.
Workflow: Iterate
Read the existing ADR in full.
Upstream check: If docs/system-design.md exists, check whether the revised decision conflicts with current architecture. Warn the user if so.
Identify what changed and why.
Update in place: revise decision/rationale, update alternatives and consequences, note what shifted.
Update Last updated date.
Transition status: proposed → accepted when team agrees. accepted stays accepted when decision evolves.
Output
Create: complete ADR file using canonical naming
Iterate: update in place with current decision and rationale
Decision statement is clear and implementable
Alternatives section is always present with concrete trade-offs
Consequences section is always present with short-term and long-term impact
If decision changed, rationale explains what shifted
Weekly Installs
12
Repository
commandosslabs/ai-devkit
GitHub Stars
3
First Seen
Mar 9, 2026