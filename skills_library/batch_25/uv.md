---
title: uv
url: https://skills.sh/mitsuhiko/agent-stuff/uv
---

# uv

skills/mitsuhiko/agent-stuff/uv
uv
Installation
$ npx skills add https://github.com/mitsuhiko/agent-stuff --skill uv
SKILL.md
Quick Reference
uv run script.py                   # Run a script
uv run --with requests script.py   # Run with ad-hoc dependency
uv run python -m ast foo.py >/dev/null  # Verify syntax without writing __pycache__
uv add requests                    # Add dependency to project
uv init --script foo.py            # Create script with inline metadata

Inline Script Dependencies
# /// script
# requires-python = ">=3.12"
# dependencies = ["requests"]
# ///


See scripts.md for full details on running scripts, locking, and reproducibility.

Build Backend

Use uv_build for pure Python packages:

[build-system]
requires = ["uv_build>=0.9.28,<0.10.0"]
build-backend = "uv_build"


See build.md for project structure, namespaces, and file inclusion.

Weekly Installs
88
Repository
mitsuhiko/agent-stuff
GitHub Stars
2.2K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn