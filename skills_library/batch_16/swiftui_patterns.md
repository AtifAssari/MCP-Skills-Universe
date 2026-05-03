---
title: swiftui-patterns
url: https://skills.sh/johnrogers/claude-swift-engineering/swiftui-patterns
---

# swiftui-patterns

skills/johnrogers/claude-swift-engineering/swiftui-patterns
swiftui-patterns
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill swiftui-patterns
SKILL.md
SwiftUI Patterns (iOS 17+)

SwiftUI 17+ removes ObservableObject boilerplate with @Observable, simplifies environment injection with @Environment, and introduces task-based async patterns. The core principle: use Apple's modern APIs instead of reactive libraries.

Overview
Quick Reference
Need	Use (iOS 17+)	NOT
Observable model	@Observable	ObservableObject
Published property	Regular property	@Published
Own state	@State	@StateObject
Passed model (binding)	@Bindable	@ObservedObject
Environment injection	environment(_:)	environmentObject(_:)
Environment access	@Environment(Type.self)	@EnvironmentObject
Async on appear	.task { }	.onAppear { Task {} }
Value change	onChange(of:initial:_:)	onChange(of:perform:)
Core Workflow
Use @Observable for model classes (no @Published needed)
Use @State for view-owned models, @Bindable for passed models
Use .task { } for async work (auto-cancels on disappear)
Use NavigationStack with NavigationPath for programmatic navigation
Apply .accessibilityLabel() and .accessibilityHint() to interactive elements
Reference Loading Guide

ALWAYS load reference files if there is even a small chance the content may be required. It's better to have the context than to miss a pattern or make a mistake.

Reference	Load When
Observable	Creating new @Observable model classes
State Management	Deciding between @State, @Bindable, @Environment
Environment	Injecting dependencies into view hierarchy
View Modifiers	Using onChange, task, or iOS 17+ modifiers
Migration Guide	Updating iOS 16 code to iOS 17+
MVVM Observable	Setting up view model architecture
Navigation	Programmatic or deep-link navigation
Performance	Lists with 100+ items or excessive re-renders
UIKit Interop	Wrapping UIKit components (WKWebView, PHPicker)
Accessibility	VoiceOver, Dynamic Type, accessibility actions
Async Patterns	Loading states, refresh, background tasks
Composition	Reusable view modifiers or complex conditional UI
Common Mistakes

Over-using @Bindable for passed models — Creating @Bindable for every property causes unnecessary view reloads. Use @Bindable only for mutable model properties that need two-way binding. Read-only computed properties should use regular properties.

State placement errors — Putting model state in the view instead of a dedicated @Observable model causes view logic to become tangled. Always separate model and view concerns.

NavigationPath state corruption — Mutating NavigationPath incorrectly can leave it in inconsistent state. Use navigationDestination(for:destination:) with proper state management to avoid path corruption.

Missing .task cancellation — .task handles cancellation on disappear automatically, but nested Tasks don't. Complex async flows need explicit cancellation tracking to avoid zombie tasks.

Ignoring environment invalidation — Changing environment values at parent doesn't invalidate child views automatically. Use @Environment consistently and understand when re-renders happen based on observation.

UIKit interop memory leaks — UIViewRepresentable and UIViewControllerRepresentable can leak if delegate cycles aren't broken. Weak references and explicit cleanup are required.

Weekly Installs
172
Repository
johnrogers/clau…ineering
GitHub Stars
201
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn