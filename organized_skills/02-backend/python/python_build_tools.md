---
rating: ⭐⭐
title: python:build-tools
url: https://skills.sh/martinffx/claude-code-atelier/python:build-tools
---

# python:build-tools

skills/martinffx/claude-code-atelier/python:build-tools
python:build-tools
Installation
$ npx skills add https://github.com/martinffx/claude-code-atelier --skill python:build-tools
SKILL.md
Python Build Tools

Modern Python development tooling using uv, mise, ruff, basedpyright, and pytest.

Quick Start
Minimal pyproject.toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["fastapi", "pydantic"]

[project.optional-dependencies]
dev = ["pytest>=8.0.0", "ruff>=0.8.0", "basedpyright>=1.0.0"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "UP", "RUF"]

[tool.basedpyright]
typeCheckingMode = "strict"

[tool.pytest.ini_options]
testpaths = ["tests"]

Setup Project
uv init my-project && cd my-project
uv sync
uv add fastapi pydantic
uv add --dev pytest ruff basedpyright

Tool Overview
Tool	Purpose	Replaces
uv	Package management	pip, virtualenv
mise	Version & tasks	pyenv, asdf
ruff	Lint & format	black, isort, flake8
basedpyright	Type checking	mypy
pytest	Testing	unittest
Common Commands
Lint and Format
uv run ruff check --fix .
uv run ruff format .

Type Check
uv run basedpyright
uv run basedpyright src/main.py

Test
uv run pytest
uv run pytest --cov=src --cov-report=html

Manage Dependencies
uv add fastapi
uv add --dev pytest
uv lock --upgrade
uv tree

Mise Configuration

Create .mise.toml for consistent development:

[tools]
python = "3.12"

[tasks.lint]
run = "uv run ruff check --fix ."

[tasks.format]
run = "uv run ruff format ."

[tasks.typecheck]
run = "uv run basedpyright"

[tasks.test]
run = "uv run pytest"

[tasks.check]
depends = ["lint", "format", "typecheck", "test"]


Usage:

mise install
mise run check

Type Hints Example
from decimal import Decimal
from typing import Optional

def calculate_discount(
    total: Decimal,
    rate: Optional[Decimal] = None
) -> Decimal:
    if rate is None:
        rate = Decimal("0.1")
    return total * rate

Best Practices
Use uv for all package management (faster, reliable)
Pin Python version with mise
Configure tools in pyproject.toml
Enable strict type checking
Run checks before commit
References

For detailed configuration and advanced patterns:

references/uv.md - Workspaces, scripts, dependency management
references/ruff.md - Rules, per-file ignores, pre-commit integration
references/basedpyright.md - Type patterns, generics, protocols
Weekly Installs
12
Repository
martinffx/claud…-atelier
GitHub Stars
20
First Seen
Feb 16, 2026