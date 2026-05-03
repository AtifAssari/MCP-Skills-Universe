---
title: laravel:policies-and-authorization
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:policies-and-authorization
---

# laravel:policies-and-authorization

skills/jpcaparas/superpowers-laravel/laravel:policies-and-authorization
laravel:policies-and-authorization
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:policies-and-authorization
SKILL.md
Policies and Authorization

Use Policies for per-model actions; use Gates for cross-cutting checks.

Commands
# Generate a policy
sail artisan make:policy PostPolicy --model=Post   # or: php artisan make:policy PostPolicy --model=Post

# Apply in routes (resource controllers)
Route::resource('posts', PostController::class);
// In controller constructor
$this->authorizeResource(Post::class, 'post');

# One-off checks
$this->authorize('update', $post);           // in controller
Gate::allows('manage-billing', $user);       // ad-hoc gate

Patterns
Use resource policy methods: viewAny, view, create, update, delete, restore, forceDelete
Prefer policy methods over inline checks; keeps controllers clean
Register policies in AuthServiceProvider
Use can middleware for quick route protection: ->middleware('can:update,post')
In tests, assert actingAs($user)->get(...)->assertForbidden() for denied cases
Weekly Installs
68
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026