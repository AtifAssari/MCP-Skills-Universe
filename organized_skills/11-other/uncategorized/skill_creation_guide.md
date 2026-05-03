---
rating: ⭐⭐⭐
title: skill-creation-guide
url: https://skills.sh/gmh5225/awesome-skills/skill-creation-guide
---

# skill-creation-guide

skills/gmh5225/awesome-skills/skill-creation-guide
skill-creation-guide
Installation
$ npx skills add https://github.com/gmh5225/awesome-skills --skill skill-creation-guide
SKILL.md
Skill Creation Guide
Scope

Use this skill when:

Creating new Agent Skills
Understanding SKILL.md format and conventions
Learning best practices for skill authoring
Skill Structure
skill-name/
├── SKILL.md          # Required: Instructions and metadata
├── scripts/          # Optional: Helper scripts
├── templates/        # Optional: Document templates
└── resources/        # Optional: Reference files

SKILL.md Format
Required Frontmatter
---
name: my-skill-name
description: A clear description of what this skill does and when to use it.
---

Body Structure
# Skill Name

Detailed description of the skill's purpose.

## When to Use This Skill

- Use case 1
- Use case 2

## Instructions

[Detailed instructions for the agent]

## Examples

[Real-world examples]

Best Practices
Keep descriptions exhaustive: The frontmatter description helps agents decide when to trigger the skill.
Focus on execution: The body should contain clear, actionable steps.
Use progressive disclosure: Put detailed references in references/ folder.
Include scripts for automation: Use helper scripts for deterministic operations.
Keep SKILL.md under 500 lines: For optimal performance.
Test across platforms: Verify skills work with Claude Code, Codex, etc.
Token Efficiency

Skills employ progressive disclosure architecture:

Metadata loading (~100 tokens): Agent scans available skills
Full instructions (<5k tokens): Load when skill is activated
Bundled resources: Only load as needed
Platform-Specific Paths
Platform	Project Path	Global Path
Claude Code	.claude/skills/	~/.claude/skills/
Codex	.codex/skills/	~/.codex/skills/
Cursor	.cursor/skills/	~/.cursor/skills/
Gemini CLI	.gemini/skills/	~/.gemini/skills/
GitHub Copilot	.github/skills/	~/.copilot/skills/
Quality Checklist
 Clear, actionable instructions
 Includes real-world examples
 Written for AI agents, not end users
 Documents prerequisites and dependencies
 Includes error handling guidance
 Tested on target platform(s)
Full Resource List

For more detailed skill creation resources, complete link lists, or the latest information, use WebFetch to retrieve the full README.md:

https://raw.githubusercontent.com/gmh5225/awesome-skills/refs/heads/main/README.md


The README.md contains the complete categorized resource list with all links.

Weekly Installs
21
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