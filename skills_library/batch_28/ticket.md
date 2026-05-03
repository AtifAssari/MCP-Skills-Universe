---
title: ticket
url: https://skills.sh/cygnusfear/agent-skills/ticket
---

# ticket

skills/cygnusfear/agent-skills/ticket
ticket
Installation
$ npx skills add https://github.com/cygnusfear/agent-skills --skill ticket
SKILL.md
Ticket — Artifact Creation

All skill output that needs to persist goes into a ticket. No custom directories.

Tag Taxonomy

Every artifact ticket MUST use the appropriate tags:

Artifact type	Tags	Example title
Oracle research	research, oracle	"Oracle: Why API latency spiked"
Delphi investigation (epic)	research, delphi	"Delphi: Database migration strategy"
Delphi synthesis	research, delphi-synthesis	"Delphi synthesis: Database migration strategy"
Implementation plan	plan	"Plan: Refactor auth middleware"
Architecture decision	decision	"ADR: Use Zustand for state management"
Postmortem	postmortem	"Postmortem: Agent skipped codebase exploration"
Code review	review	"Review: PR #42 auth changes"
Design spec	design-spec	"Design spec: Dashboard redesign"
Creating Artifact Tickets

Use tk (via todos_oneshot or todos tool):

todos_oneshot(
  title: "Oracle: <topic>",
  description: "<full findings>",
  tags: "research,oracle",
  type: "task"
)

Epics with Subtasks

For multi-part artifacts (e.g. Delphi = N oracles + synthesis):

Create the epic ticket first
Create subtask tickets linked to it
Use teams delegate to run subtasks in parallel
Update the epic with synthesized results
# 1. Epic
todos_oneshot(title: "Delphi: <topic>", tags: "research,delphi", type: "epic")

# 2. Subtasks (one per oracle)
todos_oneshot(title: "Oracle 1: <topic>", tags: "research,oracle", type: "task")
todos_oneshot(title: "Oracle 2: <topic>", tags: "research,oracle", type: "task")
todos_oneshot(title: "Oracle 3: <topic>", tags: "research,oracle", type: "task")

# 3. teams delegate to run in parallel
# 4. Synthesize into epic

Rules
No custom output directories. No .oracle/, .plans/, .design-specs/, docs/postmortems/, docs/research/.
Tags are mandatory. Every artifact ticket uses tags from the taxonomy above.
Titles are descriptive. Prefix with artifact type (Oracle:, Plan:, ADR:, etc.).
Full content in the ticket. The ticket body IS the artifact — not a pointer to a file elsewhere.
Link related tickets. Subtasks link to epics. Plans link to implementation tickets. Postmortems link to the incident tickets.
Weekly Installs
27
Repository
cygnusfear/agent-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass