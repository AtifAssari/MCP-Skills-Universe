---
title: swiftui-pro
url: https://skills.sh/twostraws/swiftui-agent-skill/swiftui-pro
---

# swiftui-pro

skills/twostraws/swiftui-agent-skill/swiftui-pro
swiftui-pro
Installation
$ npx skills add https://github.com/twostraws/swiftui-agent-skill --skill swiftui-pro
Summary

Comprehensive SwiftUI code review against modern APIs, accessibility, and performance standards.

Validates code across nine dimensions: deprecated APIs, view optimization, data flow, navigation, design compliance, accessibility (Dynamic Type, VoiceOver, Reduce Motion), performance, Swift concurrency, and code hygiene
References built-in guides for each review category, enabling targeted partial reviews when needed
Targets iOS 26+ and Swift 6.2 with modern concurrency patterns; prioritizes SwiftUI over UIKit
Reports only genuine issues with before/after code fixes, organized by file and prioritized by impact
Enforces consistent project structure with separate files per type and feature-based folder layout
SKILL.md

Review Swift and SwiftUI code for correctness, modern API usage, and adherence to project conventions. Report only genuine problems - do not nitpick or invent issues.

Review process:

Check for deprecated API using references/api.md.
Check that views, modifiers, and animations have been written optimally using references/views.md.
Validate that data flow is configured correctly using references/data.md.
Ensure navigation is updated and performant using references/navigation.md.
Ensure the code uses designs that are accessible and compliant with Apple’s Human Interface Guidelines using references/design.md.
Validate accessibility compliance including Dynamic Type, VoiceOver, and Reduce Motion using references/accessibility.md.
Ensure the code is able to run efficiently using references/performance.md.
Quick validation of Swift code using references/swift.md.
Final code hygiene check using references/hygiene.md.

If doing a partial review, load only the relevant reference files.

Core Instructions
iOS 26 exists, and is the default deployment target for new apps.
Target Swift 6.2 or later, using modern Swift concurrency.
As a SwiftUI developer, the user will want to avoid UIKit unless requested.
Do not introduce third-party frameworks without asking first.
Break different types up into different Swift files rather than placing multiple structs, classes, or enums into a single file.
Use a consistent project structure, with folder layout determined by app features.
Output Format

Organize findings by file. For each issue:

State the file and relevant line(s).
Name the rule being violated (e.g., "Use foregroundStyle() instead of foregroundColor()").
Show a brief before/after code fix.

Skip files with no issues. End with a prioritized summary of the most impactful changes to make first.

Example output:

ContentView.swift

Line 12: Use foregroundStyle() instead of foregroundColor().

// Before
Text("Hello").foregroundColor(.red)

// After
Text("Hello").foregroundStyle(.red)


Line 24: Icon-only button is bad for VoiceOver - add a text label.

// Before
Button(action: addUser) {
    Image(systemName: "plus")
}

// After
Button("Add User", systemImage: "plus", action: addUser)


Line 31: Avoid Binding(get:set:) in view body - use @State with onChange() instead.

// Before
TextField("Username", text: Binding(
    get: { model.username },
    set: { model.username = $0; model.save() }
))

// After
TextField("Username", text: $model.username)
    .onChange(of: model.username) {
        model.save()
    }

Summary
Accessibility (high): The add button on line 24 is invisible to VoiceOver.
Deprecated API (medium): foregroundColor() on line 12 should be foregroundStyle().
Data flow (medium): The manual binding on line 31 is fragile and harder to maintain.

End of example.

References
references/accessibility.md - Dynamic Type, VoiceOver, Reduce Motion, and other accessibility requirements.
references/api.md - updating code for modern API, and the deprecated code it replaces.
references/design.md - guidance for building accessible apps that meet Apple’s Human Interface Guidelines.
references/hygiene.md - making code compile cleanly and be maintainable in the long term.
references/navigation.md - navigation using NavigationStack/NavigationSplitView, plus alerts, confirmation dialogs, and sheets.
references/performance.md - optimizing SwiftUI code for maximum performance.
references/data.md - data flow, shared state, and property wrappers.
references/swift.md - tips on writing modern Swift code, including using Swift Concurrency effectively.
references/views.md - view structure, composition, and animation.
Weekly Installs
14.2K
Repository
twostraws/swift…nt-skill
GitHub Stars
3.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass