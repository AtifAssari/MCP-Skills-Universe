---
rating: ⭐⭐⭐
title: python-env
url: https://skills.sh/0xdarkmatter/claude-mods/python-env
---

# python-env

skills/0xdarkmatter/claude-mods/python-env
python-env
Installation
$ npx skills add https://github.com/0xdarkmatter/claude-mods --skill python-env
SKILL.md
Python Environment

Fast Python environment management with uv.

Quick Commands
Task	Command
Create venv	uv venv
Install package	uv pip install requests
Install from requirements	uv pip install -r requirements.txt
Run script	uv run python script.py
Show installed	uv pip list
Virtual Environment
# Create venv (instant)
uv venv

# Create with specific Python
uv venv --python 3.11

# Activate (or use uv run)
source .venv/bin/activate  # Unix
.venv\Scripts\activate     # Windows

Package Installation
# Single package
uv pip install requests

# Multiple packages
uv pip install flask sqlalchemy pytest

# With extras
uv pip install "fastapi[all]"

# Version constraints
uv pip install "django>=4.0,<5.0"

# Uninstall
uv pip uninstall requests

Minimal pyproject.toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "httpx>=0.25",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "ruff>=0.1",
]

Project Setup Checklist
mkdir my-project && cd my-project
uv venv
# Create pyproject.toml
uv pip install -e ".[dev]"
uv pip list

Troubleshooting
Issue	Solution
"No Python found"	uv python install 3.11
Wrong Python version	uv venv --python 3.11
Conflicting deps	uv pip compile --resolver=backtracking
Cache issues	uv cache clean
When to Use
Always use uv over pip for speed
Creating virtual environments
Installing packages
Managing dependencies
Running scripts in project context
Additional Resources

For detailed patterns, load:

./references/pyproject-patterns.md - Full pyproject.toml examples, tool configs
./references/dependency-management.md - Lock files, workspaces, private packages
./references/publishing.md - PyPI publishing, versioning, CI/CD
See Also

This is a foundation skill with no prerequisites.

Build on this skill:

python-typing-ops - Type hints for projects
python-pytest-ops - Testing infrastructure
python-fastapi-ops - Web API development
Weekly Installs
50
Repository
0xdarkmatter/claude-mods
GitHub Stars
17
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass