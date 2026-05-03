---
rating: ⭐⭐
title: mapbox-android-patterns
url: https://skills.sh/mapbox/mapbox-agent-skills/mapbox-android-patterns
---

# mapbox-android-patterns

skills/mapbox/mapbox-agent-skills/mapbox-android-patterns
mapbox-android-patterns
Installation
$ npx skills add https://github.com/mapbox/mapbox-agent-skills --skill mapbox-android-patterns
SKILL.md
Mapbox Android Integration Patterns

Official patterns for integrating Mapbox Maps SDK v11 on Android with Kotlin, Jetpack Compose, and View system.

Use this skill when:

Installing and configuring Mapbox Maps SDK for Android
Adding markers and annotations to maps
Showing user location and tracking with camera
Adding custom data (GeoJSON) to maps
Working with map styles, camera, or user interaction
Handling feature interactions and taps

Official Resources:

Android Maps Guides
API Reference
Example Apps
Installation & Setup
Requirements
Android SDK 21+
Kotlin or Java
Android Studio
Free Mapbox account
Step 1: Configure Access Token

Create app/res/values/mapbox_access_token.xml:

<?xml version="1.0" encoding="utf-8"?>
<resources xmlns:tools="http://schemas.android.com/tools">
    <string name="mapbox_access_token" translatable="false"
        tools:ignore="UnusedResources">YOUR_MAPBOX_ACCESS_TOKEN</string>
</resources>


Get your token: Sign in at mapbox.com

Step 2: Add Maven Repository

In settings.gradle.kts:

dependencyResolutionManagement {
    repositories {
        google()
        mavenCentral()
        maven {
            url = uri("https://api.mapbox.com/downloads/v2/releases/maven")
        }
    }
}

Step 3: Add Dependency

In module build.gradle.kts:

android {
    defaultConfig {
        minSdk = 21
    }
}

dependencies {
    implementation("com.mapbox.maps:android:11.18.1")
}


For Jetpack Compose:

dependencies {
    implementation("com.mapbox.maps:android:11.18.1")
    implementation("com.mapbox.extension:maps-compose:11.18.1")
}

Map Initialization
Jetpack Compose Pattern

Basic map:

import androidx.compose.runtime.*
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.ui.Modifier
import com.mapbox.maps.extension.compose.*
import com.mapbox.maps.Style
import com.mapbox.geojson.Point

@Composable
fun MapScreen() {
    MapboxMap(
        modifier = Modifier.fillMaxSize()
    ) {
        // Initialize camera via MapEffect (Style.STANDARD loads by default)
        MapEffect(Unit) { mapView ->
            // Set initial camera position
            mapView.mapboxMap.setCamera(
                CameraOptions.Builder()
                    .center(Point.fromLngLat(-122.4194, 37.7749))
                    .zoom(12.0)
                    .build()
            )
        }
    }
}


With ornaments:

MapboxMap(
    modifier = Modifier.fillMaxSize(),
    scaleBar = {
        ScaleBar(
            enabled = true,
            position = Alignment.BottomStart
        )
    },
    compass = {
        Compass(enabled = true)
    }
) {
    // Style.STANDARD loads by default
}

View System Pattern

Layout XML (activity_map.xml):

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <com.mapbox.maps.MapView
        android:id="@+id/mapView"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</androidx.constraintlayout.widget.ConstraintLayout>


Activity:

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.mapbox.maps.MapView
import com.mapbox.maps.Style
import com.mapbox.geojson.Point

class MapActivity : AppCompatActivity() {
    private lateinit var mapView: MapView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_map)

        mapView = findViewById(R.id.mapView)

        mapView.mapboxMap.setCamera(
            CameraOptions.Builder()
                .center(Point.fromLngLat(-122.4194, 37.7749))
                .zoom(12.0)
                .build()
        )

        mapView.mapboxMap.loadStyle(Style.STANDARD)
    }

    override fun onStart() {
        super.onStart()
        mapView.onStart()
    }

    override fun onStop() {
        super.onStop()
        mapView.onStop()
    }

    override fun onDestroy() {
        super.onDestroy()
        mapView.onDestroy()
    }
}

Add Markers (Point Annotations)

Point annotations are the most common way to mark locations on the map.

Jetpack Compose:

MapboxMap(modifier = Modifier.fillMaxSize()) {
    MapEffect(Unit) { mapView ->
        // Load style first
        mapView.mapboxMap.loadStyle(Style.STANDARD)

        // Create annotation manager and add markers
        val annotationManager = mapView.annotations.createPointAnnotationManager()
        val pointAnnotation = PointAnnotationOptions()
            .withPoint(Point.fromLngLat(-122.4194, 37.7749))
            .withIconImage("custom-marker")
        annotationManager.create(pointAnnotation)
    }
}

// Note: Compose doesn't have declarative PointAnnotation component
// Markers must be added imperatively via MapEffect


View System:

// Create annotation manager (once, reuse for updates)
val pointAnnotationManager = mapView.annotations.createPointAnnotationManager()

// Create marker
val pointAnnotation = PointAnnotationOptions()
    .withPoint(Point.fromLngLat(-122.4194, 37.7749))
    .withIconImage("custom-marker")

pointAnnotationManager.create(pointAnnotation)


Multiple markers:

val locations = listOf(
    Point.fromLngLat(-122.4194, 37.7749),
    Point.fromLngLat(-122.4094, 37.7849),
    Point.fromLngLat(-122.4294, 37.7649)
)

val annotations = locations.map { point ->
    PointAnnotationOptions()
        .withPoint(point)
        .withIconImage("marker")
}

pointAnnotationManager.create(annotations)

Show User Location (Display)

Step 1: Add permissions to AndroidManifest.xml:

<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />


Step 2: Request permissions and show location:

// Request permissions first (use ActivityResultContracts)

// Show location puck
mapView.location.updateSettings {
    enabled = true
    puckBearingEnabled = true
}

Performance Best Practices
Reuse Annotation Managers
// Don't create new managers repeatedly
// val manager = mapView.annotations.createPointAnnotationManager() // each call

// Create once, reuse
val pointAnnotationManager = mapView.annotations.createPointAnnotationManager()

fun updateMarkers() {
    pointAnnotationManager.deleteAll()
    pointAnnotationManager.create(markers)
}

Batch Annotation Updates
// Create all at once
pointAnnotationManager.create(allAnnotations)

// Don't create one by one in a loop

Lifecycle Management
// Always call lifecycle methods
override fun onStart() {
    super.onStart()
    mapView.onStart()
}

override fun onStop() {
    super.onStop()
    mapView.onStop()
}

override fun onDestroy() {
    super.onDestroy()
    mapView.onDestroy()
}

Use Standard Style
// Standard style is optimized and recommended
Style.STANDARD

// Use other styles only when needed for specific use cases
Style.STANDARD_SATELLITE // Satellite imagery

Troubleshooting
Map Not Displaying

Check:

Token in mapbox_access_token.xml
Token is valid (test at mapbox.com)
Maven repository configured
Dependency added correctly
Internet permission in manifest
Style Not Loading
mapView.mapboxMap.subscribeStyleLoaded { _ ->
    Log.d("Map", "Style loaded successfully")
    // Add layers and sources here
}

Performance Issues
Use Style.STANDARD (recommended and optimized)
Limit visible annotations to viewport
Reuse annotation managers
Avoid frequent style reloads
Call lifecycle methods (onStart, onStop, onDestroy)
Batch annotation updates
Reference Files

Load these references when you need detailed patterns for specific topics:

references/compose.md -- Jetpack Compose: dependencies, token setup, MapboxMap, annotations with click, GeoJSON, MapEffect
references/annotations.md -- Circle, Polyline, and Polygon annotation patterns
references/location-tracking.md -- Camera follow user location + get current location once
references/custom-data.md -- GeoJSON sources and layers: lines, polygons, points, update/remove
references/camera-styles.md -- Camera control (set, animate, fit) + map styles (built-in and custom)
references/interactions.md -- Featureset interactions, custom layer taps, long press, gestures
Additional Resources
Android Maps Guides
API Reference
Interactions Guide
Jetpack Compose Guide
Example Apps
Migration Guide (v10 -> v11)
Weekly Installs
437
Repository
mapbox/mapbox-a…t-skills
GitHub Stars
48
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass