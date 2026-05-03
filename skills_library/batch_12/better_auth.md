---
title: better-auth
url: https://skills.sh/blogic-cz/blogic-marketplace/better-auth
---

# better-auth

skills/blogic-cz/blogic-marketplace/better-auth
better-auth
Installation
$ npx skills add https://github.com/blogic-cz/blogic-marketplace --skill better-auth
SKILL.md
Better Auth Procedure Selection

Select authorization boundaries with Better Auth + TRPC patterns used in template-ts apps.

Procedure Selection Table
Procedure	Access Level	Context Provided
publicProcedure	No auth	{ db, session?, headers }
protectedProcedure	Authenticated	{ db, session, userId, headers }
adminProcedure	Admin role	{ db, session, headers }
protectedOrganizationMemberProcedure	Org member	{ ..., member, organizationId }
protectedOrganizationAdminProcedure	Org admin/owner	{ ..., member, organizationId }
protectedProjectMemberProcedure	Project access	{ ..., project, projectRole, orgRole }
protectedProjectAdminProcedure	Project admin	{ ..., project, projectRole, orgRole }
protectedProjectEditorProcedure	Project editor+	{ ..., project, projectRole, orgRole }

Use this table as the primary selector before writing router logic.

Use This Skill When
Select the correct protected procedure for organization/project/member/admin access.
Implement Better Auth authorization checks inside TRPC procedures.
Review auth boundaries in existing routers.
Follow This Workflow
Identify required access level from the Procedure Selection Table.
Start implementation from the matching base procedure.
Chain stricter middleware only when the table does not fully satisfy the access rule.
Load references/better-auth-examples.md for detailed examples and copy-ready snippets.
Keep context shape stable; add only route-specific fields.
Key Rules
Select the narrowest procedure that matches the required permission.
Reuse inherited context (userId, organizationId, project, roles) instead of recomputing it.
Grant organization admins automatic project-admin behavior; avoid duplicate checks.
Pass ctx.headers to auth.api.* server calls.
Validate variable origins in every middleware (opts.ctx, opts.input) before adding business logic.
References
references/better-auth-examples.md — auth configuration, context setup, middleware examples, client auth usage, and admin API patterns.
Weekly Installs
59
Repository
blogic-cz/blogi…ketplace
GitHub Stars
3
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass