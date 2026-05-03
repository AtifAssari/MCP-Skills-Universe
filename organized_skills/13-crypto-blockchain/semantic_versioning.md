---
rating: ⭐⭐
title: semantic-versioning
url: https://skills.sh/aj-geddes/useful-ai-prompts/semantic-versioning
---

# semantic-versioning

skills/aj-geddes/useful-ai-prompts/semantic-versioning
semantic-versioning
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill semantic-versioning
SKILL.md
Semantic Versioning
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Establish semantic versioning practices to maintain consistent version numbering aligned with release significance, enabling automated version management and release notes generation.

When to Use
Package and library releases
API versioning
Version bumping automation
Release note generation
Breaking change tracking
Dependency management
Changelog management
Quick Start

Minimal working example:

# package.json
{
  "name": "my-awesome-package",
  "version": "1.2.3",
  "description": "An awesome package",
  "main": "dist/index.js",
  "repository": { "type": "git", "url": "https://github.com/org/repo.git" },
  "scripts": { "release": "semantic-release" },
  "devDependencies":
    {
      "semantic-release": "^21.0.0",
      "@semantic-release/changelog": "^6.0.0",
      "@semantic-release/git": "^10.0.0",
      "@semantic-release/github": "^9.0.0",
      "conventional-changelog-cli": "^3.0.0",
    },
}

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Semantic Versioning Configuration	Semantic Versioning Configuration
Conventional Commits Format	Conventional Commits Format
Semantic Release Configuration	Semantic Release Configuration
Version Bumping Script	Version Bumping Script
Changelog Generation	Changelog Generation
Best Practices
✅ DO
Follow strict MAJOR.MINOR.PATCH format
Use conventional commits
Automate version bumping
Generate changelogs automatically
Tag releases in git
Document breaking changes
Use prerelease versions for testing
❌ DON'T
Manually bump versions inconsistently
Skip breaking change documentation
Use arbitrary version numbering
Mix features in patch releases
Weekly Installs
333
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