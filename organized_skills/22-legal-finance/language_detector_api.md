---
rating: ⭐⭐
title: language-detector-api
url: https://skills.sh/webmaxru/agent-skills/language-detector-api
---

# language-detector-api

skills/webmaxru/agent-skills/language-detector-api
language-detector-api
Installation
$ npx skills add https://github.com/webmaxru/agent-skills --skill language-detector-api
SKILL.md
Language Detector API
Procedures

Step 1: Identify the browser integration surface

Inspect the workspace for browser entry points, UI handlers, text-input flows, and any existing AI abstraction layer.
Execute node scripts/find-language-detector-targets.mjs . to inventory likely frontend files and existing Language Detector API markers when a Node runtime is available.
If a Node runtime is unavailable, inspect the nearest package.json, HTML entry point, and framework bootstrap files manually to identify the browser app boundary.
If the workspace contains multiple frontend apps, prefer the app that contains the active route, component, or user-requested feature surface.
If the inventory still leaves multiple plausible frontend targets, stop and ask which app should receive the Language Detector API integration.
If the project is not a browser web app, stop and explain that this skill does not apply.

Step 2: Confirm API viability and choose the integration shape

Read references/language-detector-reference.md before writing code.
Read references/examples.md when the feature needs a session wrapper, download-progress UI, confidence thresholding, or cleanup shape.
Read references/compatibility.md when preview flags, browser channels, iframe rules, or environment constraints matter.
Read references/troubleshooting.md when support checks, creation, detection, or cleanup fail.
Verify that the feature runs in a secure Window context.
Verify that the current frame is allowed to use the language-detector permissions-policy feature.
Choose the narrowest session shape that matches the task:
bare LanguageDetector.create() for general language detection
expectedInputLanguages when the product depends on a narrower language set or better accuracy for known languages
monitor when the UI must surface model download progress
If the feature must run in a worker, on the server, or through a cloud-only contract, stop and explain the platform mismatch.
If the project uses TypeScript, add or preserve narrow typings for the Language Detector API surface used by the feature.

Step 3: Implement a guarded session wrapper

Read assets/language-detector-session.template.ts and adapt it to the framework, state model, and file layout in the workspace.
Centralize support checks around globalThis.isSecureContext, LanguageDetector, and the same expectedInputLanguages shape the feature will use at runtime.
Gate session creation behind LanguageDetector.availability() using the same create options that will be passed to LanguageDetector.create().
Treat availability() as a capability check, not a guarantee that creation will succeed without download time, policy approval, or user activation.
Create sessions only after user activation when creation may trigger a model download.
Use the monitor option during create() when the product needs download progress.
Use AbortController for cancelable create(), detect(), or measureInputUsage() calls, and call destroy() when the session is no longer needed.
Recreate the session instead of mutating expectedInputLanguages after creation; session options are fixed per instance.
If the feature lives in a cross-origin iframe, require explicit delegation through allow="language-detector".

Step 4: Wire UX and fallback behavior

Surface distinct states for missing APIs, insecure contexts, blocked frames, downloadable or downloading models, ready sessions, in-flight detection, and aborted work.
Keep a non-AI fallback for unsupported browsers, blocked frames, or environments that do not meet current preview requirements.
Treat very short text, single words, and mixed-language snippets as lower-confidence inputs; present confidence-aware UI instead of pretending the top result is always reliable.
Preserve the full ordered result list when the product needs ranked candidates, and apply any confidence threshold or und handling in product logic instead of truncating silently.
Treat the trailing und result as meaningful uncertainty, not as a defect to remove.
Use measureInputUsage() when quota or input-size budgeting affects the flow.
Do not route translation, summarization, or generic chat tasks through this API; switch to Translator, Writing Assistance APIs, Prompt API, or another approved capability when the task is not language detection.

Step 5: Validate behavior

Execute node scripts/find-language-detector-targets.mjs . to confirm that the intended app boundary and Language Detector API markers still resolve to the edited integration surface.
Verify secure-context checks, LanguageDetector feature detection, and availability() behavior before debugging deeper runtime failures.
Test at least one create() plus detect() flow with representative user text.
If the feature depends on expectedInputLanguages, test both the constrained and unconstrained path or confirm why only one is valid.
Confirm that cancellation rejects with the expected abort reason and that destroyed sessions are not reused.
If the target environment depends on preview browser flags or channel-specific behavior, confirm the required browser state from references/compatibility.md before treating failures as application bugs.
Run the workspace build, typecheck, or tests after editing.
Error Handling
If LanguageDetector is missing, keep a non-AI fallback and confirm secure-context, browser, channel, and flag requirements before changing product logic.
If availability() returns downloadable or downloading, require user-driven session creation before promising that detection is ready.
If create() throws NotAllowedError, check permissions-policy constraints, missing user activation for downloads, browser policy restrictions, or user rejection.
If detect() throws InvalidStateError, confirm the document is still fully active and recreate the session after major lifecycle changes if needed.
If a detection call throws QuotaExceededError, reduce the input size or measure usage before retrying.
If the feature must run in a worker or server context, stop and explain that the Language Detector API is a window-only browser API.
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