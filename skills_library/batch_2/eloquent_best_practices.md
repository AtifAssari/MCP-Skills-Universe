---
title: eloquent-best-practices
url: https://skills.sh/iserter/laravel-claude-agents/eloquent-best-practices
---

# eloquent-best-practices

skills/iserter/laravel-claude-agents/eloquent-best-practices
eloquent-best-practices
Installation
$ npx skills add https://github.com/iserter/laravel-claude-agents --skill eloquent-best-practices
Summary

Laravel Eloquent query optimization and relationship management patterns with N+1 prevention.

Eager load relationships with with() and use withCount() for efficient aggregations instead of triggering additional queries in loops
Select only needed columns at query time and define return types on relationship methods for better IDE support and clarity
Use query scopes to encapsulate reusable filtering logic and leverage database-level operations (update(), increment()) instead of loading models into memory
Implement mass assignment protection via $fillable or $guarded, define type casts for safety, and chunk large datasets to manage memory efficiently
Add database indexes on foreign keys and frequently queried columns, and enable lazy loading prevention in development to catch N+1 issues early
SKILL.md
Eloquent Best Practices
Query Optimization
Always Eager Load Relationships
// ❌ N+1 Query Problem
$posts = Post::all();
foreach ($posts as $post) {
    echo $post->user->name; // N additional queries
}

// ✅ Eager Loading
$posts = Post::with('user')->get();
foreach ($posts as $post) {
    echo $post->user->name; // No additional queries
}

Select Only Needed Columns
// ❌ Fetches all columns
$users = User::all();

// ✅ Only needed columns
$users = User::select(['id', 'name', 'email'])->get();

// ✅ With relationships
$posts = Post::with(['user:id,name'])->select(['id', 'title', 'user_id'])->get();

Use Query Scopes
// ✅ Define reusable query logic
class Post extends Model
{
    public function scopePublished($query)
    {
        return $query->where('status', 'published')
                    ->whereNotNull('published_at');
    }
    
    public function scopePopular($query, $threshold = 100)
    {
        return $query->where('views', '>', $threshold);
    }
}

// Usage
$posts = Post::published()->popular()->get();

Relationship Best Practices
Define Return Types
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Post extends Model
{
    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }
    
    public function comments(): HasMany
    {
        return $this->hasMany(Comment::class);
    }
}

Use withCount for Counts
// ❌ Triggers additional queries
foreach ($posts as $post) {
    echo $post->comments()->count();
}

// ✅ Load counts efficiently
$posts = Post::withCount('comments')->get();
foreach ($posts as $post) {
    echo $post->comments_count;
}

Mass Assignment Protection
class Post extends Model
{
    // ✅ Whitelist fillable attributes
    protected $fillable = ['title', 'content', 'status'];
    
    // Or blacklist guarded attributes
    protected $guarded = ['id', 'user_id'];
    
    // ❌ Never do this
    // protected $guarded = [];
}

Use Casts for Type Safety
class Post extends Model
{
    protected $casts = [
        'published_at' => 'datetime',
        'metadata' => 'array',
        'is_featured' => 'boolean',
        'views' => 'integer',
    ];
}

Chunking for Large Datasets
// ✅ Process in chunks to save memory
Post::chunk(200, function ($posts) {
    foreach ($posts as $post) {
        // Process each post
    }
});

// ✅ Or use lazy collections
Post::lazy()->each(function ($post) {
    // Process one at a time
});

Database-Level Operations
// ❌ Slow - loads into memory first
$posts = Post::where('status', 'draft')->get();
foreach ($posts as $post) {
    $post->update(['status' => 'archived']);
}

// ✅ Fast - single query
Post::where('status', 'draft')->update(['status' => 'archived']);

// ✅ Increment/decrement
Post::where('id', $id)->increment('views');

Use Model Events Wisely
class Post extends Model
{
    protected static function booted()
    {
        static::creating(function ($post) {
            $post->slug = Str::slug($post->title);
        });
        
        static::deleting(function ($post) {
            $post->comments()->delete();
        });
    }
}

Common Pitfalls to Avoid
Don't Query in Loops
// ❌ Bad
foreach ($userIds as $id) {
    $user = User::find($id);
}

// ✅ Good
$users = User::whereIn('id', $userIds)->get();

Don't Forget Indexes
// Migration
Schema::create('posts', function (Blueprint $table) {
    $table->id();
    $table->foreignId('user_id')->constrained()->index();
    $table->string('slug')->unique();
    $table->string('status')->index();
    $table->timestamp('published_at')->nullable()->index();
    
    // Composite index for common queries
    $table->index(['status', 'published_at']);
});

Prevent Lazy Loading in Development
// In AppServiceProvider boot method
Model::preventLazyLoading(!app()->isProduction());

Checklist
 Relationships eagerly loaded where needed
 Only selecting required columns
 Using query scopes for reusability
 Mass assignment protection configured
 Appropriate casts defined
 Indexes on foreign keys and query columns
 Using database-level operations when possible
 Chunking for large datasets
 Model events used appropriately
 Lazy loading prevented in development
Weekly Installs
891
Repository
iserter/laravel…e-agents
GitHub Stars
35
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass