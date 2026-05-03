---
rating: ⭐⭐
title: fusion-core-services
url: https://skills.sh/equinor/fusion-skills/fusion-core-services
---

# fusion-core-services

skills/equinor/fusion-skills/fusion-core-services
fusion-core-services
Installation
$ npx skills add https://github.com/equinor/fusion-skills --skill fusion-core-services
SKILL.md
Fusion Core Services
When to use

Use this skill when the task involves one or more Fusion Core service APIs and the agent needs to identify the right service guidance without requiring separate skill installs.

Typical triggers:

implement a Fusion API client
wire a Fusion backend service integration
figure out which Fusion Core service owns a workflow
solve a cross-service task such as context plus people, roles plus notifications, or apps plus service messages
When not to use

Do not use this skill for:

modifying code inside fusion-core-services
non-Fusion APIs or generic Microsoft Graph / Power BI work with no Fusion service layer involved
standalone product workflows already covered by another dedicated skill outside Fusion Core services
Required inputs
target workflow or user goal
target consumer shape (react, typescript client, csharp httpclient, backend service, or other)
known service hints, if any
versioning or authorization expectations when relevant
Instructions
Scope the request first.
Identify whether the workflow touches one service or multiple services.
If the service is ambiguous, use agents/service-router.md to map the workflow to likely services before producing implementation guidance.
Read only the relevant service references.
Start with Combined API surface.
Then open the matching per-service reference file.
Pull in the endpoint catalog and model asset for only the services that materially affect the answer.
Preserve source-grounded guidance.
Prefer controller-backed endpoint and model notes already captured in the bundled references.
Call out any route or model area that still requires direct source confirmation before shipping.
Handle capabilities explicitly.
If a service exposes OPTIONS or other access-probe routes, use them to drive capability-aware UI or mutation logic.
If a service does not expose stable probes, document conservative client behavior and treat 403 Forbidden as the fallback capability signal.
Treat subscriptions as backend-only unless the reference says otherwise.
The /subscriptions/... routes in this skill are for application-token event registration and CloudEvent-style change handling, not normal frontend CRUD flows.
Return consumer-ready guidance.
For frontend consumers, return TypeScript-friendly DTOs and a minimal client/hook pattern.
For .NET consumers, return a typed HttpClient plan plus DTO record suggestions.
For cross-service tasks, explain the service sequence and data handoff between services.
Service catalog
Apps: reference, endpoint catalog, models
Bookmarks: reference, endpoint catalog, models
Context: reference, endpoint catalog, models
Contract Personnel: reference, endpoint catalog, models
Mail: reference, endpoint catalog, models
Notification: reference, endpoint catalog, models
People: reference, endpoint catalog, models
Portal Config: reference, endpoint catalog, models
Reports: reference, endpoint catalog, models
RolesV2: reference, endpoint catalog, models
Service Messages: reference, endpoint catalog, models
Tasks: reference, endpoint catalog, models
Expected output

Return headings in this order:

Scope check
Service selection
Endpoint mapping
Model mapping
Consumer implementation plan
Integration code sketch
Validation and test notes
Risks and assumptions
Safety & constraints

Never:

invent service ownership, routes, or DTO fields
answer from generic SaaS/API assumptions when the bundled Fusion references are specific
treat backend subscription routes as normal frontend interaction flows

Always:

keep cross-service reasoning explicit when more than one service is involved
call out capability-probe behavior when the service exposes OPTIONS
prefer the narrowest set of service references needed for the user’s workflow
Weekly Installs
157
Repository
equinor/fusion-skills
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass