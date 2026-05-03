---
title: ruff-formatter
url: https://skills.sh/frizzle-chan/mudd/ruff-formatter
---

# ruff-formatter

skills/frizzle-chan/mudd/ruff-formatter
ruff-formatter
Installation
$ npx skills add https://github.com/frizzle-chan/mudd --skill ruff-formatter
SKILL.md
Ruff Formatter

Fast Python code formatter, drop-in replacement for Black with >99.9% compatibility.

Quick Reference
# Format all files in current directory
ruff format .

# Format specific file(s)
ruff format path/to/file.py

# Check without modifying (CI/pre-commit)
ruff format --check .

# Show diff of what would change
ruff format --diff .

Fixing Formatting Issues

When ruff format --check fails:

Run ruff format . to auto-fix all formatting
Review changes with git diff
Commit the formatted code

For import sorting issues, run linter first:

ruff check --select I --fix .  # Sort imports
ruff format .                   # Then format

Format Suppression

Disable formatting for specific code:

# fmt: off
matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
# fmt: on

x = 1  # fmt: skip

Configuration

In pyproject.toml or ruff.toml:

[tool.ruff.format]
quote-style = "double"      # or "single"
indent-style = "space"      # or "tab"
line-length = 88            # default
docstring-code-format = true

Exit Codes
0: Success (files formatted or already formatted)
1: With --check: files need formatting
2: Error (invalid config, CLI error)
Weekly Installs
30
Repository
frizzle-chan/mudd
GitHub Stars
3
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass