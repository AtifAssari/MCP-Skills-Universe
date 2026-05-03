---
rating: ⭐⭐
title: creating-jira-subtasks
url: https://skills.sh/b-mendoza/agent-skills/creating-jira-subtasks
---

# creating-jira-subtasks

skills/b-mendoza/agent-skills/creating-jira-subtasks
creating-jira-subtasks
Installation
$ npx skills add https://github.com/b-mendoza/agent-skills --skill creating-jira-subtasks
SKILL.md
Creating Jira Subtasks

Create or reconcile Jira subtasks for a clarified task plan at docs/<TICKET_KEY>-tasks.md. This skill coordinates Phase 4 by dispatching one specialist subagent, keeping only its structured summary, and reporting the outcome the parent workflow needs for progress tracking.

The orchestrator does four things directly: read its bundled files, derive identifiers from JIRA_URL, dispatch subtask-creator, and relay the subagent's summary. Plan parsing, Jira operations, and plan-file edits all stay inside subtask-creator after dispatch.

Inputs
Input	Required	Example
JIRA_URL	Yes	https://workspace.atlassian.net/browse/PROJ-123

Derive these values from the URL when you need to describe the ticket:

Workspace: subdomain before .atlassian.net
Project: prefix before the dash in the ticket key
Ticket key: full path segment, such as PROJ-123

Prefer passing the full JIRA_URL downstream rather than only TICKET_KEY. The URL carries the workspace context needed for Jira reads and writes.

Workflow Overview
1. Read the subtask-creator definition
2. Dispatch it with JIRA_URL
3. Interpret its structured result
4. Report only the concise phase summary to the caller

Subagent Registry

Read a subagent definition only when you are about to dispatch it.

Subagent	Path	Purpose
subtask-creator	./subagents/subtask-creator.md	Reconcile the clarified plan with Jira and return a structured Phase 4 summary
How This Skill Works

This skill is intentionally narrow. The parent workflow is responsible for Phase 4 gating and progress tracking; this skill assumes the Phase 3 approval step has already happened before Jira writes begin.

Inside Phase 4, keep only the routing verdicts plus the caller-facing rollup. For Jira, that means the parent / artifact identifiers, creation totals, warnings or failures, and the linkage rollup the caller needs for progress tracking. Jira stays on the single native subtask path, so no write-model or capability metadata is expected in the summary.

Relay only the structured fields the subagent returns. Raw Jira payloads, full API responses, raw file contents, and intermediate parse details stay inside subtask-creator unless the user explicitly asks for them.

Phase 4 Contract

Primary artifact:

docs/<TICKET_KEY>-tasks.md


For the complete standalone input contract, output contract, and summary-field definitions, read ./references/phase-4-io-contracts.md.

That bundled reference file is the only normative Phase 4 contract source for this skill. SKILL.md covers dispatch, routing, and reporting only. The subagent defines how to achieve the contract but does not replace it.

Execution Steps
1. Dispatch subtask-creator

Read ./subagents/subtask-creator.md, then dispatch it with:

JIRA_URL

The subagent owns plan parsing, Jira-capable tool discovery, parent lookup, idempotent reuse of existing subtask links, sequential creation of missing subtasks, plan-file updates, and post-write validation.

2. Interpret the structured result

Handle the returned summary this way:

SUBTASKS: PASS with Validation: PASS: report success and proceed.
SUBTASKS: WARN with Validation: PASS: report partial success or degraded input clearly. Phase 4 may still be usable if the plan file now satisfies the local Phase 4 output contract, but make failed tasks visible so the user can retry before executing them.
SUBTASKS: BLOCKED: stop and relay the artifact or data-shape problem. This usually means the plan is missing, malformed, or contains unsafe existing Jira links that need manual correction.
SUBTASKS: FAIL: stop and relay the fatal Jira or validation failure.
SUBTASKS: ERROR: stop and relay the unexpected failure.
Any result paired with Validation: FAIL: treat the phase as incomplete even if some Jira writes succeeded, because the local plan contract is not trustworthy yet.
Any result paired with Validation: NOT_RUN: treat the phase as incomplete; no trustworthy local post-write artifact was produced for downstream use.
3. Report only the summary

Using only the subagent's structured summary, tell the caller:

Use the subagent summary as routing input; do not rewrite its contract schema inside SKILL.md.
Surface the caller-facing rollup: parent reference, explicit TICKET_KEY, updated plan-file path, creation totals, warnings or failures, and the reminder that no implementation has started.
Do not add GitHub-style write-model or capability lines to the Jira report.

Dispatch subtask-creator as a subagent. If the environment cannot invoke subagents, report the skill as blocked rather than reproducing the subagent inline.

Example

Read ./subagents/subtask-creator.md

Dispatch subtask-creator with JIRA_URL

Subagent returns the contract-defined summary from ./references/phase-4-io-contracts.md, for example:

SUBTASKS: PASS Validation: PASS Parent: PROJ-123 TICKET_KEY: PROJ-123 Plan file: docs/PROJ-123-tasks.md ...

Route on that summary, then relay only the caller-facing rollup. Do not add GitHub-style write-path metadata to the Jira report.

Escalation

Use the subagent's structured verdict as the only routing input:

Summary state	Orchestrator action
SUBTASKS: PASS with Validation: PASS	Report success and proceed
SUBTASKS: WARN with Validation: PASS	Report usable output with warnings and make failed or skipped linkage visible
SUBTASKS: BLOCKED	Stop and surface the plan-shape or unsafe-linkage issue
SUBTASKS: FAIL	Stop and surface the fatal Jira or validation failure
SUBTASKS: ERROR or Validation: FAIL	Stop and surface the unexpected failure or local contract failure

Treat Validation: NOT_RUN as incomplete Phase 4 output even when the top-level status is already BLOCKED, FAIL, or ERROR.

Weekly Installs
43
Repository
b-mendoza/agent-skills
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass