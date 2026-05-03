---
rating: ⭐⭐
title: mapkit
url: https://skills.sh/dpearson2699/swift-ios-skills/mapkit
---

# mapkit

skills/dpearson2699/swift-ios-skills/mapkit
mapkit
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill mapkit
SKILL.md
MapKit

Build map-based and location-aware features targeting iOS 17+ with SwiftUI MapKit and modern CoreLocation async APIs. Use Map with MapContentBuilder for views, CLLocationUpdate.liveUpdates() for streaming location, and CLMonitor for geofencing.

See references/mapkit-patterns.md for extended MapKit patterns and references/mapkit-corelocation-patterns.md for CoreLocation patterns.

Contents
Workflow
SwiftUI Map View (iOS 17+)
CoreLocation Modern API
Geocoding
Search
Directions
PlaceDescriptor (iOS 26+)
Common Mistakes
Review Checklist
References
Workflow
1. Add a map with markers or annotations
Import MapKit.
Create a Map view with optional MapCameraPosition binding.
Add Marker, Annotation, MapPolyline, MapPolygon, or MapCircle inside the MapContentBuilder closure.
Configure map style with .mapStyle().
Add map controls with .mapControls { }.
Handle selection with a selection: binding.
2. Track user location
Add NSLocationWhenInUseUsageDescription to Info.plist.
On iOS 18+, create a CLServiceSession to manage authorization.
Iterate CLLocationUpdate.liveUpdates() in a Task.
Filter updates by distance or accuracy before updating the UI.
Stop the task when location tracking is no longer needed.
3. Search for places
Configure MKLocalSearchCompleter for autocomplete suggestions.
Debounce user input (at least 300ms) before setting the query.
Convert selected completion to MKLocalSearch.Request for full results.
Display results as markers or in a list.
4. Get directions and display a route
Create an MKDirections.Request with source and destination MKMapItem.
Set transportType (.automobile, .walking, .transit, .cycling).
Await MKDirections.calculate().
Draw the route with MapPolyline(route.polyline).
5. Review existing map/location code

Run through the Review Checklist at the end of this file.

SwiftUI Map View (iOS 17+)
import MapKit
import SwiftUI

struct PlaceMap: View {
    @State private var position: MapCameraPosition = .automatic

    var body: some View {
        Map(position: $position) {
            Marker("Apple Park", coordinate: applePark)
            Marker("Infinite Loop", systemImage: "building.2",
                   coordinate: infiniteLoop)
        }
        .mapStyle(.standard(elevation: .realistic))
        .mapControls {
            MapUserLocationButton()
            MapCompass()
            MapScaleView()
        }
    }
}

Marker and Annotation
// Balloon marker -- simplest way to pin a location
Marker("Cafe", systemImage: "cup.and.saucer.fill", coordinate: cafeCoord)
    .tint(.brown)

// Annotation -- custom SwiftUI view at a coordinate
Annotation("You", coordinate: userCoord, anchor: .bottom) {
    Image(systemName: "figure.wave")
        .padding(6)
        .background(.blue.gradient, in: .circle)
        .foregroundStyle(.white)
}

Overlays: Polyline, Polygon, Circle
Map {
    // Polyline from coordinates
    MapPolyline(coordinates: routeCoords)
        .stroke(.blue, lineWidth: 4)

    // Polygon (area highlight)
    MapPolygon(coordinates: parkBoundary)
        .foregroundStyle(.green.opacity(0.3))
        .stroke(.green, lineWidth: 2)

    // Circle (radius around a point)
    MapCircle(center: storeCoord, radius: 500)
        .foregroundStyle(.red.opacity(0.15))
        .stroke(.red, lineWidth: 1)
}

Camera Position

MapCameraPosition controls what the map displays. Bind it to let the user interact and to programmatically move the camera.

// Center on a region
@State private var position: MapCameraPosition = .region(
    MKCoordinateRegion(
        center: CLLocationCoordinate2D(latitude: 37.334, longitude: -122.009),
        span: MKCoordinateSpan(latitudeDelta: 0.05, longitudeDelta: 0.05)
    )
)

// Follow user location
@State private var position: MapCameraPosition = .userLocation(fallback: .automatic)

// Specific camera angle (3D perspective)
@State private var position: MapCameraPosition = .camera(
    MapCamera(centerCoordinate: applePark, distance: 1000, heading: 90, pitch: 60)
)

// Frame specific items
position = .item(MKMapItem.forCurrentLocation())
position = .rect(MKMapRect(...))

Map Style
.mapStyle(.standard)                                        // Default road map
.mapStyle(.standard(elevation: .realistic, showsTraffic: true))
.mapStyle(.imagery)                                         // Satellite
.mapStyle(.imagery(elevation: .realistic))                  // 3D satellite
.mapStyle(.hybrid)                                          // Satellite + labels
.mapStyle(.hybrid(elevation: .realistic, showsTraffic: true))

Map Interaction Modes
.mapInteractionModes(.all)           // Default: pan, zoom, rotate, pitch
.mapInteractionModes(.pan)           // Pan only
.mapInteractionModes([.pan, .zoom])  // Pan and zoom
.mapInteractionModes([])             // Static map (no interaction)

Map Selection
@State private var selectedMarker: MKMapItem?

Map(selection: $selectedMarker) {
    ForEach(places) { place in
        Marker(place.name, coordinate: place.coordinate)
            .tag(place.mapItem)     // Tag must match selection type
    }
}
.onChange(of: selectedMarker) { _, newValue in
    guard let item = newValue else { return }
    // React to selection
}

CoreLocation Modern API
CLLocationUpdate.liveUpdates() (iOS 17+)

Replace CLLocationManagerDelegate callbacks with a single async sequence. Each iteration yields a CLLocationUpdate containing an optional CLLocation.

import CoreLocation

@Observable
final class LocationTracker: @unchecked Sendable {
    var currentLocation: CLLocation?
    private var updateTask: Task<Void, Never>?

    func startTracking() {
        updateTask = Task {
            let updates = CLLocationUpdate.liveUpdates()
            for try await update in updates {
                guard let location = update.location else { continue }
                // Filter by horizontal accuracy
                guard location.horizontalAccuracy < 50 else { continue }
                await MainActor.run {
                    self.currentLocation = location
                }
            }
        }
    }

    func stopTracking() {
        updateTask?.cancel()
        updateTask = nil
    }
}

CLServiceSession (iOS 18+)

Declare authorization requirements for a feature's lifetime. Hold a reference to the session for as long as you need location services.

// When-in-use authorization with full accuracy preference
let session = CLServiceSession(
    authorization: .whenInUse,
    fullAccuracyPurposeKey: "NearbySearchPurpose"
)
// Hold `session` as a stored property; release it when done.


On iOS 18+, CLLocationUpdate.liveUpdates() and CLMonitor take an implicit CLServiceSession if you do not create one explicitly. Create one explicitly when you need .always authorization or full accuracy.

Authorization Flow
// Info.plist keys (required):
// NSLocationWhenInUseUsageDescription
// NSLocationAlwaysAndWhenInUseUsageDescription (only if .always needed)

// Check authorization and guide user to Settings when denied
struct LocationPermissionView: View {
    @Environment(\.openURL) private var openURL

    var body: some View {
        ContentUnavailableView {
            Label("Location Access Denied", systemImage: "location.slash")
        } description: {
            Text("Enable location access in Settings to use this feature.")
        } actions: {
            Button("Open Settings") {
                if let url = URL(string: UIApplication.openSettingsURLString) {
                    openURL(url)
                }
            }
        }
    }
}

Geocoding
CLGeocoder (iOS 8+)
let geocoder = CLGeocoder()

// Forward geocoding: address string -> coordinates
let placemarks = try await geocoder.geocodeAddressString("1 Apple Park Way, Cupertino")
if let location = placemarks.first?.location {
    print(location.coordinate) // CLLocationCoordinate2D
}

// Reverse geocoding: coordinates -> placemark
let location = CLLocation(latitude: 37.3349, longitude: -122.0090)
let placemarks = try await geocoder.reverseGeocodeLocation(location)
if let placemark = placemarks.first {
    let address = [placemark.name, placemark.locality, placemark.administrativeArea]
        .compactMap { $0 }
        .joined(separator: ", ")
}

MKGeocodingRequest and MKReverseGeocodingRequest (iOS 26+)

New MapKit-native geocoding that returns MKMapItem with richer data and MKAddress / MKAddressRepresentations for flexible address formatting.

@available(iOS 26, *)
func reverseGeocode(location: CLLocation) async throws -> MKMapItem? {
    guard let request = MKReverseGeocodingRequest(location: location) else {
        return nil
    }
    let mapItems = try await request.mapItems
    return mapItems.first
}

@available(iOS 26, *)
func forwardGeocode(address: String) async throws -> [MKMapItem] {
    guard let request = MKGeocodingRequest(addressString: address) else { return [] }
    return try await request.mapItems
}

Search
MKLocalSearchCompleter (Autocomplete)
@Observable
final class SearchCompleter: NSObject, MKLocalSearchCompleterDelegate {
    var results: [MKLocalSearchCompletion] = []
    var query: String = "" { didSet { completer.queryFragment = query } }

    private let completer = MKLocalSearchCompleter()

    override init() {
        super.init()
        completer.delegate = self
        completer.resultTypes = [.address, .pointOfInterest]
    }

    func completerDidUpdateResults(_ completer: MKLocalSearchCompleter) {
        results = completer.results
    }

    func completer(_ completer: MKLocalSearchCompleter, didFailWithError error: Error) {
        results = []
    }
}

MKLocalSearch (Full Search)
func search(for completion: MKLocalSearchCompletion) async throws -> [MKMapItem] {
    let request = MKLocalSearch.Request(completion: completion)
    request.resultTypes = [.pointOfInterest, .address]
    let search = MKLocalSearch(request: request)
    let response = try await search.start()
    return response.mapItems
}

// Search by natural language query within a region
func searchNearby(query: String, region: MKCoordinateRegion) async throws -> [MKMapItem] {
    let request = MKLocalSearch.Request()
    request.naturalLanguageQuery = query
    request.region = region
    let search = MKLocalSearch(request: request)
    let response = try await search.start()
    return response.mapItems
}

Directions
func getDirections(from source: MKMapItem, to destination: MKMapItem,
                   transport: MKDirectionsTransportType = .automobile) async throws -> MKRoute? {
    let request = MKDirections.Request()
    request.source = source
    request.destination = destination
    request.transportType = transport
    let directions = MKDirections(request: request)
    let response = try await directions.calculate()
    return response.routes.first
}

Display Route on Map
@State private var route: MKRoute?

Map {
    if let route {
        MapPolyline(route.polyline)
            .stroke(.blue, lineWidth: 5)
    }
    Marker("Start", coordinate: startCoord)
    Marker("End", coordinate: endCoord)
}
.task {
    route = try? await getDirections(from: startItem, to: endItem)
}

ETA Calculation
func getETA(from source: MKMapItem, to destination: MKMapItem) async throws -> TimeInterval {
    let request = MKDirections.Request()
    request.source = source
    request.destination = destination
    let directions = MKDirections(request: request)
    let response = try await directions.calculateETA()
    return response.expectedTravelTime
}

Cycling Directions (iOS 26+)
@available(iOS 26, *)
func getCyclingDirections(to destination: MKMapItem) async throws -> MKRoute? {
    let request = MKDirections.Request()
    request.source = MKMapItem.forCurrentLocation()
    request.destination = destination
    request.transportType = .cycling
    let directions = MKDirections(request: request)
    let response = try await directions.calculate()
    return response.routes.first
}

PlaceDescriptor (iOS 26+)

Create rich place references from coordinates or addresses without needing a Place ID. Requires import GeoToolbox.

@available(iOS 26, *)
func lookupPlace(name: String, coordinate: CLLocationCoordinate2D) async throws -> MKMapItem {
    let descriptor = PlaceDescriptor(
        representations: [.coordinate(coordinate)],
        commonName: name
    )
    let request = MKMapItemRequest(placeDescriptor: descriptor)
    return try await request.mapItem
}

Common Mistakes

DON'T: Request .authorizedAlways upfront — users distrust broad permissions. DO: Start with .requestWhenInUseAuthorization(), escalate to .always only when the user enables a background feature.

DON'T: Use CLLocationManagerDelegate for simple location fetches on iOS 17+. DO: Use CLLocationUpdate.liveUpdates() async stream for cleaner, more concise code.

DON'T: Keep location updates running when the map/view is not visible (drains battery). DO: Use .task { } in SwiftUI so updates cancel automatically on disappear.

DON'T: Force-unwrap CLPlacemark properties — they are all optional. DO: Use nil-coalescing: placemark.locality ?? "Unknown".

DON'T: Fire MKLocalSearchCompleter queries on every keystroke. DO: Debounce with .task(id: searchText) + Task.sleep(for: .milliseconds(300)).

DON'T: Silently fail when location authorization is denied. DO: Detect .denied status and show an alert with a Settings deep link.

DON'T: Assume geocoding always succeeds — handle empty results and network errors.

Review Checklist
 Info.plist has NSLocationWhenInUseUsageDescription with specific reason
 Authorization denial handled with Settings deep link
 CLLocationUpdate task cancelled when not needed (battery)
 Location accuracy appropriate for the use case
 Map annotations use Identifiable data with stable IDs
 Geocoding errors handled (network failure, no results)
 Search completer input debounced
 CLMonitor limited to 20 conditions, instance kept alive
 Background location uses CLBackgroundActivitySession
 Map tested with VoiceOver
 Map annotation view models and location UI updates are @MainActor-isolated
References
references/mapkit-patterns.md — Map setup, annotations, search, routes, clustering, Look Around, snapshots.
references/mapkit-corelocation-patterns.md — CLLocationUpdate, CLMonitor, CLServiceSession, background location, testing.
Weekly Installs
683
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