---
title: checkpoint-resume
url: https://skills.sh/yonatangross/orchestkit/checkpoint-resume
---

# checkpoint-resume

skills/yonatangross/orchestkit/checkpoint-resume
checkpoint-resume
Installation
$ npx skills add https://github.com/yonatangross/orchestkit --skill checkpoint-resume
SKILL.md
Checkpoint Resume

Rate-limit-resilient pipeline orchestrator. Saves progress to .claude/pipeline-state.json after every phase so long sessions survive interruptions.

Quick Reference
Category	Rule	Impact	Key Pattern
Phase Ordering	${CLAUDE_SKILL_DIR}/rules/ordering-priority.md	CRITICAL	GitHub issues/commits first, file-heavy phases last
State Writes	${CLAUDE_SKILL_DIR}/rules/state-write-timing.md	CRITICAL	Write after every phase, never batch
Mini-Commits	${CLAUDE_SKILL_DIR}/rules/checkpoint-mini-commit.md	HIGH	Every 3 phases, checkpoint commit format

Total: 3 rules across 3 categories

On Invocation

If .claude/pipeline-state.json exists: run scripts/show-status.sh to display progress, then ask to resume, pick a different phase, or restart. Load Read("${CLAUDE_SKILL_DIR}/references/resume-decision-tree.md") for the full decision tree.

If no state file exists: ask the user to describe the task, build an execution plan, write initial state via scripts/init-pipeline.sh <branch>, begin Phase 1.

Execution Plan Structure
{
  "phases": [
    { "id": "create-issues", "name": "Create GitHub Issues", "dependencies": [], "status": "pending" },
    { "id": "commit-scaffold", "name": "Commit Scaffold", "dependencies": [], "status": "pending" },
    { "id": "write-source", "name": "Write Source Files", "dependencies": ["commit-scaffold"], "status": "pending" }
  ]
}


Phases with empty dependencies may run in parallel via Task sub-agents (when they don't share file writes).

After Each Phase
Update .claude/pipeline-state.json — see Read("${CLAUDE_SKILL_DIR}/rules/state-write-timing.md")
Every 3 phases: create a mini-commit — see Read("${CLAUDE_SKILL_DIR}/rules/checkpoint-mini-commit.md")
References

Load on demand with Read("${CLAUDE_SKILL_DIR}/references/<file>"):

File	Content
references/pipeline-state-schema.md	Full field-by-field schema with examples
references/pipeline-state.schema.json	Machine-readable JSON Schema for validation
references/resume-decision-tree.md	Logic for resuming, picking phases, or restarting
Scripts
scripts/init-pipeline.sh <branch> — print skeleton state JSON to stdout
scripts/show-status.sh [path] — print human-readable pipeline status (requires jq)
Key Decisions
Decision	Recommendation
Phase granularity	One meaningful deliverable per phase (a commit, a set of issues, a feature)
Parallelism	Task sub-agents only for phases with empty dependencies that don't share file writes
Rate limit recovery	State is already saved — re-invoke /checkpoint-resume to continue
Weekly Installs
106
Repository
yonatangross/orchestkit
GitHub Stars
163
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass