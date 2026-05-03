---
rating: ⭐⭐
title: iceywu-dev-workflow
url: https://skills.sh/iceywu/skills/iceywu-dev-workflow
---

# iceywu-dev-workflow

skills/iceywu/skills/iceywu-dev-workflow
iceywu-dev-workflow
Installation
$ npx skills add https://github.com/iceywu/skills --skill iceywu-dev-workflow
SKILL.md
IceyWu Dev Workflow

A concise execution playbook centered on @iceywu/utils development and integration.

When to Use
Selecting utility functions for app/business logic
Extracting duplicated code into reusable utilities
Fixing utility edge cases and regression bugs
Reviewing or preparing pull requests related to @iceywu/utils
Workflow

Confirm utility intent

Define expected input/output and error behavior
Prefer deterministic, side-effect-free helpers

Reuse before creating

Search existing helpers in @iceywu/utils
Avoid near-duplicate APIs with overlapping semantics

Design stable API surface

Keep function names explicit and behavior predictable
Favor backward-compatible changes for published utilities

Implement with edge-case safety

Cover nullish values, empty collections, invalid ranges, and type boundaries
Keep runtime dependencies minimal

Validate and document

Add or run focused tests for changed utility behavior
Update usage examples/changelog context for consumers
Quality Checklist
Is this helper generic enough to belong in shared utils?
Is naming clear and consistent with existing utils conventions?
Are breaking behavior changes explicitly documented?
Are edge cases and invalid inputs handled predictably?
Do tests cover normal path + boundary path + failure path?
Output Style

When returning results:

State impact on @iceywu/utils consumers first
List API changes and migration notes (if any)
Mention tests/checks executed and outcomes
Call out assumptions, risks, and follow-up actions
Weekly Installs
25
Repository
iceywu/skills
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass