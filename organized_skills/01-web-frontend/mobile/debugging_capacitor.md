---
rating: ⭐⭐⭐
title: debugging-capacitor
url: https://skills.sh/cap-go/capgo-skills/debugging-capacitor
---

# debugging-capacitor

skills/cap-go/capgo-skills/debugging-capacitor
debugging-capacitor
Installation
$ npx skills add https://github.com/cap-go/capgo-skills --skill debugging-capacitor
SKILL.md
Debugging Capacitor Applications

Complete guide to debugging Capacitor apps on iOS and Android.

When to Use This Skill
User reports app crashes
User needs to debug WebView/JavaScript
User needs to debug native code
User has network/API issues
User sees unexpected behavior
User asks how to debug
Quick Reference: Debugging Tools
Platform	WebView Debug	Native Debug	Logs
iOS	Safari Web Inspector	Xcode Debugger	Console.app
Android	Chrome DevTools	Android Studio	adb logcat
WebView Debugging
iOS: Safari Web Inspector

Enable on device:

Settings > Safari > Advanced > Web Inspector: ON
Settings > Safari > Advanced > JavaScript: ON

Enable in Xcode (capacitor.config.ts):

const config: CapacitorConfig = {
  ios: {
    webContentsDebuggingEnabled: true, // Required for iOS 16.4+
  },
};


Connect Safari:

Open Safari on Mac
Develop menu > [Device Name] > [App Name]
If no Develop menu: Safari > Settings > Advanced > Show Develop menu

Debug:

Console: View JavaScript logs
Network: Inspect API calls
Elements: Inspect DOM
Sources: Set breakpoints
Android: Chrome DevTools
Enable in config (capacitor.config.ts):
const config: CapacitorConfig = {
  android: {
    webContentsDebuggingEnabled: true,
  },
};


Connect Chrome:

Open Chrome on computer
Navigate to chrome://inspect
Your device/emulator should appear
Click "inspect" under your app

Debug features:

Console: JavaScript logs
Network: API requests
Performance: Profiling
Application: Storage, cookies
Remote Debugging with VS Code

Install "Debugger for Chrome" extension:

// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "chrome",
      "request": "attach",
      "name": "Attach to Android WebView",
      "port": 9222,
      "webRoot": "${workspaceFolder}/dist"
    }
  ]
}

Native Debugging
iOS: Xcode Debugger
Open in Xcode:
npx cap open ios


Set breakpoints:

Click line number in Swift/Obj-C files
Or use breakpoint set --name methodName in LLDB

Run with debugger:

Product > Run (Cmd + R)
Or click Play button

LLDB Console commands:

# Print variable
po myVariable

# Print object description
p myObject

# Continue execution
continue

# Step over
next

# Step into
step

# Print backtrace
bt

View crash logs:
Window > Devices and Simulators
Select device > View Device Logs
Android: Android Studio Debugger
Open in Android Studio:
npx cap open android


Attach debugger:

Run > Attach Debugger to Android Process
Select your app

Set breakpoints:

Click line number in Java/Kotlin files

Debug console:

# Evaluate expression
myVariable

# Run method
myObject.toString()

Logcat shortcuts:
View > Tool Windows > Logcat
Filter by package: package:com.yourapp
Console Logging
JavaScript Side
// Basic logging
console.log('Debug info:', data);
console.warn('Warning:', issue);
console.error('Error:', error);

// Grouped logs
console.group('API Call');
console.log('URL:', url);
console.log('Response:', response);
console.groupEnd();

// Table format
console.table(arrayOfObjects);

// Timing
console.time('operation');
// ... operation
console.timeEnd('operation');

Native Side (iOS)
import os.log

let logger = Logger(subsystem: "com.yourapp", category: "MyPlugin")

// Log levels
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")

// With data
logger.info("User ID: \(userId)")

// Legacy NSLog (shows in Console.app)
NSLog("Legacy log: %@", message)

Native Side (Android)
import android.util.Log

// Log levels
Log.v("MyPlugin", "Verbose message")
Log.d("MyPlugin", "Debug message")
Log.i("MyPlugin", "Info message")
Log.w("MyPlugin", "Warning message")
Log.e("MyPlugin", "Error message")

// With exception
Log.e("MyPlugin", "Error occurred", exception)

Common Issues and Solutions
Issue: App Crashes on Startup

Diagnosis:

# iOS - Check crash logs
xcrun simctl spawn booted log stream --level debug | grep -i crash

# Android - Check logcat
adb logcat *:E | grep -i "fatal\|crash"


Common causes:

Missing plugin registration
Invalid capacitor.config
Missing native dependencies

Solution checklist:

 Run npx cap sync
 iOS: cd ios/App && pod install
 Check Info.plist permissions
 Check AndroidManifest.xml permissions
Issue: Plugin Method Not Found

Error: Error: "MyPlugin" plugin is not implemented on ios/android

Diagnosis:

import { Capacitor } from '@capacitor/core';

// Check if plugin exists
console.log('Plugins:', Capacitor.Plugins);
console.log('MyPlugin available:', !!Capacitor.Plugins.MyPlugin);


Solutions:

Ensure plugin is installed: npm install @capgo/plugin-name
Run sync: npx cap sync
Check plugin is registered (native code)
Issue: Network Requests Failing

Diagnosis:

// Add request interceptor
const originalFetch = window.fetch;
window.fetch = async (...args) => {
  console.log('Fetch:', args[0]);
  try {
    const response = await originalFetch(...args);
    console.log('Response status:', response.status);
    return response;
  } catch (error) {
    console.error('Fetch error:', error);
    throw error;
  }
};


Common causes:

iOS ATS blocking HTTP: Add to Info.plist:
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>

Android cleartext blocked: Add to capacitor.config.ts:
server: {
  cleartext: true, // Only for development!
}

CORS issues: Use native HTTP:
import { CapacitorHttp } from '@capacitor/core';

const response = await CapacitorHttp.request({
  method: 'GET',
  url: 'https://api.example.com/data',
});

Issue: Permission Denied

Diagnosis:

import { Permissions } from '@capacitor/core';

// Check permission status
const status = await Permissions.query({ name: 'camera' });
console.log('Camera permission:', status.state);


iOS: Check Info.plist has usage descriptions:

<key>NSCameraUsageDescription</key>
<string>We need camera access to scan documents</string>


Android: Check AndroidManifest.xml:

<uses-permission android:name="android.permission.CAMERA" />

Issue: White Screen on Launch

Diagnosis:

Check WebView console for errors (Safari/Chrome)
Check if dist/ folder exists
Verify webDir in capacitor.config.ts

Solutions:

# Rebuild web assets
npm run build

# Sync to native
npx cap sync

# Check config
cat capacitor.config.ts

Issue: Deep Links Not Working

Diagnosis:

import { App } from '@capacitor/app';

App.addListener('appUrlOpen', (event) => {
  console.log('Deep link:', event.url);
});


iOS: Check Associated Domains entitlement and apple-app-site-association file.

Android: Check intent filters in AndroidManifest.xml.

Performance Debugging
JavaScript Performance
// Mark performance
performance.mark('start');
// ... operation
performance.mark('end');
performance.measure('operation', 'start', 'end');

const measures = performance.getEntriesByName('operation');
console.log('Duration:', measures[0].duration);

iOS Performance (Instruments)
Product > Profile (Cmd + I)
Choose template:
Time Profiler: CPU usage
Allocations: Memory usage
Network: Network activity
Android Performance (Profiler)
View > Tool Windows > Profiler
Select:
CPU: Method tracing
Memory: Heap analysis
Network: Request timeline
Memory Debugging
JavaScript Memory Leaks

Use Chrome DevTools Memory tab:

Take heap snapshot
Perform action
Take another snapshot
Compare snapshots
iOS Memory (Instruments)
# Run with Leaks instrument
xcrun instruments -t Leaks -D output.trace YourApp.app

Android Memory (LeakCanary)

Add to build.gradle:

debugImplementation 'com.squareup.leakcanary:leakcanary-android:2.12'

Debugging Checklist

When debugging issues:

 Check WebView console (Safari/Chrome DevTools)
 Check native logs (Xcode Console/Logcat)
 Verify plugin is installed and synced
 Check permissions (Info.plist/AndroidManifest)
 Test on real device (not just simulator)
 Try clean build (rm -rf node_modules && npm install)
 Verify capacitor.config.ts settings
 Check for version mismatches (capacitor packages)
Resources
Capacitor Debugging Guide: https://capacitorjs.com/docs/guides/debugging
Safari Web Inspector: https://webkit.org/web-inspector
Chrome DevTools: https://developer.chrome.com/docs/devtools
Xcode Debugging: https://developer.apple.com/documentation/xcode/debugging
Android Studio Debugging: https://developer.android.com/studio/debug
Weekly Installs
199
Repository
cap-go/capgo-skills
GitHub Stars
31
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass