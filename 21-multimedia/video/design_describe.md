---
title: design-describe
url: https://skills.sh/duc01226/easyplatform/design-describe
---

# design-describe

skills/duc01226/easyplatform/design-describe
design-describe
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill design-describe
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Skill Variant: Variant of design skills — describe UI from screenshot or video.

Quick Summary

Goal: Analyze a screenshot or video and produce a detailed written description of the UI design.

Workflow:

Analyze — Process the visual input (screenshot/video) using vision capabilities
Describe — Write detailed description of layout, colors, typography, interactions

Key Rules:

Use ai-multimodal skill for image/video analysis
Focus on design elements: layout, spacing, colors, typography, interactions

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

Think hard to describe the design based on this screenshot/video: $ARGUMENTS

Required Skills (Priority Order)
ui-ux-pro-max - Design intelligence database (ALWAYS ACTIVATE FIRST)
frontend-design - Visual analysis

Ensure token efficiency while maintaining high quality.

Workflow:
Use ai-multimodal skills to describe super details of the screenshot/video so the developer can implement it easily.
Be specific about design style, every element, elements' positions, every interaction, every animation, every transition, every color, every border, every icon, every font style, font size, font weight, every spacing, every padding, every margin, every size, every shape, every texture, every material, every light, every shadow, every reflection, every refraction, every blur, every glow, every image, background transparency, etc.
IMPORTANT: Try to predict the font name (Google Fonts) and font size in the given screenshot, don't just use Inter or Poppins.
Use ui-ux-designer subagent to create a design implementation plan following the progressive disclosure structure so the result matches the screenshot/video:
Create a directory using naming pattern from ## Naming section.
Save the overview access point at plan.md, keep it generic, under 80 lines, and list each phase with status/progress and links.
For each phase, add phase-XX-phase-name.md files containing sections (Context links, Overview with date/priority/statuses, Key Insights, Requirements, Architecture, Related code files, Implementation Steps, Todo list, Success Criteria, Risk Assessment, Security Considerations, Next steps).
Report back to user with a summary of the plan.
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
SocketPass
SnykPass