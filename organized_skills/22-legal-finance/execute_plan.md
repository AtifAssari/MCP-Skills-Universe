---
rating: ⭐⭐
title: execute-plan
url: https://skills.sh/antinomyhq/forge/execute-plan
---

# execute-plan

skills/antinomyhq/forge/execute-plan
execute-plan
Installation
$ npx skills add https://github.com/antinomyhq/forge --skill execute-plan
SKILL.md
Execute Plan

Execute structured task plans with automatic status tracking and progress updates.

Commitment to Completion

When a plan is provided, all tasks in the plan must be completed. Before starting execution, recite:

"I will execute this plan to completion. All the 20 tasks will be addressed and marked as DONE."

Execution Steps

STEP 1: Recite the commitment to complete all tasks in the plan.

STEP 2: Read the entire plan file to identify pending tasks based on task_status.

STEP 3: Announce the next pending task and update its status to IN_PROGRESS in the plan file.

STEP 4: Execute all actions required to complete the task and mark the task status to DONE in the plan file.

STEP 5: Repeat from Step 3 until all tasks are marked as DONE.

STEP 6: Re-read the plan file to verify all tasks are completed before announcing completion.

Task Status Format

Use these status indicators in the plan file:

[ ]: PENDING
[~]: IN_PROGRESS
[x]: DONE
[!]: FAILED

Example Usage
User provides: "Execute plan at plans/2025-11-23-refactor-auth-v1.md"
Recite commitment: "I will execute this plan to completion..."
Read the plan file
Find first [ ] (PENDING) task
Update to [~] (IN_PROGRESS)
Execute the task
Update to [x] (DONE)
Move to next PENDING task
Repeat until all tasks appear DONE
Re-read plan file to verify completion
Announce completion
Weekly Installs
54
Repository
antinomyhq/forge
GitHub Stars
7.1K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass