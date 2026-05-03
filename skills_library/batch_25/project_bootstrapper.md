---
title: project_bootstrapper
url: https://skills.sh/vuralserhat86/antigravity-agentic-skills/project_bootstrapper
---

# project_bootstrapper

skills/vuralserhat86/antigravity-agentic-skills/project_bootstrapper
project_bootstrapper
Installation
$ npx skills add https://github.com/vuralserhat86/antigravity-agentic-skills --skill project_bootstrapper
SKILL.md
Project Bootstrapper

Sets up new projects or improves existing projects with development best practices, tooling, documentation, and workflow automation.

When to Use
"set up a new project"
"bootstrap this project"
"add best practices"
"improve project structure"
"set up development tooling"
"initialize project properly"
What It Sets Up
1. Project Structure
Standard directories (src/, tests/, docs/, scripts/, .github/)
Logical file organization
Structure improvements
2. Git Configuration
Comprehensive .gitignore
.gitattributes for line endings/diffs
Git hooks (pre-commit, commit-msg)
Branch protection patterns
Git LFS if needed
3. Documentation
Comprehensive README.md
CONTRIBUTING.md
Code documentation (JSDoc, docstrings)
CHANGELOG.md structure
Architecture docs if complex
4. Testing Setup
Identify/suggest testing framework
Test structure and conventions
Example/template tests
Configure test runners
Coverage reporting
Testing scripts/commands
5. Code Quality Tools
Linters (ESLint, Pylint, etc.)
Formatters (Prettier, Black, etc.)
Type checking (TypeScript, mypy, etc.)
Pre-commit hooks for quality
Editor configs (.editorconfig)
Code quality badges
6. Dependencies Management
Package manager configuration
Organize dependencies
Check security vulnerabilities
Set up dependency updates (Dependabot, Renovate)
Create lock files
Document dependency choices
7. Development Workflow
Useful npm scripts / Makefile targets
Environment variable templates (.env.example)
Docker configuration if appropriate
Development startup scripts
Hot-reload / watch modes
Document development workflow
8. CI/CD Setup
GitHub Actions / GitLab CI config
Automated testing
Automated deployment (if applicable)
Status badges
Release automation
Branch protection
Approach
Discovery Phase

Ask clarifying questions:

Project type: New or existing?
Primary purpose: Web app, library, CLI tool?
Language/framework: JS/TS, Python, Go, etc.?
Collaboration: Personal or team?
Deployment target: Server, cloud, mobile, desktop?
Preferences: Specific tools/frameworks?
Scope: Full setup or specific areas?
Implementation Phase
Analyze existing structure (if existing project)
Create plan based on answers
Show plan and get approval
Implement systematically (one area at a time)
Verify completeness
Provide handoff documentation
Customization

Adapts to:

Language ecosystem: Node.js vs Python vs Go vs Rust
Project size: Small script vs large app
Team size: Solo vs collaborative
Maturity: Startup speed vs enterprise standards
Tools Used
AskUserQuestion: Gather requirements
Write: Create configuration files, documentation
Edit: Update existing files
Bash: Initialize tools (git init, npm init)
Read: Analyze existing structure
Glob: Find files to update
Success Criteria
All standard files present and configured
Clear and complete documentation
Documented development workflow
Automated quality tooling (pre-commit hooks)
Easy test execution
Follows language/framework conventions
Quick developer onboarding
No obvious best practices missing
Templates
Node.js/TypeScript web app
Python CLI tool
Python web API (FastAPI/Flask)
React/Next.js app
Go service
Rust CLI/library
Integration
feature-planning: For planning custom features
code-auditor: For validating setup quality
codebase-documenter: For generating detailed docs
Scope Control
Full bootstrap: Everything from scratch
Partial setup: Specific areas only (e.g., "just add testing")
Improvement pass: Enhance existing project Project Bootstrapper v1.1 - Enhanced
🔄 Workflow

Kaynak: Cookiecutter Documentation & UV Package Manager

Aşama 1: Stack & Tool Selection
 Python: 2025 standardı olarak uv kullan (pip/poetry yerine). pyproject.toml tek konfigürasyon dosyası olsun.
 Node.js: pnpm (disk efficiency) veya bun (speed) tercih et.
 Monorepo: Birden fazla paket varsa Turborepo veya Nx kur.
Aşama 2: Scaffolding (Opinionated Defaults)
 Linter/Formatter: Python için Ruff (tek tool, hepsi içinde), JS için Biome veya ESLint + Prettier.
 Git Hooks: pre-commit (Python) veya husky (JS) ile commit öncesi kalite kontrolü zorunlu kıl.
 Editor config: .editorconfig ve .vscode/extensions.json ile takımın aynı ortamda çalışmasını sağla.
Aşama 3: CI/CD & Documentation
 GitHub Actions: ci.yml (Test & Lint) ve release.yml (NPM/PyPI publish) workflowlarını baştan ekle.
 README: "Nasıl Kurulur", "Nasıl Test Edilir", "Nasıl Katkı Verilir" başlıklarını şablon olarak ekle.
 License: Proje türüne uygun (MIT, Apache 2.0) lisans dosyasını oluştur.
Kontrol Noktaları
Aşama	Doğrulama
1	git clone ve npm install (veya uv sync) sonrası proje hemen çalışıyor mu?
2	CI pipeline'ı ilk commit ile yeşil yanıyor mu?
3	Gizli anahtarlar (.env) gitignore'a ekli mi?
Weekly Installs
9
Repository
vuralserhat86/a…c-skills
GitHub Stars
42
First Seen
Jan 24, 2026