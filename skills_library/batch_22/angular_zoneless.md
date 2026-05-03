---
title: angular-zoneless
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-zoneless
---

# angular-zoneless

skills/oguzhan18/angular-ecosystem-skills/angular-zoneless
angular-zoneless
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-zoneless
SKILL.md
Angular Zoneless

Version: Angular 19+ (2025) Tags: Zoneless, Change Detection, Signals, Reactivity

References: Zoneless Guide • Signals

API Changes

This section documents recent version-specific API changes.

NEW: provideZonelessChangeDetection — Enable zoneless mode source

NEW: afterNextRender — Run code after rendering without zone.js

NEW: Experimental Zoneless — Available since Angular 17, stable in Angular 19+

NEW: signal() + computed() — Works without zone.js

Best Practices
Enable zoneless change detection
export const appConfig: ApplicationConfig = {
  providers: [
    provideZonelessChangeDetection()
  ]
};

Use signals for reactivity
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <p>Count: {{ count() }}</p>
    <p>Double: {{ double() }}</p>
  `
})
export class CounterComponent {
  count = signal(0);
  double = computed(() => this.count() * 2);

  increment() {
    this.count.update(c => c + 1);
  }
}

Use afterNextRender for DOM operations
constructor() {
  afterNextRender(() => {
    // Runs after rendering, outside zone
    this.initChart();
  });
}

Use afterRender for repeated operations
constructor() {
  afterRender(() => {
    // Runs after every render
  });
}

Handle async without zone.js
@Component({
  template: `
    @if (data$ | async; as data) {
      {{ data.name }}
    }
  `
})
export class AsyncComponent {
  data$ = from(fetch('/api/data')).pipe(
    share()
  );
}

Use ChangeDetectorRef manually when needed
constructor(private cdr: ChangeDetectorRef) {}

update() {
  this.value = newValue;
  this.cdr.markForCheck();
}

Remove zone.js from polyfills
// polyfills.ts
// Remove or comment out zone.js import
// import 'zone.js';

Use untracked for non-reactive reads
import { untracked } from '@angular/core';

ngOnInit() {
  // Read without creating dependency
  const value = untracked(() => this.signal());
}

Handle browser events
@HostListener('click')
onClick() {
  // Works without zone.js
  this.count.update(c => c + 1);
}

Test in zoneless mode
TestBed.configureTestingModule({
  providers: [
    provideZonelessChangeDetection()
  ]
});

Weekly Installs
122
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
7 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass