---
rating: ⭐⭐
title: angular-router
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-router
---

# angular-router

skills/oguzhan18/angular-ecosystem-skills/angular-router
angular-router
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-router
SKILL.md
@angular/router

Version: Angular 21 (2025) Tags: Routing, Navigation, Guards, Lazy Loading, SPA

References: Docs — official routing guide • API • GitHub

API Changes

This section documents recent version-specific API changes.

NEW: Functional guards and resolvers — Prefer functional approach over class-based guards source

NEW: Router inputs — New way to pass data to components via route inputs source

NEW: withComponentInputBinding — Enable component input binding from route params

NEW: Router snapshots improvement — Better type safety for route parameters

NEW: provideRouter() — Modern router configuration with functional providers

DEPRECATED: RouterModule.forRoot() — Use provideRouter() in modern applications

Best Practices
Use lazy loading for feature modules — Reduce initial bundle size by 50-70%
const routes: Routes = [
  {
    path: 'dashboard',
    loadChildren: () => import('./dashboard/dashboard.routes').then(m => m.DASHBOARD_ROUTES)
  }
];

Use functional guards over class-based guards
// ✅ Modern functional guard
const authGuard = () => {
  const authService = inject(AuthService);
  const router = inject(Router);
  
  if (authService.isAuthenticated()) {
    return true;
  }
  return router.createUrlTree(['/login']);
};

// ❌ Avoid class-based guards for new code
// @Injectable() export class AuthGuard implements CanActivate { ... }

Use CanMatch guard for lazy-loaded routes — Prevents unauthorized code downloads
{
  path: 'admin',
  canMatch: [authGuard],
  loadComponent: () => import('./admin/admin.component').then(m => m.AdminComponent)
}

Use resolvers for pre-fetching data — Eliminates loading spinners
{
  path: 'user/:id',
  resolve: { user: userResolver }
}

// In component
@Component({})
export class UserComponent {
  private route = inject(ActivatedRoute);
  
  // Modern way
  user = input.required<User>();
  
  // Legacy way
  ngOnInit() {
    this.route.data.subscribe(data => {
      this.user = data['user'];
    });
  }
}

Use router inputs for better type safety
// app.config.ts
export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes, withComponentInputBinding())
  ]
};

// Component receives route params as inputs
@Component({})
export class UserComponent {
  @Input() id!: string;
}

Use wildcard routes for 404 pages
{
  path: '**',
  component: NotFoundComponent
}

Use PreloadAllModules for background loading
provideRouter(routes, withPreloading(PreloadAllModules))

Use routerLink for navigation — Maintains SPA behavior
// ✅ Correct
<a routerLink="/dashboard">Dashboard</a>

// ❌ Wrong - causes full page reload
<a href="/dashboard">Dashboard</a>

Use kebab-case for URL paths — Consistent naming convention
// ✅ Good
{ path: 'user-profile', ... }

// ❌ Avoid
{ path: 'userProfile', ... }

Weekly Installs
124
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