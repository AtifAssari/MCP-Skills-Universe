---
title: angular-module-design
url: https://skills.sh/aj-geddes/useful-ai-prompts/angular-module-design
---

# angular-module-design

skills/aj-geddes/useful-ai-prompts/angular-module-design
angular-module-design
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill angular-module-design
SKILL.md
Angular Module Design
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Architect scalable Angular applications using feature modules, lazy loading, services, and RxJS for reactive programming patterns.

When to Use
Large Angular applications
Feature-based organization
Lazy loading optimization
Dependency injection patterns
Reactive state management
Quick Start

Minimal working example:

// users.module.ts
import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { ReactiveFormsModule } from "@angular/forms";
import { UsersRoutingModule } from "./users-routing.module";
import { UsersListComponent } from "./components/users-list/users-list.component";
import { UserDetailComponent } from "./components/user-detail/user-detail.component";
import { UsersService } from "./services/users.service";

@NgModule({
  declarations: [UsersListComponent, UserDetailComponent],
  imports: [CommonModule, ReactiveFormsModule, UsersRoutingModule],
  providers: [UsersService],
})
export class UsersModule {}

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Feature Module Structure	Feature Module Structure
Lazy Loading Routes	Lazy Loading Routes
Service with RxJS	Service with RxJS
Smart and Presentational Components	Smart and Presentational Components
Dependency Injection and Providers	Dependency Injection and Providers
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
293
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass