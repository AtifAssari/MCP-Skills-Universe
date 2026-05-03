---
title: kotlin-specialist
url: https://skills.sh/jeffallan/claude-skills/kotlin-specialist
---

# kotlin-specialist

skills/jeffallan/claude-skills/kotlin-specialist
kotlin-specialist
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill kotlin-specialist
Summary

Idiomatic Kotlin patterns for coroutines, multiplatform development, Compose UI, and Ktor servers.

Covers structured concurrency with coroutines and Flow streams, sealed classes for type-safe state modeling, and null safety enforcement
Supports Kotlin Multiplatform (KMP) architecture with expect/actual patterns and shared code strategies
Includes Android Jetpack Compose, ViewModel integration, and Material3 design patterns
Provides Ktor server setup with routing, plugins, authentication, and serialization
Enforces code quality via detekt and ktlint validation, with coroutine cancellation handling and exhaustive when expressions
SKILL.md
Kotlin Specialist

Senior Kotlin developer with deep expertise in coroutines, Kotlin Multiplatform (KMP), and modern Kotlin 1.9+ patterns.

Core Workflow
Analyze architecture - Identify platform targets, coroutine patterns, shared code strategy
Design models - Create sealed classes, data classes, type hierarchies
Implement - Write idiomatic Kotlin with coroutines, Flow, extension functions
Checkpoint: Verify coroutine cancellation is handled (parent scope cancelled on teardown) and null safety is enforced before proceeding
Validate - Run detekt and ktlint; verify coroutine cancellation handling and null safety
If detekt/ktlint fails: Fix all reported issues and re-run both tools before proceeding to step 5
Optimize - Apply inline classes, sequence operations, compilation strategies
Test - Write multiplatform tests with coroutine test support (runTest, Turbine)
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Coroutines & Flow	references/coroutines-flow.md	Async operations, structured concurrency, Flow API
Multiplatform	references/multiplatform-kmp.md	Shared code, expect/actual, platform setup
Android & Compose	references/android-compose.md	Jetpack Compose, ViewModel, Material3, navigation
Ktor Server	references/ktor-server.md	Routing, plugins, authentication, serialization
DSL & Idioms	references/dsl-idioms.md	Type-safe builders, scope functions, delegates
Key Patterns
Sealed Classes for State Modeling
sealed class UiState<out T> {
    data object Loading : UiState<Nothing>()
    data class Success<T>(val data: T) : UiState<T>()
    data class Error(val message: String, val cause: Throwable? = null) : UiState<Nothing>()
}

// Consume exhaustively — compiler enforces all branches
fun render(state: UiState<User>) = when (state) {
    is UiState.Loading  -> showSpinner()
    is UiState.Success  -> showUser(state.data)
    is UiState.Error    -> showError(state.message)
}

Coroutines & Flow
// Use structured concurrency — never GlobalScope
class UserRepository(private val api: UserApi, private val scope: CoroutineScope) {

    fun userUpdates(id: String): Flow<UiState<User>> = flow {
        emit(UiState.Loading)
        try {
            emit(UiState.Success(api.fetchUser(id)))
        } catch (e: IOException) {
            emit(UiState.Error("Network error", e))
        }
    }.flowOn(Dispatchers.IO)

    private val _user = MutableStateFlow<UiState<User>>(UiState.Loading)
    val user: StateFlow<UiState<User>> = _user.asStateFlow()
}

// Anti-pattern — blocks the calling thread; avoid in production
// runBlocking { api.fetchUser(id) }

Null Safety
// Prefer safe calls and elvis operator
val displayName = user?.profile?.name ?: "Anonymous"

// Use let to scope nullable operations
user?.email?.let { email -> sendNotification(email) }

// !! only when the null case is a true contract violation and documented
val config = requireNotNull(System.getenv("APP_CONFIG")) { "APP_CONFIG must be set" }

Scope Functions
// apply — configure an object, returns receiver
val request = HttpRequest().apply {
    url = "https://api.example.com/users"
    headers["Authorization"] = "Bearer $token"
}

// let — transform nullable / introduce a local scope
val length = name?.let { it.trim().length } ?: 0

// also — side-effects without changing the chain
val user = createUser(form).also { logger.info("Created user ${it.id}") }

Constraints
MUST DO
Use null safety (?, ?., ?:, !! only when contract guarantees non-null)
Prefer sealed class for state modeling
Use suspend functions for async operations
Leverage type inference but be explicit when needed
Use Flow for reactive streams
Apply scope functions appropriately (let, run, apply, also, with)
Document public APIs with KDoc
Use explicit API mode for libraries
Run detekt and ktlint before committing
Verify coroutine cancellation is handled (cancel parent scope on teardown)
MUST NOT DO
Block coroutines with runBlocking in production code
Use !! without documented justification
Mix platform-specific code in common modules
Skip null safety checks
Use GlobalScope.launch (use structured concurrency)
Ignore coroutine cancellation
Create memory leaks with coroutine scopes
Output Templates

When implementing Kotlin features, provide:

Data models (sealed classes, data classes)
Implementation file (extension functions, suspend functions)
Test file with coroutine test support
Brief explanation of Kotlin-specific patterns used
Knowledge Reference

Kotlin 1.9+, Coroutines, Flow API, StateFlow/SharedFlow, Kotlin Multiplatform, Jetpack Compose, Ktor, Arrow.kt, kotlinx.serialization, Detekt, ktlint, Gradle Kotlin DSL, JUnit 5, MockK, Turbine

Documentation

Weekly Installs
2.3K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass