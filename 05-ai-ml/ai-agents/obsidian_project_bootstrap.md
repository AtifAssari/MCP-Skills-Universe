---
rating: ⭐⭐
title: obsidian-project-bootstrap
url: https://skills.sh/galaxy-dawn/claude-scholar/obsidian-project-bootstrap
---

# obsidian-project-bootstrap

skills/galaxy-dawn/claude-scholar/obsidian-project-bootstrap
obsidian-project-bootstrap
Installation
$ npx skills add https://github.com/galaxy-dawn/claude-scholar --skill obsidian-project-bootstrap
SKILL.md
Obsidian Project Bootstrap

Bootstrap a project knowledge base for the current repository.

Role in the workflow

This is a supporting skill.

Use obsidian-project-memory as the main workflow authority. Use this skill only when a repository still needs its initial binding or rebuild.

When to use
The user says “start a new research project”.
The user has an existing repo with code plus Markdown and wants an Obsidian knowledge base generated automatically.
obsidian-project-memory detects a research-project candidate but no existing binding.
Required input

Resolve the vault path from one of:

explicit user input,
OBSIDIAN_VAULT_PATH.
Procedure
Identify the repository root.
Run a preflight detect step first:
python3 "${CLAUDE_PLUGIN_ROOT}/skills/obsidian-project-memory/scripts/project_kb.py" detect --cwd "$PWD"

Only if the repo is unbound and should be imported, run bootstrap:
python3 "${CLAUDE_PLUGIN_ROOT}/skills/obsidian-project-memory/scripts/project_kb.py" bootstrap --cwd "$PWD" --vault-path "$OBSIDIAN_VAULT_PATH"

Verify that bootstrap created at least:
.claude/project-memory/registry.yaml
.claude/project-memory/<project_id>.md
Research/{project-slug}/00-Hub.md
Research/{project-slug}/01-Plan.md
Research/{project-slug}/Knowledge/Source-Inventory.md
Research/{project-slug}/Knowledge/Codebase-Overview.md
If the imported project still lacks real background or experiment context, switch to an agent-first pass:
read the most informative repo docs and code entry points,
synthesize durable notes into Knowledge/, Papers/, Experiments/, Results/, or Writing/,
avoid placeholder notes.
Summarize the created knowledge base and the next recommended canonical notes to fill in.
Notes
The bootstrap process imports structure and summaries, not raw datasets, caches, checkpoints, or the whole code tree.
Ignore .git, .venv, node_modules, caches, checkpoints, binaries, and other heavy artifacts.
The default vault is compact: 00-Hub.md, 01-Plan.md, Knowledge/, Papers/, Experiments/, Results/, Writing/, Daily/, Archive/.
If python3 is unavailable in the current shell, use the system Python interpreter that can run project_kb.py and say so explicitly.
References
references/BOOTSTRAP-RUNBOOK.md - preflight decisions, failure modes, and post-bootstrap verification
Weekly Installs
45
Repository
galaxy-dawn/cla…-scholar
GitHub Stars
3.5K
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass