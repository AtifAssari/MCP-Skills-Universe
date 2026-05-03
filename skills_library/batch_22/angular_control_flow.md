---
title: angular-control-flow
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-control-flow
---

# angular-control-flow

skills/oguzhan18/angular-ecosystem-skills/angular-control-flow
angular-control-flow
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-control-flow
SKILL.md
Angular Control Flow

Version: Angular 17+ (2025) Tags: Control Flow, @if, @for, @switch, @defer

References: Control Flow • Deferrable Views

API Changes

This section documents recent version-specific API changes.

NEW: @if replaces *ngIf — New control flow syntax

NEW: @for replaces *ngFor — New loop syntax with track

NEW: @switch replaces ngSwitch — New switch syntax

NEW: @defer — Lazy load components

DEPRECATED: *ngIf, *ngFor, *ngSwitch — Migrate to new syntax

Best Practices
Use @if for conditionals
@Component({
  template: `
    @if (isLoggedIn) {
      <p>Welcome!</p>
    } @else {
      <p>Please login</p>
    }
  `
})
export class MyComponent {
  isLoggedIn = signal(false);
}

Use @else if
@Component({
  template: `
    @if (user.role === 'admin') {
      <p>Admin panel</p>
    } @else if (user.role === 'user') {
      <p>User dashboard</p>
    } @else {
      <p>Guest view</p>
    }
  `
})
export class MyComponent {}

Use @for for loops
@Component({
  template: `
    @for (item of items; track item.id) {
      <li>{{ item.name }}</li>
    }
  `
})
export class MyComponent {
  items = [{ id: 1, name: 'A' }, { id: 2, name: 'B' }];
}

Use track for performance
@for (user of users; track user.id) {
  <li>{{ user.name }}</li>
}

Use @empty for empty lists
@Component({
  template: `
    @for (item of items; track item.id) {
      {{ item.name }}
    } @empty {
      <p>No items found</p>
    }
  `
})
export class MyComponent {}

Use @switch for conditionals
@Component({
  template: `
    @switch (status) {
      @case ('loading') {
        <p>Loading...</p>
      }
      @case ('success') {
        <p>Success!</p>
      }
      @case ('error') {
        <p>Error occurred</p>
      }
      @default {
        <p>Unknown status</p>
      }
    }
  `
})
export class MyComponent {
  status = 'loading';
}

Use @defer for lazy loading
@Component({
  template: `
    @defer (on viewport) {
      <heavy-chart />
    } @placeholder {
      <div>Loading chart...</div>
    }
  `
})
export class DashboardComponent {}

Use @defer with conditions
@Component({
  template: `
    @defer (on hover) {
      <tooltip />
    }
    
    @defer (when isReady) {
      <ready-component />
    }
  `
})
export class MyComponent {}

Migrate from *ngIf
ng generate @angular/core:control-flow

Use else with @if
@if (condition) {
  content
} @else {
  alternative
}

Weekly Installs
121
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