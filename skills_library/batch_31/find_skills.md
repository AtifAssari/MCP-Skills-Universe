---
title: find-skills
url: https://skills.sh/vilin1927/autoflux-landing/find-skills
---

# find-skills

skills/vilin1927/autoflux-landing/find-skills
find-skills
Installation
$ npx skills add https://github.com/vilin1927/autoflux-landing --skill find-skills
SKILL.md
Find Skills

Search and discover Claude Code skills from the community.

How to Search for Skills
Using npx skills CLI
# Search for skills by keyword
npx skills search <keyword>

# Browse popular skills
npx skills search --sort=popular

# Search by category
npx skills search --category=<category>

Categories
architecture - System design, patterns, decision frameworks
debugging - Bug investigation, root cause analysis
testing - Test strategies, TDD, coverage
frontend - UI/UX, React, Vue, CSS
backend - APIs, databases, servers
devops - CI/CD, Docker, Kubernetes
security - Auth, encryption, vulnerability scanning
productivity - Workflow automation, code generation
How to Install Skills
# Install from GitHub repository
npx skills add https://github.com/<owner>/<repo> --skill <skill-name>

# Install from registry
npx skills add <skill-name>

# List installed skills
npx skills list

# Remove a skill
npx skills remove <skill-name>

How to Create Skills
Skill Structure
skills/
└── my-skill/
    ├── SKILL.md          # Main skill file (required)
    ├── references/       # Reference documentation
    │   └── guide.md
    └── scripts/          # Automation scripts
        └── tool.py

SKILL.md Format
---
name: my-skill
description: Brief description of what the skill does
allowed-tools: Read, Glob, Grep  # Optional: restrict tool access
---

# Skill Name

## When to Use
Describe when this skill should be activated.

## Instructions
Step-by-step instructions for the AI assistant.

## Examples
Show example inputs and expected outputs.

Publishing
# Validate skill structure
npx skills validate

# Publish to registry
npx skills publish

Evaluating Skills

When choosing skills, consider:

Relevance - Does it solve your specific problem?
Quality - Is the SKILL.md well-written with clear instructions?
Maintenance - Is the repository actively maintained?
Compatibility - Does it work with your tech stack?
Reviews - What do other users say?
Useful Repositories
vercel-labs/skills - Official skills registry
anthropics/claude-code - Claude Code documentation
Weekly Installs
16
Repository
vilin1927/autof…-landing
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn