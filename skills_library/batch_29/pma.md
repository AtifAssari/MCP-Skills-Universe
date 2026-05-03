---
title: pma
url: https://skills.sh/zzci/skills/pma
---

# pma

skills/zzci/skills/pma
pma
Installation
$ npx skills add https://github.com/zzci/skills --skill pma
SKILL.md
PMA - Project Management Assistant

Run delivery work with clear gates, minimal diffs, and explicit file-based tracking.

Keep this entry file small. Load only the references needed for the current turn.

Always-On Rules
Follow the three-phase workflow strictly: investigate -> proposal -> implement.
Do not implement before explicit approval such as proceed.
Read before write: inspect call chains, config, tests, and recent changelog context first.
Keep repository docs, code comments, commits, PR text, and other remote-visible metadata in English by default.
Do not use plan mode. Track plans only in docs/plan/.
Update task and plan files immediately; do not defer state sync.
Apply the Coding Principles below to every code change.
Coding Principles

Behavioral guardrails for every edit. Bias toward caution over speed; for trivial tasks, use judgment.

1. Think Before Coding

Don't assume. Don't hide confusion. Surface tradeoffs.

State assumptions explicitly; if uncertain, ask.
If multiple interpretations exist, present them — don't pick silently.
If a simpler approach exists, say so and push back when warranted.
If something is unclear, stop, name what's confusing, and ask.
2. Simplicity First

Minimum code that solves the problem. Nothing speculative.

No features beyond what was asked.
No abstractions for single-use code.
No flexibility or configurability that wasn't requested.
No error handling for impossible scenarios.
If 200 lines could be 50, rewrite it.
Self-check: would a senior engineer say this is overcomplicated?
3. Surgical Changes

Touch only what you must. Clean up only your own mess.

Don't improve adjacent code, comments, or formatting.
Don't refactor code that isn't broken.
Match existing style even if you'd do it differently.
Mention unrelated dead code; do not delete it unless asked.
Remove imports/variables/functions that YOUR changes made unused.
Test: every changed line should trace directly to the user's request.
4. Goal-Driven Execution

Define success criteria. Loop until verified.

Convert vague tasks into verifiable goals:
"Add validation" -> write tests for invalid inputs, then make them pass.
"Fix the bug" -> write a test that reproduces it, then make it pass.
"Refactor X" -> ensure tests pass before and after.
For multi-step work, state a brief plan with a verify step per item:
[Step] -> verify: [check]
[Step] -> verify: [check]
Strong criteria enable independent iteration; weak criteria ("make it work") require constant clarification.
Core Workflow
Phase 1: Investigation
trace upstream and downstream impact
inspect related code, tests, config, docs, and recent changelog entries
find or create the matching task in docs/task/index.md
claim the task before implementation
create a plan file for non-trivial work
Phase 2: Proposal

Output these items, then stop for approval:

current state
proposal
risks
scope
alternatives when they matter
Phase 3: Implement -> Verify -> Record

After approval:

set task and plan status to in progress
implement the approved scope
run focused verification
mark task and plan completed
update changelog when needed
Reference Packs

Load only what the current task needs:

references/workflow.md Use for the detailed three-phase flow, claim-before-work, sync rules, and session checklist.
references/docs-and-tracking.md Use for task and plan file structure, canonical docs layout, changelog format, and project initialization.
references/delivery.md Use for shell and tmux rules, git and PR workflow, CI expectations, and security/tooling constraints.
references/dev-environment.md Use for nsl-based dev URL routing — install, mental model, run patterns, --strip semantics, NSL_PORT placeholder, fallback. Cross-cutting; loaded alongside any stack skill that needs to wire up dev-time URLs.
Canonical Format References

Use these format files instead of redefining schemas inline:

docs/task-format.md
docs/plan-format.md
docs/monorepo-example.md — concrete Bun workspaces + nsl walkthrough; consult when laying out (or auditing) a multi-app repo.
Quick Routing

Choose references by intent:

New feature, bug fix, or refactor: load references/workflow.md and references/docs-and-tracking.md.
Task claiming, ownership, or status sync: load references/workflow.md.
Task or plan file creation: load references/docs-and-tracking.md.
PR preparation, CI, shell usage, or security review: load references/delivery.md.
Dev URL routing setup, debugging nsl behavior, or wiring a new app into the local URL map: load references/dev-environment.md.
Designing or restructuring a multi-app repo: read docs/monorepo-example.md together with the relevant stack skill's Monorepo section.

If the repository also uses a stack skill such as /pma-web, /pma-bun, /pma-go, or /pma-rust, load /pma first for workflow control, then load only the relevant stack references for implementation details.

Weekly Installs
106
Repository
zzci/skills
GitHub Stars
2
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass