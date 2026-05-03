---
title: angular-di
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-di
---

# angular-di

skills/oguzhan18/angular-ecosystem-skills/angular-di
angular-di
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-di
SKILL.md
Angular Dependency Injection

Version: Angular 21 (2025) Tags: DI, Services, Providers, Tokens, inject()

References: DI Guide • API • inject()

API Changes

This section documents recent version-specific API changes.

NEW: Functional injection with inject() — Preferred over constructor injection in modern Angular source

NEW: inject() with Optional decorator — inject(Service, { optional: true })

NEW: inject() with SkipSelf — inject(Service, { skipSelf: true })

NEW: Tree-shakable InjectionToken — new InjectionToken<T>(desc, { providedIn: 'root' })

Best Practices
Use providedIn: 'root' for singleton services
@Injectable({ providedIn: 'root' })
export class LoggerService {
  log(message: string) { console.log(message); }
}

Use inject() function for cleaner code
@Component({})
export class MyComponent {
  private service = inject(MyService);
  private router = inject(Router);
}

Use InjectionToken for non-class dependencies
export const API_URL = new InjectionToken<string>('apiUrl');

providers: [
  { provide: API_URL, useValue: 'https://api.example.com' }
]

constructor(@Inject(API_URL) private apiUrl: string) {}

Use factory providers for complex instantiation
providers: [
  {
    provide: AuthService,
    useFactory: (http: HttpClient, config: AppConfig) => {
      return new AuthService(http, config.apiUrl);
    },
    deps: [HttpClient, APP_CONFIG]
  }
]

Use multi providers for multiple implementations
providers: [
  { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true },
  { provide: HTTP_INTERCEPTORS, useClass: LogInterceptor, multi: true }
]

Use @Optional for optional dependencies
constructor(@Optional() private logger: LoggerService) {
  this.logger?.log('Optional dependency');
}

Use @SkipSelf to avoid self-injection
constructor(@SkipSelf() @Optional() private parent: ParentService) {}

Use forwardRef for circular dependencies
constructor(@Inject(forwardRef(() => ParentService)) private parent: ParentService) {}

Use hierarchical injectors for scoping
// Component-level provider
@Component({
  providers: [MyService]
})
export class MyComponent {}

// Lazy-loaded module provider
@Injectable({ providedIn: MyModule })
export class MyService {}

Use interface injection pattern
export interface CacheInterface {
  get(key: string): any;
}

export const CACHE_TOKEN = new InjectionToken<CacheInterface>('cache');

Use providedIn: 'any' for lazy-loaded services
@Injectable({ providedIn: 'any' })
export class LazyService {}

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