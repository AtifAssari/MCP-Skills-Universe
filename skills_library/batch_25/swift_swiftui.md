---
title: swift_swiftui
url: https://skills.sh/swiftzilla/skills/swift_swiftui
---

# swift_swiftui

skills/swiftzilla/skills/swift_swiftui
swift_swiftui
Installation
$ npx skills add https://github.com/swiftzilla/skills --skill swift_swiftui
SKILL.md
SwiftUI

This skill covers SwiftUI framework concepts for building declarative user interfaces.

Overview

SwiftUI is Apple's modern declarative framework for building user interfaces across all Apple platforms using a reactive, state-driven approach.

Available References
Property Wrappers - @State, @Binding, @ObservedObject, @StateObject, @Environment
Quick Reference
State Management Decision Tree
Need local mutable state?
├── YES → Is it a value type?
│   ├── YES → Use @State
│   └── NO → Use @StateObject
└── NO → Shared from parent?
    ├── YES → Is it value type?
    │   ├── YES → Use @Binding
    │   └── NO → Use @ObservedObject
    └── NO → Use @Environment

Property Wrappers
Wrapper	Owns Data	Data Type	Use For
@State	Yes	Value type	Local UI state
@Binding	No	Value type	Shared state with parent
@ObservedObject	No	Reference type	Injected dependencies
@StateObject	Yes	Reference type	Owned view models
@Environment	No	Any	Shared resources
Common Usage Patterns
// Local state
struct CounterView: View {
    @State private var count = 0
    
    var body: some View {
        Button("Count: \(count)") { count += 1 }
    }
}

// Shared state (parent to child)
struct ParentView: View {
    @State private var isOn = false
    
    var body: some View {
        ChildView(isOn: $isOn)
    }
}

struct ChildView: View {
    @Binding var isOn: Bool
    
    var body: some View {
        Toggle("Enable", isOn: $isOn)
    }
}

// Observable object
class ViewModel: ObservableObject {
    @Published var items: [Item] = []
}

struct ContentView: View {
    @StateObject private var viewModel = ViewModel()
    
    var body: some View {
        List(viewModel.items) { item in
            Text(item.name)
        }
    }
}

// Environment values
struct EnvironmentView: View {
    @Environment(\.colorScheme) var colorScheme
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        Text(colorScheme == .dark ? "Dark" : "Light")
    }
}

Best Practices
Use @State for local UI state - Toggles, text fields, counters
Lift state up when shared - Single source of truth
Use @StateObject for owned view models - Survives view recreation
Pass @Binding to child views - Two-way data flow
Keep @State minimal - Only store what's needed for UI
Use @Environment for system values - Color scheme, locale, etc.
Access on main thread - All property wrappers require @MainActor
Initialize with underscore - _count = State(initialValue:)
Common Pitfalls
Pitfall	Solution
Initializing @State directly	Use _property = State(initialValue:)
Creating @ObservedObject in init	Use @StateObject instead
Mutating on background thread	Dispatch to main queue
Passing @State instead of Binding	Use $property for Binding
For More Information

Visit https://swiftzilla.dev for comprehensive SwiftUI documentation.

Weekly Installs
51
Repository
swiftzilla/skills
GitHub Stars
6
First Seen
Jan 28, 2026