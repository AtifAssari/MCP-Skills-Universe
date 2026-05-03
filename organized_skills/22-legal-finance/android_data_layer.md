---
rating: ⭐⭐
title: android-data-layer
url: https://skills.sh/new-silvermoon/awesome-android-agent-skills/android-data-layer
---

# android-data-layer

skills/new-silvermoon/awesome-android-agent-skills/android-data-layer
android-data-layer
Installation
$ npx skills add https://github.com/new-silvermoon/awesome-android-agent-skills --skill android-data-layer
SKILL.md
Android Data Layer & Offline-First
Instructions

The Data Layer coordinates data from multiple sources.

1. Repository Pattern
Role: Single Source of Truth (SSOT).
Logic: The repository decides whether to return cached data or fetch fresh data.
Implementation:
class NewsRepository @Inject constructor(
    private val newsDao: NewsDao,
    private val newsApi: NewsApi
) {
    // Expose data from Local DB as the source of truth
    val newsStream: Flow<List<News>> = newsDao.getAllNews()

    // Sync operation
    suspend fun refreshNews() {
        val remoteNews = newsApi.fetchLatest()
        newsDao.insertAll(remoteNews)
    }
}

2. Local Persistence (Room)
Usage: Primary cache and offline storage.
Entities: Define @Entity data classes.
DAOs: Return Flow<T> for observable data.
3. Remote Data (Retrofit)
Usage: Fetching data from backend.
Response: Use suspend functions in interfaces.
Error Handling: Wrap network calls in try-catch blocks or a Result wrapper to handle exceptions (NoInternet, 404, etc.) gracefully.
4. Synchronization
Read: "Stale-While-Revalidate". Show local data immediately, trigger a background refresh.
Write: "Outbox Pattern" (Advanced). Save local change immediately, mark as "unsynced", use WorkManager to push changes to server.
5. Dependency Injection
Bind Repository interfaces to implementations in a Hilt Module.
@Binds
abstract fun bindNewsRepository(impl: OfflineFirstNewsRepository): NewsRepository

Weekly Installs
258
Repository
new-silvermoon/…t-skills
GitHub Stars
778
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass