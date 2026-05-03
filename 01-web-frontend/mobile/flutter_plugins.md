---
rating: ⭐⭐⭐
title: flutter-plugins
url: https://skills.sh/flutter/skills/flutter-plugins
---

# flutter-plugins

skills/flutter/skills/flutter-plugins
flutter-plugins
Installation
$ npx skills add https://github.com/flutter/skills --skill flutter-plugins
Summary

Scaffolds Flutter plugins with native interop, method channels, FFI integration, and federated architectures.

Generates standard plugins, FFI plugins, or federated multi-package architectures based on native code requirements and team structure
Configures Android v2 embedding lifecycle interfaces, platform-specific native environments (Kotlin/Java, Swift/Objective-C), and method channel registration
Implements package-separated federated plugins with app-facing and platform-specific implementation packages for decoupled multi-team development
Includes decision tree logic to determine plugin type: FFI-only, method channels, combined FFI+channels, or federated setup
SKILL.md
flutter-plugin-generator
Goal

Scaffolds and configures Flutter plugin packages, handling standard method channels, FFI integrations, and federated plugin architectures. It configures platform-specific native code environments, implements Android v2 embedding lifecycle interfaces, and establishes platform interface packages.

Decision Logic

Use the following decision tree to determine the plugin architecture and template:

Does the plugin require C/C++ native code via dart:ffi?
Yes: Use --template=plugin_ffi.
Note: FFI plugins support bundling native code and method channel registration, but not method channels themselves.
No: Proceed to step 2.
Does the plugin require BOTH dart:ffi and Method Channels?
Yes: Use --template=plugin (Non-FFI). You must configure FFI manually within the standard plugin structure.
No: Proceed to step 3.
Will the plugin be developed by multiple teams or require highly decoupled platform implementations?
Yes: Implement a Package-Separated Federated Plugin (App-facing package, Platform Interface package, Platform Implementation packages).
No: Implement a standard monolithic plugin.
Instructions

Gather Plugin Requirements STOP AND ASK THE USER:

What is the plugin name?
What is the organization name (reverse domain notation, e.g., com.example)?
Which platforms should be supported (comma-separated: android,ios,web,linux,macos,windows)?
Do you need an FFI plugin or a standard Method Channel plugin?
Do you prefer Java or Kotlin for Android? Objective-C or Swift for iOS?
Should this be a federated plugin?

Generate the Plugin Package Execute the Flutter CLI command based on the user's parameters.

Standard Plugin Example:

flutter create --org com.example --template=plugin --platforms=android,ios,macos -a kotlin -i swift my_plugin


FFI Plugin Example:

flutter create --template=plugin_ffi my_ffi_plugin


Configure Federated Plugin Architecture (If Applicable) If the user requested a federated plugin, configure the pubspec.yaml of the app-facing package to endorse the platform implementations.

# App-facing pubspec.yaml
flutter:
  plugin:
    platforms:
      android:
        default_package: my_plugin_android
      windows:
        default_package: my_plugin_windows

dependencies:
  my_plugin_android: ^1.0.0
  my_plugin_windows: ^1.0.0


For the platform implementation packages, define the implements key:

# Platform implementation pubspec.yaml (e.g., my_plugin_windows)
flutter:
  plugin:
    implements: my_plugin
    platforms:
      windows:
        pluginClass: MyPlugin


Prepare Native Environments for Editing Before modifying native code, you MUST build the example app to resolve dependencies and generate necessary files.

cd my_plugin/example
flutter build apk --config-only # For Android
flutter build ios --no-codesign --config-only # For iOS
flutter build windows # For Windows


Implement Android v2 Embedding Lifecycle Modify the Android plugin class (e.g., android/src/main/kotlin/com/example/my_plugin/MyPlugin.kt). Extract logic from registerWith() into a private method shared with onAttachedToEngine(). Implement ActivityAware or ServiceAware if context is needed.

package com.example.my_plugin

import androidx.annotation.NonNull
import io.flutter.embedding.engine.plugins.FlutterPlugin
import io.flutter.embedding.engine.plugins.activity.ActivityAware
import io.flutter.embedding.engine.plugins.activity.ActivityPluginBinding
import io.flutter.plugin.common.MethodCall
import io.flutter.plugin.common.MethodChannel
import io.flutter.plugin.common.MethodChannel.MethodCallHandler
import io.flutter.plugin.common.MethodChannel.Result

class MyPlugin: FlutterPlugin, MethodCallHandler, ActivityAware {
  private lateinit var channel : MethodChannel

  override fun onAttachedToEngine(@NonNull flutterPluginBinding: FlutterPlugin.FlutterPluginBinding) {
    setupChannel(flutterPluginBinding.binaryMessenger)
  }

  // Shared private method for v1 and v2 embedding compatibility
  private fun setupChannel(messenger: BinaryMessenger) {
    channel = MethodChannel(messenger, "my_plugin")
    channel.setMethodCallHandler(this)
  }

  override fun onMethodCall(@NonNull call: MethodCall, @NonNull result: Result) {
    if (call.method == "getPlatformVersion") {
      result.success("Android ${android.os.Build.VERSION.RELEASE}")
    } else {
      result.notImplemented()
    }
  }

  override fun onDetachedFromEngine(@NonNull binding: FlutterPlugin.FlutterPluginBinding) {
    channel.setMethodCallHandler(null)
  }

  override fun onAttachedToActivity(binding: ActivityPluginBinding) {
    // Handle Activity attachment
  }

  override fun onDetachedFromActivityForConfigChanges() {}
  override fun onReattachedToActivityForConfigChanges(binding: ActivityPluginBinding) {}
  override fun onDetachedFromActivity() {}
}


Validate and Fix Run the plugin tests and analyzer to ensure the generated code is valid.

cd my_plugin
flutter analyze
flutter test


If the analyzer reports missing dependencies or unresolved native symbols, verify that step 4 (building the example app) was executed successfully. Fix any missing imports in the native code blocks.

Constraints
Never attempt to use Method Channels inside a package created with --template=plugin_ffi. If both are required, use --template=plugin.
Always build the example project (flutter build <platform>) at least once before attempting to edit or analyze native Android (build.gradle), iOS (.xcworkspace), or Windows (.sln) files.
Never leave public members undocumented in the Dart API (lib/<package_name>.dart).
Always use the v2 Android embedding (FlutterPlugin). Do not rely solely on the deprecated PluginRegistry.Registrar.
Never edit the .android or .ios directories inside a Flutter module; only edit the native code inside the plugin's android/ or ios/ directories.
Weekly Installs
956
Repository
flutter/skills
GitHub Stars
1.3K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass