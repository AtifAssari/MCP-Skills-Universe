---
title: saiadmin6
url: https://skills.sh/saithink/skills/saiadmin6
---

# saiadmin6

skills/saithink/skills/saiadmin6
saiadmin6
Installation
$ npx skills add https://github.com/saithink/skills --skill saiadmin6
SKILL.md
SaiAdmin Plugin Development

This skill provides guidance on the standard structure and development workflow for SaiAdmin6.x plugins, based on the saiadmin6.x architecture.

Overview

A standard SaiAdmin plugin consists of two main parts:

Backend: Located in server/plugin/<plugin_name>. See Backend Rules.
Frontend: Located in saiadmin-artd/src/views/plugin/<plugin_name>. See Frontend Rules.
Database Standards

All plugin tables must follow standardized structure. See Database Standards for:

Primary key requirements
Required standard fields (status, created_by, updated_by, timestamps)
Complete table creation examples
Naming conventions
Creating a New Plugin
Step 1: Create Backend (Automatic)

Use the built-in SaiAdmin command to generate the backend structure:

Open terminal in server/ directory.
Run: php webman sai:plugin <your_plugin_name>

This command automatically creates:

server/plugin/<your_plugin> directory
config/ files (app, route, middleware, etc.)
app/ directory with admin/controller, api/controller, etc.
A default IndexController.
Step 2: Create Frontend (Manual)
Create directory saiadmin-artd/src/views/plugin/<your_plugin>.
Create api/ directory for API definitions.
Create view directories as needed.
Development Standards

For detailed development standards and code patterns, please refer to:

Database Standards: Covers table structure, required fields, and naming conventions.
Backend Development Rules: Covers Controllers, Models, Validators, and directory structure.
Frontend Development Rules: Covers API definitions, List Pages, Dialogs, and directory structure.
Weekly Installs
9
Repository
saithink/skills
GitHub Stars
3
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass