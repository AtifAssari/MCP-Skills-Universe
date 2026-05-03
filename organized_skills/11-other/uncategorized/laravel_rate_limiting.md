---
rating: ⭐⭐
title: laravel:rate-limiting
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:rate-limiting
---

# laravel:rate-limiting

skills/jpcaparas/superpowers-laravel/laravel:rate-limiting
laravel:rate-limiting
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:rate-limiting
SKILL.md
Rate Limiting and Throttle

Protect endpoints from abuse while keeping UX predictable.

Commands
// App\Providers\RouteServiceProvider
RateLimiter::for('api', function (Request $request) {
    return Limit::perMinute(60)->by(optional($request->user())->id ?: $request->ip());
});

// routes/api.php
Route::middleware(['throttle:api'])->group(function () {
    // ...
});

Patterns
Scope limits by user when authenticated; fall back to IP
Communicate limits to clients via standard headers
Provide sensible 429 responses with retry hints
Separate bursty endpoints into specialized limiters
Weekly Installs
61
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026