---
rating: ⭐⭐
title: prompt-api
url: https://skills.sh/webmaxru/agent-skills/prompt-api
---

# prompt-api

skills/webmaxru/agent-skills/prompt-api
prompt-api
Installation
$ npx skills add https://github.com/webmaxru/agent-skills --skill prompt-api
SKILL.md
Prompt API
Procedures

Step 1: Identify the integration surface

Inspect the workspace for browser entry points, UI handlers, and any existing AI abstraction layer.
Execute node scripts/find-frontend-targets.mjs . to inventory likely frontend files and existing Prompt API usage when a Node runtime is available.
If a Node runtime is unavailable, inspect the nearest package.json, HTML entry point, and framework entry files manually to identify the browser app boundary.
If the workspace contains multiple frontend apps, prefer the app that contains the active route, component, or user-requested feature surface.
If the inventory still leaves multiple plausible frontend targets, stop and ask the user which app should receive the Prompt API integration.
If the project is not a browser web app, stop and explain that this skill does not apply.

Step 2: Confirm Prompt API viability

Read references/prompt-api-reference.md before writing code.
Read references/examples.md when the feature needs a spec-valid message shape for text, multimodal, prefix, or tool-enabled sessions.
Read references/compatibility.md when the feature must support multiple browser generations or decide between native support and polyfills.
Read references/polyfills.md when the feature needs concrete package installation or backend configuration examples for Prompt API or Task API polyfills.
Verify that the feature runs in a secure window context and that the language-model permissions-policy allows access from the current frame.
If the integration must run in a Web Worker or other non-window context, stop and explain the platform limitation.
Choose the session shape the feature needs: prompt(), promptStreaming(), initialPrompts, append(), measureContextUsage(), tools, or responseConstraint.
If the project uses TypeScript, add or preserve typings that cover the Prompt API surface used by the project.

Step 3: Implement a guarded session wrapper

Read assets/language-model-service.template.ts and adapt it to the framework, state model, and file layout in the workspace.
Gate session creation behind LanguageModel.availability() using the same creation options that the feature will use at runtime, including expected modalities and tools.
Create sessions only after user activation when model download or instantiation may begin.
Use AbortController for cancelable prompts and call destroy() when the session is no longer needed.
If the feature runs in a cross-origin iframe, require allow="language-model" on the embedding iframe.
Do not depend on params(), topK, or temperature; the spec marks them EXPERIMENTAL and extension-only, so portable web page integrations must not require them.
Treat availability() as a passive capability check: if it reports downloading before user activation, do not assume the current page initiated that download or lock the UI into an app-started busy state.

Step 4: Wire UX and fallback behavior

Surface distinct states for unavailable devices, model download, ready sessions, and in-flight prompts.
If download progress matters to the feature, attach a monitor listener during LanguageModel.create() and render progress in the UI.
Keep a non-AI fallback for unsupported browsers, unsupported devices, or blocked iframe contexts.
If the feature needs structured output, pass a JSON Schema through responseConstraint, use omitResponseConstraintInput only when the prompt already carries the required format instructions, and parse the returned string before using it.
Respect prompt-shape validation rules: system messages belong in initialPrompts, prefix: true applies only to the final assistant message, and assistant message content must remain text-only.
If availability() reports downloading before the app has called create(), present that as informational browser state rather than a page-owned active download, and keep controls usable unless the app itself is busy.

Step 5: Validate behavior

Test short responses with prompt() and long responses with promptStreaming() when applicable.
Verify that repeated prompts reuse context intentionally, that destroyed sessions are not reused, and that the app uses compatibility checks for context measurement and overflow handling across browser versions.
Read references/troubleshooting.md if the integration throws NotSupportedError or behaves differently across frames or execution contexts.
Run the workspace build, typecheck, or tests after editing.
Error Handling
If LanguageModel is missing, prefer progressive enhancement with a maintained Prompt API polyfill or a non-AI fallback instead of inventing a custom compatibility layer.
If availability() returns downloading before the app has called create(), treat it as passive browser state. Only surface live progress and block prompt submission when the app itself has started LanguageModel.create().
If availability() or prompt() throws NotSupportedError, align the creation and prompt options with the actual modalities, languages, message roles, and tools used by the feature.
If the feature must run in Web Workers, redirect the integration to a window context because the Prompt API is not available in workers.
If the feature lives in a cross-origin iframe, require allow="language-model" from the embedding page before continuing.
If node scripts/find-frontend-targets.mjs . cannot run, identify the browser app boundary manually and continue only after a single target app is clear.
Weekly Installs
83
Repository
webmaxru/agent-skills
GitHub Stars
27
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass