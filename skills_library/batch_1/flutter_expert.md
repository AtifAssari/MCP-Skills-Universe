---
title: flutter-expert
url: https://skills.sh/jeffallan/claude-skills/flutter-expert
---

# flutter-expert

skills/jeffallan/claude-skills/flutter-expert
flutter-expert
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill flutter-expert
Summary

Cross-platform mobile development with Flutter 3, Dart, and production-grade state management patterns.

Covers widget development, Riverpod and Bloc state management, GoRouter navigation, and platform-specific implementations with detailed reference guides for each
Enforces const optimization, proper key usage, and scoped state patterns to prevent unnecessary rebuilds and full-subtree re-renders
Includes profiling workflows with Flutter DevTools, jank diagnosis, and performance optimization techniques
Provides troubleshooting guidance for common failures: analyze errors, test assertions, dependency conflicts, and hot reload issues
SKILL.md
Flutter Expert

Senior mobile engineer building high-performance cross-platform applications with Flutter 3 and Dart.

When to Use This Skill
Building cross-platform Flutter applications
Implementing state management (Riverpod, Bloc)
Setting up navigation with GoRouter
Creating custom widgets and animations
Optimizing Flutter performance
Platform-specific implementations
Core Workflow
Setup — Scaffold project, add dependencies (flutter pub get), configure routing
State — Define Riverpod providers or Bloc/Cubit classes; verify with flutter analyze
If flutter analyze reports issues: fix all lints and warnings before proceeding; re-run until clean
Widgets — Build reusable, const-optimized components; run flutter test after each feature
If tests fail: inspect widget tree with Flutter DevTools, fix failing assertions, re-run flutter test
Test — Write widget and integration tests; confirm with flutter test --coverage
If coverage drops or tests fail: identify untested branches, add targeted tests, re-run before merging
Optimize — Profile with Flutter DevTools (flutter run --profile), eliminate jank, reduce rebuilds
If jank persists: check rebuild counts in the Performance overlay, isolate expensive build() calls, apply const or move state closer to consumers
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Riverpod	references/riverpod-state.md	State management, providers, notifiers
Bloc	references/bloc-state.md	Bloc, Cubit, event-driven state, complex business logic
GoRouter	references/gorouter-navigation.md	Navigation, routing, deep linking
Widgets	references/widget-patterns.md	Building UI components, const optimization
Structure	references/project-structure.md	Setting up project, architecture
Performance	references/performance.md	Optimization, profiling, jank fixes
Code Examples
Riverpod Provider + ConsumerWidget (correct pattern)
// provider definition
final counterProvider = StateNotifierProvider<CounterNotifier, int>(
  (ref) => CounterNotifier(),
);

class CounterNotifier extends StateNotifier<int> {
  CounterNotifier() : super(0);
  void increment() => state = state + 1; // new instance, never mutate
}

// consuming widget — use ConsumerWidget, not StatefulWidget
class CounterView extends ConsumerWidget {
  const CounterView({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final count = ref.watch(counterProvider);
    return Text('$count');
  }
}

Before / After — State Management
// ❌ WRONG: app-wide state in setState
class _BadCounterState extends State<BadCounter> {
  int _count = 0;
  void _inc() => setState(() => _count++); // causes full subtree rebuild
}

// ✅ CORRECT: scoped Riverpod consumer
class GoodCounter extends ConsumerWidget {
  const GoodCounter({super.key});
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final count = ref.watch(counterProvider);
    return IconButton(
      onPressed: () => ref.read(counterProvider.notifier).increment(),
      icon: const Icon(Icons.add), // const on static widgets
    );
  }
}

Constraints
MUST DO
Use const constructors wherever possible
Implement proper keys for lists
Use Consumer/ConsumerWidget for state (not StatefulWidget)
Follow Material/Cupertino design guidelines
Profile with DevTools, fix jank
Test widgets with flutter_test
MUST NOT DO
Build widgets inside build() method
Mutate state directly (always create new instances)
Use setState for app-wide state
Skip const on static widgets
Ignore platform-specific behavior
Block UI thread with heavy computation (use compute())
Troubleshooting Common Failures
Symptom	Likely Cause	Recovery
flutter analyze errors	Unresolved imports, missing const, type mismatches	Fix flagged lines; run flutter pub get if imports are missing
Widget test assertion failures	Widget tree mismatch or async state not settled	Use tester.pumpAndSettle() after state changes; verify finder selectors
Build fails after adding package	Incompatible dependency version	Run flutter pub upgrade --major-versions; check pub.dev compatibility
Jank / dropped frames	Expensive build() calls, uncached widgets, heavy main-thread work	Use RepaintBoundary, move heavy work to compute(), add const
Hot reload not reflecting changes	State held in StateNotifier not reset	Use hot restart (R in terminal) to reset full app state
Output Templates

When implementing Flutter features, provide:

Widget code with proper const usage
Provider/Bloc definitions
Route configuration if needed
Test file structure

Documentation

Weekly Installs
10.2K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass