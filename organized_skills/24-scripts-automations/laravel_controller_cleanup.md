---
rating: ⭐⭐
title: laravel:controller-cleanup
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:controller-cleanup
---

# laravel:controller-cleanup

skills/jpcaparas/superpowers-laravel/laravel:controller-cleanup
laravel:controller-cleanup
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:controller-cleanup
SKILL.md
Controller Cleanup

Keep controllers small and focused on orchestration.

Move auth/validation to Form Requests
Create a Request class (e.g., StoreUserRequest) and use authorize() + rules()
Type-hint the Request in your controller method; Laravel runs it before the action
php artisan make:request StoreUserRequest

Extract business logic to Actions/Services
Create a small Action (one thing well) or a Service for larger workflows
Pass a DTO from the Request to the Action to avoid leaking framework concerns
final class CreateUserAction {
    public function __invoke(CreateUserDTO $dto): User { /* ... */ }
}

Prefer Resource or Single-Action Controllers
Use resource controllers for standard CRUD
For one-off endpoints, use invokable (single-action) controllers
Testing
Write feature tests for the controller route
Unit test Actions/Services independently with DTOs
Weekly Installs
60
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026