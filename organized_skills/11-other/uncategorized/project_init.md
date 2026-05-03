---
rating: ⭐⭐
title: project-init
url: https://skills.sh/arjenschwarz/agentic-coding/project-init
---

# project-init

skills/arjenschwarz/agentic-coding/project-init
project-init
Installation
$ npx skills add https://github.com/arjenschwarz/agentic-coding --skill project-init
SKILL.md
Project Init

Initialize a project with standard Claude Code configuration.

What It Does
Adds a SessionStart hook to .claude/settings.json for remote environment setup
Detects project languages and adds appropriate tool permissions
Language Detection

The script detects languages based on project files and adds permissions:

Detection File	Language	Permissions Added
go.mod	Go	go, golangci-lint, staticcheck, govulncheck
Package.swift, *.xcodeproj	Swift	swift, xcodebuild, swiftlint, xcrun
package.json	Node.js	npm, npx, node, plus yarn/pnpm/bun if lockfiles present
pyproject.toml, requirements.txt	Python	python, pip, uv, pytest, ruff, mypy
Cargo.toml	Rust	cargo, rustc
Gemfile	Ruby	ruby, bundle, rake, rspec
pom.xml	Java (Maven)	mvn, java
build.gradle	Java (Gradle)	gradle, ./gradlew, java
Dockerfile	Docker	docker, docker-compose
*.tf	Terraform	terraform, tofu
Makefile	Make	make

git is always included.

Usage

Run the setup script from your project directory:

~/.claude/skills/project-init/scripts/setup-project.sh


The script:

Creates .claude/settings.json if it doesn't exist
Merges hooks and permissions into existing settings without overwriting
Is idempotent (safe to run multiple times)
Requires jq for JSON manipulation
Batch Setup

To initialize multiple projects:

for dir in ~/projects/*; do
  (cd "$dir" && ~/.claude/skills/project-init/scripts/setup-project.sh)
done

Weekly Installs
20
Repository
arjenschwarz/ag…c-coding
GitHub Stars
18
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail