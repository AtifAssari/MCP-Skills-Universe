---
title: addon-llm-translation
url: https://skills.sh/ajrlewis/ai-skills/addon-llm-translation
---

# addon-llm-translation

skills/ajrlewis/ai-skills/addon-llm-translation
addon-llm-translation
Installation
$ npx skills add https://github.com/ajrlewis/ai-skills --skill addon-llm-translation
SKILL.md
Add-on: LLM Translation

Use this skill when an app needs LLM translation endpoints or batch translation jobs with explicit user review before publish.

Compatibility
Works with architect-nextjs-bun-app, architect-python-uv-fastapi-sqlalchemy, and architect-python-uv-batch.
Can be combined with addon-langchain-llm for provider abstraction.
Can be combined with addon-langgraph-agent for multi-step translation workflows.
Inputs

Collect:

SOURCE_LANGUAGE: IETF language tag (for example en, es, fr).
TARGET_LANGUAGE: IETF language tag.
LLM_PROVIDER: openai | anthropic | ollama.
LLM_MODEL: provider model id.
REVIEW_MODE: dual-output (recommended) | translation-only.
MAX_SOURCE_CHARS: default 12000.
Integration Workflow
Add dependencies:
Next.js:
# Use the project's package manager (examples):
bun add zod
pnpm add zod

Python:
uv add pydantic pydantic-settings

Add files by architecture:
Next.js:
src/lib/llm/translation.ts
src/app/api/translation/route.ts

Python API:
src/{{MODULE_NAME}}/schemas/translation.py
src/{{MODULE_NAME}}/services/translation.py
src/{{MODULE_NAME}}/api/routes/translation.py

Python batch:
src/{{MODULE_NAME}}/translation/jobs.py
src/{{MODULE_NAME}}/translation/schemas.py

Keep provider calls server-side:
Never call provider APIs directly from browser clients.
Return typed payloads with source text, translated text, and review metadata.
Enforce output schema and fallbacks:
Validate SOURCE_LANGUAGE/TARGET_LANGUAGE.
Reject empty translation output.
Add provider timeout/retry boundaries and explicit degraded behavior.
Required Templates
Translation response shape
{
  "sourceLanguage": "en",
  "targetLanguage": "es",
  "sourceText": "Hello world",
  "translatedText": "Hola mundo",
  "translatorNotes": "Preserved idiom intent."
}

Guardrails

Documentation contract for generated code:

Python: write module docstrings and docstrings for public classes, methods, and functions.
Next.js/TypeScript: write JSDoc for exported components, hooks, utilities, and route handlers.
Add concise rationale comments only for non-obvious logic, invariants, or safety constraints.
Apply this contract even when using template snippets below; expand templates as needed.

Keep API keys server-only.

Preserve user intent; do not silently rewrite meaning for fluency.

Do not auto-publish untranslated or invalid outputs.

Emit explicit review state for publish pipelines.

Validation Checklist
Confirm generated code includes required docstrings/JSDoc and rationale comments for non-obvious logic.
test -f src/lib/llm/translation.ts || true
test -f src/{{MODULE_NAME}}/api/routes/translation.py || true
rg -n "sourceLanguage|targetLanguage|translatedText" src || true

Manual checks:
Translation response validates with expected schema.
Timeout/failure path returns controlled fallback response.
Decision Justification Rule
Every non-trivial decision must include a concrete justification.
Capture the alternatives considered and why they were rejected.
State tradeoffs and residual risks for the chosen option.
If justification is missing, treat the task as incomplete and surface it as a blocker.
Weekly Installs
8
Repository
ajrlewis/ai-skills
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass