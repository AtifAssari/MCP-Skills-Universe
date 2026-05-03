---
title: angular-ssr
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-ssr
---

# angular-ssr

skills/oguzhan18/angular-ecosystem-skills/angular-ssr
angular-ssr
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-ssr
SKILL.md
@angular/ssr (Server-Side Rendering)

Version: Angular 21 (2025) Tags: SSR, Hydration, Prerendering, SEO, Angular Universal

References: SSR Guide • Hydration • @angular/ssr

API Changes

This section documents recent version-specific API changes.

NEW: Incremental Hydration — Hydrate components incrementally instead of all at once source

NEW: Hybrid Rendering — Per-route rendering mode configuration source

NEW: provideClientHydration — Modern hydration setup with event replay

NEW: Deferrable views (@defer) — Load components lazily with SSR support

NEW: ngSkipHydration — Opt-out of hydration for specific components

DEPRECATED: Angular Universal — Migrate to @angular/ssr

Best Practices
Enable SSR with CLI
ng add @angular/ssr

# Or create new project with SSR
ng new my-app --ssr

Enable client hydration
import { provideClientHydration } from '@angular/platform-browser';

export const appConfig: ApplicationConfig = {
  providers: [
    provideClientHydration()
  ]
};

Use incremental hydration for better performance
import { provideClientHydration, withIncrementalHydration } from '@angular/platform-browser';

export const appConfig: ApplicationConfig = {
  providers: [
    provideClientHydration(withIncrementalHydration())
  ]
};

Use @defer for lazy loading
@Component({
  template: `
    @defer (on viewport) {
      <heavy-component />
    } @placeholder {
      <div>Loading...</div>
    }
  `
})
export class MainComponent {}

Handle browser-specific code with isPlatformBrowser
import { PLATFORM_ID, Inject } from '@angular/core';

constructor(@Inject(PLATFORM_ID) private platformId: Object) {
  if (isPlatformBrowser(this.platformId)) {
    // Browser-only code
  }
}

Use TransferState to prevent duplicate HTTP requests
import { TransferState, makeStateKey } from '@angular/platform-browser';

@Injectable()
export class DataService {
  constructor(private http: HttpClient, private transferState: TransferState) {}

  getData() {
    const DATA_KEY = makeStateKey('DATA');
    
    if (this.transferState.hasKey(DATA_KEY)) {
      return of(this.transferState.get(DATA_KEY, []));
    }
    
    return this.http.get('/api/data').pipe(
      tap(data => this.transferState.set(DATA_KEY, data))
    );
  }
}

Skip hydration for DOM-manipulating components
@Component({
  selector: 'app-third-party',
  host: {
    'ngSkipHydration': 'true'
  }
})
export class ThirdPartyComponent {}

Configure hybrid rendering per route
import { RenderMode, ServerRoute } from '@angular/ssr';

export const serverRoutes: ServerRoute[] = [
  {
    path: 'dashboard',
    renderMode: RenderMode.Client
  },
  {
    path: 'blog/:slug',
    renderMode: RenderMode.Server
  },
  {
    path: 'about',
    renderMode: RenderMode.Prerender
  }
];

Use platform-server for server-side logic
import { isPlatformServer } from '@angular/common';

constructor(@Inject(PLATFORM_ID) platformId: Object) {
  if (isPlatformServer(platformId)) {
    // Server-side only
  }
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