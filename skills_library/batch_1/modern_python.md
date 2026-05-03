---
title: modern-python
url: https://skills.sh/trailofbits/skills/modern-python
---

# modern-python

skills/trailofbits/skills/modern-python
modern-python
Installation
$ npx skills add https://github.com/trailofbits/skills --skill modern-python
Summary

Modern Python project setup with uv, ruff, and ty for Python 3.11+.

Replaces pip, Poetry, black, flake8, mypy, and pre-commit with faster, simpler alternatives from the Astral team
Covers new project creation, dependency management via uv add/uv remove, and linting/formatting/type-checking workflows
Includes migration paths from legacy tooling (requirements.txt, setup.py, flake8+black+isort, mypy/pyright)
Provides decision tree for single-file scripts (PEP 723), simple projects, and distributable packages, plus security tool integration (pip-audit, detect-secrets, shellcheck)
SKILL.md
Modern Python

Guide for modern Python tooling and best practices, based on trailofbits/cookiecutter-python.

When to Use This Skill
Creating a new Python project or package
Setting up pyproject.toml configuration
Configuring development tools (linting, formatting, testing)
Writing Python scripts with external dependencies
Migrating from legacy tools (when user requests it)
When NOT to Use This Skill
User wants to keep legacy tooling: Respect existing workflows if explicitly requested
Python < 3.11 required: These tools target modern Python
Non-Python projects: Mixed codebases where Python isn't primary
Anti-Patterns to Avoid
Avoid	Use Instead
[tool.ty] python-version	[tool.ty.environment] python-version
uv pip install	uv add and uv sync
Editing pyproject.toml manually to add deps	uv add <pkg> / uv remove <pkg>
hatchling build backend	uv_build (simpler, sufficient for most cases)
Poetry	uv (faster, simpler, better ecosystem integration)
requirements.txt	PEP 723 for scripts, pyproject.toml for projects
mypy / pyright	ty (faster, from Astral team)
[project.optional-dependencies] for dev tools	[dependency-groups] (PEP 735)
Manual virtualenv activation (source .venv/bin/activate)	uv run <cmd>
pre-commit	prek (faster, no Python runtime needed)

Key principles:

Always use uv add and uv remove to manage dependencies
Never manually activate or manage virtual environments—use uv run for all commands
Use [dependency-groups] for dev/test/docs dependencies, not [project.optional-dependencies]
Decision Tree
What are you doing?
│
├─ Single-file script with dependencies?
│   └─ Use PEP 723 inline metadata (./references/pep723-scripts.md)
│
├─ New multi-file project (not distributed)?
│   └─ Minimal uv setup (see Quick Start below)
│
├─ New reusable package/library?
│   └─ Full project setup (see Full Setup below)
│
└─ Migrating existing project?
    └─ See Migration Guide below

Tool Overview
Tool	Purpose	Replaces
uv	Package/dependency management	pip, virtualenv, pip-tools, pipx, pyenv
ruff	Linting AND formatting	flake8, black, isort, pyupgrade, pydocstyle
ty	Type checking	mypy, pyright (faster alternative)
pytest	Testing with coverage	unittest
prek	Pre-commit hooks (setup)	pre-commit (faster, Rust-native)
Security Tools
Tool	Purpose	When It Runs
shellcheck	Shell script linting	pre-commit
detect-secrets	Secret detection	pre-commit
actionlint	Workflow syntax validation	pre-commit, CI
zizmor	Workflow security audit	pre-commit, CI
pip-audit	Dependency vulnerability scanning	CI, manual
Dependabot	Automated dependency updates	scheduled

See security-setup.md for configuration and usage.

Quick Start: Minimal Project

For simple multi-file projects not intended for distribution:

# Create project with uv
uv init myproject
cd myproject

# Add dependencies
uv add requests rich

# Add dev dependencies
uv add --group dev pytest ruff ty

# Run code
uv run python src/myproject/main.py

# Run tools
uv run pytest
uv run ruff check .

Full Project Setup

If starting from scratch, ask the user if they prefer to use the Trail of Bits cookiecutter template to bootstrap a complete project with already preconfigured tooling.

uvx cookiecutter gh:trailofbits/cookiecutter-python

1. Create Project Structure
uv init --package myproject
cd myproject


This creates:

myproject/
├── pyproject.toml
├── README.md
├── src/
│   └── myproject/
│       └── __init__.py
└── .python-version

2. Configure pyproject.toml

See pyproject.md for complete configuration reference.

Key sections:

[project]
name = "myproject"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = []

[dependency-groups]
dev = [{include-group = "lint"}, {include-group = "test"}, {include-group = "audit"}]
lint = ["ruff", "ty"]
test = ["pytest", "pytest-cov"]
audit = ["pip-audit"]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["ALL"]
ignore = ["D", "COM812", "ISC001"]

[tool.pytest]
addopts = ["--cov=myproject", "--cov-fail-under=80"]

[tool.ty.terminal]
error-on-warning = true

[tool.ty.environment]
python-version = "3.11"

[tool.ty.rules]
# Strict from day 1 for new projects
possibly-unresolved-reference = "error"
unused-ignore-comment = "warn"

3. Install Dependencies
# Install all dependency groups
uv sync --all-groups

# Or install specific groups
uv sync --group dev

4. Add Makefile
.PHONY: dev lint format test build

dev:
	uv sync --all-groups

lint:
	uv run ruff format --check && uv run ruff check && uv run ty check src/

format:
	uv run ruff format .

test:
	uv run pytest

build:
	uv build

Migration Guide

When a user requests migration from legacy tooling:

From requirements.txt + pip

First, determine the nature of the code:

For standalone scripts: Convert to PEP 723 inline metadata (see pep723-scripts.md)

For projects:

# Initialize uv in existing project
uv init --bare

# Add dependencies using uv (not by editing pyproject.toml)
uv add requests rich  # add each package

# Or import from requirements.txt (review each package before adding)
# Note: Complex version specifiers may need manual handling
grep -v '^#' requirements.txt | grep -v '^-' | grep -v '^\s*$' | while read -r pkg; do
    uv add "$pkg" || echo "Failed to add: $pkg"
done

uv sync


Then:

Delete requirements.txt, requirements-dev.txt
Delete virtual environment (venv/, .venv/)
Add uv.lock to version control
From setup.py / setup.cfg
Run uv init --bare to create pyproject.toml
Use uv add to add each dependency from install_requires
Use uv add --group dev for dev dependencies
Copy non-dependency metadata (name, version, description, etc.) to [project]
Delete setup.py, setup.cfg, MANIFEST.in
From flake8 + black + isort
Remove flake8, black, isort via uv remove
Delete .flake8, pyproject.toml [tool.black], [tool.isort] configs
Add ruff: uv add --group dev ruff
Add ruff configuration (see ruff-config.md)
Run uv run ruff check --fix . to apply fixes
Run uv run ruff format . to format
From mypy / pyright
Remove mypy/pyright via uv remove
Delete mypy.ini, pyrightconfig.json, or [tool.mypy]/[tool.pyright] sections
Add ty: uv add --group dev ty
Run uv run ty check src/
Quick Reference: uv Commands
Command	Description
uv init	Create new project
uv init --package	Create distributable package
uv add <pkg>	Add dependency
uv add --group dev <pkg>	Add to dependency group
uv remove <pkg>	Remove dependency
uv sync	Install dependencies
uv sync --all-groups	Install all dependency groups
uv run <cmd>	Run command in venv
uv run --with <pkg> <cmd>	Run with temporary dependency
uv build	Build package
uv publish	Publish to PyPI
Ad-hoc Dependencies with --with

Use uv run --with for one-off commands that need packages not in your project:

# Run Python with a temporary package
uv run --with requests python -c "import requests; print(requests.get('https://httpbin.org/ip').json())"

# Run a module with temporary deps
uv run --with rich python -m rich.progress

# Multiple packages
uv run --with requests --with rich python script.py

# Combine with project deps (adds to existing venv)
uv run --with httpx pytest  # project deps + httpx


When to use --with vs uv add:

uv add: Package is a project dependency (goes in pyproject.toml/uv.lock)
--with: One-off usage, testing, or scripts outside a project context

See uv-commands.md for complete reference.

Quick Reference: Dependency Groups
[dependency-groups]
dev = ["ruff", "ty"]
test = ["pytest", "pytest-cov", "hypothesis"]
docs = ["sphinx", "myst-parser"]


Install with: uv sync --group dev --group test

Best Practices Checklist
 Use src/ layout for packages
 Set requires-python = ">=3.11"
 Configure ruff with select = ["ALL"] and explicit ignores
 Use ty for type checking
 Enforce test coverage minimum (80%+)
 Use dependency groups instead of extras for dev tools
 Add uv.lock to version control
 Use PEP 723 for standalone scripts
Read Next
migration-checklist.md - Step-by-step migration cleanup
pyproject.md - Complete pyproject.toml reference
uv-commands.md - uv command reference
ruff-config.md - Ruff linting/formatting configuration
testing.md - pytest and coverage setup
pep723-scripts.md - PEP 723 inline script metadata
prek.md - Fast pre-commit hooks with prek
security-setup.md - Security hooks and dependency scanning
dependabot.md - Automated dependency updates
Weekly Installs
3.1K
Repository
trailofbits/skills
GitHub Stars
5.0K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass