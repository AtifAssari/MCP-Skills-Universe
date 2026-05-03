---
title: code-formatter-installer
url: https://skills.sh/patricio0312rev/skills/code-formatter-installer
---

# code-formatter-installer

skills/patricio0312rev/skills/code-formatter-installer
code-formatter-installer
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill code-formatter-installer
SKILL.md
Code Formatter & Linter Installer

Establish consistent code formatting and linting across your project.

Core Workflow
Detect stack: Identify language/framework (JS/TS, Python, Go, Rust)
Choose tools: Select appropriate formatters and linters
Generate configs: Create config files with best-practice rules
Add scripts: Include npm/package scripts for format/lint
Configure editor: Provide VS Code, IntelliJ, Vim settings
Setup pre-commit: Add git hooks for automatic formatting
CI integration: Suggest GitHub Actions or CI config
Tool Selection by Stack
JavaScript/TypeScript
Formatter: Prettier
Linter: ESLint + typescript-eslint
Editor: EditorConfig
Hooks: Husky + lint-staged
Python
Formatter: Black + isort
Linter: Ruff or Flake8 + mypy
Hooks: pre-commit
Go
Formatter: gofmt + goimports
Linter: golangci-lint
Rust
Formatter: rustfmt
Linter: clippy
Configuration Templates
Prettier (.prettierrc.json)
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "arrowParens": "avoid"
}

ESLint (.eslintrc.json)
{
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:react/recommended",
    "prettier"
  ],
  "rules": {
    "no-console": "warn",
    "@typescript-eslint/no-unused-vars": "error"
  }
}

EditorConfig (.editorconfig)
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.py]
indent_size = 4

[*.md]
trim_trailing_whitespace = false

Python (pyproject.toml)
[tool.black]
line-length = 100
target-version = ['py311']

[tool.isort]
profile = "black"
line_length = 100

[tool.mypy]
strict = true
warn_return_any = true

Package Scripts
JavaScript/TypeScript (package.json)
{
  "scripts": {
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "lint": "eslint . --ext .ts,.tsx,.js,.jsx",
    "lint:fix": "eslint . --ext .ts,.tsx,.js,.jsx --fix",
    "typecheck": "tsc --noEmit"
  }
}

Python
# Makefile or scripts
format:
	black .
	isort .

lint:
	ruff check .
	mypy .

format-check:
	black --check .
	isort --check .

Git Hooks Setup
Husky + lint-staged (Node.js)
Install dependencies:
npm install --save-dev husky lint-staged
npx husky init

Configure lint-staged (.lintstagedrc.json):
{
  "*.{ts,tsx,js,jsx}": ["eslint --fix", "prettier --write"],
  "*.{json,md,yml}": ["prettier --write"]
}

Add pre-commit hook (.husky/pre-commit):
#!/bin/sh
npx lint-staged

pre-commit (Python)
Create .pre-commit-config.yaml:
repos:
  - repo: https://github.com/psf/black
    rev: 24.1.1
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.0
    hooks:
      - id: ruff
        args: [--fix]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy

Install:
pip install pre-commit
pre-commit install

Editor Configuration
VS Code (settings.json)
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}

VS Code Extensions (.vscode/extensions.json)
{
  "recommendations": [
    "esbenp.prettier-vscode",
    "dbaeumer.vscode-eslint",
    "editorconfig.editorconfig",
    "ms-python.black-formatter"
  ]
}

IntelliJ/WebStorm
Enable: Settings → Languages & Frameworks → JavaScript → Prettier → On save
Enable: Settings → Tools → Actions on Save → Reformat code
CI Integration
GitHub Actions (.github/workflows/lint.yml)
name: Lint

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm run format:check
      - run: npm run lint
      - run: npm run typecheck

Pre-merge checks
# .github/workflows/pr-checks.yml
- name: Check formatting
  run: |
    npm run format:check || {
      echo "Code is not formatted. Run 'npm run format' locally."
      exit 1
    }

Installation Checklist

For every setup, provide:

 Config files (.prettierrc, .eslintrc, .editorconfig, etc.)
 Ignore files (.prettierignore, .eslintignore)
 Package scripts (format, lint, format:check, lint:fix)
 Git hooks (husky/pre-commit)
 Editor settings (.vscode/settings.json)
 CI workflow (.github/workflows/lint.yml)
 Documentation (README section on running lint/format)
Best Practices
Run formatter last: Prettier should override other formatting rules
Extend configs: Use popular presets (Airbnb, Standard, etc.)
Ignore generated files: Add build outputs to ignore files
Make hooks skippable: Allow git commit --no-verify for emergencies
Document process: Add "Code Style" section to CONTRIBUTING.md
Test on clean install: Ensure configs work without local editor setup
Keep rules minimal: Start strict, relax if needed
Common Configurations

See assets/configs/ for ready-to-use config files:

Next.js + TypeScript
React + TypeScript
Node.js + TypeScript
Python FastAPI
Python Django
Bypass Instructions (Emergencies)
# Skip pre-commit hooks
git commit --no-verify

# Skip CI checks (not recommended)
git push --no-verify


Document when bypass is acceptable (hotfixes, emergencies only).

Weekly Installs
93
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass