---
rating: ⭐⭐
title: app-intents
url: https://skills.sh/dpearson2699/swift-ios-skills/app-intents
---

# app-intents

skills/dpearson2699/swift-ios-skills/app-intents
app-intents
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill app-intents
Summary

Implement App Intents to expose app functionality to Siri, Shortcuts, Spotlight, widgets, and Apple Intelligence.

Covers seven integration surfaces: Siri/Shortcuts, configurable widgets, Control Center, Spotlight search, Apple Intelligence schemas, interactive snippets, and visual intelligence queries
Requires shadow AppEntity models with EntityQuery variants (base, string search, enumerable, or singleton), plus AppEnum for fixed parameter choices
Includes AppShortcutsProvider for pre-built shortcuts with phrase registration, WidgetConfigurationIntent for widget parameters, and IndexedEntity with structured metadata keys for Spotlight (iOS 18+)
iOS 26 additions: SnippetIntent for interactive system UI snippets and IntentValueQuery for visual intelligence value resolution
SKILL.md
App Intents (iOS 26+)

Implement, review, and extend App Intents to expose app functionality to Siri, Shortcuts, Spotlight, widgets, Control Center, and Apple Intelligence.

Contents
Triage Workflow
AppIntent Protocol
@Parameter
AppEntity
EntityQuery (4 Variants)
AppEnum
AppShortcutsProvider
Siri Integration
Interactive Widget Intents
Control Center Widgets (iOS 18+)
Spotlight and IndexedEntity (iOS 18+)
iOS 26 Additions
Common Mistakes
Review Checklist
References
Triage Workflow
Step 1: Identify the integration surface

Determine which system feature the intent targets:

Surface	Protocol	Since
Siri / Shortcuts	AppIntent	iOS 16
Configurable widget	WidgetConfigurationIntent	iOS 17
Control Center	ControlConfigurationIntent	iOS 18
Spotlight search	IndexedEntity	iOS 18
Apple Intelligence	@AppIntent(schema:)	iOS 18
Interactive snippets	SnippetIntent	iOS 26
Visual Intelligence	IntentValueQuery	iOS 26
Step 2: Define the data model
Create AppEntity shadow models (do NOT conform core data models directly).
Create AppEnum types for fixed parameter choices.
Choose the right EntityQuery variant for resolution.
Mark searchable entities with IndexedEntity and @Property(indexingKey:).
Step 3: Implement the intent
Conform to AppIntent (or a specialized sub-protocol).
Declare @Parameter properties for all user-facing inputs.
Implement perform() async throws -> some IntentResult.
Add parameterSummary for Shortcuts UI.
Register phrases via AppShortcutsProvider.
Step 4: Verify
Build and run in Shortcuts app to confirm parameter resolution.
Test Siri phrases with the intent preview in Xcode.
Confirm Spotlight results for IndexedEntity types.
Check widget configuration for WidgetConfigurationIntent intents.
AppIntent Protocol

The system instantiates the struct via init(), sets parameters, then calls perform(). Declare a title and parameterSummary for Shortcuts UI.

struct OrderSoupIntent: AppIntent {
    static var title: LocalizedStringResource = "Order Soup"
    static var description = IntentDescription("Place a soup order.")

    @Parameter(title: "Soup") var soup: SoupEntity
    @Parameter(title: "Quantity", default: 1) var quantity: Int

    static var parameterSummary: some ParameterSummary {
        Summary("Order \(\.$soup)") { \.$quantity }
    }

    func perform() async throws -> some IntentResult {
        try await OrderService.shared.place(soup: soup.id, quantity: quantity)
        return .result(dialog: "Ordered \(quantity) \(soup.name).")
    }
}


Optional members: description (IntentDescription), openAppWhenRun (Bool), isDiscoverable (Bool), authenticationPolicy (IntentAuthenticationPolicy).

@Parameter

Declare each user-facing input with @Parameter. Optional parameters are not required; non-optional parameters with a default are pre-filled.

// WRONG: Non-optional parameter without default -- system cannot preview
@Parameter(title: "Count")
var count: Int

// CORRECT: Provide a default or make optional
@Parameter(title: "Count", default: 1)
var count: Int

@Parameter(title: "Count")
var count: Int?

Supported value types

Primitives: Int, Double, Bool, String, URL, Date, DateComponents. Framework: Currency, Person, IntentFile. Measurements: Measurement<UnitLength>, Measurement<UnitTemperature>, and others. Custom: any AppEntity or AppEnum.

Common initializer patterns
// Basic
@Parameter(title: "Name")
var name: String

// With default
@Parameter(title: "Count", default: 5)
var count: Int

// Numeric slider
@Parameter(title: "Volume", controlStyle: .slider, inclusiveRange: (0, 100))
var volume: Int

// Options provider (dynamic list)
@Parameter(title: "Category", optionsProvider: CategoryOptionsProvider())
var category: Category

// File with content types
@Parameter(title: "Document", supportedContentTypes: [.pdf, .plainText])
var document: IntentFile

// Measurement with unit
@Parameter(title: "Distance", defaultUnit: .miles, supportsNegativeNumbers: false)
var distance: Measurement<UnitLength>


See references/appintents-advanced.md for all initializer variants.

AppEntity

Create shadow models that mirror app data -- never conform core data model types directly.

struct SoupEntity: AppEntity {
    static let defaultQuery = SoupEntityQuery()
    static var typeDisplayRepresentation: TypeDisplayRepresentation = "Soup"
    var id: String

    @Property(title: "Name") var name: String
    @Property(title: "Price") var price: Double

    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(title: "\(name)", subtitle: "$\(String(format: "%.2f", price))")
    }

    init(from soup: Soup) {
        self.id = soup.id; self.name = soup.name; self.price = soup.price
    }
}


Required: id, defaultQuery (static), displayRepresentation, typeDisplayRepresentation (static). Mark properties with @Property(title:) to expose for filtering/sorting. Properties without @Property remain internal.

EntityQuery (4 Variants)
1. EntityQuery (base -- resolve by ID)
struct SoupEntityQuery: EntityQuery {
    func entities(for identifiers: [String]) async throws -> [SoupEntity] {
        SoupStore.shared.soups.filter { identifiers.contains($0.id) }.map { SoupEntity(from: $0) }
    }
    func suggestedEntities() async throws -> [SoupEntity] {
        SoupStore.shared.featured.map { SoupEntity(from: $0) }
    }
}

2. EntityStringQuery (free-text search)
struct SoupStringQuery: EntityStringQuery {
    func entities(matching string: String) async throws -> [SoupEntity] {
        SoupStore.shared.search(string).map { SoupEntity(from: $0) }
    }
    func entities(for identifiers: [String]) async throws -> [SoupEntity] {
        SoupStore.shared.soups.filter { identifiers.contains($0.id) }.map { SoupEntity(from: $0) }
    }
}

3. EnumerableEntityQuery (finite set)
struct AllSoupsQuery: EnumerableEntityQuery {
    func allEntities() async throws -> [SoupEntity] {
        SoupStore.shared.allSoups.map { SoupEntity(from: $0) }
    }
    func entities(for identifiers: [String]) async throws -> [SoupEntity] {
        SoupStore.shared.soups.filter { identifiers.contains($0.id) }.map { SoupEntity(from: $0) }
    }
}

4. UniqueAppEntityQuery (singleton, iOS 18+)

Use for single-instance entities like app settings.

struct AppSettingsEntity: UniqueAppEntity {
    static let defaultQuery = AppSettingsQuery()
    static var typeDisplayRepresentation: TypeDisplayRepresentation = "Settings"
    var displayRepresentation: DisplayRepresentation { "App Settings" }

    var id: String { "app-settings" }
}

struct AppSettingsQuery: UniqueAppEntityQuery {
    func entity() async throws -> AppSettingsEntity {
        AppSettingsEntity()
    }
}


See references/appintents-advanced.md for EntityPropertyQuery with filter/sort support.

AppEnum

Define fixed sets of selectable values. Must be backed by a LosslessStringConvertible raw value (use String).

enum SoupSize: String, AppEnum {
    case small, medium, large

    static var typeDisplayRepresentation: TypeDisplayRepresentation = "Size"

    static var caseDisplayRepresentations: [SoupSize: DisplayRepresentation] = [
        .small: "Small",
        .medium: "Medium",
        .large: "Large"
    ]
}

// WRONG: Using Int raw value
enum Priority: Int, AppEnum { // Compiler error -- Int is not LosslessStringConvertible
    case low = 1, medium = 2, high = 3
}

// CORRECT: Use String raw value
enum Priority: String, AppEnum {
    case low, medium, high
    // ...
}

AppShortcutsProvider

Register pre-built shortcuts that appear in Siri and the Shortcuts app without user configuration.

struct MyAppShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: OrderSoupIntent(),
            phrases: [
                "Order \(\.$soup) in \(.applicationName)",
                "Get soup from \(.applicationName)"
            ],
            shortTitle: "Order Soup",
            systemImageName: "cup.and.saucer"
        )
    }

    static var shortcutTileColor: ShortcutTileColor = .navy
}

Phrase rules
Every phrase MUST include \(.applicationName).
Phrases can reference parameters: \(\.$soup).
Call updateAppShortcutParameters() when dynamic option values change.
Use negativePhrases to prevent false Siri activations.
Siri Integration
Donating intents

Donate intents so the system learns user patterns and suggests them in Spotlight:

let intent = OrderSoupIntent()
intent.soup = favoriteSoupEntity
try await intent.donate()

Predictable intents

Conform to PredictableIntent for Siri prediction of upcoming actions.

Interactive Widget Intents

Use AppIntent with Button/Toggle in widgets. Use WidgetConfigurationIntent for configurable widget parameters.

struct ToggleFavoriteIntent: AppIntent {
    static var title: LocalizedStringResource = "Toggle Favorite"
    @Parameter(title: "Item ID") var itemID: String

    func perform() async throws -> some IntentResult {
        FavoriteStore.shared.toggle(itemID)
        return .result()
    }
}

// In widget view:
Button(intent: ToggleFavoriteIntent(itemID: entry.id)) {
    Image(systemName: entry.isFavorite ? "heart.fill" : "heart")
}

WidgetConfigurationIntent
struct BookWidgetConfig: WidgetConfigurationIntent {
    static var title: LocalizedStringResource = "Favorite Book"
    @Parameter(title: "Book", default: "The Swift Programming Language") var bookTitle: String
}

// Connect to WidgetKit:
struct MyWidget: Widget {
    var body: some WidgetConfiguration {
        AppIntentConfiguration(kind: "FavoriteBook", intent: BookWidgetConfig.self, provider: MyTimelineProvider()) { entry in
            BookWidgetView(entry: entry)
        }
    }
}

Control Center Widgets (iOS 18+)

Expose controls in Control Center and Lock Screen with ControlConfigurationIntent and ControlWidget.

struct LightControlConfig: ControlConfigurationIntent {
    static var title: LocalizedStringResource = "Light Control"
    @Parameter(title: "Light", default: .livingRoom) var light: LightEntity
}

struct ToggleLightIntent: AppIntent {
    static var title: LocalizedStringResource = "Toggle Light"
    @Parameter(title: "Light") var light: LightEntity
    func perform() async throws -> some IntentResult {
        try await LightService.shared.toggle(light.id)
        return .result()
    }
}

struct LightControl: ControlWidget {
    var body: some ControlWidgetConfiguration {
        AppIntentControlConfiguration(kind: "LightControl", intent: LightControlConfig.self) { config in
            ControlWidgetToggle(config.light.name, isOn: config.light.isOn, action: ToggleLightIntent(light: config.light))
        }
    }
}

Spotlight and IndexedEntity (iOS 18+)

Conform to IndexedEntity for Spotlight search. On iOS 26+, use indexingKey for structured metadata:

struct RecipeEntity: IndexedEntity {
    static let defaultQuery = RecipeQuery()
    static var typeDisplayRepresentation: TypeDisplayRepresentation = "Recipe"
    var id: String

    @Property(title: "Name", indexingKey: .title) var name: String   // iOS 26+
    @ComputedProperty(indexingKey: .description)                      // iOS 26+
    var summary: String { "\(name) -- a delicious recipe" }

    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(title: "\(name)")
    }
}

iOS 26 Additions
SnippetIntent

Display interactive snippets in system UI:

struct OrderStatusSnippet: SnippetIntent {
    static var title: LocalizedStringResource = "Order Status"
    func perform() async throws -> some IntentResult & ShowsSnippetView {
        let status = await OrderTracker.currentStatus()
        return .result(view: OrderStatusSnippetView(status: status))
    }
    static func reload() { /* notify system to refresh */ }
}

// A calling intent can display this snippet via:
// return .result(snippetIntent: OrderStatusSnippet())

IntentValueQuery (Visual Intelligence)
struct ProductValueQuery: IntentValueQuery {
    typealias Input = String
    typealias Result = ProductEntity
    func values(for input: String) async throws -> [ProductEntity] {
        ProductStore.shared.search(input).map { ProductEntity(from: $0) }
    }
}

Common Mistakes

Conforming core data models to AppEntity. Create dedicated shadow models instead. Core models carry persistence logic that conflicts with intent lifecycle.

Missing \(.applicationName) in phrases. Every AppShortcut phrase MUST include the application name token. Siri uses it for disambiguation.

Non-optional @Parameter without default. The system cannot preview or pre-fill such parameters. Make non-optional parameters have a default, or mark them optional.

// WRONG
@Parameter(title: "Count")
var count: Int

// CORRECT
@Parameter(title: "Count", default: 1)
var count: Int


Using Int raw value for AppEnum. AppEnum requires RawRepresentable where RawValue: LosslessStringConvertible. Use String.

Forgetting suggestedEntities(). Without it, the Shortcuts picker shows no defaults.

Throwing for missing entities in entities(for:). Omit missing entities instead.

Stale Spotlight index. Call updateAppShortcutParameters() when entity data changes.

Missing typeDisplayRepresentation. Both AppEntity and AppEnum require it.

Using deprecated @AssistantEntity(schema:) / @AssistantEnum(schema:). Use @AppEntity(schema:) and @AppEnum(schema:) instead. Note: @AssistantIntent(schema:) is still active.

Blocking perform(). perform() is async -- use await for I/O.

Review Checklist
 Every AppIntent has a descriptive title (verb + noun, title case)
 @Parameter types are optional or have defaults for system preview
 AppEntity types are shadow models, not core data model conformances
 AppEntity has displayRepresentation and typeDisplayRepresentation
 EntityQuery.entities(for:) omits missing IDs; suggestedEntities() implemented
 AppEnum uses String raw value with caseDisplayRepresentations
 AppShortcutsProvider phrases include \(.applicationName); parameterSummary defined
 IndexedEntity properties use @Property(indexingKey:) on iOS 26+
 Control Center intents conform to ControlConfigurationIntent; widget intents to WidgetConfigurationIntent
 No deprecated @AssistantEntity / @AssistantEnum macros (note: @AssistantIntent(schema:) is still active)
 perform() uses async/await (no blocking); runs in expected isolation context; intent types are Sendable
References
See references/appintents-advanced.md for @Parameter variants, EntityPropertyQuery, assistant schemas, focus filters, SiriKit migration, error handling, confirmation flows, authentication, URL-representable types, and Spotlight indexing details.
Weekly Installs
1.2K
Repository
dpearson2699/sw…s-skills
GitHub Stars
512
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass