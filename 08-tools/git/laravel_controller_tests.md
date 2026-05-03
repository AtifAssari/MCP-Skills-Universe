---
rating: ⭐⭐
title: laravel:controller-tests
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:controller-tests
---

# laravel:controller-tests

skills/jpcaparas/superpowers-laravel/laravel:controller-tests
laravel:controller-tests
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:controller-tests
SKILL.md
Controller Tests
Feature tests for endpoints
it('rejects empty email', function () {
  $this->post('/register', ['email' => ''])->assertSessionHasErrors('email');
});

Better tests
Move validation to Form Requests; assert errors from the request class
Extract business logic into Actions; unit test them directly
Use factories for realistic data; avoid heavy mocking
Weekly Installs
53
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026