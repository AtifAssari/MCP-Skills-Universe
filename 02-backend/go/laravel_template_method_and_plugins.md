---
title: laravel:template-method-and-plugins
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:template-method-and-plugins
---

# laravel:template-method-and-plugins

skills/jpcaparas/superpowers-laravel/laravel:template-method-and-plugins
laravel:template-method-and-plugins
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:template-method-and-plugins
SKILL.md
Template Method and Pluggable Strategies

Keep core flows stable; enable extension via small classes.

Template Method

Use a base class that defines the algorithm skeleton; subclasses override hooks.

abstract class Importer {
    final public function handle(string $path): void {
        $rows = $this->load($path);
        $data = $this->normalize($rows);
        $this->validate($data);
        $this->save($data);
    }
    abstract protected function load(string $path): array;
    protected function normalize(array $rows): array { return $rows; }
    protected function validate(array $data): void {}
    abstract protected function save(array $data): void;
}

Strategy/Plugin

Define an interface; register implementations; select by key/config.

interface PaymentGateway { public function charge(int $cents, string $currency): string; }

final class StripeGateway implements PaymentGateway { /* ... */ }
final class BraintreeGateway implements PaymentGateway { /* ... */ }

final class PaymentsRegistry {
    /** @param array<string,PaymentGateway> $drivers */
    public function __construct(private array $drivers) {}
    public function for(string $key): PaymentGateway { return $this->drivers[$key]; }
}


Prefer adding a class over editing switch statements. Test implementations in isolation.

Weekly Installs
52
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026