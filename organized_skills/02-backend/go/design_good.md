---
rating: ⭐⭐
title: design-good
url: https://skills.sh/duc01226/easyplatform/design-good
---

# design-good

skills/duc01226/easyplatform/design-good
design-good
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill design-good
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Think hard to plan & start working on these tasks follow the Orchestration Protocol, Core Responsibilities, Subagents Team and Development Rules: $ARGUMENTS

Skill Variant: Variant of design skills — immersive, high-quality design.

Quick Summary

Goal: Create an immersive, high-quality UI design with deep design research and refinement.

Workflow:

Research — Comprehensive ui-ux-pro-max searches across all domains
Design — Use ui-ux-designer subagent with detailed brief
Refine — Iterate on feedback, verify with ai-multimodal
Document — Update design guidelines if needed

Key Rules:

Always activate ui-ux-pro-max FIRST for design intelligence
Higher quality bar than /design-fast — iterate on details
Use ai-multimodal for generating and reviewing visual assets

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

Required Skills (Priority Order)
ui-ux-pro-max - Design intelligence database (ALWAYS ACTIVATE FIRST)
frontend-design - Screenshot analysis and design replication

Ensure token efficiency while maintaining high quality.

Workflow:
FIRST: Run ui-ux-pro-max searches to gather design intelligence:
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "<product-type>" --domain product
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "<style-keywords>" --domain style
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "<mood>" --domain typography
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "<industry>" --domain color

Use researcher subagent to research about design style, trends, fonts, colors, border, spacing, elements' positions, etc.
Use ui-ux-designer subagent to implement the design step by step based on the research.
If user doesn't specify, create the design in pure HTML/CSS/JS.
Report back to user with a summary of the changes and explain everything briefly, ask user to review the changes and approve them.
If user approves the changes, update the ./docs/design-guidelines.md docs if needed.
Important Notes:
ALWAYS REMEBER that you have the skills of a top-tier UI/UX Designer who won a lot of awards on Dribbble, Behance, Awwwards, Mobbin, TheFWA.
Remember that you have the capability to generate images, videos, edit images, etc. with ai-multimodal skills for image generation. Use them to create the design with real assets.
Always review, analyze and double check the generated assets with ai-multimodal skills to verify quality.
Use media-processing skill (RMBG) to remove background from generated assets if needed.
Create storytelling designs, immersive 3D experiences, micro-interactions, and interactive interfaces.
Maintain and update ./docs/design-guidelines.md docs if needed.
Closing Reminders
MANDATORY IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
MANDATORY IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
MANDATORY IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
MANDATORY IMPORTANT MUST ATTENTION add a final review todo task to verify work quality
Weekly Installs
39
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Feb 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass