---
title: angular-best-practices
url: https://skills.sh/boise-state-development/agentcore-public-stack/angular-best-practices
---

# angular-best-practices

skills/boise-state-development/agentcore-public-stack/angular-best-practices
angular-best-practices
Installation
$ npx skills add https://github.com/boise-state-development/agentcore-public-stack --skill angular-best-practices
Summary

Angular 21 development with signals, standalone components, reactive patterns, and strict TypeScript typing.

Use standalone components with ChangeDetectionStrategy.OnPush, input()/output() functions, and computed() for derived state instead of decorators and ngClass/ngStyle
Manage async data with resource() for signal-based fetching, handling loading/error states via hasValue() and status checks
Build templates with native control flow (@if, @for, @switch), async pipes, and avoid arrow functions or template logic
Inject services with inject() function, implement lazy loading for routes, and use Tailwind 4.1 for styling
Ensure WCAG AA accessibility compliance including focus management, color contrast, and ARIA attributes
SKILL.md
Angular 21 Best Practices
TypeScript
Use strict type checking
Prefer type inference when type is obvious
Avoid any; use unknown when type is uncertain
Components
Always use standalone components (do NOT set standalone: true — it's the default in v20+)
Set changeDetection: ChangeDetectionStrategy.OnPush
Use input() and output() functions instead of decorators
Use computed() for derived state
Keep components small and single-responsibility
Prefer inline templates for small components
Use Reactive forms over Template-driven
Use class bindings instead of ngClass
Use style bindings instead of ngStyle
For external templates/styles, use paths relative to the component TS file
Do NOT use @HostBinding/@HostListener — use the host object in the decorator instead
State Management with Signals
Use signals for local component state
Use computed() for derived state
Keep state transformations pure and predictable
Do NOT use mutate on signals — use update or set instead

For complex derived state patterns, see references/signal-patterns.md.

Resources (Async Data)

Use resource() for async data fetching with signals:

const userResource = resource({
  params: () => ({ id: userId() }),
  loader: ({ params, abortSignal }) => fetch(`/api/users/${params.id}`, { signal: abortSignal }),
});

const userName = computed(() => userResource.hasValue() ? userResource.value().name : undefined);


Key resource patterns:

params returns undefined → loader doesn't run, status becomes 'idle'
Use abortSignal to cancel in-flight requests
Check hasValue() before accessing value() to handle loading/error states
Status values: 'idle', 'loading', 'reloading', 'resolved', 'error', 'local'
Templates
Use native control flow: @if, @for, @switch (NOT *ngIf, *ngFor, *ngSwitch)
Use async pipe for observables
Keep templates simple — no complex logic
Do NOT use arrow functions in templates (not supported)
Do NOT assume globals like new Date() are available
Services
Single responsibility per service
Use providedIn: 'root' for singletons
Use inject() function instead of constructor injection
@Injectable({ providedIn: 'root' })
export class UserService {
  private readonly http = inject(HttpClient);
}

Routing
Implement lazy loading for feature routes:
export const routes: Routes = [
  {
    path: 'admin',
    loadComponent: () => import('./admin/admin.page').then(m => m.AdminPage),
  },
];

File Naming
Routable view components: file-name.page.ts, file-name.page.html, file-name.page.css
Regular components: file-name.component.ts
Services: file-name.service.ts
Icons (ng-icon)
import { NgIcon, provideIcons } from '@ng-icons/core';
import { heroSparkles, heroTrash } from '@ng-icons/heroicons/outline';

@Component({
  selector: 'app-example',
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [NgIcon],
  providers: [provideIcons({ heroSparkles, heroTrash })],
  template: `<ng-icon name="heroSparkles" />`,
})
export class ExampleComponent {}

Images
Use NgOptimizedImage for all static images
NgOptimizedImage does NOT work for inline base64 images
Styling
Use Tailwind 4.1 for CSS (see tailwind skill if available)
Angular CDK is available when needed
Accessibility
MUST pass all AXE checks
MUST meet WCAG AA minimums: focus management, color contrast, ARIA attributes
Weekly Installs
660
Repository
boise-state-dev…ic-stack
GitHub Stars
8
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass