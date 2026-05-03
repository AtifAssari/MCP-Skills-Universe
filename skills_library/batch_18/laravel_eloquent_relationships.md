---
title: laravel:eloquent-relationships
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:eloquent-relationships
---

# laravel:eloquent-relationships

skills/jpcaparas/superpowers-laravel/laravel:eloquent-relationships
laravel:eloquent-relationships
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:eloquent-relationships
SKILL.md
Eloquent Relationships and Loading

Model relationships express your domain; load only what you need.

Commands
# Typical loading
Post::with(['author', 'tags'])->withCount('comments')->paginate(20);

# Constrained eager loading
User::with(['posts' => fn($q) => $q->latest()->where('published', true)])->find($id);

# Pivot ops (many-to-many)
$post->tags()->sync([1,2,3]);       // atomic replace
$post->tags()->syncWithoutDetaching([4]);

# Chunking large reads
Order::where('status', 'open')->lazy()->each(fn($o) => ...);

Patterns
See laravel:performance-eager-loading for N+1 detection and measurement
Use whereHas() / has() to filter by related existence
Prefer withCount, withSum, withMax for simple aggregates
Apply global / local scopes for recurring constraints
Keep relationship names consistent and pluralized where appropriate
Weekly Installs
74
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026