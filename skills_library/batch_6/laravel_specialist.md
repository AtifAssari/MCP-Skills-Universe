---
title: laravel-specialist
url: https://skills.sh/jeffallan/claude-skills/laravel-specialist
---

# laravel-specialist

skills/jeffallan/claude-skills/laravel-specialist
laravel-specialist
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill laravel-specialist
Summary

Build and configure Laravel 10+ applications with Eloquent models, Sanctum auth, queues, and Livewire components.

Covers Eloquent ORM with relationships, scopes, and query optimization; API resource design; and RESTful controller patterns
Implements queue jobs with Horizon, Sanctum authentication flows, and reactive Livewire interfaces
Enforces PHP 8.2+ typing, eager loading to prevent N+1 queries, comprehensive testing (>85% coverage), and PSR-12 standards
Includes code templates for models, migrations, API resources, jobs, and Pest feature tests with validation checkpoints at each workflow stage
SKILL.md
Laravel Specialist

Senior Laravel specialist with deep expertise in Laravel 10+, Eloquent ORM, and modern PHP 8.2+ development.

Core Workflow
Analyse requirements — Identify models, relationships, APIs, and queue needs
Design architecture — Plan database schema, service layers, and job queues
Implement models — Create Eloquent models with relationships, scopes, and casts; run php artisan make:model and verify with php artisan migrate:status
Build features — Develop controllers, services, API resources, and jobs; run php artisan route:list to verify routing
Test thoroughly — Write feature and unit tests; run php artisan test before considering any step complete (target >85% coverage)
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Eloquent ORM	references/eloquent.md	Models, relationships, scopes, query optimization
Routing & APIs	references/routing.md	Routes, controllers, middleware, API resources
Queue System	references/queues.md	Jobs, workers, Horizon, failed jobs, batching
Livewire	references/livewire.md	Components, wire:model, actions, real-time
Testing	references/testing.md	Feature tests, factories, mocking, Pest PHP
Constraints
MUST DO
Use PHP 8.2+ features (readonly, enums, typed properties)
Type hint all method parameters and return types
Use Eloquent relationships properly (avoid N+1 with eager loading)
Implement API resources for transforming data
Queue long-running tasks
Write comprehensive tests (>85% coverage)
Use service containers and dependency injection
Follow PSR-12 coding standards
MUST NOT DO
Use raw queries without protection (SQL injection)
Skip eager loading (causes N+1 problems)
Store sensitive data unencrypted
Mix business logic in controllers
Hardcode configuration values
Skip validation on user input
Use deprecated Laravel features
Ignore queue failures
Code Templates

Use these as starting points for every implementation.

Eloquent Model
<?php

declare(strict_types=1);

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\SoftDeletes;

final class Post extends Model
{
    use HasFactory, SoftDeletes;

    protected $fillable = ['title', 'body', 'status', 'user_id'];

    protected $casts = [
        'status' => PostStatus::class, // backed enum
        'published_at' => 'immutable_datetime',
    ];

    // Relationships — always eager-load via ::with() at call site
    public function author(): BelongsTo
    {
        return $this->belongsTo(User::class, 'user_id');
    }

    public function comments(): HasMany
    {
        return $this->hasMany(Comment::class);
    }

    // Local scope
    public function scopePublished(Builder $query): Builder
    {
        return $query->where('status', PostStatus::Published);
    }
}

Migration
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('posts', function (Blueprint $table): void {
            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->string('title');
            $table->text('body');
            $table->string('status')->default('draft');
            $table->timestamp('published_at')->nullable();
            $table->softDeletes();
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('posts');
    }
};

API Resource
<?php

declare(strict_types=1);

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

final class PostResource extends JsonResource
{
    public function toArray(Request $request): array
    {
        return [
            'id'           => $this->id,
            'title'        => $this->title,
            'body'         => $this->body,
            'status'       => $this->status->value,
            'published_at' => $this->published_at?->toIso8601String(),
            'author'       => new UserResource($this->whenLoaded('author')),
            'comments'     => CommentResource::collection($this->whenLoaded('comments')),
        ];
    }
}

Queued Job
<?php

declare(strict_types=1);

namespace App\Jobs;

use App\Models\Post;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Queue\SerializesModels;

final class PublishPost implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public int $tries = 3;
    public int $backoff = 60;

    public function __construct(
        private readonly Post $post,
    ) {}

    public function handle(): void
    {
        $this->post->update([
            'status'       => PostStatus::Published,
            'published_at' => now(),
        ]);
    }

    public function failed(\Throwable $e): void
    {
        // Log or notify — never silently swallow failures
        logger()->error('PublishPost failed', ['post' => $this->post->id, 'error' => $e->getMessage()]);
    }
}

Feature Test (Pest)
<?php

use App\Models\Post;
use App\Models\User;

it('returns a published post for authenticated users', function (): void {
    $user = User::factory()->create();
    $post = Post::factory()->published()->for($user, 'author')->create();

    $response = $this->actingAs($user)
        ->getJson("/api/posts/{$post->id}");

    $response->assertOk()
        ->assertJsonPath('data.status', 'published')
        ->assertJsonPath('data.author.id', $user->id);
});

it('queues a publish job when a draft is submitted', function (): void {
    Queue::fake();
    $user = User::factory()->create();
    $post = Post::factory()->draft()->for($user, 'author')->create();

    $this->actingAs($user)
        ->postJson("/api/posts/{$post->id}/publish")
        ->assertAccepted();

    Queue::assertPushed(PublishPost::class, fn ($job) => $job->post->is($post));
});

Validation Checkpoints

Run these at each workflow stage to confirm correctness before proceeding:

Stage	Command	Expected Result
After migration	php artisan migrate:status	All migrations show Ran
After routing	php artisan route:list --path=api	New routes appear with correct verbs
After job dispatch	php artisan queue:work --once	Job processes without exception
After implementation	php artisan test --coverage	>85% coverage, 0 failures
Before PR	./vendor/bin/pint --test	PSR-12 linting passes
Knowledge Reference

Laravel 10+, Eloquent ORM, PHP 8.2+, API resources, Sanctum/Passport, queues, Horizon, Livewire, Inertia, Octane, Pest/PHPUnit, Redis, broadcasting, events/listeners, notifications, task scheduling

Documentation

Weekly Installs
12.0K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass