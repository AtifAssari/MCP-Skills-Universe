---
title: ios-xcode
url: https://skills.sh/pproenca/dot-skills/ios-xcode
---

# ios-xcode

skills/pproenca/dot-skills/ios-xcode
ios-xcode
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill ios-xcode
SKILL.md
iOS Xcode & Tooling Best Practices

Comprehensive guide for Xcode project configuration, SwiftData persistence, testing, debugging, profiling, and app distribution. Contains 19 rules across 6 categories.

Clinic Architecture Contract (iOS 26 / Swift 6.2)

All guidance in this skill assumes the clinic modular MVVM-C architecture:

Feature modules import Domain + DesignSystem only (never Data, never sibling features)
App target is the convergence point and owns DependencyContainer, concrete coordinators, and Route Shell wiring
Domain stays pure Swift and defines models plus repository, *Coordinating, ErrorRouting, and AppError contracts
Data owns SwiftData/network/sync/retry/background I/O and implements Domain protocols
Read/write flow defaults to stale-while-revalidate reads and optimistic queued writes
ViewModels call repository protocols directly (no default use-case/interactor layer)
When to Apply

Reference these guidelines when:

Setting up Xcode projects with AppStorage, ScenePhase, or widgets
Implementing SwiftData models, queries, and CRUD operations
Writing tests with Swift Testing framework
Debugging with breakpoints and console output
Profiling performance with Instruments
Distributing apps via TestFlight
Building for visionOS or integrating ML features
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	SwiftData & Persistence	CRITICAL	data-
2	Project & Platform	HIGH	platform-
3	Testing	HIGH	test-
4	Debugging & Profiling	MEDIUM-HIGH	debug-, perf-
5	Distribution	MEDIUM	dist-
6	Specialty Platforms	MEDIUM	ml-, spatial-
Quick Reference
1. Project & Platform (HIGH)
platform-app-storage - Use AppStorage for user preferences
platform-scene-phase - Respond to app lifecycle with ScenePhase
platform-widget-integration - Design for widget and Live Activity integration
platform-system-features - Integrate system features natively
2. SwiftData & Persistence (CRITICAL)
data-model-macro - Define models with @Model macro
data-query-for-fetching - Use @Query for fetching data
data-model-container - Configure model containers
data-relationships - Define model relationships
data-crud-operations - Implement CRUD operations
3. Testing (HIGH)
test-swift-testing - Use Swift Testing framework
test-preview-sample-data - Create preview sample data
test-preview-macro - Use #Preview macro for rapid iteration
4. Debugging & Profiling (MEDIUM-HIGH)
debug-breakpoints - Use breakpoints for debugging
debug-console-output - Use console output for debugging
perf-instruments-profiling - Profile SwiftUI with Instruments
5. Distribution (MEDIUM)
dist-testflight - Distribute via TestFlight
dist-app-icons - Design app icons for distribution
6. Specialty Platforms (MEDIUM)
ml-natural-language - Integrate Natural Language ML
spatial-visionos-windows - Build for visionOS spatial computing
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
Weekly Installs
144
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass