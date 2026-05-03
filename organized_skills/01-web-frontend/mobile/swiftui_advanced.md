---
rating: ⭐⭐
title: swiftui-advanced
url: https://skills.sh/johnrogers/claude-swift-engineering/swiftui-advanced
---

# swiftui-advanced

skills/johnrogers/claude-swift-engineering/swiftui-advanced
swiftui-advanced
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill swiftui-advanced
SKILL.md
SwiftUI Advanced

Advanced SwiftUI patterns for gesture composition, adaptive layouts, architecture decisions, and performance optimization.

Reference Loading Guide

ALWAYS load reference files if there is even a small chance the content may be required. It's better to have the context than to miss a pattern or make a mistake.

Reference	Load When
Gestures	Composing multiple gestures, GestureState, custom recognizers
Adaptive Layout	ViewThatFits, AnyLayout, size classes, iOS 26 free-form windows
Architecture	MVVM vs TCA decision, State-as-Bridge, property wrapper selection
Performance	Instruments 26, view body optimization, unnecessary updates
Core Workflow
Identify pattern category from user's question
Load relevant reference for detailed patterns and code examples
Apply pattern following the decision trees and anti-patterns
Verify using provided checklists or profiling guidance
Decision Trees
Gesture Composition
Both gestures at same time? -> .simultaneously
One must complete before next? -> .sequenced
Only one should win? -> .exclusively
Layout Adaptation
Pick best-fitting variant? -> ViewThatFits
Animated H/V switch? -> AnyLayout
Need actual dimensions? -> onGeometryChange
Architecture Selection
Small app, Apple patterns? -> @Observable + State-as-Bridge
Complex presentation logic? -> MVVM with @Observable
Rigorous testability needed? -> TCA
Common Mistakes

Gesture composition order matters — .simultaneously and .sequenced have different trigger timing. Swapping them silently changes behavior. Understand gesture semantics before using.

ViewThatFits over-used — ViewThatFits remeasures on every view change. For animated H/V switches, use AnyLayout instead. Use ViewThatFits only for static variant selection.

onGeometryChange triggering unnecessary updates — Reading geometry changes geometry, which triggers updates, which changes geometry... circular. Use .onGeometryChange only with proper state management to avoid loops.

Architecture mismatch mid-project — Starting with @Observable + State-as-Bridge then realizing you need TCA is expensive. Choose architecture upfront based on complexity (small app = @Observable, complex = TCA).

Ignoring view body optimization — Computing expensive calculations in view body repeatedly kills performance. Move calculations to properties or models. Profile with Instruments 26 before optimizing prematurely.

Weekly Installs
102
Repository
johnrogers/clau…ineering
GitHub Stars
201
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass