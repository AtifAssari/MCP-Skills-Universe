---
title: adapt-materal-enums
url: https://skills.sh/haibaraaiaptx/frontend-openapi-skills/adapt-materal-enums
---

# adapt-materal-enums

skills/haibaraaiaptx/frontend-openapi-skills/adapt-materal-enums
adapt-materal-enums
Installation
$ npx skills add https://github.com/haibaraaiaptx/frontend-openapi-skills --skill adapt-materal-enums
SKILL.md
Materal Framework Enum Adapter

Specialized workflow for Materal framework enum adaptation with semantic naming.

Prerequisites
pnpm add -D @aptx/frontend-tk-cli

Strict Workflow
Fetch enum patch from provider API
LLM fills suggested_name based on comment field (no Value1/Value2 style allowed)
Apply patch only after all suggested_name fields are filled
Cleanup intermediate files in production
Commands
# 1) Fetch Materal enum patch (disable auto-naming, delegate to LLM)
pnpm exec aptx-ft -i <spec-file> materal enum-patch \
  --base-url <base-url> \
  --output ./tmp/enum-patch.json \
  --naming-strategy none

# 2) LLM fills suggested_name in patch
# Rule: Translate comment to semantic PascalCase name, preserve value/comment

# 3) Apply translated patch (requires non-empty suggested_name)
pnpm exec aptx-ft -i <spec-file> model enum-apply \
  --patch ./tmp/enum-patch.translated.json \
  --output ./generated/models \
  --style module \
  --conflict-policy patch-first

# 4) Cleanup intermediate files (required in production)
rm -f ./tmp/enum-patch.json ./tmp/enum-patch.translated.json


Alternative (without pnpm):

npx aptx-ft -i <spec-file> materal enum-patch --base-url <base-url> --output ./tmp/enum-patch.json --naming-strategy none
npx aptx-ft -i <spec-file> model enum-apply --patch ./tmp/enum-patch.translated.json --output ./generated/models --style module --conflict-policy patch-first

Advanced Options
Option	Default	Description
--max-retries <n>	3	Max retry attempts on network failure
--timeout-ms <ms>	10000	Request timeout in milliseconds
pnpm exec aptx-ft -i <spec-file> materal enum-patch \
  --base-url <base-url> \
  --output ./tmp/enum-patch.json \
  --naming-strategy none \
  --max-retries 5 \
  --timeout-ms 30000

Output Files
File	Description
enum-patch.json	Raw patch from API (value/suggested_name/comment)
enum-patch.translated.json	LLM-filled patch
./generated/models/	Final TypeScript models with adapted enums

Cleanup required: Delete enum-patch.json and enum-patch.translated.json after successful apply.

Boundaries

This skill is ONLY for Materal framework adaptation:

Generic OpenAPI projects → use generate-artifacts or generate-models
Requires access to Materal enum provider API
Does not validate Materal API availability
Related Skills
generate-models: Generic model generation
generate-artifacts: Full artifact generation
Weekly Installs
23
Repository
haibaraaiaptx/f…i-skills
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn