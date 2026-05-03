---
title: swiftui-ui-patterns
url: https://skills.sh/dimillian/skills/swiftui-ui-patterns
---

# swiftui-ui-patterns

skills/dimillian/skills/swiftui-ui-patterns
swiftui-ui-patterns
Originally fromopenai/plugins
Installation
$ npx skills add https://github.com/dimillian/skills --skill swiftui-ui-patterns
Summary

Best practices and patterns for building SwiftUI views, navigation, and state management.

Covers state ownership strategies (from @State and @Binding to @Observable on iOS 17+), async/await patterns with .task, and environment injection for shared dependencies
Includes cross-cutting references for NavigationStack routing, sheet presentation, deep linking, and app-level wiring with concrete ownership rules
Provides component-specific guidance via indexed references, with anti-patterns and performance considerations for large or scroll-heavy screens
Workflow-driven approach: define state ownership and dependencies first, sketch hierarchy, implement async loading with explicit states, then validate with previews and builds
SKILL.md
SwiftUI UI Patterns
Quick start

Choose a track based on your goal:

Existing project
Identify the feature or screen and the primary interaction model (list, detail, editor, settings, tabbed).
Find a nearby example in the repo with rg "TabView\(" or similar, then read the closest SwiftUI view.
Apply local conventions: prefer SwiftUI-native state, keep state local when possible, and use environment injection for shared dependencies.
Choose the relevant component reference from references/components-index.md and follow its guidance.
If the interaction reveals secondary content by dragging or scrolling the primary content away, read references/scroll-reveal.md before implementing gestures manually.
Build the view with small, focused subviews and SwiftUI-native data flow.
New project scaffolding
Start with references/app-wiring.md to wire TabView + NavigationStack + sheets.
Add a minimal AppTab and RouterPath based on the provided skeletons.
Choose the next component reference based on the UI you need first (TabView, NavigationStack, Sheets).
Expand the route and sheet enums as new screens are added.
General rules to follow
Use modern SwiftUI state (@State, @Binding, @Observable, @Environment) and avoid unnecessary view models.
If the deployment target includes iOS 16 or earlier and cannot use the Observation API introduced in iOS 17, fall back to ObservableObject with @StateObject for root ownership, @ObservedObject for injected observation, and @EnvironmentObject only for truly shared app-level state.
Prefer composition; keep views small and focused.
Use async/await with .task and explicit loading/error states. For restart, cancellation, and debouncing guidance, read references/async-state.md.
Keep shared app services in @Environment, but prefer explicit initializer injection for feature-local dependencies and models. For root wiring patterns, read references/app-wiring.md.
Prefer the newest SwiftUI API that fits the deployment target and call out the minimum OS whenever a pattern depends on it.
Maintain existing legacy patterns only when editing legacy files.
Follow the project's formatter and style guide.
Sheets: Prefer .sheet(item:) over .sheet(isPresented:) when state represents a selected model. Avoid if let inside a sheet body. Sheets should own their actions and call dismiss() internally instead of forwarding onCancel/onConfirm closures.
Scroll-driven reveals: Prefer deriving a normalized progress value from scroll offset and driving the visual state from that single source of truth. Avoid parallel gesture state machines unless scroll alone cannot express the interaction.
State ownership summary

Use the narrowest state tool that matches the ownership model:

Scenario	Preferred pattern
Local UI state owned by one view	@State
Child mutates parent-owned value state	@Binding
Root-owned reference model on iOS 17+	@State with an @Observable type
Child reads or mutates an injected @Observable model on iOS 17+	Pass it explicitly as a stored property
Shared app service or configuration	@Environment(Type.self)
Legacy reference model on iOS 16 and earlier	@StateObject at the root, @ObservedObject when injected

Choose the ownership location first, then pick the wrapper. Do not introduce a reference model when plain value state is enough.

Cross-cutting references
references/navigationstack.md: navigation ownership, per-tab history, and enum routing.
references/sheets.md: centralized modal presentation and enum-driven sheets.
references/deeplinks.md: URL handling and routing external links into app destinations.
references/app-wiring.md: root dependency graph, environment usage, and app shell wiring.
references/async-state.md: .task, .task(id:), cancellation, debouncing, and async UI state.
references/previews.md: #Preview, fixtures, mock environments, and isolated preview setup.
references/performance.md: stable identity, observation scope, lazy containers, and render-cost guardrails.
Anti-patterns
Giant views that mix layout, business logic, networking, routing, and formatting in one file.
Multiple boolean flags for mutually exclusive sheets, alerts, or navigation destinations.
Live service calls directly inside body-driven code paths instead of view lifecycle hooks or injected models/services.
Reaching for AnyView to work around type mismatches that should be solved with better composition.
Defaulting every shared dependency to @EnvironmentObject or a global router without a clear ownership reason.
Workflow for a new SwiftUI view
Define the view's state, ownership location, and minimum OS assumptions before writing UI code.
Identify which dependencies belong in @Environment and which should stay as explicit initializer inputs.
Sketch the view hierarchy, routing model, and presentation points; extract repeated parts into subviews. For complex navigation, read references/navigationstack.md, references/sheets.md, or references/deeplinks.md. Build and verify no compiler errors before proceeding.
Implement async loading with .task or .task(id:), plus explicit loading and error states when needed. Read references/async-state.md when the work depends on changing inputs or cancellation.
Add previews for the primary and secondary states, then add accessibility labels or identifiers when the UI is interactive. Read references/previews.md when the view needs fixtures or injected mock dependencies.
Validate with a build: confirm no compiler errors, check that previews render without crashing, ensure state changes propagate correctly, and sanity-check that list identity and observation scope will not cause avoidable re-renders. Read references/performance.md if the screen is large, scroll-heavy, or frequently updated. For common SwiftUI compilation errors — missing @State annotations, ambiguous ViewBuilder closures, or mismatched generic types — resolve them before updating callsites. If the build fails: read the error message carefully, fix the identified issue, then rebuild before proceeding to the next step. If a preview crashes, isolate the offending subview, confirm its state initialisation is valid, and re-run the preview before continuing.
Component references

Use references/components-index.md as the entry point. Each component reference should include:

Intent and best-fit scenarios.
Minimal usage pattern with local conventions.
Pitfalls and performance notes.
Paths to existing examples in the current repo.
Adding a new component reference
Create references/<component>.md.
Keep it short and actionable; link to concrete files in the current repo.
Update references/components-index.md with the new entry.
Weekly Installs
2.1K
Repository
dimillian/skills
GitHub Stars
3.4K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn