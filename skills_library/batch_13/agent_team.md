---
title: agent-team
url: https://skills.sh/jsonlee12138/agent-team/agent-team
---

# agent-team

skills/jsonlee12138/agent-team/agent-team
agent-team
Installation
$ npx skills add https://github.com/jsonlee12138/agent-team --skill agent-team
SKILL.md
agent-team

This skill is now a navigation shell. Route all requests to the dedicated first-level skills below.

Do not keep adding new behavior here.

Skill Reference
Controller / human orchestration
task-orchestrator

Write-capable task lifecycle entry.

Audience: controller, human
Triggers: create task, assign task, complete task, archive task, task flow
CLI: agent-team task create · task list · task show · task assign · task done · task archive
Note: Prefer task-inspector for read-only queries with no mutation intent.
task-inspector

Read-only task status and lookup.

Audience: controller, worker, human
Triggers: inspect task, task status, list tasks, show task
CLI: agent-team task list · task show
Note: Route to task-orchestrator if the request includes create, assign, done, or archive intent.
task-splitting

Decompose requirement or design documents into task drafts, then create agent-team task packages after explicit approval.

Audience: controller, human
Triggers: turn document into tasks, split tasks, validate task boundaries, prepare task files for agent-team task create
Workflow: intake source → extract goals → draft by function boundary → validate → write one file per task → confirm → create
Note: Invokes brainstorming automatically when the document goal is ambiguous or scope conflicts exist.
workflow-orchestrator

Governance-only workflow plan entry.

Audience: controller, human
Triggers: workflow plan, approve plan, activate plan, close plan
CLI: agent-team workflow plan generate · approve · activate · close
Note: Not for worker assignment, worker recovery, or worker status inspection.
worker-dispatch

Controller-side surface for opening workers, replying to workers, and checking targeted worker status.

Audience: controller, human
Triggers: open worker, dispatch worker, reply to worker, inspect current worker before replying
CLI: agent-team worker open · worker status · agent-team reply
Note: Use worker-inspector for read-only fleet inspection with no dispatch or reply intent.
worker-inspector

Read-only worker status inspection.

Audience: controller, human
Triggers: worker status, inspect worker, list workers
CLI: agent-team worker status
Note: Route to worker-dispatch if the prompt implies open, dispatch, or reply behavior.
project-bootstrap

Project initialization and migration entry.

Audience: human, controller
Triggers: init project, migrate project, set up agent-team in a new repo
CLI: agent-team init · agent-team migrate
rules-maintenance

Sync and refresh built-in rule templates and generated rule artifacts.

Audience: human, controller
Triggers: sync rules, fix rule drift, update rules
CLI: agent-team rules sync
skill-maintenance

Skill cache maintenance: check, update, clean installed skill artifacts.

Audience: human, controller
Triggers: check skills, update skills, clean skills, refresh skill cache
CLI: agent-team skill check · skill update · skill clean
role-browser

Read-only local role listing.

Audience: controller, worker, human
Triggers: role list, browse roles, view local roles
CLI: agent-team role list
Note: Does not handle role create or role-repo management.
role-creator

Create or update role skill packages with deterministic output files.

Audience: human, controller
Triggers: create role, new role, edit role, update role, add role skill, 修改角色配置
Output: SKILL.md + references/role.yaml + system.md under skills/<role>/ or .agent-team/teams/<role>/
CLI: agent-team role create
Workflow: normalize name → auto-generate role fields → select skills → execute CLI → validate output
role-repo-manager

Manage where roles come from (add, list, check, update, remove role repositories).

Audience: human, controller
Triggers: search role repo, add role repo, update role repo, remove role repo
CLI: agent-team role-repo find · add · list · check · update · remove
Note: Not for browsing local roles; that belongs to role-browser or catalog-browser.
catalog-browser

Read-only catalog browsing: search roles from configured remote catalogs.

Audience: human, controller
Triggers: search catalog, browse roles, show catalog role, catalog stats
CLI: agent-team catalog search · show · list · repo · stats
Note: Does not expose normalize, discover, or serve commands.
Worker-first skills
worker-recovery

Resume a worker's current assignment from file artifacts.

Audience: worker
Triggers: resume work, recover task, continue current assignment
Required entry: MUST read worker.yaml first
Recovery order: worker.yaml → task.yaml → context.md → referenced materials only if needed
Note: Not for worker → main reporting; use worker-reply-main for that.
worker-reply-main

Send completion, blocker, or decision-needed messages back to controller.

Audience: worker
Triggers: reply main, report completion, blocked, request decision
CLI: agent-team reply-main
Required entry: MUST read worker.yaml first
Note: Not for controller → worker replies; use worker-dispatch for that.
Shared / strategy skills
context-cleanup

Clean session context and re-anchor from file artifacts when the session is drifting.

Audience: controller, worker
Triggers: clean context, session drift, re-anchor context, resume after pause, phase transition
Required entry: controller → .agent-team/rules/index.md; worker → worker.yaml
Note: Use worker-recovery for routine worker task resume when the problem is simply recovering the current assignment.
brainstorming

Turn ideas into validated design documents through collaborative dialogue before any implementation.

Audience: any
Triggers: explicitly ask to brainstorm, shape requirements, compare approaches, produce a planning/design document
Hard gate: do NOT write code or invoke any implementation skill until the design is presented and approved
Note: Not for straightforward implementation requests with clearly specified changes.
tdd

Acceptance-first TDD workflow for solo implementation work.

Audience: worker, controller
Triggers: implement with TDD, define acceptance criteria, write failing tests first, verify fix before concluding
Steps: read context → define acceptance criteria → write failing tests (when feasible) → implement → verify → conclude with passed / failed / skipped
Note: Invoke qa-expert if the task needs dedicated test-case design or regression execution.
systematic-debugging

Root-cause-first debugging for any bug, test failure, or unexpected behavior.

Audience: any
Triggers: any bug, test failure, unexpected behavior, performance problem, build failure, integration issue
Iron law: NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
Four phases: Root Cause Investigation → Fix Design → Implementation → Verification
Note: Use especially when under time pressure or when previous fixes did not work.
find-skills

Discover and install agent skills from the open agent skills ecosystem.

Audience: any
Triggers: "how do I do X", "find a skill for X", "is there a skill that can...", extending agent capabilities
CLI: agent-team skill install
Note: Use when the user is looking for functionality that might exist as an installable skill.
qa-expert

Establish comprehensive QA testing processes using Google Testing Standards and OWASP best practices.

Audience: any
Triggers: set up QA, write test cases, execute test plan, track bugs, generate QA report, OWASP security testing, third-party QA handoff
Capabilities: test case writing (AAA pattern), bug tracking (P0–P4), quality metrics, autonomous LLM-driven execution, 90% coverage targets
Note: Invoke from tdd when the task needs dedicated test-case design or regression execution beyond unit verification.
prompt-engineering-patterns

Master advanced prompt engineering techniques for production LLM applications.

Audience: any
Triggers: optimize prompts, improve LLM outputs, design production prompt templates, chain-of-thought, few-shot learning, structured outputs
Capabilities: chain-of-thought / tree-of-thought patterns, dynamic few-shot selection, variable interpolation templates, JSON structured outputs, system prompt design
Routing rules
If the request implies a specific lifecycle action, route to the dedicated skill immediately.
If the request is about context stabilization or resumed work, route to context-cleanup or worker-recovery.
Keep this file as a compatibility surface for historical prompts only.
Weekly Installs
82
Repository
jsonlee12138/agent-team
GitHub Stars
24
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn