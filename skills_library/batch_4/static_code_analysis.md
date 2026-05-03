---
title: static-code-analysis
url: https://skills.sh/aj-geddes/useful-ai-prompts/static-code-analysis
---

# static-code-analysis

skills/aj-geddes/useful-ai-prompts/static-code-analysis
static-code-analysis
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill static-code-analysis
SKILL.md
Static Code Analysis
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Use automated tools to analyze code without executing it, catching bugs, security issues, and style violations early.

When to Use
Enforcing coding standards
Security vulnerability detection
Bug prevention
Code review automation
CI/CD pipelines
Pre-commit hooks
Refactoring assistance
Quick Start

Minimal working example:

// .eslintrc.js
module.exports = {
  extends: [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:security/recommended",
  ],
  plugins: ["@typescript-eslint", "security", "import"],
  rules: {
    "no-console": ["warn", { allow: ["error", "warn"] }],
    "no-unused-vars": "error",
    "prefer-const": "error",
    eqeqeq: ["error", "always"],
    "no-eval": "error",
    "security/detect-object-injection": "warn",
    "security/detect-non-literal-regexp": "warn",
    "@typescript-eslint/no-explicit-any": "warn",
    "@typescript-eslint/explicit-function-return-type": "error",
    "import/order": [
      "error",
      {
        groups: [
          "builtin",
          "external",
          "internal",
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
ESLint Configuration	ESLint Configuration
Python Linting (pylint + mypy)	Python Linting (pylint + mypy)
Pre-commit Hooks	Pre-commit Hooks
SonarQube Integration	SonarQube Integration
Custom AST Analysis	Custom AST Analysis
Security Scanning	Security Scanning
Best Practices
✅ DO
Run linters in CI/CD
Use pre-commit hooks
Configure IDE integration
Fix issues incrementally
Document custom rules
Share configuration across team
Automate security scanning
❌ DON'T
Ignore all warnings
Skip linter setup
Commit lint violations
Use overly strict rules initially
Skip security scans
Disable rules without reason
Weekly Installs
376
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass