---
rating: ⭐⭐⭐
title: forge-init
url: https://skills.sh/fwehrling/forge/forge-init
---

# forge-init

skills/fwehrling/forge/forge-init
forge-init
Installation
$ npx skills add https://github.com/fwehrling/forge --skill forge-init
SKILL.md
/forge-init — FORGE Initialization

Initializes the FORGE framework in a new or existing project.

Workflow

Detect the context:

If a path is provided as argument, initialize that directory
Otherwise, initialize the current directory
Check if FORGE is already initialized (.forge/config.yml exists)
If already initialized: still run Token Saver setup (step 8), then suggest /forge-resume for project work

Detect the tech stack:

Language: TypeScript, Python, Go, Rust, etc. (via tsconfig.json, pyproject.toml, go.mod, Cargo.toml)
Project type: web-app, api, mobile, library, cli (via package.json, framework markers)
Framework: React, Next.js, Angular, Express, Django, FastAPI, Expo, etc.
Package manager: pnpm, npm, yarn, pip, cargo, go modules

Create the FORGE structure:

.forge/
  config.yml              # Main configuration (generated)
  sprint-status.yaml      # Sprint tracking (empty)
  templates/              # Artifact templates
    prd.md
    architecture.md
    story.md
    ux-design.md
    sprint-status.yaml
  workflows/              # Workflow definitions
    quick.yaml
    standard.yaml
    enterprise.yaml
docs/
  stories/                # Stories directory
references/
  agents/                 # Agent personas (copied from FORGE repo)


Generate .forge/config.yml:

Pre-fill project.name, project.type, project.language based on detection
Ask the user to confirm or adjust
Offer the scale choice: quick, standard, enterprise

Generate CLAUDE.md:

If the file does not exist, create it with:
Detected project name and type
List of available FORGE commands
Conventions (commits, tests, branches)
Architecture section (placeholder → to be filled by /forge-architect)
If the file already exists, offer to add the FORGE Commands section

Configure .gitignore:

Add FORGE entries (.forge/secrets/, .forge/audit.log, .env, etc.)

Copy individual skills:

Create .claude/skills/forge-*/SKILL.md for each FORGE command
This gives the user immediate access to all /forge-* commands

Install Token Saver (global, idempotent):

Creates ~/.claude/hooks/output-filter.js (PreToolUse hook that rewrites known verbose commands)
Creates ~/.claude/hooks/token-saver.sh (wrapper that executes commands and filters output)
Patches ~/.claude/settings.json to add the hook and permission
Skips files that already exist (safe to re-run)
Covered commands: git, npm, pnpm, yarn, bun, pip, pytest, go, cargo, docker, make, mvn, gradle, dotnet, swift, tsc

Display the summary:

Detected stack
Created files
Recommended next steps:
/forge-plan to start planning
/forge-status to view the project state
Notes
The shell script forge-init.sh (in .claude/skills/forge/) contains the basic initialization logic
This skill extends the script with advanced detection and Claude interactivity
Never overwrite an existing CLAUDE.md without asking for confirmation
Never overwrite an existing .forge/config.yml → suggest /forge-resume instead
Weekly Installs
14
Repository
fwehrling/forge
GitHub Stars
1
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass