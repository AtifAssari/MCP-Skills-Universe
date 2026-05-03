---
rating: ⭐⭐
title: advanced-alchemy-types
url: https://skills.sh/alti3/litestar-skills/advanced-alchemy-types
---

# advanced-alchemy-types

skills/alti3/litestar-skills/advanced-alchemy-types
advanced-alchemy-types
Installation
$ npx skills add https://github.com/alti3/litestar-skills --skill advanced-alchemy-types
SKILL.md
Types
Execution Workflow
Choose the column type based on storage semantics, not convenience.
Use DateTimeUTC for timezone-aware timestamps that must normalize to UTC.
Use EncryptedString or EncryptedText only after choosing the encryption backend and key source.
Use GUID, JsonB, PasswordHash, and StoredObject where the database contract truly requires them.
Check migration and dialect behavior before committing to a custom type in a widely used model.
Implementation Rules
Require timezone-aware input for UTC datetime fields.
Never hardcode real encryption keys in model definitions.
Keep type constructor arguments hashable and cache-safe when custom decorators participate in SQLAlchemy statement caching.
Treat file-object and password-hash columns as lifecycle-bearing fields, not plain strings.
Example Pattern
from advanced_alchemy.types import DateTimeUTC, EncryptedString, GUID, JsonB


class User(DefaultBase):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(GUID, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTimeUTC)
    secret: Mapped[str] = mapped_column(EncryptedString(key="secret-key"))
    preferences: Mapped[dict] = mapped_column(JsonB)

Validation Checklist
Confirm the selected type behaves correctly on the target database dialect.
Confirm encrypted and password-hash fields use the intended backend and key management path.
Confirm stored datetimes are timezone-aware and normalized to UTC.
Confirm migrations can render and replay the custom types cleanly.
Cross-Skill Handoffs
Use advanced-alchemy-modeling to place these types on the right models.
Use advanced-alchemy-caching when custom type configuration affects SQLAlchemy cacheability.
Use advanced-alchemy-litestar if file-object or DTO behavior must line up with Litestar transport contracts.
Advanced Alchemy References
https://advanced-alchemy.litestar.dev/latest/usage/types.html
https://docs.advanced-alchemy.litestar.dev/latest/reference/types.html
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