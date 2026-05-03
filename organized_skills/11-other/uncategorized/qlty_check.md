---
rating: ⭐⭐⭐
title: qlty-check
url: https://skills.sh/parcadei/continuous-claude-v3/qlty-check
---

# qlty-check

skills/parcadei/continuous-claude-v3/qlty-check
qlty-check
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill qlty-check
SKILL.md
Qlty Code Quality

Universal code quality tool supporting 70+ linters for 40+ languages via qlty CLI.

When to Use
Check code for linting issues before commit/handoff
Auto-fix formatting and style issues
Calculate code metrics (complexity, duplication)
Find code smells
Quick Reference
# Check changed files with auto-fix
uv run python -m runtime.harness scripts/qlty_check.py --fix

# Check all files
uv run python -m runtime.harness scripts/qlty_check.py --all

# Format files
uv run python -m runtime.harness scripts/qlty_check.py --fmt

# Get metrics
uv run python -m runtime.harness scripts/qlty_check.py --metrics

# Find code smells
uv run python -m runtime.harness scripts/qlty_check.py --smells

Parameters
Parameter	Description
--check	Run linters (default)
--fix	Auto-fix issues
--all	Process all files, not just changed
--fmt	Format files instead
--metrics	Calculate code metrics
--smells	Find code smells
--paths	Specific files/directories
--level	Min issue level: note/low/medium/high
--cwd	Working directory
--init	Initialize qlty in a repo
--plugins	List available plugins
Common Workflows
After Implementation
# Auto-fix what's possible, see what remains
uv run python -m runtime.harness scripts/qlty_check.py --fix

Quality Report
# Get metrics for changed code
uv run python -m runtime.harness scripts/qlty_check.py --metrics

# Find complexity hotspots
uv run python -m runtime.harness scripts/qlty_check.py --smells

Initialize in New Repo
uv run python -m runtime.harness scripts/qlty_check.py --init --cwd /path/to/repo

Direct CLI (if qlty installed)
# Check changed files
qlty check

# Auto-fix
qlty check --fix

# JSON output
qlty check --json

# Format
qlty fmt

Requirements
qlty CLI: https://github.com/qltysh/qlty
MCP server: servers/qlty/server.py wraps CLI
Config: .qlty/qlty.toml in repo (run qlty init first)
vs Other Tools
Tool	Use Case
qlty	Unified linting, formatting, metrics for any language
ast-grep	Structural code patterns and refactoring
morph	Fast text search
Weekly Installs
303
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass