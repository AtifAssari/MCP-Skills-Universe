---
rating: ⭐⭐
title: design-fast
url: https://skills.sh/duc01226/easyplatform/design-fast
---

# design-fast

skills/duc01226/easyplatform/design-fast
design-fast
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill design-fast
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Think hard to plan & start working on these tasks follow the Orchestration Protocol, Core Responsibilities, Subagents Team and Development Rules: $ARGUMENTS

Skill Variant: Variant of design skills — quick design implementation.

Quick Summary

Goal: Create a quick UI design using design intelligence databases and subagents.

Workflow:

Research — Run ui-ux-pro-max searches for design intelligence
Design — Use ui-ux-designer subagent to create the design
Review — Present to user for approval

Key Rules:

Always activate ui-ux-pro-max FIRST for design intelligence
Default to pure HTML/CSS/JS if user doesn't specify framework
Use ai-multimodal for generating real visual assets

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

Required Skills (Priority Order)
ui-ux-pro-max - Design intelligence database (ALWAYS ACTIVATE FIRST)
frontend-design - Quick implementation

Ensure token efficiency while maintaining high quality.

Workflow:
FIRST: Run ui-ux-pro-max searches to gather design intelligence:
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "<product-type>" --domain product
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "<style-keywords>" --domain style
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "<mood>" --domain typography
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "<industry>" --domain color

Use ui-ux-designer subagent to start the design process.
If user doesn't specify, create the design in pure HTML/CSS/JS.
Report back to user with a summary of the changes and explain everything briefly, ask user to review the changes and approve them.
If user approves the changes, update the ./docs/design-guidelines.md docs if needed.
Notes:
Remember that you have the capability to generate images, videos, edit images, etc. with ai-multimodal skills. Use them to create the design and real assets.
Always review, analyze and double check generated assets with ai-multimodal skills to verify quality.
Maintain and update ./docs/design-guidelines.md docs if needed.
Closing Reminders
MANDATORY IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
MANDATORY IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
MANDATORY IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
MANDATORY IMPORTANT MUST ATTENTION add a final review todo task to verify work quality
Weekly Installs
35
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass