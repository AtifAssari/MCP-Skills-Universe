---
rating: ⭐⭐
title: ralph-driven-development
url: https://skills.sh/tomkrikorian/visionosagents/ralph-driven-development
---

# ralph-driven-development

skills/tomkrikorian/visionosagents/ralph-driven-development
ralph-driven-development
Installation
$ npx skills add https://github.com/tomkrikorian/visionosagents --skill ralph-driven-development
SKILL.md
Ralph Driven Development (RDD)
Description and Goals

Ralph Driven Development (RDD) is a spec runner that repeatedly invokes Codex (or other agents) over ordered specs until a magic phrase signals completion. It automates the execution of development tasks by running an AI agent against a sequence of specifications until each one is completed.

Goals
Automate development workflow by running AI agents against specifications
Track progress through ordered specs and completion markers
Enable resumable workflows that can continue after interruptions
Provide customizable runner configuration for different agents and workflows
Support structured development with plan, specs, and completion tracking
What This Skill Should Do

When setting up or operating an RDD workflow, this skill should:

Guide workflow setup - Help you create plan.md, specs directory, and done.md files
Configure the runner - Show how to customize ralph.py for your agent and workflow
Execute specs - Run the agent against ordered specifications until completion
Track progress - Monitor completion status and log agent runs
Handle interruptions - Enable resuming workflows after breaks or errors

Use this skill when setting up or operating an RDD workflow with plan.md, specs/, done.md, agent-run.log, and a ralph.py runner.

Information About the Skill
What You Have
docs/specifications.md: the product plan and architecture overview.
docs/tasks/0001-...: incremental work units.
scripts/ralph.py: Python runner (execute directly from the skill folder).
Quick Start (Python + uv)
uv run python scripts/ralph.py

How It Works
Read docs/tasks/ for spec files and sort by filename order.
Skip completed specs listed in docs/done.md.
Invoke Codex with a prompt that:
follows the spec,
commits on completion,
records useful learnings in AGENTS.md,
prints the magic phrase when done.
Move to the next spec only after the magic phrase appears.
Sleep on usage limit errors until reset, then retry.
Progress Tracking
Show live console output:
[start] when a spec begins,
[done] when a spec completes,
[retry] when no magic phrase is found,
[skip] when a spec is already in docs/done.md.
Append full logs to docs/logs/agent-run.log.
Append completed specs to docs/done.md.
Resume After Interruptions

Rerun the script; it skips specs already listed in docs/done.md.

Customize Defaults
Python + uv
uv run python scripts/ralph.py \
  --magic-phrase SPEC_COMPLETE \
  --codex-exe codex \
  --codex-args "exec --dangerously-bypass-approvals-and-sandbox -m gpt-5.2-codex"

Troubleshooting
Handle usage limits by sleeping until reset time and retrying.
Inspect docs/logs/agent-run.log for repeated failures.
Ensure codex is on PATH if not found.
Where to Start

Create the plan in docs/specifications.md and some docs/tasks/... files for incremental work, then run the runner. Start at the first spec not listed in docs/done.md.

Weekly Installs
13
Repository
tomkrikorian/vi…osagents
GitHub Stars
49
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail