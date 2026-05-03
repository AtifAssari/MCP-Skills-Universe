---
rating: ⭐⭐
title: webnn
url: https://skills.sh/webmaxru/agent-skills/webnn
---

# webnn

skills/webmaxru/agent-skills/webnn
webnn
Installation
$ npx skills add https://github.com/webmaxru/agent-skills --skill webnn
SKILL.md
WebNN
Procedures

Step 1: Identify the browser integration surface

Inspect the workspace for browser entry points, UI handlers, worker entry files, and any existing model-loading or inference abstraction layer.
Execute node scripts/find-webnn-targets.mjs . to inventory likely frontend files and existing WebNN markers when a Node runtime is available.
If a Node runtime is unavailable, inspect the nearest package.json, HTML entry point, framework bootstrap files, and worker entry files manually to identify the browser app boundary.
If the workspace contains multiple frontend apps, prefer the app that contains the active route, component, or user-requested feature surface.
If the inventory still leaves multiple plausible frontend targets, stop and ask which app should receive the WebNN integration.
If the project is not a browser web app, stop and explain that this skill does not apply.

Step 2: Confirm WebNN viability and choose the runtime shape

Read references/webnn-reference.md before writing code.
Read references/examples.md when choosing between a direct WebNN graph flow and an adapter around an existing browser ML runtime.
Read references/compatibility.md when native support, preview flags, device behavior, or backend differences matter.
Read references/troubleshooting.md when context creation, graph build, tensor readback, or device selection fails.
Verify that the feature runs in a secure context and in a Window or Worker context (DedicatedWorker, SharedWorker, or ServiceWorker).
If the feature must run on the server, train models, or depend on cloud inference, stop and explain the platform mismatch.
Choose device intent deliberately: use powerPreference: "high-performance" for throughput, powerPreference: "low-power" for power-efficient acceleration, or accelerated: false to prefer CPU inference for maximum reach.
Treat accelerated and powerPreference as preferences, not guarantees. Browser backends can still partition graphs or fall back per operator.
Choose a direct MLGraphBuilder flow when the application owns graph construction or can keep a small deterministic graph path.
Choose an adapter around an existing local runtime only when the application already loads models through that runtime and the task is to prefer WebNN acceleration without rewriting the full inference stack.
If the project uses TypeScript, add or preserve typings for the WebNN surface used by the project.

Step 3: Implement a guarded runtime adapter

Read assets/webnn-runtime.template.ts and adapt it to the framework, state model, and file layout in the workspace.
Centralize support detection around window.isSecureContext, navigator.ml, and the requested execution context instead of scattering checks through UI components.
Create an MLContext only at the boundary where the app is ready to initialize local inference.
Pass explicit accelerated and powerPreference values when the product has a real preference, and omit tuning that the product cannot justify.
Build the graph through MLGraphBuilder when the feature uses direct WebNN operations, or route existing model execution through the app's existing local runtime adapter when that runtime is already responsible for model loading and pre/post-processing.
Reuse the compiled graph and reusable tensors when input and output shapes stay stable across requests.
Use context.writeTensor(), context.dispatch(), and await context.readTensor() in that order for direct graph execution.
Observe context.lost and rebuild the context, graph, and tensors if the browser invalidates the execution state.
Destroy tensors, graphs, and contexts when the feature is disposed or the route no longer needs them.

Step 4: Wire UX and fallback behavior

Surface distinct states for unsupported browsers, secure-context failures, runtime preparation, ready native execution, and explicit fallback execution.
Keep a non-WebNN path for unsupported browsers or unsupported devices when the feature must remain available.
Keep the fallback explicit and product-approved. Do not silently swap in a remote model provider when the feature is supposed to stay local.
Present device choice as an intent, not a promise that every operator will execute on that device.
Move long-running model preparation or repeated inference off the main thread when the application already uses a worker-friendly architecture.
Keep all user data handling consistent with the product's local-processing promises and privacy requirements.

Step 5: Validate behavior

Execute node scripts/find-webnn-targets.mjs . to confirm that the intended app boundary and WebNN markers still resolve to the edited integration surface.
Verify secure-context and navigator.ml detection before debugging deeper runtime issues.
For direct WebNN paths, run a smoke test that creates a context, builds a trivial graph, writes inputs, dispatches, and reads outputs.
Test the intended accelerated and powerPreference settings and confirm that fallback behavior remains usable when an accelerated context cannot be created.
Use context.opSupportLimits() when operator coverage or tensor data type support influences graph design.
Confirm the app does not reuse destroyed tensors, graphs, or contexts.
If the target environment depends on preview Chromium flags or milestone-specific behavior, confirm the required browser state from references/compatibility.md before treating runtime failures as application bugs.
Run the workspace build, typecheck, or tests after editing.
Error Handling
If navigator.ml is missing, confirm secure-context requirements and browser support from references/compatibility.md before changing application code.
If createContext() fails for an accelerated or high-performance request, retry only through the product's approved fallback plan and surface the failure reason.
If build() or dispatch() fails, check references/examples.md and references/troubleshooting.md for operator, shape, and device mismatches before rewriting the feature.
If context.lost resolves, treat the current context, graph, and tensors as invalid and recreate them before the next inference attempt.
If the product only has a remote inference contract, stop and explain that this skill does not directly apply.
Weekly Installs
82
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