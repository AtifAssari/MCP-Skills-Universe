---
title: gw-config-management
url: https://skills.sh/mthines/gw-tools/gw-config-management
---

# gw-config-management

skills/mthines/gw-tools/gw-config-management
gw-config-management
Installation
$ npx skills add https://github.com/mthines/gw-tools --skill gw-config-management
SKILL.md
gw Configuration Management

Configure gw-tools for optimal workflows across different project types and team environments.

Rules
Rule	Description
fundamentals	HIGH - Config file location, creation, and precedence
options-reference	HIGH - Complete reference for all config options
setup	HIGH - Initial setup flow, secrets, team onboarding
auto-copy	HIGH - File patterns to copy, what to include/exclude
team-config	MEDIUM - Sharing config, documentation, onboarding
advanced	LOW - Multiple sources, secret management integration
troubleshooting	HIGH - Common issues and solutions
Project-Type Patterns
Pattern	Description
nextjs	MEDIUM - Next.js with Vercel deployment
nodejs-api	MEDIUM - Node.js backend/API services
monorepo	MEDIUM - pnpm/Yarn/npm workspaces
react-spa	MEDIUM - React Single Page Applications
Quick Reference
Task	Command
Initialize config	gw init
Initialize with options	gw init --auto-copy-files .env,secrets/
Interactive setup	gw init --interactive
Clone and initialize	gw init git@github.com:user/repo.git
Sync files to worktree	gw sync feature-branch
Show setup command	gw show-init
Configuration Options
Option	Purpose	Default
$schema	JSON Schema for IDE support	(auto-set)
configVersion	Schema migration version	(auto-managed)
root	Repository root path	Auto-detected
defaultBranch	Source for file copying	"main"
autoCopyFiles	Files to auto-copy	[]
hooks	Pre/post checkout commands	{}
updateStrategy	merge or rebase	"merge"
cleanThreshold	Days before stale	7
autoClean	Background cleanup	false
IDE Autocompletion

The .gw/config.json file includes a $schema property that provides autocompletion and validation in VS Code, JetBrains IDEs, and other editors with JSON Schema support. The schema is automatically added when running gw init.

Key Principles
Set up secrets in defaultBranch first: Source must exist before auto-copy works.
Commit config to version control: Team gets it automatically.
Copy secrets, not dependencies: .env yes, node_modules no.
Use gw show-init for documentation: Generate setup command.
Related Skills
git-worktree-workflows - Using worktrees effectively
autonomous-workflow - Autonomous development workflows
Resources
Project-Type Guides - Configuration guides for common project types
Next.js Setup Example
Monorepo Setup Example
Troubleshooting Guide
Weekly Installs
27
Repository
mthines/gw-tools
GitHub Stars
7
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass