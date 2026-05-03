---
rating: ⭐⭐⭐
title: bootstrap-project
url: https://skills.sh/kylelundstedt/dotfiles/bootstrap-project
---

# bootstrap-project

skills/kylelundstedt/dotfiles/bootstrap-project
bootstrap-project
Installation
$ npx skills add https://github.com/kylelundstedt/dotfiles --skill bootstrap-project
SKILL.md
Bootstrap Project

Set up agent context files so Claude Code, Codex, and other AI agents understand a project from the first prompt.

When to Use This Skill

Use when the user:

Wants to start a new project with agent context from the beginning
Opens an existing repo that lacks AGENTS.md
Says "bootstrap this project", "set up agent context", or similar
Asks for help creating CLAUDE.md or AGENTS.md
Steps
1. Determine whether this is a new or existing project

Existing project — the current directory has source files, a README, or a .git directory:

Skip to step 3.

New project — the current directory is not a project, or the user wants to create one:

Ask for:
Project name — used for the directory name (kebab-case, e.g. my-project) and the AGENTS.md heading.
Location — parent directory (default: current directory).
Brief description — purpose, intended stack, key constraints. This replaces file-based inference in step 3.
Create the directory: mkdir -p <location>/<project-name>
cd into it.
Run git init.
Create a .gitignore appropriate for the described stack (e.g. Node, Python, Rust).
2. Guard against overwrites
If AGENTS.md already exists, stop and ask before overwriting.
If CLAUDE.md exists and is not a symlink to AGENTS.md, stop and ask.
If agent_docs/ already exists, skip creating it but mention it.
3. Gather project context

Read (do not modify) the following if they exist:

README.md / README
package.json, pyproject.toml, Cargo.toml, go.mod, or equivalent manifest
Top-level directory listing (one level deep)
CI config (.github/workflows/, .gitlab-ci.yml, Makefile, Justfile, etc.)

For new projects with no files, use the user's description from step 1 instead.

3b. Detect data projects

If the project is a data pipeline or analytics project — indicated by dependencies like dlt, sqlmesh, polars, duckdb in pyproject.toml, the presence of .duckdb files, ingest/ or transform/ directories, or the user's description — suggest the /data-pipelines skill's directory layout:

ingest/          # Extraction and loading scripts
transform/       # SQL models or transformation logic
notebooks/       # marimo notebooks (.py files)
data/            # Local data files (gitignored)


Include this layout in the Directory Structure section of AGENTS.md. For new data projects, create the directories. For existing projects that already have a different layout, document what exists — don't restructure.

Also mention in the Conventions section: "Use the /data-pipelines skill for ingestion, transformation, and analytics work."

4. Write AGENTS.md

Create AGENTS.md in the project root. Use the structure below as a guide — fill every section with specifics from step 3. Omit sections that don't apply. Never leave placeholder text or angle-bracket tokens in the output.

Structure:

Heading — project name.
Opening line — one-sentence purpose.
Stack — language, framework, major dependencies.
Directory Structure — table of key paths and their purpose.
Key Commands — build, test, lint/format, dev server (only those that exist).
Conventions — coding style, naming, branching model, PR process.
Gotchas — non-obvious things an agent should know (env vars, generated files, monorepo quirks, etc.).
5. Create CLAUDE.md symlink
ln -s AGENTS.md CLAUDE.md


Claude Code reads CLAUDE.md for project instructions. The symlink keeps AGENTS.md as the single source of truth. Codex reads AGENTS.md directly — no extra symlink needed.

6. Create agent_docs/ directory
mkdir -p agent_docs


Add agent_docs/README.md so the directory is tracked by git:

# agent_docs

Supplementary context for AI agents working in this repository.
Place architecture decisions, API specs, or onboarding notes here.

7. Report results

Print a summary of what was created:

Created:
  AGENTS.md          — project context for AI agents
  CLAUDE.md          -> AGENTS.md (symlink)
  agent_docs/        — supplementary context directory

Next steps:
  - Review AGENTS.md and refine any sections
  - Add architecture docs or API specs to agent_docs/
  - Commit the new files

Weekly Installs
57
Repository
kylelundstedt/dotfiles
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass