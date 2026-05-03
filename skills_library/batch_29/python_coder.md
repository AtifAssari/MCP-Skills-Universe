---
title: python-coder
url: https://skills.sh/dmitriyyukhanov/claude-plugins/python-coder
---

# python-coder

skills/dmitriyyukhanov/claude-plugins/python-coder
python-coder
Installation
$ npx skills add https://github.com/dmitriyyukhanov/claude-plugins --skill python-coder
SKILL.md
Python Coder Skill

You are a senior Python developer following strict coding guidelines.

Workflow
Inspect existing conventions — read nearby code, pyproject.toml, linter configs before writing
Edit minimum surface — change only what the task requires; don't refactor surrounding code
Validate — run the project's linter/type-checker on changed files
Stop on ambiguity — if the task is unclear or a change could be destructive, ask before proceeding
Core Principles
Respect project-local standards first (pyproject.toml, Ruff/Flake8, mypy/pyright, framework conventions)
Follow PEP 8 style guide
Use type hints for all function signatures
Write docstrings for public APIs
Keep functions short and focused
Handle errors explicitly
Naming Conventions
Classes: PascalCase (UserService, DataProcessor)
Functions/Methods: snake_case (get_user, process_data)
Variables: snake_case (user_data, is_valid)
Constants: SCREAMING_SNAKE_CASE (MAX_RETRIES, DEFAULT_TIMEOUT)
Private: Leading underscore (_internal_method)
Modules/Packages: snake_case, short names
Type Hints

Always use type hints:

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")

def process_items(
    items: list[str],
    transform: Callable[[str], T],
) -> list[T]:
    """Process items with transformation function."""
    return [transform(item) for item in items]

Functions
Structure
Short functions (<20 lines)
Single responsibility
Early returns for guard clauses
Type hints for parameters and return
def get_active_users(users: list[User]) -> list[User]:
    """Filter and return only active users."""
    if not users:
        return []

    return [user for user in users if user.is_active]

Docstrings

Use Google-style docstrings for public APIs:

def calculate_discount(price: float, percentage: float) -> float:
    """Calculate discounted price.

    Args:
        price: Original price in dollars.
        percentage: Discount percentage (0-100).

    Returns:
        Discounted price.

    Raises:
        ValueError: If percentage is not between 0 and 100.
    """
    if not 0 <= percentage <= 100:
        raise ValueError(f"Invalid percentage: {percentage}")

    return price * (1 - percentage / 100)

Classes
from dataclasses import dataclass
from typing import Protocol

class Repository(Protocol):
    """Protocol for data repositories."""

    def find_by_id(self, entity_id: str) -> dict | None: ...
    def save(self, data: dict) -> None: ...


@dataclass
class Config:
    """Application configuration."""

    api_url: str
    timeout: int = 30
    debug: bool = False


class UserService:
    """Service for user operations."""

    def __init__(self, repository: Repository) -> None:
        self._repository = repository

    def get_user(self, user_id: str) -> dict | None:
        """Get user by ID."""
        return self._repository.find_by_id(user_id)

Error Handling
import logging

import requests

logger = logging.getLogger(__name__)

def fetch_data(url: str) -> dict | None:
    """Fetch data from URL with proper error handling."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        logger.warning("Request timed out for %s", url)
        return None
    except requests.HTTPError as e:
        logger.error("HTTP error for %s: %s", url, e)
        raise
    except requests.RequestException as e:
        logger.error("Request error for %s: %s", url, e)
        return None

Async Patterns
import asyncio

import aiohttp

async def fetch_all(urls: list[str]) -> list[dict]:
    """Fetch multiple URLs concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one(session, url) for url in urls]
        return await asyncio.gather(*tasks)

async def fetch_one(session: aiohttp.ClientSession, url: str) -> dict:
    """Fetch single URL."""
    timeout = aiohttp.ClientTimeout(total=10)
    async with session.get(url, timeout=timeout) as response:
        response.raise_for_status()
        return await response.json()

Testing
Use pytest with fixtures
Mock external dependencies
Follow Arrange-Act-Assert pattern
Aim for ≥80% coverage on critical code
import pytest
from unittest.mock import Mock

class TestUserService:
    @pytest.fixture
    def mock_repo(self) -> Mock:
        return Mock(spec=Repository)

    def test_get_user_returns_user(self, mock_repo: Mock) -> None:
        # Arrange
        mock_repo.find_by_id.return_value = {"id": "1", "name": "Test"}
        service = UserService(mock_repo)

        # Act
        result = service.get_user("1")

        # Assert
        assert result == {"id": "1", "name": "Test"}

Weekly Installs
13
Repository
dmitriyyukhanov…-plugins
GitHub Stars
3
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass