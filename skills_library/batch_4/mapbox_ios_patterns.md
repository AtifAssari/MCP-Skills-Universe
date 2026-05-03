---
title: mapbox-ios-patterns
url: https://skills.sh/mapbox/mapbox-agent-skills/mapbox-ios-patterns
---

# mapbox-ios-patterns

skills/mapbox/mapbox-agent-skills/mapbox-ios-patterns
mapbox-ios-patterns
Installation
$ npx skills add https://github.com/mapbox/mapbox-agent-skills --skill mapbox-ios-patterns
SKILL.md
Mapbox iOS Integration Patterns

Official patterns for integrating Mapbox Maps SDK v11 on iOS with Swift, SwiftUI, and UIKit.

Use this skill when:

Installing and configuring Mapbox Maps SDK for iOS
Adding markers and annotations to maps
Showing user location and tracking with camera
Adding custom data (GeoJSON) to maps
Working with map styles, camera, or user interaction
Handling feature interactions and taps

Official Resources:

iOS Maps Guides
API Reference
Example Apps
Installation & Setup
Requirements
iOS 12+
Xcode 15+
Swift 5.9+
Free Mapbox account
Step 1: Configure Access Token

Add your public token to Info.plist:

<key>MBXAccessToken</key>
<string>pk.your_mapbox_token_here</string>


Get your token: Sign in at mapbox.com

Step 2: Add Swift Package Dependency
File → Add Package Dependencies
Enter URL: https://github.com/mapbox/mapbox-maps-ios.git
Version: "Up to Next Major" from 11.0.0
Verify four dependencies appear: MapboxCommon, MapboxCoreMaps, MapboxMaps, Turf

Alternative: CocoaPods or direct download (install guide)

Map Initialization
SwiftUI Pattern (iOS 13+)

Basic map:

import SwiftUI
import MapboxMaps

struct ContentView: View {
    @State private var viewport: Viewport = .camera(
        center: CLLocationCoordinate2D(latitude: 37.7749, longitude: -122.4194),
        zoom: 12
    )

    var body: some View {
        Map(viewport: $viewport)
            .mapStyle(.standard)
    }
}


With ornaments:

Map(viewport: $viewport)
    .mapStyle(.standard)
    .ornamentOptions(OrnamentOptions(
        scaleBar: .init(visibility: .visible),
        compass: .init(visibility: .adaptive),
        logo: .init(position: .bottomLeading)
    ))

UIKit Pattern
import UIKit
import MapboxMaps

class MapViewController: UIViewController {
    private var mapView: MapView!

    override func viewDidLoad() {
        super.viewDidLoad()

        let options = MapInitOptions(
            cameraOptions: CameraOptions(
                center: CLLocationCoordinate2D(latitude: 37.7749, longitude: -122.4194),
                zoom: 12
            )
        )

        mapView = MapView(frame: view.bounds, mapInitOptions: options)
        mapView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        view.addSubview(mapView)

        mapView.mapboxMap.loadStyle(.standard)
    }
}

Add Markers (Point Annotations)

Point annotations are the most common way to mark locations on the map.

SwiftUI:

Map(viewport: $viewport) {
    PointAnnotation(coordinate: CLLocationCoordinate2D(latitude: 37.7749, longitude: -122.4194))
        .iconImage("custom-marker")
}


UIKit:

// Create annotation manager (once, reuse for updates)
var pointAnnotationManager = mapView.annotations.makePointAnnotationManager()

// Create marker
var annotation = PointAnnotation(coordinate: CLLocationCoordinate2D(latitude: 37.7749, longitude: -122.4194))
annotation.image = .init(image: UIImage(named: "marker")!, name: "marker")
annotation.iconAnchor = .bottom

// Add to map
pointAnnotationManager.annotations = [annotation]


Multiple markers:

let locations = [
    CLLocationCoordinate2D(latitude: 37.7749, longitude: -122.4194),
    CLLocationCoordinate2D(latitude: 37.7849, longitude: -122.4094),
    CLLocationCoordinate2D(latitude: 37.7649, longitude: -122.4294)
]

let annotations = locations.map { coordinate in
    var annotation = PointAnnotation(coordinate: coordinate)
    annotation.image = .init(image: UIImage(named: "marker")!, name: "marker")
    return annotation
}

pointAnnotationManager.annotations = annotations

Show User Location

Step 1: Add location permission to Info.plist:

<key>NSLocationWhenInUseUsageDescription</key>
<string>Show your location on the map</string>


Step 2: Request permissions and show location:

import CoreLocation

// Request permissions
let locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()

// Show user location puck
mapView.location.options.puckType = .puck2D()
mapView.location.options.puckBearingEnabled = true

Performance Best Practices
Reuse Annotation Managers
// ❌ Don't create new managers repeatedly
func updateMarkers() {
    let manager = mapView.annotations.makePointAnnotationManager()
    manager.annotations = markers
}

// ✅ Create once, reuse
let pointAnnotationManager: PointAnnotationManager

init() {
    pointAnnotationManager = mapView.annotations.makePointAnnotationManager()
}

func updateMarkers() {
    pointAnnotationManager.annotations = markers
}

Batch Annotation Updates
// ✅ Update all at once
pointAnnotationManager.annotations = newAnnotations

// ❌ Don't update one by one
for annotation in newAnnotations {
    pointAnnotationManager.annotations.append(annotation)
}

Memory Management
// Use weak self in closures
mapView.gestures.onMapTap.observe { [weak self] context in
    self?.handleTap(context.coordinate)
}.store(in: &cancelables)

// Clean up on deinit
deinit {
    cancelables.forEach { $0.cancel() }
}

Use Standard Style
// ✅ Standard style is optimized and recommended
.mapStyle(.standard)

// Use other styles only when needed for specific use cases
.mapStyle(.standardSatellite) // Satellite imagery

Troubleshooting
Map Not Displaying

Check:

✅ MBXAccessToken in Info.plist
✅ Token is valid (test at mapbox.com)
✅ MapboxMaps framework imported
✅ MapView added to view hierarchy
✅ Correct frame/constraints set
Style Not Loading
mapView.mapboxMap.onStyleLoaded.observe { [weak self] _ in
    print("Style loaded successfully")
    // Add layers and sources here
}.store(in: &cancelables)

Performance Issues
Use .standard style (recommended and optimized)
Limit visible annotations to viewport
Reuse annotation managers
Avoid frequent style reloads
Batch annotation updates
Reference Files

Load these references when the task requires deeper patterns:

references/annotations.md — Circle, Polyline, Polygon Annotations
references/location-tracking.md — Camera Follow User + Get Current Location
references/custom-data.md — GeoJSON: Lines, Polygons, Points, Update/Remove
references/camera-styles.md — Camera Control + Map Styles
references/interactions.md — Featureset Interactions, Custom Layer Taps, Long Press, Gestures
Additional Resources
iOS Maps Guides
API Reference
Interactions Guide
SwiftUI User Guide
Example Apps
Migration Guide (v10 → v11)
Weekly Installs
463
Repository
mapbox/mapbox-a…t-skills
GitHub Stars
48
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass