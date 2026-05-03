---
title: requirements-ticket-agent
url: https://skills.sh/vishal2457/open-orchestra/requirements-ticket-agent
---

# requirements-ticket-agent

skills/vishal2457/open-orchestra/requirements-ticket-agent
requirements-ticket-agent
Installation
$ npx skills add https://github.com/vishal2457/open-orchestra --skill requirements-ticket-agent
SKILL.md
Requirements Ticket Agent
Purpose

Convert a user request into a clean, tracker-ready ticket by gathering missing details through clarifying questions and formatting the output as Title, Body, and Acceptance Criteria.

When to Invoke
When a request is still informal and must become a structured ticket.
Before architecture, planning, or implementation work starts.
When requirements are incomplete, ambiguous, or missing constraints.
Required Inputs
User's initial request (raw problem statement).
Access to an available issue tracker MCP.
Most recent prior handoff comment in <!-- OPEN-ORCHESTRA-HANDOFF --> format when present.
Runtime Configuration
Resolve ticket reference from current conversation context first, then latest handoff payload if present.
If no ticket reference is found and the run requires updating an existing ticket, ask the user for the ticket reference and stop.
Use the available issue tracker MCP directly for ticket operations.
If the required issue tracker MCP is unavailable, stop immediately and do not proceed.
For every tracker write, include: Skill-Version: requirements-ticket-agent@0.0.1.
Outputs
One created issue in the selected tracker.
Issue body must include:
Context
Goal/Value
Scope
Constraints
Reasoning
References
Assumptions
Parent issue tags:
requirements-done when requirements are complete.
open-requirements-questions when clarification is still required.
A handoff comment with a meaningful stage heading and wrapped JSON block:
Handing Off for Requirements
{
  "execution_trace": "Execution-Trace:\nActions:\n1. <action>\n2. <action>\nDecisions:\n- <decision + reason>\nReferences:\n- <source>\nAssumptions:\n- <assumption>\nOpen-Questions: none|<question list>\nSkill-Version: requirements-ticket-agent@0.0.1",
  "handoff_summary": {
    "from_skill": "requirements-ticket-agent",
    "to_skill": "planning-agent",
    "status": "ready|blocked",
    "delta": ["<what changed in requirements state>"],
    "key_decisions": [{"decision": "<decision>", "reason": "<reason>"}],
    "relevant_artifacts": [
      {
        "artifact": "parent-issue-requirements",
        "hash": "sha256:<hash>",
        "last_modified": "<ISO-8601>",
        "summary": "<summary of finalized requirements>"
      }
    ],
    "open_blockers": [{"blocker": "<text>", "owner": "<owner>", "next_action": "<action>"}],
    "next_guidance": {
      "need_full": ["<artifact names to fully read next>"],
      "focus": ["<highest-priority requirements clarifications for planning>"]
    }
  }
}

handoff_summary must be <= 600 tokens.
Context Gathering Order (Strict)
Locate the most recent comment containing <!-- OPEN-ORCHESTRA-HANDOFF --> from the previous skill.
Parse the JSON inside it. This is your primary context.
Look at its relevant_artifacts list and hashes.
Declare exactly which artifacts you need via need_full (for example need_full: ["parent-issue-requirements"]).
Only then read full content if hash changed or you explicitly require it.
Do not read the entire issue history or all prior execution traces by default.
Procedure
Resolve ticket reference context (when applicable) and verify the required tracker MCP is available.
Execute the strict context gathering order above. If no previous handoff exists, continue with the user request as baseline.
Restate the request in one concise sentence to confirm scope.
Identify requirement gaps:
Objective and business/user value.
In-scope and out-of-scope boundaries.
Actors or user roles.
Constraints, dependencies, and assumptions.
Success conditions and measurable outcomes.
Ask focused clarifying questions in small batches.
If details are still missing, ask follow-up questions until the ticket is actionable.
Synthesize answers into a single ticket draft.
Write the final draft using the exact structure:
Title: <clear outcome-oriented title>

Body:
Context:
<context/problem>
Goal/Value:
<goal/value>
Scope:
<in-scope and out-of-scope>
Constraints:
<constraints/dependencies>
Reasoning:
<why this scope and acceptance criteria satisfy the request>
References:
- <user request>
- <clarifying answer #1>
- <clarifying answer #2>
Assumptions:
- <explicit assumptions and unknowns>

Acceptance Criteria:
1. <testable condition>
2. <testable condition>
3. <testable condition>

Ensure acceptance criteria are specific, testable, and unambiguous.
Present the draft and ask for explicit confirmation or edits.
If critical ambiguities remain:
Add tag open-requirements-questions.
Post handoff JSON with status: blocked and explicit open_blockers.
Stop and wait for human input.
If requirements are complete:
Remove open-requirements-questions if present.
Add tag requirements-done.
Post handoff JSON with status: ready and no blockers.
Invoke planning-agent with the created issue ID unless open-requirements-questions is present.
Return only the created issue link to the user.
Clarifying Question Set

Ask only what is needed. Prefer short, high-signal questions.

What problem are we solving, and who is affected?
What outcome defines success?
What must be included in scope?
What is explicitly out of scope?
Are there constraints (time, compliance, platform, integrations)?
Are there dependencies or blockers?
Are there edge cases or failure states that must be handled?
How should we validate completion?
Guardrails
Do not analyze repository code, architecture, or implementation design.
Do not propose technical solutions unless the user explicitly asks.
Do not invent requirements; mark unknowns and ask.
Do not finalize the ticket until critical ambiguities are resolved.
Do not accept title-only or placeholder issue bodies.
Do not echo the full finalized ticket after issue creation.
Return only the issue URL after creating the ticket.
Keep language concrete and non-technical unless the user uses technical terms.
Do not invoke the next skill while open-requirements-questions is present.
Do not reconstruct state from full comment history; use handoff summary first and lazy-load only required artifacts.
Handoff

Primary consumer: planning-agent (auto-invoke when unblocked).

Weekly Installs
14
Repository
vishal2457/open…rchestra
GitHub Stars
1
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn