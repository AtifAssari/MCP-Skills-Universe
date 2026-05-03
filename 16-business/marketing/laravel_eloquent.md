---
title: laravel-eloquent
url: https://skills.sh/fusengine/agents/laravel-eloquent
---

# laravel-eloquent

skills/fusengine/agents/laravel-eloquent
laravel-eloquent
Installation
$ npx skills add https://github.com/fusengine/agents --skill laravel-eloquent
SKILL.md
Laravel Eloquent ORM
Agent Workflow (MANDATORY)

Before ANY implementation, use TeamCreate to spawn 3 agents:

fuse-ai-pilot:explore-codebase - Check existing models, relationships
fuse-ai-pilot:research-expert - Verify latest Eloquent docs via Context7
mcp__context7__query-docs - Query specific patterns (casts, scopes)

After implementation, run fuse-ai-pilot:sniper for validation.

Overview

Eloquent is Laravel's ActiveRecord ORM implementation. Models represent database tables and provide a fluent interface for queries.

Feature	Purpose
Models	Table representation with attributes
Relationships	Define connections between models
Query Scopes	Reusable query constraints
Casts	Attribute type conversion
Events/Observers	React to model lifecycle
Factories	Generate test data
Critical Rules
Always eager load relationships - Prevent N+1 queries
Use scopes for reusable queries - Don't repeat WHERE clauses
Cast attributes properly - Type safety for dates, arrays, enums
No business logic in models - Keep models slim
Use factories for testing - Never hardcode test data
Decision Guide
Relationship Type
What's the cardinality?
├── One-to-One → hasOne / belongsTo
├── One-to-Many → hasMany / belongsTo
├── Many-to-Many → belongsToMany (pivot table)
├── Through another → hasOneThrough / hasManyThrough
└── Polymorphic?
    ├── One-to-One → morphOne / morphTo
    ├── One-to-Many → morphMany / morphTo
    └── Many-to-Many → morphToMany / morphedByMany

Performance Issue
What's the problem?
├── Too many queries → Eager loading (with)
├── Memory exhaustion → chunk() or cursor()
├── Slow queries → Add indexes, select columns
├── Repeated queries → Cache results
└── Large inserts → Batch operations

Reference Guide
Concepts (WHY & Architecture)
Topic	Reference	When to Consult
Models	models.md	Model config, fillable, conventions
Basic Relations	relationships-basic.md	HasOne, HasMany, BelongsTo
Many-to-Many	relationships-many-to-many.md	Pivot tables, attach/sync
Advanced Relations	relationships-advanced.md	Through, dynamic relations
Polymorphic	relationships-polymorphic.md	MorphTo, MorphMany
Eager Loading	eager-loading.md	N+1 prevention, with()
Scopes	scopes.md	Local, global, dynamic
Casts	casts.md	Type casting, custom casts
Accessors/Mutators	accessors-mutators.md	Attribute transformation
Events/Observers	events-observers.md	Lifecycle hooks
Soft Deletes	soft-deletes.md	Recoverable deletion
Collections	collections.md	Eloquent collection methods
Serialization	serialization.md	toArray, toJson, hidden
Factories	factories.md	Test data generation
Performance	performance.md	Optimization techniques
API Resources	resources.md	JSON transformation
Transactions	transactions.md	Atomic operations, rollback
Pagination	pagination.md	paginate, cursor, simplePaginate
Aggregates	aggregates.md	count, sum, withCount, exists
Batch Operations	batch-operations.md	insert, upsert, mass update
Query Debugging	query-debugging.md	toSql, dd, DB::listen
Templates (Complete Code)
Template	When to Use
ModelBasic.php.md	Standard model with scopes
ModelRelationships.php.md	All relationship types
ModelCasts.php.md	Casts and accessors
Observer.php.md	Complete observer
Factory.php.md	Factory with states
Resource.php.md	API resource
EagerLoadingExamples.php.md	N+1 prevention
Quick Reference
Basic Model
class Post extends Model
{
    protected $fillable = ['title', 'content', 'author_id'];

    protected function casts(): array
    {
        return [
            'published_at' => 'datetime',
            'metadata' => 'array',
        ];
    }

    public function author(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }
}

Eager Loading
// ✅ Good - 2 queries
$posts = Post::with('author')->get();

// ❌ Bad - N+1 queries
$posts = Post::all();
foreach ($posts as $post) {
    echo $post->author->name;
}

Query Scopes
#[Scope]
protected function published(Builder $query): void
{
    $query->whereNotNull('published_at');
}

// Usage: Post::published()->get();

Best Practices
DO
Use $fillable for mass assignment protection
Eager load relationships with with()
Use scopes for reusable query logic
Cast dates, arrays, and enums
Use factories in tests
DON'T
Put business logic in models
Lazy load in loops (N+1)
Use $guarded = [] in production
Query in accessors/mutators
Forget foreign keys in with() columns
Weekly Installs
34
Repository
fusengine/agents
GitHub Stars
11
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass