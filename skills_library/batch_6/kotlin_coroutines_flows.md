---
title: kotlin-coroutines-flows
url: https://skills.sh/affaan-m/everything-claude-code/kotlin-coroutines-flows
---

# kotlin-coroutines-flows

skills/affaan-m/everything-claude-code/kotlin-coroutines-flows
kotlin-coroutines-flows
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill kotlin-coroutines-flows
SKILL.md
Kotlin Coroutines & Flows

Patterns for structured concurrency, Flow-based reactive streams, and coroutine testing in Android and Kotlin Multiplatform projects.

When to Activate
Writing async code with Kotlin coroutines
Using Flow, StateFlow, or SharedFlow for reactive data
Handling concurrent operations (parallel loading, debounce, retry)
Testing coroutines and Flows
Managing coroutine scopes and cancellation
Structured Concurrency
Scope Hierarchy
Application
  └── viewModelScope (ViewModel)
        └── coroutineScope { } (structured child)
              ├── async { } (concurrent task)
              └── async { } (concurrent task)


Always use structured concurrency — never GlobalScope:

// BAD
GlobalScope.launch { fetchData() }

// GOOD — scoped to ViewModel lifecycle
viewModelScope.launch { fetchData() }

// GOOD — scoped to composable lifecycle
LaunchedEffect(key) { fetchData() }

Parallel Decomposition

Use coroutineScope + async for parallel work:

suspend fun loadDashboard(): Dashboard = coroutineScope {
    val items = async { itemRepository.getRecent() }
    val stats = async { statsRepository.getToday() }
    val profile = async { userRepository.getCurrent() }
    Dashboard(
        items = items.await(),
        stats = stats.await(),
        profile = profile.await()
    )
}

SupervisorScope

Use supervisorScope when child failures should not cancel siblings:

suspend fun syncAll() = supervisorScope {
    launch { syncItems() }       // failure here won't cancel syncStats
    launch { syncStats() }
    launch { syncSettings() }
}

Flow Patterns
Cold Flow — One-Shot to Stream Conversion
fun observeItems(): Flow<List<Item>> = flow {
    // Re-emits whenever the database changes
    itemDao.observeAll()
        .map { entities -> entities.map { it.toDomain() } }
        .collect { emit(it) }
}

StateFlow for UI State
class DashboardViewModel(
    observeProgress: ObserveUserProgressUseCase
) : ViewModel() {
    val progress: StateFlow<UserProgress> = observeProgress()
        .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5_000),
            initialValue = UserProgress.EMPTY
        )
}


WhileSubscribed(5_000) keeps the upstream active for 5 seconds after the last subscriber leaves — survives configuration changes without restarting.

Combining Multiple Flows
val uiState: StateFlow<HomeState> = combine(
    itemRepository.observeItems(),
    settingsRepository.observeTheme(),
    userRepository.observeProfile()
) { items, theme, profile ->
    HomeState(items = items, theme = theme, profile = profile)
}.stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), HomeState())

Flow Operators
// Debounce search input
searchQuery
    .debounce(300)
    .distinctUntilChanged()
    .flatMapLatest { query -> repository.search(query) }
    .catch { emit(emptyList()) }
    .collect { results -> _state.update { it.copy(results = results) } }

// Retry with exponential backoff
fun fetchWithRetry(): Flow<Data> = flow { emit(api.fetch()) }
    .retryWhen { cause, attempt ->
        if (cause is IOException && attempt < 3) {
            delay(1000L * (1 shl attempt.toInt()))
            true
        } else {
            false
        }
    }

SharedFlow for One-Time Events
class ItemListViewModel : ViewModel() {
    private val _effects = MutableSharedFlow<Effect>()
    val effects: SharedFlow<Effect> = _effects.asSharedFlow()

    sealed interface Effect {
        data class ShowSnackbar(val message: String) : Effect
        data class NavigateTo(val route: String) : Effect
    }

    private fun deleteItem(id: String) {
        viewModelScope.launch {
            repository.delete(id)
            _effects.emit(Effect.ShowSnackbar("Item deleted"))
        }
    }
}

// Collect in Composable
LaunchedEffect(Unit) {
    viewModel.effects.collect { effect ->
        when (effect) {
            is Effect.ShowSnackbar -> snackbarHostState.showSnackbar(effect.message)
            is Effect.NavigateTo -> navController.navigate(effect.route)
        }
    }
}

Dispatchers
// CPU-intensive work
withContext(Dispatchers.Default) { parseJson(largePayload) }

// IO-bound work
withContext(Dispatchers.IO) { database.query() }

// Main thread (UI) — default in viewModelScope
withContext(Dispatchers.Main) { updateUi() }


In KMP, use Dispatchers.Default and Dispatchers.Main (available on all platforms). Dispatchers.IO is JVM/Android only — use Dispatchers.Default on other platforms or provide via DI.

Cancellation
Cooperative Cancellation

Long-running loops must check for cancellation:

suspend fun processItems(items: List<Item>) = coroutineScope {
    for (item in items) {
        ensureActive()  // throws CancellationException if cancelled
        process(item)
    }
}

Cleanup with try/finally
viewModelScope.launch {
    try {
        _state.update { it.copy(isLoading = true) }
        val data = repository.fetch()
        _state.update { it.copy(data = data) }
    } finally {
        _state.update { it.copy(isLoading = false) }  // always runs, even on cancellation
    }
}

Testing
Testing StateFlow with Turbine
@Test
fun `search updates item list`() = runTest {
    val fakeRepository = FakeItemRepository().apply { emit(testItems) }
    val viewModel = ItemListViewModel(GetItemsUseCase(fakeRepository))

    viewModel.state.test {
        assertEquals(ItemListState(), awaitItem())  // initial

        viewModel.onSearch("query")
        val loading = awaitItem()
        assertTrue(loading.isLoading)

        val loaded = awaitItem()
        assertFalse(loaded.isLoading)
        assertEquals(1, loaded.items.size)
    }
}

Testing with TestDispatcher
@Test
fun `parallel load completes correctly`() = runTest {
    val viewModel = DashboardViewModel(
        itemRepo = FakeItemRepo(),
        statsRepo = FakeStatsRepo()
    )

    viewModel.load()
    advanceUntilIdle()

    val state = viewModel.state.value
    assertNotNull(state.items)
    assertNotNull(state.stats)
}

Faking Flows
class FakeItemRepository : ItemRepository {
    private val _items = MutableStateFlow<List<Item>>(emptyList())

    override fun observeItems(): Flow<List<Item>> = _items

    fun emit(items: List<Item>) { _items.value = items }

    override suspend fun getItemsByCategory(category: String): Result<List<Item>> {
        return Result.success(_items.value.filter { it.category == category })
    }
}

Anti-Patterns to Avoid
Using GlobalScope — leaks coroutines, no structured cancellation
Collecting Flows in init {} without a scope — use viewModelScope.launch
Using MutableStateFlow with mutable collections — always use immutable copies: _state.update { it.copy(list = it.list + newItem) }
Catching CancellationException — let it propagate for proper cancellation
Using flowOn(Dispatchers.Main) to collect — collection dispatcher is the caller's dispatcher
Creating Flow in @Composable without remember — recreates the flow every recomposition
References

See skill: compose-multiplatform-patterns for UI consumption of Flows. See skill: android-clean-architecture for where coroutines fit in layers.

Weekly Installs
2.6K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass