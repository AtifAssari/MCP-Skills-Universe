---
title: math-router
url: https://skills.sh/parcadei/continuous-claude-v3/math-router
---

# math-router

skills/parcadei/continuous-claude-v3/math-router
math-router
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill math-router
SKILL.md
Math Router

ALWAYS use this router first for math requests.

Instead of reading individual skill documentation, call the router to get the exact command:

Usage
# Route any math intent to get the CLI command
uv run python scripts/cc_math/math_router.py route "<user's math request>"

Example Workflow
User says: "integrate sin(x) from 0 to pi"
You run: uv run python scripts/cc_math/math_router.py route "integrate sin(x) from 0 to pi"
Router returns:
{
  "command": "uv run python scripts/cc_math/sympy_compute.py integrate \"sin(x)\" --var x --lower 0 --upper pi",
  "confidence": 0.95
}

You execute the returned command
Return result to user
Why Use The Router
Faster: No need to read skill docs
Deterministic: Pattern-based, not LLM inference
Accurate: Extracts arguments correctly
Complete: Covers 32 routes across 7 scripts
Available Routes
Category	Commands
sympy	integrate, diff, solve, simplify, limit, det, eigenvalues, inv, expand, factor, series, laplace, fourier
pint	convert, check
shapely	create, measure, pred, op
z3	prove, sat, optimize
scratchpad	verify, explain
tutor	hint, steps, generate
plot	plot2d, plot3d, latex
List All Commands
# List all available routes
uv run python scripts/cc_math/math_router.py list

# List routes by category
uv run python scripts/cc_math/math_router.py list --category sympy

Fallback

If the router returns {"command": null}, the intent wasn't recognized. Then:

Ask user to clarify
Or use individual skills: /sympy-compute, /z3-solve, /pint-compute, etc.
Weekly Installs
310
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass