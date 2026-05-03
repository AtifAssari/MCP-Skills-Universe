---
title: update
url: https://skills.sh/assistant-ui/skills/update
---

# update

skills/assistant-ui/skills/update
update
Installation
$ npx skills add https://github.com/assistant-ui/skills --skill update
Summary

Automated version detection and migration for assistant-ui and AI SDK with breaking-change guidance.

Detects current installed versions against npm ground truth and identifies which migrations are needed
Routes updates through AI SDK v6 migration first (if required), then assistant-ui version-specific migrations, with clear dependency ordering
Includes reference guides for AI SDK v4/v5 to v6 transitions, assistant-ui version jumps, and a breaking-changes quick reference table
Provides shell commands for package updates and verification steps (type checking, build validation)
SKILL.md
assistant-ui Update

Always verifies against npm ground truth and GitHub commits.

References
./references/ai-sdk-v6.md -- AI SDK v4/v5 → v6 migration (complete guide)
./references/assistant-ui.md -- assistant-ui version migrations
./references/breaking-changes.md -- Quick reference table
Phase 1: Detect Versions
Get Ground Truth
# Installed versions
npm ls @assistant-ui/react @assistant-ui/react-ai-sdk ai @ai-sdk/react 2>/dev/null

# Latest from npm
npm view @assistant-ui/react version
npm view @assistant-ui/react-ai-sdk version
npm view ai version

Version Analysis
Package	Check For
ai	< 6.0.0 → needs AI SDK v6 migration
@assistant-ui/react	< 0.12.0 → needs unified state API migration
@assistant-ui/react	< 0.11.0 → needs runtime migration
@assistant-ui/react	< 0.10.0 → needs ESM migration
@assistant-ui/react	< 0.8.0 → needs UI split migration
@assistant-ui/react-ai-sdk	< 1.0.0 → needs AI SDK v6 first
Phase 2: Route to Migration
AI SDK < 6.0.0?
├─ Yes → See ./references/ai-sdk-v6.md
└─ No
   └─ assistant-ui outdated?
      ├─ Yes → See ./references/assistant-ui.md
      └─ No → Already up to date

Migration Order
AI SDK first (if < 6.0.0) - Required for @assistant-ui/react-ai-sdk >= 1.0
assistant-ui second - Apply breaking changes for version jump
Verify - Type check, build, test
Phase 3: Execute
Update Packages
# pnpm
pnpm add @assistant-ui/react@latest @assistant-ui/react-ai-sdk@latest ai@latest @ai-sdk/react@latest

# npm
npm install @assistant-ui/react@latest @assistant-ui/react-ai-sdk@latest ai@latest @ai-sdk/react@latest

Apply Migrations

Based on version jump, apply relevant migrations from references.

Verify
npx tsc --noEmit  # Type check
pnpm build        # Build check

Troubleshooting

"Peer dependency conflict"

Update all packages together
Check version compatibility in ./references/breaking-changes.md

Type errors after upgrade

Consult breaking changes reference
Check specific migration guide

Runtime errors

Verify API patterns match new version
Check for renamed/moved APIs
Weekly Installs
1.1K
Repository
assistant-ui/skills
GitHub Stars
14
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn