---
title: docs
url: https://skills.sh/mwguerra/claude-code-plugins/docs
---

# docs

skills/mwguerra/claude-code-plugins/docs
docs
Installation
$ npx skills add https://github.com/mwguerra/claude-code-plugins --skill docs
SKILL.md
Docker Documentation Reference Skill
Overview

This skill provides access to comprehensive Docker and Docker Compose documentation. Use this skill to look up exact configurations, command syntax, and best practices before generating any Docker-related files.

Documentation Location

All documentation is stored in: /home/mwguerra/projects/mwguerra/claude-code-plugins/docker-specialist/skills/docs/references/

Directory Structure
references/
├── 01-introduction.md       # Docker concepts, key terms
├── 02-dockerfile.md         # Dockerfile instructions, multi-stage builds
├── 03-compose-fundamentals.md  # Compose file structure, options
├── 04-networking.md         # Network types, DNS, external networks
├── 05-databases.md          # PostgreSQL, MySQL, MongoDB, Redis
├── 06-services.md           # Dependencies, scaling, patterns
├── 07-ports-ssl.md          # Port mapping, Traefik, Nginx SSL
├── 08-volumes.md            # Volume types, persistence, backups
├── 09-environment.md        # Env vars, secrets, .env files
├── 10-architecture.md       # Project structures, folder organization
├── 11-global-local.md       # Global vs project containers
├── 12-examples.md           # Complete working examples
├── 13-commands.md           # Essential Docker commands
├── 14-security.md           # Security best practices
├── 15-port-conflicts.md     # Port conflict resolution
├── 16-restart-strategies.md # Restart policies, data persistence
└── 17-troubleshooting.md    # Common issues and solutions

Usage
When to Use This Skill
Before generating any Dockerfile or compose configuration
When troubleshooting Docker errors
To verify correct command syntax
To find proper configuration patterns
To understand Docker networking
For security best practices
Search Workflow
Identify Topic: Determine what documentation is needed
Navigate to File: Go to relevant documentation file
Read Documentation: Extract exact patterns
Apply Knowledge: Use in configuration generation
Common Lookups
Topic	File
Dockerfile creation	02-dockerfile.md
Compose configuration	03-compose-fundamentals.md
Container networking	04-networking.md
Database setup	05-databases.md
Multi-container apps	06-services.md
SSL/TLS setup	07-ports-ssl.md
Volume management	08-volumes.md
Environment variables	09-environment.md
Project structure	10-architecture.md
Commands reference	13-commands.md
Security	14-security.md
Troubleshooting	17-troubleshooting.md
Documentation Reading Pattern

When reading documentation:

Find the right file: Match topic to documentation file
Read the overview: Understand the concept
Extract code examples: Copy exact patterns
Note configuration options: Review available settings
Check best practices: Apply security and performance tips
Example Usage
Looking up PostgreSQL Configuration
Navigate to 05-databases.md
Find PostgreSQL section
Extract:
Image version
Environment variables
Health check configuration
Volume setup
Network configuration
Looking up Network Configuration
Navigate to 04-networking.md
Find relevant section (bridge, external, internal)
Extract:
Network definition syntax
Service network configuration
DNS resolution patterns
Output

After reading documentation, provide:

Exact configuration pattern from docs
Required settings
Optional configurations
Best practices noted
Security considerations
Weekly Installs
19
Repository
mwguerra/claude…-plugins
GitHub Stars
29
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass