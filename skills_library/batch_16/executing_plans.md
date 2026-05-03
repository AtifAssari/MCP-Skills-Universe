---
title: executing-plans
url: https://skills.sh/hjewkes/agent-skills/executing-plans
---

# executing-plans

skills/hjewkes/agent-skills/executing-plans
executing-plans
Installation
$ npx skills add https://github.com/hjewkes/agent-skills --skill executing-plans
SKILL.md
Executing Plans
Overview

Load plan, review critically, execute tasks in batches, report for review between batches.

Core principle: Batch execution with checkpoints for architect review.

Announce at start: "I'm using the executing-plans skill to implement this plan."

The Process
Step 1: Load and Review Plan

Plan directory format (.claude/plans/<plan-id>/):

Read orchestration plan at plan.md and manifest at manifest.json
For each task in the current batch, read its briefing file from briefings/task-NN.md
Only load briefings for the current batch (default 3), not all tasks at once
Review critically — identify any questions or concerns about the plan
If concerns: Raise them with your human partner before starting
If no concerns: Create TodoWrite and proceed

Legacy monolithic format (docs/plans/*.md):

Read the plan file directly
Follow the same review and batch process below

Format detection: If the path contains manifest.json or points to a directory, use plan directory format. If it points to a .md file, use legacy format. If no path given, check .claude/plans/ for the most recent directory, fall back to docs/plans/ for the most recent .md.

Step 2: Execute Batch

Default: First 3 tasks

For each task:

Mark as in_progress
Follow each step exactly (briefing files have bite-sized steps)
Run verifications as specified in the briefing's Success Criteria
Mark as completed
Step 3: Report

When batch complete:

Show what was implemented
Show verification output
Say: "Ready for feedback."
Step 4: Continue

Based on feedback:

Apply changes if needed
Execute next batch (load next batch's briefing files)
Repeat until complete
Step 5: Complete Development

After all tasks complete and verified:

If using plan directory format, clean up:
Optionally write .claude/plans/<plan-id>/summary.md with execution notes
Delete the plan directory: rm -rf .claude/plans/<plan-id>/
If deletion fails, warn but do not block
Announce: "I'm using the git-workflow skill to complete this work."
REQUIRED SUB-SKILL: Use git-workflow stack
Follow that skill to verify tests, present options, execute choice
Guardrails

Stop and ask when blocked — don't guess. See references/guardrails.md for full stop conditions and checklist.

Integration

Required workflow skills:

git-workflow - REQUIRED: Worktrees for isolated workspaces, stack for completing development
writing-plans - Creates the plan this skill executes
Weekly Installs
8
Repository
hjewkes/agent-skills
GitHub Stars
3
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass