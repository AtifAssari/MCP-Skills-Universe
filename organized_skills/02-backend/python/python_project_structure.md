---
rating: ⭐⭐⭐
title: python-project-structure
url: https://skills.sh/wshobson/agents/python-project-structure
---

# python-project-structure

skills/wshobson/agents/python-project-structure
python-project-structure
Installation
$ npx skills add https://github.com/wshobson/agents --skill python-project-structure
Summary

Clear module boundaries, explicit public interfaces, and maintainable directory layouts for Python projects.

Define public APIs with __all__ in every module; unlisted members remain internal implementation details
Prefer flat directory structures with minimal nesting; add sub-packages only for genuine sub-domains
Organize by architectural layers (API, services, repositories, models) or business domains depending on project complexity
Keep files focused on a single concept; consider splitting when files exceed 300–500 lines or handle unrelated responsibilities
Use absolute imports and consistent snake_case naming; match file names to their primary class or concept
SKILL.md
Python Project Structure & Module Architecture

Design well-organized Python projects with clear module boundaries, explicit public interfaces, and maintainable directory structures. Good organization makes code discoverable and changes predictable.

When to Use This Skill
Starting a new Python project from scratch
Reorganizing an existing codebase for clarity
Defining module public APIs with __all__
Deciding between flat and nested directory structures
Determining test file placement strategies
Creating reusable library packages
Core Concepts
1. Module Cohesion

Group related code that changes together. A module should have a single, clear purpose.

2. Explicit Interfaces

Define what's public with __all__. Everything not listed is an internal implementation detail.

3. Flat Hierarchies

Prefer shallow directory structures. Add depth only for genuine sub-domains.

4. Consistent Conventions

Apply naming and organization patterns uniformly across the project.

Quick Start
myproject/
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── services/
│       ├── models/
│       └── api/
├── tests/
├── pyproject.toml
└── README.md

Fundamental Patterns
Pattern 1: One Concept Per File

Each file should focus on a single concept or closely related set of functions. Consider splitting when a file:

Handles multiple unrelated responsibilities
Grows beyond 300-500 lines (varies by complexity)
Contains classes that change for different reasons
# Good: Focused files
# user_service.py - User business logic
# user_repository.py - User data access
# user_models.py - User data structures

# Avoid: Kitchen sink files
# user.py - Contains service, repository, models, utilities...

Pattern 2: Explicit Public APIs with __all__

Define the public interface for every module. Unlisted members are internal implementation details.

# mypackage/services/__init__.py
from .user_service import UserService
from .order_service import OrderService
from .exceptions import ServiceError, ValidationError

__all__ = [
    "UserService",
    "OrderService",
    "ServiceError",
    "ValidationError",
]

# Internal helpers remain private by omission
# from .internal_helpers import _validate_input  # Not exported

Pattern 3: Flat Directory Structure

Prefer minimal nesting. Deep hierarchies make imports verbose and navigation difficult.

# Preferred: Flat structure
project/
├── api/
│   ├── routes.py
│   └── middleware.py
├── services/
│   ├── user_service.py
│   └── order_service.py
├── models/
│   ├── user.py
│   └── order.py
└── utils/
    └── validation.py

# Avoid: Deep nesting
project/core/internal/services/impl/user/


Add sub-packages only when there's a genuine sub-domain requiring isolation.

Pattern 4: Test File Organization

Choose one approach and apply it consistently throughout the project.

Option A: Colocated Tests

src/
├── user_service.py
├── test_user_service.py
├── order_service.py
└── test_order_service.py


Benefits: Tests live next to the code they verify. Easy to see coverage gaps.

Option B: Parallel Test Directory

src/
├── services/
│   ├── user_service.py
│   └── order_service.py
tests/
├── services/
│   ├── test_user_service.py
│   └── test_order_service.py


Benefits: Clean separation between production and test code. Standard for larger projects.

Advanced Patterns
Pattern 5: Package Initialization

Use __init__.py to provide a clean public interface for package consumers.

# mypackage/__init__.py
"""MyPackage - A library for doing useful things."""

from .core import MainClass, HelperClass
from .exceptions import PackageError, ConfigError
from .config import Settings

__all__ = [
    "MainClass",
    "HelperClass",
    "PackageError",
    "ConfigError",
    "Settings",
]

__version__ = "1.0.0"


Consumers can then import directly from the package:

from mypackage import MainClass, Settings

Pattern 6: Layered Architecture

Organize code by architectural layer for clear separation of concerns.

myapp/
├── api/           # HTTP handlers, request/response
│   ├── routes/
│   └── middleware/
├── services/      # Business logic
├── repositories/  # Data access
├── models/        # Domain entities
├── schemas/       # API schemas (Pydantic)
└── config/        # Configuration


Each layer should only depend on layers below it, never above.

Pattern 7: Domain-Driven Structure

For complex applications, organize by business domain rather than technical layer.

ecommerce/
├── users/
│   ├── models.py
│   ├── services.py
│   ├── repository.py
│   └── api.py
├── orders/
│   ├── models.py
│   ├── services.py
│   ├── repository.py
│   └── api.py
└── shared/
    ├── database.py
    └── exceptions.py

File and Module Naming
Conventions
Use snake_case for all file and module names: user_repository.py
Avoid abbreviations that obscure meaning: user_repository.py not usr_repo.py
Match class names to file names: UserService in user_service.py
Import Style

Use absolute imports for clarity and reliability:

# Preferred: Absolute imports
from myproject.services import UserService
from myproject.models import User

# Avoid: Relative imports
from ..services import UserService
from . import models


Relative imports can break when modules are moved or reorganized.

Best Practices Summary
Keep files focused - One concept per file, consider splitting at 300-500 lines (varies by complexity)
Define __all__ explicitly - Make public interfaces clear
Prefer flat structures - Add depth only for genuine sub-domains
Use absolute imports - More reliable and clearer
Be consistent - Apply patterns uniformly across the project
Match names to content - File names should describe their purpose
Separate concerns - Keep layers distinct and dependencies flowing one direction
Document your structure - Include a README explaining the organization
Weekly Installs
6.6K
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