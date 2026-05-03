---
title: laravel:bootstrap-check
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:bootstrap-check
---

# laravel:bootstrap-check

skills/jpcaparas/superpowers-laravel/laravel:bootstrap-check
laravel:bootstrap-check
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:bootstrap-check
SKILL.md
Bootstrap Check (Laravel)

Quickly determine if the project should run with Sail or host tools, then list the correct commands for this session.

Detect Runner

Run this snippet in your project root:

if [ -f sail ] || [ -x vendor/bin/sail ]; then
  echo "Sail detected. Use: sail artisan|composer|pnpm ...";
else
  echo "Sail not found. Use host tools: php artisan, composer, pnpm ...";
fi


Optional portable alias:

alias sail='sh $([ -f sail ] && echo sail || echo vendor/bin/sail)'

Command Pairs
sail artisan about | php artisan about
sail artisan test | php artisan test
sail artisan migrate | php artisan migrate
sail composer install | composer install
sail pnpm install | pnpm install
sail pnpm run dev | pnpm run dev
Service Smoke Checks
DB: sail mysql -e 'select 1' or mysql -e 'select 1'
Cache: sail redis ping or redis-cli ping
Weekly Installs
48
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026