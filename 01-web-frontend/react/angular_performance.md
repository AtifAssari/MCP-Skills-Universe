---
rating: ⭐⭐
title: angular-performance
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-performance
---

# angular-performance

skills/oguzhan18/angular-ecosystem-skills/angular-performance
angular-performance
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-performance
SKILL.md
Angular Performance

Version: Angular 21 (2025) Tags: Performance, Optimization, Bundle Size, Change Detection

References: Performance Guide • Change Detection

API Changes

This section documents recent version-specific API changes.

NEW: Zoneless change detection — Disable zone.js for better performance source

NEW: Deferrable views (@defer) — Lazy load component code

NEW: Signal-based reactivity — Use signals instead of zone.js

NEW: afterNextRender — Run code after rendering without zone.js

Best Practices
Use OnPush change detection strategy
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  // ...
})
export class MyComponent {}

Use trackBy with @for
@Component({
  template: `
    @for (item of items; track item.id) {
      {{ item.name }}
    }
  `
})
export class MyComponent {}

Use lazy loading for routes
const routes: Routes = [
  {
    path: 'dashboard',
    loadComponent: () => import('./dashboard/dashboard.component').then(m => m.DashboardComponent)
  }
];

Use @defer for lazy loading
@Component({
  template: `
    @defer (on viewport) {
      <heavy-chart-component />
    } @placeholder {
      <div>Loading...</div>
    }
  `
})
export class MyComponent {}

Use trackBy in @for loops
@for (item of items; track item.id) {
  <li>{{ item.name }}</li>
}

Use pure pipes
@Pipe({
  name: 'myPipe',
  pure: true // Default - only runs when input changes
})
export class MyPipe implements PipeTransform {}

Avoid function calls in templates
// ❌ Bad
{{ calculateTotal() }}

// ✅ Good
{{ total }}

Use ngSrc for images
<img [ngSrc]="imageUrl" width="100" height="100" priority>

Use ChangeDetectionRef manually when needed
constructor(private cdr: ChangeDetectorRef) {}

updateData() {
  this.data = newData;
  this.cdr.detectChanges();
}

Use runOutsideAngular for third-party libs
import { runOutsideAngular } from '@angular/core/zone';

onClick() {
  runOutsideAngular(() => {
    this第三方Lib.doSomething();
  });
}

Use provideZonelessChangeDetection
export const appConfig: ApplicationConfig = {
  providers: [
    provideZonelessChangeDetection()
  ]
};

Use afterNextRender for initialization
constructor() {
  afterNextRender(() => {
    // Runs after rendering, outside zone
  });
}

Optimize bundle size
# Analyze bundle
ng build --stats-json
npx webpack-bundle-analyzer dist/stats.json

Use standalone components
@Component({
  standalone: true,
  imports: [CommonModule],
  // ...
})
export class MyComponent {}

Weekly Installs
123
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass