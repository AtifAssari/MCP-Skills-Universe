---
rating: ⭐⭐
title: task manager
url: https://skills.sh/jmsktm/claude-settings/task-manager
---

# task manager

skills/jmsktm/claude-settings/Task Manager
Task Manager
Installation
$ npx skills add https://github.com/jmsktm/claude-settings --skill 'Task Manager'
SKILL.md
Task Manager

The Task Manager skill helps you organize, prioritize, and track tasks efficiently using proven productivity frameworks like Eisenhower Matrix, GTD (Getting Things Done), and MoSCoW prioritization. It ensures work is properly sequenced, delegated, and tracked to completion.

This skill excels at breaking down large projects into actionable tasks, identifying dependencies, estimating effort, and helping you focus on high-impact work. It integrates with your existing project management tools and provides clear daily/weekly task views.

Task Manager emphasizes clarity (well-defined tasks), ownership (clear assignees), and progress visibility (real-time status tracking).

Core Workflows
Workflow 1: Daily Task Organization

Steps:

Capture - Collect all pending tasks from:

Project plans and backlogs
Email and Slack messages
Meeting notes and action items
Bug reports and support tickets
Personal ideas and commitments

Clarify - For each task:

Write clear, actionable description starting with a verb
Estimate effort (S/M/L or hours)
Identify any dependencies or blockers
Assign to person or role
Add due date if time-sensitive

Organize - Categorize by:

Priority: Critical, High, Medium, Low
Type: Feature, Bug, Chore, Spike
Status: Todo, In Progress, Blocked, Done
Project/Epic: Which larger effort does this belong to?

Prioritize - Use Eisenhower Matrix:

Urgent + Important: Do today (top 3 tasks)
Important + Not Urgent: Schedule this week
Urgent + Not Important: Delegate or automate
Neither: Defer or delete

Execute - Focus on:

Starting with highest-impact task
Completing one task before starting another
Updating status as you progress
Communicating blockers immediately

Review - End of day:

Mark completed tasks as done
Move unfinished work to tomorrow
Note any learnings or obstacles
Prep tomorrow's top 3 tasks

Output: Prioritized daily task list with clear next actions.

Workflow 2: Weekly Task Planning

Steps:

Review project milestones and sprint goals
Identify this week's key deliverables (3-5 max)
Break deliverables into daily tasks
Estimate total effort vs. available capacity
Adjust scope or timeline if over-committed
Schedule deep work blocks for complex tasks
Reserve 20% capacity for interruptions and emergencies

Output: Week-at-a-glance task board with daily breakdown.

Workflow 3: Task Delegation

Steps:

Identify tasks that can be delegated
Match task to person with right skills and capacity
Provide clear context and acceptance criteria
Set expectations on timeline and check-ins
Create tracking mechanism for delegated work
Follow up at agreed intervals
Workflow 4: Backlog Grooming

Steps:

Review all tasks in backlog (weekly or bi-weekly)
Archive or delete obsolete tasks
Update priorities based on current goals
Break down vague tasks into specific actions
Identify quick wins (< 1 hour tasks)
Flag tasks that need more information
Quick Reference
Action	Command/Trigger
Create task	"add task: [description]"
Prioritize tasks	"prioritize my tasks"
Show today's work	"what should I work on today"
Weekly plan	"plan this week's tasks"
Delegate task	"delegate [task] to [person]"
Update status	"mark [task] as [status]"
Show blockers	"what's blocked"
Quick wins	"show me quick wins"
Review backlog	"groom backlog"
Estimate effort	"estimate [task]"
Best Practices
Make tasks atomic: Each task should be completable in 4-8 hours max; if larger, break it down
Use action verbs: Start every task with a verb (Build, Fix, Write, Review, Test, Deploy)
Define "done": Every task needs clear acceptance criteria so you know when it's complete
Limit WIP: Work on 1-3 tasks at a time; multitasking destroys productivity
Track blockers immediately: Don't let blocked tasks sit silently; escalate and communicate
Time-box tasks: If a task is taking 2x estimated time, stop and reassess approach
Batch similar tasks: Group related tasks (all code reviews, all email responses) to reduce context switching
Protect deep work: Block 2-4 hour chunks for complex tasks; no meetings or interruptions
Review daily: Spend 10 minutes at end of day reviewing progress and planning tomorrow
Celebrate completions: Acknowledge finished tasks; builds momentum and morale
Use templates: Create task templates for recurring work (code review, bug triage, deployment)
Link to context: Include links to relevant docs, PRs, issues, or designs in task description
Prioritization Frameworks
Eisenhower Matrix
                URGENT              NOT URGENT
IMPORTANT    |  DO NOW           |  SCHEDULE    |
             |  (Crises, fires)  |  (Planning)  |
             |-------------------|--------------|
NOT          |  DELEGATE         |  ELIMINATE   |
IMPORTANT    |  (Interruptions)  |  (Busywork)  |

MoSCoW Method
Must Have: Non-negotiable for release
Should Have: Important but not critical
Could Have: Nice to have if time permits
Won't Have: Out of scope for this iteration
RICE Scoring

Score = (Reach × Impact × Confidence) / Effort

Reach: How many users affected
Impact: How much it helps (0.25, 0.5, 1, 2, 3)
Confidence: How sure are you (%, as decimal)
Effort: Person-weeks required
Value vs. Effort
         HIGH VALUE
            |
    QUICK WINS | BIG BETS
            |
  --------- + ---------- EFFORT
            |
  TIME SINKS | LOW VALUE
            |
       LOW VALUE


Priority order: Quick Wins > Big Bets > Low Value > Time Sinks

Task Sizing Guide
Size	Duration	Complexity	Example
XS	15-30 min	Trivial	Fix typo, update config
S	1-2 hours	Simple	Write documentation, simple bug fix
M	4-8 hours	Moderate	Build new component, API endpoint
L	1-2 days	Complex	Feature integration, performance optimization
XL	3-5 days	Very Complex	Major refactor, new service

If task is > 5 days: Break it down into smaller tasks.

Status Definitions
Todo: Ready to start, all dependencies met
In Progress: Currently being worked on
Blocked: Waiting on dependency or decision
In Review: Work complete, awaiting approval
Done: Shipped to production or accepted by stakeholder
Deferred: Postponed to future sprint/release
Integration Points
Project Planner: Pulls tasks from project plans
Sprint Planner: Organizes tasks into sprints
GitHub Issues: Syncs with issue tracker
TodoWrite tool: Uses built-in task tracking
Calendar: Schedules time blocks for tasks
Slack/Discord: Sends task notifications and updates
Weekly Installs
–
Repository
jmsktm/claude-settings
GitHub Stars
3
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn