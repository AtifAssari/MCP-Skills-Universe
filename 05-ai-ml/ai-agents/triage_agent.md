---
rating: ⭐⭐
title: triage-agent
url: https://skills.sh/vishal2457/open-orchestra/triage-agent
---

# triage-agent

skills/vishal2457/open-orchestra/triage-agent
triage-agent
Installation
$ npx skills add https://github.com/vishal2457/open-orchestra --skill triage-agent
SKILL.md
Triage Agent
Purpose

Classify incoming work into trivial, standard, or complex track and define skip_steps guidance so downstream skills can run with minimal context and token cost.

Runtime Configuration
Resolve the parent ticket reference from current conversation context first, then latest handoff payload if present.
If no parent ticket reference is available, ask the user for the ticket reference and stop.
Use the available issue tracker MCP directly for ticket operations.
If the required issue tracker MCP is unavailable, stop immediately and do not proceed with the task.
For every task/comment/status update written to the tracker, include: Skill-Version: triage-agent@0.0.1.
When to Invoke
After a parent issue already exists in the tracker (created manually, by intake automation, or by requirements-ticket-agent).
At workflow start for an existing parent issue that has not yet been triaged.
When scope changes materially and track classification needs refresh.
Required Inputs
Parent issue ID
Parent issue with at least baseline context (title + description or equivalent requirements artifact)
Current workflow tags/labels on parent issue
Latest previous handoff comment (if present)
Outputs
A compact handoff comment for the next stage with a meaningful stage heading and wrapped JSON block:
Handing Off for Triage
{
  "execution_trace": "Execution-Trace:\nActions:\n1. <action>\n2. <action>\nDecisions:\n- <decision + reason>\nReferences:\n- <source>\nAssumptions:\n- <assumption>\nOpen-Questions: none|<question list>\nSkill-Version: triage-agent@0.0.1",
  "handoff_summary": {
    "from_skill": "triage-agent",
    "to_skill": "requirements-ticket-agent|planning-agent",
    "status": "ready|blocked",
    "delta": ["<what changed since prior handoff>"],
    "key_decisions": [{"decision": "<decision>", "reason": "<why>"}],
    "relevant_artifacts": [
      {
        "artifact": "<name>",
        "hash": "sha256:<hash>",
        "last_modified": "<ISO-8601>",
        "summary": "<why this artifact matters>"
      }
    ],
    "open_blockers": [{"blocker": "<text>", "owner": "<owner>", "next_action": "<action>"}],
    "next_guidance": {
      "track": "trivial|standard|complex",
      "skip_steps": ["<skill-name>"],
      "need_full": ["<artifact names to fully read next>"]
    }
  }
}

handoff_summary must be <= 600 tokens.
Existing workflow tags/labels remain the trigger mechanism; do not replace tag-based routing.
Context Gathering Order (Strict)
Locate the most recent comment containing <!-- OPEN-ORCHESTRA-HANDOFF --> from the previous skill.
Parse the JSON inside it. This is your primary context.
Look at its relevant_artifacts list and hashes.
Declare exactly which artifacts you need via need_full.
Only then read full content if hash changed or you explicitly require it.
Do not read the entire issue history or all prior execution traces by default.
Procedure
Resolve the parent ticket reference from context and verify the required issue tracker MCP is available.
Execute the strict context gathering order above.
Determine readiness route from tags/context:
Route to requirements-ticket-agent when requirements are missing/ambiguous or open-requirements-questions is present.
Route to planning-agent when requirements are complete (requirements-done) and planning is not yet done.
Classify track:
trivial: isolated change, low regression risk, no cross-module impact.
standard: moderate scope, known patterns, normal implementation/review flow.
complex: cross-module/API/data contract/security/runtime impact or high ambiguity.
Build skip_steps guidance (empty when full standard flow is required). Only skip a stage when required artifacts already exist and no corresponding open-*-questions tag is present.
Keep tags unchanged except normal stage tags already defined by workflow policy.
Post the handoff comment in the exact wrapper format above.
Route to the next skill using existing tag/label triggers and the next_guidance payload.
Decision Heuristics
Complexity signals:
trivial: single-component/single-file intent, no API/schema/permission/runtime contract changes, clear acceptance criteria.
standard: bounded multi-file change with known pattern reuse, moderate regression surface, no critical contract shifts.
complex: cross-service/module coupling, API/schema/contract changes, security/privacy implications, migration/rollout concerns, or unresolved ambiguity.
Routing signals:
Prefer requirements-ticket-agent if intent is not testable as written.
Route to planning-agent once requirements are done; planning now inspects the live codebase and produces technical context without requiring pre-built architecture documents.
Confidence rule:
If confidence is low, mark status: blocked, list blockers in open_blockers, and avoid aggressive skip_steps.
Guardrails
Do not read full issue history by default.
Do not read all artifacts by default.
Do not modify existing workflow tag contracts.
Do not run tracker operations until a parent ticket reference is resolved.
Do not emit handoff payloads over 600 tokens.
Handoff

Primary consumer: requirements-ticket-agent (when requirements are incomplete) or planning-agent (when requirements are done), with next_guidance.track and next_guidance.skip_steps as routing hints.

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
SnykWarn