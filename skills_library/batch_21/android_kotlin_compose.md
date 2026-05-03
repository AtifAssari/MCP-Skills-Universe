---
title: android-kotlin-compose
url: https://skills.sh/drjacky/claude-android-ninja/android-kotlin-compose
---

# android-kotlin-compose

skills/drjacky/claude-android-ninja/android-kotlin-compose
android-kotlin-compose
Installation
$ npx skills add https://github.com/drjacky/claude-android-ninja --skill android-kotlin-compose
SKILL.md
Android Kotlin Compose Development

Create production-quality Android applications following Google's official architecture guidance and best practices. Use when building Android apps with Kotlin, Jetpack Compose, MVVM architecture, Hilt dependency injection, Room database, or Android multi-module projects. Triggers on requests to create Android projects, screens, ViewModels, repositories, feature modules, or when asked about Android architecture patterns.

Quick Reference
Task	Reference File
Project structure & modules	modularization.md
Architecture layers (Presentation, Domain, Data, UI)	architecture.md
Compose patterns, animation, effects, modifiers	compose-patterns.md
Accessibility & TalkBack support	android-accessibility.md
Notifications & foreground services	android-notifications.md
Data sync & offline-first patterns	android-data-sync.md
Material 3 theming & dynamic colors	android-theming.md
Navigation3 & adaptive navigation	android-navigation.md
Kotlin best practices	kotlin-patterns.md
Coroutines best practices	coroutines-patterns.md
Gradle & build configuration	gradle-setup.md
Testing approach	testing.md
Internationalization & localization	android-i18n.md
Icons, graphics, and custom drawing	android-graphics.md
Runtime permissions	android-permissions.md
Kotlin delegation patterns	kotlin-delegation.md
Crash reporting	crashlytics.md
StrictMode guardrails	android-strictmode.md
Multi-module dependencies	dependencies.md
Code quality (Detekt)	code-quality.md
Code coverage (JaCoCo)	android-code-coverage.md
Security (encryption, biometrics, pinning)	android-security.md
Design patterns	design-patterns.md
Android performance, recomposition & app startup	android-performance.md
Debugging (Logcat, ANR, R8, memory leaks)	android-debugging.md
Migration guides (XML, RxJava, Navigation, Compose)	migration.md
Workflow Decision Tree

Creating a new project? → Start with assets/settings.gradle.kts.template for settings and module includes
→ Start with assets/libs.versions.toml.template for the version catalog
→ Copy all files from assets/convention/ to build-logic/convention/src/main/kotlin/
→ Create build-logic/settings.gradle.kts (see assets/convention/QUICK_REFERENCE.md)
→ Add includeBuild("build-logic") to root settings.gradle.kts
→ Add plugin entries to gradle/libs.versions.toml (see assets/convention/QUICK_REFERENCE.md) → Copy assets/proguard-rules.pro.template to app/proguard-rules.pro → Read modularization.md for structure and module types
→ Use gradle-setup.md for build files and build logic

Configuring Gradle/build files? → Use gradle-setup.md for module build.gradle.kts patterns
→ Use gradle-setup.md → "Build Performance" for optimization workflow, diagnostics, and bottleneck troubleshooting
→ Copy convention plugins from assets/convention/ to build-logic/ in your project
→ See assets/convention/QUICK_REFERENCE.md for setup instructions and examples
→ Copy assets/proguard-rules.pro.template to app/proguard-rules.pro for R8 rules

Setting up code quality / Detekt? → Use code-quality.md for Detekt convention plugin setup
→ Start from assets/detekt.yml.template for rules and enable Compose rules

Adding or updating dependencies? → Follow dependencies.md
→ Update assets/libs.versions.toml.template if the dependency is missing

Adding a new feature/module? → Follow module naming in modularization.md
→ Implement Presentation in the feature module
→ Follow dependency flow: Feature → Core/Domain → Core/Data

Building UI screens/components? → Read compose-patterns.md for screen architecture, state, components, modifiers
→ Use android-theming.md for Material 3 colors, typography, and shapes
→ Always align Kotlin code with kotlin-patterns.md
→ Create Screen + ViewModel + UiState in the feature module
→ Use shared components from core/ui when possible

Setting up app theme (colors, typography, shapes)? → Follow android-theming.md for Material 3 theming and dynamic colors
→ Use semantic color roles from MaterialTheme.colorScheme (never hardcoded colors)
→ Support light/dark themes with user preference toggle
→ Enable dynamic color (Material You) for API 31+

Writing any Kotlin code? → Always follow kotlin-patterns.md
→ Ensure practices align with architecture.md, modularization.md, and compose-patterns.md

Setting up data/domain layers? → Read architecture.md
→ Create Repository interfaces in core/domain → Implement Repository in core/data → Create DataSource + DAO in core/data

Implementing offline-first or data synchronization? → Follow android-data-sync.md for sync strategies, conflict resolution, and cache invalidation
→ Use Room as single source of truth with sync metadata (syncStatus, lastModified)
→ Schedule background sync with WorkManager
→ Monitor network state before syncing

Setting up navigation? → Follow android-navigation.md for Navigation3 architecture, state management, and adaptive navigation
→ See modularization.md for feature module navigation components (Destination, Navigator, Graph)
→ Configure navigation graph in the app module
→ Use feature navigation destinations and navigator interfaces

Adding tests? → Use testing.md for patterns and examples
→ Use testing.md → "Screenshot Testing" for Compose Preview Screenshot Testing setup
→ Keep test doubles in core/testing

Handling runtime permissions? → Follow android-permissions.md for manifest declarations and Compose permission patterns
→ Request permissions contextually and handle "Don't ask again" flows

Showing notifications or foreground services? → Use android-notifications.md for notification channels, styles, actions, and foreground services
→ Check POST_NOTIFICATIONS permission on API 33+ before showing notifications
→ Create notification channels at app startup (required for API 26+)

Sharing logic across ViewModels or avoiding base classes? → Use delegation via interfaces as described in kotlin-delegation.md
→ Prefer small, injected delegates for validation, analytics, or feature flags

Adding crash reporting / monitoring? → Follow crashlytics.md for provider-agnostic interfaces and module placement
→ Use DI bindings to swap between Firebase Crashlytics or Sentry

Enabling StrictMode guardrails? → Follow android-strictmode.md for app-level setup and Compose compiler diagnostics
→ Use Sentry/Firebase init from crashlytics.md to ship StrictMode logs

Choosing design patterns for a new feature, business logic, or system? → Use design-patterns.md for Android-focused pattern guidance
→ Align with architecture.md and modularization.md

Measuring performance regressions or startup/jank? → Use android-performance.md for Macrobenchmark, Baseline Profiles, and ProfileInstaller setup
→ Keep benchmark module aligned with benchmark build type in gradle-setup.md
→ If the user explicitly requests to investigate jank or add custom trace points, use android-performance.md for System Tracing (androidx.tracing) setup

Setting up app initialization or splash screen? → Follow android-performance.md → "App Startup & Initialization" for App Startup library, lazy init, and splash screen
→ Avoid ContentProvider-based auto-initialization - use Initializer interface instead
→ Use installSplashScreen() with setKeepOnScreenCondition for loading state

Adding icons, images, or custom graphics? → Use android-graphics.md for Material Symbols icons and custom drawing
→ Download icons via Iconify API or Google Fonts (avoid deprecated Icons.Default.* library)
→ Use Modifier.drawWithContent, drawBehind, or drawWithCache for custom graphics

Creating custom UI effects (glow, shadows, gradients)? → Check android-graphics.md for Canvas drawing, BlendMode, and Palette API patterns
→ Use rememberInfiniteTransition for animated effects

Ensuring accessibility compliance (TalkBack, touch targets, color contrast)? → Follow android-accessibility.md for semantic properties and WCAG guidelines
→ Provide contentDescription for all icons and images
→ Ensure 48dp × 48dp minimum touch targets
→ Test with TalkBack and Accessibility Scanner

Working with images and color extraction? → Use android-graphics.md → "Image Loading with Coil3" for AsyncImage, SubcomposeAsyncImage, rememberAsyncImagePainter, and Hilt ImageLoader setup
→ Use android-graphics.md for Palette API and color extraction

Implementing complex coroutine flows or background work? → Follow coroutines-patterns.md for structured concurrency patterns
→ Use appropriate dispatchers (IO, Default, Main) and proper cancellation handling
→ Prefer StateFlow/SharedFlow over channels for state management
→ Use callbackFlow to wrap Android callback APIs (connectivity, sensors, location) into Flow
→ Use suspendCancellableCoroutine for one-shot callbacks (Play Services tasks, biometrics)
→ Use combine() to merge multiple Flows in ViewModels, shareIn to share expensive upstream
→ Handle backpressure with buffer, conflate, debounce, or sample

Need to share behavior across multiple classes? → Use kotlin-delegation.md for interface delegation patterns
→ Avoid base classes; prefer composition with delegated interfaces
→ Examples: Analytics, FormValidator, CrashReporter

Refactoring existing code or improving architecture? → Review architecture.md for layer responsibilities
→ Check design-patterns.md for applicable patterns
→ Follow kotlin-patterns.md for Kotlin-specific improvements
→ Ensure compliance with modularization.md dependency rules

Debugging crashes, ANRs, or obfuscated stack traces? → Follow android-debugging.md for Logcat, ANR traces, and Compose recomposition debugging
→ Use android-debugging.md for R8 mapping files and manual de-obfuscation
→ See gradle-setup.md for R8 build configuration and keep rules

Debugging performance issues or memory leaks? → Enable android-strictmode.md for development builds
→ Use android-performance.md for profiling and benchmarking
→ Use android-debugging.md for LeakCanary and heap dump analysis
→ Check coroutines-patterns.md for coroutine cancellation patterns

Setting up CI/CD or code quality checks? → Use code-quality.md for Detekt baseline and CI integration
→ Use gradle-setup.md for build cache and convention plugins
→ Use testing.md for test organization and coverage

Handling sensitive data or privacy concerns? → Follow crashlytics.md for data scrubbing patterns
→ Use android-permissions.md for proper permission justification
→ Check android-strictmode.md for detecting cleartext network traffic

Migrating legacy code (LiveData, Fragments, Accompanist, RxJava)? → Use migration.md for all migration paths
→ Follow architecture.md for modern MVVM patterns

Adding Compose animations? → Use compose-patterns.md → "Animation" for AnimatedVisibility, AnimatedContent, animate*AsState, Animatable, shared elements
→ Use graphicsLayer for GPU-accelerated transforms (no recomposition)
→ Always provide label parameter for Layout Inspector debugging

Using side effects (LaunchedEffect, DisposableEffect)? → Use compose-patterns.md → "Side Effects" for effect selection guide
→ LaunchedEffect(key) for state-driven coroutines, rememberCoroutineScope for event-driven
→ DisposableEffect for listener/resource cleanup, always include onDispose
→ LifecycleResumeEffect for onResume/onPause work (camera, media), LifecycleStartEffect for onStart/onStop (location, sensors)

Working with Modifier ordering or custom modifiers? → Use compose-patterns.md → "Modifiers" for chain ordering rules and patterns
→ Use Modifier.Node for custom modifiers (not deprecated Modifier.composed)
→ Order: size → padding → drawing → interaction

Migrating from Accompanist or deprecated Compose APIs? → Use migration.md for Accompanist, Compose API, Material, and Edge-to-Edge migrations
→ See compose-patterns.md → "Deprecated Patterns & Migrations" for a summary list

Optimizing Compose recomposition or stability? → Use compose-patterns.md for @Immutable/@Stable annotations
→ Use android-performance.md → "Compose Recomposition Performance" for three phases, deferred state reads, Strong Skipping Mode
→ Check gradle-setup.md for Compose Compiler metrics and stability reports
→ Use kotlin-patterns.md for immutable data structures

Working with databases (Room)? → Define DAOs and entities in core/database per modularization.md
→ Use testing.md for in-memory database testing and migration tests
→ Follow architecture.md for repository patterns with Room

Need internationalization/localization (i18n/l10n)? → Use android-i18n.md for string resources, plurals, and RTL support
→ Follow compose-patterns.md for RTL-aware Compose layouts
→ Use testing.md for locale-specific testing

Implementing network calls (Retrofit)? → Use architecture.md → "Network Layer Setup" for Retrofit service interfaces, Hilt NetworkModule, and AuthInterceptor
→ Define API interfaces in core/network per modularization.md
→ Follow dependencies.md for Retrofit, OkHttp, and serialization setup
→ Handle errors with generic Result<T> from kotlin-patterns.md

Creating custom lint rules or code checks? → Use code-quality.md for Detekt custom rules
→ Follow gradle-setup.md for convention plugin setup
→ Check android-strictmode.md for runtime checks

Need code coverage reporting? → Use android-code-coverage.md for JaCoCo setup
→ Follow testing.md for test strategies
→ Check gradle-setup.md for convention plugin integration

Implementing security features (encryption, biometrics, pinning)? → Use android-security.md for comprehensive security guide
→ Follow android-permissions.md for runtime permissions
→ Check crashlytics.md for PII scrubbing and data privacy

Weekly Installs
89
Repository
drjacky/claude-…id-ninja
GitHub Stars
47
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass