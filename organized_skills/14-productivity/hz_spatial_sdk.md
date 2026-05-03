---
rating: ⭐⭐⭐
title: hz-spatial-sdk
url: https://skills.sh/meta-quest/agentic-tools/hz-spatial-sdk
---

# hz-spatial-sdk

skills/meta-quest/agentic-tools/hz-spatial-sdk
hz-spatial-sdk
Installation
$ npx skills add https://github.com/meta-quest/agentic-tools --skill hz-spatial-sdk
SKILL.md
Spatial SDK Skill

Build native Android spatial applications for Meta Quest using the Meta Spatial SDK. This skill covers the Entity-Component-System architecture, 2D panel rendering, 3D object placement, hybrid app development, and deployment to Horizon OS devices.

When to Use This Skill

Use this skill when you need to:

Build a native Android app for Meta Quest using the Spatial SDK and Kotlin
Create hybrid experiences that combine 2D Android UI panels with 3D content
Work with the Entity-Component-System (ECS) architecture in Spatial SDK
Add 3D objects, animations, or spatial interactions to a Quest application
Configure panels using Jetpack Compose or Android Views for spatial rendering
Use the Spatial Editor to compose 3D scenes visually
Deploy and test Spatial SDK applications on a Quest device

This skill applies to all Meta Quest headsets running Horizon OS (Quest 2, Quest 3, Quest 3S, Quest Pro).

What is Meta Spatial SDK

Meta Spatial SDK is Meta's native Android framework for building spatial applications on Horizon OS. It extends the standard Android development model with spatial capabilities, allowing developers to write apps in Kotlin that render 2D UI panels in 3D space, display glTF models, handle spatial input, and integrate with Horizon OS features like passthrough, scene understanding, and hand tracking.

Unlike Unity or Unreal Engine, Spatial SDK builds on top of the Android Activity lifecycle. Applications are standard Android APKs that use Spatial SDK libraries to gain spatial rendering and interaction capabilities.

Key characteristics:
Kotlin-first: all application logic is written in Kotlin
Android-native: builds on standard Android Activity, Gradle, and Jetpack libraries
ECS architecture: entities, components, and systems manage 3D scene state
Panel rendering: Android UI frameworks (Jetpack Compose, Views) render as spatial panels
Gradle integration: Spatial SDK ships as AAR libraries pulled via Gradle dependencies
Key Concepts
Entity-Component-System (ECS)

The Spatial SDK uses an ECS architecture to manage the 3D scene graph. This separates data (components) from behavior (systems):

Entity: a lightweight identifier (ID) that groups components together. An entity has no behavior on its own.
Component: a data container attached to an entity. Components are defined via XML attribute schemas and hold typed fields (floats, vectors, references, enums). Examples: Transform, Mesh, Panel, Grabbable.
System: a Kotlin class that queries entities by their components and executes logic each frame. Systems extend SystemBase and override the execute() method.
// Example: a simple system that rotates all entities with a Spinner component
class SpinnerSystem : SystemBase() {
  override fun execute() {
    val query = Query.where { has(Spinner.id, Transform.id) }
    for (entity in query.eval()) {
      val transform = entity.getComponent<Transform>()
      val spinner = entity.getComponent<Spinner>()
      transform.rotation *= Quaternion.fromAxisAngle(Vector3.UP, spinner.speed * getDeltaTime())
      entity.setComponent(transform)
    }
  }
}

2D Panels

Panels are the primary way to display Android UI in spatial apps. A PanelRegistration maps a panel name to a Jetpack Compose composable or an Android View. Panels render as flat rectangles positioned in 3D space.

override fun registerPanels(): List<PanelRegistration> {
  return listOf(
    PanelRegistration("main_panel") {
      layoutParams = LayoutParams(592f, 592f, SpatialPanelLayoutParams.HORIZONTAL)
      panel {
        MainScreen()  // Jetpack Compose composable
      }
    }
  )
}

3D Objects

Load glTF models as meshes and place them in the scene using Transform and Mesh components:

val modelEntity = Entity.create()
modelEntity.setComponent(
  Mesh(Uri.parse("apk:///models/robot.glb"))
)
modelEntity.setComponent(
  Transform(Pose(Vector3(0f, 1f, -2f)))
)

Hybrid Apps

Spatial SDK excels at hybrid applications that combine 2D panels with 3D content. A single activity can display Android UI panels alongside 3D models, allowing users to interact with familiar 2D interfaces while surrounded by spatial content.

Activity Structure

For most Spatial SDK apps, keep one SpatialActivity subclass as the root shell for the whole experience. Tool-style apps usually work best when that single activity owns the scene, registered panels, and ECS systems while UI states change inside that shell.

Avoid structuring a Quest-native tool app like a standard multi-activity Android app unless you have a specific platform reason. Multiple panels or different UI states are usually better expressed inside the same spatial activity.

Scene

The Scene class manages the 3D environment, including the skybox, image-based lighting (IBL), viewer position, and the reference space. Each SpatialActivity has an associated scene.

Spatial Editor

The Spatial Editor is a visual tool (integrated into Android Studio via the Meta Horizon plugin) for composing 3D scenes. It produces .glxf files that define entity arrangements, panel placements, and 3D object positions. These files are loaded at runtime.

Quick Start
Prerequisites
Android Studio with the Meta Horizon Android Studio Plugin installed
Meta Spatial SDK dependencies added to your Gradle project
A Meta Quest device connected via USB with developer mode enabled
Step-by-step

Create a new project from the Spatial SDK template in Android Studio (or add Spatial SDK dependencies to an existing project).

Define your activity by extending SpatialActivity:

class MyActivity : SpatialActivity() {

  override fun registerPanels(): List<PanelRegistration> {
    return listOf(
      PanelRegistration("home_panel") {
        layoutParams = LayoutParams(592f, 592f, SpatialPanelLayoutParams.HORIZONTAL)
        panel {
          HomeScreen()
        }
      }
    )
  }

  override fun registerSystems(): List<SystemBase> {
    return listOf(
      SpinnerSystem()
    )
  }

  override fun onSceneReady(scene: Scene) {
    super.onSceneReady(scene)
    scene.setViewerPosition(Vector3(0f, 0f, 0f))
    // Spawn panels and 3D objects here
    Entity.createPanelEntity("home_panel")
  }
}

Add 3D content via the Spatial Editor or programmatically:
// Load a 3D model
val robot = Entity.create(
  Mesh(Uri.parse("apk:///models/robot.glb")),
  Transform(Pose(Vector3(0f, 0.5f, -1.5f)))
)

Build and deploy to your connected Quest device using hzdb (invoke via npx -y @meta-quest/hzdb <args>):
# Build the APK via Gradle
./gradlew assembleDebug

# Install using hzdb
hzdb app install app/build/outputs/apk/debug/app-debug.apk

# Launch the app
hzdb app launch com.example.myspatialapp

# View logs
hzdb log

Architecture Overview

The high-level architecture of a Spatial SDK application:

Android Activity
  └── SpatialActivity
        ├── Scene (environment, lighting, viewer)
        ├── DataModel (entity-component store)
        │     ├── Entity: Panel ("home_panel")
        │     │     ├── Transform
        │     │     ├── PanelComponent
        │     │     └── Grabbable
        │     ├── Entity: 3D Object ("robot")
        │     │     ├── Transform
        │     │     └── Mesh
        │     └── Entity: Light
        │           ├── Transform
        │           └── PointLight
        ├── Systems
        │     ├── SpinnerSystem
        │     ├── IsdkSupportingSystems (input)
        │     └── PhysicsSystem
        └── PanelRegistrations
              └── "home_panel" → Jetpack Compose UI

SpatialActivity extends Android Activity and manages the Scene and DataModel lifecycle.
DataModel is the central ECS store where all entities and components live.
Scene configures the 3D environment (skybox, IBL, reference space).
Systems run each frame and operate on entities matching their queries.
PanelRegistrations bind panel names to UI content.
Gradle Dependencies

Add the Spatial SDK to your build.gradle.kts:

dependencies {
  implementation("com.meta.spatial:meta-spatial-sdk:latest")
  implementation("com.meta.spatial:meta-spatial-sdk-physics:latest")
  implementation("com.meta.spatial:meta-spatial-sdk-isdk:latest")
  implementation("com.meta.spatial:meta-spatial-sdk-mruk:latest")
}


Apply the Spatial SDK Gradle plugin for code generation:

plugins {
  id("com.meta.spatial.plugin") version "latest"
}

Manifest Configuration

Spatial SDK apps require specific manifest entries:

<uses-feature
  android:name="android.hardware.vr.headtracking"
  android:required="true" />

<!-- Include these when the app should launch and remain usable with hands,
     not only paired controllers. -->
<uses-feature
  android:name="oculus.software.handtracking"
  android:required="false" />
<uses-permission android:name="com.oculus.permission.HAND_TRACKING" />

<application>
  <activity
    android:name=".MyActivity"
    android:exported="true">
    <intent-filter>
      <action android:name="android.intent.action.MAIN" />
      <category android:name="android.intent.category.LAUNCHER" />
      <category android:name="com.oculus.intent.category.VR" />
    </intent-filter>
  </activity>
</application>


For panel or hybrid apps that should work without controllers, declare hand tracking support and make sure the experience handles switching between hands and controllers cleanly. Meta's VRC guidance applies to panel apps as well as immersive apps.

If your app needs to talk to a local development service over http:// or ws://, you may also need debug-only cleartext traffic settings or a network security config. Keep that scoped to development builds and prefer https:// and wss:// in release builds.

References
Skill References
Architecture Guide -- ECS model, custom components and systems, scene management, and activity lifecycle
Panels and 3D Objects -- 2D panel rendering, 3D object loading, hybrid app development
Interaction SDK -- Input handling, grabbables, hand tracking, controller input, haptics
Debugging -- Data Model Inspector, OVR Metrics Tool, logcat filtering, common issues
Weekly Installs
10
Repository
meta-quest/agentic-tools
GitHub Stars
31
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass