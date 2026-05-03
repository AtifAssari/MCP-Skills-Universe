---
rating: ⭐⭐
title: laravel:api-surface-evolution
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:api-surface-evolution
---

# laravel:api-surface-evolution

skills/jpcaparas/superpowers-laravel/laravel:api-surface-evolution
laravel:api-surface-evolution
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:api-surface-evolution
SKILL.md
API Surface Evolution

Design for change without breaking clients.

Versioning Strategy
Choose explicit versioning (URI /v1/... or header negotiation)
Default to additive changes; never break a released contract
DTOs & Transformers
Define versioned DTOs; map from models/services via transformers
Keep controller thin—validate → transform → respond
Deprecations
Mark fields as deprecated in docs and responses (e.g., headers)
Provide sunset timelines; add metrics to see remaining usage
Testing
Contract tests per version (request/response shapes)
Backward compatibility tests for commonly used flows
Weekly Installs
51
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026