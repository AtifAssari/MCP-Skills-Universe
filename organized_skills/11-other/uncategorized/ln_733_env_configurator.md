---
rating: ⭐⭐
title: ln-733-env-configurator
url: https://skills.sh/levnikolaevich/claude-code-skills/ln-733-env-configurator
---

# ln-733-env-configurator

skills/levnikolaevich/claude-code-skills/ln-733-env-configurator
ln-733-env-configurator
Installation
$ npx skills add https://github.com/levnikolaevich/claude-code-skills --skill ln-733-env-configurator
SKILL.md

Paths: File paths (shared/, references/, ../ln-*) are relative to skills repo root. If not found at CWD, locate this SKILL.md directory and go up one level for repo root. If shared/ is missing, fetch files via WebFetch from https://raw.githubusercontent.com/levnikolaevich/claude-code-skills/master/skills/{path}.

ln-733-env-configurator

Type: L3 Worker Category: 7XX Project Bootstrap

Configures environment variables for development and production environments.

Purpose & Scope

Creates environment configuration files:

Does: Generate .env files, update .gitignore for secrets protection
Does NOT: Store secrets, manage external secrets managers, configure CI/CD secrets
Inputs
Input	Source	Description
Project Name	Directory name	Used for database/service naming
Backend Port	Stack-dependent	5000 (.NET), 8000 (Python)
Frontend Port	Default	3000
Database Port	Default	5432
Detected Vars	Code analysis	Environment variables found in code
Outputs
File	Purpose	Template
.env.example	Documented template	env_example.template
.env.development	Local development defaults	env_development.template
.env.production	Production placeholders	env_production.template
.gitignore (append)	Secrets protection	gitignore_secrets.template
Workflow
Phase 1: Environment Discovery

Scan project for existing environment usage:

Check for existing .env files
Search code for process.env, os.environ, Configuration[]
Identify which variables are secrets vs configuration

Output: List of required environment variables with types

Phase 2: Variable Classification

Classify discovered variables:

Category	Examples	Treatment
Database	DATABASE_URL, POSTGRES_*	Auto-generate with project name
API Config	API_PORT, LOG_LEVEL	Use detected or defaults
Security	JWT_SECRET, API_KEY	Placeholder with warning
External	REDIS_URL, SMTP_*	Comment out as optional
Phase 3: Template Generation

Generate environment files from templates:

Apply variable substitution
Include all discovered variables
Add comments for undocumented variables
Phase 4: Gitignore Update

Append secrets protection to .gitignore:

Read existing .gitignore (if exists)
Check if secrets patterns already present
Append missing patterns from template
Preserve existing entries
Generated File Structure
.env.example

Documented template with all variables:

Section headers (Database, Backend, Frontend, Security, External)
Descriptive comments for each variable
Safe placeholder values (never real secrets)
Optional variables commented out
.env.development

Ready-to-use development configuration:

Pre-filled values that work with docker-compose
Development-only secrets (clearly marked)
Debug-level logging enabled
.env.production

Production placeholder file:

${VARIABLE} syntax for deployment substitution
Comments indicating required secrets
Production-appropriate defaults (Warning log level)
Security Best Practices
Practice	Implementation
No real secrets	Placeholder values only in templates
Gitignore protection	All .env files except .env.example
Development warnings	Mark dev secrets as insecure
Production guidance	Comments about secrets manager usage
Key rotation reminder	Note about regular secret rotation
Security Notes

Generated files include these security reminders:

Never commit real secrets - .gitignore prevents accidental commits
Use secrets manager - GitHub Secrets, AWS Secrets Manager for production
Rotate secrets regularly - Especially JWT secrets
Strong JWT secrets - Minimum 256 bits (32 bytes)
Restrict CORS - Only allow necessary origins in production
Quality Criteria

Generated files must:

 .env.example contains all required variables
 No real secrets or passwords in any file
 .gitignore updated with secrets patterns
 .env.development works with docker-compose
 .env.production uses placeholder syntax
Critical Notes
Template-based: Use templates from references/. Do NOT hardcode file contents.
Idempotent: Check file existence. Append to .gitignore, don't overwrite.
No Real Secrets: Never generate files with actual passwords or API keys.
Development Safety: Development defaults should work out-of-box with docker-compose.
Reference Files
File	Purpose
env_example.template	Documented .env template
env_development.template	Development defaults
env_production.template	Production placeholders
gitignore_secrets.template	.gitignore additions
Definition of Done
 .env.example, .env.development, .env.production generated
 No real secrets or passwords in any generated file
 .gitignore updated with secrets protection patterns

Version: 1.1.0 Last Updated: 2026-01-10

Weekly Installs
275
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