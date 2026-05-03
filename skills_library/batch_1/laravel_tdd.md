---
title: laravel-tdd
url: https://skills.sh/affaan-m/everything-claude-code/laravel-tdd
---

# laravel-tdd

skills/affaan-m/everything-claude-code/laravel-tdd
laravel-tdd
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill laravel-tdd
SKILL.md
Laravel TDD Workflow

Test-driven development for Laravel applications using PHPUnit and Pest with 80%+ coverage (unit + feature).

When to Use
New features or endpoints in Laravel
Bug fixes or refactors
Testing Eloquent models, policies, jobs, and notifications
Prefer Pest for new tests unless the project already standardizes on PHPUnit
How It Works
Red-Green-Refactor Cycle
Write a failing test
Implement the minimal change to pass
Refactor while keeping tests green
Test Layers
Unit: pure PHP classes, value objects, services
Feature: HTTP endpoints, auth, validation, policies
Integration: database + queue + external boundaries

Choose layers based on scope:

Use Unit tests for pure business logic and services.
Use Feature tests for HTTP, auth, validation, and response shape.
Use Integration tests when validating DB/queues/external services together.
Database Strategy
RefreshDatabase for most feature/integration tests (runs migrations once per test run, then wraps each test in a transaction when supported; in-memory databases may re-migrate per test)
DatabaseTransactions when the schema is already migrated and you only need per-test rollback
DatabaseMigrations when you need a full migrate/fresh for every test and can afford the cost

Use RefreshDatabase as the default for tests that touch the database: for databases with transaction support, it runs migrations once per test run (via a static flag) and wraps each test in a transaction; for :memory: SQLite or connections without transactions, it migrates before each test. Use DatabaseTransactions when the schema is already migrated and you only need per-test rollbacks.

Testing Framework Choice
Default to Pest for new tests when available.
Use PHPUnit only if the project already standardizes on it or requires PHPUnit-specific tooling.
Examples
PHPUnit Example
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

final class ProjectControllerTest extends TestCase
{
    use RefreshDatabase;

    public function test_owner_can_create_project(): void
    {
        $user = User::factory()->create();

        $response = $this->actingAs($user)->postJson('/api/projects', [
            'name' => 'New Project',
        ]);

        $response->assertCreated();
        $this->assertDatabaseHas('projects', ['name' => 'New Project']);
    }
}

Feature Test Example (HTTP Layer)
use App\Models\Project;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

final class ProjectIndexTest extends TestCase
{
    use RefreshDatabase;

    public function test_projects_index_returns_paginated_results(): void
    {
        $user = User::factory()->create();
        Project::factory()->count(3)->for($user)->create();

        $response = $this->actingAs($user)->getJson('/api/projects');

        $response->assertOk();
        $response->assertJsonStructure(['success', 'data', 'error', 'meta']);
    }
}

Pest Example
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;

use function Pest\Laravel\actingAs;
use function Pest\Laravel\assertDatabaseHas;

uses(RefreshDatabase::class);

test('owner can create project', function () {
    $user = User::factory()->create();

    $response = actingAs($user)->postJson('/api/projects', [
        'name' => 'New Project',
    ]);

    $response->assertCreated();
    assertDatabaseHas('projects', ['name' => 'New Project']);
});

Feature Test Pest Example (HTTP Layer)
use App\Models\Project;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;

use function Pest\Laravel\actingAs;

uses(RefreshDatabase::class);

test('projects index returns paginated results', function () {
    $user = User::factory()->create();
    Project::factory()->count(3)->for($user)->create();

    $response = actingAs($user)->getJson('/api/projects');

    $response->assertOk();
    $response->assertJsonStructure(['success', 'data', 'error', 'meta']);
});

Factories and States
Use factories for test data
Define states for edge cases (archived, admin, trial)
$user = User::factory()->state(['role' => 'admin'])->create();

Database Testing
Use RefreshDatabase for clean state
Keep tests isolated and deterministic
Prefer assertDatabaseHas over manual queries
Persistence Test Example
use App\Models\Project;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

final class ProjectRepositoryTest extends TestCase
{
    use RefreshDatabase;

    public function test_project_can_be_retrieved_by_slug(): void
    {
        $project = Project::factory()->create(['slug' => 'alpha']);

        $found = Project::query()->where('slug', 'alpha')->firstOrFail();

        $this->assertSame($project->id, $found->id);
    }
}

Fakes for Side Effects
Bus::fake() for jobs
Queue::fake() for queued work
Mail::fake() and Notification::fake() for notifications
Event::fake() for domain events
use Illuminate\Support\Facades\Queue;

Queue::fake();

dispatch(new SendOrderConfirmation($order->id));

Queue::assertPushed(SendOrderConfirmation::class);

use Illuminate\Support\Facades\Notification;

Notification::fake();

$user->notify(new InvoiceReady($invoice));

Notification::assertSentTo($user, InvoiceReady::class);

Auth Testing (Sanctum)
use Laravel\Sanctum\Sanctum;

Sanctum::actingAs($user);

$response = $this->getJson('/api/projects');
$response->assertOk();

HTTP and External Services
Use Http::fake() to isolate external APIs
Assert outbound payloads with Http::assertSent()
Coverage Targets
Enforce 80%+ coverage for unit + feature tests
Use pcov or XDEBUG_MODE=coverage in CI
Test Commands
php artisan test
vendor/bin/phpunit
vendor/bin/pest
Test Configuration
Use phpunit.xml to set DB_CONNECTION=sqlite and DB_DATABASE=:memory: for fast tests
Keep separate env for tests to avoid touching dev/prod data
Authorization Tests
use Illuminate\Support\Facades\Gate;

$this->assertTrue(Gate::forUser($user)->allows('update', $project));
$this->assertFalse(Gate::forUser($otherUser)->allows('update', $project));

Inertia Feature Tests

When using Inertia.js, assert on the component name and props with the Inertia testing helpers.

use App\Models\User;
use Inertia\Testing\AssertableInertia;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

final class DashboardInertiaTest extends TestCase
{
    use RefreshDatabase;

    public function test_dashboard_inertia_props(): void
    {
        $user = User::factory()->create();

        $response = $this->actingAs($user)->get('/dashboard');

        $response->assertOk();
        $response->assertInertia(fn (AssertableInertia $page) => $page
            ->component('Dashboard')
            ->where('user.id', $user->id)
            ->has('projects')
        );
    }
}


Prefer assertInertia over raw JSON assertions to keep tests aligned with Inertia responses.

Weekly Installs
2.4K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass