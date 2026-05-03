---
title: skill-development
url: https://skills.sh/parcadei/continuous-claude-v3/skill-development
---

# skill-development

skills/parcadei/continuous-claude-v3/skill-development
skill-development
Originally fromanthropics/claude-code
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill skill-development
SKILL.md
Skill Development Rules

When working with files in .claude/skills/:

SKILL.md Structure
DO
Keep SKILL.md concise (< 200 lines)
Include clear "When to Use" section
Provide copy-paste bash commands
Reference scripts/ for MCP operations
Add triggers to skill-rules.json
DON'T
Include implementation details in SKILL.md
Duplicate content across skills
Create skills without corresponding trigger in skill-rules.json
Use allowed-tools that aren't needed
MCP Wrapper Skills

For skills that wrap MCP scripts:

Use allowed-tools: [Bash, Read] to restrict capabilities
Point to the script in scripts/ directory
Include parameter documentation
Weekly Installs
313
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass