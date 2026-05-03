---
rating: ⭐⭐⭐
title: task-runner
url: https://skills.sh/0xdarkmatter/claude-mods/task-runner
---

# task-runner

skills/0xdarkmatter/claude-mods/task-runner
task-runner
Installation
$ npx skills add https://github.com/0xdarkmatter/claude-mods --skill task-runner
SKILL.md
Task Runner
Purpose

Execute project-specific commands using just, a modern command runner that's simpler than make and works cross-platform.

Tools
Tool	Command	Use For
just	just	List available recipes
just	just test	Run specific recipe
Usage Examples
Basic Usage
# List all available recipes
just

# Run a recipe
just test
just build
just lint

# Run recipe with arguments
just deploy production

# Run specific recipe from subdirectory
just --justfile backend/justfile test

Common justfile Recipes
# Example justfile

# Run tests
test:
    pytest tests/

# Build project
build:
    npm run build

# Lint code
lint:
    ruff check .
    eslint src/

# Start development server
dev:
    npm run dev

# Clean build artifacts
clean:
    rm -rf dist/ build/ *.egg-info/

# Deploy to environment
deploy env:
    ./scripts/deploy.sh {{env}}

Discovery
# Check if justfile exists
just --summary

# Show recipe details
just --show test

# List recipes with descriptions
just --list

When to Use
First check: just to see available project commands
Running tests: just test
Building: just build
Any project-specific task
Cross-platform command running
Best Practice

Always check for a justfile when entering a new project:

just --list


This shows what commands are available without reading documentation.

Weekly Installs
35
Repository
0xdarkmatter/claude-mods
GitHub Stars
17
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass