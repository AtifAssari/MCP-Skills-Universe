---
rating: ⭐⭐⭐
title: timeline-creator
url: https://skills.sh/mhattingpete/claude-skills-marketplace/timeline-creator
---

# timeline-creator

skills/mhattingpete/claude-skills-marketplace/timeline-creator
timeline-creator
Installation
$ npx skills add https://github.com/mhattingpete/claude-skills-marketplace --skill timeline-creator
SKILL.md
Timeline Creator

Create interactive HTML timelines and project roadmaps with Gantt charts and milestones.

When to Use
"Create timeline for [project]"
"Generate roadmap for Q1-Q4"
"Make Gantt chart for schedule"
"Show project milestones"
Components
Timeline Header: project name, date range, completion %
Phase Groups: Q1, Q2, Q3, Q4 or custom phases
Timeline Items: tasks with start/end dates, progress, status
Milestones: key deliverables with dates
Gantt Visualization: horizontal bars showing duration
HTML Structure
<!DOCTYPE html>
<html>
<head>
  <title>[Project] Timeline</title>
  <style>
    body { font-family: system-ui; max-width: 1400px; margin: 0 auto; }
    .timeline-bar { background: linear-gradient(90deg, #4299e1, #48bb78); height: 20px; border-radius: 4px; }
    .milestone { border-left: 3px solid #e53e3e; padding-left: 10px; }
    /* Status colors: #48bb78 (done), #4299e1 (in-progress), #718096 (planned) */
  </style>
</head>
<body>
  <h1>[Project] Timeline</h1>
  <!-- Phase sections with timeline bars -->
  <!-- Milestones list -->
</body>
</html>

Timeline Bar Pattern
<div class="timeline-item">
  <span>Task Name</span>
  <div class="timeline-bar" style="width: [percentage]%; background: [status-color];"></div>
  <span>[start] - [end]</span>
</div>

Workflow
Extract tasks, dates, phases from project
Calculate duration percentages
Group by phases (quarters or custom)
Create HTML with Gantt-style bars
Add milestones section
Write to [project]-timeline.html

Use semantic colors for status, keep layout responsive.

Weekly Installs
120
Repository
mhattingpete/cl…ketplace
GitHub Stars
563
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass