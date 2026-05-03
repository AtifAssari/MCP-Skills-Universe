---
title: swiftui-patterns
url: https://skills.sh/affaan-m/everything-claude-code/swiftui-patterns
---

# swiftui-patterns

skills/affaan-m/everything-claude-code/swiftui-patterns
swiftui-patterns
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill swiftui-patterns
Summary

Modern SwiftUI patterns for declarative, performant UIs with @Observable state management and type-safe navigation.

Covers property wrapper selection (@State, @Observable, @Binding, @Environment), view model architecture, and environment injection for dependency management
Provides view composition strategies, subview extraction, and ViewModifier patterns to minimize re-renders and optimize rendering performance
Includes type-safe NavigationStack routing with NavigationPath and Destination enums for programmatic navigation
Details performance optimization techniques: lazy containers for large collections, stable identifiers, avoiding expensive work in body, and Equatable conformance for complex views
Lists anti-patterns to avoid, including deprecated ObservableObject/@StateObject in favor of @Observable, and improper async handling
SKILL.md
SwiftUI Patterns

Modern SwiftUI patterns for building declarative, performant user interfaces on Apple platforms. Covers the Observation framework, view composition, type-safe navigation, and performance optimization.

When to Activate
Building SwiftUI views and managing state (@State, @Observable, @Binding)
Designing navigation flows with NavigationStack
Structuring view models and data flow
Optimizing rendering performance for lists and complex layouts
Working with environment values and dependency injection in SwiftUI
State Management
Property Wrapper Selection

Choose the simplest wrapper that fits:

Wrapper	Use Case
@State	View-local value types (toggles, form fields, sheet presentation)
@Binding	Two-way reference to parent's @State
@Observable class + @State	Owned model with multiple properties
@Observable class (no wrapper)	Read-only reference passed from parent
@Bindable	Two-way binding to an @Observable property
@Environment	Shared dependencies injected via .environment()
@Observable ViewModel

Use @Observable (not ObservableObject) — it tracks property-level changes so SwiftUI only re-renders views that read the changed property:

@Observable
final class ItemListViewModel {
    private(set) var items: [Item] = []
    private(set) var isLoading = false
    var searchText = ""

    private let repository: any ItemRepository

    init(repository: any ItemRepository = DefaultItemRepository()) {
        self.repository = repository
    }

    func load() async {
        isLoading = true
        defer { isLoading = false }
        items = (try? await repository.fetchAll()) ?? []
    }
}

View Consuming the ViewModel
struct ItemListView: View {
    @State private var viewModel: ItemListViewModel

    init(viewModel: ItemListViewModel = ItemListViewModel()) {
        _viewModel = State(initialValue: viewModel)
    }

    var body: some View {
        List(viewModel.items) { item in
            ItemRow(item: item)
        }
        .searchable(text: $viewModel.searchText)
        .overlay { if viewModel.isLoading { ProgressView() } }
        .task { await viewModel.load() }
    }
}

Environment Injection

Replace @EnvironmentObject with @Environment:

// Inject
ContentView()
    .environment(authManager)

// Consume
struct ProfileView: View {
    @Environment(AuthManager.self) private var auth

    var body: some View {
        Text(auth.currentUser?.name ?? "Guest")
    }
}

View Composition
Extract Subviews to Limit Invalidation

Break views into small, focused structs. When state changes, only the subview reading that state re-renders:

struct OrderView: View {
    @State private var viewModel = OrderViewModel()

    var body: some View {
        VStack {
            OrderHeader(title: viewModel.title)
            OrderItemList(items: viewModel.items)
            OrderTotal(total: viewModel.total)
        }
    }
}

ViewModifier for Reusable Styling
struct CardModifier: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding()
            .background(.regularMaterial)
            .clipShape(RoundedRectangle(cornerRadius: 12))
    }
}

extension View {
    func cardStyle() -> some View {
        modifier(CardModifier())
    }
}

Navigation
Type-Safe NavigationStack

Use NavigationStack with NavigationPath for programmatic, type-safe routing:

@Observable
final class Router {
    var path = NavigationPath()

    func navigate(to destination: Destination) {
        path.append(destination)
    }

    func popToRoot() {
        path = NavigationPath()
    }
}

enum Destination: Hashable {
    case detail(Item.ID)
    case settings
    case profile(User.ID)
}

struct RootView: View {
    @State private var router = Router()

    var body: some View {
        NavigationStack(path: $router.path) {
            HomeView()
                .navigationDestination(for: Destination.self) { dest in
                    switch dest {
                    case .detail(let id): ItemDetailView(itemID: id)
                    case .settings: SettingsView()
                    case .profile(let id): ProfileView(userID: id)
                    }
                }
        }
        .environment(router)
    }
}

Performance
Use Lazy Containers for Large Collections

LazyVStack and LazyHStack create views only when visible:

ScrollView {
    LazyVStack(spacing: 8) {
        ForEach(items) { item in
            ItemRow(item: item)
        }
    }
}

Stable Identifiers

Always use stable, unique IDs in ForEach — avoid using array indices:

// Use Identifiable conformance or explicit id
ForEach(items, id: \.stableID) { item in
    ItemRow(item: item)
}

Avoid Expensive Work in body
Never perform I/O, network calls, or heavy computation inside body
Use .task {} for async work — it cancels automatically when the view disappears
Use .sensoryFeedback() and .geometryGroup() sparingly in scroll views
Minimize .shadow(), .blur(), and .mask() in lists — they trigger offscreen rendering
Equatable Conformance

For views with expensive bodies, conform to Equatable to skip unnecessary re-renders:

struct ExpensiveChartView: View, Equatable {
    let dataPoints: [DataPoint] // DataPoint must conform to Equatable

    static func == (lhs: Self, rhs: Self) -> Bool {
        lhs.dataPoints == rhs.dataPoints
    }

    var body: some View {
        // Complex chart rendering
    }
}

Previews

Use #Preview macro with inline mock data for fast iteration:

#Preview("Empty state") {
    ItemListView(viewModel: ItemListViewModel(repository: EmptyMockRepository()))
}

#Preview("Loaded") {
    ItemListView(viewModel: ItemListViewModel(repository: PopulatedMockRepository()))
}

Anti-Patterns to Avoid
Using ObservableObject / @Published / @StateObject / @EnvironmentObject in new code — migrate to @Observable
Putting async work directly in body or init — use .task {} or explicit load methods
Creating view models as @State inside child views that don't own the data — pass from parent instead
Using AnyView type erasure — prefer @ViewBuilder or Group for conditional views
Ignoring Sendable requirements when passing data to/from actors
References

See skill: swift-actor-persistence for actor-based persistence patterns. See skill: swift-protocol-di-testing for protocol-based DI and testing with Swift Testing.

Weekly Installs
2.9K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass