---
title: pr-review-agent
url: https://skills.sh/vishal2457/open-orchestra/pr-review-agent
---

# pr-review-agent

skills/vishal2457/open-orchestra/pr-review-agent
pr-review-agent
Installation
$ npx skills add https://github.com/vishal2457/open-orchestra --skill pr-review-agent
SKILL.md
PR Review Agent
Open Orchestra Settings

Before doing anything else, look for orchestra-settings.json in the current workspace or repository root.

If the file exists, treat it as the workflow source of truth.
Read workflow.sequence to understand the expected stage order.
Read workflow.agents.pr-review-agent to determine:
dependsOn: agents that must be complete before this agent runs.
next: the next agent to hand off to.
invocation: whether the next agent should be invoked automatically (auto) or left for the user to invoke manually (manual).
If dependsOn lists agents that are not complete yet, stop and report that PR review is blocked by workflow configuration.
When this agent finishes, hand off only to the configured next agent.
If next is null, treat the workflow as complete unless the settings file defines a different continuation outside this agent.
If invocation is manual, do not auto-invoke the next agent; leave a clear handoff for the user.
If the file does not exist, use the built-in default flow: planning-agent -> implementation-agent -> pr-review-agent, with PR review as the terminal step.
Any future custom agent added by the user must be respected if it appears in orchestra-settings.json; do not assume the core three-agent workflow is exhaustive.
Purpose

Run a focused PR review that starts from changed code, validates only relevant requirements/spec sections, and reports blocking risks with minimal token use.

Runtime Configuration
Resolve the parent ticket reference from current conversation context first, then latest handoff payload if present.
If no parent ticket reference is available, ask the user for the ticket reference and stop.
Use the available issue tracker MCP directly for ticket operations.
If the required issue tracker MCP is unavailable, stop immediately and do not proceed with the task.
For every tracker comment/status update, include: Skill-Version: pr-review-agent@0.0.1.
When to Invoke
When a PR is ready for review and linked to an issue.
Required Inputs
Parent issue ID.
Parent issue tag pr-published.
Linked PR and PR diff / changed files.
Most recent prior handoff comment in <!-- OPEN-ORCHESTRA-HANDOFF --> format.
Outputs
PR comment:
Short review summary.
Findings that require changes (if any), tied to changed code.
Issue tracker comment:
Short review summary.
Required changes checklist (if any).
Status update:
In Progress when changes are required.
Done when changes are acceptable.
Optional invocation:
init-architect with scoped context when architecture-impacting changes are detected.
Parent issue tags:
pr-reviewed when review is clean.
open-pr-review-questions when review is blocked by missing context.
A handoff comment with a meaningful stage heading and wrapped JSON block:
Handing Off for PR Review
{
  "execution_trace": "Execution-Trace:\nActions:\n1. <action>\n2. <action>\nDecisions:\n- <review decision + reason>\nReferences:\n- <PR diff or requirement artifact>\nAssumptions:\n- <assumption>\nOpen-Questions: none|<question list>\nSkill-Version: pr-review-agent@0.0.1",
  "handoff_summary": {
    "from_skill": "pr-review-agent",
    "to_skill": "implementation-agent|none",
    "status": "ready|blocked|completed",
    "delta": ["<new findings or closure updates from this review pass>"],
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
      "need_full": ["<artifact names implementation must fully read>"],
      "focus": ["<highest-priority fix/check items>"],
      "findings": [
        {
          "id": "<finding-id>",
          "severity": "high|medium|low",
          "file": "<path>",
          "problem": "<what is wrong>",
          "required_change": "<what to change>",
          "affected_subtasks": ["<subtask identifier>"]
        }
      ]
    }
  }
}

handoff_summary must be <= 600 tokens.
Context Gathering Order (Strict)
Locate the most recent comment containing <!-- OPEN-ORCHESTRA-HANDOFF --> from the previous skill.
Parse the JSON inside it; treat handoff_summary as primary context.
Review relevant_artifacts and hashes first.
Declare exactly which artifacts require full reads with need_full.
Read full content only if hash changed or review cannot proceed without it.
Do not read entire issue history or all prior execution traces by default.
Procedure (Diff-First)
Resolve the parent ticket reference from context and verify the required issue tracker MCP is available.
Validate parent issue has tag pr-published.
Execute the strict context gathering order above.
Fetch PR diff and changed files first. This is the primary review input.
Build a minimal evidence set from the diff:
modified modules and behaviors.
affected API/data/auth/integration/runtime surfaces.
acceptance criteria touched by changed code.
Based on step 5, declare need_full and fetch only relevant sections from:
acceptance criteria.
technical-details.
other artifacts explicitly referenced by prior handoff.
Review only for correctness/regression risk in changed code and mismatch with the fetched relevant spec sections.
In the same pass, detect architecture impact from the PR diff. Impact is true when one or more of these is present:
API contract changes.
Data model/migration/index/persistence contract changes.
Service/module boundary changes.
Integration/event flow changes.
Authn/authz/session/security boundary changes.
Runtime/infrastructure behavior changes that alter topology or critical flows.
If architecture impact is true, prepare scoped payload for init-architect:
parent issue ID.
PR identifier/link.
changed files list.
concise diff summary.
matched architecture-impact cases.
suggested architecture doc sections to update.
Do not over-engineer:
avoid style-only nits.
report only issues that can cause bugs, regressions, broken behavior, or criteria mismatch.
Post a short PR comment with result and concise findings.
Post a short issue tracker comment with the same outcome summary.
If review is blocked by missing context:
Add open-pr-review-questions.
Post handoff JSON with status: blocked and explicit open_blockers.
Stop and wait for clarifications.
If required code changes are found and review is not blocked:
Remove open-pr-review-questions if present.
Set issue status to In Progress.
Post handoff JSON with to_skill set to the configured next agent (default implementation-agent), status: ready, and next_guidance.findings populated.
If orchestra-settings.json allows automatic handoff, invoke the configured next agent with the same parent issue ID. Otherwise stop after leaving the handoff for the user.
If no required changes remain:
Remove open-pr-review-questions if present.
Add tag pr-reviewed.
Set issue status to Done.
Post handoff JSON with to_skill: none and status: completed.
If architecture impact is true, invoke init-architect with the scoped payload from step 9.
Guardrails
Use the PR diff as the first and primary source.
Do not read the full repository for this review.
Do not read entire issue history by default.
Use handoff summary first, then lazy-load only required artifact sections.
Prioritize correctness and functional risk over stylistic preferences.
Keep findings actionable and tied to specific changed files.
Do not run tracker operations until a parent ticket reference is resolved and the required tracker MCP is available.
Keep PR and tracker comments concise; do not paste raw command logs.
Handoff

Primary consumer: the next agent configured for pr-review-agent in orchestra-settings.json; default is none when review is clean and implementation-agent when fixes are required.

Weekly Installs
21
Repository
vishal2457/open…rchestra
GitHub Stars
1
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass