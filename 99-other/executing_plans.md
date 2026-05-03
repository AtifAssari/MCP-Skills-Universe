---
rating: ⭐⭐
title: executing-plans
url: https://skills.sh/sickn33/antigravity-awesome-skills/executing-plans
---

# executing-plans

skills/sickn33/antigravity-awesome-skills/executing-plans
executing-plans
Originally fromobra/superpowers
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill executing-plans
Summary

Structured plan execution with batch processing and architect review checkpoints.

Loads and critically reviews implementation plans before execution, raising concerns with human partners upfront rather than proceeding blindly
Executes tasks in batches (default: first 3 tasks) with verification steps and completion marking between each batch
Reports results and verification output after each batch, pausing for feedback before continuing to the next batch
Stops immediately on blockers, missing dependencies, test failures, or unclear instructions rather than guessing or forcing through
Integrates with the finishing-a-development-branch skill to handle final verification, testing, and deployment decisions once all tasks complete
SKILL.md
Executing Plans
Overview

Load plan, review critically, execute tasks in batches, report for review between batches.

Core principle: Batch execution with checkpoints for architect review.

Announce at start: "I'm using the executing-plans skill to implement this plan."

The Process
Step 1: Load and Review Plan
Read plan file
Review critically - identify any questions or concerns about the plan
If concerns: Raise them with your human partner before starting
If no concerns: Create TodoWrite and proceed
Step 2: Execute Batch

Default: First 3 tasks

For each task:

Mark as in_progress
Follow each step exactly (plan has bite-sized steps)
Run verifications as specified
Mark as completed
Step 3: Report

When batch complete:

Show what was implemented
Show verification output
Say: "Ready for feedback."
Step 4: Continue

Based on feedback:

Apply changes if needed
Execute next batch
Repeat until complete
Step 5: Complete Development

After all tasks complete and verified:

Announce: "I'm using the finishing-a-development-branch skill to complete this work."
REQUIRED SUB-SKILL: Use superpowers:finishing-a-development-branch
Follow that skill to verify tests, present options, execute choice
When to Stop and Ask for Help

STOP executing immediately when:

Hit a blocker mid-batch (missing dependency, test fails, instruction unclear)
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
Between batches: just report and wait
Stop when blocked, don't guess
When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
442
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass