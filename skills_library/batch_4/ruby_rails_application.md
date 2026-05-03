---
title: ruby-rails-application
url: https://skills.sh/aj-geddes/useful-ai-prompts/ruby-rails-application
---

# ruby-rails-application

skills/aj-geddes/useful-ai-prompts/ruby-rails-application
ruby-rails-application
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill ruby-rails-application
SKILL.md
Ruby Rails Application
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build comprehensive Ruby on Rails applications with proper model associations, RESTful controllers, Active Record queries, authentication systems, middleware chains, and view rendering following Rails conventions.

When to Use
Building Rails web applications
Implementing Active Record models with associations
Creating RESTful controllers and actions
Integrating authentication and authorization
Building complex database relationships
Implementing Rails middleware and filters
Quick Start

Minimal working example:

rails new myapp --api --database=postgresql
cd myapp
rails db:create

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Rails Project Setup	Rails Project Setup
Models with Active Record	Models with Active Record
Database Migrations	Database Migrations
Controllers with RESTful Actions	Controllers with RESTful Actions
Authentication with JWT	Authentication with JWT
Active Record Queries	Active Record Queries
Serializers	Serializers
Best Practices
✅ DO
Use conventions over configuration
Leverage Active Record associations
Implement proper scopes for queries
Use strong parameters for security
Implement authentication in ApplicationController
Use services for complex business logic
Implement proper error handling
Use database migrations for schema changes
Validate all inputs at model level
Use before_action filters appropriately
❌ DON'T
Use raw SQL without parameterization
Implement business logic in controllers
Trust user input without validation
Store secrets in code
Use select * without specifying columns
Forget N+1 query problems (use includes/joins)
Implement authentication in each controller
Use global variables
Ignore database constraints
Weekly Installs
439
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass