---
title: mobile-app-debugging
url: https://skills.sh/secondsky/claude-skills/mobile-app-debugging
---

# mobile-app-debugging

skills/secondsky/claude-skills/mobile-app-debugging
mobile-app-debugging
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill mobile-app-debugging
SKILL.md
Mobile App Debugging

Debug mobile applications across iOS, Android, and cross-platform frameworks.

iOS Debugging (Xcode)
// Breakpoint with condition
// Right-click breakpoint > Edit > Condition: userId == "123"

// LLDB commands
po variable          // Print object
p expression         // Evaluate expression
bt                   // Backtrace

Memory Debugging
Use Memory Graph Debugger to find retain cycles
Enable Zombie Objects for use-after-free bugs
Profile with Instruments > Leaks
Android Debugging (Android Studio)
// Logcat filtering
Log.d("TAG", "Debug message")
Log.e("TAG", "Error", exception)

// Filter: tag:MyApp level:error

Common Issues
ANR: Check main thread blocking
OOM: Profile with Memory Profiler
Layout issues: Use Layout Inspector
React Native
// Remote debugging
// Shake device > Debug JS Remotely

// Console logging
console.log('Debug:', variable);
console.warn('Warning');
console.error('Error');

// Performance Monitor
// Shake > Show Perf Monitor
// Target: 60 FPS, <16ms per frame

Network Debugging
// Intercept requests
XMLHttpRequest.prototype._send = XMLHttpRequest.prototype.send;
XMLHttpRequest.prototype.send = function() {
  console.log('Request:', this._url);
  this._send.apply(this, arguments);
};

Debug Checklist
 Test on physical devices (not just simulators)
 Test on older device models
 Simulate slow 3G network
 Test offline mode
 Check memory under load
 Test rotation and safe areas
 Verify 60 FPS target
Performance Targets
Metric	Target
Frame rate	60 FPS (16ms/frame)
Memory	<100MB
App launch	<2 seconds
Weekly Installs
174
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass