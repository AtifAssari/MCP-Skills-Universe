---
title: kotlin
url: https://skills.sh/dralgorhythm/claude-agentic-framework/kotlin
---

# kotlin

skills/dralgorhythm/claude-agentic-framework/kotlin
kotlin
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill kotlin
SKILL.md
Kotlin / Android Development
Project Setup
Gradle Kotlin DSL
// settings.gradle.kts
pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "MyApp"
include(":app")

build.gradle.kts (app)
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.kotlin.compose)
}

android {
    namespace = "com.example.myapp"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.example.myapp"
        minSdk = 26
        targetSdk = 35
        versionCode = 1
        versionName = "1.0"
    }

    buildFeatures {
        compose = true
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
    }
}

dependencies {
    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.lifecycle.runtime.ktx)
    implementation(libs.androidx.activity.compose)
    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.ui)
    implementation(libs.androidx.material3)

    testImplementation(libs.junit)
    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.androidx.espresso.core)
}

Version Catalog (libs.versions.toml)
[versions]
kotlin = "2.0.0"
compose-bom = "2024.06.00"
lifecycle = "2.8.0"

[libraries]
androidx-core-ktx = { group = "androidx.core", name = "core-ktx", version = "1.13.1" }
androidx-lifecycle-runtime-ktx = { group = "androidx.lifecycle", name = "lifecycle-runtime-ktx", version.ref = "lifecycle" }
androidx-compose-bom = { group = "androidx.compose", name = "compose-bom", version.ref = "compose-bom" }

[plugins]
android-application = { id = "com.android.application", version = "8.5.0" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
kotlin-compose = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }

Type Patterns
Null Safety
// Safe call operator
val length = name?.length

// Elvis operator
val displayName = user?.name ?: "Guest"

// Safe cast
val number = value as? Int

// Not-null assertion (use sparingly)
val name = user!!.name

// let for null checks
user?.let { safeUser ->
    println(safeUser.name)
}

Sealed Classes
sealed class Result<out T> {
    data class Success<T>(val data: T) : Result<T>()
    data class Error(val exception: Throwable) : Result<Nothing>()
    data object Loading : Result<Nothing>()
}

// Exhaustive when
fun handleResult(result: Result<User>) = when (result) {
    is Result.Success -> showUser(result.data)
    is Result.Error -> showError(result.exception)
    Result.Loading -> showLoading()
}

Data Classes
data class User(
    val id: String,
    val email: String,
    val name: String,
    val createdAt: Instant = Instant.now()
)

// Copy with modifications
val updatedUser = user.copy(name = "New Name")

// Destructuring
val (id, email, name) = user

Value Classes
@JvmInline
value class UserId(val value: String)

@JvmInline
value class Email(val value: String) {
    init {
        require(value.contains("@")) { "Invalid email" }
    }
}

Error Handling
Result Type
fun parseNumber(input: String): Result<Int> {
    return try {
        Result.success(input.toInt())
    } catch (e: NumberFormatException) {
        Result.failure(e)
    }
}

// Usage
parseNumber("123")
    .onSuccess { number -> println("Parsed: $number") }
    .onFailure { error -> println("Error: ${error.message}") }

// Transform
val doubled = parseNumber("42")
    .map { it * 2 }
    .getOrDefault(0)

runCatching
val result = runCatching {
    riskyOperation()
}.getOrElse { error ->
    logError(error)
    defaultValue
}

// Chain operations
runCatching { fetchUser(id) }
    .mapCatching { user -> processUser(user) }
    .onSuccess { result -> display(result) }
    .onFailure { error -> showError(error) }

Coroutines
Basic Coroutines
// Suspend function
suspend fun fetchUser(id: String): User {
    return withContext(Dispatchers.IO) {
        api.getUser(id)
    }
}

// Launch coroutine
viewModelScope.launch {
    try {
        val user = fetchUser("123")
        _uiState.value = UiState.Success(user)
    } catch (e: Exception) {
        _uiState.value = UiState.Error(e.message)
    }
}

Flow
// Create flow
fun observeUsers(): Flow<List<User>> = flow {
    while (true) {
        emit(repository.getUsers())
        delay(5000)
    }
}.flowOn(Dispatchers.IO)

// Collect flow
viewModelScope.launch {
    observeUsers()
        .catch { e -> emit(emptyList()) }
        .collect { users ->
            _users.value = users
        }
}

StateFlow
class UserViewModel : ViewModel() {
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()

    fun loadUser(id: String) {
        viewModelScope.launch {
            _uiState.value = UiState.Loading
            try {
                val user = repository.getUser(id)
                _uiState.value = UiState.Success(user)
            } catch (e: Exception) {
                _uiState.value = UiState.Error(e.message ?: "Unknown error")
            }
        }
    }
}

Jetpack Compose
Basic Composable
@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello, $name!",
        modifier = modifier.padding(16.dp),
        style = MaterialTheme.typography.headlineMedium
    )
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    MyAppTheme {
        Greeting("Android")
    }
}

State Management
@Composable
fun Counter() {
    var count by remember { mutableIntStateOf(0) }

    Column(
        modifier = Modifier.padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(
            text = "Count: $count",
            style = MaterialTheme.typography.headlineMedium
        )
        Spacer(modifier = Modifier.height(8.dp))
        Button(onClick = { count++ }) {
            Text("Increment")
        }
    }
}

ViewModel Integration
@Composable
fun UserScreen(
    viewModel: UserViewModel = hiltViewModel()
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    when (val state = uiState) {
        is UiState.Loading -> CircularProgressIndicator()
        is UiState.Success -> UserContent(state.user)
        is UiState.Error -> ErrorMessage(state.message)
    }
}

@Composable
fun UserContent(user: User) {
    Column(modifier = Modifier.padding(16.dp)) {
        Text(user.name, style = MaterialTheme.typography.titleLarge)
        Text(user.email, style = MaterialTheme.typography.bodyMedium)
    }
}

Side Effects
@Composable
fun UserDetailScreen(userId: String, viewModel: UserViewModel = hiltViewModel()) {
    // Run once when userId changes
    LaunchedEffect(userId) {
        viewModel.loadUser(userId)
    }

    // Run on every recomposition
    SideEffect {
        analytics.trackScreen("UserDetail")
    }

    // Cleanup when leaving composition
    DisposableEffect(Unit) {
        val listener = viewModel.addListener()
        onDispose {
            listener.remove()
        }
    }
}

Testing
Unit Tests (JUnit 5)
class UserViewModelTest {
    @Test
    fun `loadUser updates state to success`() = runTest {
        val repository = mockk<UserRepository>()
        coEvery { repository.getUser("123") } returns User("123", "test@example.com")

        val viewModel = UserViewModel(repository)
        viewModel.loadUser("123")

        assertEquals(
            UiState.Success(User("123", "test@example.com")),
            viewModel.uiState.value
        )
    }

    @Test
    fun `loadUser updates state to error on failure`() = runTest {
        val repository = mockk<UserRepository>()
        coEvery { repository.getUser(any()) } throws IOException("Network error")

        val viewModel = UserViewModel(repository)
        viewModel.loadUser("123")

        assertTrue(viewModel.uiState.value is UiState.Error)
    }
}

Compose UI Tests
class UserScreenTest {
    @get:Rule
    val composeTestRule = createComposeRule()

    @Test
    fun displaysUserName() {
        val user = User("1", "test@example.com", "John Doe")

        composeTestRule.setContent {
            MyAppTheme {
                UserContent(user = user)
            }
        }

        composeTestRule.onNodeWithText("John Doe").assertIsDisplayed()
        composeTestRule.onNodeWithText("test@example.com").assertIsDisplayed()
    }

    @Test
    fun buttonClickIncrementsCounter() {
        composeTestRule.setContent {
            MyAppTheme {
                Counter()
            }
        }

        composeTestRule.onNodeWithText("Count: 0").assertIsDisplayed()
        composeTestRule.onNodeWithText("Increment").performClick()
        composeTestRule.onNodeWithText("Count: 1").assertIsDisplayed()
    }
}

Tooling
# Build
./gradlew build
./gradlew assembleDebug
./gradlew assembleRelease

# Run tests
./gradlew test                          # Unit tests
./gradlew connectedAndroidTest          # Instrumented tests

# Linting
./gradlew detekt                        # Code smells
./gradlew ktlintCheck                   # Style check
./gradlew ktlintFormat                  # Auto-fix style

# Code analysis
./gradlew lint                          # Android Lint

# Clean
./gradlew clean

detekt.yml
build:
  maxIssues: 0

complexity:
  LongMethod:
    threshold: 30
  ComplexCondition:
    threshold: 4

style:
  MaxLineLength:
    maxLineLength: 120
  WildcardImport:
    active: true

naming:
  FunctionNaming:
    functionPattern: '[a-z][a-zA-Z0-9]*'

.editorconfig (ktlint)
[*.{kt,kts}]
indent_size = 4
max_line_length = 120
ktlint_code_style = android_studio

Weekly Installs
32
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass