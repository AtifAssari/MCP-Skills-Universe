---
rating: ⭐⭐
title: fba
url: https://skills.sh/fastapi-practices/skills/fba
---

# fba

skills/fastapi-practices/skills/fba
fba
Installation
$ npx skills add https://github.com/fastapi-practices/skills --skill fba
SKILL.md
FastAPI Best Architecture

Official documentation: https://fastapi-practices.github.io/fastapi_best_architecture_docs/

Core Architecture

Project adopts Three-tier architecture:

Layer	Responsibility
API	Route processing, parameter validation, and response return
Schema	Data transfer objects, request/response data structure definitions
Service	Business logic, data processing, exception handling
CRUD	Database operations (inherits CRUDPlus)
Model	ORM models (inherits Base)
Development Workflow
Define database models (model)
Define data validation models (schema)
Define routes (router)
Write business logic (service)
Write database operations (crud)
Detailed Guides
Module	Document
API	references/api.md
Schema	references/schema.md
Model	references/model.md
Naming	references/naming.md
Plugin	references/plugin.md
Coding Style	references/coding-style.md
Config	references/config.md
CLI

Execute fba -h for more details.

Weekly Installs
200
Repository
fastapi-practices/skills
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass