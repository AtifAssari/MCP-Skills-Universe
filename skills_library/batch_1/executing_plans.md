---
title: executing-plans
url: https://skills.sh/obra/superpowers/executing-plans
---

# executing-plans

skills/obra/superpowers/executing-plans
executing-plans
Installation
$ npx skills add https://github.com/obra/superpowers --skill executing-plans
Summary

Execute a written implementation plan with critical review and task checkpoints.

Requires loading and critically reviewing the plan before execution; raises concerns with the human partner if issues are identified
Executes tasks sequentially, marking progress and running verifications as specified in the plan
Stops immediately on blockers (missing dependencies, test failures, unclear instructions) rather than guessing; asks for clarification
Integrates with git-worktrees for isolated workspaces and finishing-a-development-branch to complete the work after all tasks verify
Works best on platforms with subagent support; recommends subagent-driven-development skill as the preferred alternative when available
SKILL.md
Executing Plans
Overview

Load plan, review critically, execute all tasks, report when complete.

Announce at start: "I'm using the executing-plans skill to implement this plan."

Note: Tell your human partner that Superpowers works much better with access to subagents. The quality of its work will be significantly higher if run on a platform with subagent support (such as Claude Code or Codex). If subagents are available, use superpowers:subagent-driven-development instead of this skill.

The Process
Step 1: Load and Review Plan
Read plan file
Review critically - identify any questions or concerns about the plan
If concerns: Raise them with your human partner before starting
If no concerns: Create TodoWrite and proceed
Step 2: Execute Tasks

For each task:

Mark as in_progress
Follow each step exactly (plan has bite-sized steps)
Run verifications as specified
Mark as completed
Step 3: Complete Development

After all tasks complete and verified:

Announce: "I'm using the finishing-a-development-branch skill to complete this work."
REQUIRED SUB-SKILL: Use superpowers:finishing-a-development-branch
Follow that skill to verify tests, present options, execute choice
When to Stop and Ask for Help

STOP executing immediately when:

Hit a blocker (missing dependency, test fails, instruction unclear)
Plan has critical gaps preventing starting
You don't understand an instruction
Verification fails repeatedly

Ask for clarification rather than guessing.

When to Revisit Earlier Steps

Return to Review (Step 1) when:

Partner updates the plan based on your feedback
Fundamental approach needs rethinking

Don't force through blockers - stop and ask.

Remember
Review plan critically first
Follow plan steps exactly
Don't skip verifications
Reference skills when plan says to
Stop when blocked, don't guess
Never start implementation on main/master branch without explicit user consent
Integration

Required workflow skills:

superpowers:using-git-worktrees - REQUIRED: Set up isolated workspace before starting
superpowers:writing-plans - Creates the plan this skill executes
superpowers:finishing-a-development-branch - Complete development after all tasks
Weekly Installs
63.1K
Repository
obra/superpowers
GitHub Stars
176.5K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass