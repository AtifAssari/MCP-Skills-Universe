---
title: swift-charts
url: https://skills.sh/dpearson2699/swift-ios-skills/swift-charts
---

# swift-charts

skills/dpearson2699/swift-ios-skills/swift-charts
swift-charts
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill swift-charts
Summary

Build data visualizations with bar, line, area, point, pie, and donut charts in Swift.

Compose marks (BarMark, LineMark, PointMark, AreaMark, RuleMark, RectangleMark, SectorMark) inside a Chart container and configure axes, scales, and legends with view modifiers
Support for multi-series encoding via .foregroundStyle(by:), symbol and line style variations, and stacked or grouped layouts
Selection, scrolling, and annotation capabilities (iOS 17+); vectorized plots (BarPlot, LinePlot, AreaPlot, PointPlot) for datasets exceeding 1000 points (iOS 18+)
Specialized patterns for heat maps, Gantt charts, sparklines, threshold lines, and function plotting with explicit domain control
Comprehensive review checklist and common-mistake guidance covering data model setup, accessibility, Dynamic Type compatibility, and performance optimization
SKILL.md
Swift Charts

Build data visualizations with Swift Charts targeting iOS 26+. Compose marks inside a Chart container, configure axes and scales with view modifiers, and use vectorized plots for large datasets.

See references/charts-patterns.md for extended patterns, accessibility, and theming guidance.

Contents
Workflow
Chart Container
Mark Types
Axis Customization
Scale Configuration
Foreground Style and Encoding
Selection (iOS 17+)
Scrollable Charts (iOS 17+)
Annotations
Legend
Vectorized Plots (iOS 18+)
Common Mistakes
Review Checklist
References
Workflow
1. Build a new chart
Define data as an Identifiable struct or use id: key path.
Choose mark type(s): BarMark, LineMark, PointMark, AreaMark, RuleMark, RectangleMark, or SectorMark.
Wrap marks in a Chart container.
Encode visual channels: .foregroundStyle(by:), .symbol(by:), .lineStyle(by:).
Configure axes with .chartXAxis / .chartYAxis.
Set scale domains with .chartXScale(domain:) / .chartYScale(domain:).
Add selection, scrolling, or annotations as needed.
For 1000+ data points, use vectorized plots (BarPlot, LinePlot, etc.).
2. Review existing chart code

Run through the Review Checklist at the end of this file.

Chart Container
// Data-driven init (single-series)
Chart(sales) { item in
    BarMark(x: .value("Month", item.month), y: .value("Revenue", item.revenue))
}

// Content closure init (multi-series, mixed marks)
Chart {
    ForEach(seriesA) { item in
        LineMark(x: .value("Date", item.date), y: .value("Value", item.value))
            .foregroundStyle(.blue)
    }
    RuleMark(y: .value("Target", 500))
        .foregroundStyle(.red)
}

// Custom ID key path
Chart(data, id: \.category) { item in
    BarMark(x: .value("Category", item.category), y: .value("Count", item.count))
}

Mark Types
BarMark (iOS 16+)
// Vertical bar
BarMark(x: .value("Month", item.month), y: .value("Sales", item.sales))

// Stacked by category (automatic when same x maps to multiple bars)
BarMark(x: .value("Month", item.month), y: .value("Sales", item.sales))
    .foregroundStyle(by: .value("Product", item.product))

// Horizontal bar
BarMark(x: .value("Sales", item.sales), y: .value("Month", item.month))

// Interval bar (Gantt chart)
BarMark(
    xStart: .value("Start", item.start),
    xEnd: .value("End", item.end),
    y: .value("Task", item.task)
)

LineMark (iOS 16+)
// Single line
LineMark(x: .value("Date", item.date), y: .value("Price", item.price))

// Multi-series via foregroundStyle encoding
LineMark(x: .value("Date", item.date), y: .value("Temp", item.temp))
    .foregroundStyle(by: .value("City", item.city))
    .interpolationMethod(.catmullRom)

// Multi-series with explicit series parameter
LineMark(
    x: .value("Date", item.date),
    y: .value("Price", item.price),
    series: .value("Ticker", item.ticker)
)

PointMark (iOS 16+)
PointMark(x: .value("Height", item.height), y: .value("Weight", item.weight))
    .foregroundStyle(by: .value("Species", item.species))
    .symbol(by: .value("Species", item.species))
    .symbolSize(100)

AreaMark (iOS 16+)
// Stacked area
AreaMark(x: .value("Date", item.date), y: .value("Sales", item.sales))
    .foregroundStyle(by: .value("Category", item.category))

// Range band
AreaMark(
    x: .value("Date", item.date),
    yStart: .value("Min", item.min),
    yEnd: .value("Max", item.max)
)
.opacity(0.3)

RuleMark (iOS 16+)
RuleMark(y: .value("Target", 9000))
    .foregroundStyle(.red)
    .lineStyle(StrokeStyle(dash: [5, 3]))
    .annotation(position: .top, alignment: .leading) {
        Text("Target").font(.caption).foregroundStyle(.red)
    }

RectangleMark (iOS 16+)
RectangleMark(x: .value("Hour", item.hour), y: .value("Day", item.day))
    .foregroundStyle(by: .value("Intensity", item.intensity))

SectorMark (iOS 17+)
// Pie chart
Chart(data, id: \.name) { item in
    SectorMark(angle: .value("Sales", item.sales))
        .foregroundStyle(by: .value("Category", item.name))
}

// Donut chart
Chart(data, id: \.name) { item in
    SectorMark(
        angle: .value("Sales", item.sales),
        innerRadius: .ratio(0.618),
        outerRadius: .inset(10),
        angularInset: 1
    )
    .cornerRadius(4)
    .foregroundStyle(by: .value("Category", item.name))
}

Axis Customization
// Hide axes
.chartXAxis(.hidden)
.chartYAxis(.hidden)

// Custom axis content
.chartXAxis {
    AxisMarks(values: .stride(by: .month)) { value in
        AxisGridLine()
        AxisTick()
        AxisValueLabel(format: .dateTime.month(.abbreviated))
    }
}

// Multiple AxisMarks compositions (different intervals for grid vs. labels)
.chartXAxis {
    AxisMarks(values: .stride(by: .day)) { _ in AxisGridLine() }
    AxisMarks(values: .stride(by: .week)) { _ in
        AxisTick()
        AxisValueLabel(format: .dateTime.week())
    }
}

// Axis labels (titles)
.chartXAxisLabel("Time", position: .bottom, alignment: .center)
.chartYAxisLabel("Revenue ($)", position: .leading, alignment: .center)

Scale Configuration
.chartYScale(domain: 0...100)                          // Explicit numeric domain
.chartYScale(domain: .automatic(includesZero: true))   // Include zero
.chartYScale(domain: 1...10000, type: .log)            // Logarithmic scale
.chartXScale(domain: ["Mon", "Tue", "Wed", "Thu"])     // Categorical ordering

Foreground Style and Encoding
BarMark(...).foregroundStyle(.blue)                                    // Static color
BarMark(...).foregroundStyle(by: .value("Category", item.category))   // Data encoding
AreaMark(...).foregroundStyle(                                         // Gradient
    .linearGradient(colors: [.blue, .cyan], startPoint: .bottom, endPoint: .top)
)

Selection (iOS 17+)
@State private var selectedDate: Date?
@State private var selectedRange: ClosedRange<Date>?
@State private var selectedAngle: String?

// Point selection
Chart(data) { item in
    LineMark(x: .value("Date", item.date), y: .value("Value", item.value))
}
.chartXSelection(value: $selectedDate)

// Range selection
.chartXSelection(range: $selectedRange)

// Angular selection (pie/donut)
.chartAngleSelection(value: $selectedAngle)

Scrollable Charts (iOS 17+)
Chart(dailyData) { item in
    BarMark(x: .value("Date", item.date, unit: .day), y: .value("Steps", item.steps))
}
.chartScrollableAxes(.horizontal)
.chartXVisibleDomain(length: 3600 * 24 * 7) // 7 days visible
.chartScrollPosition(initialX: latestDate)
.chartScrollTargetBehavior(
    .valueAligned(matching: DateComponents(hour: 0), majorAlignment: .page)
)

Annotations
BarMark(x: .value("Month", item.month), y: .value("Sales", item.sales))
    .annotation(position: .top, alignment: .center, spacing: 4) {
        Text("\(item.sales, format: .number)").font(.caption2)
    }

// Overflow resolution
.annotation(
    position: .top,
    overflowResolution: .init(x: .fit(to: .chart), y: .padScale)
) { Text("Label") }

Legend
.chartLegend(.hidden)                                           // Hide
.chartLegend(position: .bottom, alignment: .center, spacing: 10) // Position
.chartLegend(position: .bottom) {                                // Custom
    HStack {
        ForEach(categories, id: \.self) { cat in
            Label(cat, systemImage: "circle.fill").font(.caption)
        }
    }
}

Vectorized Plots (iOS 18+)

Use for large datasets (1000+ points). Accept entire collections or functions.

// Data-driven
Chart {
    BarPlot(sales, x: .value("Month", \.month), y: .value("Revenue", \.revenue))
        .foregroundStyle(\.barColor)
}

// Function plotting: y = f(x)
Chart {
    LinePlot(x: "x", y: "y", domain: -5...5) { x in sin(x) }
}

// Parametric: (x, y) = f(t)
Chart {
    LinePlot(x: "x", y: "y", t: "t", domain: 0...(2 * .pi)) { t in
        (x: cos(t), y: sin(t))
    }
}


Apply KeyPath-based modifiers before simple-value modifiers:

BarPlot(data, x: .value("X", \.x), y: .value("Y", \.y))
    .foregroundStyle(\.color)    // KeyPath first
    .opacity(0.8)                // Value modifier second

Common Mistakes
1. Using ObservableObject instead of @Observable
// WRONG
class ChartModel: ObservableObject {
    @Published var data: [Sale] = []
}
struct ChartView: View {
    @StateObject private var model = ChartModel()
}

// CORRECT
@Observable class ChartModel {
    var data: [Sale] = []
}
struct ChartView: View {
    @State private var model = ChartModel()
}

2. Missing series parameter for multi-line charts
// WRONG -- all points connect into one line
Chart {
    ForEach(allCities) { item in
        LineMark(x: .value("Date", item.date), y: .value("Temp", item.temp))
    }
}

// CORRECT -- separate lines per city
Chart {
    ForEach(allCities) { item in
        LineMark(x: .value("Date", item.date), y: .value("Temp", item.temp))
            .foregroundStyle(by: .value("City", item.city))
    }
}

3. Too many SectorMark slices
// WRONG -- 20 tiny sectors are unreadable
Chart(twentyCategories, id: \.name) { item in
    SectorMark(angle: .value("Value", item.value))
}

// CORRECT -- group into top 5 + "Other"
Chart(groupedData, id: \.name) { item in
    SectorMark(angle: .value("Value", item.value))
        .foregroundStyle(by: .value("Category", item.name))
}

4. Missing scale domain when zero-baseline matters
// WRONG -- axis starts at ~95; small changes look dramatic
Chart(data) {
    LineMark(x: .value("Day", $0.day), y: .value("Score", $0.score))
}

// CORRECT -- explicit domain for honest representation
Chart(data) {
    LineMark(x: .value("Day", $0.day), y: .value("Score", $0.score))
}
.chartYScale(domain: 0...100)

5. Static foregroundStyle overriding data encoding
// WRONG -- static color overrides by-value encoding
BarMark(x: .value("X", item.x), y: .value("Y", item.y))
    .foregroundStyle(by: .value("Category", item.category))
    .foregroundStyle(.blue)

// CORRECT -- use only the data encoding
BarMark(x: .value("X", item.x), y: .value("Y", item.y))
    .foregroundStyle(by: .value("Category", item.category))

6. Individual marks for 10,000+ data points
// WRONG -- creates 10,000 mark views; slow
Chart(largeDataset) { item in
    PointMark(x: .value("X", item.x), y: .value("Y", item.y))
}

// CORRECT -- vectorized plot (iOS 18+)
Chart {
    PointPlot(largeDataset, x: .value("X", \.x), y: .value("Y", \.y))
}

7. Fixed chart height breaking Dynamic Type
// WRONG -- clips axis labels at large text sizes
Chart(data) { ... }
    .frame(height: 200)

// CORRECT -- adaptive sizing
Chart(data) { ... }
    .frame(minHeight: 200, maxHeight: 400)

8. KeyPath modifier after value modifier on vectorized plots
// WRONG -- compiler error
BarPlot(data, x: .value("X", \.x), y: .value("Y", \.y))
    .opacity(0.8)
    .foregroundStyle(\.color)

// CORRECT -- KeyPath modifiers first
BarPlot(data, x: .value("X", \.x), y: .value("Y", \.y))
    .foregroundStyle(\.color)
    .opacity(0.8)

9. Missing accessibility labels
// WRONG -- VoiceOver users get no context
Chart(data) {
    BarMark(x: .value("Month", $0.month), y: .value("Sales", $0.sales))
}

// CORRECT -- add per-mark accessibility
Chart(data) { item in
    BarMark(x: .value("Month", item.month), y: .value("Sales", item.sales))
        .accessibilityLabel("\(item.month)")
        .accessibilityValue("\(item.sales) units sold")
}

Review Checklist
 Data model uses Identifiable or chart uses id: key path
 Model uses @Observable with @State, not ObservableObject
 Mark type matches goal (bar=comparison, line=trend, sector=proportion)
 Multi-series lines use series: parameter or .foregroundStyle(by:)
 Axes configured with appropriate labels, ticks, and grid lines
 Scale domain set explicitly when zero-baseline matters
 Pie/donut limited to 5-7 sectors; small values grouped into "Other"
 Selection binding type matches axis data type (Date? for date axis)
 Scrollable charts set .chartXVisibleDomain(length:) for viewport
 Vectorized plots used for datasets exceeding 1000 points
 KeyPath modifiers applied before value modifiers on vectorized plots
 Accessibility labels added to marks for VoiceOver
 Chart tested with Dynamic Type and Dark Mode
 Legend visible and positioned, or intentionally hidden
 Ensure chart data model types are Sendable; update chart data on @MainActor
References
Extended patterns: references/charts-patterns.md
Apple docs: Swift Charts
Apple docs: Creating a chart using Swift Charts
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