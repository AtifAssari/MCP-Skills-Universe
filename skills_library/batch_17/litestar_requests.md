---
title: litestar-requests
url: https://skills.sh/alti3/litestar-skills/litestar-requests
---

# litestar-requests

skills/alti3/litestar-skills/litestar-requests
litestar-requests
Installation
$ npx skills add https://github.com/alti3/litestar-skills --skill litestar-requests
SKILL.md
Requests
Execution Workflow
Choose the narrowest input mechanism that matches the contract: typed parameters, structured body data, or raw Request access.
Type every path, query, header, and cookie input explicitly.
Use Parameter(...) and Body(...) metadata when aliases, constraints, content type, or documentation need to be explicit.
Reach for Request only when you need raw body access, connection metadata, auth context, or request-scoped state.
Handle forms, multipart, and uploads with explicit media type and size/security expectations.
Keep transport validation separate from business-domain validation.
Core Rules
Prefer typed handler parameters over manual parsing from request.
Prefer structured body models over untyped dict[str, object] payloads when the schema is known.
Keep aliases and constraints close to the parameter definition with Parameter(...) or Body(...).
Use precise domain types such as UUID, enums, dataclasses, and validated models where possible.
Use raw Request access only when the handler genuinely needs request metadata or raw-body methods.
Treat multipart and file uploads as explicit transport choices with bounded resource usage.
Keep malformed-input behavior deterministic and consistent with the exception-handling strategy.
Decision Guide
Use normal function parameters for path, query, header, and cookie data.
Use Parameter(...) when aliasing, validation constraints, or source selection must be explicit.
Use a structured data parameter for JSON or other modeled body content.
Use Body(...) when body metadata or request encoding must be declared explicitly.
Use Request when you need headers, cookies, query_params, url, client, user, auth, state, or raw body methods.
Use multipart plus UploadFile only when the endpoint actually needs file transport.
Reference Files

Read only the sections you need:

For path, query, header, cookie, and structured body patterns, read references/parameter-and-body-patterns.md.
For raw Request access, request metadata, raw-body methods, forms, multipart, and uploads, read references/request-object-and-upload-patterns.md.
Recommended Defaults
Use explicit aliases only when the wire contract requires them.
Prefer keyword arguments and readable parameter names over transport-parsing logic in the handler body.
Keep request metadata access minimal and intentional.
Validate file size and content expectations before reading large uploads fully into memory.
Keep request parsing behavior aligned with documented OpenAPI contracts.
Anti-Patterns
Parsing every input manually from request when typed parameters already express the contract.
Accepting opaque untyped payloads when the body schema is known.
Mixing unrelated query, header, and cookie parsing logic deep inside the handler body.
Reading large uploads eagerly without a size or processing plan.
Hiding transport aliases or validation rules away from the route signature.
Letting request parsing decisions leak into response-shaping concerns.
Validation Checklist
Confirm every client-supplied input has an explicit source and type.
Confirm aliases, defaults, and constraints match the public API contract.
Confirm body parsing uses the intended media type and payload model.
Confirm raw Request access is only used where the typed API is insufficient.
Confirm multipart and file handling cannot exhaust memory unintentionally.
Confirm malformed input produces the expected validation or client-error behavior.
Confirm auth, user, and state access from Request are used intentionally, not as hidden globals.
Cross-Skill Handoffs
Use litestar-responses for outbound contract design.
Use litestar-exception-handling for validation and client-error response strategy.
Use litestar-dto and litestar-custom-types for advanced transformation or custom parsing.
Use litestar-file-uploads for deeper upload security and storage workflows.
Litestar References
https://docs.litestar.dev/2/usage/requests.html
https://docs.litestar.dev/2/usage/routing/parameters.html
Weekly Installs
15
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