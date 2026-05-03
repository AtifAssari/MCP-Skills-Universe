---
rating: ⭐⭐⭐
title: pyright-type-checker
url: https://skills.sh/bobmatnyc/claude-mpm-skills/pyright-type-checker
---

# pyright-type-checker

skills/bobmatnyc/claude-mpm-skills/pyright-type-checker
pyright-type-checker
Installation
$ npx skills add https://github.com/bobmatnyc/claude-mpm-skills --skill pyright-type-checker
SKILL.md
Pyright - Fast Python Type Checker
progressive_disclosure: entry_point: summary: "Fast Python type checker from Microsoft with VS Code integration and strict modes" when_to_use: - "When needing faster type checking than mypy" - "When using VS Code (Pylance)" - "When requiring stricter type checking" - "When migrating from mypy" quick_start: - "npm install -g pyright" - "Create pyrightconfig.json" - "pyright ." token_estimate: entry: 65-80 full: 3500-4500
Installation
Node.js (Recommended)
# Global installation
npm install -g pyright

# Per-project installation
npm install --save-dev pyright

# Verify installation
pyright --version

VS Code (Pylance)

Pyright powers Pylance extension:

# Install Pylance extension (includes pyright)
code --install-extension ms-python.vscode-pylance

pip Installation
# Community wrapper
pip install pyright

# Note: Still requires Node.js runtime

Configuration
pyrightconfig.json
{
  "include": [
    "src"
  ],
  "exclude": [
    "**/node_modules",
    "**/__pycache__",
    ".venv"
  ],
  "typeCheckingMode": "basic",
  "pythonVersion": "3.11",
  "pythonPlatform": "Linux",
  "reportMissingImports": true,
  "reportMissingTypeStubs": false,
  "strictListInference": true,
  "strictDictionaryInference": true,
  "strictSetInference": true
}

Type Checking Modes

Basic Mode (Default):

{
  "typeCheckingMode": "basic",
  "reportUnusedImport": "warning",
  "reportUnusedVariable": "warning"
}


Standard Mode:

{
  "typeCheckingMode": "standard",
  "reportUnknownParameterType": "error",
  "reportUnknownArgumentType": "error",
  "reportUnknownVariableType": "error"
}


Strict Mode (Maximum type safety):

{
  "typeCheckingMode": "strict",
  "reportPrivateUsage": "error",
  "reportConstantRedefinition": "error",
  "reportIncompatibleMethodOverride": "error",
  "reportIncompatibleVariableOverride": "error",
  "reportUnnecessaryIsInstance": "warning",
  "reportUnnecessaryCast": "warning"
}

Per-File Configuration
# pyright: strict
"""Strict type checking for this file."""

# pyright: basic
"""Basic type checking."""

# pyright: reportGeneralTypeIssues=false
"""Disable specific diagnostics."""

VS Code Integration
settings.json
{
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.diagnosticMode": "workspace",
  "python.analysis.autoImportCompletions": true,
  "python.analysis.inlayHints.functionReturnTypes": true,
  "python.analysis.inlayHints.variableTypes": true,
  "python.analysis.completeFunctionParens": true
}

Workspace Configuration
{
  "python.analysis.extraPaths": [
    "./src",
    "./lib"
  ],
  "python.analysis.stubPath": "./typings",
  "python.analysis.diagnosticSeverityOverrides": {
    "reportUnusedImport": "warning",
    "reportUnusedVariable": "warning",
    "reportGeneralTypeIssues": "error"
  }
}

Type Checking Features
Type Narrowing
from typing import Union

def process(value: Union[str, int]) -> str:
    # Pyright narrows type based on isinstance
    if isinstance(value, str):
        return value.upper()  # value is str here
    else:
        return str(value)  # value is int here

# Type guards
from typing import TypeGuard

def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)

def process_list(items: list[object]) -> None:
    if is_str_list(items):
        # items is list[str] here
        print(", ".join(items))

Protocol Support
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

def render(obj: Drawable) -> None:
    obj.draw()

# Works with structural typing
render(Circle())  # ✓ No explicit inheritance needed

TypedDict
from typing import TypedDict, NotRequired

class User(TypedDict):
    name: str
    age: int
    email: NotRequired[str]  # Optional in Python 3.11+

def create_user(data: User) -> None:
    print(data["name"])  # ✓ Type-safe
    # print(data["missing"])  # ✗ Error

user: User = {
    "name": "Alice",
    "age": 30
}  # ✓ email is optional

Literal Types
from typing import Literal

Mode = Literal["read", "write", "append"]

def open_file(mode: Mode) -> None:
    ...

open_file("read")    # ✓
open_file("delete")  # ✗ Error

Advanced Features
Variance and Generics
from typing import TypeVar, Generic, Sequence

T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

class Reader(Generic[T_co]):
    def read(self) -> T_co: ...

class Writer(Generic[T_contra]):
    def write(self, item: T_contra) -> None: ...

# Covariance: Reader[Dog] is subtype of Reader[Animal]
# Contravariance: Writer[Animal] is subtype of Writer[Dog]

ParamSpec
from typing import ParamSpec, TypeVar, Callable

P = ParamSpec("P")
R = TypeVar("R")

def add_logging(f: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Calling {f.__name__}")
        return f(*args, **kwargs)
    return wrapper

@add_logging
def greet(name: str, age: int) -> str:
    return f"Hello {name}, {age}"

# Type-safe: greet("Alice", 30)

Type Aliases
from typing import TypeAlias

# Simple alias
UserId: TypeAlias = int
Username: TypeAlias = str

# Generic alias
from collections.abc import Sequence
Vector: TypeAlias = Sequence[float]

# Complex alias
JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None

CI/CD Integration
GitHub Actions
name: Type Check

on: [push, pull_request]

jobs:
  typecheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install pyright
        run: npm install -g pyright

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run pyright
        run: pyright

Pre-commit Hook
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: pyright
        name: pyright
        entry: pyright
        language: node
        types: [python]
        pass_filenames: false
        additional_dependencies: ['pyright@1.1.350']

Makefile
.PHONY: typecheck typecheck-strict

typecheck:
	pyright

typecheck-strict:
	pyright --level strict

typecheck-watch:
	pyright --watch

typecheck-stats:
	pyright --stats

Migration from mypy
Configuration Mapping
{
  "// mypy: disallow_untyped_defs": "reportUntypedFunctionDecorator",
  "// mypy: disallow_any_generics": "reportMissingTypeArgument",
  "// mypy: warn_return_any": "reportUnknownArgumentType",
  "// mypy: strict_equality": "reportUnnecessaryComparison",
  "// mypy: warn_unused_ignores": "reportUnnecessaryTypeIgnoreComment"
}

Comment Syntax
# mypy: ignore-errors
# ↓ pyright equivalent
# pyright: reportGeneralTypeIssues=false

# type: ignore
# ↓ pyright equivalent
# pyright: ignore

# type: ignore[error-code]
# ↓ pyright equivalent
# pyright: ignore[reportGeneralTypeIssues]

Gradual Migration
{
  "typeCheckingMode": "basic",
  "include": ["src/new_module"],
  "exclude": ["src/legacy"],
  "reportMissingImports": true,
  "reportMissingTypeStubs": false
}

Performance Optimization
Baseline Performance
# Create performance baseline
pyright --stats --createstub

# Compare after changes
pyright --stats

Watch Mode
# Fast incremental checking
pyright --watch

# With specific path
pyright --watch src/

Parallel Checking
{
  "executionEnvironments": [
    {
      "root": "src",
      "pythonVersion": "3.11"
    },
    {
      "root": "tests",
      "pythonVersion": "3.11",
      "extraPaths": ["src"]
    }
  ]
}

Common Patterns
Optional Handling
from typing import Optional

def get_user(user_id: int) -> Optional[str]:
    return "Alice" if user_id == 1 else None

# Before pyright 1.1.200
user = get_user(1)
if user is not None:
    print(user.upper())

# With pyright type narrowing
user = get_user(1)
if user:  # Narrows to str
    print(user.upper())

Union Narrowing
from typing import Union

def process(value: Union[str, list[str]]) -> str:
    if isinstance(value, list):
        return ", ".join(value)  # value is list[str]
    return value  # value is str

Overload
from typing import overload, Literal

@overload
def open_file(path: str, mode: Literal["r"]) -> str: ...

@overload
def open_file(path: str, mode: Literal["rb"]) -> bytes: ...

def open_file(path: str, mode: str) -> str | bytes:
    if mode == "rb":
        return b"binary data"
    return "text data"

# Type-safe usage
text: str = open_file("file.txt", "r")
data: bytes = open_file("file.bin", "rb")

Assertion Functions
from typing import Never

def assert_never(value: Never) -> Never:
    raise AssertionError(f"Unexpected value: {value}")

def handle_status(status: Literal["success", "error"]) -> None:
    if status == "success":
        print("OK")
    elif status == "error":
        print("Failed")
    else:
        assert_never(status)  # Exhaustiveness check

Pyright vs mypy
Performance Comparison
# Typical project (10K lines)
# mypy: ~5-10 seconds
# pyright: ~1-2 seconds

# Large project (100K lines)
# mypy: ~60-120 seconds
# pyright: ~10-20 seconds

Feature Differences

Pyright Advantages:

5-10x faster type checking
Better type inference
VS Code integration (Pylance)
Active development by Microsoft
Better Protocol support
Superior type narrowing

mypy Advantages:

More mature ecosystem
Plugin system
Finer-grained control
Better documentation
More configuration options
When to Use Pyright
✅ VS Code users
✅ Need fast feedback
✅ Want strict type checking
✅ Modern Python (3.10+)
✅ Starting new projects
When to Use mypy
✅ Existing mypy setup
✅ Need mypy plugins
✅ Non-VS Code editors
✅ Legacy Python (<3.8)
✅ Team prefers mypy
Best Practices
Start with Basic Mode
{
  "typeCheckingMode": "basic",
  "reportMissingImports": true,
  "reportUndefinedVariable": true
}

Gradually Increase Strictness
{
  "typeCheckingMode": "standard",
  "reportUnknownParameterType": "warning",
  "reportUnknownArgumentType": "warning"
}

Use Type Stubs
# Generate stubs for third-party packages
pyright --createstub package_name

# Custom stubs directory
mkdir -p typings

Leverage Inlay Hints
{
  "python.analysis.inlayHints.variableTypes": true,
  "python.analysis.inlayHints.functionReturnTypes": true,
  "python.analysis.inlayHints.callArgumentNames": true
}

Type Coverage
# Check type completeness
pyright --stats

# Output:
# Files analyzed: 42
# Lines of code: 3,421
# Type completeness: 87.3%

Ignore Strategically
# Avoid broad ignores
# pyright: ignore  # ✗ Too broad

# Prefer specific ignores
# pyright: ignore[reportGeneralTypeIssues]  # ✓ Specific

# Or fix the issue
value: str = cast(str, unknown_value)  # ✓ Best

Troubleshooting
Import Resolution
{
  "extraPaths": ["src", "lib"],
  "stubPath": "typings",
  "venvPath": ".",
  "venv": ".venv"
}

Stub Generation
# Generate stubs for package
pyright --createstub requests

# Custom stub location
pyright --createstub requests --outputdir typings

Performance Issues
{
  "exclude": [
    "**/node_modules",
    "**/__pycache__",
    ".venv",
    "build",
    "dist"
  ]
}

VS Code Not Using Pyright
{
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.diagnosticMode": "workspace"
}

Resources

Official:

Pyright Docs
Pylance Extension
Type Checking Mode Guide

Community:

awesome-pyright
Python Type Hints
PEP 484 - Type Hints

Related Skills: mypy, FastAPI, Django, pytest Token Count: ~3,850 tokens

Weekly Installs
150
Repository
bobmatnyc/claud…m-skills
GitHub Stars
40
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass