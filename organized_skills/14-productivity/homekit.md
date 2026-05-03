---
rating: ⭐⭐
title: homekit
url: https://skills.sh/dpearson2699/swift-ios-skills/homekit
---

# homekit

skills/dpearson2699/swift-ios-skills/homekit
homekit
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill homekit
SKILL.md
HomeKit

Control home automation accessories and commission Matter devices. HomeKit manages the home/room/accessory model, action sets, and triggers. MatterSupport handles device commissioning into your ecosystem. Targets Swift 6.3 / iOS 26+.

Contents
Setup
HomeKit Data Model
Managing Accessories
Reading and Writing Characteristics
Action Sets and Triggers
Matter Commissioning
MatterAddDeviceExtensionRequestHandler
Common Mistakes
Review Checklist
References
Setup
HomeKit Configuration
Enable the HomeKit capability in Xcode (Signing & Capabilities)
Add NSHomeKitUsageDescription to Info.plist:
<key>NSHomeKitUsageDescription</key>
<string>This app controls your smart home accessories.</string>

MatterSupport Configuration

For Matter commissioning into your own ecosystem:

Enable the MatterSupport capability
Add a MatterSupport Extension target to your project
Add the com.apple.developer.matter.allow-setup-payload entitlement if your app provides the setup code directly
Availability Check
import HomeKit

let homeManager = HMHomeManager()

// HomeKit is available on iPhone, iPad, Apple TV, Apple Watch, Mac, and Vision Pro.
// Authorization is handled through the delegate:
homeManager.delegate = self

HomeKit Data Model

HomeKit organizes home automation in a hierarchy:

HMHomeManager
  -> HMHome (one or more)
       -> HMRoom (rooms in the home)
            -> HMAccessory (devices in a room)
                 -> HMService (functions: light, thermostat, etc.)
                      -> HMCharacteristic (readable/writable values)
       -> HMZone (groups of rooms)
       -> HMActionSet (grouped actions)
       -> HMTrigger (time or event-based triggers)

Initializing the Home Manager

Create a single HMHomeManager and implement the delegate to know when data is loaded. HomeKit loads asynchronously -- do not access homes until the delegate fires.

import HomeKit

final class HomeStore: NSObject, HMHomeManagerDelegate {
    let homeManager = HMHomeManager()

    override init() {
        super.init()
        homeManager.delegate = self
    }

    func homeManagerDidUpdateHomes(_ manager: HMHomeManager) {
        // Safe to access manager.homes now
        let homes = manager.homes
        let primaryHome = manager.primaryHome
        print("Loaded \(homes.count) homes")
    }

    func homeManager(
        _ manager: HMHomeManager,
        didUpdate status: HMHomeManagerAuthorizationStatus
    ) {
        if status.contains(.authorized) {
            print("HomeKit access granted")
        }
    }
}

Accessing Rooms
guard let home = homeManager.primaryHome else { return }

let rooms = home.rooms
let kitchen = rooms.first { $0.name == "Kitchen" }

// Room for accessories not assigned to a specific room
let defaultRoom = home.roomForEntireHome()

Managing Accessories
Discovering and Adding Accessories
// System UI for accessory discovery
home.addAndSetupAccessories { error in
    if let error {
        print("Setup failed: \(error)")
    }
}

Listing Accessories and Services
for accessory in home.accessories {
    print("\(accessory.name) in \(accessory.room?.name ?? "unassigned")")

    for service in accessory.services {
        print("  Service: \(service.serviceType)")

        for characteristic in service.characteristics {
            print("    \(characteristic.characteristicType): \(characteristic.value ?? "nil")")
        }
    }
}

Moving an Accessory to a Room
guard let accessory = home.accessories.first,
      let bedroom = home.rooms.first(where: { $0.name == "Bedroom" }) else { return }

home.assignAccessory(accessory, to: bedroom) { error in
    if let error {
        print("Failed to move accessory: \(error)")
    }
}

Reading and Writing Characteristics
Reading a Value
let characteristic: HMCharacteristic = // obtained from a service

characteristic.readValue { error in
    guard error == nil else { return }
    if let value = characteristic.value as? Bool {
        print("Power state: \(value)")
    }
}

Writing a Value
// Turn on a light
characteristic.writeValue(true) { error in
    if let error {
        print("Write failed: \(error)")
    }
}

Observing Changes

Enable notifications for real-time updates:

characteristic.enableNotification(true) { error in
    guard error == nil else { return }
}

// In HMAccessoryDelegate:
func accessory(
    _ accessory: HMAccessory,
    service: HMService,
    didUpdateValueFor characteristic: HMCharacteristic
) {
    print("Updated: \(characteristic.value ?? "nil")")
}

Action Sets and Triggers
Creating an Action Set

An HMActionSet groups characteristic writes that execute together:

home.addActionSet(withName: "Good Night") { actionSet, error in
    guard let actionSet, error == nil else { return }

    // Turn off living room light
    let lightChar = livingRoomLight.powerCharacteristic
    let action = HMCharacteristicWriteAction(
        characteristic: lightChar,
        targetValue: false as NSCopying
    )
    actionSet.addAction(action) { error in
        guard error == nil else { return }
        print("Action added to Good Night scene")
    }
}

Executing an Action Set
home.executeActionSet(actionSet) { error in
    if let error {
        print("Execution failed: \(error)")
    }
}

Creating a Timer Trigger
var dateComponents = DateComponents()
dateComponents.hour = 22
dateComponents.minute = 30

let trigger = HMTimerTrigger(
    name: "Nightly",
    fireDate: Calendar.current.nextDate(
        after: Date(),
        matching: dateComponents,
        matchingPolicy: .nextTime
    )!,
    timeZone: .current,
    recurrence: dateComponents,  // Repeats daily at 22:30
    recurrenceCalendar: .current
)

home.addTrigger(trigger) { error in
    guard error == nil else { return }

    // Attach the action set to the trigger
    trigger.addActionSet(goodNightActionSet) { error in
        guard error == nil else { return }

        trigger.enable(true) { error in
            print("Trigger enabled: \(error == nil)")
        }
    }
}

Creating an Event Trigger
let motionDetected = HMCharacteristicEvent(
    characteristic: motionSensorCharacteristic,
    triggerValue: true as NSCopying
)

let eventTrigger = HMEventTrigger(
    name: "Motion Lights",
    events: [motionDetected],
    predicate: nil
)

home.addTrigger(eventTrigger) { error in
    // Add action sets as above
}

Matter Commissioning

Use MatterAddDeviceRequest to commission a Matter device into your ecosystem. This is separate from HomeKit -- it handles the pairing flow.

Basic Commissioning
import MatterSupport

func addMatterDevice() async throws {
    guard MatterAddDeviceRequest.isSupported else {
        print("Matter not supported on this device")
        return
    }

    let topology = MatterAddDeviceRequest.Topology(
        ecosystemName: "My Smart Home",
        homes: [
            MatterAddDeviceRequest.Home(displayName: "Main House")
        ]
    )

    let request = MatterAddDeviceRequest(
        topology: topology,
        setupPayload: nil,
        showing: .allDevices
    )

    // Presents system UI for device pairing
    try await request.perform()
}

Filtering Devices
// Only show devices from a specific vendor
let criteria = MatterAddDeviceRequest.DeviceCriteria.vendorID(0x1234)

let request = MatterAddDeviceRequest(
    topology: topology,
    setupPayload: nil,
    showing: criteria
)

Combining Device Criteria
let criteria = MatterAddDeviceRequest.DeviceCriteria.all([
    .vendorID(0x1234),
    .not(.productID(0x0001))  // Exclude a specific product
])

MatterAddDeviceExtensionRequestHandler

For full ecosystem support, create a MatterSupport Extension. The extension handles commissioning callbacks:

import MatterSupport

final class MatterHandler: MatterAddDeviceExtensionRequestHandler {

    override func validateDeviceCredential(
        _ deviceCredential: DeviceCredential
    ) async throws {
        // Validate the device attestation certificate
        // Throw to reject the device
    }

    override func rooms(
        in home: MatterAddDeviceRequest.Home?
    ) async -> [MatterAddDeviceRequest.Room] {
        // Return rooms in the selected home
        return [
            MatterAddDeviceRequest.Room(displayName: "Living Room"),
            MatterAddDeviceRequest.Room(displayName: "Kitchen")
        ]
    }

    override func configureDevice(
        named name: String,
        in room: MatterAddDeviceRequest.Room?
    ) async {
        // Save the device configuration to your backend
        print("Configuring \(name) in \(room?.displayName ?? "no room")")
    }

    override func commissionDevice(
        in home: MatterAddDeviceRequest.Home?,
        onboardingPayload: String,
        commissioningID: UUID
    ) async throws {
        // Use the onboarding payload to commission the device
        // into your fabric using the Matter framework
    }
}

Common Mistakes
DON'T: Access homes before the delegate fires
// WRONG -- homes array is empty until delegate is called
let manager = HMHomeManager()
let homes = manager.homes  // Always empty here

// CORRECT -- wait for delegate
func homeManagerDidUpdateHomes(_ manager: HMHomeManager) {
    let homes = manager.homes  // Now populated
}

DON'T: Confuse HomeKit setup with Matter commissioning
// WRONG -- using HomeKit accessory setup for a Matter ecosystem app
home.addAndSetupAccessories { error in }

// CORRECT -- use MatterAddDeviceRequest for Matter ecosystem commissioning
let request = MatterAddDeviceRequest(
    topology: topology,
    setupPayload: nil,
    showing: .allDevices
)
try await request.perform()

DON'T: Forget required entitlements
// WRONG -- calling Matter APIs without the MatterSupport entitlement
// Results in runtime error

// CORRECT -- ensure these are set up:
// 1. HomeKit capability for HMHomeManager access
// 2. MatterSupport Extension target for ecosystem commissioning
// 3. com.apple.developer.matter.allow-setup-payload if providing setup codes

DON'T: Create multiple HMHomeManager instances
// WRONG -- each instance loads the full database independently
class ScreenA { let manager = HMHomeManager() }
class ScreenB { let manager = HMHomeManager() }

// CORRECT -- single shared instance
@Observable
final class HomeStore {
    static let shared = HomeStore()
    let homeManager = HMHomeManager()
}

DON'T: Write characteristics without checking metadata
// WRONG -- writing a value outside the valid range
characteristic.writeValue(500) { _ in }

// CORRECT -- check metadata first
if let metadata = characteristic.metadata,
   let maxValue = metadata.maximumValue?.intValue {
    let safeValue = min(brightness, maxValue)
    characteristic.writeValue(safeValue) { _ in }
}

Review Checklist
 HomeKit capability enabled in Xcode
 NSHomeKitUsageDescription present in Info.plist
 Single HMHomeManager instance shared across the app
 HMHomeManagerDelegate implemented; homes not accessed before homeManagerDidUpdateHomes
 HMHomeDelegate set on homes to receive accessory and room changes
 HMAccessoryDelegate set on accessories to receive characteristic updates
 Characteristic metadata checked before writing values
 Error handling in all completion handlers
 MatterSupport capability and extension target added for Matter commissioning
 MatterAddDeviceRequest.isSupported checked before performing requests
 Matter extension handler implements commissionDevice(in:onboardingPayload:commissioningID:)
 Action sets tested with the HomeKit Accessory Simulator before shipping
 Triggers enabled after creation (trigger.enable(true))
References
Extended patterns (Matter extension, delegate wiring, SwiftUI): references/matter-commissioning.md
HomeKit framework
HMHomeManager
HMHome
HMAccessory
HMRoom
HMActionSet
HMTrigger
MatterSupport framework
MatterAddDeviceRequest
MatterAddDeviceExtensionRequestHandler
Enabling HomeKit in your app
Adding Matter support to your ecosystem
Weekly Installs
667
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