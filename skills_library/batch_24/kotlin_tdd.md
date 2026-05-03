---
title: kotlin-tdd
url: https://skills.sh/anderssv/the-example/kotlin-tdd
---

# kotlin-tdd

skills/anderssv/the-example/kotlin-tdd
kotlin-tdd
Installation
$ npx skills add https://github.com/anderssv/the-example --skill kotlin-tdd
SKILL.md

STARTER_CHARACTER = 🧪

Kotlin TDD approach built on three pillars: Test Setup, Fakes, and Testing Through The Domain (TTTD).

Test qualities to aim for
Predictable (not flaky)
Readable
Easy to write
Maintainable (resistant to irrelevant changes)
Fast (all in-memory)
Three pillars
1. Test Setup

Extension functions on companion objects create test data with sensible defaults.

// In test source: TestExtensions.kt
fun Customer.Companion.valid() = Customer(
    id = UUID.randomUUID(),
    name = "Test Customer",
    active = true,
)

fun Application.Companion.valid(
    customerId: UUID,
    monthsOld: Long = 0,  // Helper for complex setup
) = Application(
    id = UUID.randomUUID(),
    customerId = customerId,
    name = "Tester One",
    birthDate = LocalDate.of(1978, 2, 23),
    applicationDate = LocalDate.now().minusMonths(monthsOld),
    status = ApplicationStatus.ACTIVE,
)


Use .copy() for simple variations:

val deniedApp = Application.valid(customer.id).copy(status = ApplicationStatus.DENIED)


Use helper parameters for complex variations that would be verbose with .copy().

For detailed patterns, see test-setup.md.

2. Fakes

HashMap-based implementations that replace real dependencies. No mocking frameworks needed.

class ApplicationRepositoryFake : ApplicationRepository {
    private val db = mutableMapOf<UUID, Application>()

    override fun addApplication(application: Application) {
        db[application.id] = application
    }

    override fun getApplication(applicationId: UUID): Application = db[applicationId]!!

    override fun getApplicationsForName(name: String): List<Application> =
        db.values.filter { it.name == name }
}


For verification and error testing patterns, see fakes.md.

3. Testing Through The Domain (TTTD)

Set up test state using domain operations, not direct data manipulation.

// Data-oriented (brittle)
repositories.applicationRepo.addApplication(application)
applicationService.approveApplication(application.id)

// Domain-oriented (resilient)
applicationService.registerInitialApplication(customer, application)
applicationService.approveApplication(application.id)


The domain-oriented version survives changes to domain logic. When registerInitialApplication adds customer validation, tests using the domain approach keep working.

For detailed explanation, see tttd.md.

SystemTestContext pattern

Central test context with fakes injected:

class SystemTestContext : SystemContext() {
    class Repositories : SystemContext.Repositories() {
        override val applicationRepo = ApplicationRepositoryFake()
        override val customerRepository = CustomerRepositoryFake()
    }

    class Clients : SystemContext.Clients() {
        override val userNotificationClient = UserNotificationClientFake()
    }

    override val repositories = Repositories()
    override val clients = Clients()
    override val clock = TestClock.now()
}


Usage in tests:

class ApplicationTest {
    private val testContext = SystemTestContext()

    @Test
    fun shouldApproveApplication() {
        with(testContext) {
            val customer = Customer.valid()
            val application = Application.valid(customer.id)

            applicationService.registerInitialApplication(customer, application)
            applicationService.approveApplication(application.id)

            assertThat(repositories.applicationRepo.getApplication(application.id).status)
                .isEqualTo(ApplicationStatus.APPROVED)
        }
    }
}

TestClock for time control
class TestClock private constructor(private var dateTime: ZonedDateTime) : Clock() {
    companion object {
        fun at(dateTime: ZonedDateTime): TestClock = TestClock(dateTime)
        fun now(): TestClock = at(ZonedDateTime.now())
    }

    override fun instant(): Instant = dateTime.toInstant()
    override fun withZone(zone: ZoneId?): Clock = TestClock(dateTime.withZoneSameInstant(zone ?: ZoneId.systemDefault()))
    override fun getZone(): ZoneId = dateTime.zone

    fun advance(duration: Duration) { dateTime = dateTime.plus(duration) }
    fun setTo(newDateTime: ZonedDateTime) { dateTime = newDateTime }
    fun setTo(localDate: LocalDate) { dateTime = localDate.atStartOfDay(dateTime.zone) }
}


Usage:

@Test
fun shouldExpireOldApplications() {
    with(testContext) {
        clock.setTo(LocalDate.of(2022, 1, 1))
        val customer = Customer.valid()
        val application = Application.valid(customer.id)
        applicationService.registerInitialApplication(customer, application)

        clock.advance(Duration.ofDays(7 * 30))  // 7 months later
        applicationService.expireApplications()

        assertThat(applicationService.activeApplicationFor(application.name))
            .doesNotContain(application)
    }
}

Test types
Domain tests (no fakes): Pure business logic, no I/O
IO tests (no fakes): HTTP calls, SQL queries - verify adapter correctness
Variation tests (with fakes): Edge cases, specific variations
Outcome tests (with fakes): Interactions between components, end-to-end flows
When to use real implementations vs fakes

Use real database/HTTP tests when:

Testing JSONB/JSON serialization behavior
Verifying SQL query correctness (joins, indexes, edge cases)
Testing database-specific features (constraints, triggers, transactions)
Validating migration scripts work correctly
Testing HTTP client response parsing and error handling

Use fakes when:

Testing business logic and domain rules
Testing component interactions
Most outcome/variation tests
Speed matters (fakes are in-memory, real DBs are slow)
Test tagging

Use JUnit tags to run test subsets:

@Tag("unit")
class DomainLogicTest { ... }

@Tag("integration")
class DatabaseRepositoryTest { ... }

@Tag("database")
class JsonbSerializationTest { ... }

@Tag("e2e")
class FullFlowTest { ... }


Run specific tags:

./gradlew test -Dinclude.tags=unit
./gradlew test -Dexclude.tags=e2e

Parallel-safe assertions

Whether using shared databases or shared fake instances, always set up unique data and assert on that specific data. Never assert on absolute counts or global state:

// BAD - fails when other tests create data concurrently
assertThat(repository.getAllPolls()).hasSize(1)
assertThat(repository.count()).isEqualTo(5)

// GOOD - verify specific data you created using its ID
val poll = repository.findPollById(myPollId)
assertThat(poll).isNotNull
assertThat(poll.title).isEqualTo("My Poll")

// GOOD - filter to your specific test data
assertThat(repository.getAllPolls())
    .anyMatch { it.id == myPollId }


Key principles:

Each test creates its own data with unique IDs (UUIDs)
Query by the specific ID you created, not by position or count
Use anyMatch/contains instead of hasSize when checking lists
Fakes should be per-test-instance, not shared across tests
Anti-patterns
Using mocks when fakes would work (fakes are reusable, mocks are not)
Setting up test data directly in repositories instead of through domain operations
Verifying method calls instead of system state
Creating new test data factories for each test file (centralize in TestExtensions.kt)
Testing DTOs at interface boundaries (interfaces should use domain objects)
When mocks are appropriate

Mocks are rarely needed but are the right choice for testing HTTP protocol behavior (status codes, timeouts, retries, headers). For everything else, prefer fakes. See fakes.md for detailed comparison and examples.

Weekly Installs
22
Repository
anderssv/the-example
GitHub Stars
13
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass