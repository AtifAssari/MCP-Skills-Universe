---
title: python
url: https://skills.sh/i9wa4/dotfiles/python
---

# python

skills/i9wa4/dotfiles/python
python
Installation
$ npx skills add https://github.com/i9wa4/dotfiles --skill python
SKILL.md
Python Skill
1. Python-specific Rules
NEVER: Do not add shebang lines (#!/usr/bin/env python3)
NEVER: Do not set execute permission on Python files
YOU MUST: Always execute with explicit python command
2. Virtual Environment Usage
2.1. When uv.lock Exists

Use uv to execute Python commands:

uv run dbt debug --profiles-dir ~/.dbt --no-use-colors

2.2. When poetry.lock Exists

Create virtual environment with uv referring to the blog article:

https://i9wa4.github.io/blog/2025-06-08-create-uv-venv-with-poetry-pyproject-toml.html
2.3. When uv.lock Does Not Exist

Activate the virtual environment

source .venv/bin/activate


Execute Python commands

dbt debug --profiles-dir ~/.dbt --no-use-colors

Weekly Installs
41
Repository
i9wa4/dotfiles
GitHub Stars
9
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass