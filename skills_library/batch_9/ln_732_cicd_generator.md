---
title: ln-732-cicd-generator
url: https://skills.sh/levnikolaevich/claude-code-skills/ln-732-cicd-generator
---

# ln-732-cicd-generator

skills/levnikolaevich/claude-code-skills/ln-732-cicd-generator
ln-732-cicd-generator
Installation
$ npx skills add https://github.com/levnikolaevich/claude-code-skills --skill ln-732-cicd-generator
SKILL.md

Paths: File paths (shared/, references/, ../ln-*) are relative to skills repo root. If not found at CWD, locate this SKILL.md directory and go up one level for repo root. If shared/ is missing, fetch files via WebFetch from https://raw.githubusercontent.com/levnikolaevich/claude-code-skills/master/skills/{path}.

ln-732-cicd-generator

Type: L3 Worker Category: 7XX Project Bootstrap

Generates GitHub Actions CI pipeline for automated testing and validation.

Purpose & Scope

Creates CI/CD workflow for GitHub:

Does: Generate .github/workflows/ci.yml with lint, test, build, docker jobs
Does NOT: Configure deployment, manage secrets, set up CD pipelines
Inputs
Input	Source	Description
Stack Type	ln-730 coordinator	backend-dotnet, backend-python
Versions	Auto-detected	Node.js, .NET or Python versions
Frontend Path	Auto-detected	Path to frontend directory
Build Commands	Auto-detected	npm scripts, dotnet/pytest commands
Outputs
File	Purpose	Template
.github/workflows/ci.yml	Main CI pipeline	github_ci_dotnet.template.yml or github_ci_python.template.yml
Workflow
Phase 1: Stack Analysis

Determine which template to use:

Detection	Backend Template
.sln or .csproj present	github_ci_dotnet.template.yml
requirements.txt or pyproject.toml present	github_ci_python.template.yml

Detect commands:

Frontend: Read scripts from package.json (lint, build, test)
.NET: Standard dotnet restore/build/test
Python: pip install, ruff lint, pytest
Phase 2: Variable Substitution

Replace template variables:

Variable	Source	Default
{{NODE_VERSION}}	package.json engines	22
{{DOTNET_VERSION}}	*.csproj TargetFramework	9.0.x
{{PYTHON_VERSION}}	pyproject.toml	3.12
{{FRONTEND_PATH}}	Directory detection	src/frontend
Phase 3: Directory Creation

Create .github/workflows/ directory if not exists.

Phase 4: File Generation

Generate ci.yml from selected template:

Check if workflow already exists (warn before overwrite)
Apply variable substitution
Write to .github/workflows/ci.yml
Validate YAML syntax
Generated Pipeline Structure
Jobs Overview
Job	Purpose	Dependencies
frontend	Lint, build, test React/Vite	None
backend	Build, test .NET or Python	None
docker	Build images, health checks	frontend, backend
Frontend Job Steps
Checkout code
Setup Node.js with caching
Install dependencies (npm ci)
Run linter (npm run lint)
Build application (npm run build)
Run tests (npm test)
Backend Job Steps (.NET)
Checkout code
Setup .NET SDK
Restore dependencies (dotnet restore)
Build (dotnet build)
Run tests (dotnet test)
Backend Job Steps (Python)
Checkout code
Setup Python with pip caching
Install dependencies (pip install -r requirements.txt)
Run linter (ruff check)
Run tests (pytest)
Docker Job Steps
Checkout code
Build images (docker compose build)
Start containers (docker compose up -d)
Wait for startup (30 seconds)
Health check frontend (port 3000)
Health check backend (port 5000/8000)
Show logs on failure
Stop containers (docker compose down)
Triggers
Event	Branches
Push	main, develop
Pull Request	main
Best Practices Applied
Practice	Implementation
Dependency caching	npm cache, pip cache
Pinned versions	actions/checkout@v4, setup-node@v4
Parallel jobs	frontend and backend run in parallel
Fail fast	docker job waits for both to succeed
Clean up	docker compose down runs always
Debug support	logs shown on failure
Quality Criteria

Generated workflow must:

 Pass YAML syntax validation
 Use pinned action versions (not @latest)
 Include dependency caching
 Have health checks for docker job
 Clean up resources on completion
Critical Notes
GitHub Actions Only: This skill generates only GitHub Actions workflows. No Azure/GitLab support.
Template-based: Use templates from references/. Do NOT hardcode workflow contents.
Idempotent: Check if .github/workflows/ exists. Warn before overwriting ci.yml.
Version Detection: Use detected versions, not hardcoded defaults.
Reference Files
File	Purpose
github_ci.template.yml	Full template with comments
github_ci_dotnet.template.yml	Compact .NET stack template
github_ci_python.template.yml	Compact Python stack template
Definition of Done
 .github/workflows/ci.yml generated and passes YAML validation
 Pipeline includes lint, build, test, and docker jobs
 All action versions pinned (not @latest)

Version: 1.1.0 Last Updated: 2026-01-10

Weekly Installs
277
Repository
levnikolaevich/…e-skills
GitHub Stars
445
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn