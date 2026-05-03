---
rating: ⭐⭐⭐
title: pi-planning-with-files
url: https://skills.sh/othmanadi/planning-with-files/pi-planning-with-files
---

# pi-planning-with-files

skills/othmanadi/planning-with-files/pi-planning-with-files
pi-planning-with-files
Installation
$ npx skills add https://github.com/othmanadi/planning-with-files --skill pi-planning-with-files
Summary

Persistent file-based planning system for organizing complex multi-step tasks and maintaining context across sessions.

Creates three markdown files (task_plan.md, findings.md, progress.md) in your project directory to serve as persistent working memory
Includes session recovery via script to sync context after /clear commands and resume interrupted work
Enforces structured workflows: plan first, update after each phase, log all errors, and never repeat failed actions
Provides templates, helper scripts, and a 3-strike error protocol to prevent silent failures and guide systematic troubleshooting
SKILL.md
Planning with Files

Work like Manus: Use persistent markdown files as your "working memory on disk."

FIRST: Check for Previous Session

Before starting work, check for unsynced context from a previous session:

Note: The scripts/ directory is inside this skill's installation folder.

# Linux/macOS
python scripts/session-catchup.py "$(pwd)"

# Windows PowerShell
python "scripts\session-catchup.py" (Get-Location)


If you cannot find the script: Ask Pi to locate it for you: Run the session-catchup.py script from the planning-with-files skill

If catchup report shows unsynced context:

Run git diff --stat to see actual code changes
Read current planning files
Update planning files based on catchup + git diff
Then proceed with task
Important: Where Files Go
Templates are in templates/ inside this skill
Your planning files go in your project directory
Location	What Goes There
Skill directory	Templates, scripts, reference docs
Your project directory	task_plan.md, findings.md, progress.md
Quick Start

Before ANY complex task:

Create task_plan.md — Use templates/task_plan.md as reference
Create findings.md — Use templates/findings.md as reference
Create progress.md — Use templates/progress.md as reference
Re-read plan before decisions — Refreshes goals in attention window
Update after each phase — Mark complete, log errors

Note: Planning files go in your project root, not the skill installation folder.

The Core Pattern
Context Window = RAM (volatile, limited)
Filesystem = Disk (persistent, unlimited)

→ Anything important gets written to disk.

File Purposes
File	Purpose	When to Update
task_plan.md	Phases, progress, decisions	After each phase
findings.md	Research, discoveries	After ANY discovery
progress.md	Session log, test results	Throughout session
Critical Rules
1. Create Plan First

Never start a complex task without task_plan.md. Non-negotiable.

2. The 2-Action Rule

"After every 2 view/browser/search operations, IMMEDIATELY save key findings to text files."

This prevents visual/multimodal information from being lost.

3. Read Before Decide

Before major decisions, read the plan file. This keeps goals in your attention window.

4. Update After Act

After completing any phase:

Mark phase status: in_progress → complete
Log any errors encountered
Note files created/modified
5. Log ALL Errors

Every error goes in the plan file. This builds knowledge and prevents repetition.

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| FileNotFoundError | 1 | Created default config |
| API timeout | 2 | Added retry logic |

6. Never Repeat Failures
if action_failed:
    next_action != same_action


Track what you tried. Mutate the approach.

The 3-Strike Error Protocol
ATTEMPT 1: Diagnose & Fix
  → Read error carefully
  → Identify root cause
  → Apply targeted fix

ATTEMPT 2: Alternative Approach
  → Same error? Try different method
  → Different tool? Different library?
  → NEVER repeat exact same failing action

ATTEMPT 3: Broader Rethink
  → Question assumptions
  → Search for solutions
  → Consider updating the plan

AFTER 3 FAILURES: Escalate to User
  → Explain what you tried
  → Share the specific error
  → Ask for guidance

Read vs Write Decision Matrix
Situation	Action	Reason
Just wrote a file	DON'T read	Content still in context
Viewed image/PDF	Write findings NOW	Multimodal → text before lost
Browser returned data	Write to file	Screenshots don't persist
Starting new phase	Read plan/findings	Re-orient if context stale
Error occurred	Read relevant file	Need current state to fix
Resuming after gap	Read all planning files	Recover state
The 5-Question Reboot Test

If you can answer these, your context management is solid:

Question	Answer Source
Where am I?	Current phase in task_plan.md
Where am I going?	Remaining phases
What's the goal?	Goal statement in plan
What have I learned?	findings.md
What have I done?	progress.md
When to Use This Pattern

Use for:

Multi-step tasks (3+ steps)
Research tasks
Building/creating projects
Tasks spanning many tool calls
Anything requiring organization

Skip for:

Simple questions
Single-file edits
Quick lookups
Templates

Copy these templates to start:

templates/task_plan.md — Phase tracking
templates/findings.md — Research storage
templates/progress.md — Session logging
Scripts

Helper scripts for automation:

scripts/init-session.sh — Initialize all planning files
scripts/check-complete.sh — Verify all phases complete
scripts/session-catchup.py — Recover context from previous session (v2.2.0)
Advanced Topics
Manus Principles: See reference.md
Real Examples: See examples.md
Anti-Patterns
Don't	Do Instead
Use TodoWrite for persistence	Create task_plan.md file
State goals once and forget	Re-read plan before decisions
Hide errors and retry silently	Log errors to plan file
Stuff everything in context	Store large content in files
Start executing immediately	Create plan file FIRST
Repeat failed actions	Track attempts, mutate approach
Create files in skill directory	Create files in your project
Weekly Installs
4.5K
Repository
othmanadi/plann…th-files
GitHub Stars
20.1K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn