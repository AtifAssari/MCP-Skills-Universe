---
rating: ⭐⭐⭐
title: daily
url: https://skills.sh/ballred/obsidian-claude-pkm/daily
---

# daily

skills/ballred/obsidian-claude-pkm/daily
daily
Installation
$ npx skills add https://github.com/ballred/obsidian-claude-pkm --skill daily
SKILL.md
Daily Workflow Skill

Creates daily notes and provides structured workflows for morning planning, midday check-ins, and evening shutdowns.

Usage

Invoke with /daily or ask Claude to create today's note or help with daily routines.

Create Today's Note
/daily


Or simply ask:

"Create today's daily note"
"Start my morning routine"
"Help me with evening shutdown"
Daily Note Creation
What Happens

Checks if today's note exists

If yes: Opens the existing note
If no: Creates new note from template

Template Processing

Replaces {{date}} with today's date
Replaces {{date:format}} with formatted dates
Handles date arithmetic (e.g., {{date-1}} for yesterday)

Automatic Organization

Places note in Daily Notes/ folder
Names file with today's date (YYYY-MM-DD.md)
Preserves template structure
Template Variables

Your daily template can use:

{{date}} - Today's date in default format
{{date:dddd}} - Day name (e.g., Monday)
{{date:MMMM DD, YYYY}} - Formatted date
{{date-1:YYYY-MM-DD}} - Yesterday's date
{{date+1:YYYY-MM-DD}} - Tomorrow's date
{{time}} - Current time
Morning Routine (5-10 minutes)
Automated Steps
Create today's daily note (if not exists)
Pull incomplete tasks from yesterday
Read this week's ONE Big Thing from Goals/3. Weekly Review.md
Surface active project next-actions from Projects/*/CLAUDE.md
Review weekly goals for today's priority
Cascade Context Surfacing

Before interactive prompts, automatically surface:

ONE Big Thing from most recent weekly review
Active project next-actions from Projects/*/CLAUDE.md (read "Next Actions" section)
Monthly priority from Goals/2. Monthly Goals.md

Display as a brief context block at the top of the morning routine:

### Today's Context
- **Week's ONE Big Thing:** [from weekly review]
- **Active Projects:** [project names with first next-action each]
- **Monthly Focus:** [from monthly goals]

Interactive Prompts
"What's your ONE thing for today?"
"What might get in the way?"
"How do you want to feel at end of day?"
Task Creation Guidance

When adding tasks to the daily note, recommend linking to goals/projects:

- [ ] Draft API spec — Supports: [[Projects/MyApp]]
- [ ] Review chapter 3 — Supports: [[1. Yearly Goals#Read 12 books]]

Morning Checklist
 Daily note created
 Cascade context reviewed (ONE Big Thing, projects, monthly focus)
 Yesterday's incomplete tasks reviewed
 ONE priority identified
 Time blocks set
 Potential obstacles identified
Midday Check-in (2-3 minutes)
Quick Review
Check morning task completion
Compare actual vs planned time use
Assess energy level
Identify afternoon priorities
Adjustments
Reschedule incomplete morning tasks
Add urgent items that emerged
Reorder by current energy level
Note any blockers
Midday Questions
"How's your energy right now?"
"What's the most important thing for this afternoon?"
"What can you let go of today?"
Evening Shutdown (5 minutes)
Capture
Mark completed tasks with [x]
Add notes and learnings
Log energy levels (1-10)
Record gratitude items
Goal & Project Attention Summary

Automatically generate an end-of-day summary showing which goals and projects received attention:

### Today's Cascade Impact
- **Goals touched:** [[Goal 1]] (2 tasks), [[Goal 3]] (1 task)
- **Projects advanced:** [[ProjectA]] (3 tasks), [[ProjectB]] (1 task)
- **Unlinked tasks:** 2 (consider linking to a goal or project)

Reflect
What went well today?
What could be better?
What did I learn?
What am I grateful for?
Prepare
Identify tomorrow's priority (preview)
Move incomplete tasks to tomorrow or delete
Commit changes to git (/push)
Shutdown Checklist
 All tasks updated (done/moved/deleted)
 Reflection completed
 Tomorrow's priority identified
 Changes committed
Daily Note Structure

Standard daily note template:

# {{date}}

## Focus
> What's the ONE thing that would make today successful?

## Time Blocks
- Morning (9-12):
- Afternoon (12-5):
- Evening (5+):

## Tasks
### Must Do Today
- [ ]

### Work
- [ ]

### Personal
- [ ]

## Notes
[Capture thoughts, meeting notes, ideas]

## Reflection
- **Wins:**
- **Challenges:**
- **Learned:**
- **Grateful for:**
- **Energy:** /10
- **Tomorrow's priority:**

Time Block Strategies
Energy-Based
High energy tasks in morning
Administrative work after lunch
Creative work when naturally alert
Context-Based
Batch similar tasks together
Minimize context switching
Protect deep work blocks
Configuration

Customize paths to match your vault:

Daily notes folder: Daily Notes/
Template location: Templates/Daily Template.md
Date format: YYYY-MM-DD
Different Date Formats
YYYY-MM-DD - Standard ISO format (recommended)
MM-DD-YYYY - US format
DD-MM-YYYY - European format
YYYY-MM-DD-ddd - Include day abbreviation
Folder Organization by Month

Organize daily notes by month/year:

Daily Notes/2024/01/2024-01-15.md

Task-Based Progress Tracking

The daily skill uses session tasks to show progress during multi-step routines.

Morning Routine Tasks

Create tasks at skill start:

TaskCreate:
  subject: "Create daily note"
  description: "Create or open today's daily note from template"
  activeForm: "Creating daily note..."

TaskCreate:
  subject: "Pull incomplete tasks"
  description: "Carry forward uncompleted tasks from yesterday"
  activeForm: "Pulling incomplete tasks from yesterday..."

TaskCreate:
  subject: "Surface relevant goals"
  description: "Review weekly/monthly goals for today's priority"
  activeForm: "Surfacing relevant goals..."

TaskCreate:
  subject: "Set time blocks"
  description: "Establish time blocks based on energy and priorities"
  activeForm: "Setting time blocks..."

Dependencies

Morning routine tasks run sequentially:

TaskUpdate: "Pull incomplete tasks", addBlockedBy: [create-daily-note-id]
TaskUpdate: "Surface relevant goals", addBlockedBy: [pull-incomplete-tasks-id]
TaskUpdate: "Set time blocks", addBlockedBy: [surface-relevant-goals-id]

Evening Shutdown Tasks
TaskCreate:
  subject: "Update task statuses"
  description: "Mark completed tasks, note blockers"
  activeForm: "Updating task statuses..."

TaskCreate:
  subject: "Generate reflection prompts"
  description: "Prompt for wins, challenges, learnings, gratitude"
  activeForm: "Generating reflection prompts..."

TaskCreate:
  subject: "Prepare tomorrow's preview"
  description: "Identify tomorrow's priority and move incomplete tasks"
  activeForm: "Preparing tomorrow's preview..."


Mark each task in_progress when starting, completed when done using TaskUpdate.

Task tools provide visibility into what's happening during longer operations. Tasks are session-scoped and don't persist between Claude sessions—your actual work items remain in your daily note markdown checkboxes.

Integration

Works with:

/push - Commit end-of-day changes
/weekly - Weekly planning uses daily notes
/monthly - Monthly goals inform daily focus
/project - Surface project next-actions in morning
/onboard - Load context before planning
Goal tracking skill - Align daily tasks to goals
Productivity Coach - Accountability for daily routines
Weekly Installs
58
Repository
ballred/obsidia…aude-pkm
GitHub Stars
1.4K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass