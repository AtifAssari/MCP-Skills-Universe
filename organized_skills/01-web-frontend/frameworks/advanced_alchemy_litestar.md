---
rating: ⭐⭐
title: advanced-alchemy-litestar
url: https://skills.sh/alti3/litestar-skills/advanced-alchemy-litestar
---

# advanced-alchemy-litestar

skills/alti3/litestar-skills/advanced-alchemy-litestar
advanced-alchemy-litestar
Installation
$ npx skills add https://github.com/alti3/litestar-skills --skill advanced-alchemy-litestar
SKILL.md
Litestar
Execution Workflow
Configure SQLAlchemyAsyncConfig or SQLAlchemySyncConfig and register SQLAlchemyPlugin.
Use the plugin to provide session and engine dependencies instead of hand-rolling request-scoped session management.
Build controllers around services first, and fall back to repository-only patterns only when they stay simpler.
Keep application composition in Litestar(...) and let providers or DI supply services.
Enable CLI database commands and optional session-backend support only after the core CRUD path is stable.
Implementation Rules
Prefer a single canonical plugin configuration per application.
Keep before_send_handler and session dependency keys explicit when changing defaults.
Use controller or handler injection for db_session only when service injection is unnecessary.
Keep DTO or schema shaping close to the controller boundary, not inside repositories.
Example Pattern
from advanced_alchemy.extensions.litestar import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
)
from litestar import Litestar

alchemy_config = SQLAlchemyAsyncConfig(
    connection_string="sqlite+aiosqlite:///test.sqlite",
    before_send_handler="autocommit",
    session_config=AsyncSessionConfig(expire_on_commit=False),
    create_all=True,
)

app = Litestar(plugins=[SQLAlchemyPlugin(config=alchemy_config)])

Validation Checklist
Confirm Litestar injects the expected db_session or renamed dependency.
Confirm request lifecycle commit and rollback behavior matches before_send_handler.
Confirm litestar database commands are available when the plugin is installed.
Confirm route handlers, providers, and DTOs agree on model and schema types.
Cross-Skill Handoffs
Use advanced-alchemy-routing for CRUD route structure.
Use advanced-alchemy-services for service-backed controllers.
Use advanced-alchemy-cli for migration commands exposed through Litestar CLI.
Use litestar-app-setup, litestar-dependency-injection, or litestar-dto for deeper Litestar-only concerns.
Advanced Alchemy References
https://github.com/litestar-org/advanced-alchemy/blob/main/examples/litestar/litestar_service.py
https://advanced-alchemy.litestar.dev/latest/usage/frameworks/litestar.html
https://github.com/litestar-org/advanced-alchemy/blob/main/README.md
Weekly Installs
9
Repository
alti3/litestar-skills
GitHub Stars
5
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykPass