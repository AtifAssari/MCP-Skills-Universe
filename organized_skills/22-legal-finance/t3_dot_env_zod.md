---
rating: ⭐⭐
title: t3-dot-env-zod
url: https://skills.sh/onnokh/t3-dot-env-zod/t3-dot-env-zod
---

# t3-dot-env-zod

skills/onnokh/t3-dot-env-zod/t3-dot-env-zod
t3-dot-env-zod
Installation
$ npx skills add https://github.com/onnokh/t3-dot-env-zod --skill t3-dot-env-zod
SKILL.md
T3 Env with Zod

Use T3 Env to validate and type your environment variables with Zod, with correct client/server separation and framework-aware runtime env handling.

Workflow
Identify the target framework.
Choose the correct createEnv variant and runtime strategy.
Apply Zod patterns that are safe for env strings.
Add build-time validation where possible.
Use presets instead of hand-maintaining platform vars.
Decision Tree
Is this Next.js (16+)?
  |-- Yes → use @t3-oss/env-nextjs
  |     |-- Use experimental__runtimeEnv (usually client vars only)
  |     '-- Validate on build → import env in next.config.ts
  |
  '-- Is this Vite?
        '-- Yes → use @t3-oss/env-core
              |-- clientPrefix: "VITE_"
              '-- runtimeEnv: import.meta.env

References
references/nextjs.md
references/core.md
references/zod.md
references/presets.md
references/pitfalls.md
Examples

Copy/paste examples live under examples/:

examples/nextjs/nextjs-16-plus/
examples/core/vite-import-meta-env/
Weekly Installs
10
Repository
onnokh/t3-dot-env-zod
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass