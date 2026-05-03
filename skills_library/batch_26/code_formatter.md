---
title: code-formatter
url: https://skills.sh/curiouslearner/devkit/code-formatter
---

# code-formatter

skills/curiouslearner/devkit/code-formatter
code-formatter
Installation
$ npx skills add https://github.com/curiouslearner/devkit --skill code-formatter
SKILL.md
Code Formatter Skill

Automatically format code across multiple languages with opinionated configurations.

Instructions

You are a code formatting expert. When invoked:

Detect Languages: Identify all code file types in the current directory or specified path

Check for Configs: Look for existing formatting configurations (.prettierrc, .editorconfig, pyproject.toml, etc.)

Apply Formatting: Format code according to:

Existing project configuration (if found)
Language-specific best practices (if no config exists)
Popular style guides (e.g., PEP 8 for Python, StandardJS, Google Style Guide)

Report Changes: Summarize what was formatted and any style decisions made

Supported Languages
JavaScript/TypeScript (Prettier)
Python (Black, autopep8)
Go (gofmt)
Rust (rustfmt)
Java (Google Java Format)
CSS/SCSS/LESS
HTML
JSON/YAML
Markdown
Usage Examples
@code-formatter
@code-formatter src/
@code-formatter --check-only
@code-formatter --language python

Formatting Rules
Use 2 spaces for JavaScript/TypeScript/CSS
Use 4 spaces for Python
Use tabs for Go
Maximum line length: 100 characters (unless project config specifies otherwise)
Always use semicolons in JavaScript (unless project uses StandardJS)
Single quotes preferred for JavaScript (unless project config says otherwise)
Trailing commas in multi-line structures
Notes
Always respect existing project configuration files
Ask before modifying configuration files
Never format generated code or vendor directories
Skip binary files and lock files
Weekly Installs
17
Repository
curiouslearner/devkit
GitHub Stars
26
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass