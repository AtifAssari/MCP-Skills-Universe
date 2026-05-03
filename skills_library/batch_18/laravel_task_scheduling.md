---
title: laravel:task-scheduling
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:task-scheduling
---

# laravel:task-scheduling

skills/jpcaparas/superpowers-laravel/laravel:task-scheduling
laravel:task-scheduling
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:task-scheduling
SKILL.md
Task Scheduling

Run scheduled tasks predictably across environments.

Commands
// app/Console/Kernel.php
protected function schedule(Schedule $schedule): void
{
    $schedule->command('reports:daily')
        ->dailyAt('01:00')
        ->withoutOverlapping()
        ->onOneServer()
        ->runInBackground()
        ->evenInMaintenanceMode();
}

# Run the scheduler from cron
* * * * * cd /var/www/app && php artisan schedule:run >> /dev/null 2>&1

Patterns
Guard long-running commands with withoutOverlapping()
Use onOneServer() when running on multiple nodes
Emit logs/metrics for visibility; consider notifications on failure
Feature-flag risky jobs via config/env
Weekly Installs
58
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026