---
title: litestar-dataclasses
url: https://skills.sh/alti3/litestar-skills/litestar-dataclasses
---

# litestar-dataclasses

skills/alti3/litestar-skills/litestar-dataclasses
litestar-dataclasses
Installation
$ npx skills add https://github.com/alti3/litestar-skills --skill litestar-dataclasses
SKILL.md
Dataclasses
Execution Workflow
Define dataclasses for transport boundaries with explicit field types.
Use defaults and optionality intentionally to avoid ambiguous schemas.
Combine with DTO configuration when write/read shapes diverge.
Keep domain entities and transport dataclasses separate when needed.
Implementation Rules
Favor immutable or clearly controlled mutation patterns.
Avoid embedding persistence/session behavior in dataclasses.
Keep field names/schema stable for clients.
Validate nested dataclass behavior in serialization paths.
Example Pattern
from dataclasses import dataclass
from litestar import post

@dataclass
class CreateUser:
    name: str
    email: str

@post("/users")
async def create_user(data: CreateUser) -> dict[str, str]:
    return {"email": data.email}

Validation Checklist
Confirm request binding maps correctly into dataclass fields.
Confirm response serialization matches expected JSON schema.
Confirm DTO include/exclude behavior remains predictable.
Cross-Skill Handoffs
Use litestar-dto for advanced shaping and nested field policy.
Use litestar-plugins when switching to different model ecosystems.
Litestar References
https://docs.litestar.dev/latest/usage/dto/index.html
Weekly Installs
14
Repository
alti3/litestar-skills
GitHub Stars
5
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass