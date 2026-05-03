---
title: laravel:strategy-pattern
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:strategy-pattern
---

# laravel:strategy-pattern

skills/jpcaparas/superpowers-laravel/laravel:strategy-pattern
laravel:strategy-pattern
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:strategy-pattern
SKILL.md
Strategy Pattern

Create a common interface and multiple implementations. Choose a strategy by key or context.

interface TaxCalculator { public function for(int $cents): int; }
final class NzTax implements TaxCalculator { /* ... */ }
final class AuTax implements TaxCalculator { /* ... */ }

final class TaxFactory {
  public function __construct(private array $drivers) {}
  public function forCountry(string $code): TaxCalculator { return $this->drivers[$code]; }
}


Register in a service provider and inject the factory where needed.

Weekly Installs
50
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026