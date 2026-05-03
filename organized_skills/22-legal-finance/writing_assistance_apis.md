---
rating: ⭐⭐
title: writing-assistance-apis
url: https://skills.sh/webmaxru/agent-skills/writing-assistance-apis
---

# writing-assistance-apis

skills/webmaxru/agent-skills/writing-assistance-apis
writing-assistance-apis
Installation
$ npx skills add https://github.com/webmaxru/agent-skills --skill writing-assistance-apis
SKILL.md
Writing Assistance APIs
Procedures

Step 1: Identify the browser integration surface

Inspect the workspace for browser entry points, UI handlers, and any existing AI abstraction layer.
Execute node scripts/find-writing-assistance-targets.mjs . to inventory likely frontend files and existing Summarizer, Writer, or Rewriter usage when a Node runtime is available.
If a Node runtime is unavailable, inspect the nearest package.json, HTML entry point, and framework bootstrap files manually to identify the browser app boundary.
If the workspace contains multiple frontend apps, prefer the app that contains the active route, component, or user-requested feature surface.
If the inventory still leaves multiple plausible frontend targets, stop and ask which app should receive the Writing Assistance API integration.
If the project is not a browser web app, stop and explain that this skill does not apply.

Step 2: Confirm API viability and choose the right surface

Read references/writing-assistance-reference.md before writing code.
Read references/examples.md when the feature needs a session shape for monitoring downloads, batch output, streaming output, or cancellation.
Read references/compatibility.md when preview flags, browser channels, hardware requirements, or iframe constraints matter.
Read references/troubleshooting.md when availability checks, creation, streaming, or session cleanup fail.
Verify that the feature runs in a secure Window context and that the relevant permissions-policy feature allows access from the current frame.
Choose the narrowest surface that matches the task:
Summarizer for article, document, or conversation summaries.
Writer for generating new text from a short prompt or writing task.
Rewriter for transforming existing text while preserving its intent.
If the feature must run in a worker, on the server, or against a remote model provider, stop and explain the platform mismatch.
If the project uses TypeScript, add or preserve typings that cover the specific browser APIs used by the feature.

Step 3: Implement a guarded session wrapper

Read assets/writing-assistance-session.template.ts and adapt it to the framework, state model, and file layout in the workspace.
Gate session creation behind the API's availability() method using the same create options that will be used at runtime.
Treat availability() as a capability check, not a guarantee that creation will succeed without user interaction or download time.
Create sessions only after user activation when creation may initiate a download.
Use the monitor option during create() when the UI needs download progress.
Use AbortController for cancelable create and run calls, and call destroy() when the session is no longer needed.
Recreate the session instead of mutating options after creation; session options are fixed per instance.
If the feature lives in a cross-origin iframe, require explicit delegation for each API that the frame needs.

Step 4: Wire UX and fallback behavior

Surface distinct states for missing APIs, unavailable devices, downloadable or downloading models, ready sessions, in-flight generation, and aborted work.
Keep a non-AI fallback for unsupported browsers, blocked frames, or devices that do not meet the current preview requirements.
Strip or normalize HTML before summarization or rewriting when the source text comes from rendered page content.
Use the batch methods when the feature needs the full result before continuing, and use the streaming methods when the UI should reveal output incrementally.
Pass sharedContext only for persistent session-wide guidance, and pass per-call context only for request-specific background detail.
Keep language options explicit when the feature depends on supported input, context, or output languages.
Do not route generic chatbot, tool-calling, or open-ended assistant tasks through these APIs; switch to the Prompt API or another approved capability when the task is not summarization, writing, or rewriting.

Step 5: Validate behavior

Execute node scripts/find-writing-assistance-targets.mjs . to confirm that the intended app boundary and API markers still resolve to the edited integration surface.
Verify feature detection, secure-context checks, and availability() behavior before debugging deeper runtime failures.
Test at least one batch call and one streaming call when the feature exposes both modes.
Confirm that cancellation stops generation cleanly and that destroyed sessions are not reused.
If the target environment depends on preview browser flags or channel-specific behavior, confirm the required browser state from references/compatibility.md before treating failures as application bugs.
Run the workspace build, typecheck, or tests after editing.
Error Handling
If Summarizer, Writer, or Rewriter is missing, keep a non-AI fallback and confirm that the environment satisfies the browser and preview requirements before changing product logic.
If availability() returns downloadable or downloading, require user-driven session creation before promising that generation is ready.
If create() throws NotAllowedError, check permissions-policy constraints, missing user activation for downloads, browser policy restrictions, or user rejection.
If create() or a run call throws NotSupportedError, align the requested languages, output format, summary type, tone, or length with the browser's supported combinations.
If a call throws QuotaExceededError, shrink sharedContext, per-call context, or the user input before retrying.
If the feature must run in a worker or server context, stop and explain that the Writing Assistance APIs are window-only browser APIs.
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