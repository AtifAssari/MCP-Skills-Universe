---
rating: ⭐⭐⭐
title: laravel:tdd-with-pest
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:tdd-with-pest
---

# laravel:tdd-with-pest

skills/jpcaparas/superpowers-laravel/laravel:tdd-with-pest
laravel:tdd-with-pest
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:tdd-with-pest
SKILL.md
Laravel TDD (Pest/PHPUnit)

Write the test first. Watch it fail. Write minimal code to pass. Keep tests fast and realistic.

Test Runner
# Sail
sail artisan test --parallel

# Non-Sail
php artisan test --parallel


Prefer Pest (default in new Laravel apps). PHPUnit is fine if your project uses it.

RED – Write a failing test
Use model factories; avoid heavy mocking
Feature tests for HTTP/controllers; unit tests for pure services
Name tests by behavior

Example (feature):

it('rejects empty email on signup', function () {
    $response = $this->post('/register', [
        'name' => 'Alice',
        'email' => '',
        'password' => 'secret',
        'password_confirmation' => 'secret',
    ]);

    $response->assertSessionHasErrors('email');
});


Run and confirm it fails for the right reason.

GREEN – Minimal implementation

Write the simplest code to pass your failing test. No extras. No refactors.

REFACTOR – Clean up

Remove duplication, clarify names, extract small services. Keep tests green.

Guidelines
Every production change starts with a failing test
Watch failures; never skip the failing phase
Use factories/seeders for realistic data
Use DB transactions or refreshes in tests as needed
Keep tests deterministic; avoid sleeps in async flows
When stuck
If a test is hard to write, design is too coupled; extract a service or port
Prefer dependency injection; avoid static/global state
Weekly Installs
74
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026