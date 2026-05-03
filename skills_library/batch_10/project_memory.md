---
title: project-memory
url: https://skills.sh/abpai/skills/project-memory
---

# project-memory

skills/abpai/skills/project-memory
project-memory
Installation
$ npx skills add https://github.com/abpai/skills --skill project-memory
SKILL.md
Project Memory

Maintain a per-project markdown memory file so future work improves over time.

This skill is always active. No trigger phrase is required.

Session Start
Read .agents/LEARNINGS.md before doing any task work.
Apply its guidance silently during execution.
If it does not exist, create it with this template:
# LEARNINGS

## Corrections

| Date | Source | What Went Wrong | What To Do Instead |
| ---- | ------ | --------------- | ------------------ |

## User Preferences

- (accumulate here as you learn them)

## Patterns That Work

- (approaches that succeeded)

## Patterns That Don't Work

- (approaches that failed and why)

## Domain Notes

- (project/domain context that matters)


Adapt sections to fit the repo, but keep entries easy to scan.

Continuous Updates

Update .agents/LEARNINGS.md continuously while working, not only at session boundaries.

Add an entry immediately when:

You identify the cause of an error.
The user corrects your behavior or preferred approach.
You catch your own mistake.
An attempted approach fails.
A non-obvious approach works reliably.
You re-check project memory before a risky or previously error-prone step.
What To Log

Log anything that should change behavior in future sessions:

Self mistakes: wrong assumptions, misread code, failed commands, incorrect fixes.
User corrections: what was requested instead.
Tool or environment surprises.
User preferences: style, workflow, structure.
Reliable patterns: what worked and when.

Write entries that are specific and actionable.

Bad: Made an error Good: Assumed API returned a list; it returns a paginated object with .items

Maintenance

Every 5 to 10 sessions, or when file length exceeds about 150 lines:

Merge redundant entries.
Promote repeated corrections into User Preferences.
Remove notes already captured by stable rules.
Archive outdated or resolved items.
Keep the file under 200 high-signal lines.
Examples

Self-caught mistake:

| 2026-02-06 | self | Passed (name, id) to createUser but signature is (id, name) | Check function signatures before calling; this repo does not use conventional arg ordering |


User correction:

| 2026-02-06 | user | Used relative imports | Use absolute imports from `src/` in this repo |

Update Check

On first use in a session, silently check for a newer version:

Fetch https://raw.githubusercontent.com/abpai/skills/main/versions.json.
Compare the version for project-memory against this file's metadata.version.
If the remote version is newer, pause before the main task and ask:

project-memory update available (local {X.Y} → remote {A.B}). Would you like me to update it for you first? I can run npx skills update project-memory for you.

If the user says yes, run the update before continuing.
If the user says no, continue with the current local version.
If the fetch fails or web access is unavailable, skip silently.
Weekly Installs
21
Repository
abpai/skills
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass