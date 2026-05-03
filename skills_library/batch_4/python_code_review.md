---
title: python-code-review
url: https://skills.sh/existential-birds/beagle/python-code-review
---

# python-code-review

skills/existential-birds/beagle/python-code-review
python-code-review
Installation
$ npx skills add https://github.com/existential-birds/beagle --skill python-code-review
SKILL.md
Python Code Review
Quick Reference
Issue Type	Reference
Indentation, line length, whitespace, naming	references/pep8-style.md
Missing/wrong type hints, Any usage	references/type-safety.md
Blocking calls in async, missing await	references/async-patterns.md
Bare except, missing context, logging	references/error-handling.md
Mutable defaults, print statements	references/common-mistakes.md
Review Checklist
PEP8 Style
 4-space indentation (no tabs)
 Line length ≤79 characters (≤72 for docstrings/comments)
 Two blank lines around top-level definitions, one within classes
 Imports grouped: stdlib → third-party → local (blank line between groups)
 No whitespace inside brackets or before colons/commas
 Naming: snake_case for functions/variables, CamelCase for classes, UPPER_CASE for constants
 Inline comments separated by at least two spaces
Type Safety
 Type hints on all function parameters and return types
 No Any unless necessary (with comment explaining why)
 Proper T | None syntax (Python 3.10+)
Async Patterns
 No blocking calls (time.sleep, requests) in async functions
 Proper await on all coroutines
Error Handling
 No bare except: clauses
 Specific exception types with context
 raise ... from to preserve stack traces
Common Mistakes
 No mutable default arguments
 Using logger not print() for output
 f-strings preferred over .format() or %
Valid Patterns (Do NOT Flag)

These patterns are intentional and correct - do not report as issues:

Type annotation vs type assertion - Annotations declare types but are not runtime assertions; don't confuse with missing validation
Using Any when interacting with untyped libraries - Required when external libraries lack type stubs
Empty __init__.py files - Valid for package structure, no code required
noqa comments - Valid when linter rule doesn't apply to specific case
Using cast() after runtime type check - Correct pattern to inform type checker of narrowed type
Context-Sensitive Rules

Only flag these issues when the specific conditions apply:

Issue	Flag ONLY IF
Generic exception handling	Specific exception types are available and meaningful
Unused variables	Variable lacks _ prefix AND isn't used in f-strings, logging, or debugging
Gates (reporting workflow)

Complete in order. Do not advance until each pass condition is met.

Scope — Pass: You list every .py path (or explicit glob) you inspected this run.
False-positive screen — Pass: For each issue you plan to report, you checked Valid Patterns and Context-Sensitive Rules above; you drop or narrow the finding if those sections say not to flag it.
Evidence — Pass: Each remaining finding includes [FILE:LINE] (or a bounded line range). Symbols or short verbatim snippets may supplement the location anchor but do not replace it.
Verification protocol — Pass: You load review-verification-protocol and complete its mandatory steps for each reported issue before the user-facing write-up.
Ship — Pass: The user-visible output matches whatever structure that protocol requires (no issues-only dump that skips its checks).
When to Load References
Reviewing code formatting/style → pep8-style.md
Reviewing function signatures → type-safety.md
Reviewing async def functions → async-patterns.md
Reviewing try/except blocks → error-handling.md
General Python review → common-mistakes.md
Review Questions
Does the code follow PEP8 formatting (indentation, line length, whitespace)?
Are imports properly grouped (stdlib → third-party → local)?
Do names follow conventions (snake_case, CamelCase, UPPER_CASE)?
Are all function signatures fully typed?
Are async functions truly non-blocking?
Do exceptions include meaningful context?
Are there any mutable default arguments?

Before reporting: complete Gates (reporting workflow) above (especially gate 4).

Weekly Installs
391
Repository
existential-birds/beagle
GitHub Stars
56
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass