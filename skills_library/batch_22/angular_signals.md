---
title: angular-signals
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-signals
---

# angular-signals

skills/oguzhan18/angular-ecosystem-skills/angular-signals
angular-signals
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-signals
SKILL.md
Angular Signals

Version: Angular 16+ (2025) Tags: Reactivity, State Management, Signals API

References: Angular Signals • API Reference

API Changes

This section documents version-specific API changes.

NEW: Angular 19 Resource API — New way to handle async data with built-in loading/error states

NEW: linkedSignal() — Creates a signal linked to external sources with getter/setter source

NEW: Signal inputs — Use input() and input.required() for reactive component inputs

NEW: toSignal() and toObservable() — Bridge between RxJS and Signals

NEW: effect() improvements — Better cleanup with onCleanup callback

NEW: Zoneless change detection — Works seamlessly with Signals

Best Practices
Use computed() for derived state — Never use effect() for deriving values
// ✅ DO THIS - derived state
totalPrice = computed(() => {
  return this.items().reduce((sum, item) => sum + item.price, 0);
});

// ❌ DON'T - side effects in computed
badComputed = computed(() => {
  const data = this.data();
  this.logService.log(data); // Side effect - don't do this!
});

Use signal() for writable state
count = signal(0);

// Update with set()
count.set(5);

// Update with update()
count.update(value => value + 1);

// Update with mutate() for objects
user.update(u => ({ ...u, name: 'New Name' }));

Use effect() only for side effects
effect(() => {
  analytics.track('cart-updated', {
    itemCount: this.items().length
  });
});

Always cleanup effects to prevent memory leaks
effect((onCleanup) => {
  const timer = setTimeout(() => { /* ... */ }, 300);
  onCleanup(() => clearTimeout(timer));
});

Use Signal Inputs instead of traditional @Input()
// Modern signal inputs (Angular 17+)
userId = input<string>('');
user = input.required<User>();

// Computed based on input
greeting = computed(() => `Hello, ${this.user()?.name}`);

Use toSignal() for RxJS to Signal conversion
// Convert Observable to Signal
users = toSignal(this.http.get('/api/users'), { initialValue: [] });


Don't nest effects — Can cause performance issues

Use equality functions for complex object comparisons

user = signal<User | null>(null, {
  equal: (a, b) => a?.id === b?.id
});

Use Signals for UI state, RxJS for complex async — Signals and RxJS serve different purposes
Weekly Installs
121
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
6 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass