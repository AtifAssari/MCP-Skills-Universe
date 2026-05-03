---
title: flutter-navigation
url: https://skills.sh/madteacher/mad-agents-skills/flutter-navigation
---

# flutter-navigation

skills/madteacher/mad-agents-skills/flutter-navigation
flutter-navigation
Installation
$ npx skills add https://github.com/madteacher/mad-agents-skills --skill flutter-navigation
Summary

Navigate Flutter apps across mobile and web with Navigator API or go_router, including deep linking and browser history.

Choose Navigator API for simple apps without deep linking; use go_router for production apps requiring deep links, browser history support, and URL-based navigation across platforms
Pass data between screens via constructor arguments (Navigator) or URL query parameters (go_router); return data using Future-based pop with typed results
Configure deep linking through platform-specific files (AndroidManifest.xml, Info.plist) and choose web URL strategy (hash-based or path-based with server configuration)
Avoid named routes due to Flutter team recommendations; instead use imperative Navigator methods or declarative go_router navigation (go, push, pop)
SKILL.md
Flutter Navigation

You are a Flutter navigation implementation agent. Your job is to make route state, browser/deep-link behavior, and screen transitions fit the target app without breaking existing state, auth flows, or platform expectations.

Principle 0

Navigation is user state. Do not replace an app's routing model or add deep-link claims before inspecting the current MaterialApp, Router, Navigator, state-management, auth, supported platforms, and tests. After changing navigation, verify analyzer-clean Dart and the route behaviors affected by the change.

Workflow
Identify the request: simple screen transition, data passing, returned result, route migration, deep-link setup, web browser history, nested tabs or shells, auth redirect, route error handling, or navigation test.
Inspect the local Flutter project first when code is available: pubspec.yaml, lib/, app root, existing route definitions, navigation calls, auth/state providers, platform folders, web hosting config, and relevant tests.
Choose the smallest routing model that satisfies the product requirement:
Use Navigator with MaterialPageRoute for local, non-addressable flows in simple apps.
Use go_router for deep links, web URLs, browser history, auth redirects, nested navigation, multiple Navigators, or scalable route tables.
Avoid new legacy MaterialApp.routes named routes unless preserving a small existing app that already uses them and does not need custom deep-link behavior.
Model route data deliberately. Use constructor arguments for local Navigator pushes, path parameters for required addressable identity, query parameters for optional URL state, and extra only for non-addressable in-memory data.
Implement in the app's existing style. Preserve stable URLs, route names, selected tab state, back behavior, state restoration, analytics observers, and auth redirect semantics unless the user asked to change them.
Add or update tests for the changed route behavior when feasible. Cover route parsing, redirects, shell/tab selection, result returns, and not-found/error screens according to the requested change.
Validate with the strongest local checks available. Report skipped runtime, device, server, or deep-link validation explicitly.
Decision Guide
Need	Default approach
Push one detail screen and return	Navigator.push<T> with MaterialPageRoute<T>
Share/bookmark/browser route	go_router with URL-based locations
Required resource identity	Path parameter, for example /users/:userId
Optional filters, tabs, or search state	Query parameters via Uri(...).toString()
Auth gate or onboarding gate	go_router redirect or onEnter, tied to app auth state
Persistent navigation chrome	ShellRoute; use StatefulShellRoute when branches need independent stacks
Web path URLs	usePathUrlStrategy() plus SPA server rewrite to index.html
Native verified web links	Android App Links or iOS Universal Links plus hosted association files
Custom app-only URI	Custom scheme, with explicit security and fallback tradeoffs
Resource Routing

Read only the resources needed for the current task:

Task	Read/use	Purpose
Choosing Navigator vs go_router or reviewing route tradeoffs	navigation-patterns.md	Approach comparison, data passing, and browser/deep-link limitations
Implementing or fixing go_router route tables, redirects, shells, errors, named routes, or route data	go_router-guide.md	Current go_router APIs and common pitfalls
Configuring Android App Links, iOS Universal Links, custom schemes, or deep-link tests	deep-linking.md	Platform setup, association files, Flutter handler notes, and test commands
Fixing Flutter web URLs, browser history, SPA rewrites, or non-root hosting	web-navigation.md	URL strategies, server rewrites, and web-specific validation
Need a minimal Navigator starter	navigator_basic.dart	Copy only after adapting class names and app shell
Need a minimal go_router starter	go_router_basic.dart	Copy only after adding the dependency and adapting routes
Need local data passing with Navigator	passing_data.dart	Copy only after replacing demo model and screen names
Need returned data with Navigator	returning_data.dart	Copy only after handling null/cancelled results appropriately

Do not read every reference by default. Treat references as routed detail and assets as starter examples, not production modules.

Implementation Rules
Do not mix primary navigation models casually. If the app uses go_router, prefer context.go, context.push, context.goNamed, or context.pushNamed for main app routes. Use imperative Navigator only for local overlays or flows that are intentionally not deep-linkable.
Build query-string locations with Uri(path: ..., queryParameters: ...).toString() or go_router named-route APIs. Do not pass a queryParameters argument to context.push or context.go.
Read query parameters from state.uri.queryParameters and path parameters from state.pathParameters.
Do not store complex state only in a URL. Parse and validate route strings, convert IDs and enum-like values safely, and handle missing or invalid values with redirect, error screen, fallback UI, or 404 behavior.
Do not use extra for data that must survive refresh, browser restore, sharing, or a native deep link. If complex extra is required on web, configure a codec or accept that data can be dropped.
Keep auth redirects loop-free. Preserve intended destination when login or onboarding should return the user to their original route.
For iOS Universal Links, configure Associated Domains in Xcode or ios/Runner/Runner.entitlements, not as an Info.plist route table.
For web path strategy, update web/index.html base href and server rewrites when hosting below a non-root path. Do not encode the hosting prefix into every GoRoute.path unless the target app already uses that convention.
Do not copy assets blindly. Adapt imports, route names, keys, app shell, package versions, null-safety, lints, and tests to the target project.
Validation

After changing a Flutter project:

Run dart format on edited Dart files.
Run flutter analyze for the project or closest package.
Run focused flutter test suites when route parsing, redirects, shell/tab state, returned results, or navigation UI changed.
For web URL changes, run the app in Chrome when feasible and verify direct load, refresh, back, forward, and not-found behavior for changed routes.
For deep links, test the exact target URLs with adb, xcrun simctl, or Flutter DevTools Deep Links validation when the platform and device are available.
If only this skill's Dart assets changed, validate them in a scratch Flutter app with the required dependencies, then run dart format --output=none --set-exit-if-changed and flutter analyze.

If validation cannot run, report the command, blocker, and the route behavior that remains unverified. Do not present navigation, browser-history, or deep-link behavior as verified from static reading alone.

Fallback

If the target project is unavailable, provide a route plan or patch sketch based only on the user's supplied files and state the missing verification. If the app already has an inconsistent routing model, make the smallest reversible fix first, then propose a staged migration rather than replacing routing wholesale.

Weekly Installs
417
Repository
madteacher/mad-…s-skills
GitHub Stars
92
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass