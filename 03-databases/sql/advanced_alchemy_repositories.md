---
title: advanced-alchemy-repositories
url: https://skills.sh/alti3/litestar-skills/advanced-alchemy-repositories
---

# advanced-alchemy-repositories

skills/alti3/litestar-skills/advanced-alchemy-repositories
advanced-alchemy-repositories
Installation
$ npx skills add https://github.com/alti3/litestar-skills --skill advanced-alchemy-repositories
SKILL.md
Repositories
Execution Workflow
Choose the base repository class that matches the runtime: SQLAlchemyAsyncRepository, SQLAlchemySyncRepository, or a slug or query variant.
Set model_type immediately and keep repositories model-specific.
Use built-in filters and list_and_count() for list endpoints instead of reimplementing pagination logic.
Use bulk helpers for inserts, updates, upserts, and deletes when the workload is batch-shaped.
Keep transaction ownership outside the repository unless the framework integration explicitly handles commit behavior.
Implementation Rules
Keep repositories focused on persistence and query composition, not HTTP contracts.
Prefer repository subclasses over duplicated ad hoc helper functions spread across handlers.
Reach for query repositories only when custom SQL or aggregation work is materially different from standard CRUD.
Keep loader options explicit so relationship behavior is predictable.
Example Pattern
from advanced_alchemy.repository import SQLAlchemyAsyncRepository


class PostRepository(SQLAlchemyAsyncRepository[Post]):
    model_type = Post

Validation Checklist
Confirm the repository type matches the session type.
Confirm model_type points at the intended mapped class.
Confirm list filters, counts, and pagination stay consistent under real data.
Confirm bulk operations are tested against the target database dialect.
Cross-Skill Handoffs
Use advanced-alchemy-modeling before defining repositories.
Use advanced-alchemy-services when handlers need schema conversion or domain rules.
Use advanced-alchemy-routing or a framework skill when repository methods are exposed over HTTP.
Advanced Alchemy References
https://advanced-alchemy.litestar.dev/latest/usage/repositories.html
https://github.com/litestar-org/advanced-alchemy/blob/main/README.md
Weekly Installs
10
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