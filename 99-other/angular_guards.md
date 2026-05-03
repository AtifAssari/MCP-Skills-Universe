---
rating: ⭐⭐
title: angular-guards
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-guards
---

# angular-guards

skills/oguzhan18/angular-ecosystem-skills/angular-guards
angular-guards
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-guards
SKILL.md
Angular Route Guards

Version: Angular 21 (2025) Tags: Guards, Routing, Auth, CanActivate

References: Guards Guide • CanActivate

API Changes

This section documents recent version-specific API changes.

NEW: Functional guards — Use CanActivateFn instead of class-based

NEW: CanMatch guard — Prevent lazy loading of unauthorized code

NEW: provideRouter with guards — Modern guard registration

DEPRECATED: Class-based guards — Migrate to functional

Best Practices
Create functional guard
export const authGuard: CanActivateFn = () => {
  const authService = inject(AuthService);
  const router = inject(Router);
  
  if (authService.isAuthenticated()) {
    return true;
  }
  return router.createUrlTree(['/login']);
};

Use CanActivate for route protection
const routes: Routes = [
  {
    path: 'dashboard',
    canActivate: [authGuard],
    component: DashboardComponent
  }
];

Use CanActivateChild for child routes
export const adminGuard: CanActivateChildFn = () => {
  const auth = inject(AuthService);
  return auth.isAdmin() || inject(Router).createUrlTree(['/unauthorized']);
};

const routes: Routes = [
  {
    path: 'admin',
    canActivateChild: [adminGuard],
    children: [...]
  }
];

Use CanMatch for lazy loading
const routes: Routes = [
  {
    path: 'admin',
    canMatch: [authGuard],
    loadComponent: () => import('./admin/admin.component')
  }
];

Use CanDeactivate for unsaved changes
export const canDeactivateGuard: CanDeactivateFn<CanComponentDeactivate> = (component) => {
  if (component.hasUnsavedChanges?.()) {
    return confirm('You have unsaved changes. Are you sure?');
  }
  return true;
};

Use withComponentInputBinding
export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes, withComponentInputBinding())
  ]
};

Use multiple guards
const routes: Routes = [
  {
    path: 'admin',
    canActivate: [authGuard, adminGuard],
    loadComponent: () => import('./admin/admin.component')
  }
];

Pass data to guards
const routes: Routes = [
  {
    path: 'user/:id',
    canActivate: [userGuard],
    data: { requiredRole: 'admin' }
  }
];

export const userGuard: CanActivateFn = (route, state) => {
  const requiredRole = route.data['requiredRole'];
  // Check role
};

Weekly Installs
122
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
10 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass