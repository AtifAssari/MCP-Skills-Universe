---
rating: ⭐⭐
title: architect-agent
url: https://skills.sh/vishal2457/open-orchestra/architect-agent
---

# architect-agent

skills/vishal2457/open-orchestra/architect-agent
architect-agent
Installation
$ npx skills add https://github.com/vishal2457/open-orchestra --skill architect-agent
SKILL.md
Architect Agent
Purpose

Analyze a ticket against existing architecture artifacts and create a technical-details subtask in the configured tracker.

Runtime Configuration
Read /orchestra-config.json from repository root.
Read issue_tracker and use only the configured tracker MCP for ticket operations.
If the configured tracker MCP is unavailable, stop immediately.
For tracker writes, include: Skill-Version: architect-agent@2.0.0.
Required Inputs
Parent issue ID.
Parent issue tag requirements-done.
/architecture/architecture.md.
Relevant /architecture/docs/*.md files.
Most recent prior handoff comment in <!-- OPEN-ORCHESTRA-HANDOFF --> format.
Outputs
One tracker subtask tagged technical-details.
technical-details body must include:
Scope Decision
Module/Domain Targets
Blast Radius
Sensitive Areas
Reasoning
References
Assumptions
Parent issue tags:
architecture-done when architecture output is ready.
open-architecture-questions when architecture is blocked.
Parent issue status update based on open questions/readiness.
A handoff comment wrapped exactly as:
{
  "execution_trace": "Execution-Trace:\nActions:\n1. <action>\n2. <action>\nDecisions:\n- <decision + reason>\nReferences:\n- <architecture file or issue field>\nAssumptions:\n- <assumption>\nOpen-Questions: none|<question list>\nSkill-Version: architect-agent@2.0.0",
  "handoff_summary": {
    "from_skill": "architect-agent",
    "to_skill": "qa-agent",
    "status": "ready|blocked",
    "delta": ["<what changed in technical direction>"],
    "key_decisions": [{"decision": "<decision>", "reason": "<reason>"}],
    "relevant_artifacts": [
      {
        "artifact": "technical-details",
        "hash": "sha256:<hash>",
        "last_modified": "<ISO-8601>",
        "summary": "<key architecture guidance for QA/planning>"
      }
    ],
    "open_blockers": [{"blocker": "<text>", "owner": "<owner>", "next_action": "<action>"}],
    "next_guidance": {
      "need_full": ["<artifact names to fully read next>"],
      "focus": ["<highest-priority risk areas for QA>"]
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
Read /orchestra-config.json and verify the configured tracker MCP is available.
Execute the strict context gathering order above.
Validate parent issue has requirements-done.
Validate /architecture/architecture.md exists.
Read parent issue summary, description, and acceptance criteria only when required by declared need_full.
Load /architecture/architecture.md first, then only relevant /architecture/docs/*.md based on declared need.
Determine:
scope decision (proceed vs decompose recommendation).
high-level domains/modules and where planning should inspect files.
blast radius.
sensitive area flags.
open questions.
Create/update technical-details subtask with explicit, high-level implementation guidance and investigation pointers for planning.
If open questions remain:
Add tag open-architecture-questions.
Post handoff JSON with status: blocked and explicit open_blockers.
Set parent status to clarification-needed and stop.
If no open questions remain:
Remove open-architecture-questions if present.
Add tag architecture-done.
Post handoff JSON with status: ready and no blockers.
Set parent status to TODO.
Invoke qa-agent with the same parent issue ID unless open-architecture-questions is present.
Guardrails
Do not generate or rewrite architecture docs; init-architect owns that.
Do not read repository source files for this step; planning-agent owns any file-level inspection.
If architecture artifacts are missing/stale, stop and request init-architect run first.
Keep output actionable and bounded to current ticket scope.
Do not create title-only technical-details; include required sections.
Keep tracker comments concise; avoid repeating issue text verbatim.
Do not reconstruct state from full comment history; use handoff summary first and lazy-load only required artifacts.
Handoff

Primary consumer: qa-agent (auto-invoke when unblocked).

Weekly Installs
10
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