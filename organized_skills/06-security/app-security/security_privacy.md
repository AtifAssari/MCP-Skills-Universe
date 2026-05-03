---
rating: ⭐⭐
title: security-privacy
url: https://skills.sh/7spade/black-tortoise/security-privacy
---

# security-privacy

skills/7spade/black-tortoise/security-privacy
security-privacy
Installation
$ npx skills add https://github.com/7spade/black-tortoise --skill security-privacy
SKILL.md
Security & Privacy (Pre-flight)
Use when
Adding/reading/writing user/workspace data.
Touching identity/auth, permissions, Firebase rules, or external APIs.
Adding logging, analytics, telemetry, or error reporting.
Workflow
Identify data: what fields are PII, where stored, retention expectations.
Identify trust boundaries: browser ↔ Firebase/backend; who can call what.
Minimize & redact: remove unnecessary fields; ensure logs/errors redact secrets/PII.
Validate inputs at the edge; keep Domain pure.
Confirm least privilege: tokens, rules, and access paths.
Output checklist
No secrets in repo, fixtures, or logs.
No PII in logs/errors/templates.
Clear authorization point (not scattered across UI).
Deletion path does not leave access holes.
References
.github/instructions/65-security-privacy-copilot-instructions.md
Weekly Installs
8
Repository
7spade/black-tortoise
First Seen
Feb 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass