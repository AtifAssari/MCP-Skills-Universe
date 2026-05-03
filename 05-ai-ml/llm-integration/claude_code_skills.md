---
title: claude-code-skills
url: https://skills.sh/gmh5225/awesome-skills/claude-code-skills
---

# claude-code-skills

skills/gmh5225/awesome-skills/claude-code-skills
claude-code-skills
Installation
$ npx skills add https://github.com/gmh5225/awesome-skills --skill claude-code-skills
SKILL.md
Claude Code Skills
Scope

Use this skill when:

Installing skills for Claude Code
Developing Claude Code specific skills
Understanding Claude Code skill discovery
Installation Paths
Project scope: .claude/skills/ in project root
User scope: ~/.claude/skills/

Claude Code auto-discovers skills from these directories.

Installing Skills
From GitHub Repository
# Clone to project
git clone https://github.com/user/skill-repo .claude/skills/skill-name

# Or clone to user directory
git clone https://github.com/user/skill-repo ~/.claude/skills/skill-name

Manual Installation
Create skill folder in .claude/skills/
Add SKILL.md with frontmatter
Restart Claude Code to pick up new skills
Verifying Installation
# List installed skills
ls ~/.claude/skills/

# Check skill metadata
head ~/.claude/skills/skill-name/SKILL.md

Using Skills

Skills activate automatically based on your request context. You can also:

Mention skill name explicitly in your prompt
Use /init to bootstrap context for a repository
Official Skills Repository
https://github.com/anthropics/skills
Key Official Skills
Skill	Purpose
docx	Word document manipulation
xlsx	Excel spreadsheet operations
pptx	PowerPoint presentations
pdf	PDF extraction and creation
webapp-testing	Playwright-based web testing
mcp-builder	Create MCP servers
skill-creator	Interactive skill creation
Claude Code Commands
/init - Initialize project context
Skills auto-load when relevant to your task
Best Practices
Keep skills focused on specific tasks
Use progressive disclosure for large reference files
Include scripts for automation
Test skills in isolated environments first
Full Resource List

For more detailed Claude Code skill resources, complete link lists, or the latest information, use WebFetch to retrieve the full README.md:

https://raw.githubusercontent.com/gmh5225/awesome-skills/refs/heads/main/README.md


The README.md contains the complete categorized resource list with all links.

Weekly Installs
22
Repository
gmh5225/awesome-skills
GitHub Stars
31
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn