---
rating: ⭐⭐
title: angular-pipes
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-pipes
---

# angular-pipes

skills/oguzhan18/angular-ecosystem-skills/angular-pipes
angular-pipes
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-pipes
SKILL.md
Angular Pipes

Version: Angular 21 (2025) Tags: Pipes, Transform, Format, Async

References: Pipes Guide • API

API Changes

This section documents recent version-specific API changes.

NEW: Standalone pipes — All pipes can be standalone

NEW: Signal-based pipes — Pipes can use signals

NEW: inject() in pipes — Use functional DI in pipes

DEPRECATED: Impure pipes — Avoid for performance; use pure pipes

Best Practices
Use pure pipes for stateless transformations
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'capitalize',
  standalone: true
})
export class CapitalizePipe implements PipeTransform {
  transform(value: string): string {
    if (!value) return '';
    return value.charAt(0).toUpperCase() + value.slice(1);
  }
}

Use pipes in templates
@Component({
  template: `
    <p>{{ name | capitalize }}</p>
    <p>{{ price | currency:'USD' }}</p>
    <p>{{ items | json }}</p>
  `
})
export class MyComponent {}

Use pipe with parameters
@Pipe({ name: 'slice' })
export class SlicePipe implements PipeTransform {
  transform(value: string, start: number, end?: number): string {
    return value.slice(start, end);
  }
}

// Usage: {{ text | slice:0:10 }}

Use async pipe for observables
@Component({
  template: `
    @if (user$ | async; as user) {
      <p>{{ user.name }}</p>
    }
  `
})
export class UserComponent {
  user$ = this.userService.getUser();
}

Use impure pipes only when necessary
@Pipe({
  name: 'myPipe',
  pure: false // Impure - runs on every change detection
})
export class ImpurePipe implements PipeTransform {}

Use KeyValue pipe for object iteration
@Component({
  template: `
    @for (item of object | keyvalue; track item.key) {
      {{ item.key }}: {{ item.value }}
    }
  `
})
export class MyComponent {
  object = { a: 1, b: 2 };
}

Use Json pipe for debugging
@Component({
  template: `
    <pre>{{ object | json }}</pre>
  `
})
export class DebugComponent {}

Chain pipes
@Component({
  template: `
    {{ name | uppercase | slice:0:5 }}
  `
})
export class ChainedPipeComponent {}

Use standalone pipes in imports
@Component({
  standalone: true,
  imports: [DatePipe, CurrencyPipe, CapitalizePipe],
  template: `{{ date | date }}`
})
export class MyComponent {}

Use inject() in pipes
@Pipe({ name: 'translate', standalone: true })
export class TranslatePipe implements PipeTransform {
  private service = inject(TranslateService);

  transform(key: string): string {
    return this.service.get(key);
  }
}

Weekly Installs
123
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