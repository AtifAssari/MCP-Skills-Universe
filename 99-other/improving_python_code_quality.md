---
title: improving-python-code-quality
url: https://skills.sh/wdm0006/python-skills/improving-python-code-quality
---

# improving-python-code-quality

skills/wdm0006/python-skills/improving-python-code-quality
improving-python-code-quality
Installation
$ npx skills add https://github.com/wdm0006/python-skills --skill improving-python-code-quality
SKILL.md
Python Code Quality
Quick Reference
Tool	Purpose	Command
ruff	Lint + format	ruff check src && ruff format src
mypy	Type check	mypy src
Ruff Configuration

Minimal config in pyproject.toml:

[tool.ruff]
line-length = 88
target-version = "py310"

[tool.ruff.lint]
select = ["E", "W", "F", "I", "B", "C4", "UP"]


For full configuration options, see RUFF_CONFIG.md.

MyPy Configuration
[tool.mypy]
python_version = "3.10"
disallow_untyped_defs = true
warn_return_any = true


For strict settings and overrides, see MYPY_CONFIG.md.

Type Hints Patterns
# Basic
def process(items: list[str]) -> dict[str, int]: ...

# Optional
def fetch(url: str, timeout: int | None = None) -> bytes: ...

# Callable
def apply(func: Callable[[int], str], value: int) -> str: ...

# Generic
T = TypeVar("T")
def first(items: Sequence[T]) -> T | None: ...


For protocols and advanced patterns, see TYPE_PATTERNS.md.

Common Anti-Patterns
# Bad: Mutable default
def process(items: list = []):  # Bug!
    ...

# Good: None default
def process(items: list | None = None):
    items = items or []
    ...

# Bad: Bare except
try:
    ...
except:
    pass

# Good: Specific exception
try:
    ...
except ValueError as e:
    logger.error(e)

Pythonic Idioms
# Iteration
for item in items:           # Not: for i in range(len(items))
for i, item in enumerate(items):  # When index needed

# Dictionary access
value = d.get(key, default)  # Not: if key in d: value = d[key]

# Context managers
with open(path) as f:        # Not: f = open(path); try: finally: f.close()

# Comprehensions (simple only)
squares = [x**2 for x in numbers]

Module Organization
src/my_library/
├── __init__.py      # Public API exports
├── _internal.py     # Private (underscore prefix)
├── exceptions.py    # Custom exceptions
├── types.py         # Type definitions
└── py.typed         # Type hint marker

Checklist
Code Quality:
- [ ] ruff check passes
- [ ] mypy passes (strict mode)
- [ ] Public API has type hints
- [ ] Public API has docstrings
- [ ] No mutable default arguments
- [ ] Specific exception handling
- [ ] py.typed marker present

Learn More

This skill is based on the Code Quality section of the Guide to Developing High-Quality Python Libraries by Will McGinnis. See these posts for deeper coverage:

Linting & Formatting with Ruff
Understanding McCabe Complexity
Adding Type Hints
Weekly Installs
40
Repository
wdm0006/python-skills
GitHub Stars
24
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass