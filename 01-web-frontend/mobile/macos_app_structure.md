---
title: macos-app-structure
url: https://skills.sh/makgunay/claude-swift-skills/macos-app-structure
---

# macos-app-structure

skills/makgunay/claude-swift-skills/macos-app-structure
macos-app-structure
Installation
$ npx skills add https://github.com/makgunay/claude-swift-skills --skill macos-app-structure
SKILL.md
macOS App Structure
Critical Constraints
❌ DO NOT use iOS-only scenes (TabView as root scene) → ✅ Use WindowGroup, Window, or NavigationSplitView
❌ DO NOT use UIApplicationDelegate → ✅ Use NSApplicationDelegateAdaptor for AppKit hooks
❌ DO NOT forget Settings scene for Preferences → ✅ macOS apps should have a Settings scene
❌ DO NOT assume single-window → ✅ macOS apps can have multiple windows; design for it
❌ DO NOT use iOS navigation patterns → ✅ Use NavigationSplitView (sidebar + detail) for macOS
Standard macOS App
import SwiftUI

@main
struct MyApp: App {
    @NSApplicationDelegateAdaptor(AppDelegate.self) var appDelegate

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .defaultSize(width: 900, height: 600)

        Settings {
            SettingsView()
        }
    }
}

class AppDelegate: NSObject, NSApplicationDelegate {
    func applicationDidFinishLaunching(_ notification: Notification) {
        // AppKit lifecycle hooks
    }
    func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool {
        return true  // Quit when last window closes
    }
}

Menu Bar App
@main
struct MenuBarApp: App {
    var body: some Scene {
        MenuBarExtra("My App", systemImage: "command") {
            MenuBarView()
        }
        .menuBarExtraStyle(.window)  // Full window popover (not just menu items)

        Settings {
            SettingsView()
        }
    }
}


To hide dock icon, add to Info.plist:

<key>LSUIElement</key>
<true/>

Multiple Named Windows
@main
struct MultiWindowApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }

        Window("Inspector", id: "inspector") {
            InspectorView()
        }
        .defaultSize(width: 300, height: 400)
        .defaultPosition(.trailing)

        Settings {
            SettingsView()
        }
    }
}

// Open a named window from code
@Environment(\.openWindow) private var openWindow
Button("Open Inspector") { openWindow(id: "inspector") }

Content View with Sidebar
struct ContentView: View {
    @State private var selection: SidebarItem? = .library

    var body: some View {
        NavigationSplitView {
            List(selection: $selection) {
                Section("Library") {
                    Label("All Items", systemImage: "square.grid.2x2")
                        .tag(SidebarItem.library)
                    Label("Favorites", systemImage: "heart")
                        .tag(SidebarItem.favorites)
                }
            }
            .navigationSplitViewColumnWidth(min: 180, ideal: 220)
        } detail: {
            switch selection {
            case .library: LibraryView()
            case .favorites: FavoritesView()
            case nil: ContentUnavailableView("Select an item", systemImage: "sidebar.left")
            }
        }
        .navigationTitle("My App")
    }
}

Project Structure Convention
MyApp/
├── MyApp.swift              # @main App struct
├── AppDelegate.swift        # NSApplicationDelegateAdaptor (if needed)
├── Models/                  # SwiftData @Model classes
├── Views/
│   ├── ContentView.swift    # Main navigation structure
│   ├── Components/          # Reusable view components
│   └── Settings/            # Settings/Preferences views
├── ViewModels/              # @Observable view models
├── Services/                # Business logic, networking, persistence
├── Utilities/               # Extensions, helpers
├── Resources/
│   ├── Assets.xcassets
│   └── Localizable.xcstrings
├── Info.plist
└── MyApp.entitlements

Key Info.plist Entries (macOS)
<key>LSUIElement</key>           <!-- true = menu bar only, no dock icon -->
<key>NSAccessibilityUsageDescription</key>  <!-- Required for Accessibility API -->
<key>NSAppleEventsUsageDescription</key>    <!-- Required for AppleScript -->

Key Entitlements
<!-- App Sandbox (required for App Store) -->
<key>com.apple.security.app-sandbox</key><true/>

<!-- Network access -->
<key>com.apple.security.network.client</key><true/>

<!-- File access -->
<key>com.apple.security.files.user-selected.read-write</key><true/>

<!-- iCloud -->
<key>com.apple.developer.icloud-container-identifiers</key>

Common Mistakes & Fixes
Mistake	Fix
No Settings scene	Add Settings { SettingsView() } — expected on macOS
App doesn't quit when last window closes	Implement applicationShouldTerminateAfterLastWindowClosed
Dock icon showing for menu bar app	Add LSUIElement = true to Info.plist
Window too small on macOS	Add .defaultSize(width:height:) to WindowGroup
Using TabView as main navigation	Use NavigationSplitView with sidebar on macOS
References
SwiftUI App Structure
MenuBarExtra
App Sandbox Design Guide
Weekly Installs
29
Repository
makgunay/claude…t-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass