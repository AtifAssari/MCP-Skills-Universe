---
title: copilotkit-self-update
url: https://skills.sh/copilotkit/skills/copilotkit-self-update
---

# copilotkit-self-update

skills/copilotkit/skills/copilotkit-self-update
copilotkit-self-update
Installation
$ npx skills add https://github.com/copilotkit/skills --skill copilotkit-self-update
SKILL.md
Update CopilotKit Skills

Run this command to pull the latest CopilotKit skills from GitHub:

npx skills add copilotkit/skills --full-depth -y


This does a fresh clone every time — it always gets the latest version regardless of what's cached.

This works across all tools — Claude Code, Codex, Cursor, Gemini CLI, and others. It detects which tools are installed and updates skills for each.

After the command completes, start a new session in your tool to pick up the changes.

When to Suggest This
User says the skills have wrong API names or outdated information
User reports that a CopilotKit API doesn't match what the skill says
User explicitly asks to update or refresh skills
A new CopilotKit version was released and skills may be stale
Weekly Installs
154
Repository
copilotkit/skills
GitHub Stars
22
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SnykWarn