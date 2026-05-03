---
title: flutter-testing
url: https://skills.sh/vp-k/flutter-craft/flutter-testing
---

# flutter-testing

skills/vp-k/flutter-craft/flutter-testing
flutter-testing
Installation
$ npx skills add https://github.com/vp-k/flutter-craft --skill flutter-testing
SKILL.md
Flutter Testing Guide
Overview

Write tests following priority order after implementation. Focus on business logic first, UI last.

Announce at start: "I'm using the flutter-testing skill to write tests."

Test Priority Order
Priority 1: Repository & DataSource Unit Tests
  ├── Business logic correctness
  ├── API integration
  └── Data transformation

Priority 2: State Management Unit Tests
  ├── BLoC/Cubit event handling
  ├── Provider state transitions
  └── Error state handling

Priority 3: Widget Tests (Optional)
  ├── User interactions
  ├── Widget rendering
  └── Navigation

Priority 4: Golden Tests (Visual Regression)
  ├── Design system component snapshots
  ├── Pixel-perfect comparison
  └── CI integration

Optional: Integration Tests
  └── Full app flow testing

Priority 1: Repository & DataSource Tests
Repository Test Template
import 'package:flutter_test/flutter_test.dart';
import 'package:mockito/mockito.dart';
import 'package:mockito/annotations.dart';

@GenerateMocks([UserRemoteDataSource, UserLocalDataSource])
import 'user_repository_impl_test.mocks.dart';

void main() {
  late UserRepositoryImpl repository;
  late MockUserRemoteDataSource mockRemoteDataSource;
  late MockUserLocalDataSource mockLocalDataSource;

  setUp(() {
    mockRemoteDataSource = MockUserRemoteDataSource();
    mockLocalDataSource = MockUserLocalDataSource();
    repository = UserRepositoryImpl(
      remoteDataSource: mockRemoteDataSource,
      localDataSource: mockLocalDataSource,
    );
  });

  group('getUser', () {
    const tUserId = '123';
    final tUserModel = UserModel(id: '123', name: 'Test', email: 'test@test.com');
    final tUserEntity = User(id: '123', name: 'Test', email: 'test@test.com');

    test('should return User when remote data source succeeds', () async {
      // Arrange
      when(mockRemoteDataSource.getUser(any))
          .thenAnswer((_) async => tUserModel);

      // Act
      final result = await repository.getUser(tUserId);

      // Assert
      expect(result, equals(tUserEntity));
      verify(mockRemoteDataSource.getUser(tUserId));
    });

    test('should throw Exception when remote data source fails', () async {
      // Arrange
      when(mockRemoteDataSource.getUser(any))
          .thenThrow(Exception('Server error'));

      // Act & Assert
      expect(
        () => repository.getUser(tUserId),
        throwsException,
      );
    });
  });
}

DataSource Test Template
import 'package:flutter_test/flutter_test.dart';
import 'package:http/http.dart' as http;
import 'package:mockito/mockito.dart';

@GenerateMocks([http.Client])
import 'user_remote_datasource_test.mocks.dart';

void main() {
  late UserRemoteDataSourceImpl dataSource;
  late MockClient mockHttpClient;

  setUp(() {
    mockHttpClient = MockClient();
    dataSource = UserRemoteDataSourceImpl(client: mockHttpClient);
  });

  group('getUser', () {
    const tUserId = '123';
    final tUserJson = '{"id": "123", "name": "Test", "email": "test@test.com"}';

    test('should return UserModel when response is 200', () async {
      // Arrange
      when(mockHttpClient.get(any, headers: anyNamed('headers')))
          .thenAnswer((_) async => http.Response(tUserJson, 200));

      // Act
      final result = await dataSource.getUser(tUserId);

      // Assert
      expect(result, isA<UserModel>());
      expect(result.id, equals('123'));
    });

    test('should throw ServerException when response is not 200', () async {
      // Arrange
      when(mockHttpClient.get(any, headers: anyNamed('headers')))
          .thenAnswer((_) async => http.Response('Error', 500));

      // Act & Assert
      expect(
        () => dataSource.getUser(tUserId),
        throwsA(isA<ServerException>()),
      );
    });
  });
}

Priority 2: State Management Tests
BLoC Test Template
import 'package:bloc_test/bloc_test.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mockito/mockito.dart';

@GenerateMocks([GetUserUseCase])
import 'user_bloc_test.mocks.dart';

void main() {
  late UserBloc bloc;
  late MockGetUserUseCase mockGetUser;

  setUp(() {
    mockGetUser = MockGetUserUseCase();
    bloc = UserBloc(getUser: mockGetUser);
  });

  tearDown(() {
    bloc.close();
  });

  test('initial state should be UserInitial', () {
    expect(bloc.state, equals(UserInitial()));
  });

  blocTest<UserBloc, UserState>(
    'should emit [Loading, Loaded] when GetUser succeeds',
    build: () {
      when(mockGetUser(any))
          .thenAnswer((_) async => const User(id: '1', name: 'Test'));
      return bloc;
    },
    act: (bloc) => bloc.add(const GetUserEvent('1')),
    expect: () => [
      UserLoading(),
      const UserLoaded(User(id: '1', name: 'Test')),
    ],
  );

  blocTest<UserBloc, UserState>(
    'should emit [Loading, Error] when GetUser fails',
    build: () {
      when(mockGetUser(any)).thenThrow(Exception('error'));
      return bloc;
    },
    act: (bloc) => bloc.add(const GetUserEvent('1')),
    expect: () => [
      UserLoading(),
      const UserError('error'),
    ],
  );
}

Provider/Riverpod Test Template
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:mockito/mockito.dart';

void main() {
  late ProviderContainer container;
  late MockUserRepository mockRepository;

  setUp(() {
    mockRepository = MockUserRepository();
    container = ProviderContainer(
      overrides: [
        userRepositoryProvider.overrideWithValue(mockRepository),
      ],
    );
  });

  tearDown(() {
    container.dispose();
  });

  test('should return user when fetchUser succeeds', () async {
    // Arrange
    when(mockRepository.getUser(any))
        .thenAnswer((_) async => const User(id: '1', name: 'Test'));

    // Act
    final result = await container.read(userProvider('1').future);

    // Assert
    expect(result.name, equals('Test'));
  });
}

Priority 3: Widget Tests (Optional)
Widget Test Template
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:mockito/mockito.dart';

void main() {
  late MockUserBloc mockBloc;

  setUp(() {
    mockBloc = MockUserBloc();
  });

  Widget createWidgetUnderTest() {
    return MaterialApp(
      home: BlocProvider<UserBloc>.value(
        value: mockBloc,
        child: const UserScreen(),
      ),
    );
  }

  testWidgets('should display loading indicator when state is Loading',
      (tester) async {
    // Arrange
    when(mockBloc.state).thenReturn(UserLoading());

    // Act
    await tester.pumpWidget(createWidgetUnderTest());

    // Assert
    expect(find.byType(CircularProgressIndicator), findsOneWidget);
  });

  testWidgets('should display user name when state is Loaded',
      (tester) async {
    // Arrange
    when(mockBloc.state).thenReturn(
      const UserLoaded(User(id: '1', name: 'John Doe')),
    );

    // Act
    await tester.pumpWidget(createWidgetUnderTest());

    // Assert
    expect(find.text('John Doe'), findsOneWidget);
  });

  testWidgets('should call GetUserEvent when button is tapped',
      (tester) async {
    // Arrange
    when(mockBloc.state).thenReturn(UserInitial());

    // Act
    await tester.pumpWidget(createWidgetUnderTest());
    await tester.tap(find.byType(ElevatedButton));

    // Assert
    verify(mockBloc.add(any)).called(1);
  });
}

Priority 4: Golden Tests (Visual Regression)

디자인 시스템 컴포넌트의 시각적 일관성을 검증합니다. UI가 의도치 않게 변경되는 것을 방지합니다.

Golden Test Template
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('LoginButton matches golden', (tester) async {
    // 고정 크기로 일관된 스크린샷 보장
    await tester.binding.setSurfaceSize(const Size(400, 200));

    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: Center(
            child: LoginButton(onPressed: () {}),
          ),
        ),
      ),
    );

    await expectLater(
      find.byType(LoginButton),
      matchesGoldenFile('goldens/login_button.png'),
    );
  });

  testWidgets('UserCard dark mode matches golden', (tester) async {
    await tester.binding.setSurfaceSize(const Size(400, 300));

    await tester.pumpWidget(
      MaterialApp(
        theme: ThemeData.dark(),
        home: Scaffold(
          body: UserCard(
            user: User(id: '1', name: 'Test User', avatar: 'assets/test/avatar.png'),
          ),
        ),
      ),
    );

    await expectLater(
      find.byType(UserCard),
      matchesGoldenFile('goldens/user_card_dark.png'),
    );
  });
}

Golden File Management
# 최초 생성 / 기준선 업데이트 (의도적 변경 후)
flutter test --update-goldens

# 비교 실행 (CI/CD에서 사용)
flutter test --tags golden

# 특정 파일만
flutter test test/features/auth/presentation/widgets/login_button_golden_test.dart --update-goldens

테스트 파일 명명 규칙

골든 테스트 파일은 _golden_test.dart 접미사로 구분:

test/features/auth/presentation/widgets/
├── login_button_test.dart         # 기능 테스트 (Priority 3)
└── login_button_golden_test.dart  # 골든 테스트 (Priority 4)

태그 기반 실행

dart_test.yaml에서 골든 테스트를 태그로 분리:

tags:
  golden:
    # CI에서 별도 실행 가능


테스트 파일에 태그 추가:

@Tags(['golden'])
library;

import 'package:flutter_test/flutter_test.dart';
// ...

Golden Test 작성 시 주의사항
고정 크기: setSurfaceSize()로 일관된 캔버스 크기 설정
결정적 데이터: 랜덤/시간 의존 데이터 사용 금지
폰트 로딩: 커스텀 폰트는 FontLoader로 미리 로드
네트워크 이미지: Mock으로 대체 (네트워크 의존성 제거)
플랫폼 차이: macOS/Linux/Windows에서 렌더링이 다를 수 있음 → CI 환경 고정
언제 Golden Test를 작성하는가
디자인 시스템 컴포넌트 (Button, Card, Input, Badge 등)
테마 변경 후 시각적 영향 검증
다크 모드 / 라이트 모드 전환 검증
반응형 레이아웃의 브레이크포인트별 검증
언제 Golden Test를 건너뛰는가
비즈니스 로직 위주 화면 (데이터 표시만 다름)
자주 변경되는 화면 (골든 파일 업데이트 비용 > 이득)
외부 데이터에 크게 의존하는 화면
Test File Structure
test/
├── features/
│   └── auth/
│       ├── data/
│       │   ├── datasources/
│       │   │   └── auth_remote_datasource_test.dart
│       │   └── repositories/
│       │       └── auth_repository_impl_test.dart
│       └── presentation/
│           ├── bloc/
│           │   └── auth_bloc_test.dart
│           └── widgets/
│               └── login_button_test.dart
└── helpers/
    ├── test_helpers.dart
    └── pump_app.dart

Running Tests
# All tests
flutter test

# Specific feature
flutter test test/features/auth/

# Specific file
flutter test test/features/auth/data/repositories/auth_repository_impl_test.dart

# With coverage
flutter test --coverage

# Generate coverage report
genhtml coverage/lcov.info -o coverage/html

Test Dependencies
# Mocking (choose one)
flutter pub add dev:mockito        # Requires codegen
flutter pub add dev:mocktail       # No codegen required (recommended)

# Code generation
flutter pub add dev:build_runner

# State management testing
flutter pub add dev:bloc_test      # If using BLoC
flutter pub add dev:riverpod_test  # If using Riverpod (optional)

# Freezed (if using immutable states)
flutter pub add freezed_annotation
flutter pub add dev:freezed

Generate Mocks
# Generate mock files
flutter pub run build_runner build --delete-conflicting-outputs

Key Principles
Priority Order: Repository → State → Widget
Mock Dependencies: Don't test real APIs or databases
Arrange-Act-Assert: Clear test structure
One Assertion Focus: Each test tests one thing
Descriptive Names: Test names describe behavior
When to Skip Tests

Skip Widget Tests when:

Simple stateless widgets
No user interaction logic
Pure presentation (no business logic)

Never Skip:

Repository tests (business logic)
State management tests (state transitions)
Error handling tests
REQUIRED SUB-SKILL

After writing tests, you MUST invoke: → flutter-craft:flutter-verification

Run flutter test and verify all tests pass.

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