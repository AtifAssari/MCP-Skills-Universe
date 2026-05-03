---
rating: ⭐⭐
title: rxjs
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/rxjs
---

# rxjs

skills/oguzhan18/angular-ecosystem-skills/rxjs
rxjs
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill rxjs
SKILL.md
RxJS (Reactive Extensions for JavaScript)

Version: 8.x (2025) Tags: Reactive Programming, Observables, Async

References: Docs — operators, API • Angular RxJS • GitHub

API Changes

This section documents recent version-specific API changes.

NEW: RxJS 8 — Modern TypeScript types, smaller bundles, better tree-shaking source

NEW: Improved interop helpers — Simpler conversion to/from Signals with toSignal and toObservable

NEW: RxJS 8 ergonomics — Compact operator signatures and safer defaults

DEPRECATED: Legacy import style — Use RxJS 7+ pipeable operators instead of patch imports

Best Practices
Use AsyncPipe in templates — Handles subscription/unsubscription automatically, prevents memory leaks
@Component({
  template: `
    <div *ngIf="data$ | async as data">
      {{ data.name }}
    </div>
  `
})
export class MyComponent {
  data$ = this.service.getData();
}

Use proper flattening operators — Choose based on use case:
// switchMap - cancel previous, keep latest (search)
search(term: string): Observable<SearchResult[]> {
  return this.searchService.search(term).pipe(
    debounceTime(300),
    distinctUntilChanged(),
    switchMap(term => term ? this.http.get(...) : of([]))
  );
}

// mergeMap - run concurrently (multiple API calls)
this.items$.pipe(
  mergeMap(item => this.save(item))
);

// concatMap - run sequentially (order matters)
this.orders$.pipe(
  concatMap(order => this.processOrder(order))
);

// exhaustMap - ignore while running (form submit)
this.submit$.pipe(
  exhaustMap(() => this.submitForm())
);

Always unsubscribe — Prevent memory leaks
// Use takeUntil pattern
private destroy$ = new Subject<void>();

ngOnInit() {
  this.data$.pipe(takeUntil(this.destroy$)).subscribe();
}

ngOnDestroy() {
  this.destroy$.next();
  this.destroy$.complete();
}

// Or use takeUntilDestroyed (Angular 16+)
private destroy$ = takeUntilDestroyed();

Use catchError for error handling
this.http.get('/api/data').pipe(
  catchError(error => {
    console.error(error);
    return of([]); // Return fallback value
  })
);

Use shareReplay(1) for caching shared observables
this.data$ = this.http.get('/api/data').pipe(
  shareReplay(1)
);


Name observables with $ suffix — Improves readability

Use Signals for UI state, RxJS for events — Modern Angular pattern

// Convert Observable to Signal
users = toSignal(this.users$, { initialValue: [] });

// Convert Signal to Observable (if needed)
name$ = toObservable(this.name);

Weekly Installs
133
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass