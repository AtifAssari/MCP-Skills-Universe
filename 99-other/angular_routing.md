---
rating: ⭐⭐
title: angular-routing
url: https://skills.sh/analogjs/angular-skills/angular-routing
---

# angular-routing

skills/analogjs/angular-skills/angular-routing
angular-routing
Installation
$ npx skills add https://github.com/analogjs/angular-skills --skill angular-routing
Summary

Angular v20+ routing with lazy loading, functional guards, resolvers, and signal-based route parameters.

Supports lazy loading of feature modules and individual components with loadChildren and loadComponent
Functional guards for authentication, role-based access control, and unsaved changes detection; resolvers pre-fetch data before route activation
Route parameters and query strings bind directly to component inputs via withComponentInputBinding(), with signal-based access to ActivatedRoute data
Nested routing with child outlets, programmatic navigation with Router.navigate(), and router event monitoring for navigation state tracking
SKILL.md
Angular Routing

Configure routing in Angular v20+ with lazy loading, functional guards, and signal-based route parameters.

Basic Setup
// app.routes.ts
import { Routes } from '@angular/router';

export const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: Home },
  { path: 'about', component: About },
  { path: '**', component: NotFound },
];

// app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
  ],
};

// app.component.ts
import { Component } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <nav>
      <a routerLink="/home" routerLinkActive="active">Home</a>
      <a routerLink="/about" routerLinkActive="active">About</a>
    </nav>
    <router-outlet />
  `,
})
export class App {}

Lazy Loading

Load feature modules on demand:

// app.routes.ts
export const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: Home },
  
  // Lazy load entire feature
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.routes').then(m => m.adminRoutes),
  },
  
  // Lazy load single component
  {
    path: 'settings',
    loadComponent: () => import('./settings/settings.component').then(m => m.Settings),
  },
];

// admin/admin.routes.ts
export const adminRoutes: Routes = [
  { path: '', component: AdminDashboard },
  { path: 'users', component: AdminUsers },
  { path: 'settings', component: AdminSettings },
];

Route Parameters
With Signal Inputs (Recommended)
// Route config
{ path: 'users/:id', component: UserDetail }

// Component - use input() for route params
import { Component, input, computed } from '@angular/core';

@Component({
  selector: 'app-user-detail',
  template: `
    <h1>User {{ id() }}</h1>
  `,
})
export class UserDetail {
  // Route param as signal input
  id = input.required<string>();
  
  // Computed based on route param
  userId = computed(() => parseInt(this.id(), 10));
}


Enable with withComponentInputBinding():

// app.config.ts
import { provideRouter, withComponentInputBinding } from '@angular/router';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes, withComponentInputBinding()),
  ],
};

Query Parameters
// Route: /search?q=angular&page=1

@Component({...})
export class Search {
  // Query params as inputs
  q = input<string>('');
  page = input<string>('1');
  
  currentPage = computed(() => parseInt(this.page(), 10));
}

With ActivatedRoute (Alternative)
import { Component, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { toSignal } from '@angular/core/rxjs-interop';
import { map } from 'rxjs';

@Component({...})
export class UserDetail {
  private route = inject(ActivatedRoute);
  
  // Convert route params to signal
  id = toSignal(
    this.route.paramMap.pipe(map(params => params.get('id'))),
    { initialValue: null }
  );
  
  // Query params
  query = toSignal(
    this.route.queryParamMap.pipe(map(params => params.get('q'))),
    { initialValue: '' }
  );
}

Functional Guards
Auth Guard
// guards/auth.guard.ts
import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';

export const authGuard: CanActivateFn = (route, state) => {
  const authService = inject(Auth);
  const router = inject(Router);
  
  if (authService.isAuthenticated()) {
    return true;
  }
  
  // Redirect to login with return URL
  return router.createUrlTree(['/login'], {
    queryParams: { returnUrl: state.url },
  });
};

// Usage in routes
{
  path: 'dashboard',
  component: Dashboard,
  canActivate: [authGuard],
}

Role Guard
export const roleGuard = (allowedRoles: string[]): CanActivateFn => {
  return (route, state) => {
    const authService = inject(Auth);
    const router = inject(Router);
    
    const userRole = authService.currentUser()?.role;
    
    if (userRole && allowedRoles.includes(userRole)) {
      return true;
    }
    
    return router.createUrlTree(['/unauthorized']);
  };
};

// Usage
{
  path: 'admin',
  component: Admin,
  canActivate: [authGuard, roleGuard(['admin', 'superadmin'])],
}

Can Deactivate Guard
export interface CanDeactivate {
  canDeactivate: () => boolean | Promise<boolean>;
}

export const unsavedChangesGuard: CanDeactivateFn<CanDeactivate> = (component) => {
  if (component.canDeactivate()) {
    return true;
  }
  
  return confirm('You have unsaved changes. Leave anyway?');
};

// Component implementation
@Component({...})
export class Edit implements CanDeactivate {
  form = inject(FormBuilder).group({...});
  
  canDeactivate(): boolean {
    return !this.form.dirty;
  }
}

// Route
{
  path: 'edit/:id',
  component: Edit,
  canDeactivate: [unsavedChangesGuard],
}

Resolvers

Pre-fetch data before route activation:

// resolvers/user.resolver.ts
import { inject } from '@angular/core';
import { ResolveFn } from '@angular/router';

export const userResolver: ResolveFn<User> = (route) => {
  const userService = inject(User);
  const id = route.paramMap.get('id')!;
  return userService.getById(id);
};

// Route config
{
  path: 'users/:id',
  component: UserDetail,
  resolve: { user: userResolver },
}

// Component - access resolved data via input
@Component({...})
export class UserDetail {
  user = input.required<User>();
}

Nested Routes
// Parent route with children
export const routes: Routes = [
  {
    path: 'products',
    component: ProductsLayout,
    children: [
      { path: '', component: ProductList },
      { path: ':id', component: ProductDetail },
      { path: ':id/edit', component: ProductEdit },
    ],
  },
];

// ProductsLayout
@Component({
  imports: [RouterOutlet],
  template: `
    <h1>Products</h1>
    <router-outlet /> <!-- Child routes render here -->
  `,
})
export class ProductsLayout {}

Programmatic Navigation
import { Component, inject } from '@angular/core';
import { Router } from '@angular/router';

@Component({...})
export class Product {
  private router = inject(Router);
  
  // Navigate to route
  goToProducts() {
    this.router.navigate(['/products']);
  }
  
  // Navigate with params
  goToProduct(id: string) {
    this.router.navigate(['/products', id]);
  }
  
  // Navigate with query params
  search(query: string) {
    this.router.navigate(['/search'], {
      queryParams: { q: query, page: 1 },
    });
  }
  
  // Navigate relative to current route
  goToEdit() {
    this.router.navigate(['edit'], { relativeTo: this.route });
  }
  
  // Replace current history entry
  replaceUrl() {
    this.router.navigate(['/new-page'], { replaceUrl: true });
  }
}

Route Data
// Static route data
{
  path: 'admin',
  component: Admin,
  data: {
    title: 'Admin Dashboard',
    roles: ['admin'],
  },
}

// Access in component
@Component({...})
export class AdminCmpt {
  title = input<string>(); // From route data
  roles = input<string[]>(); // From route data
}

// Or via ActivatedRoute
private route = inject(ActivatedRoute);
data = toSignal(this.route.data);

Router Events
import { Router, NavigationStart, NavigationEnd } from '@angular/router';
import { filter } from 'rxjs';

@Component({...})
export class AppMain {
  private router = inject(Router);
  
  isNavigating = signal(false);
  
  constructor() {
    this.router.events.pipe(
      filter(e => e instanceof NavigationStart || e instanceof NavigationEnd)
    ).subscribe(event => {
      this.isNavigating.set(event instanceof NavigationStart);
    });
  }
}


For advanced patterns, see references/routing-patterns.md.

Weekly Installs
4.6K
Repository
analogjs/angular-skills
GitHub Stars
588
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass