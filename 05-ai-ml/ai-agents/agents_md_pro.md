---
rating: ⭐⭐⭐
title: agents-md-pro
url: https://skills.sh/alexander-danilenko/ai-skills/agents-md-pro
---

# agents-md-pro

skills/alexander-danilenko/ai-skills/agents-md-pro
agents-md-pro
Installation
$ npx skills add https://github.com/alexander-danilenko/ai-skills --skill agents-md-pro
SKILL.md
AGENTS.md Pro

Create token-efficient AGENTS.md files that maximize clarity with minimal tokens.

Core Principles
Token efficiency - Every word justifies its cost
Commands over explanations - Show, don't tell
Reference configs - Point to .eslintrc, never duplicate
Model-agnostic - Universal terminology only
Condensed default - Always minimal output
Input

Required: Project directory path If missing: Request from user

Workflow Router

Map user request to workflow:

Create → workflows.md
Optimize/condense → workflows.md
Update/refresh → workflows.md
Validate → workflows.md
Quick Reference

Output template - Standard repo:

# [Project] | [Tech Stack]
## COMMANDS
- Dev: `cmd` | Build: `cmd` | Test: `cmd` | Lint: `cmd --fix`
## STRUCTURE
- `dir/` - purpose
## PATTERNS
[1-2 key patterns with minimal code]
## CODE STYLE
See `.eslintrc`, `.prettierrc`
## DOMAIN
| Term | Definition |
## SECURITY
[Auth/validation only]
## GIT
Format: `convention`


Line limits:

Standard: ≤150 lines
Monorepo root: ≤50 lines
Sub-project: ≤100 lines

Target tokens:

Standard: 500-800
Monorepo root: 300-400
Sub-project: 400-600
Resources

Load as needed:

Workflows: workflows.md - All 4 workflows with step-by-step procedures
Optimization: optimization-patterns.md - Token reduction techniques
Validation: validation-rules.md - Quality checklist and scoring
Anti-patterns: anti-patterns.md - Common bloat patterns to avoid
Weekly Installs
27
Repository
alexander-danil…i-skills
GitHub Stars
12
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass