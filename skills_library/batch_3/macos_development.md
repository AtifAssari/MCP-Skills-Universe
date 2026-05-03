---
title: macos-development
url: https://skills.sh/rshankras/claude-code-apple-skills/macos-development
---

# macos-development

skills/rshankras/claude-code-apple-skills/macos-development
macos-development
Installation
$ npx skills add https://github.com/rshankras/claude-code-apple-skills --skill macos-development
Summary

Expert guidance for Swift 6+, SwiftUI, SwiftData, and macOS 26 development with architecture patterns and platform integration.

Covers Swift 6+ modern concurrency, SwiftData schema design and query optimization, and SwiftUI best practices with AppKit bridging
Includes SOLID principles, design patterns, and modular architecture approaches tailored to macOS projects
Provides macOS 26 (Tahoe) feature guidance, Apple Intelligence integration, on-device ML with MLX, and Xcode 16 tooling
Supports code review, UI/UX review against Human Interface Guidelines, sandboxing and entitlements, and cross-device continuity features
Modular structure lets you pull specific guidance for data persistence, project organization, accessibility, or new app architecture planning
SKILL.md
macOS Development Expert

Comprehensive guidance for macOS app development. This skill aggregates specialized modules for different aspects of macOS development.

When This Skill Activates

Use this skill when the user:

Asks about macOS development best practices
Wants code review for macOS/Swift projects
Needs help with SwiftUI, SwiftData, or AppKit
Is implementing macOS 26 (Tahoe) features
Wants UI/UX review against HIG
Needs architecture guidance for macOS apps
Available Modules

Read relevant module files based on the user's needs:

coding-best-practices/

Swift 6+ code quality and modern idioms.

swift-language.md - Modern Swift patterns
modern-concurrency.md - async/await, actors, Sendable
data-persistence.md - SwiftData, UserDefaults, Keychain
code-organization.md - Project structure and modularity
architecture-principles.md - Clean architecture patterns
architecture-patterns/

Software design and architecture.

solid-detailed.md - SOLID principles with Swift examples
design-patterns.md - Common design patterns
modular-design.md - Modular architecture approaches
swiftdata-architecture/

SwiftData deep dive.

schema-design.md - Model design and relationships
query-patterns.md - Efficient queries and predicates
performance.md - Optimization techniques
macos-tahoe-apis/

macOS 26 specific features.

tahoe-features.md - New macOS 26 capabilities
apple-intelligence.md - AI/ML integration
mlx-framework.md - On-device ML with MLX
continuity.md - Cross-device features
xcode16.md - Xcode 16 tools and features
macos-capabilities/

Platform integration.

sandboxing.md - App Sandbox and entitlements
System integration features
appkit-swiftui-bridge/

Hybrid development.

nsviewrepresentable.md - Wrapping AppKit views
State management between frameworks
ui-review-tahoe/

UI/UX review for macOS 26.

Liquid Glass design system
HIG compliance checking
Accessibility review
app-planner/

Project planning and analysis.

New app architecture planning
Existing app audits
How to Use
Identify user's need from their question
Read relevant module files from subdirectories
Apply the guidance to their specific context
Reference Apple documentation when needed
Example Workflow

User asks about SwiftData performance:

Read swiftdata-architecture/performance.md
Read swiftdata-architecture/query-patterns.md if relevant
Apply recommendations to their code
Weekly Installs
599
Repository
rshankras/claud…e-skills
GitHub Stars
312
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass