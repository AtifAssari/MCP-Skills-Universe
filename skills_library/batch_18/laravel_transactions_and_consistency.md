---
title: laravel:transactions-and-consistency
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:transactions-and-consistency
---

# laravel:transactions-and-consistency

skills/jpcaparas/superpowers-laravel/laravel:transactions-and-consistency
laravel:transactions-and-consistency
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:transactions-and-consistency
SKILL.md
Transactions and Consistency

Ensure multi-step changes are atomic; make retries safe.

Commands
DB::transaction(function () use ($order, $payload) {
    $order->update([...]);
    $order->items()->createMany($payload['items']);
    OrderUpdated::dispatch($order);        // or flag for after-commit
});

// Listener queued after commit
class SendInvoice implements ShouldQueue {
    public $afterCommit = true;
}

Patterns
Use DB::transaction to wrap write sequences and related side-effects
Prefer $afterCommit or dispatchAfterCommit() for events / jobs
Make jobs idempotent (check existing state, use unique constraints)
Use lockForUpdate() for row-level coordination when needed
Validate invariants at the boundary before starting the transaction
Weekly Installs
67
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026