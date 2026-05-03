---
rating: ⭐⭐
title: docs-sync
url: https://skills.sh/jmerta/codex-skills/docs-sync
---

# docs-sync

skills/jmerta/codex-skills/docs-sync
docs-sync
Installation
$ npx skills add https://github.com/jmerta/codex-skills --skill docs-sync
SKILL.md
Docs sync
Goal

Update documentation so it matches the current code and is easy for the target audience to follow.

Inputs to ask for (if missing)
What changed (feature/bugfix/refactor) and who the docs are for.
Which docs surfaces matter: README, /docs, wiki, runbooks, API spec, changelog, onboarding.
Any required format/voice (company style guide, "keep it short", etc.).
Workflow (checklist)
Identify what changed
Use the diff to locate impacted areas:
git diff --name-only
git diff
Inventory docs surfaces in the repo
Common locations: README.md, docs/, CONTRIBUTING.md, CHANGELOG.md, openapi.*, schema.graphql, adr/, runbooks/.
For Spring: check for generated OpenAPI/Swagger docs or endpoint annotations.
For Next/TypeScript: check for docs pages, Storybook, or typed API clients.
If your repo uses docs/ as the primary doc root, see references/docs-structure.md for a suggested layout.
Decide what needs updating
Ensure docs cover:
setup and local dev commands
required env vars / config keys
API contract changes (request/response examples)
DB migrations and operational steps
behavior changes visible to users
If the change is an architectural/behavioral decision, add or update an ADR (use references/adr-template.md).
Apply edits with minimal churn
Prefer small, targeted edits over rewrites.
Add examples that are copy/paste runnable.
Keep headings stable to avoid breaking deep links.
Use templates in references/ when helpful.
Verify docs are consistent
Run the repo's existing doc checks if present (md lint, docs build, site build).
At minimum: ensure code fences match the actual commands and file paths, and env var names match the code.
Deliverable

Provide:

The list of docs files updated and why.
A short "How to verify" section (commands or manual checks).
Weekly Installs
20
Repository
jmerta/codex-skills
GitHub Stars
126
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass