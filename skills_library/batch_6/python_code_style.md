---
title: python-code-style
url: https://skills.sh/wshobson/agents/python-code-style
---

# python-code-style

skills/wshobson/agents/python-code-style
python-code-style
Installation
$ npx skills add https://github.com/wshobson/agents --skill python-code-style
Summary

Modern Python tooling, naming conventions, type checking, and documentation standards for maintainable codebases.

Configure ruff for unified linting and formatting, replacing flake8, isort, and black with a single fast tool
Set up strict type checking with mypy or pyright to catch errors before runtime
Follow PEP 8 naming conventions: snake_case for functions/variables, PascalCase for classes, SCREAMING_SNAKE_CASE for constants
Write Google-style docstrings for all public APIs with Args, Returns, Raises, and Examples sections
Organize imports in three groups (standard library, third-party, local) and use absolute imports exclusively
SKILL.md
Python Code Style & Documentation

Consistent code style and clear documentation make codebases maintainable and collaborative. This skill covers modern Python tooling, naming conventions, and documentation standards.

When to Use This Skill
Setting up linting and formatting for a new project
Writing or reviewing docstrings
Establishing team coding standards
Configuring ruff, mypy, or pyright
Reviewing code for style consistency
Creating project documentation
Core Concepts
1. Automated Formatting

Let tools handle formatting debates. Configure once, enforce automatically.

2. Consistent Naming

Follow PEP 8 conventions with meaningful, descriptive names.

3. Documentation as Code

Docstrings should be maintained alongside the code they describe.

4. Type Annotations

Modern Python code should include type hints for all public APIs.

Quick Start
# Install modern tooling
pip install ruff mypy

# Configure in pyproject.toml
[tool.ruff]
line-length = 120
target-version = "py312"  # Adjust based on your project's minimum Python version

[tool.mypy]
strict = true

Fundamental Patterns
Pattern 1: Modern Python Tooling

Use ruff as an all-in-one linter and formatter. It replaces flake8, isort, and black with a single fast tool.

# pyproject.toml
[tool.ruff]
line-length = 120
target-version = "py312"  # Adjust based on your project's minimum Python version

[tool.ruff.lint]
select = [
    "E",    # pycodestyle errors
    "W",    # pycodestyle warnings
    "F",    # pyflakes
    "I",    # isort
    "B",    # flake8-bugbear
    "C4",   # flake8-comprehensions
    "UP",   # pyupgrade
    "SIM",  # flake8-simplify
]
ignore = ["E501"]  # Line length handled by formatter

[tool.ruff.format]
quote-style = "double"
indent-style = "space"


Run with:

ruff check --fix .  # Lint and auto-fix
ruff format .       # Format code

Pattern 2: Type Checking Configuration

Configure strict type checking for production code.

# pyproject.toml
[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
warn_unused_ignores = true
disallow_untyped_defs = true
disallow_incomplete_defs = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false


Alternative: Use pyright for faster checking.

[tool.pyright]
pythonVersion = "3.12"
typeCheckingMode = "strict"

Pattern 3: Naming Conventions

Follow PEP 8 with emphasis on clarity over brevity.

Files and Modules:

# Good: Descriptive snake_case
user_repository.py
order_processing.py
http_client.py

# Avoid: Abbreviations
usr_repo.py
ord_proc.py
http_cli.py


Classes and Functions:

# Classes: PascalCase
class UserRepository:
    pass

class HTTPClientFactory:  # Acronyms stay uppercase
    pass

# Functions and variables: snake_case
def get_user_by_email(email: str) -> User | None:
    retry_count = 3
    max_connections = 100


Constants:

# Module-level constants: SCREAMING_SNAKE_CASE
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
API_BASE_URL = "https://api.example.com"

Pattern 4: Import Organization

Group imports in a consistent order: standard library, third-party, local.

# Standard library
import os
from collections.abc import Callable
from typing import Any

# Third-party packages
import httpx
from pydantic import BaseModel
from sqlalchemy import Column

# Local imports
from myproject.models import User
from myproject.services import UserService


Use absolute imports exclusively:

# Preferred
from myproject.utils import retry_decorator

# Avoid relative imports
from ..utils import retry_decorator

Advanced Patterns
Pattern 5: Google-Style Docstrings

Write docstrings for all public classes, methods, and functions.

Simple Function:

def get_user(user_id: str) -> User:
    """Retrieve a user by their unique identifier."""
    ...


Complex Function:

def process_batch(
    items: list[Item],
    max_workers: int = 4,
    on_progress: Callable[[int, int], None] | None = None,
) -> BatchResult:
    """Process items concurrently using a worker pool.

    Processes each item in the batch using the configured number of
    workers. Progress can be monitored via the optional callback.

    Args:
        items: The items to process. Must not be empty.
        max_workers: Maximum concurrent workers. Defaults to 4.
        on_progress: Optional callback receiving (completed, total) counts.

    Returns:
        BatchResult containing succeeded items and any failures with
        their associated exceptions.

    Raises:
        ValueError: If items is empty.
        ProcessingError: If the batch cannot be processed.

    Example:
        >>> result = process_batch(items, max_workers=8)
        >>> print(f"Processed {len(result.succeeded)} items")
    """
    ...


Class Docstring:

class UserService:
    """Service for managing user operations.

    Provides methods for creating, retrieving, updating, and
    deleting users with proper validation and error handling.

    Attributes:
        repository: The data access layer for user persistence.
        logger: Logger instance for operation tracking.

    Example:
        >>> service = UserService(repository, logger)
        >>> user = service.create_user(CreateUserInput(...))
    """

    def __init__(self, repository: UserRepository, logger: Logger) -> None:
        """Initialize the user service.

        Args:
            repository: Data access layer for users.
            logger: Logger for tracking operations.
        """
        self.repository = repository
        self.logger = logger

Pattern 6: Line Length and Formatting

Set line length to 120 characters for modern displays while maintaining readability.

# Good: Readable line breaks
def create_user(
    email: str,
    name: str,
    role: UserRole = UserRole.MEMBER,
    notify: bool = True,
) -> User:
    ...

# Good: Chain method calls clearly
result = (
    db.query(User)
    .filter(User.active == True)
    .order_by(User.created_at.desc())
    .limit(10)
    .all()
)

# Good: Format long strings
error_message = (
    f"Failed to process user {user_id}: "
    f"received status {response.status_code} "
    f"with body {response.text[:100]}"
)

Pattern 7: Project Documentation

README Structure:

# Project Name

Brief description of what the project does.

## Installation

\`\`\`bash
pip install myproject
\`\`\`

## Quick Start

\`\`\`python
from myproject import Client

client = Client(api_key="...")
result = client.process(data)
\`\`\`

## Configuration

Document environment variables and configuration options.

## Development

\`\`\`bash
pip install -e ".[dev]"
pytest
\`\`\`


CHANGELOG Format (Keep a Changelog):

# Changelog

## [Unreleased]

### Added
- New feature X

### Changed
- Modified behavior of Y

### Fixed
- Bug in Z

Best Practices Summary
Use ruff - Single tool for linting and formatting
Enable strict mypy - Catch type errors before runtime
120 character lines - Modern standard for readability
Descriptive names - Clarity over brevity
Absolute imports - More maintainable than relative
Google-style docstrings - Consistent, readable documentation
Document public APIs - Every public function needs a docstring
Keep docs updated - Treat documentation as code
Automate in CI - Run linters on every commit
Target Python 3.10+ - For new projects, Python 3.12+ is recommended for modern language features
Weekly Installs
7.2K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass