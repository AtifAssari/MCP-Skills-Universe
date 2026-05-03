---
title: task-coordination-strategies
url: https://skills.sh/wshobson/agents/task-coordination-strategies
---

# task-coordination-strategies

skills/wshobson/agents/task-coordination-strategies
task-coordination-strategies
Installation
$ npx skills add https://github.com/wshobson/agents --skill task-coordination-strategies
Summary

Decompose complex tasks, design dependency graphs, and coordinate multi-agent work with structured task descriptions.

Provides four decomposition strategies: by architectural layer, functional component, cross-cutting concern, or file ownership to parallelize work effectively
Includes dependency graph patterns (independent, sequential, diamond) with principles for minimizing chain depth and identifying critical paths
Offers task description template covering objective, owned files, requirements, interface contracts, acceptance criteria, and scope boundaries
Supplies workload monitoring indicators and rebalancing steps to detect imbalances and reassign tasks across agent teams
SKILL.md
Task Coordination Strategies

Strategies for decomposing complex tasks into parallelizable units, designing dependency graphs, writing effective task descriptions, and monitoring workload across agent teams.

When to Use This Skill
Breaking down a complex task for parallel execution
Designing task dependency relationships (blockedBy/blocks)
Writing task descriptions with clear acceptance criteria
Monitoring and rebalancing workload across teammates
Identifying the critical path in a multi-task workflow
Task Decomposition Strategies
By Layer

Split work by architectural layer:

Frontend components
Backend API endpoints
Database migrations/models
Test suites

Best for: Full-stack features, vertical slices

By Component

Split work by functional component:

Authentication module
User profile module
Notification module

Best for: Microservices, modular architectures

By Concern

Split work by cross-cutting concern:

Security review
Performance review
Architecture review

Best for: Code reviews, audits

By File Ownership

Split work by file/directory boundaries:

src/components/ — Implementer 1
src/api/ — Implementer 2
src/utils/ — Implementer 3

Best for: Parallel implementation, conflict avoidance

Dependency Graph Design
Principles
Minimize chain depth — Prefer wide, shallow graphs over deep chains
Identify the critical path — The longest chain determines minimum completion time
Use blockedBy sparingly — Only add dependencies that are truly required
Avoid circular dependencies — Task A blocks B blocks A is a deadlock
Patterns

Independent (Best parallelism):

Task A ─┐
Task B ─┼─→ Integration
Task C ─┘


Sequential (Necessary dependencies):

Task A → Task B → Task C


Diamond (Mixed):

        ┌→ Task B ─┐
Task A ─┤          ├→ Task D
        └→ Task C ─┘

Using blockedBy/blocks
TaskCreate: { subject: "Build API endpoints" }         → Task #1
TaskCreate: { subject: "Build frontend components" }    → Task #2
TaskCreate: { subject: "Integration testing" }          → Task #3
TaskUpdate: { taskId: "3", addBlockedBy: ["1", "2"] }  → #3 waits for #1 and #2

Task Description Best Practices

Every task should include:

Objective — What needs to be accomplished (1-2 sentences)
Owned Files — Explicit list of files/directories this teammate may modify
Requirements — Specific deliverables or behaviors expected
Interface Contracts — How this work connects to other teammates' work
Acceptance Criteria — How to verify the task is done correctly
Scope Boundaries — What is explicitly out of scope
Template
## Objective
Build the user authentication API endpoints.

## Owned Files
- src/api/auth.ts
- src/api/middleware/auth-middleware.ts
- src/types/auth.ts (shared — read only, do not modify)

## Requirements
- POST /api/login — accepts email/password, returns JWT
- POST /api/register — creates new user, returns JWT
- GET /api/me — returns current user profile (requires auth)

## Interface Contract
- Import User type from src/types/auth.ts (owned by implementer-1)
- Export AuthResponse type for frontend consumption

## Acceptance Criteria
- All endpoints return proper HTTP status codes
- JWT tokens expire after 24 hours
- Passwords are hashed with bcrypt

## Out of Scope
- OAuth/social login
- Password reset flow
- Rate limiting

Workload Monitoring
Indicators of Imbalance
Signal	Meaning	Action
Teammate idle, others busy	Uneven distribution	Reassign pending tasks
Teammate stuck on one task	Possible blocker	Check in, offer help
All tasks blocked	Dependency issue	Resolve critical path first
One teammate has 3x others	Overloaded	Split tasks or reassign
Rebalancing Steps
Call TaskList to assess current state
Identify idle or overloaded teammates
Use TaskUpdate to reassign tasks
Use SendMessage to notify affected teammates
Monitor for improved throughput
Weekly Installs
4.7K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass