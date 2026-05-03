---
rating: ⭐⭐⭐
title: legacy-to-ai-ready
url: https://skills.sh/nicepkg/ai-workflow/legacy-to-ai-ready
---

# legacy-to-ai-ready

skills/nicepkg/ai-workflow/legacy-to-ai-ready
legacy-to-ai-ready
Installation
$ npx skills add https://github.com/nicepkg/ai-workflow --skill legacy-to-ai-ready
SKILL.md
Legacy to AI-Ready

Transform legacy codebases into AI-ready projects by generating Claude Code configurations.

Quick Start (5-Minute Setup)

For most projects, start with just CLAUDE.md:

Analyze: python scripts/analyze_codebase.py [path]
Create CLAUDE.md with build commands, code style, architecture overview
Done - Claude can now write code following your project's conventions

Expand to full configuration only when needed.

Interactive Discovery

Before generating configs, ask these questions:

Project Scope:

What is this project? (web app, API, CLI, library)
Primary language and frameworks?
Team size? (solo, small team, enterprise)

Pain Points:

What mistakes do new developers commonly make?
What patterns should always be followed?
What operations are repeated frequently?

Integration Needs:

External services used? (databases, APIs, cloud)
CI/CD pipeline? (GitHub Actions, Jenkins)
Code quality tools? (linters, formatters)
Configuration Decision Tree
Start
│
├─ Small project / Solo dev
│  └─ CLAUDE.md only
│
├─ Team project
│  ├─ Multi-language? → Add .claude/rules/
│  ├─ Complex domain? → Add .claude/skills/
│  ├─ Code reviews? → Add .claude/agents/
│  └─ Repeated tasks? → Add .claude/commands/
│
└─ Enterprise / Large team
   └─ All configurations + MCP servers + Hooks

Generated Configurations
Config	Purpose	When to Create
CLAUDE.md	Project memory (shared)	Always (required)
CLAUDE.local.md	Personal preferences (git-ignored)	Individual customization
.claudeignore	Files Claude should not access	Sensitive files exist
.claude/rules/	Path-specific rules	Multi-module projects
.claude/skills/	Domain knowledge	Complex business logic
.claude/agents/	Task specialists	Repeated review/debug tasks
.claude/commands/	Quick prompts	Common workflows
.claude/settings.json	Hooks + permissions	Auto-formatting, security
MCP servers	External tools	Database/API integrations
Workflow
Phase 1: Automated Analysis
python scripts/analyze_codebase.py [project-path]


The script detects:

Languages and frameworks
Directory structure patterns
Development tools (linters, formatters)
Git commit patterns
Environment variables
Code style indicators
CI/CD configurations (GitHub Actions, etc.)
Sensitive files (warns about .env, credentials)

Output includes:

Recommendations for which configs to create
Security warnings for sensitive files
Suggested .claudeignore patterns
Phase 2: Context Gathering

Claude should read:

3-5 representative source files - understand naming, patterns
Test files - understand testing approach
Config files - package.json, tsconfig, etc.
README/docs - project overview
Recent commits - understand commit style
Phase 2.5: Discover Existing Resources

Before creating custom configs, search for existing skills and MCP servers:

Search skill marketplaces - SkillsMP, SkillHub.club, Claude Skills Hub
Check GitHub repositories - awesome-claude-skills, themed skill collections
Find relevant MCP servers - Glama, MCP Market, official registry

See references/resource-discovery.md for complete directory of sources.

Tip: Many common needs (git commit, code review, database patterns) already have well-maintained skills available.

Phase 3: Generate Configurations
1. CLAUDE.md (Required)

Create at project root with:

Quick reference commands (build, test, lint)
Naming conventions
Architecture overview
Testing guidelines
Git workflow

See references/claude-md-patterns.md.

2. Rules (If Multi-Module)

Create .claude/rules/ when:

Multiple languages need different conventions
Modules have distinct patterns (frontend/backend)
Path-specific requirements exist

See references/rules-patterns.md.

3. Skills (If Complex Domain)

Create .claude/skills/ when:

Domain-specific workflows exist (database, API patterns)
Team knowledge needs preservation
Complex procedures are repeated

See references/skills-patterns.md.

4. Subagents (If Specialized Tasks)

Create .claude/agents/ for:

Code review automation
Debugging assistance
Security auditing
Documentation generation

See references/agents-patterns.md.

5. Commands (If Common Operations)

Create .claude/commands/ for:

Git commit workflow
PR review process
Deployment steps
Test running

See references/commands-patterns.md.

6. Hooks (If Auto-Formatting Needed)

Configure .claude/settings.json for:

Auto-format on file edit
Protected files
Command logging

See references/hooks-patterns.md.

7. MCP Servers (If External Integrations)

Configure MCP for:

Database access
GitHub integration
Slack notifications
Custom internal tools

See references/mcp-patterns.md.

Phase 4: Validate
Ask Claude to perform a typical task
Verify it follows project conventions
Iterate based on gaps discovered
Output Structure

Minimal (small projects):

project/
├── CLAUDE.md
└── [existing files]


Standard (team projects):

project/
├── CLAUDE.md
├── .claude/
│   ├── rules/
│   │   └── code-style.md
│   └── commands/
│       └── commit.md
└── [existing files]


Complete (enterprise):

project/
├── CLAUDE.md              # Shared project memory
├── CLAUDE.local.md        # Personal (git-ignored)
├── .claudeignore          # Files to protect
├── .claude/
│   ├── settings.json      # Hooks + permissions
│   ├── rules/
│   ├── skills/
│   ├── agents/
│   └── commands/
└── [existing files]

Reference Materials
Reference	When to Read
examples.md	Complete real-world examples
resource-discovery.md	Find existing skills & MCP servers
advanced-patterns.md	Migrations, team collab, monorepos
claude-md-patterns.md	Creating CLAUDE.md
rules-patterns.md	Module-specific rules
skills-patterns.md	Domain knowledge
agents-patterns.md	Task specialists
commands-patterns.md	Quick prompts
hooks-patterns.md	Auto-formatting
mcp-patterns.md	External tools
Templates & Bundled Skills

Templates:

assets/CLAUDE.md.template - Project memory template
assets/settings.json.template - Hooks configuration
assets/claudeignore.template - File ignore patterns

Bundled skills to install in target project:

assets/skill-creator/ - For creating new project-specific skills
assets/skill-downloader/ - For downloading additional skills
assets/resource-scout/ - For discovering existing skills & MCP servers
Installing Bundled Skills

Copy these skills to the target project's .claude/skills/ directory:

cp -r assets/skill-creator [target-project]/.claude/skills/
cp -r assets/skill-downloader [target-project]/.claude/skills/
cp -r assets/resource-scout [target-project]/.claude/skills/


This enables the target project to:

resource-scout - Discover existing skills & MCP servers before building custom
skill-downloader - Download and install skills from GitHub or archives
skill-creator - Create custom skills tailored to their domain
Language Quick Reference
TypeScript/JavaScript
Extract: eslint, prettier, tsconfig
Hooks: prettier auto-format
Skills: API patterns, component patterns
Python
Extract: black, ruff, mypy, pyproject.toml
Hooks: black/ruff auto-format
Skills: API patterns, ORM patterns
Go
Extract: gofmt, golangci-lint
Hooks: gofmt auto-format
Skills: error handling patterns
Rust
Extract: rustfmt, clippy
Hooks: rustfmt auto-format
Skills: error handling, async patterns
Weekly Installs
210
Repository
nicepkg/ai-workflow
GitHub Stars
176
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn