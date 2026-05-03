---
title: kanban method
url: https://skills.sh/danhvb/my-ba-skills/kanban-method
---

# kanban method

skills/danhvb/my-ba-skills/Kanban Method
Kanban Method
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Kanban Method'
SKILL.md
Kanban Method Skill
Purpose

Guide the Product Owner agent in managing work items using Kanban principles, focusing on the flow of value and limiting work in progress (WIP).

Core Principles
1. Visualize the Workflow
Map current steps (To Do, In Progress, Review, Done).
Make policies explicit for each column.
Use simple boards (Trello, Jira, physical).
2. Limit Work in Progress (WIP)
Stop Starting, Start Finishing.
Identify bottlenecks.
Prevent context switching.
3. Manage Flow
Measure cycle time (Start to Finish).
Optimize for smooth delivery.
Reduce "wait" states.
4. Make Process Policies Explicit
Define "Ready for Pull."
Define "Definition of Done" for each column.
5. Implement Feedback Loops
Replenishment meetings (Weekly/On Demand).
Service Delivery Review (Bi-weekly/Monthly).
Daily Standup (Active walk of the board, right to left).
6. Improve Collaboratively (Kaizen)
Use metrics to drive changes.
Small, continuous experiments.
Applying the Skill
Interaction Guide for AI

1. Board Setup Prompts:

"Design a Kanban board for a Customer Support team."
"What columns should I add for a software dev team with heavy UAT?"
"Define 'WIP Limits' for a team of 4 developers."

AI Response Strategy:

Suggest columns based on actual workflow stages.
Recommend WIP limits based on team size (e.g., Team Size - 1).
Explain pull vs. push systems.

2. Flow Management Prompts:

"My 'Testing' column is always full. How do I fix this bottleneck?"
"Calculate cycle time for these completed items."
"How do I handle expedited (emergency) items on the board?"

AI Response Strategy:

Suggest swarming on bottlenecks.
Explain "Stop the Line" mentality.
Propose an "Expedite" swimlane (with strict WIP limit of 1).

3. Replenishment Prompts:

"How often should we replenish the 'To Do' column?"
"What criteria should we use for pulling the next item?"
"Facilitate a replenishment meeting agenda."

AI Response Strategy:

Focus on Just-In-Time (JIT) commitment.
Using "Cost of Delay" (CoD) for prioritization.
Commitment points vs. Delivery points.
Metrics
Cycle Time: Average time to complete an item.
Throughput: Items completed per time period.
WIP: Number of items currently in progress.
Cumulative Flow Diagram (CFD): Visualizes stability and bottlenecks.
Common Anti-Patterns
Infinite WIP: Columns with 20+ items for 2 people.
Hidden Work: Tasks happening outside the board.
Pushing Work: Assigning tasks to people instead of letting them pull.
Ignoring Policies: Skipping "Definition of Done".
References
"Kanban" by David J. Anderson
"Actionable Agile Metrics" by Daniel S. Vacanti
Lean Thinking principles
Weekly Installs
–
Repository
danhvb/my-ba-skills
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass