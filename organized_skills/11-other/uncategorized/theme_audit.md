---
rating: ⭐⭐
title: theme-audit
url: https://skills.sh/chmouel/lazyworktree/theme-audit
---

# theme-audit

skills/chmouel/lazyworktree/theme-audit
theme-audit
Installation
$ npx skills add https://github.com/chmouel/lazyworktree --skill theme-audit
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Theme Audit

Audit theme definitions and usage across the codebase.

Theme definitions

!cat internal/theme/theme.go | head -200

Theme usage in UI

!grep -r "theme\." internal/app/ --include="*.go" | head -50

Potential hardcoded colours

!grep -rE "(lipgloss\.(Color|AdaptiveColor)\(|#[0-9a-fA-F]{6})" internal/app/ --include="*.go" | head -30

Audit themes for:

Missing colour fields that UI code expects
Unused theme values that can be removed
Hardcoded colours in UI code that should use theme fields
Contrast issues between foreground and background colours
Inconsistencies between different theme variants
Weekly Installs
44
Repository
chmouel/lazyworktree
GitHub Stars
215
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass