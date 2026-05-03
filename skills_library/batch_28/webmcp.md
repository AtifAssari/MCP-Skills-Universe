---
title: webmcp
url: https://skills.sh/webmaxru/agent-skills/webmcp
---

# webmcp

skills/webmaxru/agent-skills/webmcp
webmcp
Installation
$ npx skills add https://github.com/webmaxru/agent-skills --skill webmcp
SKILL.md
WebMCP
Procedures

Step 1: Identify the browser integration surface

Inspect the workspace for browser entry points, UI handlers, and any existing app state or form handling layer.
Execute node scripts/find-webmcp-targets.mjs . to inventory likely frontend files and existing WebMCP markers when a Node runtime is available.
If a Node runtime is unavailable, inspect the nearest package.json, HTML entry point, and framework bootstrap files manually to identify the browser app boundary.
If the workspace contains multiple frontend apps, prefer the app that contains the active route, component, or user-requested feature surface.
If the inventory still leaves multiple plausible frontend targets, stop and ask the user which app should receive the WebMCP integration.
If the project is not a browser web app, stop and explain that this skill does not apply.

Step 2: Choose the WebMCP shape

Read references/webmcp-reference.md before writing code.
Read references/declarative-api.md when the feature can be expressed as an HTML form flow or needs agent-invoked submit handling.
Read references/compatibility.md when native availability, Chrome preview setup, or draft-versus-preview behavior matters.
Read references/troubleshooting.md when registration, schema serialization, or agent-driven form execution fails.
Verify that the integration runs in a secure window browsing context.
If the feature must run on the server, in a worker, or headlessly without a visible browsing context, stop and explain the platform limitation.
Choose the imperative API when the tool wraps existing JavaScript logic, requires dynamic registration, or needs ModelContextClient.requestUserInteraction().
Choose the declarative API when the user flow already maps cleanly to a form submission and the page can keep the human-visible form in sync with agent activity.
Keep tool names, descriptions, and parameters explicit and positive, and prefer atomic tools over overlapping variants.

Step 3: Implement tool registration

Read assets/model-context-registry.template.ts and adapt it to the framework, state model, and file layout in the workspace when using the imperative API.
Register imperative tools with navigator.modelContext.registerTool() using a stable name, a positive description, an object inputSchema, and an execute callback.
Set annotations.readOnlyHint to true only for tools that do not modify state.
Validate business rules inside the tool implementation even when the schema is strict, and return descriptive errors that help the agent retry with corrected input.
Return tool results only after the UI and application state reflect the tool's effect.
If tool availability depends on route, selection, or page state, register tools only while they are valid and unregister stale tools by aborting the AbortController whose signal was passed to registerTool(); during the Chrome 148 transition window, also call navigator.modelContext.unregisterTool?.() with optional chaining before aborting.
For declarative tools, annotate the target <form> with toolname and tooldescription, and let form controls define the parameter surface.
Use labels or toolparamdescription to produce clear parameter descriptions for declarative fields.
Use toolautosubmit only when the page should submit automatically after the agent populates the form.

Step 4: Wire agent-driven UX safely

Preserve the normal human interaction path even when the page supports agent invocation.
When an imperative tool needs explicit confirmation or a user-facing step, call client.requestUserInteraction() instead of bypassing the UI.
When customizing declarative submit handling, call preventDefault() before respondWith() and return structured validation errors for agent-invoked submits.
Use preview-only events such as toolactivated, toolcancel, agentInvoked, and WebMCP form pseudo-classes only behind compatibility-aware UI logic.
Keep destructive or sensitive actions gated behind visible user confirmation, even if the agent can prepare the input.
Keep UI state synchronized so the same page accurately reflects changes caused by human input and tool calls.

Step 5: Validate behavior

Test the register and unregister lifecycle, including duplicate-name protection and cleanup on route or state changes.
Test invalid or incomplete inputs to confirm the tool returns corrective errors instead of silently failing.
For declarative tools, verify generated parameter descriptions, required fields, submit behavior, and any custom respondWith() handling.
If the target environment is the current Chrome preview, confirm the required version and flag state from references/compatibility.md before treating runtime failures as application bugs.
Use the Model Context Tool Inspector or equivalent preview tooling only as a validation aid, not as a runtime dependency.
Validate deterministic execution first by inspecting the registered tool set and manually invoking the tool with representative arguments when preview tooling is available.
After deterministic execution is correct, validate natural-language routing so descriptions and parameter shapes guide the agent toward the correct tool.
Run the workspace build, typecheck, or tests after editing.
Error Handling
If navigator.modelContext is missing, confirm the code is running in a secure browser window context and then check the preview requirements in references/compatibility.md.
If registerTool() throws InvalidStateError, check for duplicate names or empty name or description values.
If registerTool() throws TypeError or JSON serialization errors, replace non-serializable or circular inputSchema values with plain JSON-compatible objects.
If an older demo or article references provideContext, clearContext, or toolparamtitle, treat those surfaces as obsolete for current implementations.
If declarative execution does not update the page correctly, read references/declarative-api.md and references/troubleshooting.md before changing the tool contract.
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