---
title: angular-di
url: https://skills.sh/analogjs/angular-skills/angular-di
---

# angular-di

skills/analogjs/angular-skills/angular-di
angular-di
Installation
$ npx skills add https://github.com/analogjs/angular-skills --skill angular-di
Summary

Dependency injection configuration and service management for Angular v20+ using inject() and providers.

Use inject() for cleaner dependency declaration in components and services; configure providers at root, component, or route level to control singleton vs instance-per-component behavior
Create and inject custom tokens for configuration objects, third-party values, and multi-provider collections; supports useValue, useClass, useFactory, and useExisting provider strategies
Manage injection scope with optional injection, self/skipSelf/host modifiers, and multi-providers for collecting multiple implementations of the same token
Run async initialization code before app startup using provideAppInitializer; create custom injectors programmatically with createEnvironmentInjector and runInInjectionContext
SKILL.md
Angular Dependency Injection

Configure and use dependency injection in Angular v20+ with inject() and providers.

Basic Injection
Using inject()

Prefer inject() over constructor injection:

import { Component, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from './user.service';

@Component({
  selector: 'app-user-list',
  template: `...`,
})
export class UserList {
  // Inject dependencies
  private http = inject(HttpClient);
  private userService = inject(User);
  
  // Can use immediately
  users = this.userService.getUsers();
}

Injectable Services
import { Injectable, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root', // Singleton at root level
})
export class User {
  private http = inject(HttpClient);
  
  private users = signal<User[]>([]);
  readonly users$ = this.users.asReadonly();
  
  async loadUsers() {
    const users = await firstValueFrom(
      this.http.get<User[]>('/api/users')
    );
    this.users.set(users);
  }
}

Provider Scopes
Root Level (Singleton)
// Recommended: providedIn
@Injectable({
  providedIn: 'root',
})
export class Auth {}

// Alternative: in app.config.ts
export const appConfig: ApplicationConfig = {
  providers: [
    Auth,
  ],
};

Component Level (Instance per Component)
@Component({
  selector: 'app-editor',
  providers: [EditorState], // New instance for each component
  template: `...`,
})
export class Editor {
  private editorState = inject(EditorState);
}

Route Level
export const routes: Routes = [
  {
    path: 'admin',
    providers: [Admin], // Shared within this route tree
    children: [
      { path: '', component: AdminDashboard },
      { path: 'users', component: AdminUsers },
    ],
  },
];

Injection Tokens
Creating Tokens
import { InjectionToken } from '@angular/core';

// Simple value token
export const API_URL = new InjectionToken<string>('API_URL');

// Object token
export interface AppConfig {
  apiUrl: string;
  features: {
    darkMode: boolean;
    analytics: boolean;
  };
}

export const APP_CONFIG = new InjectionToken<AppConfig>('APP_CONFIG');

// Token with factory (self-providing)
export const WINDOW = new InjectionToken<Window>('Window', {
  providedIn: 'root',
  factory: () => window,
});

export const LOCAL_STORAGE = new InjectionToken<Storage>('LocalStorage', {
  providedIn: 'root',
  factory: () => localStorage,
});

Providing Token Values
// app.config.ts
export const appConfig: ApplicationConfig = {
  providers: [
    { provide: API_URL, useValue: 'https://api.example.com' },
    {
      provide: APP_CONFIG,
      useValue: {
        apiUrl: 'https://api.example.com',
        features: { darkMode: true, analytics: true },
      },
    },
  ],
};

Injecting Tokens
@Injectable({ providedIn: 'root' })
export class Api {
  private apiUrl = inject(API_URL);
  private config = inject(APP_CONFIG);
  private window = inject(WINDOW);
  
  getBaseUrl(): string {
    return this.apiUrl;
  }
}

Provider Types
useClass
// Provide implementation
{ provide: Logger, useClass: ConsoleLogger }

// Conditional implementation
{
  provide: Logger,
  useClass: environment.production
    ? ProductionLogger
    : ConsoleLogger,
}

useValue
// Static values
{ provide: API_URL, useValue: 'https://api.example.com' }

// Configuration objects
{ provide: APP_CONFIG, useValue: { theme: 'dark', language: 'en' } }

useFactory
// Factory with dependencies
{
  provide: User,
  useFactory: (http: HttpClient, config: AppConfig) => {
    return new User(http, config.apiUrl);
  },
  deps: [HttpClient, APP_CONFIG],
}

// Async factory (not recommended - use provideAppInitializer)
{
  provide: CONFIG,
  useFactory: () => fetch('/config.json').then(r => r.json()),
}

useExisting
// Alias to existing provider
{ provide: AbstractLogger, useExisting: ConsoleLogger }

// Multiple tokens pointing to same instance
providers: [
  ConsoleLogger,
  { provide: Logger, useExisting: ConsoleLogger },
  { provide: ErrorLogger, useExisting: ConsoleLogger },
]

Injection Options
Optional Injection
@Component({...})
export class My {
  // Returns null if not provided
  private analytics = inject(Analytics, { optional: true });
  
  trackEvent(name: string) {
    this.analytics?.track(name);
  }
}

Self, SkipSelf, Host
@Component({
  providers: [Local],
})
export class Parent {
  // Only look in this component's injector
  private local = inject(Local, { self: true });
}

@Component({...})
export class Child {
  // Skip this component, look in parent
  private parentService = inject(ParentSvc, { skipSelf: true });

  // Only look up to host component
  private hostService = inject(Host, { host: true });
}

Multi Providers

Collect multiple values for same token:

// Token for multiple validators
export const VALIDATORS = new InjectionToken<Validator[]>('Validators');

// Provide multiple values
providers: [
  { provide: VALIDATORS, useClass: RequiredValidator, multi: true },
  { provide: VALIDATORS, useClass: EmailValidator, multi: true },
  { provide: VALIDATORS, useClass: MinLengthValidator, multi: true },
]

// Inject as array
@Injectable()
export class Validation {
  private validators = inject(VALIDATORS); // Validator[]
  
  validate(value: string): ValidationError[] {
    return this.validators
      .map(v => v.validate(value))
      .filter(Boolean);
  }
}

HTTP Interceptors (Multi Provider)
// Interceptors use multi providers internally
export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(
      withInterceptors([
        authInterceptor,
        loggingInterceptor,
        errorInterceptor,
      ])
    ),
  ],
};

App Initializers

Run async code before app starts using provideAppInitializer:

import { provideAppInitializer, inject } from '@angular/core';

export const appConfig: ApplicationConfig = {
  providers: [
    Config,
    provideAppInitializer(() => {
      const configService = inject(Config);
      return configService.loadConfig();
    }),
  ],
};

Multiple Initializers
providers: [
  provideAppInitializer(() => {
    const config = inject(Config);
    return config.load();
  }),
  provideAppInitializer(() => {
    const auth = inject(Auth);
    return auth.checkSession();
  }),
]

Environment Injector

Create injectors programmatically:

import { createEnvironmentInjector, EnvironmentInjector, inject } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class Plugin {
  private parentInjector = inject(EnvironmentInjector);
  
  loadPlugin(providers: Provider[]): EnvironmentInjector {
    return createEnvironmentInjector(providers, this.parentInjector);
  }
}

runInInjectionContext

Run code with injection context:

import { runInInjectionContext, EnvironmentInjector, inject } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class Utility {
  private injector = inject(EnvironmentInjector);
  
  executeWithDI<T>(fn: () => T): T {
    return runInInjectionContext(this.injector, fn);
  }
}

// Usage
utilityService.executeWithDI(() => {
  const http = inject(HttpClient);
  // Use http...
});


For advanced patterns, see references/di-patterns.md.

Weekly Installs
4.1K
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