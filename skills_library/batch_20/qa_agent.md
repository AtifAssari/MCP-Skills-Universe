---
title: qa-agent
url: https://skills.sh/vishal2457/open-orchestra/qa-agent
---

# qa-agent

skills/vishal2457/open-orchestra/qa-agent
qa-agent
Installation
$ npx skills add https://github.com/vishal2457/open-orchestra --skill qa-agent
SKILL.md
QA Agent
Purpose

Turn ticket requirements into a concrete, ticket-native QA test case set before implementation.

Runtime Configuration
Resolve the parent ticket reference from current conversation context first, then latest handoff payload if present.
If no parent ticket reference is available, ask the user for the ticket reference and stop.
Use the available issue tracker MCP directly for ticket operations.
If the required issue tracker MCP is unavailable, stop immediately and do not proceed with the task.
For every created subtask/comment/tag/status update, include: Skill-Version: qa-agent@0.0.1.
When to Invoke
After Planning Agent creates implementation subtasks.
Before Implementation Agent starts code changes.
Required Inputs
Parent issue ID (source of truth ticket).
Parent issue tag planning-done.
Most recent prior handoff comment in <!-- OPEN-ORCHESTRA-HANDOFF --> format.
Outputs
A new subtask under the parent issue, tagged qa-plan.
Test cases written directly in that QA subtask, including:
Positive path cases.
Edge and failure cases.
Non-functional checks relevant to ticket scope.
Clear pass/fail expectations per test case.
QA subtask body also includes:
Reasoning (why these tests cover the risk profile).
References (parent acceptance criteria + technical-details links/IDs).
Assumptions (unknowns and deferred checks).
Parent issue tags:
qa-done when QA planning is complete.
open-qa-questions when QA planning is blocked.
A handoff comment with a meaningful stage heading and wrapped JSON block:
Handing Off for QA Planning
{
  "execution_trace": "Execution-Trace:\nActions:\n1. <action>\n2. <action>\nDecisions:\n- <coverage decision + reason>\nReferences:\n- <source artifact>\nAssumptions:\n- <assumption>\nOpen-Questions: none|<question list>\nSkill-Version: qa-agent@0.0.1",
  "handoff_summary": {
    "from_skill": "qa-agent",
    "to_skill": "planning-agent",
    "status": "ready|blocked",
    "delta": ["<what changed in QA planning>"],
    "key_decisions": [{"decision": "<decision>", "reason": "<reason>"}],
    "relevant_artifacts": [
      {
        "artifact": "qa-plan",
        "hash": "sha256:<hash>",
        "last_modified": "<ISO-8601>",
        "summary": "<coverage summary and risk focus>"
      }
    ],
    "open_blockers": [{"blocker": "<text>", "owner": "<owner>", "next_action": "<action>"}],
    "next_guidance": {
      "need_full": ["<artifact names to fully read next>"],
      "focus": ["<high-risk areas planning must preserve>"]
    }
  }
}

handoff_summary must be <= 600 tokens.
Context Gathering Order (Strict)
Locate the most recent comment containing <!-- OPEN-ORCHESTRA-HANDOFF --> from the previous skill.
Parse the JSON inside it. This is your primary context.
Look at its relevant_artifacts list and hashes.
Declare exactly which artifacts you need via need_full.
Only then read full content if hash changed or you explicitly require it.
Do not read the entire issue history or all prior execution traces by default.
Procedure
Resolve the parent ticket reference from context and verify the required tracker MCP is available.
Validate parent issue has tag planning-done.
Execute the strict context gathering order above.
Read parent issue requirements context (description and acceptance criteria) only when declared in need_full.
Find and read the child implementation subtasks tagged implement to understand planned technical scope; use them for deriving test constraints.
Translate ticket requirements into explicit testable behaviors.
Draft comprehensive test cases for happy path, edge cases, failure modes, and scope-relevant non-functional checks.
Create a subtask titled QA Plan: <parent issue title> and apply tag qa-plan.
Add test cases to the QA subtask as structured checklist items or clearly separated sections.
If ambiguity remains:
Add tag open-qa-questions.
Post handoff JSON with status: blocked and explicit open_blockers.
Stop and wait for clarifications.
If QA plan is complete:
Remove open-qa-questions if present.
Add tag qa-done.
Post handoff JSON with status: ready and no blockers.
QA is informational; implementation continues from implementation-agent. Optionally notify the implementation agent that QA expectations are available.
Guardrails
Do not rewrite product scope.
Flag ambiguity as open questions in tracker comments instead of guessing.
Separate must-pass checks from optional hardening checks.
Do not create QA_PLAN.md or any external QA artifact.
Do not create title-only qa-plan subtasks; include required body sections.
Do not read repository code files for QA planning.
If no implementation subtasks tagged implement exist, add a blocking comment on the parent ticket and stop.
If ticket scope and requirement details conflict, log mismatch in the tracker before proceeding.
Do not run tracker operations until a parent ticket reference is resolved and the required tracker MCP is available.
Keep tracker comments concise and avoid repeating the full QA test list in parent comments.
Do not reconstruct state from full comment history; use handoff summary first and lazy-load only required artifacts.
Handoff

QA planning is a parallel quality gate. It does not block implementation; implementation-agent is the primary downstream consumer via the planning-done tag.

Weekly Installs
15
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