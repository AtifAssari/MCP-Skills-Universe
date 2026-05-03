---
title: xcuitest
url: https://skills.sh/vabole/apple-skills/xcuitest
---

# xcuitest

skills/vabole/apple-skills/xcuitest
xcuitest
Installation
$ npx skills add https://github.com/vabole/apple-skills --skill xcuitest
SKILL.md
XCUITest Reference

Comprehensive reference for writing reliable XCUITest UI tests in Swift 6.

Quick Reference
// Basic test structure
@MainActor
final class MyUITests: XCTestCase {
    var app: XCUIApplication!

    override func setUp() {
        super.setUp()
        continueAfterFailure = false
        app = XCUIApplication()
        app.launch()
    }

    func testExample() {
        let button = app.buttons["Submit"]
        XCTAssertTrue(button.waitForExistence(timeout: 5))
        button.tap()
    }
}

Core API Classes
XCUIApplication

Proxy for launching, monitoring, and terminating the app under test.

let app = XCUIApplication()

// Launch configuration
app.launchArguments = ["-UITest", "-DisableAnimations"]
app.launchEnvironment["API_URL"] = "https://test.example.com"

// Lifecycle
app.launch()      // Start the app
app.terminate()   // Stop the app
app.activate()    // Bring to foreground

// State checking
app.state == .runningForeground
app.state == .runningBackground
app.state == .notRunning

XCUIElement

Represents a single UI element. Supports interactions and property queries.

let element = app.buttons["Submit"]

// Properties
element.exists           // Bool - element is in hierarchy
element.isHittable       // Bool - element can receive taps
element.isEnabled        // Bool - element is enabled
element.isSelected       // Bool - element is selected
element.label            // String - accessibility label
element.value            // Any? - current value
element.identifier       // String - accessibility identifier
element.frame            // CGRect - frame in screen coordinates
element.elementType      // XCUIElement.ElementType

XCUIElementQuery

Defines search criteria for finding UI elements.

// Type-based queries (convenience)
app.buttons              // All buttons
app.staticTexts          // All text labels
app.textFields           // All text inputs
app.secureTextFields     // Password fields
app.switches             // Toggle switches
app.sliders              // Slider controls
app.tables               // Table views
app.cells                // Table/collection cells
app.scrollViews          // Scroll views
app.images               // Image views
app.alerts               // Alert dialogs
app.sheets               // Action sheets
app.navigationBars       // Navigation bars
app.tabBars              // Tab bars
app.toolbars             // Toolbars

// Querying by identifier (subscript)
app.buttons["Submit"]
app.staticTexts["Welcome"]

// Descendants query (any element type)
app.descendants(matching: .any)
app.descendants(matching: .button)
app.descendants(matching: .staticText)

// Chained queries
app.descendants(matching: .any).matching(identifier: "my-id").firstMatch

// Predicate queries
app.buttons.matching(NSPredicate(format: "label CONTAINS[c] 'Save'"))
app.buttons.matching(NSPredicate(format: "identifier == 'submit-btn'"))
app.staticTexts.matching(NSPredicate(format: "label BEGINSWITH 'Error'"))

// Query results
query.count              // Number of matches
query.element            // Single element (fails if not exactly 1)
query.firstMatch         // First matching element
query.element(boundBy: 0) // Element at index
query.allElementsBoundByIndex  // Array of all elements

XCUICoordinate

Represents a screen location for coordinate-based interactions.

// Normalized offset (0,0 = top-left, 1,1 = bottom-right)
let center = element.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0.5))
let topLeft = element.coordinate(withNormalizedOffset: CGVector(dx: 0, dy: 0))

// Absolute offset from normalized point
let point = app.coordinate(withNormalizedOffset: .zero)
    .withOffset(CGVector(dx: 100, dy: 200))

// Screen coordinates
let screenCenter = app.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0.5))

Element Interactions
Tap Actions
element.tap()                    // Single tap
element.doubleTap()              // Double tap
element.twoFingerTap()           // Two finger tap (iOS only)
element.tap(withNumberOfTaps: 3, numberOfTouches: 1) // Triple tap

Press Actions
element.press(forDuration: 1.0)  // Long press
element.press(forDuration: 0.5, thenDragTo: otherElement) // Press and drag

Text Input
textField.tap()                  // Focus first
textField.typeText("Hello")      // Type text
textField.clearAndEnterText("New text") // Custom helper needed

// Clear text field
textField.tap()
textField.press(forDuration: 1.0)
app.menuItems["Select All"].tap()
textField.typeText("")           // Or use delete key

Swipe Gestures
element.swipeUp()
element.swipeDown()
element.swipeLeft()
element.swipeRight()

// With velocity (iOS 16+)
element.swipeUp(velocity: .fast)
element.swipeUp(velocity: .slow)

Coordinate-Based Gestures
// Pull to refresh
let start = cell.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0))
let end = cell.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 6))
start.press(forDuration: 0, thenDragTo: end)

// Custom swipe
let from = app.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0.8))
let to = app.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0.2))
from.press(forDuration: 0.1, thenDragTo: to)

// Tap at specific point
let point = app.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0.5))
point.tap()

Other Gestures
element.pinch(withScale: 0.5, velocity: -1)  // Pinch in
element.pinch(withScale: 2.0, velocity: 1)   // Pinch out
element.rotate(0.5, withVelocity: 1)         // Rotate

// Sliders
slider.adjust(toNormalizedSliderPosition: 0.7)

// Pickers
picker.adjust(toPickerWheelValue: "Option 3")

Waiting Mechanisms
waitForExistence (Simplest)
// Returns Bool - does not fail test automatically
let exists = element.waitForExistence(timeout: 5)
XCTAssertTrue(exists, "Element did not appear")

// Common pattern
if button.waitForExistence(timeout: 3) {
    button.tap()
}

XCTWaiter (More Control)
// Wait with result handling
let predicate = NSPredicate(format: "exists == true")
let expectation = XCTNSPredicateExpectation(predicate: predicate, object: element)
let result = XCTWaiter().wait(for: [expectation], timeout: 5)

switch result {
case .completed:
    // Element found
case .timedOut:
    XCTFail("Element did not appear within timeout")
case .incorrectOrder:
    // Multiple expectations fulfilled out of order
case .invertedFulfillment:
    // Inverted expectation was fulfilled (unexpected)
case .interrupted:
    // Wait was interrupted
@unknown default:
    break
}

Wait for Non-Existence (Xcode 16+)
// Native API (Xcode 16+) - preferred
let loadingIndicator = app.activityIndicators["loading"]
XCTAssertTrue(loadingIndicator.waitForNonExistence(withTimeout: 10), "Loading should complete")

// Legacy approach (pre-Xcode 16)
func waitForNonExistence(_ element: XCUIElement, timeout: TimeInterval) -> Bool {
    let predicate = NSPredicate(format: "exists == false")
    let expectation = XCTNSPredicateExpectation(predicate: predicate, object: element)
    let result = XCTWaiter().wait(for: [expectation], timeout: timeout)
    return result == .completed
}

Wait for Property Change
// Wait for element to become enabled
let predicate = NSPredicate(format: "isEnabled == true")
let expectation = XCTNSPredicateExpectation(predicate: predicate, object: button)
XCTWaiter().wait(for: [expectation], timeout: 5)

// Wait for label to change
let predicate = NSPredicate(format: "label == 'Done'")
let expectation = XCTNSPredicateExpectation(predicate: predicate, object: statusLabel)
XCTWaiter().wait(for: [expectation], timeout: 10)

Multiple Expectations
let exp1 = XCTNSPredicateExpectation(predicate: pred1, object: element1)
let exp2 = XCTNSPredicateExpectation(predicate: pred2, object: element2)
XCTWaiter().wait(for: [exp1, exp2], timeout: 10, enforceOrder: false)

Wait for Property Value (Xcode 26+ / iOS 26+)
// New KeyPath-based waiting - wait for any property to equal a value
let favoriteButton = app.buttons["Favorite"]
favoriteButton.tap()

// Wait for value property to become true
XCTAssertTrue(
    favoriteButton.wait(for: \.value, toEqual: true, timeout: 10),
    "Button should show favorited state"
)

// Wait for label to change
XCTAssertTrue(
    statusLabel.wait(for: \.label, toEqual: "Complete", timeout: 5),
    "Status should update to Complete"
)

// Wait for element to become enabled
XCTAssertTrue(
    submitButton.wait(for: \.isEnabled, toEqual: true, timeout: 3),
    "Submit button should become enabled"
)


Note: The wait(for:toEqual:timeout:) method uses Swift KeyPaths for type-safe property access. It returns true if the property matches the expected value within the timeout, false otherwise.

Permission Handling
Reset Authorization Status

Reset permissions before tests to ensure consistent state. Call before app.launch().

override func setUp() {
    super.setUp()
    let app = XCUIApplication()

    // Reset permissions before launch
    app.resetAuthorizationStatus(for: .location)
    app.resetAuthorizationStatus(for: .camera)
    app.resetAuthorizationStatus(for: .photos)
    app.resetAuthorizationStatus(for: .health)

    app.launch()
}

XCUIProtectedResource Types
// Available protected resources
.contacts          // Contacts access
.calendar          // Calendar access
.reminders         // Reminders access
.photos            // Photo library access
.microphone        // Microphone access
.camera            // Camera access
.mediaLibrary      // Media library access
.homeKit           // HomeKit access
.bluetooth         // Bluetooth access
.keyboardNetwork   // Network keyboard access
.location          // Location services
.health            // HealthKit access

Handling HealthKit Permission Dialog (iOS 26)

HealthKit authorization on iOS 26 uses a scrollable sheet with buttons below the fold:

func handleHealthKitDialog(allow: Bool = false) {
    let healthAccessText = app.staticTexts["Health Access"]

    if healthAccessText.waitForExistence(timeout: 5) {
        // Scroll down to reveal buttons (iOS 26 sheet is scrollable)
        let from = app.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0.8))
        let to = app.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0.3))
        from.press(forDuration: 0.1, thenDragTo: to)

        // Tap the appropriate button
        let buttonLabel = allow ? "Allow" : "Don't Allow"
        let button = app.buttons[buttonLabel]
        if button.waitForExistence(timeout: 5) {
            button.tap()
        } else {
            // Fallback: find by partial match
            let fallback = app.buttons.matching(
                NSPredicate(format: "label CONTAINS[c] '\(buttonLabel)'")
            ).firstMatch
            if fallback.exists { fallback.tap() }
        }
    }
}

Using UI Interruption Monitor

For handling unexpected permission dialogs during tests:

override func setUp() {
    super.setUp()

    // Handle location permission
    addUIInterruptionMonitor(withDescription: "Location Permission") { alert -> Bool in
        if alert.buttons["Allow While Using App"].exists {
            alert.buttons["Allow While Using App"].tap()
            return true
        }
        if alert.buttons["Don't Allow"].exists {
            alert.buttons["Don't Allow"].tap()
            return true
        }
        return false
    }

    // Handle HealthKit permission
    addUIInterruptionMonitor(withDescription: "Health Permission") { alert -> Bool in
        // Note: HealthKit uses a sheet, not a system alert
        // This may not trigger the interruption monitor
        return false
    }

    app.launch()
}

func testWithPermissions() {
    // Trigger action that shows permission dialog
    app.buttons["Enable Location"].tap()

    // IMPORTANT: Must interact with app to trigger the monitor
    app.tap()

    // Continue test...
}

Springboard Alert Handling

For system-level alerts not caught by interruption monitor:

func handleSpringboardAlert(buttonLabel: String) {
    let springboard = XCUIApplication(bundleIdentifier: "com.apple.springboard")
    let alertButton = springboard.buttons[buttonLabel]

    if alertButton.waitForExistence(timeout: 3) {
        alertButton.tap()
    }
}

// Usage
handleSpringboardAlert(buttonLabel: "Allow")
handleSpringboardAlert(buttonLabel: "Don't Allow")

Swift 6 Concurrency
The Problem

Swift 6 strict concurrency requires proper actor isolation. XCTestCase methods are not main-actor-isolated by default, causing errors when accessing @MainActor objects.

Error you'll see:

Call to main actor-isolated initializer 'init()' in a synchronous nonisolated context

Solution 1: Mark Test Class with @MainActor (Recommended)
@MainActor
final class MyUITests: XCTestCase {
    var app: XCUIApplication!

    override func setUp() {
        super.setUp()
        app = XCUIApplication()
        app.launch()
    }

    override func tearDown() {
        app = nil
        super.tearDown()
    }

    func testSomething() {
        // All code runs on main actor
    }
}

Solution 2: Async setUp/tearDown with MainActor.run
final class MyUITests: XCTestCase {
    var app: XCUIApplication!

    override func setUp() async throws {
        try await super.setUp()
        await MainActor.run {
            app = XCUIApplication()
            app.launch()
        }
    }

    override func tearDown() async throws {
        await MainActor.run {
            app = nil
        }
        try await super.tearDown()
    }
}

Solution 3: Mark Properties as nonisolated

For properties that don't need main actor:

@MainActor
final class MyUITests: XCTestCase {
    nonisolated var testUserID: String {
        ProcessInfo.processInfo.environment["TEST_USER_ID"] ?? "default"
    }
}

Async Test Methods
@MainActor
func testAsyncOperation() async throws {
    app.buttons["Start"].tap()

    // Await async operation
    try await Task.sleep(nanoseconds: 1_000_000_000)

    XCTAssertTrue(app.staticTexts["Complete"].exists)
}

Screenshots and Attachments
Take Screenshot
// Screenshot of entire screen
let screenshot = XCUIScreen.main.screenshot()

// Screenshot of specific element
let elementShot = element.screenshot()

// Create attachment
let attachment = XCTAttachment(screenshot: screenshot)
attachment.name = "Login Screen"
attachment.lifetime = .keepAlways  // Don't delete after test
add(attachment)

Automatic Screenshot on Failure
override func tearDown() {
    if let failureCount = testRun?.failureCount, failureCount > 0 {
        let screenshot = XCUIScreen.main.screenshot()
        let attachment = XCTAttachment(screenshot: screenshot)
        attachment.name = "Failure-\(name)"
        attachment.lifetime = .keepAlways
        add(attachment)
    }
    super.tearDown()
}

Access Screenshots After Test

Screenshots are stored in the .xcresult bundle in DerivedData. Use xcparse to extract:

brew install xcparse
xcparse screenshots /path/to/Test.xcresult /output/directory

Launch Arguments and Environment
Setting Values
let app = XCUIApplication()

// Launch arguments (appear in ProcessInfo.processInfo.arguments)
app.launchArguments = ["-UITest", "-DisableAnimations"]
app.launchArguments.append("-SkipOnboarding")

// Launch environment (appear in ProcessInfo.processInfo.environment)
app.launchEnvironment["API_URL"] = "https://test.example.com"
app.launchEnvironment["TEST_USER_ID"] = "test-user-123"

app.launch()  // Must be set before launch!

Reading in App Code
// Check for launch argument
if ProcessInfo.processInfo.arguments.contains("-UITest") {
    UIView.setAnimationsEnabled(false)
}

// Read environment variable
if let testUserID = ProcessInfo.processInfo.environment["TEST_USER_ID"] {
    UserDefaults.standard.set(testUserID, forKey: "testUserID")
}

UserDefaults Override Trick

Arguments with - prefix set UserDefaults:

// In test
app.launchArguments = ["-myKey", "myValue"]

// In app - reads from UserDefaults
UserDefaults.standard.string(forKey: "myKey") // "myValue"

Localization Testing
app.launchArguments = [
    "-AppleLanguages", "(es)",
    "-AppleLocale", "es_ES"
]

Accessibility Testing
app.launchArguments = [
    "-UIPreferredContentSizeCategoryName",
    UIContentSizeCategory.accessibilityExtraExtraExtraLarge.rawValue
]

Assertions
Basic Assertions
XCTAssertTrue(element.exists)
XCTAssertFalse(element.exists)
XCTAssertEqual(element.label, "Expected")
XCTAssertNotEqual(element.value as? String, "Wrong")
XCTAssertNil(element.value)
XCTAssertNotNil(element.value)

With Custom Messages
XCTAssertTrue(element.exists, "Submit button should be visible")
XCTAssertEqual(element.label, "Done", "Button label should be 'Done' after completion")

Existence Patterns
// Element must exist (fails test if not)
XCTAssertTrue(element.waitForExistence(timeout: 5), "Element not found")

// Element should not exist
XCTAssertFalse(app.alerts["Error"].exists, "Unexpected error alert")

// Element state
XCTAssertTrue(button.isEnabled, "Button should be enabled")
XCTAssertTrue(button.isHittable, "Button should be tappable")

System Alerts
Interruption Monitor (for system dialogs)
override func setUp() {
    super.setUp()

    // Set up before launching app
    addUIInterruptionMonitor(withDescription: "System Alert") { alert -> Bool in
        // Handle location permission
        if alert.buttons["Allow While Using App"].exists {
            alert.buttons["Allow While Using App"].tap()
            return true
        }
        // Handle notification permission
        if alert.buttons["Allow"].exists {
            alert.buttons["Allow"].tap()
            return true
        }
        // Handle "Don't Allow"
        if alert.buttons["Don't Allow"].exists {
            alert.buttons["Don't Allow"].tap()
            return true
        }
        return false
    }

    app.launch()
}

func testWithSystemAlert() {
    // Trigger action that shows system alert
    app.buttons["Request Permission"].tap()

    // IMPORTANT: Must interact with app to trigger handler
    app.tap()

    // Continue test...
}

Direct Alert Handling
// For app alerts (not system)
let alert = app.alerts["Confirm Delete"]
if alert.waitForExistence(timeout: 3) {
    alert.buttons["Delete"].tap()
}

// For springboard alerts (system)
let springboard = XCUIApplication(bundleIdentifier: "com.apple.springboard")
let systemAlert = springboard.alerts.firstMatch
if systemAlert.waitForExistence(timeout: 3) {
    systemAlert.buttons["Allow"].tap()
}

Common Patterns
Page Object Model
protocol Screen {
    var app: XCUIApplication { get }
    func waitForScreen(timeout: TimeInterval) -> Bool
}

struct LoginScreen: Screen {
    let app: XCUIApplication

    var usernameField: XCUIElement { app.textFields["username"] }
    var passwordField: XCUIElement { app.secureTextFields["password"] }
    var loginButton: XCUIElement { app.buttons["Login"] }
    var errorLabel: XCUIElement { app.staticTexts["error-message"] }

    func waitForScreen(timeout: TimeInterval = 5) -> Bool {
        usernameField.waitForExistence(timeout: timeout)
    }

    func login(username: String, password: String) -> HomeScreen {
        usernameField.tap()
        usernameField.typeText(username)
        passwordField.tap()
        passwordField.typeText(password)
        loginButton.tap()
        return HomeScreen(app: app)
    }
}

Reusable Helpers
extension XCUIApplication {
    func waitForElement(_ identifier: String, timeout: TimeInterval = 5) -> XCUIElement {
        let element = descendants(matching: .any).matching(identifier: identifier).firstMatch
        XCTAssertTrue(element.waitForExistence(timeout: timeout),
                      "Element '\(identifier)' not found within \(timeout)s")
        return element
    }

    func tapTab(_ identifier: String) {
        let tab = buttons[identifier]
        XCTAssertTrue(tab.waitForExistence(timeout: 5), "Tab '\(identifier)' not found")
        tab.tap()
    }
}

extension XCUIElement {
    func clearAndType(_ text: String) {
        guard let currentValue = value as? String, !currentValue.isEmpty else {
            tap()
            typeText(text)
            return
        }
        tap()
        let deleteString = String(repeating: XCUIKeyboardKey.delete.rawValue, count: currentValue.count)
        typeText(deleteString)
        typeText(text)
    }
}

Timeout Constants
enum TestTimeout: TimeInterval {
    case short = 2
    case medium = 5
    case long = 10
    case networkLoad = 30
}

// Usage
button.waitForExistence(timeout: TestTimeout.medium.rawValue)

Advanced Patterns

For more detailed patterns including:

Base test class implementation
iOS system dialog handling (HealthKit, Location, Notifications)
Scroll and wait patterns
Text field helpers
Debugging techniques
Test organization

See patterns.md.

Troubleshooting
Element Not Found
Check accessibility identifier is set in code
Use Accessibility Inspector (Xcode > Open Developer Tool)
Print element hierarchy: print(app.debugDescription)
Check element is in view (may need scrolling)
Ensure element is enabled for accessibility
Flaky Tests
Use waitForExistence instead of sleep
Add continueAfterFailure = false
Disable animations in test setup
Reset simulator state between tests
Use unique test data
Swift 6 Concurrency Errors
Mark test class with @MainActor
Use nonisolated for properties that don't need main actor
Use async setUp/tearDown if needed
Check for Sendable conformance issues
Screenshots Not Saved
Set attachment.lifetime = .keepAlways
Check DerivedData location for .xcresult
Use xcparse to extract from result bundle
Permission Dialog Issues
Use resetAuthorizationStatus(for:) before app.launch()
HealthKit uses a scrollable sheet on iOS 26 - must scroll to reveal buttons
addUIInterruptionMonitor requires an app interaction to trigger
For system-level alerts, use springboard bundle identifier approach
What's New in Xcode 26 / iOS 26
New APIs
wait(for:toEqual:timeout:) - KeyPath-based waiting for any property value
waitForNonExistence(withTimeout:) - Native API to wait for element removal (Xcode 16+)
XCTHitchMetric - Measure UI responsiveness and frame drops
Enhanced Recording
Cleaner, more maintainable generated test code
Multiple identifier options for element selection
Integration with Test Report's Automation Explorer
Cross-Platform Testing
Run automation tests across iPhone, iPad, Mac, Apple TV, Apple Watch
Test plan configurations for multiple locales, device types, system conditions
Video recordings and screenshots of test runs in results
Swift Concurrency Debugging
Seamless stepping across threads in async tests
Task ID visibility in debugger
Thread Performance Checker integration
Sources
Apple Documentation
XCTest | Apple Developer Documentation
XCUIAutomation | Apple Developer Documentation
XCUIElementQuery | Apple Developer Documentation
waitForExistence | Apple Developer Documentation
wait(for:toEqual:timeout:) | Apple Developer Documentation
resetAuthorizationStatus(for:) | Apple Developer Documentation
XCUIProtectedResource | Apple Developer Documentation
XCUIScreenshot | Apple Developer Documentation
WWDC Sessions
Record, replay, and review: UI automation with Xcode - WWDC25
What's new in Xcode 26 - WWDC25
Community Resources
XCTest Meets @MainActor | Quality Coding
Issues with setUp() and tearDown() in XCTest for Swift 6 | Swift Forums
Waiting in XCTest | Masilotti.com
UI Testing Cheat Sheet | Masilotti.com
XCUIElement Actions and Gestures | Apps Developer Blog
Configuring UI tests with launch arguments | polpiella.dev
UI Testing improvements in Xcode 16 | Jesse Squires
Fetching More Apple Docs
Search this skill's local .md files first.
If the topic is not here, check the other installed Apple skills you have available by their names, descriptions, or SKILL.md frontmatter, then grep their local files. This is faster and uses less context than fetching new docs from the internet.
If no installed skill has the page, use the relevant documentation path from the local XCTest or XCUIAutomation indexes with the sosumi.ai Markdown mirror. For example, /documentation/xcuiautomation/xcuielement maps to https://sosumi.ai/documentation/xcuiautomation/xcuielement.
Weekly Installs
122
Repository
vabole/apple-skills
GitHub Stars
224
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn