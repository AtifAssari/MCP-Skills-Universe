---
rating: ⭐⭐
title: widgetkit
url: https://skills.sh/dpearson2699/swift-ios-skills/widgetkit
---

# widgetkit

skills/dpearson2699/swift-ios-skills/widgetkit
widgetkit
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill widgetkit
Summary

Build home screen, Lock Screen, Live Activities, Dynamic Island, Control Center, and StandBy widgets for iOS 18+.

Supports static and configurable widgets via TimelineProvider and AppIntentTimelineProvider, with adaptive layouts across system families (small, medium, large) and accessory families (circular, rectangular, inline)
Interactive widgets use AppIntent with Button and Toggle for direct actions; Live Activities display in Dynamic Island with compact, minimal, and expanded regions
Control Center controls (iOS 18+) use ControlWidgetButton and ControlWidgetToggle; Lock Screen widgets render in vibrant or accented modes
Requires App Groups entitlement for shared data, NSSupportsLiveActivities = YES for Live Activities, and push-based timeline reloads via WidgetPushHandler (iOS 26+)
Liquid Glass rendering modes and CarPlay widget support added in iOS 26
SKILL.md
WidgetKit and ActivityKit

Build home screen widgets, Lock Screen widgets, Live Activities, Dynamic Island presentations, Control Center controls, and StandBy surfaces for iOS 26+.

See references/widgetkit-advanced.md for timeline strategies, push-based updates, Xcode setup, and advanced patterns.

Contents
Workflow
Widget Protocol and WidgetBundle
Configuration Types
TimelineProvider
AppIntentTimelineProvider
Widget Families
Interactive Widgets (iOS 17+)
Live Activities and Dynamic Island
Control Center Widgets (iOS 18+)
Lock Screen Widgets
StandBy Mode
Design Patterns
iOS 26 Additions
Common Mistakes
Review Checklist
References
Workflow
1. Create a new widget
Add a Widget Extension target in Xcode (File > New > Target > Widget Extension).
Enable App Groups for shared data between the app and widget extension.
Define a TimelineEntry struct with a date property and display data.
Implement a TimelineProvider (static) or AppIntentTimelineProvider (configurable).
Build the widget view using SwiftUI, adapting layout per WidgetFamily.
Declare the Widget conforming struct with a configuration and supported families.
Register all widgets in a WidgetBundle annotated with @main.
2. Add a Live Activity
Define an ActivityAttributes struct with a nested ContentState.
Add NSSupportsLiveActivities = YES to the app's Info.plist.
Create an ActivityConfiguration in the widget bundle with Lock Screen content and Dynamic Island closures.
Start the activity with Activity.request(attributes:content:pushType:).
Update with activity.update(_:) and end with activity.end(_:dismissalPolicy:).
3. Add a Control Center control
Define an AppIntent for the action.
Create a ControlWidgetButton or ControlWidgetToggle in the widget bundle.
Use StaticControlConfiguration or AppIntentControlConfiguration.
4. Review existing widget code

Run through the Review Checklist at the end of this document.

Widget Protocol and WidgetBundle
Widget

Every widget conforms to the Widget protocol and returns a WidgetConfiguration from its body.

struct OrderStatusWidget: Widget {
    let kind: String = "OrderStatusWidget"

    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: OrderProvider()) { entry in
            OrderWidgetView(entry: entry)
        }
        .configurationDisplayName("Order Status")
        .description("Track your current order.")
        .supportedFamilies([.systemSmall, .systemMedium])
    }
}

WidgetBundle

Use WidgetBundle to expose multiple widgets from a single extension.

@main
struct MyAppWidgets: WidgetBundle {
    var body: some Widget {
        OrderStatusWidget()
        FavoritesWidget()
        DeliveryActivityWidget()   // Live Activity
        QuickActionControl()       // Control Center
    }
}

Configuration Types

Use StaticConfiguration for non-configurable widgets. Use AppIntentConfiguration (recommended) for configurable widgets paired with AppIntentTimelineProvider.

// Static
StaticConfiguration(kind: "MyWidget", provider: MyProvider()) { entry in
    MyWidgetView(entry: entry)
}
// Configurable
AppIntentConfiguration(kind: "ConfigWidget", intent: SelectCategoryIntent.self,
                       provider: CategoryProvider()) { entry in
    CategoryWidgetView(entry: entry)
}

Shared Modifiers
Modifier	Purpose
.configurationDisplayName(_:)	Name shown in the widget gallery
.description(_:)	Description shown in the widget gallery
.supportedFamilies(_:)	Array of WidgetFamily values
.supplementalActivityFamilies(_:)	Live Activity sizes (.small, .medium)
TimelineProvider

For static (non-configurable) widgets. Uses completion handlers. Three required methods:

struct WeatherProvider: TimelineProvider {
    typealias Entry = WeatherEntry

    func placeholder(in context: Context) -> WeatherEntry {
        WeatherEntry(date: .now, temperature: 72, condition: "Sunny")
    }

    func getSnapshot(in context: Context, completion: @escaping (WeatherEntry) -> Void) {
        let entry = context.isPreview
            ? placeholder(in: context)
            : WeatherEntry(date: .now, temperature: currentTemp, condition: currentCondition)
        completion(entry)
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<WeatherEntry>) -> Void) {
        Task {
            let weather = await WeatherService.shared.fetch()
            let entry = WeatherEntry(date: .now, temperature: weather.temp, condition: weather.condition)
            let nextUpdate = Calendar.current.date(byAdding: .hour, value: 1, to: .now)!
            completion(Timeline(entries: [entry], policy: .after(nextUpdate)))
        }
    }
}

AppIntentTimelineProvider

For configurable widgets. Uses async/await natively. Receives user intent configuration.

struct CategoryProvider: AppIntentTimelineProvider {
    typealias Entry = CategoryEntry
    typealias Intent = SelectCategoryIntent

    func placeholder(in context: Context) -> CategoryEntry {
        CategoryEntry(date: .now, categoryName: "Sample", items: [])
    }

    func snapshot(for config: SelectCategoryIntent, in context: Context) async -> CategoryEntry {
        let items = await DataStore.shared.items(for: config.category)
        return CategoryEntry(date: .now, categoryName: config.category.name, items: items)
    }

    func timeline(for config: SelectCategoryIntent, in context: Context) async -> Timeline<CategoryEntry> {
        let items = await DataStore.shared.items(for: config.category)
        let entry = CategoryEntry(date: .now, categoryName: config.category.name, items: items)
        return Timeline(entries: [entry], policy: .atEnd)
    }
}

Widget Families
Family	Platform
.systemSmall	iOS, iPadOS, macOS, CarPlay (iOS 26+)
.systemMedium	iOS, iPadOS, macOS
.systemLarge	iOS, iPadOS, macOS
.systemExtraLarge	iPadOS only
.accessoryCircular	iOS, watchOS
.accessoryRectangular	iOS, watchOS
.accessoryInline	iOS, watchOS
.accessoryCorner	watchOS only

Adapt layout per family using @Environment(\.widgetFamily):

@Environment(\.widgetFamily) var family

var body: some View {
    switch family {
    case .systemSmall: CompactView(entry: entry)
    case .systemMedium: DetailedView(entry: entry)
    case .accessoryCircular: CircularView(entry: entry)
    default: FullView(entry: entry)
    }
}

Interactive Widgets (iOS 17+)

Use Button and Toggle with AppIntent conforming types to perform actions directly from a widget without launching the app.

struct ToggleFavoriteIntent: AppIntent {
    static var title: LocalizedStringResource = "Toggle Favorite"
    @Parameter(title: "Item ID") var itemID: String

    func perform() async throws -> some IntentResult {
        await DataStore.shared.toggleFavorite(itemID)
        return .result()
    }
}

struct InteractiveWidgetView: View {
    let entry: FavoriteEntry
    var body: some View {
        HStack {
            Text(entry.itemName)
            Spacer()
            Button(intent: ToggleFavoriteIntent(itemID: entry.itemID)) {
                Image(systemName: entry.isFavorite ? "star.fill" : "star")
            }
        }
        .padding()
    }
}

Live Activities and Dynamic Island
ActivityAttributes

Define the static and dynamic data model.

struct DeliveryAttributes: ActivityAttributes {
    struct ContentState: Codable, Hashable {
        var driverName: String
        var estimatedDeliveryTime: ClosedRange<Date>
        var currentStep: DeliveryStep
    }

    var orderNumber: Int
    var restaurantName: String
}

ActivityConfiguration

Provide Lock Screen content and Dynamic Island closures in the widget bundle.

struct DeliveryActivityWidget: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: DeliveryAttributes.self) { context in
            VStack(alignment: .leading) {
                Text(context.attributes.restaurantName).font(.headline)
                HStack {
                    Text("Driver: \(context.state.driverName)")
                    Spacer()
                    Text(timerInterval: context.state.estimatedDeliveryTime, countsDown: true)
                }
            }
            .padding()
        } dynamicIsland: { context in
            DynamicIsland {
                DynamicIslandExpandedRegion(.leading) {
                    Image(systemName: "box.truck.fill").font(.title2)
                }
                DynamicIslandExpandedRegion(.trailing) {
                    Text(timerInterval: context.state.estimatedDeliveryTime, countsDown: true)
                        .font(.caption)
                }
                DynamicIslandExpandedRegion(.center) {
                    Text(context.attributes.restaurantName).font(.headline)
                }
                DynamicIslandExpandedRegion(.bottom) {
                    HStack {
                        ForEach(DeliveryStep.allCases, id: \.self) { step in
                            Image(systemName: step.icon)
                                .foregroundStyle(step <= context.state.currentStep ? .primary : .tertiary)
                        }
                    }
                }
            } compactLeading: {
                Image(systemName: "box.truck.fill")
            } compactTrailing: {
                Text(timerInterval: context.state.estimatedDeliveryTime, countsDown: true)
                    .frame(width: 40).monospacedDigit()
            } minimal: {
                Image(systemName: "box.truck.fill")
            }
        }
    }
}

Dynamic Island Regions
Region	Position
.leading	Left of the TrueDepth camera; wraps below
.trailing	Right of the TrueDepth camera; wraps below
.center	Directly below the camera
.bottom	Below all other regions
Starting, Updating, and Ending
let attributes = DeliveryAttributes(orderNumber: 123, restaurantName: "Pizza Place")
let state = DeliveryAttributes.ContentState(
    driverName: "Alex",
    estimatedDeliveryTime: Date()...Date().addingTimeInterval(1800),
    currentStep: .preparing
)
let content = ActivityContent(state: state, staleDate: nil, relevanceScore: 75)
let activity = try Activity.request(attributes: attributes, content: content, pushType: .token)

let updated = ActivityContent(state: newState, staleDate: nil, relevanceScore: 90)
await activity.update(updated)

let final = ActivityContent(state: finalState, staleDate: nil, relevanceScore: 0)
await activity.end(final, dismissalPolicy: .after(.now.addingTimeInterval(3600)))

Control Center Widgets (iOS 18+)
// Button control
struct OpenCameraControl: ControlWidget {
    var body: some ControlWidgetConfiguration {
        StaticControlConfiguration(kind: "OpenCamera") {
            ControlWidgetButton(action: OpenCameraIntent()) {
                Label("Camera", systemImage: "camera.fill")
            }
        }
        .displayName("Open Camera")
    }
}

// Toggle control with value provider
struct FlashlightControl: ControlWidget {
    var body: some ControlWidgetConfiguration {
        StaticControlConfiguration(kind: "Flashlight", provider: FlashlightValueProvider()) { value in
            ControlWidgetToggle(isOn: value, action: ToggleFlashlightIntent()) {
                Label("Flashlight", systemImage: value ? "flashlight.on.fill" : "flashlight.off.fill")
            }
        }
        .displayName("Flashlight")
    }
}

Lock Screen Widgets

Use accessory families and AccessoryWidgetBackground.

struct StepsWidget: Widget {
    let kind = "StepsWidget"
    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: StepsProvider()) { entry in
            ZStack {
                AccessoryWidgetBackground()
                VStack {
                    Image(systemName: "figure.walk")
                    Text("\(entry.stepCount)").font(.headline)
                }
            }
        }
        .supportedFamilies([.accessoryCircular, .accessoryRectangular, .accessoryInline])
    }
}

StandBy Mode

.systemSmall widgets automatically appear in StandBy (iPhone on charger in landscape). Use @Environment(\.widgetLocation) for conditional rendering:

@Environment(\.widgetLocation) var location
// location == .standBy, .homeScreen, .lockScreen, .carPlay, etc.

Design Patterns
Prefer Gauge over manual arcs. Use .gaugeStyle(.accessoryCircular) for Lock Screen circular widgets and .linearCapacity for home screen capacity bars. The system handles styling, accessibility, and rendering-mode adaptation.
Use .containerBackground(_:for: .widget) (iOS 17+) for widget backgrounds instead of padding and background modifiers.
Use Canvas for dense visualizations like sparklines or mini bar charts. The lack of per-element accessibility is acceptable since the entire widget surface is a single tap target.
Match timeline refresh to data granularity. Apple budgets 40–70 refreshes per day with entries at least 5 minutes apart. Use Text(timerInterval:countsDown:) for live countdowns instead of burning timeline entries.

See references/widgetkit-advanced.md for code examples and detailed guidance on each pattern.

iOS 26 Additions
Liquid Glass Support

Adapt widgets to the Liquid Glass visual style using WidgetAccentedRenderingMode.

Mode	Description
.accented	Accented rendering for Liquid Glass
.accentedDesaturated	Accented with desaturation
.desaturated	Fully desaturated
.fullColor	Full-color rendering
WidgetPushHandler

Enable push-based timeline reloads without scheduled polling.

struct MyWidgetPushHandler: WidgetPushHandler {
    func pushTokenDidChange(_ pushInfo: WidgetPushInfo, widgets: [WidgetInfo]) {
        let tokenString = pushInfo.token.map { String(format: "%02x", $0) }.joined()
        // Send tokenString to your server
    }
}

CarPlay Widgets

.systemSmall widgets render in CarPlay on iOS 26+. Ensure small widget layouts are legible at a glance for driver safety.

Common Mistakes

Using IntentTimelineProvider instead of AppIntentTimelineProvider. IntentTimelineProvider is the older SiriKit Intents-based provider. Prefer AppIntentTimelineProvider with the App Intents framework for new widgets.

Exceeding the refresh budget. Widgets have a daily refresh limit. Do not call WidgetCenter.shared.reloadTimelines(ofKind:) on every minor data change. Batch updates and use appropriate TimelineReloadPolicy values.

Forgetting App Groups for shared data. The widget extension runs in a separate process. Use UserDefaults(suiteName:) or a shared App Group container for data the widget reads.

Performing network calls in placeholder(). placeholder(in:) must return synchronously with sample data. Use getTimeline or timeline(for:in:) for async work.

Missing NSSupportsLiveActivities Info.plist key. Live Activities will not start without NSSupportsLiveActivities = YES in the host app's Info.plist.

Using the deprecated contentState API. Use ActivityContent for all Activity.request, update, and end calls. The contentState-based methods are deprecated.

Not handling the stale state. Check context.isStale in Live Activity views and show a fallback (e.g., "Updating...") when content is outdated.

Putting heavy logic in the widget view. Widget views are rendered in a size-limited process. Pre-compute data in the timeline provider and pass display-ready values through the entry.

Ignoring accessory rendering modes. Lock Screen widgets render in .vibrant or .accented mode, not .fullColor. Test with @Environment(\.widgetRenderingMode) and avoid relying on color alone.

Not testing on device. Dynamic Island and StandBy behavior differ significantly from Simulator. Always verify on physical hardware.

Review Checklist
 Widget extension target has App Groups entitlement matching the main app
 @main is on the WidgetBundle, not on individual widgets
 placeholder(in:) returns synchronously; getSnapshot/snapshot(for:in:) fast when isPreview
 Timeline reload policy matches update frequency; reloadTimelines(ofKind:) only on data change
 Layout adapts per WidgetFamily; accessory widgets tested in .vibrant mode
 Interactive widgets use AppIntent with Button/Toggle only
 Live Activity: NSSupportsLiveActivities = YES; ActivityContent used; Dynamic Island closures implemented
 activity.end(_:dismissalPolicy:) called; controls use StaticControlConfiguration/AppIntentControlConfiguration
 Timeline entries and Intent types are Sendable; tested on device
References
Advanced guide: references/widgetkit-advanced.md
Apple docs: WidgetKit | ActivityKit | Keeping a widget up to date
Weekly Installs
1.2K
Repository
dpearson2699/sw…s-skills
GitHub Stars
512
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass