---
title: laravel:interfaces-and-di
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:interfaces-and-di
---

# laravel:interfaces-and-di

skills/jpcaparas/superpowers-laravel/laravel:interfaces-and-di
laravel:interfaces-and-di
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:interfaces-and-di
SKILL.md
Interfaces and Dependency Injection

Define narrow interfaces and inject them where needed. Bind concrete implementations in a service provider.

interface Slugger { public function slug(string $s): string; }

final class AsciiSlugger implements Slugger {
  public function slug(string $s): string { /* ... */ }
}

$this->app->bind(Slugger::class, AsciiSlugger::class);


Benefits: easier testing (mock interfaces), clearer contracts, swap implementations without touching consumers.

Weekly Installs
50
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026