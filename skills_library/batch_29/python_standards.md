---
title: python-standards
url: https://skills.sh/phrazzld/claude-config/python-standards
---

# python-standards

skills/phrazzld/claude-config/python-standards
python-standards
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill python-standards
SKILL.md
Python Standards

Modern Python with uv + ruff + mypy + pytest. All config in pyproject.toml.

Toolchain
Tool	Purpose
uv	Dependencies + virtual envs (lockfile: uv.lock)
ruff	Linting + formatting (replaces black, isort, flake8)
mypy	Type checking (strict mode)
pytest	Testing + coverage
# Setup
uv init && uv add <deps> && uv sync

# Daily workflow
uv run ruff check . --fix && uv run ruff format .
uv run mypy . && uv run pytest

Type Hints

All functions and classes must have explicit type hints:

def fetch_user(user_id: str) -> User | None:
    """Fetch user by ID."""
    ...

def process_items(items: list[Item]) -> dict[str, int]:
    ...


mypy strict mode:

[tool.mypy]
strict = true
disallow_untyped_defs = true
disallow_any_generics = true

Package Structure

Feature-based, not layer-based:

src/myproject/
  users/           # Domain
    __init__.py    # Public API: __all__ = ['User', 'UserService']
    models.py
    services.py
  orders/          # Another domain
  shared/          # Cross-cutting concerns

Error Handling

Catch specific exceptions with context:

try:
    result = parse_config(path)
except FileNotFoundError:
    logger.warning(f"Config not found: {path}")
    return defaults
except json.JSONDecodeError as e:
    raise ConfigError(f"Invalid JSON in {path}") from e


Never: bare except:, silent swallowing, except Exception.

pyproject.toml

Single source of truth (no setup.py, requirements.txt):

[project]
name = "myproject"
version = "1.0.0"
requires-python = ">=3.11"
dependencies = ["httpx", "pydantic"]

[project.optional-dependencies]
dev = ["pytest", "mypy", "ruff"]

[tool.ruff]
select = ["E", "W", "F", "I", "B", "UP", "SIM", "S", "ANN"]
line-length = 88

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = ["--cov=src", "--cov-fail-under=85"]

Anti-Patterns
Any without documented justification
Layer-based folders (/controllers, /models, /views)
Circular imports
Legacy tools (pip, black+isort, flake8)
Multiple config files
noqa comments without justification
References
testing-patterns.md - pytest, fixtures, parametrize
ruff-config.md - Complete ruff rule configuration
Weekly Installs
26
Repository
phrazzld/claude-config
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass