---
title: laravel:custom-helpers
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:custom-helpers
---

# laravel:custom-helpers

skills/jpcaparas/superpowers-laravel/laravel:custom-helpers
laravel:custom-helpers
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:custom-helpers
SKILL.md
Custom Helpers
Create a helper file
// app/Support/helpers.php
function money(int $cents): string { return number_format($cents / 100, 2); }

Autoload

Add to composer.json:

{
  "autoload": { "files": ["app/Support/helpers.php"] }
}


Run composer dump-autoload.

Guidelines
Keep helpers small and pure; avoid hidden IO/state
Prefer static methods on value objects when domain-specific
Weekly Installs
56
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026