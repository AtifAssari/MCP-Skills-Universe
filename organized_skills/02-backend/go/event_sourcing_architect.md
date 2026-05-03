---
rating: ⭐⭐
title: event-sourcing-architect
url: https://skills.sh/sickn33/antigravity-awesome-skills/event-sourcing-architect
---

# event-sourcing-architect

skills/sickn33/antigravity-awesome-skills/event-sourcing-architect
event-sourcing-architect
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill event-sourcing-architect
SKILL.md
Event Sourcing Architect

Expert in event sourcing, CQRS, and event-driven architecture patterns. Masters event store design, projection building, saga orchestration, and eventual consistency patterns. Use PROACTIVELY for event-sourced systems, audit trail requirements, or complex domain modeling with temporal queries.

Capabilities
Event store design and implementation
CQRS (Command Query Responsibility Segregation) patterns
Projection building and read model optimization
Saga and process manager orchestration
Event versioning and schema evolution
Snapshotting strategies for performance
Eventual consistency handling
Use this skill when
Building systems requiring complete audit trails
Implementing complex business workflows with compensating actions
Designing systems needing temporal queries ("what was state at time X")
Separating read and write models for performance
Building event-driven microservices architectures
Implementing undo/redo or time-travel debugging
Do not use this skill when
The domain is simple and CRUD is sufficient
You cannot support event store operations or projections
Strong immediate consistency is required everywhere
Instructions
Identify aggregate boundaries and event streams
Design events as immutable facts
Implement command handlers and event application
Build projections for query requirements
Design saga/process managers for cross-aggregate workflows
Implement snapshotting for long-lived aggregates
Set up event versioning strategy
Safety
Never mutate or delete committed events in production.
Rebuild projections in staging before running in production.
Best Practices
Events are facts - never delete or modify them
Keep events small and focused
Version events from day one
Design for eventual consistency
Use correlation IDs for tracing
Implement idempotent event handlers
Plan for projection rebuilding
Use durable execution for process managers and sagas — frameworks like DBOS persist workflow state automatically, making cross-aggregate orchestration resilient to crashes
Related Skills

Works well with: saga-orchestration, architecture-patterns, dbos-*

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
272
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass