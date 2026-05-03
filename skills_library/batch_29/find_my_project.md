---
title: find-my-project
url: https://skills.sh/aviz85/claude-skills-library/find-my-project
---

# find-my-project

skills/aviz85/claude-skills-library/find-my-project
find-my-project
Installation
$ npx skills add https://github.com/aviz85/claude-skills-library --skill find-my-project
SKILL.md
Find My Project - סקיל למציאת הפרוייקט המושלם

עזרה למשתמשים למצוא את הפרוייקט האג'נטי הראשון שלהם ב-Claude Code דרך זיהוי כאבים יומיומיים

CRITICAL: Consult claude-code-guide

Before any significant decision, use:

Task tool with subagent_type=claude-code-guide


Example questions:

"What Claude Code primitives exist for [use case]?"
"How to structure an agentic project for [specific workflow]?"
"What's the difference between skills, agents, and hooks?"
What is an Agentic Project?

Agentic project ≠ traditional code or classic automation

An agentic project is built from:

CLAUDE.md - Knowledge about the user and project
Skills - Modular capabilities the agent can invoke
Processes - Stacks of skills
Tools - Connections to external world

It is NOT:

❌ React/Node.js application
❌ Python script
❌ Database with API
❌ Zapier/Make automation

It IS:

✅ Documents the agent knows how to read and update
✅ Skills the agent knows how to invoke
✅ Knowledge the agent uses for decisions
✅ Templates the agent fills in
Goal

Help new Claude Code users:

Identify their daily pain points
Find a suitable agentic project (not code!)
Set up the project structure
Start with initial files
Workflow
Step 1: Pain Point Discovery

Ask the user about their daily work:

🎯 בוא נמצא את הפרוייקט המושלם עבורך!

ענה על כמה שאלות קצרות:

1. **מה התפקיד שלך?** (מנהל, פרילנסר, יזם, עובד...)

2. **מה הדבר שהכי מתיש אותך בעבודה?**
   - משהו שחוזר על עצמו כל יום/שבוע
   - משהו שלוקח הרבה זמן
   - משהו שאתה שוכח לעשות

3. **אילו כלים אתה משתמש הכי הרבה?**
   - אימייל, וואטסאפ, אקסל...
   - CRM, יומן, מערכות ניהול...

4. **מה היית רוצה שיעשה לבד?**

Step 2: Analysis and Opportunity Identification

REQUIRED: Before continuing, consult claude-code-guide:

Use Task tool with subagent_type=claude-code-guide to ask:
"I have a user who [describe pain points]. What Claude Code primitives and project structure would be best for an AGENTIC project (not traditional code) to solve this?"


Based on responses and consultation, identify:

Repetitive tasks → Skills
Multi-step processes → Skill stacks
Information that needs to be available → CLAUDE.md + data files
External actions → Tools (MCP/API)
Step 3: Project Proposal

Present the recommended project to the user:

💡 הפרוייקט המומלץ עבורך:

**שם הפרוייקט:** [appropriate name]

**מה הוא יעשה:**
- [capability 1]
- [capability 2]
- [capability 3]

**למה זה מתאים לך:**
- פותר את: [specific pain]
- חוסך: [specific benefit]

**מבנה מומלץ:**
project-name/
├── CLAUDE.md          # הידע על הפרוייקט ועליך
├── data/              # קבצי מידע (לקוחות, משימות...)
├── templates/         # תבניות (מסמכים, הודעות...)
└── .claude/skills/    # סקילים ספציפיים לפרוייקט

רוצה שאקים את התיקייה?

Step 4: Project Setup

If user approves:

Create the folder structure:
mkdir -p ~/projects/[project-name]/{data,templates,.claude/skills}


Create initial CLAUDE.md with:

User information (from questioning)
Project purpose
Basic rules

Suggest data files to add:

📥 כדי שאוכל לעזור לך טוב יותר, שקול להכניס לתיקייה:

- רשימת לקוחות (אקסל/CSV/טקסט)
- דוגמאות של מסמכים שאתה שולח
- תבניות של הודעות
- כל מידע קבוע שאתה משתמש בו

אחרי שתכניס - אני אוכל לעזור לך לבנות את הסקיל הראשון!

Step 5: First Skill Recommendation

Based on identified pains, suggest a first skill:

⚡ הסקיל הראשון המומלץ:

**שם:** [skill name]
**מה יעשה:** [short description]

רוצה שניצור אותו יחד?


Important: Before creating the skill, consult claude-code-guide:

Use Task tool with subagent_type=claude-code-guide to ask:
"How to create a skill for [specific task]? What's the best structure?"

Common Project Examples
For Freelancers:
Client Management - quotes, contracts, tracking
Project Management - tasks, deadlines, reports
For Managers:
Weekly Reports - data collection, processing, generation
Team Tracking - tasks, statuses, alerts
For Entrepreneurs:
Lead Management - tracking, reminders, conversion
Content & Marketing - post creation, scheduling, measurement
What This Skill Does NOT Do
Does not build classic applications (React, Node.js...)
Does not create databases
Focuses on Claude Code ecosystem: documents, skills, agents
Consultation Tool

Whenever you need information about Claude Code capabilities:

Task tool with subagent_type=claude-code-guide


Example questions:

"What primitives exist in Claude Code for managing data?"
"How to create a skill that calls other skills?"
"What's the best way to structure CLAUDE.md?"
"How to create agents for background tasks?"
Weekly Installs
25
Repository
aviz85/claude-s…-library
GitHub Stars
27
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass