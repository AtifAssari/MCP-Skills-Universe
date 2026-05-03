---
rating: ⭐⭐⭐
title: planning-jira-task
url: https://skills.sh/b-mendoza/agent-skills/planning-jira-task
---

# planning-jira-task

skills/b-mendoza/agent-skills/planning-jira-task
planning-jira-task
Installation
$ npx skills add https://github.com/b-mendoza/agent-skills --skill planning-jira-task
SKILL.md
Planning Jira Task

Plan exactly how to execute one task from the task plan for a Jira ticket. This orchestrator does three things: think (interpret summaries and plan state), decide (choose the next planning dispatch or re-plan path), and dispatch (hand execution-heavy work to co-located subagents). The planning artifacts live on disk; the orchestrator keeps only concise summaries in context.

Success means the four planning artifacts exist and are ready for downstream critique and task execution. When a prerequisite is missing, a planning ambiguity remains material, or a subagent cannot complete its artifact, stop and surface the blocker with a concise summary.

Inputs
Input	Required	Example
TICKET_KEY	Yes	JNS-6065
TASK_NUMBER	Yes	3
RE_PLAN	No	true
DECISIONS_FILE	No	docs/JNS-6065-task-3-decisions.md

Read ./references/data-contracts.md when you need the upstream prerequisites or downstream artifact expectations.

Use RE_PLAN and DECISIONS_FILE only for critique-driven reruns. Read ./references/pipeline.md when deciding which stages to rerun.

Pipeline Stages
execution-prepper validates the task and writes the execution brief.
execution-planner inspects the codebase and writes the execution plan.
test-strategist writes the behavior-driven test specification.
refactoring-advisor writes the refactoring recommendation.
The skill returns only a concise planning summary and the artifact paths needed for downstream critique and task execution.
Subagent Registry
Subagent	Path	Purpose
execution-prepper	./subagents/execution-prepper.md	Validate task readiness and assemble the execution brief
execution-planner	./subagents/execution-planner.md	Inspect the codebase and write the implementation plan
test-strategist	./subagents/test-strategist.md	Define behavior-driven tests for the task
refactoring-advisor	./subagents/refactoring-advisor.md	Recommend only the refactoring needed for this task

Read a subagent definition only when you are about to dispatch that subagent.

Output Contract

This skill writes only workflow-planning artifacts that capture planning state for this task:

Artifact	Produced by	Consumed by
docs/<TICKET_KEY>-task-<TASK_NUMBER>-brief.md	execution-prepper	All downstream planning subagents, downstream critique, task execution
docs/<TICKET_KEY>-task-<TASK_NUMBER>-execution-plan.md	execution-planner	Downstream critique, task execution
docs/<TICKET_KEY>-task-<TASK_NUMBER>-test-spec.md	test-strategist	Downstream critique, task execution
docs/<TICKET_KEY>-task-<TASK_NUMBER>-refactoring-plan.md	refactoring-advisor	Downstream critique, task execution

On a successful run, all four files exist. On a re-plan, overwrite only the files owned by the subagents that are re-run. These workflow-state documents stay on disk for the life of the workflow and are never committed to git.

Dispatch Rules
Read ./references/data-contracts.md when checking prerequisites or artifact expectations.
Read ./references/pipeline.md when running the standard planning pipeline or a critique-driven re-plan.
At each boundary, validate that the current required input exists before dispatch: the task plan and task section for execution-prepper, then the prior-stage artifacts for later subagents. Confirm that the expected output artifact was written before advancing.
Pass only the explicit handoffs required for the current stage: task identity inputs for execution-prepper, plus RE_PLAN and DECISIONS_FILE on critique-driven reruns; then prior-stage artifact paths and DECISIONS_FILE when applicable for later stages.
Keep only verdicts, file paths, and next-step-relevant notes from each subagent.
Advance sequentially. Rerun only the subagents invalidated by critique, plus their downstream dependents.
Surface blockers and pause for resolution when ambiguity remains.
Reference Guide

This table tells you which reference to load. ## Orchestration Steps remains the source of truth for the actual pipeline order.

Situation	Reference file	Purpose
Standard planning run	./references/pipeline.md	Dispatch order, handoffs, and success criteria
Re-plan after critique	./references/pipeline.md	Targeted rerun rules and retry limit
Contract questions	./references/data-contracts.md	Upstream prerequisites and downstream consumers
Orchestration Steps
Read ./references/data-contracts.md and confirm the task-plan prerequisites exist for TICKET_KEY and TASK_NUMBER.
Read ./references/pipeline.md.
Use ./references/pipeline.md to determine the next required subagent. On a standard run, start with execution-prepper. On a critique-driven re-plan, start at the earliest invalidated stage. Pass only that subagent's required explicit inputs. For execution-prepper, pass only TICKET_KEY, TASK_NUMBER, and when applicable RE_PLAN and DECISIONS_FILE. For later stages, pass the artifact file paths required by ./references/pipeline.md.
Retain only its verdict, artifact path, and the notes needed for the next decision.
Continue until all required planning artifacts are written and confirmed, or a blocker is surfaced.
Report completion with the task number and title, all four artifact paths, one or two sentences on the recommended approach, the number or shape of tests specified, and the refactoring verdict.
Example
Dispatch execution-prepper with TICKET_KEY, TASK_NUMBER
Subagent returns: PREP: PASS Brief: docs/JNS-6065-task-2-brief.md
Dispatch execution-planner with BRIEF_FILE=docs/JNS-6065-task-2-brief.md
Subagent returns: PLAN: PASS Execution plan: docs/JNS-6065-task-2-execution-plan.md
Dispatch test-strategist with BRIEF_FILE=docs/JNS-6065-task-2-brief.md and PLAN_FILE=docs/JNS-6065-task-2-execution-plan.md
Subagent returns: TEST_SPEC: PASS Spec: docs/JNS-6065-task-2-test-spec.md
Dispatch refactoring-advisor with BRIEF_FILE=docs/JNS-6065-task-2-brief.md, PLAN_FILE=docs/JNS-6065-task-2-execution-plan.md, and TEST_SPEC_FILE=docs/JNS-6065-task-2-test-spec.md
Subagent returns: REFACTORING: PASS Refactoring plan: docs/JNS-6065-task-2-refactoring-plan.md
Tell the user: "Task 2 - Add webhook retry handling planning complete. Artifacts: brief, execution plan, test spec, and refactoring plan written. Recommended approach: add retry orchestration in the webhook service, then thread retry state through the worker path. Tests: 3 behavior groups with 6 high-priority checks. Refactoring verdict: Refactor during implementation."

The orchestrator keeps only those summaries and the artifact paths.

Weekly Installs
24
Repository
b-mendoza/agent-skills
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass