---
rating: ⭐⭐⭐
title: configuration-management
url: https://skills.sh/aj-geddes/useful-ai-prompts/configuration-management
---

# configuration-management

skills/aj-geddes/useful-ai-prompts/configuration-management
configuration-management
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill configuration-management
SKILL.md
Configuration Management
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Comprehensive guide to managing application configuration across environments, including environment variables, configuration files, secrets, feature flags, and following 12-factor app methodology.

When to Use
Setting up configuration for different environments
Managing secrets and credentials
Implementing feature flags
Creating configuration hierarchies
Following 12-factor app principles
Migrating configuration to cloud services
Implementing dynamic configuration
Managing multi-tenant configurations
Quick Start

Minimal working example:

# .env.development
NODE_ENV=development
PORT=3000
DATABASE_URL=postgresql://localhost:5432/myapp_dev
REDIS_URL=redis://localhost:6379
LOG_LEVEL=debug
API_KEY=dev-api-key-12345

# .env.production
NODE_ENV=production
PORT=8080
DATABASE_URL=${DATABASE_URL}  # From environment
REDIS_URL=${REDIS_URL}
LOG_LEVEL=info
API_KEY=${API_KEY}  # From secret manager

# .env.test
NODE_ENV=test
DATABASE_URL=postgresql://localhost:5432/myapp_test
LOG_LEVEL=error

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Environment Variables	Environment Variables
Configuration Hierarchies	Configuration Hierarchies
Secret Management	Secret Management
Feature Flags	Feature Flags
12-Factor App Configuration	12-Factor App Configuration
Configuration Validation	Configuration Validation
Dynamic Configuration (Remote Config)	Dynamic Configuration (Remote Config)
Best Practices
✅ DO
Store configuration in environment variables
Use different config files per environment
Validate configuration on startup
Use secret managers for sensitive data
Never commit secrets to version control
Provide sensible defaults
Document all configuration options
Use type-safe configuration objects
Implement configuration hierarchy (base + overrides)
Use feature flags for gradual rollouts
Follow 12-factor app principles
Implement graceful degradation for missing config
Cache secrets to reduce API calls
❌ DON'T
Hardcode configuration in source code
Commit .env files with real secrets
Use different config formats across services
Store secrets in plain text
Expose configuration through APIs
Use production credentials in development
Ignore configuration validation errors
Access process.env directly everywhere
Store configuration in databases (circular dependency)
Mix configuration with business logic
Weekly Installs
276
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