---
title: implementation-agent
url: https://skills.sh/vishal2457/openit/implementation-agent
---

# implementation-agent

skills/vishal2457/openit/implementation-agent
implementation-agent
Installation
$ npx skills add https://github.com/vishal2457/openit --skill implementation-agent
SKILL.md
Implementation Agent
Open Orchestra Settings

Before doing anything else, look for orchestra-settings.json in the current workspace or repository root.

If the file exists, treat it as the workflow source of truth.
Read workflow.sequence to understand the expected stage order.
Read workflow.agents.implementation-agent to determine:
dependsOn: agents that must be complete before this agent runs.
next: the next agent to hand off to.
invocation: whether the next agent should be invoked automatically (auto) or left for the user to invoke manually (manual).
If dependsOn lists agents that are not complete yet, stop and report that implementation is blocked by workflow configuration.
When this agent finishes, hand off only to the configured next agent.
If invocation is manual, do not auto-invoke the next agent; leave a clear handoff for the user.
If the file does not exist, use the built-in default flow: planning-agent -> implementation-agent -> pr-review-agent, with automatic handoff from implementation to PR review.
Any future custom agent added by the user must be respected if it appears in orchestra-settings.json; do not assume the core three-agent workflow is exhaustive.
Purpose

Implement the parent issue by executing planned implementation subtasks and handling PR publication in the same run with token-efficient context loading and auditable stage handoff.

Runtime Configuration
Resolve the parent ticket reference from current conversation context first, then latest handoff payload if present.
If no parent ticket reference is available, ask the user for the ticket reference and stop.
Use the available issue tracker MCP directly for ticket operations.
If the required issue tracker MCP is unavailable, stop immediately and do not proceed with the task.
For every task/comment/status update written to the tracker, include: Skill-Version: implementation-agent@0.0.1.
Immediately stop if gh CLI is unavailable.
When to Invoke
After planning is complete on the parent issue.
After PR review requests implementation rework.
Required Inputs
Parent issue ID.
Parent issue status is In-progress.
Parent issue has tag planning-done.
Child subtasks tagged implement.
Most recent prior handoff comment in <!-- OPEN-ORCHESTRA-HANDOFF --> format.
Outputs
Code changes implementing all completable implement subtasks.
Git branch created as: codex/<issue-id>-<short-description>.
Each completed subtask marked done in the active issue tracker.
Comment on each incomplete subtask explaining why it was not completed.
Build and lint outcomes recorded in the active issue tracker as command + pass/fail, with short error excerpts only when failing.
Branch pushed to remote when work is complete.
Pull request created (first pass) or updated (rework pass) and linked to the tracker issue.
Parent issue status moved to In review after successful publish/update.
Parent issue tags:
implementation-done when implementation is complete.
pr-published when PR is created or updated and linked.
open-implementation-questions when implementation is blocked.
A handoff comment with a meaningful stage heading and wrapped JSON block:
Handing Off for Implementation
{
  "execution_trace": "Execution-Trace:\nActions:\n1. <action>\n2. <action>\nDecisions:\n- <decision + reason>\nReferences:\n- <source artifact or command>\nAssumptions:\n- <assumption>\nOpen-Questions: none|<question list>\nSkill-Version: implementation-agent@0.0.1",
  "handoff_summary": {
    "from_skill": "implementation-agent",
    "to_skill": "pr-review-agent",
    "status": "ready|blocked",
    "delta": ["<what changed in this implementation pass>"],
    "key_decisions": [{"decision": "<decision>", "reason": "<reason>"}],
    "relevant_artifacts": [
      {
        "artifact": "<artifact name>",
        "hash": "sha256:<hash>",
        "last_modified": "<ISO-8601>",
        "summary": "<short relevance summary>"
      }
    ],
    "open_blockers": [{"blocker": "<text>", "owner": "<owner>", "next_action": "<next action>"}],
    "next_guidance": {
      "need_full": ["<artifact names needed by next skill>"],
      "focus": ["<highest-priority checks for next skill>"],
      "findings": [{"id": "<finding-id>", "file": "<path>", "action": "<required fix/check>"}]
    }
  }
}

handoff_summary must be <= 600 tokens.
Context Gathering Order (Strict)
Locate the most recent comment containing <!-- OPEN-ORCHESTRA-HANDOFF --> from the previous skill.
Parse the JSON inside it; treat handoff_summary as primary context.
Review relevant_artifacts and hashes first.
Declare exactly which artifacts require full reads with need_full.
Read full content only if hash changed or the task cannot proceed without it.
Do not read entire issue history or all prior execution traces by default.
Procedure
Resolve the parent ticket reference from context and verify the required tracker MCP is available.
Execute the strict context gathering order above.
Validate prerequisites: parent issue status is In-progress and parent has planning-done.
Determine mode:
standard_mode: previous handoff is from planning/earlier implementation stage.
rework_mode: previous handoff is from pr-review-agent and includes next_guidance.findings.
In rework_mode, read only:
next_guidance.findings from the review handoff.
affected implement subtasks referenced by those findings.
additional artifacts only if explicitly declared in need_full.
Create a git branch named codex/<issue-id>-<short-description> if one is not already active.
Implement subtasks in listed order for standard_mode, or implement only finding-scoped fixes in rework_mode.
After finishing work, mark completed subtasks done and add blocker comments for any incomplete subtask.
Detect build and lint commands from repository config (for example package.json, Makefile, or equivalent).
Run build and lint commands and record concise results.
If implementation is blocked:
Add open-implementation-questions.
Post handoff JSON with status: blocked and concrete open_blockers.
Stop and wait for clarifications.
If implementation is complete:
Remove open-implementation-questions if present.
Add tag implementation-done.
Optionally keep legacy tag implemented during migration windows.
Push branch to origin (git push -u origin <branch>).
If linked PR already exists (typical rework_mode), update the existing PR context/comments.
Otherwise create a PR targeting the base branch and include tracker issue ID/URL.
Ensure parent issue tag pr-published is present.
Add concise parent issue comment with PR URL and short review request.
Move parent issue status to In review.
Post handoff JSON with to_skill: pr-review-agent and status: ready.
If open-implementation-questions is not present and orchestra-settings.json allows automatic handoff, invoke the configured next agent with the same parent issue ID. Otherwise stop after leaving the handoff for the user.
Guardrails
Do not start implementation unless parent issue has planning-done and status In-progress.
Do not execute subtasks that are not tagged implement.
Do not change scope outside planned subtasks without explicit tracker approval.
Do not leave incomplete subtasks without a blocker comment.
Do not run tracker operations until a parent ticket reference is resolved and the required tracker MCP is available.
Do not paste full command output (for example full pnpm list or pnpm build logs) into tracker or PR comments.
Do not reconstruct state by reading full comment history; use handoff summary first, then lazy-load only required artifacts.
Do not create or update a PR if there are no committed changes from this implementation pass.
Do not move issue status to In review until PR creation/update succeeds.
Ensure the PR references the correct tracker issue ID and URL.
Handoff

Primary consumer: the next agent configured for implementation-agent in orchestra-settings.json; default is pr-review-agent.

Weekly Installs
9
Repository
vishal2457/openit
GitHub Stars
1
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass