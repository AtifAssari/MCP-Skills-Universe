---
rating: ⭐⭐
title: axiom-swiftui-containers-ref
url: https://skills.sh/charleswiltgen/axiom/axiom-swiftui-containers-ref
---

# axiom-swiftui-containers-ref

skills/charleswiltgen/axiom/axiom-swiftui-containers-ref
axiom-swiftui-containers-ref
Installation
$ npx skills add https://github.com/charleswiltgen/axiom --skill axiom-swiftui-containers-ref
SKILL.md
SwiftUI Containers Reference

Stacks, grids, outlines, and scroll enhancements. iOS 14 through iOS 26.

Sources: WWDC 2020-10031, 2022-10056, 2023-10148, 2024-10144, 2025-256

Quick Decision
Use Case	Container	iOS
Fixed views vertical/horizontal	VStack / HStack	13+
Overlapping views	ZStack	13+
Large scrollable list	LazyVStack / LazyHStack	14+
Multi-column grid	LazyVGrid	14+
Multi-row grid (horizontal)	LazyHGrid	14+
Static grid, precise alignment	Grid	16+
Hierarchical data (tree)	List with children:	14+
Custom hierarchies	OutlineGroup	14+
Show/hide content	DisclosureGroup	14+
Part 1: Stacks
VStack, HStack, ZStack
VStack(alignment: .leading, spacing: 12) {
    Text("Title")
    Text("Subtitle")
}

HStack(alignment: .top, spacing: 8) {
    Image(systemName: "star")
    Text("Rating")
}

ZStack(alignment: .bottomTrailing) {
    Image("photo")
    Badge()
}


ZStack alignments: .center (default), .top, .bottom, .leading, .trailing, .topLeading, .topTrailing, .bottomLeading, .bottomTrailing

Spacer
HStack {
    Text("Left")
    Spacer()
    Text("Right")
}

Spacer(minLength: 20)  // Minimum size

LazyVStack, LazyHStack (iOS 14+)

Render children only when visible. Use inside ScrollView.

ScrollView {
    LazyVStack(spacing: 0) {
        ForEach(items) { item in
            ItemRow(item: item)
        }
    }
}

Pinned Section Headers
ScrollView {
    LazyVStack(pinnedViews: [.sectionHeaders]) {
        ForEach(sections) { section in
            Section(header: SectionHeader(section)) {
                ForEach(section.items) { item in
                    ItemRow(item: item)
                }
            }
        }
    }
}

Part 2: Grids
Grid (iOS 16+)

Non-lazy grid with precise alignment. Loads all views at once.

Grid(alignment: .leading, horizontalSpacing: 10, verticalSpacing: 10) {
    GridRow {
        Text("Name")
        TextField("Enter name", text: $name)
    }
    GridRow {
        Text("Email")
        TextField("Enter email", text: $email)
    }
}


Modifiers:

gridCellColumns(_:) — Span multiple columns
gridColumnAlignment(_:) — Override column alignment
Grid {
    GridRow {
        Text("Header").gridCellColumns(2)
    }
    GridRow {
        Text("Left")
        Text("Right").gridColumnAlignment(.trailing)
    }
}

LazyVGrid (iOS 14+)

Vertical-scrolling grid. Define columns; rows grow unbounded.

let columns = [
    GridItem(.flexible()),
    GridItem(.flexible()),
    GridItem(.flexible())
]

ScrollView {
    LazyVGrid(columns: columns, spacing: 16) {
        ForEach(items) { item in
            ItemCard(item: item)
        }
    }
}

LazyHGrid (iOS 14+)

Horizontal-scrolling grid. Define rows; columns grow unbounded.

let rows = [GridItem(.fixed(100)), GridItem(.fixed(100))]

ScrollView(.horizontal) {
    LazyHGrid(rows: rows, spacing: 16) {
        ForEach(items) { item in
            ItemCard(item: item)
        }
    }
}

GridItem.Size
Size	Behavior
.fixed(CGFloat)	Exact width/height
.flexible(minimum:maximum:)	Fills space equally
.adaptive(minimum:maximum:)	Creates as many as fit
// Adaptive: responsive column count
let columns = [GridItem(.adaptive(minimum: 150))]

Part 3: Outlines
List with Hierarchical Data (iOS 14+)
struct FileItem: Identifiable {
    let id = UUID()
    var name: String
    var children: [FileItem]?  // nil = leaf
}

List(files, children: \.children) { file in
    Label(file.name, systemImage: file.children != nil ? "folder" : "doc")
}
.listStyle(.sidebar)

OutlineGroup (iOS 14+)

For custom hierarchical layouts outside List.

List {
    ForEach(canvases) { canvas in
        Section(header: Text(canvas.name)) {
            OutlineGroup(canvas.graphics, children: \.children) { graphic in
                GraphicRow(graphic: graphic)
            }
        }
    }
}

DisclosureGroup (iOS 14+)
@State private var isExpanded = false

DisclosureGroup("Advanced Options", isExpanded: $isExpanded) {
    Toggle("Enable Feature", isOn: $feature)
    Slider(value: $intensity)
}

Part 4: Common Patterns
Photo Grid
let columns = [GridItem(.adaptive(minimum: 100), spacing: 2)]

ScrollView {
    LazyVGrid(columns: columns, spacing: 2) {
        ForEach(photos) { photo in
            AsyncImage(url: photo.thumbnailURL) { image in
                image.resizable().aspectRatio(1, contentMode: .fill)
            } placeholder: { Color.gray }
            .aspectRatio(1, contentMode: .fill)
            .clipped()
        }
    }
}

Horizontal Carousel
ScrollView(.horizontal, showsIndicators: false) {
    LazyHStack(spacing: 16) {
        ForEach(items) { item in
            CarouselCard(item: item).frame(width: 280)
        }
    }
    .padding(.horizontal)
}

File Browser
List(selection: $selection) {
    OutlineGroup(rootItems, children: \.children) { item in
        Label {
            Text(item.name)
        } icon: {
            Image(systemName: item.children != nil ? "folder.fill" : "doc.fill")
        }
    }
}
.listStyle(.sidebar)

Part 5: Performance
When to Use Lazy
Size	Scrollable?	Use
1-20	No	VStack/HStack
1-20	Yes	VStack/HStack in ScrollView
20-100	Yes	LazyVStack/LazyHStack
100+	Yes	LazyVStack/LazyHStack or List
Grid <50	No	Grid
Grid 50+	Yes	LazyVGrid/LazyHGrid

Cache GridItem arrays — define outside body:

struct ContentView: View {
    let columns = [GridItem(.adaptive(minimum: 150))]  // ✅
    var body: some View {
        LazyVGrid(columns: columns) { ... }
    }
}

iOS 26 Performance
6x faster list loading for 100k+ items
16x faster list updates
Reduced dropped frames in scrolling
Nested ScrollViews with lazy stacks now properly defer loading:
ScrollView(.horizontal) {
    LazyHStack {
        ForEach(photoSets) { set in
            ScrollView(.vertical) {
                LazyVStack {
                    ForEach(set.photos) { PhotoView(photo: $0) }
                }
            }
        }
    }
}

Part 6: Scroll Enhancements
containerRelativeFrame (iOS 17+)

Size views relative to scroll container.

ScrollView(.horizontal) {
    LazyHStack {
        ForEach(cards) { card in
            CardView(card: card)
                .containerRelativeFrame(.horizontal, count: 3, span: 1, spacing: 16)
        }
    }
}

scrollTargetLayout (iOS 17+)

Enable snapping.

ScrollView(.horizontal) {
    LazyHStack {
        ForEach(items) { ItemCard(item: $0) }
    }
    .scrollTargetLayout()
}
.scrollTargetBehavior(.viewAligned)

scrollPosition (iOS 17+)

Track topmost visible item. Requires .id() on each item.

@State private var position: Item.ID?

ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemRow(item: item).id(item.id)
        }
    }
}
.scrollPosition(id: $position)

scrollTransition (iOS 17+)
.scrollTransition { content, phase in
    content
        .opacity(1 - abs(phase.value) * 0.5)
        .scaleEffect(phase.isIdentity ? 1.0 : 0.75)
}

onScrollGeometryChange (iOS 18+)
.onScrollGeometryChange(for: Bool.self) { geo in
    geo.contentOffset.y < geo.contentInsets.top
} action: { _, isTop in
    showBackButton = !isTop
}

onScrollVisibilityChange (iOS 18+)
VideoPlayer(player: player)
    .onScrollVisibilityChange(threshold: 0.2) { visible in
        visible ? player.play() : player.pause()
    }

Resources

WWDC: 2020-10031, 2022-10056, 2023-10148, 2024-10144, 2025-256

Docs: /swiftui/lazyvstack, /swiftui/lazyvgrid, /swiftui/lazyhgrid, /swiftui/grid, /swiftui/outlinegroup, /swiftui/disclosuregroup

Skills: axiom-swiftui-layout, axiom-swiftui-layout-ref, axiom-swiftui-nav, axiom-swiftui-26-ref

Weekly Installs
193
Repository
charleswiltgen/axiom
GitHub Stars
881
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass