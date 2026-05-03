---
title: laravel:performance-eager-loading
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:performance-eager-loading
---

# laravel:performance-eager-loading

skills/jpcaparas/superpowers-laravel/laravel:performance-eager-loading
laravel:performance-eager-loading
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:performance-eager-loading
SKILL.md
Eager Loading and N+1 Prevention
Load Relations Explicitly
Post::with(['author', 'comments'])->paginate();

Use load()/loadMissing() after fetching models when needed
Select only required columns for both base query and relations
Guard Against Lazy Loading in Dev/Test

Add to a service provider (non-production):

Model::preventLazyLoading(! app()->isProduction());

Verify
Use a query logger or debugbar to confirm relation queries are minimized
Add tests that assert counts or avoid unexpected query spikes
Weekly Installs
73
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026