---
title: workflow-orchestrator
url: https://skills.sh/404kidwiz/claude-supercode-skills/workflow-orchestrator
---

# workflow-orchestrator

skills/404kidwiz/claude-supercode-skills/workflow-orchestrator
workflow-orchestrator
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill workflow-orchestrator
SKILL.md
Workflow Orchestrator
Purpose

Provides expertise in designing and implementing durable workflow systems that coordinate complex business processes. Specializes in workflow engines like Temporal and Camunda, saga patterns, and building reliable long-running processes.

When to Use
Designing multi-step business workflows
Implementing saga patterns for distributed transactions
Building with Temporal, Camunda, or similar workflow engines
Handling long-running processes with durability requirements
Coordinating activities across multiple services
Implementing compensation and rollback logic
Building human-in-the-loop approval workflows
Managing state machines for complex processes
Quick Start

Invoke this skill when:

Designing multi-step business workflows
Implementing saga patterns for distributed transactions
Building with Temporal, Camunda, or similar workflow engines
Handling long-running processes with durability requirements
Coordinating activities across multiple services

Do NOT invoke when:

Simple async job processing → use appropriate queue solution
Task distribution for agents → use task-distributor
Event streaming → use event-driven-architect
CI/CD pipelines → use devops-engineer
Decision Framework
Workflow Need?
├── Durable Long-Running → Temporal or durable execution engine
├── Human Tasks → Camunda or process orchestration platform
├── Choreography → Event-driven with eventual consistency
├── Simple Steps → State machine or queue-based
├── Saga Pattern → Orchestrated or choreographed compensations
└── Scheduled Jobs → Cron-based with workflow wrapper

Core Workflows
1. Temporal Workflow Implementation
Define workflow interface and activities
Implement workflow logic with Temporal SDK
Create activity implementations for external calls
Configure retry policies and timeouts
Implement signals and queries for external interaction
Add versioning for workflow updates
Deploy workers and monitor execution
Implement testing with Temporal test framework
2. Saga Pattern Implementation
Identify distributed transaction boundaries
Define forward actions and compensating actions
Choose orchestration (central) or choreography (events)
Implement idempotent operations
Handle partial failures with compensation
Add timeout handling for stuck sagas
Implement observability for saga state
Test failure scenarios thoroughly
3. Human-in-the-Loop Workflow
Design process with human task points
Model workflow with BPMN or similar notation
Implement automated steps as activities
Create task inbox UI for human actions
Add escalation and timeout handling
Implement delegation and reassignment
Add audit trail for compliance
Monitor SLAs for human tasks
Best Practices
Make all activities idempotent for safe retries
Use workflow versioning for production updates
Implement comprehensive compensation for failures
Set appropriate timeouts at each step
Add observability with traces spanning workflow
Design for failure; assume any step can fail
Anti-Patterns
Non-idempotent activities → Design for safe retry
Missing compensations → Plan rollback from the start
Infinite retries → Set max attempts and handle failures
Blocking human tasks → Add timeouts and escalation
Tight coupling → Keep workflows decoupled from activity impl
Weekly Installs
114
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass