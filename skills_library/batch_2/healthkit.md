---
title: healthkit
url: https://skills.sh/dpearson2699/swift-ios-skills/healthkit
---

# healthkit

skills/dpearson2699/swift-ios-skills/healthkit
healthkit
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill healthkit
SKILL.md
HealthKit

Read and write health and fitness data from the Apple Health store. Covers authorization, queries, writing samples, background delivery, and workout sessions. Targets Swift 6.3 / iOS 26+.

Contents
Setup and Availability
Authorization
Reading Data: Sample Queries
Reading Data: Statistics Queries
Reading Data: Statistics Collection Queries
Writing Data
Background Delivery
Workout Sessions
Common Data Types
HKUnit Reference
Common Mistakes
Review Checklist
References
Setup and Availability
Project Configuration
Enable the HealthKit capability in Xcode (adds the entitlement)
Add NSHealthShareUsageDescription (read) and NSHealthUpdateUsageDescription (write) to Info.plist
For background delivery, enable the "Background Delivery" sub-capability
Availability Check

Always check availability before accessing HealthKit. iPad and some devices do not support it.

import HealthKit

let healthStore = HKHealthStore()

guard HKHealthStore.isHealthDataAvailable() else {
    // HealthKit not available on this device (e.g., iPad)
    return
}


Create a single HKHealthStore instance and reuse it throughout your app. It is thread-safe.

Authorization

Request only the types your app genuinely needs. App Review rejects apps that over-request.

func requestAuthorization() async throws {
    let typesToShare: Set<HKSampleType> = [
        HKQuantityType(.stepCount),
        HKQuantityType(.activeEnergyBurned)
    ]

    let typesToRead: Set<HKObjectType> = [
        HKQuantityType(.stepCount),
        HKQuantityType(.heartRate),
        HKQuantityType(.activeEnergyBurned),
        HKCharacteristicType(.dateOfBirth)
    ]

    try await healthStore.requestAuthorization(
        toShare: typesToShare,
        read: typesToRead
    )
}

Checking Authorization Status

The app can only determine if it has not yet requested authorization. If the user denied access, HealthKit returns empty results rather than an error -- this is a privacy design.

let status = healthStore.authorizationStatus(
    for: HKQuantityType(.stepCount)
)

switch status {
case .notDetermined:
    // Haven't requested yet -- safe to call requestAuthorization
    break
case .sharingAuthorized:
    // User granted write access
    break
case .sharingDenied:
    // User denied write access (read denial is indistinguishable from "no data")
    break
@unknown default:
    break
}

Reading Data: Sample Queries

Use HKSampleQueryDescriptor (async/await) for one-shot reads. Prefer descriptors over the older callback-based HKSampleQuery.

func fetchRecentHeartRates() async throws -> [HKQuantitySample] {
    let heartRateType = HKQuantityType(.heartRate)

    let descriptor = HKSampleQueryDescriptor(
        predicates: [.quantitySample(type: heartRateType)],
        sortDescriptors: [SortDescriptor(\.endDate, order: .reverse)],
        limit: 20
    )

    let results = try await descriptor.result(for: healthStore)
    return results
}

// Extracting values from samples:
for sample in results {
    let bpm = sample.quantity.doubleValue(
        for: HKUnit.count().unitDivided(by: .minute())
    )
    print("\(bpm) bpm at \(sample.endDate)")
}

Reading Data: Statistics Queries

Use HKStatisticsQueryDescriptor for aggregated single-value stats (sum, average, min, max).

func fetchTodayStepCount() async throws -> Double? {
    let calendar = Calendar.current
    let startOfDay = calendar.startOfDay(for: Date())
    let endOfDay = calendar.date(byAdding: .day, value: 1, to: startOfDay)!

    let predicate = HKQuery.predicateForSamples(
        withStart: startOfDay, end: endOfDay
    )
    let stepType = HKQuantityType(.stepCount)
    let samplePredicate = HKSamplePredicate.quantitySample(
        type: stepType, predicate: predicate
    )

    let query = HKStatisticsQueryDescriptor(
        predicate: samplePredicate,
        options: .cumulativeSum
    )

    let result = try await query.result(for: healthStore)
    return result?.sumQuantity()?.doubleValue(for: .count())
}


Options by data type:

Cumulative types (steps, calories): .cumulativeSum
Discrete types (heart rate, weight): .discreteAverage, .discreteMin, .discreteMax
Reading Data: Statistics Collection Queries

Use HKStatisticsCollectionQueryDescriptor for time-series data grouped into intervals -- ideal for charts.

func fetchDailySteps(forLast days: Int) async throws -> [(date: Date, steps: Double)] {
    let calendar = Calendar.current
    let endDate = calendar.startOfDay(
        for: calendar.date(byAdding: .day, value: 1, to: Date())!
    )
    let startDate = calendar.date(byAdding: .day, value: -days, to: endDate)!

    let predicate = HKQuery.predicateForSamples(
        withStart: startDate, end: endDate
    )
    let stepType = HKQuantityType(.stepCount)
    let samplePredicate = HKSamplePredicate.quantitySample(
        type: stepType, predicate: predicate
    )

    let query = HKStatisticsCollectionQueryDescriptor(
        predicate: samplePredicate,
        options: .cumulativeSum,
        anchorDate: endDate,
        intervalComponents: DateComponents(day: 1)
    )

    let collection = try await query.result(for: healthStore)
    var dailySteps: [(date: Date, steps: Double)] = []

    collection.statisticsCollection.enumerateStatistics(
        from: startDate, to: endDate
    ) { statistics, _ in
        let steps = statistics.sumQuantity()?
            .doubleValue(for: .count()) ?? 0
        dailySteps.append((date: statistics.startDate, steps: steps))
    }

    return dailySteps
}

Long-Running Collection Query

Use results(for:) (plural) to get an AsyncSequence that emits updates as new data arrives:

let updateStream = query.results(for: healthStore)

Task {
    for try await result in updateStream {
        // result.statisticsCollection contains updated data
    }
}

Writing Data

Create HKQuantitySample objects and save them to the store.

func saveSteps(count: Double, start: Date, end: Date) async throws {
    let stepType = HKQuantityType(.stepCount)
    let quantity = HKQuantity(unit: .count(), doubleValue: count)

    let sample = HKQuantitySample(
        type: stepType,
        quantity: quantity,
        start: start,
        end: end
    )

    try await healthStore.save(sample)
}



Your app can only delete samples it created. Samples from other apps or Apple Watch are read-only.

Background Delivery

Register for background updates so your app is launched when new data arrives. Requires the background delivery entitlement.

func enableStepCountBackgroundDelivery() async throws {
    let stepType = HKQuantityType(.stepCount)

    try await healthStore.enableBackgroundDelivery(
        for: stepType,
        frequency: .hourly
    )
}


Pair with an HKObserverQuery to handle notifications. Always call the completion handler:

let observerQuery = HKObserverQuery(
    sampleType: HKQuantityType(.stepCount),
    predicate: nil
) { query, completionHandler, error in
    defer { completionHandler() }  // Must call to signal done
    guard error == nil else { return }
    // Fetch new data, update UI, etc.
}
healthStore.execute(observerQuery)


Frequencies: .immediate, .hourly, .daily, .weekly

Call enableBackgroundDelivery once (e.g., at app launch). The system persists the registration.

Workout Sessions

Use HKWorkoutSession and HKLiveWorkoutBuilder to track live workouts. Available on watchOS 2+ and iOS 17+.

func startWorkout() async throws {
    let configuration = HKWorkoutConfiguration()
    configuration.activityType = .running
    configuration.locationType = .outdoor

    let session = try HKWorkoutSession(
        healthStore: healthStore,
        configuration: configuration
    )
    session.delegate = self

    let builder = session.associatedWorkoutBuilder()
    builder.dataSource = HKLiveWorkoutDataSource(
        healthStore: healthStore,
        workoutConfiguration: configuration
    )

    session.startActivity(with: Date())
    try await builder.beginCollection(at: Date())
}

func endWorkout(
    session: HKWorkoutSession,
    builder: HKLiveWorkoutBuilder
) async throws {
    session.end()
    try await builder.endCollection(at: Date())
    try await builder.finishWorkout()
}


For full workout lifecycle management including pause/resume, delegate handling, and multi-device mirroring, see references/healthkit-patterns.md.

Common Data Types
HKQuantityTypeIdentifier
Identifier	Category	Unit
.stepCount	Fitness	.count()
.distanceWalkingRunning	Fitness	.meter()
.activeEnergyBurned	Fitness	.kilocalorie()
.basalEnergyBurned	Fitness	.kilocalorie()
.heartRate	Vitals	.count()/.minute()
.restingHeartRate	Vitals	.count()/.minute()
.oxygenSaturation	Vitals	.percent()
.bodyMass	Body	.gramUnit(with: .kilo)
.bodyMassIndex	Body	.count()
.height	Body	.meter()
.bodyFatPercentage	Body	.percent()
.bloodGlucose	Lab	.gramUnit(with: .milli).unitDivided(by: .literUnit(with: .deci))
HKCategoryTypeIdentifier

Common category types: .sleepAnalysis, .mindfulSession, .appleStandHour

HKCharacteristicType

Read-only user characteristics: .dateOfBirth, .biologicalSex, .bloodType, .fitzpatrickSkinType

HKUnit Reference
// Basic units
HKUnit.count()                              // Steps, counts
HKUnit.meter()                              // Distance
HKUnit.mile()                               // Distance (imperial)
HKUnit.kilocalorie()                        // Energy
HKUnit.joule(with: .kilo)                   // Energy (SI)
HKUnit.gramUnit(with: .kilo)                // Mass (kg)
HKUnit.pound()                              // Mass (imperial)
HKUnit.percent()                            // Percentage

// Compound units
HKUnit.count().unitDivided(by: .minute())   // Heart rate (bpm)
HKUnit.meter().unitDivided(by: .second())   // Speed (m/s)

// Prefixed units
HKUnit.gramUnit(with: .milli)               // Milligrams
HKUnit.literUnit(with: .deci)               // Deciliters

Common Mistakes
1. Over-requesting data types

DON'T -- request everything:

// App Review will reject this
let allTypes: Set<HKObjectType> = [
    HKQuantityType(.stepCount),
    HKQuantityType(.heartRate),
    HKQuantityType(.bloodGlucose),
    HKQuantityType(.bodyMass),
    HKQuantityType(.oxygenSaturation),
    // ...20 more types the app never uses
]


DO -- request only what you use:

let neededTypes: Set<HKObjectType> = [
    HKQuantityType(.stepCount),
    HKQuantityType(.activeEnergyBurned)
]

2. Not handling authorization denial

DON'T -- assume data will be returned:

func getSteps() async throws -> Double {
    let result = try await query.result(for: healthStore)
    return result!.sumQuantity()!.doubleValue(for: .count()) // Crashes if denied
}


DO -- handle nil gracefully:

func getSteps() async throws -> Double {
    let result = try await query.result(for: healthStore)
    return result?.sumQuantity()?.doubleValue(for: .count()) ?? 0
}

3. Assuming HealthKit is always available

DON'T -- skip the check:

let store = HKHealthStore() // Crashes on iPad
try await store.requestAuthorization(toShare: types, read: types)


DO -- guard availability:

guard HKHealthStore.isHealthDataAvailable() else {
    showUnsupportedDeviceMessage()
    return
}

4. Running heavy queries on the main thread

DON'T -- use old callback-based queries on main thread. DO -- use async descriptors:

// Bad: HKSampleQuery with callback on main thread
// Good: async descriptor
func loadAllData() async throws -> [HKQuantitySample] {
    let descriptor = HKSampleQueryDescriptor(
        predicates: [.quantitySample(type: stepType)],
        sortDescriptors: [SortDescriptor(\.endDate, order: .reverse)],
        limit: 100
    )
    return try await descriptor.result(for: healthStore)
}

5. Forgetting to call completionHandler in observer queries

DON'T -- skip the completion handler:

let query = HKObserverQuery(sampleType: type, predicate: nil) { _, handler, _ in
    processNewData()
    // Forgot to call handler() -- system won't schedule next delivery
}


DO -- always call it:

let query = HKObserverQuery(sampleType: type, predicate: nil) { _, handler, _ in
    defer { handler() }
    processNewData()
}

6. Using wrong statistics options for the data type

DON'T -- use cumulative sum on discrete types:

// Heart rate is discrete, not cumulative -- this returns nil
let query = HKStatisticsQueryDescriptor(
    predicate: heartRatePredicate,
    options: .cumulativeSum
)


DO -- match options to data type:

// Use discrete options for discrete types
let query = HKStatisticsQueryDescriptor(
    predicate: heartRatePredicate,
    options: .discreteAverage
)

Review Checklist
 HKHealthStore.isHealthDataAvailable() checked before any HealthKit access
 Only necessary data types requested in authorization
 Info.plist includes NSHealthShareUsageDescription and/or NSHealthUpdateUsageDescription
 HealthKit capability enabled in Xcode project
 Authorization denial handled gracefully (nil results, not crashes)
 Single HKHealthStore instance reused (not created per query)
 Async query descriptors used instead of callback-based queries
 Heavy queries not blocking main thread
 Statistics options match data type (cumulative vs. discrete)
 Background delivery paired with HKObserverQuery and completionHandler called
 Background delivery entitlement enabled if using enableBackgroundDelivery
 Workout sessions properly ended and builder finalized
 Write operations only for sample types the app created
References
Extended patterns (workouts, anchored queries, SwiftUI integration): references/healthkit-patterns.md
HealthKit framework
HKHealthStore
HKSampleQueryDescriptor
HKStatisticsQueryDescriptor
HKStatisticsCollectionQueryDescriptor
HKWorkoutSession
HKLiveWorkoutBuilder
Setting up HealthKit
Authorizing access to health data
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