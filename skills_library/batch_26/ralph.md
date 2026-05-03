---
title: ralph
url: https://skills.sh/kv0906/cc-skills/ralph
---

# ralph

skills/kv0906/cc-skills/ralph
ralph
Installation
$ npx skills add https://github.com/kv0906/cc-skills --skill ralph
SKILL.md
Ralph Wiggum Loop Skill

Autonomous AI coding pattern that runs agents in iterations with clean context, working on PRD-driven features while maintaining CI green.

Commands
Command	Action
/ralph	Show help menu
/ralph setup	Create Ralph infrastructure
/ralph init	Build custom PRD interactively
/ralph run	Execute the autonomous loop
/ralph setup

Create all Ralph files in the current directory.

Steps:

Read and copy templates from this skill's templates/ folder:

templates/ralph-loop.sh → ./ralph-loop.sh
templates/prd.json → ./prd.json
templates/progress.txt → ./progress.txt
templates/README-RALPH.md → ./README-RALPH.md

Make script executable: chmod +x ralph-loop.sh

Detect project context and customize:

Check for package.json → determine package manager (pnpm/npm/yarn)
Check for tsconfig.json → TypeScript project
Update test commands in ralph-loop.sh accordingly

Show completion message with next steps

/ralph init

Guide user through creating a custom PRD interactively.

Questions to ask:

Project name?
What features do you want to build? (collect 3-5 user stories)
For each story:
Title?
Description?
Acceptance criteria? (3-5 specific, testable criteria)

Output: Generate prd.json with user's input. Offer to create other Ralph files if not present.

/ralph run

Execute the Ralph loop.

Pre-flight checks:

Verify ralph-loop.sh exists
Verify prd.json exists
Show summary:
Total user stories
Incomplete stories (where passes: false)
Max iterations configured
Ask for confirmation
Execute: ./ralph-loop.sh
/ralph (no args)

Show help menu:

Ralph Wiggum Loop - Autonomous AI Coding

Commands:
  /ralph setup  - Create Ralph infrastructure in this directory
  /ralph init   - Create a new PRD from scratch
  /ralph run    - Run the Ralph loop

What would you like to do?

Key Principles
Clean slate each iteration - Fresh context, no baggage
One feature at a time - Prevents scope creep
CI must stay green - Tests and types pass every commit
Progress tracking - Append to progress.txt each iteration
Clear stop condition - <promise>COMPLETE</promise> when all stories pass
Safety limit - Max iterations prevents infinite loops
PRD Quality Checklist

Good user stories are:

✅ Specific and scoped (completable in one iteration)
✅ Clear acceptance criteria (testable, unambiguous)
✅ Properly prioritized (1 = highest)
✅ Has "passes": false initially

Bad user stories are:

❌ Too vague ("build the UI")
❌ Too large (touches many systems)
❌ Unclear criteria ("make it nice")
Weekly Installs
26
Repository
kv0906/cc-skills
GitHub Stars
13
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass