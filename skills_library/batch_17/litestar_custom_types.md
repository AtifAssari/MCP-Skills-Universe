---
title: litestar-custom-types
url: https://skills.sh/alti3/litestar-skills/litestar-custom-types
---

# litestar-custom-types

skills/alti3/litestar-skills/litestar-custom-types
litestar-custom-types
Installation
$ npx skills add https://github.com/alti3/litestar-skills --skill litestar-custom-types
SKILL.md
Custom Types
Execution Workflow
Define the domain type and its canonical wire representation.
Register type decoders/encoders at the appropriate layer.
Ensure OpenAPI schema generation remains accurate for custom values.
Add round-trip tests for decode, business usage, and encode output.
Implementation Rules
Keep serialization behavior stable and backward compatible.
Fail fast with actionable error messages on invalid input.
Avoid ambiguous representations that vary by locale/timezone.
Keep custom type support centralized to prevent drift.
Example Pattern
from datetime import datetime
from litestar import Litestar, get


def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value)

@get("/echo-ts/{value:str}")
async def echo_timestamp(value: datetime) -> dict[str, str]:
    return {"value": value.isoformat()}

app = Litestar(route_handlers=[echo_timestamp], type_decoders=[(datetime, parse_timestamp)])

Validation Checklist
Confirm valid payloads decode to the intended Python types.
Confirm invalid payloads return deterministic client errors.
Confirm encoded responses and generated schemas match actual runtime behavior.
Cross-Skill Handoffs
Use litestar-openapi if schema customization is substantial.
Use litestar-requests and litestar-responses when custom types appear at API boundaries.
Litestar References
https://docs.litestar.dev/latest/usage/custom-types.html
Weekly Installs
15
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