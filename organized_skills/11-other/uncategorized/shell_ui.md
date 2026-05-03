---
rating: ⭐⭐
title: shell-ui
url: https://skills.sh/7spade/black-tortoise/shell-ui
---

# shell-ui

skills/7spade/black-tortoise/shell-ui
shell-ui
Installation
$ npx skills add https://github.com/7spade/black-tortoise --skill shell-ui
SKILL.md
Shell UI
Intent

Own global application chrome and cross-cutting UI state (navigation, theme, notifications) without leaking business logic.

Responsibilities
Layout composition, global navigation, and app-level UI scaffolding.
Global UI state stores (theme, toasts/snackbars, search UI state) when truly cross-cutting.
Boundaries
Shell does not own capability business logic.
Shell consumes application-facing signals; it does not call repositories directly.
UI Rules
Standalone components only.
Bind templates to signals only using Angular control flow.
Use Material 3 tokens; avoid hardcoded CSS values for color/typography.
Navigation
Prefer router-driven composition and lazy loading.
Use functional guards/resolvers with inject().
Accessibility
Ensure keyboard navigation, focus visibility, semantic landmarks, and skip links for global layout.
Weekly Installs
9
Repository
7spade/black-tortoise
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass