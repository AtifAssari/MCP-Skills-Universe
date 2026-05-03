---
title: advanced-alchemy-modeling
url: https://skills.sh/alti3/litestar-skills/advanced-alchemy-modeling
---

# advanced-alchemy-modeling

skills/alti3/litestar-skills/advanced-alchemy-modeling
advanced-alchemy-modeling
Installation
$ npx skills add https://github.com/alti3/litestar-skills --skill advanced-alchemy-modeling
SKILL.md
Modeling
Execution Workflow
Choose a base class around key shape and audit needs: BigIntBase, BigIntAuditBase, UUIDBase, UUIDv7Base, or related variants.
Add mixins intentionally: SlugKey for URL slugs, audit columns when timestamps are required, and UniqueMixin when get-or-create semantics matter.
Model relationships with explicit loading strategy such as selectin or joined instead of relying on defaults.
Use UniqueMixin to collapse duplicate creation logic for tags, lookup tables, and many-to-many helper models.
Customize the declarative base only when the built-in bases do not fit an existing schema or database-specific requirement.
Implementation Rules
Pick one primary-key strategy per bounded context and keep it consistent.
Let mixins own their concern; do not duplicate slug or audit columns by hand.
Implement both unique_hash() and unique_filter() whenever UniqueMixin is used.
Keep model classes transport-agnostic and leave request or response shaping to services or framework layers.
Example Pattern
from advanced_alchemy.base import BigIntAuditBase
from advanced_alchemy.mixins import SlugKey, UniqueMixin


class Tag(BigIntAuditBase, SlugKey, UniqueMixin):
    __tablename__ = "tag"

Validation Checklist
Confirm the base class matches the database key and migration strategy.
Confirm relationship loading avoids obvious N+1 behavior in hot paths.
Confirm UniqueMixin criteria match actual uniqueness guarantees.
Confirm timestamps, slugs, and indexes align with the expected query patterns.
Cross-Skill Handoffs
Use advanced-alchemy-types for custom column types on model fields.
Use advanced-alchemy-repositories for CRUD and filtering over these models.
Use advanced-alchemy-services when the model requires schema conversion or business rules.
Advanced Alchemy References
https://advanced-alchemy.litestar.dev/latest/usage/modeling.html
https://github.com/litestar-org/advanced-alchemy/blob/main/README.md
Weekly Installs
11
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