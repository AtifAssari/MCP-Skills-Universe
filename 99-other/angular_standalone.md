---
rating: ⭐⭐⭐
title: angular-standalone
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-standalone
---

# angular-standalone

skills/oguzhan18/angular-ecosystem-skills/angular-standalone
angular-standalone
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-standalone
SKILL.md
Angular Standalone Components

Version: Angular 21 (2025) Tags: Standalone, Components, Imports, Bootstrap

References: Standalone Guide • Migration

API Changes

This section documents recent version-specific API changes.

NEW: Standalone by default — New components are standalone by default since Angular 17

NEW: provideRouter for standalone — Use functional providers instead of RouterModule

NEW: ng generate @angular/core:standalone — Migration schematic

DEPRECATED: NgModule — Migration to standalone components recommended

Best Practices
Create standalone components
@Component({
  standalone: true,
  imports: [CommonModule, MatButtonModule],
  selector: 'app-my',
  template: `<button>Click</button>`
})
export class MyComponent {}

Use imports array for dependencies
@Component({
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    MatCardModule,
    MyChildComponent
  ],
  template: `
    <mat-card>
      <app-my-child></app-my-child>
    </mat-card>
  `
})
export class ParentComponent {}

Bootstrap standalone component
// main.ts
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { appConfig } from './app/app.config';

bootstrapApplication(AppComponent, appConfig)
  .catch(err => console.error(err));

Use functional providers
export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(),
    provideAnimations()
  ]
};

Use provideZoneChangeDetection
export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true })
  ]
};

Migrate from NgModule
# Full migration
ng generate @angular/core:standalone

# Specific component
ng generate @angular/core:standalone --path=path/to/component

Use Router Outlet with standalone
@Component({
  standalone: true,
  imports: [RouterOutlet],
  template: `<router-outlet></router-outlet>`
})
export class AppComponent {}

Lazy load standalone components
const routes: Routes = [
  {
    path: 'admin',
    loadComponent: () => import('./admin/admin.component').then(m => m.AdminComponent)
  }
];

Use forwardRef for circular imports
@Component({
  standalone: true,
  imports: [forwardRef(() => OtherComponent)]
})
export class MyComponent {}

Export standalone components
@Component({
  standalone: true,
  exports: [MyComponent],
  imports: [MyComponent]
})
export class FeatureComponent {}

Weekly Installs
125
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass