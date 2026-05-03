---
title: team-plan
url: https://skills.sh/wjaszczuk/agent-team-skills/team-plan
---

# team-plan

skills/wjaszczuk/agent-team-skills/team-plan
team-plan
Installation
$ npx skills add https://github.com/wjaszczuk/agent-team-skills --skill team-plan
SKILL.md
Team Plan

Write an implementation plan with team state tracking built in.

Announce at start: "I'm using the team-plan skill to create the implementation plan."

Process
Step 1: Delegate to obra writing-plans

REQUIRED SUB-SKILL: Use superpowers:writing-plans to generate the full plan.

Follow writing-plans exactly. Save plan to docs/plans/YYYY-MM-DD-<feature-name>.md.

Step 2: Add resume header

At the top of the generated plan (after the main header), add:

> **Resume:** Check `docs/plans/YYYY-MM-DD-<feature-name>.state.json` for current progress.
> Use `team-execute` skill to start or continue implementation.

Step 3: Add Progress section

After the plan header block (Goal/Architecture/Tech Stack), add:

## Progress

- [ ] Task 1: <title>
- [ ] Task 2: <title>
...


One checkbox per task in the plan.

Step 4: Create .state.json

Create docs/plans/YYYY-MM-DD-<feature-name>.state.json:

{
  "plan": "docs/plans/YYYY-MM-DD-<feature-name>.md",
  "worktree": null,
  "branch": null,
  "updated": "<ISO timestamp>",
  "resumePrompt": null,
  "tasks": [
    {
      "id": 1,
      "title": "<task title>",
      "status": "pending",
      "agent": null,
      "commit": null,
      "worktree": null,
      "startedAt": null,
      "completedAt": null
    }
  ]
}


One entry per task.

Step 5: Add .state.json to .gitignore

In the target project, ensure .state.json files are ignored:

echo "docs/plans/*.state.json" >> .gitignore
git add .gitignore
git commit -m "chore: ignore plan state files"


If .gitignore doesn't exist, create it first.

Step 6: Commit plan
git add docs/plans/YYYY-MM-DD-<feature-name>.md
git commit -m "docs: add implementation plan for <feature>"
git push

Step 7: Offer execution

"Plan ready. Use team-execute to start implementation with Developer and Architect agents."

Red Flags

Never:

Skip creating .state.json
Forget to add .state.json to .gitignore
Commit .state.json to the repo
Weekly Installs
9
Repository
wjaszczuk/agent…m-skills
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass