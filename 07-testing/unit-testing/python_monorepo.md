---
rating: ⭐⭐⭐
title: python:monorepo
url: https://skills.sh/martinffx/claude-code-atelier/python:monorepo
---

# python:monorepo

skills/martinffx/claude-code-atelier/python:monorepo
python:monorepo
Installation
$ npx skills add https://github.com/martinffx/claude-code-atelier --skill python:monorepo
SKILL.md
Python Monorepo with uv Workspaces

Modern Python monorepo architecture using uv for workspace management and mise for Python version and task orchestration.

Core Concepts

Monorepo: Single repository containing multiple related packages and applications

uv workspace: Python's answer to npm/pnpm workspaces

Single lock file for entire repo
Shared virtual environment
Cross-package dependency resolution
Directory Structure
my-monorepo/
├── .mise.toml           # Python version + task runner
├── pyproject.toml       # Root workspace config
├── uv.lock              # Unified lock file
├── apps/                # Deployable applications
│   ├── api/
│   └── worker/
└── packages/            # Shared libraries
    ├── core/
    └── utils/

Workspace Configuration

Root pyproject.toml:

[project]
name = "my-monorepo"
version = "0.1.0"
requires-python = ">=3.12"

[tool.uv.workspace]
members = ["apps/*", "packages/*"]

[tool.uv]
dev-dependencies = [
    "pytest>=8.0.0",
    "ruff>=0.8.0",
    "basedpyright>=1.0.0",
]


See references/workspace-config.md for detailed configurations.

Package Linking

Workspace packages reference each other by distribution name:

packages/utils/pyproject.toml:

[project]
name = "my-utils"
dependencies = ["my-core"]


apps/api/pyproject.toml:

[project]
name = "my-api"
dependencies = ["my-core", "my-utils", "fastapi>=0.100.0"]

Cross-Package Import

packages/core/src/my_core/entities.py:

class User:
    def __init__(self, email: str):
        self.email = email


apps/api/src/my_api/main.py:

from my_core.entities import User  # Import from workspace package

def run():
    # App code...

Dependency Direction (Critical)
apps/ → packages/  (Apps depend on packages)
packages/ ⇏ apps/  (Never the reverse)


Rules:

Apps can depend on packages
Packages can depend on other packages
Packages NEVER depend on apps
Avoid circular dependencies
mise Task Runner

.mise.toml:

[tools]
python = "3.12"

[tasks.check]
depends = ["lint", "typecheck", "test"]

[tasks.lint]
run = "uv run ruff check ."


Usage: mise run check

Core uv Commands
uv sync                           # Install all packages
uv add fastapi --package my-api   # Add to specific package
uv add my-core --package my-api   # Add workspace package
uv run pytest                      # Run tests
uv lock --upgrade                 # Update dependencies

Best Practices
Single lock file at root
Shared dev tools (ruff, pytest) in root dev-dependencies
Pin Python version with mise
Apps depend on packages only
Use namespace packages for logical grouping (optional)
References

For detailed patterns:

references/workspace-config.md - pyproject.toml patterns, dependencies, versions
references/docker.md - Multi-stage Docker builds
references/namespace-packages.md - PEP 420 namespace packages
Weekly Installs
13
Repository
martinffx/claud…-atelier
GitHub Stars
20
First Seen
Feb 16, 2026