---
rating: ⭐⭐⭐
title: angular-tooling
url: https://skills.sh/analogjs/angular-skills/angular-tooling
---

# angular-tooling

skills/analogjs/angular-skills/angular-tooling
angular-tooling
Installation
$ npx skills add https://github.com/analogjs/angular-skills --skill angular-tooling
Summary

Angular CLI and development tools for v20+ project setup, code generation, building, testing, and configuration.

Covers project creation, component/service/directive/pipe generation, and schematic-based code scaffolding with inline templates and change detection options
Includes development server configuration, production builds with budgets and hashing, and bundle analysis via stats-json output
Supports unit and e2e testing, linting with auto-fix, and environment-based file replacements for multi-environment builds
Handles library integration (Angular Material, PWA, SSR, Localize), Angular version updates, and persistent build caching
SKILL.md
Angular Tooling

Use Angular CLI and development tools for efficient Angular v20+ development.

Project Setup
Create New Project
# Create new standalone project (default in v20+)
ng new my-app

# With specific options
ng new my-app --style=scss --routing --ssr=false

# Skip tests
ng new my-app --skip-tests

# Minimal setup
ng new my-app --minimal --inline-style --inline-template

Project Structure
my-app/
├── src/
│   ├── app/
│   │   ├── app.component.ts
│   │   ├── app.config.ts
│   │   └── app.routes.ts
│   ├── index.html
│   ├── main.ts
│   └── styles.scss
├── public/                  # Static assets
├── angular.json             # CLI configuration
├── package.json
├── tsconfig.json
└── tsconfig.app.json

Code Generation
Components
# Generate component
ng generate component features/user-profile
ng g c features/user-profile  # Short form

# With options
ng g c shared/button --inline-template --inline-style
ng g c features/dashboard --skip-tests
ng g c features/settings --change-detection=OnPush

# Flat (no folder)
ng g c shared/icon --flat

# Dry run (preview)
ng g c features/checkout --dry-run

Services
# Generate service (providedIn: 'root' by default)
ng g service services/auth
ng g s services/user

# Skip tests
ng g s services/api --skip-tests

Other Schematics
# Directive
ng g directive directives/highlight
ng g d directives/tooltip

# Pipe
ng g pipe pipes/truncate
ng g p pipes/date-format

# Guard (functional by default)
ng g guard guards/auth

# Interceptor (functional by default)
ng g interceptor interceptors/auth

# Interface
ng g interface models/user

# Enum
ng g enum models/status

# Class
ng g class models/product

Generate with Path Alias
# Components in feature folders
ng g c @features/products/product-list
ng g c @shared/ui/button

Development Server
# Start dev server
ng serve
ng s  # Short form

# With options
ng serve --port 4201
ng serve --open  # Open browser
ng serve --host 0.0.0.0  # Expose to network

# Production mode locally
ng serve --configuration=production

# With SSL
ng serve --ssl --ssl-key ./ssl/key.pem --ssl-cert ./ssl/cert.pem

Building
Development Build
ng build

Production Build
ng build --configuration=production
ng build -c production  # Short form

# With specific options
ng build -c production --source-map=false
ng build -c production --named-chunks

Build Output
dist/my-app/
├── browser/
│   ├── index.html
│   ├── main-[hash].js
│   ├── polyfills-[hash].js
│   └── styles-[hash].css
└── server/              # If SSR enabled
    └── main.js

Testing
Unit Tests
# Run tests
ng test
ng t  # Short form

# Single run (CI)
ng test --watch=false --browsers=ChromeHeadless

# With coverage
ng test --code-coverage

# Specific file
ng test --include=**/user.service.spec.ts

E2E Tests
# Run e2e (if configured)
ng e2e

Linting
# Run linter
ng lint

# Fix auto-fixable issues
ng lint --fix

Configuration
angular.json Key Sections
{
  "projects": {
    "my-app": {
      "architect": {
        "build": {
          "builder": "@angular-devkit/build-angular:application",
          "options": {
            "outputPath": "dist/my-app",
            "index": "src/index.html",
            "browser": "src/main.ts",
            "polyfills": ["zone.js"],
            "tsConfig": "tsconfig.app.json",
            "assets": ["{ \"glob\": \"**/*\", \"input\": \"public\" }"],
            "styles": ["src/styles.scss"],
            "scripts": []
          },
          "configurations": {
            "production": {
              "budgets": [
                {
                  "type": "initial",
                  "maximumWarning": "500kB",
                  "maximumError": "1MB"
                }
              ],
              "outputHashing": "all"
            },
            "development": {
              "optimization": false,
              "extractLicenses": false,
              "sourceMap": true
            }
          }
        }
      }
    }
  }
}

Environment Configuration
// src/environments/environment.ts
export const environment = {
  production: false,
  apiUrl: 'http://localhost:3000/api',
};

// src/environments/environment.prod.ts
export const environment = {
  production: true,
  apiUrl: 'https://api.example.com',
};


Configure in angular.json:

{
  "configurations": {
    "production": {
      "fileReplacements": [
        {
          "replace": "src/environments/environment.ts",
          "with": "src/environments/environment.prod.ts"
        }
      ]
    }
  }
}

Adding Libraries
Angular Libraries
# Add Angular Material
ng add @angular/material

# Add Angular PWA
ng add @angular/pwa

# Add Angular SSR
ng add @angular/ssr

# Add Angular Localize
ng add @angular/localize

Third-Party Libraries
# Install and configure
npm install @ngrx/signals

# Some libraries have schematics
ng add @ngrx/store

Update Angular
# Check for updates
ng update

# Update Angular core and CLI
ng update @angular/core @angular/cli

# Update all packages
ng update --all

# Force update (skip peer dependency checks)
ng update @angular/core @angular/cli --force

Performance Analysis
# Build with stats
ng build -c production --stats-json

# Analyze bundle (install esbuild-visualizer)
npx esbuild-visualizer --metadata dist/my-app/browser/stats.json --open

Caching
# Enable persistent build cache (default in v20+)
# Configured in angular.json:
{
  "cli": {
    "cache": {
      "enabled": true,
      "path": ".angular/cache",
      "environment": "all"
    }
  }
}

# Clear cache
rm -rf .angular/cache


For advanced configuration, see references/tooling-patterns.md.

Weekly Installs
3.7K
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