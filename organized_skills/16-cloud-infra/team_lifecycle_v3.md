---
rating: ⭐⭐
title: team-lifecycle-v3
url: https://skills.sh/catlog22/claude-code-workflow/team-lifecycle-v3
---

# team-lifecycle-v3

skills/catlog22/claude-code-workflow/team-lifecycle-v3
team-lifecycle-v3
Installation
$ npx skills add https://github.com/catlog22/claude-code-workflow --skill team-lifecycle-v3
SKILL.md
Team Lifecycle v3

Enhanced lifecycle: specification → implementation → testing → review with parallel execution, conditional routing, and dynamic specialist role injection.

Purpose

Team Lifecycle v3 orchestrates multi-agent software development workflows from initial requirements through implementation, testing, and review. It automatically coordinates specialized agents, manages artifact dependencies, validates quality gates, and dynamically injects expert roles based on task complexity.

Key Capabilities:

Parallel execution of independent tasks
Dynamic specialist role injection (security, performance, data, devops, ML)
Artifact-based validation gating
Conditional routing based on complexity assessment
Priority-based task scheduling (P0/P1/P2)
Quality checkpoints with user feedback loops
Problem Statement

Complex software development tasks require diverse expertise—security audits, performance optimization, data pipeline design, DevOps configuration, and ML model integration. Coordinating multiple specialized agents manually is error-prone, inefficient, and difficult to scale. Developers face several challenges:

Manual Coordination Overhead: Tracking dependencies between agents, ensuring artifacts are validated before downstream work begins, and managing parallel execution requires constant human oversight.

Expertise Gaps: Not all tasks require all specialists. Injecting the right expert roles at the right time based on task complexity and keywords is a manual, subjective process prone to under- or over-staffing.

Quality Assurance Bottlenecks: Without automated quality gates and validation checkpoints, defects propagate downstream, requiring expensive rework.

Lack of Observability: Understanding where a multi-agent workflow is stalled, which artifacts are blocking progress, and what actions are needed requires manual inspection of scattered state.

Team Lifecycle v3 solves these problems by providing an event-driven orchestration system that automatically manages agent coordination, artifact validation, specialist injection, and quality checkpoints—turning multi-agent workflows into a repeatable, observable, and scalable process.

Goals
Automated Agent Coordination: Spawn workers based on task dependencies, manage parallel execution, and handle completion callbacks without manual intervention.
Artifact-Based Validation Gating: Block downstream work until upstream artifacts pass validation, preventing defect propagation.
Dynamic Specialist Injection: Analyze task descriptions and complexity to automatically inject expert roles (security, performance, data, devops, ML) when needed.
Conditional Routing: Route tasks to appropriate implementation strategies (direct, orchestrated, architecture-first) based on quantifiable complexity assessment.
Priority-Based Scheduling: Execute critical-path tasks (P0) before dependent tasks (P1/P2), optimizing workflow throughput.
Quality Checkpoints: Pause at key milestones for user review, with actionable commands (resume, improve, revise, recheck) to maintain quality.
Session Persistence: Support pause/resume across process restarts, preserving artifact registry and task state.
Observability: Provide clear status reporting, task state visibility, and actionable error messages.
Non-Goals
General-Purpose Workflow Engine: Team Lifecycle v3 is specialized for software development workflows with agent coordination. It is not a generic DAG executor or distributed job scheduler.
Project Management Tool: The system does not manage backlogs, sprints, or roadmaps. It executes individual tasks with clear requirements.
Prescriptive Agent Implementations: The skill defines role specifications and contracts but does not mandate specific agent implementations or tools.
Ticket/PR Management: State transitions, comments, and PR creation are the responsibility of individual agents using their own tools, not the orchestrator.
Approval/Sandbox Policies: The skill does not enforce specific approval workflows or sandboxing. Implementations may add these based on their trust model.
Real-Time Collaboration: The system is event-driven with asynchronous agent execution, not a real-time collaborative editing environment.
Mandatory Reading

Before using this skill, read these documents to understand the foundational concepts:

Document	Purpose	Priority
specs/core-concepts.md	Foundational principles: team-worker architecture, artifact contracts, quality gating, dynamic role injection, priority scheduling	P0 - Critical
specs/artifact-contract-spec.md	Artifact manifest schema and validation rules	P0 - Critical
specs/execution-flow.md	End-to-end execution walkthrough with pipeline definitions	P1 - High
Documentation Structure

This skill is organized into the following directories:

/roles - Agent Role Specifications
coordinator/: Orchestrator agent that manages workflow, task dependencies, and role injection
role.md: Coordinator specification
commands/: User command handlers (dispatch, monitor)
pipeline/: Core pipeline roles (always present)
analyst.md, writer.md, planner.md, executor.md, tester.md, reviewer.md
architect.md, fe-developer.md, fe-qa.md (consulting roles)
specialists/: Specialist roles (dynamically injected)
orchestrator.role.md, security-expert.role.md, performance-optimizer.role.md
data-engineer.role.md, devops-engineer.role.md, ml-engineer.role.md
/specs - Specifications and Standards
core-concepts.md: Foundational principles (mandatory reading)
execution-flow.md: End-to-end execution walkthrough
artifact-contract-spec.md: Artifact manifest schema
quality-gates.md: Quality validation criteria
document-standards.md: Document formatting standards
team-config.json: Role registry and pipeline definitions
/templates - Document Templates
product-brief.md: DRAFT-001 template
requirements-prd.md: DRAFT-002 template
architecture-doc.md: DRAFT-003 template
epics-template.md: DRAFT-004 template
/subagents - Utility Subagents
discuss-subagent.md: 3-round discussion protocol
explorer-subagent.md: Shared exploration with cache
doc-generator-subagent.md: Template-based doc generation
Quick Start
Basic Usage
Skill(skill="team-lifecycle-v3", args="<task description>")


Example:

Skill(skill="team-lifecycle-v3", args="Implement user authentication with OAuth2")

Execution Flow
User provides task description → Coordinator clarifies requirements
Coordinator creates team → TeamCreate with session folder
Coordinator analyzes complexity → Injects specialist roles if needed
Coordinator creates task chain → Based on pipeline selection (spec-only, impl-only, full-lifecycle)
Coordinator spawns first batch → Workers execute in background
Workers report completion → SendMessage callback to coordinator
Coordinator advances pipeline → Spawns next ready tasks
Quality checkpoints → User can review, improve, or revise
Coordinator generates report → Final summary and completion action
User Commands

During execution, you can use these commands:

Command	Action
check / status	View current execution status
resume / continue	Advance to next step
revise <TASK-ID> [feedback]	Revise specific task with feedback
feedback <text>	Provide feedback for targeted revision
recheck	Re-run quality check
improve [dimension]	Auto-improve weakest quality dimension
Pipeline Options

The coordinator selects the appropriate pipeline based on task requirements:

Spec-only Pipeline (6 tasks)
RESEARCH-001 → DRAFT-001 → DRAFT-002 → DRAFT-003 → DRAFT-004 → QUALITY-001


Use for: Documentation, requirements gathering, design work

Impl-only Pipeline (4 tasks)
PLAN-001 → IMPL-001 → TEST-001 + REVIEW-001


Use for: Quick implementations with clear requirements

Full-lifecycle Pipeline (10 tasks)
[Spec pipeline] → PLAN-001 → IMPL-001 → TEST-001 + REVIEW-001


Use for: Complete feature development from requirements to implementation

Advanced Features
Dynamic Role Injection

Specialist roles are automatically injected based on keywords in task description:

security, vulnerability, OWASP → security-expert
performance, optimization, bottleneck → performance-optimizer
data, pipeline, ETL, schema → data-engineer
devops, CI/CD, deployment, docker → devops-engineer
ML, model, training, inference → ml-engineer
Conditional Routing

PLAN-001 assesses complexity and routes to appropriate implementation strategy:

Low complexity (1-2 modules) → Direct implementation
Medium complexity (3-4 modules) → Orchestrated parallel implementation
High complexity (5+ modules) → Architecture design + orchestrated implementation
Quality Checkpoints

At key milestones, the coordinator pauses for user review:

Spec Phase Complete (QUALITY-001): Review specification quality, choose to proceed, improve, or revise
Implementation Complete: Review code quality and test coverage
Troubleshooting
Common Issues
Issue	Solution
Pipeline stalled	Use status to check task states, resume to advance
Quality gate failed	Use improve to auto-improve or revise <TASK-ID> to manually fix
Wrong specialist injected	Provide clearer keywords in task description
Session lost after restart	Use session resume to restore from .workflow/.team/TLS-*
Error Handling
Scenario	Resolution
Unknown command	Error with available command list
Role spec file not found	Error with expected path
Artifact validation fails	Block downstream, trigger fix loop
Dynamic role injection fails	Log warning, continue with core roles
Parallel merge timeout	Report stall, prompt user intervention
Reference Documents

For detailed information, see:

specs/core-concepts.md - Foundational principles
specs/execution-flow.md - Detailed execution walkthrough
specs/artifact-contract-spec.md - Artifact manifest specification
specs/quality-gates.md - Quality validation criteria
specs/document-standards.md - Document formatting standards
roles/coordinator/role.md - Coordinator specification
roles/README.md - Role directory guide
Weekly Installs
10
Repository
catlog22/claude…workflow
GitHub Stars
1.9K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass