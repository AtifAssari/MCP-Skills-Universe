---
title: deps-dev
url: https://skills.sh/trancong12102/ccc/deps-dev
---

# deps-dev

skills/trancong12102/ccc/deps-dev
deps-dev
Installation
$ npx skills add https://github.com/trancong12102/ccc --skill deps-dev
SKILL.md
Package Version Lookup

Query deps.dev to get the latest stable version of open source packages.

Usage

Use the Python script at scripts/deps-dev.py.

Get Latest Version
# npm package
python scripts/deps-dev.py package --system npm --package express

# Scoped npm package
python scripts/deps-dev.py package --system npm --package "@types/node"

# PyPI package
python scripts/deps-dev.py package --system pypi --package requests

# Go module
python scripts/deps-dev.py package --system go --package "github.com/gin-gonic/gin"

# Cargo crate
python scripts/deps-dev.py package --system cargo --package serde

# Show recent versions
python scripts/deps-dev.py package --system npm --package express --all-versions

Get Specific Version Details
python scripts/deps-dev.py version --system npm --package express --version 5.0.0

Supported Ecosystems
Ecosystem	System ID
npm	npm
PyPI	pypi
Go	go
Cargo	cargo
Maven	maven
NuGet	nuget
RubyGems	rubygems
Ecosystem Detection

Identify the ecosystem from project files:

package.json → npm
requirements.txt, pyproject.toml → pypi
go.mod → go
Cargo.toml → cargo
pom.xml, build.gradle → maven
*.csproj → nuget
Gemfile → rubygems
Rules
Use --format json for structured output when needed
The script handles URL encoding automatically
Use --all-versions to see recent version history
Weekly Installs
8
Repository
trancong12102/ccc
GitHub Stars
3
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass