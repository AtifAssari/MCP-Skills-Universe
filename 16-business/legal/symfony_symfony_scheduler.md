---
title: symfony:symfony-scheduler
url: https://skills.sh/makfly/superpowers-symfony/symfony:symfony-scheduler
---

# symfony:symfony-scheduler

skills/makfly/superpowers-symfony/symfony:symfony-scheduler
symfony:symfony-scheduler
Installation
$ npx skills add https://github.com/makfly/superpowers-symfony --skill symfony:symfony-scheduler
SKILL.md
Symfony Scheduler (Symfony)
Use when
Implementing asynchronous workflows with Messenger/Scheduler/Cache.
Stabilizing retries and failure transports.
Default workflow
Define async contract and delivery semantics.
Implement idempotent handlers and routing strategy.
Configure retries, failure transport, and observability.
Validate success/failure replay scenarios.
Guardrails
Assume at-least-once delivery, not exactly-once.
Keep handlers deterministic and side-effect aware.
Surface poison-message handling strategy.
Progressive disclosure
Use this file for execution posture and risk controls.
Open references when deep implementation details are needed.
Output contract
Async config/handlers updated.
Retry/failure policy decisions.
Operational validation evidence.
References
reference.md
docs/complexity-tiers.md
Weekly Installs
234
Repository
makfly/superpow…-symfony
GitHub Stars
128
First Seen
Jan 23, 2026