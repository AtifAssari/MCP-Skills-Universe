---
rating: ⭐⭐
title: quick-implement
url: https://skills.sh/buiducnhat/agent-skills/quick-implement
---

# quick-implement

skills/buiducnhat/agent-skills/quick-implement
quick-implement
Installation
$ npx skills add https://github.com/buiducnhat/agent-skills --skill quick-implement
SKILL.md
Quick Implement
Purpose

Implement small features or bug fixes directly, with strict scope control and verification.

Use this skill for speed only when risk is low and requirements are clear.

Scope Gate (Required Before Coding)

Treat a task as quick-implement eligible only if all conditions below are true:

Clear requirement

Expected behavior is explicit
No major product/architecture ambiguity

Small change surface

Usually touches a small number of files (rough guideline: <= 5 files)
No broad cross-module refactor

Low architectural risk

No foundational redesign
No migration-heavy change
No multi-phase rollout dependency

Straightforward verification

Can validate with targeted tests/checks quickly
No long exploratory debugging loop required

If any condition fails, escalate to write-plan.

Hard Stop Escalation Criteria

Immediately stop quick implementation and switch to planning when any of these appear:

Requirement ambiguity that needs design decisions
Unexpected coupling across multiple subsystems
Significant data model or schema changes
Security-sensitive or compliance-critical changes
Performance work requiring benchmarks/design trade-offs
Refactor growing beyond original small scope
Repeated failed attempts without a clear root cause
Need for phased delivery, feature flags, or migration strategy

Escalation action:

Stop all coding activities immediately.
Output the exact message: "This change exceeds rapid-implementation safety limits. Recommend write-plan first to define phased execution and risk controls."
Use Question Tool to ask the user if they want to initiate a handoff to the write-plan skill.
Workflow
Step 1: Analyze and Contextualize
Understand the user request and define acceptance criteria.
Load project context per the shared Context Loading Protocol.
Inspect only the minimum necessary code paths.
Confirm the task still passes the Scope Gate.
If ambiguity remains, ask clarifying questions before coding. Follow the Question Tool mandate.
Step 2: Implement
Make the smallest correct change to satisfy requirements.
Reuse existing patterns and conventions.
Avoid opportunistic refactors unrelated to the request.
Keep changes idempotent and safe to rerun when applicable.
Step 3: Verify

Run proportional validation for the change using the appropriate execution tools:

Targeted tests related to modified behavior
Relevant lint/type checks for touched areas
Build or runtime verification if applicable

If verification fails unexpectedly:

Attempt focused fixes if clearly local.
If failures suggest broader impact, immediately escalate to write-plan.
Step 4: Complete
Summarize what changed and why.
List modified files.
Report verification commands and outcomes.
Update documentation if minor behavior or domain rules changed (e.g., small updates to docs/project-pdr.md or component specific readmes). Do not touch architecture docs; if architecture changed, this task should have been escalated.
Execution Boundaries
Do not expand scope without explicit user approval.
Do not assume unspecified behavior; clarify instead.
Do not force completion when risk increases—escalate early.
Escalate to write-plan when complexity or risk exceeds quick-implement limits.
Use fix when the task is primarily debugging an issue.
Output Checklist

Before final response, confirm:

Scope Gate was satisfied
No hidden architectural changes were introduced
Verification was run and reported
Escalation was used if safety limits were exceeded
Weekly Installs
304
Repository
buiducnhat/agent-skills
GitHub Stars
45
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass