---
title: flutter-expert
url: https://skills.sh/nguyenthienthanh/aura-frog/flutter-expert
---

# flutter-expert

skills/nguyenthienthanh/aura-frog/flutter-expert
flutter-expert
Installation
$ npx skills add https://github.com/nguyenthienthanh/aura-frog --skill flutter-expert
SKILL.md
Flutter Expert Skill

Flutter patterns: Dart, state management (Riverpod/Bloc), cross-platform mobile.

1. Project Structure (Feature-First)
lib/
├── core/          # constants, errors, extensions, theme, utils
├── features/
│   └── auth/
│       ├── data/  # datasources, models, repositories
│       ├── domain/# entities, repository interfaces, usecases
│       └── presentation/ # bloc, pages, widgets
├── shared/widgets/
└── main.dart

2. Widget Best Practices

Always use const constructors for immutable widgets. Extract complex widgets into separate classes rather than inline builders.

class UserCard extends StatelessWidget {
  const UserCard({super.key, required this.user, this.onTap});
  final User user;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(title: Text(user.name), subtitle: Text(user.email), onTap: onTap),
    );
  }
}

3. State Management (Riverpod)
@riverpod
class AuthNotifier extends _$AuthNotifier {
  @override
  AsyncValue<User?> build() => const AsyncValue.data(null);

  Future<void> signIn(String email, String password) async {
    state = const AsyncValue.loading();
    state = await AsyncValue.guard(() => ref.read(authRepositoryProvider).signIn(email, password));
  }
}

// Widget: use ConsumerWidget, ref.watch(authNotifierProvider), .when(data/loading/error)


Repository pattern: Abstract interface + Riverpod provider for implementation.

4. State Management (Bloc)

Pattern: sealed Events + sealed States + Bloc with on<Event> handlers.

sealed class AuthEvent {}
class AuthSignInRequested extends AuthEvent { /* email, password */ }

sealed class AuthState {}
class AuthInitial extends AuthState {}
class AuthLoading extends AuthState {}
class AuthAuthenticated extends AuthState { final User user; }
class AuthError extends AuthState { final String message; }

// Use BlocBuilder with buildWhen, Dart 3 switch expressions for state matching

5. Navigation (GoRouter)
final router = GoRouter(
  redirect: (context, state) {
    if (!isLoggedIn && state.matchedLocation != '/login') return '/login';
    if (isLoggedIn && state.matchedLocation == '/login') return '/';
    return null;
  },
  routes: [
    GoRoute(path: '/', builder: (_, __) => const HomePage(), routes: [
      GoRoute(path: 'user/:id', builder: (_, state) => UserPage(userId: state.pathParameters['id']!)),
    ]),
  ],
);

6. Forms & Validation

Use GlobalKey<FormState>, TextEditingController (always dispose), TextFormField with validators. Call _formKey.currentState!.validate() on submit.

7. Performance
ListView.builder for large lists with ValueKey per item
const widgets for static content
Consumer for targeted rebuilds (only rebuilds specific widget)
RepaintBoundary for isolated paint areas
8. Error Handling (Result Pattern)
sealed class Result<T> { const Result(); }
class Success<T> extends Result<T> { const Success(this.data); final T data; }
class Failure<T> extends Result<T> { const Failure(this.error); final AppException error; }

// Use Dart 3 pattern matching: switch (result) { case Success(:final data): ... }

9. Dependency Injection

Use GetIt for DI: registerLazySingleton for services/repos, registerFactory for Blocs.

10. Testing
Widget tests: testWidgets + tester.pumpWidget + find.byType
Bloc tests: blocTest<Bloc, State> with build/act/expect
Quick Reference
checklist[12]{pattern,best_practice}:
  Widgets,Const constructors + extract complex
  State,Riverpod or Bloc pattern
  Forms,GlobalKey + TextEditingController
  Lists,ListView.builder with ValueKey
  Navigation,GoRouter typed routes
  DI,GetIt or Riverpod providers
  Errors,Sealed Result class
  Testing,Widget tests + bloc_test
  Rebuilds,Consumer for targeted updates
  Dispose,Always dispose controllers
  Null safety,Pattern matching
  Performance,const widgets + RepaintBoundary

Weekly Installs
16
Repository
nguyenthienthan…ura-frog
GitHub Stars
17
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass