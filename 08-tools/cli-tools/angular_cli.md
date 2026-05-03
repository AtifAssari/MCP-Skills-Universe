---
rating: ⭐⭐⭐
title: angular-cli
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-cli
---

# angular-cli

skills/oguzhan18/angular-ecosystem-skills/angular-cli
angular-cli
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-cli
SKILL.md
@angular/cli

Version: Angular 21 (2025) Tags: CLI, Generators, Build, Scaffolding

References: CLI Reference • Generators • Builders

API Changes

This section documents recent version-specific API changes.

NEW: Control flow migration — ng g @angular/core:control-flow for @if/@for migration source

NEW: Signal input migration — ng g @angular/core:signal-input-migration for signal inputs source

NEW: Route lazy loading migration — ng g @angular/core:route-lazy-loading for standalone routes

NEW: Named workspaces — Multiple applications in single angular.json

NEW: esbuild by default — Faster builds with esbuild/Vite

Best Practices
Use generators for scaffolding
# Generate component
ng g c components/my-component

# Generate service
ng g s services/my-service

# Generate guard
ng g g guards/auth

# Generate interceptor
ng g interceptor timing

# Generate library
ng g library my-lib

# Generate with standalone
ng g c my-component --standalone

Use schematics for migrations
# Migrate to control flow
ng g @angular/core:control-flow

# Migrate to signal inputs
ng g @angular/core:signal-input-migration

# Migrate to lazy loading routes
ng g @angular/core:route-lazy-loading

Use ng add for packages
# Add Angular Material
ng add @angular/material

# Add SSR
ng add @angular/ssr

# Add PWA
ng add @angular/pwa

Configure workspace defaults
{
  "$schema": "./node_modules/@angular/cli/lib/config/schema.json",
  "version": 1,
  "newProjectRoot": "projects",
  "projects": {
    "my-app": {
      "schematics": {
        "@schematics/angular:component": {
          "style": "scss",
          "standalone": true
        }
      }
    }
  }
}

Use ng run for builders
# Run custom builder
ng run my-app:build

# Run SSR
ng run my-app:serve-ssr

# Run prerender
ng run my-app:prerender

Use ng config for settings
# Set default style
ng config defaults.style=scss

# Enable analytics
ng analytics enable

Use ng update for migrations
# Update packages
ng update

# Update specific package
ng update @angular/core

Use ng build with options
# Production build
ng build --configuration=production

# Dev build with stats
ng build --stats-json

Use standalone by default
# New project with standalone
ng new my-app --standalone

Use functional over class-based
# Generate functional guard
ng g g guards/auth --functional

# Generate functional interceptor
ng g interceptor my-interceptor --functional

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