---
rating: ⭐⭐
title: core-motion
url: https://skills.sh/dpearson2699/swift-ios-skills/core-motion
---

# core-motion

skills/dpearson2699/swift-ios-skills/core-motion
core-motion
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill core-motion
SKILL.md
CoreMotion

Read device sensor data -- accelerometer, gyroscope, magnetometer, pedometer, and activity recognition -- on iOS and watchOS. CoreMotion fuses raw sensor inputs into processed device-motion data and provides pedometer/activity APIs for fitness and navigation use cases. Targets Swift 6.3 / iOS 26+.

Contents
Setup
CMMotionManager: Sensor Data
Processed Device Motion
CMPedometer: Step and Distance Data
CMMotionActivityManager: Activity Recognition
CMAltimeter: Altitude Data
Update Intervals and Battery
Common Mistakes
Review Checklist
References
Setup
Info.plist

Add NSMotionUsageDescription to Info.plist with a user-facing string explaining why your app needs motion data. Without this key, the app crashes on first access.

<key>NSMotionUsageDescription</key>
<string>This app uses motion data to track your activity.</string>

Authorization

CoreMotion uses CMAuthorizationStatus for pedometer and activity APIs. Sensor APIs (accelerometer, gyro) do not require explicit authorization but do require the usage description key.

import CoreMotion

let status = CMMotionActivityManager.authorizationStatus()
switch status {
case .notDetermined:
    // Will prompt on first use
    break
case .authorized:
    break
case .restricted, .denied:
    // Direct user to Settings
    break
@unknown default:
    break
}

CMMotionManager: Sensor Data

Create exactly one CMMotionManager per app. Multiple instances degrade sensor update rates.

import CoreMotion

let motionManager = CMMotionManager()

Accelerometer Updates
guard motionManager.isAccelerometerAvailable else { return }

motionManager.accelerometerUpdateInterval = 1.0 / 60.0  // 60 Hz

motionManager.startAccelerometerUpdates(to: .main) { data, error in
    guard let acceleration = data?.acceleration else { return }
    print("x: \(acceleration.x), y: \(acceleration.y), z: \(acceleration.z)")
}

// When done:
motionManager.stopAccelerometerUpdates()

Gyroscope Updates
guard motionManager.isGyroAvailable else { return }

motionManager.gyroUpdateInterval = 1.0 / 60.0

motionManager.startGyroUpdates(to: .main) { data, error in
    guard let rotationRate = data?.rotationRate else { return }
    print("x: \(rotationRate.x), y: \(rotationRate.y), z: \(rotationRate.z)")
}

motionManager.stopGyroUpdates()

Polling Pattern (Games)

For games, start updates without a handler and poll the latest sample each frame:

motionManager.startAccelerometerUpdates()

// In your game loop / display link:
if let data = motionManager.accelerometerData {
    let tilt = data.acceleration.x
    // Move player based on tilt
}

Processed Device Motion

Device motion fuses accelerometer, gyroscope, and magnetometer into a single CMDeviceMotion object with attitude, user acceleration (gravity removed), rotation rate, and calibrated magnetic field.

guard motionManager.isDeviceMotionAvailable else { return }

motionManager.deviceMotionUpdateInterval = 1.0 / 60.0

motionManager.startDeviceMotionUpdates(
    using: .xArbitraryZVertical,
    to: .main
) { motion, error in
    guard let motion else { return }

    let attitude = motion.attitude       // roll, pitch, yaw
    let userAccel = motion.userAcceleration
    let gravity = motion.gravity
    let heading = motion.heading         // 0-360 degrees (requires magnetometer)

    print("Pitch: \(attitude.pitch), Roll: \(attitude.roll)")
}

motionManager.stopDeviceMotionUpdates()

Attitude Reference Frames
Frame	Use Case
.xArbitraryZVertical	Default. Z is vertical, X arbitrary at start. Most games.
.xArbitraryCorrectedZVertical	Same as above, corrected for gyro drift over time.
.xMagneticNorthZVertical	X points to magnetic north. Requires magnetometer.
.xTrueNorthZVertical	X points to true north. Requires magnetometer + location.

Check available frames before use:

let available = CMMotionManager.availableAttitudeReferenceFrames()
if available.contains(.xTrueNorthZVertical) {
    // Safe to use true north
}

CMPedometer: Step and Distance Data

CMPedometer provides step counts, distance, pace, cadence, and floor counts.

let pedometer = CMPedometer()

guard CMPedometer.isStepCountingAvailable() else { return }

// Historical query
pedometer.queryPedometerData(
    from: Calendar.current.startOfDay(for: Date()),
    to: Date()
) { data, error in
    guard let data else { return }
    print("Steps today: \(data.numberOfSteps)")
    print("Distance: \(data.distance?.doubleValue ?? 0) meters")
    print("Floors up: \(data.floorsAscended?.intValue ?? 0)")
}

// Live updates
pedometer.startUpdates(from: Date()) { data, error in
    guard let data else { return }
    print("Steps: \(data.numberOfSteps)")
}

// Stop when done
pedometer.stopUpdates()

Availability Checks
Method	What It Checks
isStepCountingAvailable()	Step counter hardware
isDistanceAvailable()	Distance estimation
isFloorCountingAvailable()	Barometric altimeter for floors
isPaceAvailable()	Pace data
isCadenceAvailable()	Cadence data
CMMotionActivityManager: Activity Recognition

Detects whether the user is stationary, walking, running, cycling, or in a vehicle.

let activityManager = CMMotionActivityManager()

guard CMMotionActivityManager.isActivityAvailable() else { return }

// Live activity updates
activityManager.startActivityUpdates(to: .main) { activity in
    guard let activity else { return }

    if activity.walking {
        print("Walking (confidence: \(activity.confidence.rawValue))")
    } else if activity.running {
        print("Running")
    } else if activity.automotive {
        print("In vehicle")
    } else if activity.cycling {
        print("Cycling")
    } else if activity.stationary {
        print("Stationary")
    }
}

activityManager.stopActivityUpdates()

Historical Activity Query
let yesterday = Calendar.current.date(byAdding: .day, value: -1, to: Date())!

activityManager.queryActivityStarting(
    from: yesterday,
    to: Date(),
    to: .main
) { activities, error in
    guard let activities else { return }
    for activity in activities {
        print("\(activity.startDate): walking=\(activity.walking)")
    }
}

CMAltimeter: Altitude Data
let altimeter = CMAltimeter()

guard CMAltimeter.isRelativeAltitudeAvailable() else { return }

altimeter.startRelativeAltitudeUpdates(to: .main) { data, error in
    guard let data else { return }
    print("Relative altitude: \(data.relativeAltitude) meters")
    print("Pressure: \(data.pressure) kPa")
}

altimeter.stopRelativeAltitudeUpdates()


For absolute altitude (GPS-based):

guard CMAltimeter.isAbsoluteAltitudeAvailable() else { return }

altimeter.startAbsoluteAltitudeUpdates(to: .main) { data, error in
    guard let data else { return }
    print("Altitude: \(data.altitude)m, accuracy: \(data.accuracy)m")
}

altimeter.stopAbsoluteAltitudeUpdates()

Update Intervals and Battery
Interval	Hz	Use Case	Battery Impact
1.0 / 10.0	10	UI orientation	Low
1.0 / 30.0	30	Casual games	Moderate
1.0 / 60.0	60	Action games	High
1.0 / 100.0	100	Max rate (iPhone)	Very High

Use the lowest frequency that meets your needs. CMMotionManager caps at 100 Hz per sample. For higher frequencies, use CMBatchedSensorManager on watchOS/iOS 17+.

Common Mistakes
DON'T: Create multiple CMMotionManager instances
// WRONG -- degrades update rates for all instances
class ViewA { let motion = CMMotionManager() }
class ViewB { let motion = CMMotionManager() }

// CORRECT -- single instance, shared across the app
@Observable
final class MotionService {
    static let shared = MotionService()
    let manager = CMMotionManager()
}

DON'T: Skip sensor availability checks
// WRONG -- crashes on devices without gyroscope
motionManager.startGyroUpdates(to: .main) { data, _ in }

// CORRECT -- check first
guard motionManager.isGyroAvailable else {
    showUnsupportedMessage()
    return
}
motionManager.startGyroUpdates(to: .main) { data, _ in }

DON'T: Forget to stop updates
// WRONG -- updates keep running, draining battery
class MotionVC: UIViewController {
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        motionManager.startAccelerometerUpdates(to: .main) { _, _ in }
    }
    // Missing viewDidDisappear stop!
}

// CORRECT -- stop in the counterpart lifecycle method
override func viewDidDisappear(_ animated: Bool) {
    super.viewDidDisappear(animated)
    motionManager.stopAccelerometerUpdates()
}

DON'T: Use unnecessarily high update rates
// WRONG -- 100 Hz for a compass display
motionManager.deviceMotionUpdateInterval = 1.0 / 100.0

// CORRECT -- 10 Hz is more than enough for a compass
motionManager.deviceMotionUpdateInterval = 1.0 / 10.0

DON'T: Assume all CMMotionActivity properties are mutually exclusive
// WRONG -- checking only one property
if activity.walking { handleWalking() }

// CORRECT -- multiple can be true simultaneously; check confidence
if activity.walking && activity.confidence == .high {
    handleWalking()
} else if activity.automotive && activity.confidence != .low {
    handleDriving()
}

Review Checklist
 NSMotionUsageDescription present in Info.plist with a clear explanation
 Single CMMotionManager instance shared across the app
 Sensor availability checked before starting updates (isAccelerometerAvailable, etc.)
 Authorization status checked before pedometer/activity APIs
 Update interval set to the lowest acceptable frequency
 All start*Updates calls have matching stop*Updates in lifecycle counterparts
 Handlers dispatched to appropriate queues (not blocking main for heavy processing)
 CMMotionActivity.confidence checked before acting on activity type
 Error parameters checked in update handlers
 Attitude reference frame chosen based on actual need (not defaulting to true north unnecessarily)
References
Extended patterns (SwiftUI integration, batched sensor manager, headphone motion): references/motion-patterns.md
CoreMotion framework
CMMotionManager
CMPedometer
CMMotionActivityManager
CMDeviceMotion
CMAltimeter
CMBatchedSensorManager
Getting processed device-motion data
Weekly Installs
1.1K
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