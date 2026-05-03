---
rating: ⭐⭐
title: sealos-app-builder
url: https://skills.sh/zjy365/seakills/sealos-app-builder
---

# sealos-app-builder

skills/zjy365/seakills/sealos-app-builder
sealos-app-builder
Installation
$ npx skills add https://github.com/zjy365/seakills --skill sealos-app-builder
SKILL.md
Sealos App Builder
Overview

Use this skill to turn a generic web app into a Sealos app that runs inside Sealos Desktop, or to scaffold a new Sealos app from scratch. Focus on the repeatable parts: SDK initialization, session access, language sync, business-data integration, local debugging through a Desktop test app, and publish readiness.

Prefer a simple, teachable implementation that a beginner can understand and extend.

Core Workflow
1. Identify the starting point

Classify the request into one of these paths:

Create a new Sealos app from scratch.
Adapt an existing web app to run inside Sealos Desktop.
Add Sealos identity and business-data integration to an app that already renders.
Produce documentation or a tutorial instead of code changes.

If the repository already contains Sealos-related code, inspect local sources first. In particular:

Look for packages/client-sdk or equivalent SDK sources.
Look for existing provider apps under providers/ or similar directories.
Reuse the repository's established framework and routing patterns when they are already in place.

If the repository does not contain local Sealos sources, use the bundled references in this skill as the baseline.

2. Integrate the Sealos app SDK

Treat Sealos Desktop integration as a root-level concern.

Before using any starter template, install the SDK first:

pnpm add @labring/sealos-desktop-sdk


Use npm install @labring/sealos-desktop-sdk or yarn add @labring/sealos-desktop-sdk when the project uses a different package manager.

Initialize the SDK once in a client-only root component.
Fetch getSession() and getLanguage() early.
Store session, language, loading state, and desktop availability in a shared context or store.
Listen for language changes through EVENT_NAME.CHANGE_I18N when the app needs runtime language sync.
Add a graceful fallback when the app is opened outside Sealos Desktop.

Read references/minimal-app-template.md before implementing the root integration. If the app uses Next.js App Router, also read references/nextjs-app-router.md.

Use one of these starter templates:

assets/templates/react/sealos-provider.tsx for React.
assets/templates/vue/use-sealos.ts for Vue.
3. Connect Sealos identity to business data

For most apps, the key integration is not the iframe itself but the user mapping.

Use session.user.id as the stable app-level user identifier.
Persist display-friendly fields such as name, avatar, k8sUsername, and nsid when useful.
Keep business data in the app's own database and API routes.
Model Sealos user identity as input to your business logic, not as your entire backend.

Read references/data-integration-patterns.md when you need schema or API guidance.

4. Prepare local debugging in the real runtime

Do not assume a successful browser render means Sealos integration works.

The app usually needs to be opened by Sealos Desktop in an iframe for SDK calls like getSession() to succeed. When local debugging is part of the task, read references/local-debug-and-test-app.md.

Use these rules:

Explain clearly when a page is outside Sealos Desktop.
Prefer a test app inside Sealos Desktop for end-to-end verification.
Avoid server-side SDK calls.
5. Prepare for publishing

When the user wants deployment or launch readiness:

Verify environment variables.
Verify database connectivity and migrations.
Confirm the app works when launched from Sealos Desktop.
Confirm any cross-app navigation or event usage is valid.
Summarize the remaining manual registration or platform configuration steps.

Use references/publish-checklist.md as the release checklist.

Implementation Rules
Keep the integration simple

Default to the smallest viable Sealos integration:

One root provider or store.
One business identity mapping pattern.
One fallback path for non-Desktop access.

Avoid spreading SDK initialization across multiple pages or components.

Prefer the repository's real SDK surface

If the current workspace contains actual Sealos SDK sources or existing Sealos apps:

Inspect those sources.
Follow the real exported APIs and types.
Call out repository-specific differences from generic examples.
Use the official SDK package name

Use @labring/sealos-desktop-sdk in generated examples and starter code by default.

Only deviate from that if the target repository already has an established local workspace alias and the user explicitly wants to preserve it.

Decision Guide
If the user asks for "How do I build a Sealos app?"

Provide:

A short explanation of the runtime model.
A minimal SDK integration example.
A business-data mapping example.
Local debugging guidance through a Sealos Desktop test app.
If the user asks to modify an existing app

Do this order:

Inspect the current app entry point.
Add or refactor a single root Sealos provider.
Wire business APIs to session.user.id.
Verify fallback behavior outside Desktop.
If the user asks for documentation or a tutorial

Structure the output around:

What a Sealos app is.
How to initialize the SDK.
How to obtain and use the session.
How to integrate business data.
How to debug through a Desktop test app.
How to publish and verify.
References

Read only the files needed for the task:

references/sdk-capabilities.md for available SDK APIs and runtime behavior.
references/minimal-app-template.md for the recommended root integration pattern.
references/nextjs-app-router.md for a concrete Next.js App Router placement example.
references/data-integration-patterns.md for user mapping, database schemas, and API shapes.
references/local-debug-and-test-app.md for iframe-based debugging and Desktop test app setup.
references/publish-checklist.md for launch-readiness steps.
Weekly Installs
35
Repository
zjy365/seakills
GitHub Stars
1
First Seen
Apr 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass