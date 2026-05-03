---
title: react-native-best-practices
url: https://skills.sh/callstackincubator/agent-skills/react-native-best-practices
---

# react-native-best-practices

skills/callstackincubator/agent-skills/react-native-best-practices
react-native-best-practices
Installation
$ npx skills add https://github.com/callstackincubator/agent-skills --skill react-native-best-practices
Summary

Structured performance optimization reference for React Native apps covering FPS, bundle size, TTI, and memory.

Organized into 9 JavaScript/React guides (profiling, lists, animations, memory), 9 native optimization guides (Turbo Modules, threading, profiling), and 9 bundling guides (tree shaking, code splitting, size analysis)
Each reference follows a hybrid format with quick patterns/commands, impact ratings (CRITICAL/HIGH/MEDIUM), and deep-dive explanations with prerequisites and common pitfalls
Includes problem-to-skill mapping table for fast lookup: app jank points to FPS measurement, slow startup points to TTI measurement, large bundles point to analysis tools
Measurement-first workflow: baseline metrics before optimization, re-measure after applying fixes, validate improvement (e.g., FPS 45→60, TTI 3.2s→1.8s, bundle 2.1MB→1.6MB)
SKILL.md
React Native Best Practices
Overview

Performance optimization guide for React Native applications, covering JavaScript/React, Native (iOS/Android), and bundling optimizations. Based on Callstack's "Ultimate Guide to React Native Optimization".

Skill Format

Each reference file follows a hybrid format for fast lookup and deep understanding:

Quick Pattern: Incorrect/Correct code snippets for immediate pattern matching
Quick Command: Shell commands for process/measurement skills
Quick Config: Configuration snippets for setup-focused skills
Quick Reference: Summary tables for conceptual skills
Deep Dive: Full context with When to Use, Prerequisites, Step-by-Step, Common Pitfalls

Impact ratings: CRITICAL (fix immediately), HIGH (significant improvement), MEDIUM (worthwhile optimization)

When to Apply

Reference these guidelines when:

Debugging slow/janky UI or animations
Investigating memory leaks (JS or native)
Optimizing app startup time (TTI)
Reducing bundle or app size
Writing native modules (Turbo Modules)
Profiling React Native performance
Reviewing React Native code for performance
Security Notes
Treat shell commands in these references as local developer operations. Review them before running, prefer version-pinned tooling, and avoid piping remote scripts directly to a shell.
Treat third-party libraries and plugins as dependencies that still require normal supply-chain controls: pin versions, verify provenance, and update through your standard review process.
Treat Re.Pack code splitting as first-party artifact delivery only. Remote chunks must come from trusted HTTPS origins you control and be pinned to the current app release.
Priority-Ordered Guidelines
Priority	Category	Impact	Prefix
1	FPS & Re-renders	CRITICAL	js-*
2	Bundle Size	CRITICAL	bundle-*
3	TTI Optimization	HIGH	native-*, bundle-*
4	Native Performance	HIGH	native-*
5	Memory Management	MEDIUM-HIGH	js-*, native-*
6	Animations	MEDIUM	js-*
Quick Reference
Optimization Workflow

Follow this cycle for any performance issue: Measure → Optimize → Re-measure → Validate

Measure: Capture baseline metrics before changes. For runtime issues, prefer commit timeline, re-render counts, slow components, heaviest-commit breakdown, and startup/TTI when available. Component tree depth or count are optional context, not substitutes.
Optimize: Apply the targeted fix from the relevant reference
Re-measure: Run the same measurement to get updated metrics
Validate: Confirm improvement (e.g., FPS 45→60, TTI 3.2s→1.8s, bundle 2.1MB→1.6MB)

If metrics did not improve, revert and try the next suggested fix.

Review Guardrails
Check library versions before suggesting API-specific fixes. Example: FlashList v2 deprecates estimatedItemSize, so do not flag it as missing there.
Do not suggest useMemo or useCallback dependency changes unless behavior is demonstrably incorrect or profiling shows wasted work tied to that value.
Do not report stale closures speculatively. Show the stale read path, a repro, or profiler evidence before calling it out.
When profiling a flow, measure the target interaction itself. Do not treat component tree depth or component count as the main performance evidence.
Critical: FPS & Re-renders

Profile first:

# Open React Native DevTools
# Press 'j' in Metro, or shake device → "Open DevTools"


Common fixes:

Replace ScrollView with FlatList/FlashList for lists
Use React Compiler for automatic memoization
Use atomic state (Jotai/Zustand) to reduce re-renders
Use useDeferredValue for expensive computations
Critical: Bundle Size

Analyze bundle:

npx react-native bundle \
  --entry-file index.js \
  --bundle-output output.js \
  --platform ios \
  --sourcemap-output output.js.map \
  --dev false --minify true

npx source-map-explorer output.js --no-border-checks


Verify improvement after optimization:

# Record baseline size before changes
ls -lh output.js  # e.g., Before: 2.1 MB

# After applying fixes, re-bundle and compare
npx react-native bundle --entry-file index.js --bundle-output output.js \
  --platform ios --dev false --minify true
ls -lh output.js  # e.g., After: 1.6 MB  (24% reduction)


Common fixes:

Avoid barrel imports (import directly from source)
Remove unnecessary Intl polyfills only after checking Hermes API and method coverage
Enable tree shaking (Expo SDK 52+ or Re.Pack)
Enable R8 for Android native code shrinking
High: TTI Optimization

Measure TTI:

Use react-native-performance for markers
Only measure cold starts (exclude warm/hot/prewarm)

Common fixes:

Disable JS bundle compression on Android (enables Hermes mmap)
Use native navigation (react-native-screens)
Preload commonly-used expensive screens before navigating to them
High: Native Performance

Profile native:

iOS: Xcode Instruments → Time Profiler
Android: Android Studio → CPU Profiler

Common fixes:

Use background threads for heavy native work
Prefer async over sync Turbo Module methods
Use C++ for cross-platform performance-critical code
References

Full documentation with code examples in references/:

JavaScript/React (js-*)
File	Impact	Description
js-lists-flatlist-flashlist.md	CRITICAL	Replace ScrollView with virtualized lists
js-profile-react.md	MEDIUM	React DevTools profiling
js-measure-fps.md	HIGH	FPS monitoring and measurement
js-memory-leaks.md	MEDIUM	JS memory leak hunting
js-atomic-state.md	HIGH	Jotai/Zustand patterns
js-concurrent-react.md	HIGH	useDeferredValue, useTransition
js-react-compiler.md	HIGH	Automatic memoization
js-animations-reanimated.md	MEDIUM	Reanimated worklets
js-bottomsheet.md	HIGH	Bottom sheet optimization
js-uncontrolled-components.md	HIGH	TextInput optimization
Native (native-*)
File	Impact	Description
native-turbo-modules.md	HIGH	Building fast native modules
native-sdks-over-polyfills.md	HIGH	Native vs JS libraries
native-measure-tti.md	HIGH	TTI measurement setup
native-threading-model.md	HIGH	Turbo Module threads
native-profiling.md	MEDIUM	Xcode/Android Studio profiling
native-platform-setup.md	MEDIUM	iOS/Android tooling guide
native-view-flattening.md	MEDIUM	View hierarchy debugging
native-memory-patterns.md	MEDIUM	C++/Swift/Kotlin memory
native-memory-leaks.md	MEDIUM	Native memory leak hunting
native-android-16kb-alignment.md	CRITICAL	Third-party library alignment for Google Play
Bundling (bundle-*)
File	Impact	Description
bundle-barrel-exports.md	CRITICAL	Avoid barrel imports
bundle-analyze-js.md	CRITICAL	JS bundle visualization
bundle-tree-shaking.md	HIGH	Dead code elimination
bundle-analyze-app.md	HIGH	App size analysis
bundle-r8-android.md	HIGH	Android code shrinking
bundle-hermes-mmap.md	HIGH	Disable bundle compression
bundle-native-assets.md	HIGH	Asset catalog setup
bundle-library-size.md	MEDIUM	Evaluate dependencies
bundle-code-splitting.md	MEDIUM	Re.Pack code splitting
Searching References
# Find patterns by keyword
grep -l "reanimated" references/
grep -l "flatlist" references/
grep -l "memory" references/
grep -l "profil" references/
grep -l "tti" references/
grep -l "bundle" references/

Problem → Skill Mapping
Problem	Start With
App feels slow/janky	js-measure-fps.md → js-profile-react.md
Too many re-renders	js-profile-react.md → js-react-compiler.md
Slow startup (TTI)	native-measure-tti.md → bundle-analyze-js.md
Large app size	bundle-analyze-app.md → bundle-r8-android.md
Memory growing	js-memory-leaks.md or native-memory-leaks.md
Animation drops frames	js-animations-reanimated.md
Bottom sheet jank/re-renders	js-bottomsheet.md → js-animations-reanimated.md
List scroll jank	js-lists-flatlist-flashlist.md
TextInput lag	js-uncontrolled-components.md
Native module slow	native-turbo-modules.md → native-threading-model.md
Native library alignment issue	native-android-16kb-alignment.md
Attribution

Based on "The Ultimate Guide to React Native Optimization" by Callstack.

Weekly Installs
11.7K
Repository
callstackincuba…t-skills
GitHub Stars
1.3K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn