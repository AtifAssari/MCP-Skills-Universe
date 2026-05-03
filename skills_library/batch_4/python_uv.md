---
title: python-uv
url: https://skills.sh/mindrally/skills/python-uv
---

# python-uv

skills/mindrally/skills/python-uv
python-uv
Installation
$ npx skills add https://github.com/mindrally/skills --skill python-uv
SKILL.md
Python Package Management with uv

You are an expert in Python development with uv package management.

Core Directive

All Python dependencies must be installed, synchronized, and locked using uv.

Never use pip, pip-tools, or poetry directly for dependency management.

Dependency Management Commands

For standard projects:

uv add <package>
uv remove <package>
uv sync

Script Management

Execute scripts with proper dependency handling:

uv run script.py

Manual Inline Metadata Configuration

Scripts can specify dependencies via comment blocks:

# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "torch",
#   "torchvision",
#   "opencv-python",
#   "numpy",
#   "matplotlib",
#   "Pillow",
#   "timm",
# ]
# ///
print("some python code")

CLI-Based Script Dependencies
uv add package-name --script script.py
uv remove package-name --script script.py
uv sync --script script.py

Key Principles
Always use uv for all package operations
Prefer inline script metadata for standalone scripts
Use uv run to execute scripts with their dependencies
Keep dependencies locked and synchronized across environments
Never fall back to pip or other package managers
Weekly Installs
392
Repository
mindrally/skills
GitHub Stars
88
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass