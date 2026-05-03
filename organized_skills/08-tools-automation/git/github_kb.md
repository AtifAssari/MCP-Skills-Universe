---
rating: ⭐⭐⭐
title: github-kb
url: https://skills.sh/lecion/github-kb/github-kb
---

# github-kb

skills/lecion/github-kb/github-kb
github-kb
Installation
$ npx skills add https://github.com/lecion/github-kb --skill github-kb
SKILL.md
GitHub Knowledge Base Explorer
Installation

Add via Claude Code plugin marketplace:

/plugin marketplace add lecion/github-kb

Configuration

Set the GITHUB_KB_ROOT environment variable to customize the working directory.

Working Directory

Dynamic path based on GITHUB_KB_ROOT environment variable (default: ~/github-kb/).

Knowledge Base Management
CLAUDE.md Location

The knowledge base index is located at {GITHUB_KB_ROOT}/CLAUDE.md. This file indexes all explored repositories.

CLAUDE.md Format
# Claude Code 知识库

本目录包含 X 个 GitHub 项目，涵盖...领域描述

---

## Category Name

### [project-name](/project-name)
Brief description of the project

Updating CLAUDE.md

When cloning or exploring a new repository, update CLAUDE.md to maintain consistency:

Add the project under an appropriate category
Include project name (linked to its directory) and brief description
Update the project count in the header
Workflow
1. Knowledge Base Lookup (First Step)

When user asks about a repository:

Read {GITHUB_KB_ROOT}/CLAUDE.md to check if the project exists
If found, explore the existing directory using Read, Glob, and Grep tools
If not found, proceed to clone
2. Cloning New Repositories

When user wants to explore a new repo or the repo doesn't exist:

cd {GITHUB_KB_ROOT}
git clone <repo-url>

Use HTTPS or SSH based on repo accessibility
Default clone directory is always {GITHUB_KB_ROOT}
3. Exploring and Analyzing

After cloning or when working with existing repos:

Use the Task tool with Explore agent for comprehensive code analysis
Use Glob/Read/Grep for targeted on: architecture, exploration
Focus implementation details, technical decisions, key files
4. Maintaining the Knowledge Base

After successful exploration:

Update CLAUDE.md with new project entry
Include accurate category and description
Ensure links and formatting are correct
Categories for CLAUDE.md

Common categories for organizing projects:

Web Frameworks - Frontend/backend frameworks
DevOps Tools - CI/CD, deployment, infrastructure
Machine Learning - ML libraries, models, tools
Mobile Development - iOS, Android, cross-platform
Utilities - CLI tools, productivity
Databases - Database clients, ORMs
APIs & Services - API clients, SDKs
Other - Projects that don't fit other categories
Environment Variables
Variable	Description	Default
GITHUB_KB_ROOT	Root directory for clones	~/github-kb/
Examples
# Clone a new repository
cd $GITHUB_KB_ROOT
git clone https://github.com/example/repo.git

# Explore an existing repository
Task tool -> Explore agent -> analyze repo structure

# Update knowledge base
Edit CLAUDE.md -> add new project entry

Backward Compatibility

Existing users don't need any configuration changes. The default path maintains backward compatibility.

Weekly Installs
63
Repository
lecion/github-kb
GitHub Stars
2
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn