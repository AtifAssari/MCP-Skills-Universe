---
title: context-loader
url: https://skills.sh/del-taiseiozaki/claude-code-orchestra/context-loader
---

# context-loader

skills/del-taiseiozaki/claude-code-orchestra/context-loader
context-loader
Installation
$ npx skills add https://github.com/del-taiseiozaki/claude-code-orchestra --skill context-loader
SKILL.md
Context Loader Skill
Purpose

Load shared project context from .claude/ directory to ensure Codex CLI has the same knowledge as Claude Code.

When to Activate

ALWAYS - This skill must run at the beginning of every task to load project context.

Workflow
Step 1: Load Coding Rules

Read all files in .claude/rules/:

.claude/rules/
├── coding-principles.md   # Simplicity, single responsibility, early return
├── dev-environment.md     # uv, ruff, ty, pytest requirements
├── language.md            # Think in English, respond in Japanese
├── security.md            # Secrets, validation, SQLi/XSS prevention
├── testing.md             # TDD, AAA pattern, 80% coverage
└── codex-delegation.md    # (skip - not relevant for Codex itself)

Step 2: Load Design Documentation

Read .claude/docs/DESIGN.md for:

Architecture decisions
Implementation patterns
Library choices and constraints
TODO items and open questions
Step 3: Check Library Documentation

If the task involves specific libraries, read relevant files from:

.claude/docs/libraries/

Step 4: Execute Task

With the loaded context, execute the requested task following:

Coding principles from rules
Design decisions from DESIGN.md
Library constraints from docs
Key Rules to Remember

After loading, always follow these principles:

Simplicity first - Choose readable code over complex
Single responsibility - One function/class does one thing
Type hints required - All functions need annotations
Use uv - Never use pip directly
Security - No hardcoded secrets, validate input, parameterize SQL
Language Protocol
Thinking/Reasoning: English
Code: English (variables, functions, comments)
User communication: Japanese (when reporting back through Claude Code)
Output

After loading context, briefly confirm:

Rules loaded
Design document status
Ready to execute task
Weekly Installs
15
Repository
del-taiseiozaki…rchestra
GitHub Stars
135
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass