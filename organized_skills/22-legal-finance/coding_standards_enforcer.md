---
rating: ⭐⭐
title: coding-standards-enforcer
url: https://skills.sh/tomkrikorian/visionosagents/coding-standards-enforcer
---

# coding-standards-enforcer

skills/tomkrikorian/visionosagents/coding-standards-enforcer
coding-standards-enforcer
Installation
$ npx skills add https://github.com/tomkrikorian/visionosagents --skill coding-standards-enforcer
SKILL.md
Coding Standards Enforcer
Quick Start

Use this skill whenever Swift source changes are in scope and the question is whether the code matches the repository's concurrency, observation, and modern API standards.

Classify the work first:
Swift 6.2 build-setting / language-mode problem
isolation / actor / Sendable problem
view-model / observation / ownership problem
modern API / style / safety cleanup
Load only the reference files that match that category.
Review the changed code in this order:
compiler diagnostics and isolation boundaries
ownership and observation model
API modernization and safety
Fix or flag deviations explicitly; do not leave standards violations implied.
Load References When
Reference	When to Use
references/standards-review-map.md	When you need the review order, routing, and repo-level standards map.
references/concurrency-guidelines.md	When the work touches actors, @MainActor, Sendable, Task, async let, task groups, or strict concurrency diagnostics.
references/observation-modeling.md	When the work touches @Observable, view models, @State, @Binding, environment injection, or Combine-to-Observation migration.
references/modern-swift-apis.md	When the work is about API modernization, Foundation replacements, formatting, string matching, force unwraps, or Swift-native style.
Workflow
Inspect the changed Swift files and note the primary failure class.
Load the narrowest relevant reference file or files.
Apply the minimum change that restores compliance.
Rebuild or rerun the affected test scope if available.
Summarize what was fixed, what was intentionally left alone, and any remaining migration debt.
When To Switch Skills
Switch to spatial-app-architecture when the core problem is scene ownership, feature decomposition, or state placement across surfaces.
Switch to build-run-debug when the main blocker is a build failure or a runtime issue that still needs reproduction after standards fixes.
Switch to test-triage when the work is primarily about narrowing a failing test scope rather than correcting standards violations directly.
Guardrails
Do not impose a blanket @MainActor policy. The isolation choice has to match ownership and runtime behavior.
In new SwiftUI or visionOS code, do not introduce ObservableObject, @StateObject, or @ObservedObject unless the user explicitly states a compatibility constraint or the existing architecture cannot yet leave Combine-based observation.
Do not put @StateObject or @ObservedObject around an @Observable type; use @State, @Bindable, or typed @Environment according to ownership.
Do not "fix" concurrency warnings by introducing unnecessary Task.detached, DispatchQueue.main.async, or @unchecked Sendable.
Do not assume Swift 6.2 default actor isolation from memory; inspect project build settings when that choice affects the fix.
Do not modernize APIs mechanically if it changes semantics.
Output Expectations

Provide:

the files or symbols reviewed
which standards category was applied
the concrete violations fixed or still present
the validation step used
the next skill to use if the blocker is no longer a standards question
Weekly Installs
43
Repository
tomkrikorian/vi…osagents
GitHub Stars
49
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass