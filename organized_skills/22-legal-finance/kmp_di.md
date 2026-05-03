---
rating: ⭐⭐
title: kmp-di
url: https://skills.sh/ahmed3elshaer/everything-claude-code-mobile/kmp-di
---

# kmp-di

skills/ahmed3elshaer/everything-claude-code-mobile/kmp-di
kmp-di
Installation
$ npx skills add https://github.com/ahmed3elshaer/everything-claude-code-mobile --skill kmp-di
SKILL.md
KMP Dependency Injection

Cross-platform dependency injection with Koin.

Koin Multiplatform Setup
Dependencies
// build.gradle.kts (shared module)
sourceSets {
    val commonMain by getting {
        dependencies {
            implementation("io.insert-koin:koin-core:${koinVersion}")
            implementation("io.insert-koin:koin-test:${koinVersion}")
        }
    }
    val androidMain by getting {
        dependencies {
            implementation("io.insert-koin:koin-android:${koinVersion}")
        }
    }
}

Module Definition
// commonMain/kotlin/di/AppModule.kt
val sharedModule = module {
    // ViewModels (Android) / ScreenModels (multiplatform)
    factory { HomeViewModel(get(), get()) }
    factory { DetailViewModel(get()) }

    // Use Cases
    factory { GetUsersUseCase(get()) }
    factory { GetUserDetailUseCase(get()) }

    // Repositories
    single<UserRepository> { UserRepositoryImpl(get(), get()) }

    // Data Sources
    single { UserApi(get()) }
    single { createDatabase(get()) }
}

Platform Modules
// androidMain/kotlin/di/PlatformModule.kt
val androidPlatformModule = module {
    includes(sharedModule)

    // Android-specific dependencies
    single { android.content.Context() }
    single { PlatformConnectivityMonitor(get()) }
    single { PlatformFileService(get()) }
}

// iosMain/kotlin/di/PlatformModule.kt
val iosPlatformModule = module {
    includes(sharedModule)

    // iOS-specific dependencies
    single { PlatformConnectivityMonitor() }
    single { PlatformFileService() }
}

Koin Start
Android
// androidMain/kotlin/MyApp.kt
class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        startKoin {
            androidContext(this@MyApp)
            modules(androidPlatformModule)
        }
    }
}

iOS
// iosMain/kotlin/di/KoinInit.kt
fun initKoin() {
    startKoin {
        modules(iosPlatformModule)
    }
}

// Called from Swift
// KotlinKMMSharedKt.doInitKoin()

Compose Multiplatform
// commonMain/kotlin/Main.kt
fun main() {
    startKoin {
        modules(sharedModule)
    }

    App()
}

ViewModel Injection
Android (ViewModel)
// androidMain/kotlin/ui/HomeScreen.kt
@Composable
fun HomeScreen(
    viewModel: HomeViewModel = koinViewModel()
) {
    val state by viewModel.state.collectAsStateWithLifecycle()
    HomeContent(state)
}

iOS (ScreenModel)
// commonMain/kotlin/ui/HomeScreen.kt
@Composable
fun HomeScreen() {
    val model = getScreenModel<HomeScreenModel>()
    val state by model.state.collectAsState()

    HomeContent(state)
}

Repository Pattern
Factory vs Single
// ✅ factory - creates new instance each time
factory { HomeViewModel(get(), get()) }

// ✅ single - shared instance
single<UserRepository> { UserRepositoryImpl(get(), get()) }

// ✅ scoped - tied to component lifetime
scoped(HomeScope.homeScope) { HomeData(get()) }

Named Dependencies
// ✅ Named dependencies
module {
    single(named("default")) { DefaultLogger() }
    single(named("analytics")) { AnalyticsLogger() }

    factory { MyRepository(logger = get(named("default"))) }
}

Manual DI (Alternative)
Simple Service Locator
// commonMain/kotlin/di/ServiceLocator.kt
object ServiceLocator {
    private val services = mutableMapOf<String, Any>()

    fun <T> get(key: String): T {
        return services[key] as T
    }

    fun register(key: String, service: Any) {
        services[key] = service
    }

    fun init() {
        register("repository", UserRepositoryImpl())
        register("api", UserApi())
    }
}

Pure Kotlin DI
// commonMain/kotlin/di/AppContainer.kt
class AppContainer(
    private val platformService: PlatformService
) {
    val api: UserApi = UserApi()
    val database: AppDatabase = createDatabase()

    val userRepository: UserRepository by lazy {
        UserRepositoryImpl(api, database)
    }

    val homeViewModel: HomeViewModel by lazy {
        HomeViewModel(userRepository, platformService)
    }
}

Testing with DI
// commonTest/kotlin/di/TestModule.kt
val testModule = module {
    single<MockUserService> { MockUserService() }
    single<UserService>(override = true) { get<MockUserService>() }
}

// In tests
@BeforeTest
fun setup() {
    startKoin { modules(testModule) }
}

@AfterTest
fun tearDown() {
    stopKoin()
}


Remember: DI simplifies testing. Use it to inject mocks and fakes easily.

Weekly Installs
16
Repository
ahmed3elshaer/e…e-mobile
GitHub Stars
42
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass