---
rating: ⭐⭐
title: expo-react-native-performance
url: https://skills.sh/pproenca/dot-skills/expo-react-native-performance
---

# expo-react-native-performance

skills/pproenca/dot-skills/expo-react-native-performance
expo-react-native-performance
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill expo-react-native-performance
SKILL.md
Expo React Native Performance Best Practices

Comprehensive performance optimization guide for Expo React Native applications. Contains 42 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

When to Apply

Reference these guidelines when:

Writing new React Native components or screens
Implementing lists with FlatList or FlashList
Adding animations or transitions
Optimizing images and asset loading
Reviewing code for performance issues
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	App Startup & Bundle Size	CRITICAL	startup-
2	List Virtualization	CRITICAL	list-
3	Re-render Optimization	HIGH	rerender-
4	Animation Performance	HIGH	anim-
5	Image & Asset Loading	MEDIUM-HIGH	asset-
6	Memory Management	MEDIUM	mem-
7	Async & Data Fetching	MEDIUM	async-
8	Platform Optimizations	LOW-MEDIUM	platform-
Quick Reference
1. App Startup & Bundle Size (CRITICAL)
startup-enable-hermes - Enable Hermes JavaScript engine
startup-remove-console-logs - Remove console logs in production
startup-splash-screen-control - Control splash screen visibility
startup-preload-assets - Preload critical assets during splash
startup-async-routes - Use async routes for code splitting
startup-cherry-pick-imports - Use direct imports instead of barrel files
2. List Virtualization (CRITICAL)
list-use-flashlist - Use FlashList instead of FlatList
list-estimated-item-size - Provide accurate estimatedItemSize
list-get-item-type - Use getItemType for mixed lists
list-stable-render-item - Stabilize renderItem with useCallback
list-get-item-layout - Provide getItemLayout for fixed heights
list-memoize-items - Memoize list item components
3. Re-render Optimization (HIGH)
rerender-use-memo-expensive - Memoize expensive computations
rerender-use-callback-handlers - Stabilize callbacks with useCallback
rerender-functional-setstate - Use functional setState updates
rerender-lazy-state-init - Use lazy state initialization
rerender-split-context - Split context by update frequency
rerender-derive-state - Derive state instead of syncing
4. Animation Performance (HIGH)
anim-use-native-driver - Enable native driver for animations
anim-use-reanimated - Use Reanimated for complex animations
anim-layout-animation - Use LayoutAnimation for simple transitions
anim-transform-not-dimensions - Animate transform instead of dimensions
anim-interaction-manager - Defer heavy work during animations
5. Image & Asset Loading (MEDIUM-HIGH)
asset-use-expo-image - Use expo-image for image loading
asset-prefetch-images - Prefetch images before display
asset-optimize-image-size - Request appropriately sized images
asset-use-webp-format - Use WebP format for images
asset-recycling-key - Use recyclingKey in FlashList images
6. Memory Management (MEDIUM)
mem-cleanup-subscriptions - Clean up subscriptions in useEffect
mem-clear-timers - Clear timers on unmount
mem-abort-fetch - Abort fetch requests on unmount
mem-avoid-inline-objects - Avoid inline objects in props
mem-limit-list-data - Limit list data in memory
7. Async & Data Fetching (MEDIUM)
async-parallel-fetching - Fetch independent data in parallel
async-defer-await - Defer await until value needed
async-batch-api-calls - Batch related API calls
async-cache-responses - Cache API responses locally
async-refetch-on-focus - Refetch data on screen focus
8. Platform Optimizations (LOW-MEDIUM)
platform-android-overdraw - Reduce Android overdraw
platform-ios-text-rendering - Optimize iOS text rendering
platform-android-proguard - Enable ProGuard for Android release
platform-conditional-render - Platform-specific optimizations
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Full Compiled Document

For the complete guide with all rules expanded, see AGENTS.md.

Reference Files
File	Description
AGENTS.md	Complete compiled guide with all rules
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
556
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass