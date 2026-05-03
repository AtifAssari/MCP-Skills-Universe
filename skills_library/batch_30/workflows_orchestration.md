---
title: workflows-orchestration
url: https://skills.sh/7spade/black-tortoise/workflows-orchestration
---

# workflows-orchestration

skills/7spade/black-tortoise/workflows-orchestration
workflows-orchestration
Installation
$ npx skills add https://github.com/7spade/black-tortoise --skill workflows-orchestration
SKILL.md
Workflows Orchestration
Intent

Implement multi-step processes as explicit application workflows that coordinate capabilities via events, not via direct imports.

Workflow Model
A workflow is a state machine: explicit states, transitions, and terminal states.
Keep transitions deterministic and driven by events/commands.
Where Logic Lives
Workflow coordination lives in the Application layer (stores/use cases).
Domain invariants stay in Domain; do not encode rules in UI components.
Event-Driven Coordination
Workflows subscribe to events to advance state.
Publish events only after persistence (append-before-publish).
Concurrency
Choose explicit concurrency semantics for async operations (cancel, queue, ignore).
Avoid parallel append/publish operations that break causal ordering.
Observability
Include correlation IDs so a whole workflow run can be traced end-to-end.
Weekly Installs
8
Repository
7spade/black-tortoise
First Seen
Feb 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass