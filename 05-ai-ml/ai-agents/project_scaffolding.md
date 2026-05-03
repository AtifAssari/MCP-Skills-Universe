---
title: project-scaffolding
url: https://skills.sh/autumnsgrove/groveengine/project-scaffolding
---

# project-scaffolding

skills/autumnsgrove/groveengine/project-scaffolding
project-scaffolding
Installation
$ npx skills add https://github.com/autumnsgrove/groveengine --skill project-scaffolding
SKILL.md
Project Scaffolding Skill
When to Activate

Activate this skill when:

Creating new projects from scratch
Setting up project directory structure
Initializing configuration files
Starting from BaseProject template
Setting up technology-specific projects
Quick Setup Methods
Method	Best For	Time
Automated Script	Standard projects	2-3 min
Manual Setup	Custom configurations	10-15 min
Directory Naming Conventions
Directories:     CamelCase (VideoProcessor, AudioTools)
Date-based:      kebab-case with YYYY-MM-DD (logs-2025-01-15)
NO spaces or underscores in directory names

Manual Setup Workflow
Step 1: Copy Template
cp -r /path/to/BaseProject ~/Projects/YourProjectName/
cd ~/Projects/YourProjectName/

Step 2: Clean Git History
rm -rf .git

Step 3: Customize AGENT.md

Fill in project-specific sections:

## Project Purpose
A REST API for managing inventory with real-time updates.

## Tech Stack
- Language: Python 3.11+
- Framework: FastAPI
- Key Libraries: SQLAlchemy, Pydantic
- Package Manager: UV

## Architecture Notes
- Microservices with event-driven updates
- Redis for caching
- PostgreSQL for persistence

Step 4: Initialize Git
git init
git add .
git commit -m "chore: initialize repository from BaseProject"

Technology-Specific Setup
Python with UV
uv init
cp AgentUsage/templates/pyproject.toml.example pyproject.toml
uv add fastapi uvicorn sqlalchemy
uv add --dev pytest black ruff mypy

mkdir -p src/YourProject/{core,utils,config}
mkdir -p tests/{unit,integration}
touch src/YourProject/__init__.py

JavaScript/TypeScript
pnpm init
pnpm add express dotenv
pnpm add -D typescript @types/node jest eslint prettier

mkdir -p src/{routes,controllers,middleware,utils}
touch src/index.ts

Go
go mod init github.com/user/project
mkdir -p cmd/api internal/{handlers,models,database} pkg
touch cmd/api/main.go

Rust
cargo init
mkdir -p src/{routes,models,db}
cargo build

Standard Project Structure
Python
project/
├── src/
│   └── projectname/
│       ├── __init__.py
│       ├── main.py
│       ├── core/
│       ├── utils/
│       └── config/
├── tests/
│   ├── conftest.py
│   ├── unit/
│   └── integration/
├── pyproject.toml
├── uv.lock
├── AGENT.md
└── .gitignore

JavaScript
project/
├── src/
│   ├── index.ts
│   ├── routes/
│   ├── controllers/
│   └── utils/
├── tests/
├── package.json
├── tsconfig.json
├── AGENT.md
└── .gitignore

Secrets Setup
# Create template
cp AgentUsage/templates/secrets_template.json secrets_template.json

# Create actual secrets (gitignored)
cp secrets_template.json secrets.json

# Verify in .gitignore
grep "secrets.json" .gitignore

Task Tracking

Track tasks in GitHub Issues with appropriate labels. Create initial issues for:

Set up project dependencies
Configure secrets management
Create initial project structure
Implement core business logic
Add unit tests
Set up CI/CD pipeline
Verification Checklist
# Git initialized and clean
git status

# AGENT.md customized (no [Fill in:] markers)
grep "\[Fill in:" AGENT.md

# secrets.json in .gitignore
grep "secrets.json" .gitignore

# Dependencies installed
uv sync  # or pnpm install

# Project runs
uv run python src/projectname/main.py

Post-Setup Tasks
Create GitHub Issues for project-specific tasks
Create initial code entry points
Configure IDE settings and extensions
Review relevant guides in AgentUsage/
Common Issues
Permission denied on scripts
chmod +x setup_new_project.sh

Git commit fails
git config user.name "Your Name"
git config user.email "your.email@example.com"

Dependencies not installing
# Python: Clear cache
uv cache clean

# JavaScript: Fresh install
rm -rf node_modules pnpm-lock.yaml
pnpm install

Related Resources

See AgentUsage/project_setup.md and AgentUsage/project_structure.md for:

Detailed directory patterns
CI/CD setup
Pre-commit hook installation
Technology-specific guides
Weekly Installs
73
Repository
autumnsgrove/groveengine
GitHub Stars
5
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass