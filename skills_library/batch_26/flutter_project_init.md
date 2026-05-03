---
title: flutter-project-init
url: https://skills.sh/vp-k/flutter-craft/flutter-project-init
---

# flutter-project-init

skills/vp-k/flutter-craft/flutter-project-init
flutter-project-init
Installation
$ npx skills add https://github.com/vp-k/flutter-craft --skill flutter-project-init
SKILL.md
Flutter Project Initialization

Use when: "new project", "create project", "start project", "init flutter"

Workflow Overview
Step 1: Project Info     → name, org, description
Step 2: Domain Pattern   → Simple/Stateful/Categorized/Tracked/Relational/Custom
Step 3: Tech Stack       → State Management, Features
Step 4: Generate & Verify → create, build, analyze

Step 1: Gather Project Info

Ask user for:

Field	Example	Required
Project name	my_app (snake_case)	Yes
Organization	com.example	Yes
Description	"Task management app"	Yes
Entity name	Task, Note, Expense	Yes
Step 2: Domain Pattern Selection (CRUD 기반)

Ask user to choose:

Pattern	Examples	Generated Structure
Simple	Note, Memo, Bookmark	단일 엔티티 CRUD
Stateful	Todo, Task, Order	상태 필드 포함 (완료/진행중 등)
Categorized	Expense, Product, Recipe	카테고리 관계 포함
Tracked	Habit, Workout, Study	시간/날짜 기반 트래킹
Relational	Blog (User-Post-Comment)	다중 엔티티 관계
Custom	-	사용자 정의 필드
Pattern별 생성 코드
Simple Pattern
// Entity
@freezed
sealed class Note with _$Note {
  const factory Note({
    required String id,
    required String title,
    required String content,
    required DateTime createdAt,
    DateTime? updatedAt,
  }) = _Note;
}

Stateful Pattern
// Entity with status
@freezed
sealed class Task with _$Task {
  const factory Task({
    required String id,
    required String title,
    required String description,
    @Default(TaskStatus.pending) TaskStatus status,
    required DateTime createdAt,
    DateTime? completedAt,
  }) = _Task;
}

enum TaskStatus { pending, inProgress, completed, cancelled }

Categorized Pattern
// Entity with category relation
@freezed
sealed class Expense with _$Expense {
  const factory Expense({
    required String id,
    required String title,
    required double amount,
    required String categoryId,
    required DateTime date,
    String? note,
  }) = _Expense;
}

@freezed
sealed class Category with _$Category {
  const factory Category({
    required String id,
    required String name,
    required String icon,
    required String color,
  }) = _Category;
}

Tracked Pattern
// Entity with time tracking
@freezed
sealed class Habit with _$Habit {
  const factory Habit({
    required String id,
    required String name,
    required String description,
    required HabitFrequency frequency,
    required List<DateTime> completedDates,
    required int currentStreak,
    required int bestStreak,
    required DateTime createdAt,
  }) = _Habit;
}

enum HabitFrequency { daily, weekly, monthly }

Relational Pattern
// Multiple related entities
@freezed
sealed class User with _$User {
  const factory User({
    required String id,
    required String name,
    required String email,
    required DateTime createdAt,
  }) = _User;
}

@freezed
sealed class Post with _$Post {
  const factory Post({
    required String id,
    required String authorId,
    required String title,
    required String content,
    required DateTime createdAt,
    @Default(0) int likeCount,
  }) = _Post;
}

@freezed
sealed class Comment with _$Comment {
  const factory Comment({
    required String id,
    required String postId,
    required String authorId,
    required String content,
    required DateTime createdAt,
  }) = _Comment;
}

Step 3: Tech Stack Selection
State Management (필수 선택)
Option	Description
Riverpod (Recommended)	Modern, compile-safe, testable
BLoC	Event-driven, enterprise-grade
Feature Presets
Preset	Includes
Minimal	Core only (Freezed, Drift, DI)
Essential	+ GoRouter, Dio, Error handling
Full	+ Auth, Localization, Responsive
Feature Details
# Minimal preset (always included)
flutter pub add freezed_annotation
flutter pub add drift
flutter pub add get_it
flutter pub add injectable
flutter pub add dev:freezed
flutter pub add dev:build_runner
flutter pub add dev:injectable_generator
flutter pub add dev:drift_dev

# Essential preset adds
flutter pub add go_router
flutter pub add dio
flutter pub add dartz              # Either type for error handling

# Full preset adds
flutter pub add easy_localization
flutter pub add responsive_framework
flutter pub add firebase_auth      # Optional

Step 4: Project Generation
4.1 Create Flutter Project
flutter create --org <org> --project-name <name> <name>
cd <name>

4.2 Setup Folder Structure
lib/
├── core/
│   ├── constants/
│   │   └── app_constants.dart
│   ├── database/
│   │   └── app_database.dart
│   ├── di/
│   │   └── injection.dart
│   ├── errors/
│   │   ├── exceptions.dart
│   │   └── failures.dart
│   ├── router/
│   │   └── app_router.dart
│   ├── theme/
│   │   ├── app_colors.dart
│   │   └── app_theme.dart
│   └── utils/
│       └── extensions.dart
├── features/
│   └── <entity>/
│       ├── domain/
│       │   ├── entities/
│       │   │   └── <entity>.dart
│       │   ├── repositories/
│       │   │   └── <entity>_repository.dart
│       │   └── usecases/
│       │       ├── create_<entity>.dart
│       │       ├── delete_<entity>.dart
│       │       ├── get_<entity>s.dart
│       │       └── update_<entity>.dart
│       ├── data/
│       │   ├── datasources/
│       │   │   └── <entity>_local_datasource.dart
│       │   ├── models/
│       │   │   └── <entity>_model.dart
│       │   └── repositories/
│       │       └── <entity>_repository_impl.dart
│       └── presentation/
│           ├── bloc/          # or providers/
│           │   ├── <entity>_bloc.dart
│           │   ├── <entity>_event.dart
│           │   └── <entity>_state.dart
│           ├── pages/
│           │   ├── <entity>_list_page.dart
│           │   └── <entity>_detail_page.dart
│           └── widgets/
│               └── <entity>_card.dart
├── shared/
│   └── widgets/
│       └── loading_widget.dart
└── main.dart

4.3 Generate Base Files
core/errors/failures.dart
import 'package:freezed_annotation/freezed_annotation.dart';

part 'failures.freezed.dart';

@freezed
sealed class Failure with _$Failure {
  const factory Failure.server({required String message, int? code}) = ServerFailure;
  const factory Failure.cache({required String message}) = CacheFailure;
  const factory Failure.network({@Default('No internet connection') String message}) = NetworkFailure;
  const factory Failure.validation({required String message}) = ValidationFailure;
}

core/database/app_database.dart
import 'dart:io';
import 'package:drift/drift.dart';
import 'package:drift/native.dart';
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart' as p;

part 'app_database.g.dart';

// Tables will be added per domain pattern
@DriftDatabase(tables: [])
class AppDatabase extends _$AppDatabase {
  AppDatabase() : super(_openConnection());

  @override
  int get schemaVersion => 1;
}

LazyDatabase _openConnection() {
  return LazyDatabase(() async {
    final dbFolder = await getApplicationDocumentsDirectory();
    final file = File(p.join(dbFolder.path, 'app.db'));
    return NativeDatabase.createInBackground(file);
  });
}

core/di/injection.dart
import 'package:get_it/get_it.dart';
import 'package:injectable/injectable.dart';
import 'injection.config.dart';

final getIt = GetIt.instance;

@InjectableInit(preferRelativeImports: true)
Future<void> configureDependencies() async => getIt.init();

4.4 Update pubspec.yaml

Based on selected preset, add all required dependencies.

4.5 Run Code Generation
flutter pub get
flutter pub run build_runner build --delete-conflicting-outputs

4.6 Validation (REQUIRED)
flutter analyze


Must pass with 0 errors. Info/warning level issues are acceptable.

If errors exist:

Fix each error
Re-run flutter pub run build_runner build
Re-run flutter analyze
Repeat until 0 errors
Step 5: Initialize Git
git init
git add .
git commit -m "Initial commit: <project_name> with Clean Architecture

- Domain pattern: <selected_pattern>
- State management: <Riverpod/BLoC>
- Features: <selected_preset>

🤖 Generated with flutter-craft"

Completion Checklist
 Project created with correct name/org
 Folder structure matches Clean Architecture
 Domain entities generated with Freezed
 Database tables created in Drift
 DI configured with injectable
 flutter pub get successful
 flutter pub run build_runner build successful
 flutter analyze returns 0 errors
 Git initialized with initial commit
Output to User

After completion, inform:

✅ Project '<name>' created successfully!

📁 Structure: Clean Architecture
📦 Pattern: <selected_pattern>
🔄 State: <Riverpod/BLoC>
✨ Features: <preset>

Next steps:
1. cd <name>
2. flutter run
3. Use /brainstorm to plan your first feature

References

For detailed code templates per pattern, see:

references/simple-pattern.md
references/stateful-pattern.md
references/categorized-pattern.md
references/tracked-pattern.md
references/relational-pattern.md

Note: Custom 패턴은 사용자 정의 필드를 직접 설계하므로 별도 템플릿이 없습니다.

Weekly Installs
13
Repository
vp-k/flutter-craft
GitHub Stars
6
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass