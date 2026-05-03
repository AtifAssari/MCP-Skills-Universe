---
title: laravel:exception-handling-and-logging
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:exception-handling-and-logging
---

# laravel:exception-handling-and-logging

skills/jpcaparas/superpowers-laravel/laravel:exception-handling-and-logging
laravel:exception-handling-and-logging
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:exception-handling-and-logging
SKILL.md
Exception Handling and Logging

Treat errors as first-class signals; provide context and paths to remediation.

Commands
// app/Exceptions/Handler.php
public function register(): void
{
    $this->reportable(function (DomainException $e) {
        Log::warning('domain exception', ['code' => $e->getCode()]);
    });

    $this->renderable(function (ModelNotFoundException $e, $request) {
        if ($request->expectsJson()) {
            return response()->json(['message' => 'Not Found'], 404);
        }
    });
}

Patterns
Use domain-specific exceptions for expected error paths
Add structured context to logs; avoid logging secrets
Route noisy logs to separate channels; keep defaults actionable
Convert to API-appropriate responses in renderable()
Weekly Installs
59
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026