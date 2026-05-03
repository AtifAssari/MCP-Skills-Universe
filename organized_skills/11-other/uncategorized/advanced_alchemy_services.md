---
rating: ⭐⭐
title: advanced-alchemy-services
url: https://skills.sh/alti3/litestar-skills/advanced-alchemy-services
---

# advanced-alchemy-services

skills/alti3/litestar-skills/advanced-alchemy-services
advanced-alchemy-services
Installation
$ npx skills add https://github.com/alti3/litestar-skills --skill advanced-alchemy-services
SKILL.md
Services
Execution Workflow
Start from the repository and wrap it with SQLAlchemyAsyncRepositoryService or SQLAlchemySyncRepositoryService.
Define schema types for create, update, and read flows only where service boundaries need validation or conversion.
Set repository_type, loader options, and match_fields explicitly.
Override create(), update(), or to_model() only for real domain rules such as slug generation or multi-model coordination.
Convert outbound models with to_schema() instead of leaking ORM instances to transport layers.
Implementation Rules
Keep services responsible for business rules, not controller or router concerns.
Accept dictionaries or schema objects, but normalize them consistently through the service.
Use schema conversion intentionally: Pydantic, Msgspec, and attrs are all supported.
Keep multi-repository workflows atomic and explicit about commit behavior.
Example Pattern
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService


class PostService(SQLAlchemyAsyncRepositoryService[Post, PostRepository]):
    repository_type = PostRepository

Validation Checklist
Confirm service input can be converted into models for both create and update paths.
Confirm to_schema() returns the expected response shape for the chosen schema library.
Confirm custom service overrides preserve repository invariants.
Confirm complex operations load the relationships they depend on.
Cross-Skill Handoffs
Use advanced-alchemy-repositories for persistence operations beneath the service.
Use advanced-alchemy-routing when mapping service methods onto CRUD endpoints.
Use advanced-alchemy-litestar, advanced-alchemy-fastapi, or advanced-alchemy-flask for framework DI and request handling.
Advanced Alchemy References
https://advanced-alchemy.litestar.dev/latest/usage/services.html
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
SocketPass
SnykPass