---
rating: ⭐⭐⭐
title: dr-jskill
url: https://skills.sh/jdubois/dr-jskill/dr-jskill
---

# dr-jskill

skills/jdubois/dr-jskill/dr-jskill
dr-jskill
Installation
$ npx skills add https://github.com/jdubois/dr-jskill --skill dr-jskill
SKILL.md
Spring Boot skill that follows Julien Dubois' best practices.
Overview

This agent skill helps you create Spring Boot projects following Julien Dubois' best practices. It provides tools and scripts to quickly bootstrap Spring Boot applications using https://start.spring.io.

Version Management

Centralized versions live in versions.json. All scripts read from it via scripts/lib/versions.mjs (JavaScript). Update this file to bump Java, Spring Boot fallback, Postgres, Node/npm, Testcontainers, etc.

Prerequisites
Java 25 installed
Node.js 24.x and NPM 11.x (for front-end development)
Docker installed and running
Capabilities
Generate Spring Boot projects with predefined configurations
Support for various Spring Boot versions and dependencies
Follow best practices for project structure and configuration
Quick setup scripts for common use cases
Docker support for containerized deployments
Front-end development with multiple framework options:
Vue.js 3 (default) - Progressive framework with Composition API
React 19 - Popular library for building user interfaces
Angular 21 - Full-featured framework with TypeScript
Vanilla JavaScript - No framework, pure ES6+ with Vite
Usage
Using the Scripts

This skill includes cross-platform JavaScript (Node.js) scripts in the scripts/ directory that can be used to download pre-configured Spring Boot projects from start.spring.io. They work on Linux, macOS, and Windows.

Unified launcher (cross-platform):

node scripts/create-project my-app com.myco my-app com.myco.myapp 21 fullstack


Direct invocation:

node scripts/create-project-latest.mjs my-app com.myco my-app com.myco.myapp 21 fullstack


Flags supported:

--boot-version <x.y.z> / -BootVersion: override Spring Boot version
--project-type basic|web|fullstack / -ProjectType

Tip: The create-project-latest script auto-resolves preferred Boot 4.x and falls back to the configured springBootFallback if 4.x is not yet available. Override with --boot-version if needed.

Latest Version Project ⭐

Use the create-project-latest.mjs script to create a project with the latest Spring Boot version (automatically fetched):

node scripts/create-project-latest.mjs my-app com.mycompany my-app com.mycompany.myapp 21 web


Project types available:

basic - Minimal Spring Boot project
web - Web application with REST API capabilities
fullstack - Complete application with database and security
Basic Spring Boot Project

Use the create-basic-project.mjs script to create a basic Spring Boot project with essential dependencies:

node scripts/create-basic-project.mjs

Web Application

Use the create-web-project.mjs script to create a Spring Boot web application with web dependencies:

node scripts/create-web-project.mjs

Full-Stack Application

Use the create-fullstack-project.mjs script to create a comprehensive Spring Boot application with database, security, and web dependencies:

node scripts/create-fullstack-project.mjs

Best Practices

When creating Spring Boot projects:

Use the latest Spring Boot version (currently 4.x) - the create-project-latest.mjs script automatically fetches it
Review Spring Boot 4 critical considerations: See Spring Boot 4 Migration Guide for Jackson 3 annotations and TestContainers configuration
Include Spring Boot Actuator for production-ready features
Use Spring Data JPA for database access
Use PostgreSQL for database - see Database Best Practices for optimization
Use properties files for configuration - see Configuration Best Practices
Set up foundational dotfiles: .gitignore, .env.sample, .editorconfig, .gitattributes, .dockerignore, optional .vscode/, .devcontainer/ - see Project Setup & Dotfiles
The .env file is the canonical location for local secrets; instruct users to copy .env.sample → .env and fill in real values
NEVER read or expose .env: it contains real secrets — do not cat, view, or print its contents; only .env.sample (placeholder values) may be read or displayed
Use spring-boot-docker-compose for automatic database startup during development - see Docker Guide
Follow RESTful API design principles
Configure proper logging with Logback - see Logging Best Practices
Use Maven for dependency management
Include Spring Boot DevTools for development productivity
Add Spring Security only when needed - see Security Guide for best practices
Configure Docker for containerized deployments - see Docker Guide
Enable GraalVM native image support for faster startup - see GraalVM Guide
Always ship a startup banner that prints access URLs when the app is ready - see Startup Banner
The user must review changes before they are committed to git. Ask the user before initializing a Git repository, or running git commands.
Java Code Intelligence (JDTLS) ⭐

Generated projects integrate with the Eclipse JDT Language Server (JDTLS) so AI agents can navigate, refactor, and diagnose Java code semantically rather than with text search. The scripts ship a .github/lsp.json that wires JDTLS into GitHub Copilot CLI automatically.

For the AI agent: when working on Java files, prefer the lsp tool over grep/view/sed. It understands imports, generics, inheritance, and Javadoc.

Task	Use
Find where a class/method is defined	lsp goToDefinition
Find callers before changing a signature	lsp findReferences or incomingCalls
Look up types, parameters, Javadoc	lsp hover
List symbols in a file	lsp documentSymbol
Search a class/method across the project	lsp workspaceSymbol
Rename safely across files	lsp rename (never sed)
Check compile errors before ./mvnw verify	ide-get_diagnostics

Preference order for Java work: lsp → grep with .java glob → view.

Install JDTLS once: brew install jdtls (or see JDTLS guide for other platforms). Full setup, gotchas, and editor integrations live in references/JDTLS.md.

Project Structure

The service layer is only included if it adds value (e.g. complex business logic). For simple CRUD applications, the controller can directly call the repository.

Generated projects follow the following recommended structure:

my-spring-boot-app/
├── .gitignore                 # Java + front-end + secrets (see references/PROJECT-SETUP.md)
├── .env.sample                # Template for local env vars; .env is gitignored
├── .editorconfig              # Consistent formatting across IDEs
├── .gitattributes             # Normalize line endings, better diffs
├── .dockerignore              # Slim Docker build contexts
├── .vscode/                   # Optional editor recommendations
│   ├── extensions.json
│   └── settings.json
├── .devcontainer/             # Optional Dev Container (Java 25 + Node 24 + PostgreSQL)
│   ├── devcontainer.json
│   └── docker-compose.yml
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/example/app/
│   │   │       ├── Application.java
│   │   │       ├── config/
│   │   │       ├── controller/
│   │   │       ├── service/         # Only included if needed
│   │   │       ├── repository/
│   │   │       └── domain/
│   │   └── resources/
│   │       ├── static/              # Front-end web assets (HTML, CSS, JS)
│   │       │   ├── index.html
│   │       │   ├── css/
│   │       │   │   └── styles.css
│   │       │   ├── js/
│   │       │   │   └── app.js
│   │       │   └── images/
│   │       └── application.properties
│   └── test/
│       └── java/
│           └── com/example/app/
│               ├── config/
│               ├── controller/
│               ├── service/         # Only included if needed
│               ├── repository/
│               └── domain/
├── Dockerfile                   # Standard JVM Docker build
├── Dockerfile-native            # GraalVM native image build
├── compose.yaml                 # Dev database (spring-boot-docker-compose)
├── docker-compose.yml           # Full stack with PostgreSQL
├── docker-compose-native.yml    # Native image with PostgreSQL
├── pom.xml
└── README.md

Dependencies

Generated projects include: Spring Web, Spring Data JPA, Spring Boot Actuator, DevTools, PostgreSQL, Validation, Docker Compose support, Test Starter with JUnit 5, and TestContainers.

Configuration

Use .properties files (not YAML), externalize secrets via environment variables, and leverage @ConfigurationProperties for type safety. See the Configuration Guide for profiles, secrets management, and common patterns.

The .env file is the single local secret store — never read or print it; only .env.sample (placeholder values) may be shown.

For database optimization, see the Database Best Practices Guide.

Security (Optional)

Spring Security is optional - only add it when you need authentication or authorization. See the Security Guide for JWT, OAuth2, role-based access, and CORS configuration.

Testing

See the Testing Guide for unit tests (Mockito, @WebMvcTest), integration tests (TestContainers + @ServiceConnection), and Given-When-Then patterns with AssertJ.

Front-End Development

Choose a front-end framework:

Vue.js 3 (default) ⭐ → Vue.js Guide
React 19 → React Guide
Angular 21 → Angular Guide
Vanilla JavaScript (no framework) → Vanilla JS Guide

All options include: Vite/CLI dev server with hot reload, Bootstrap 5.3+, SPA routing, and automatic build into the Spring Boot JAR.

Non-interactive scaffolding (important for CI and AI agents). Two separate prompts must be silenced:

npm's own "Ok to proceed?" install prompt — silence by placing -y before the package name (flags after -- go to the scaffolder, not to npm). Use npm create -y vite@latest … or npx --yes create-vite@latest ….
The scaffolder's own prompts — create-vite 8.x and Angular CLI 21 still pose interactive questions (e.g. "Use rolldown-vite?", analytics opt-in) that -y / --yes do not silence. The reliable fix is to close stdin: pipe echo | into the command so the scaffolder immediately sees EOF and accepts defaults.

Canonical recipes:

React / Vanilla: echo | npx --yes create-vite@latest frontend --template react (or --template vanilla)
Vue: npm create -y vue@latest frontend -- --router --pinia --vitest --eslint --prettier (create-vue does not pose extra prompts)
Angular: echo | npx --yes @angular/cli@21 new frontend --style=css --ssr=false --skip-git --defaults --skip-install, then npm install
Docker Deployment

Spring Boot automatically manages Docker containers during development via spring-boot-docker-compose. For production, use the provided Dockerfile (JVM) or Dockerfile-native (GraalVM). See the Docker Guide for full setup, health checks, and deployment patterns.

GraalVM Native Images

Build native images via Docker (no local GraalVM needed) or locally with ./mvnw -Pnative -DskipTests package native:compile. See the GraalVM Guide for configuration, runtime hints, testing, and CI/CD integration.

Azure Deployment

Deploy to Azure Container Apps with an optional VNET-injected Azure Database for PostgreSQL Flexible Server. Uses GitHub Container Registry (GHCR) for image storage (pushed via GITHUB_TOKEN in CI, pulled by Container Apps using a stored PAT) and Container Apps secrets for the DB password — no secrets in source, env dumps, or shell history. Includes a GitHub Actions OIDC workflow, and supports both the JVM and GraalVM native image variants. See the Azure Deployment Guide.

Validation
#	What	Command
1	Build backend	./mvnw clean install
2	Unit tests	./mvnw test
3	Integration tests	./mvnw verify (uses Testcontainers 2 + @ServiceConnection)
4	Front-end dev server	cd frontend && npm run dev

Run validation steps first. If anything fails, fix before proceeding.

Once the project is generated, go through the steps above to ensure that the generated project is fully functional and follows best practices. If any validation step fails, try to identify the issue and fix it before proceeding. This ensures that the generated project is of high quality and ready for development.

Additional Resources
Included Reference Guides

Core Spring Boot:

Spring Boot 4 Migration Guide - Key changes from Spring Boot 3, Jackson 3 annotations
Configuration Best Practices - Properties files, profiles, secrets management
Logging Best Practices - Logback configuration and patterns
Java Code Intelligence (JDTLS) - LSP-based navigation, refactoring, diagnostics

Data and Persistence:

Database Best Practices - PostgreSQL and Hibernate optimization

Security (Optional):

Security Guide - Spring Security, JWT, OAuth2, authentication patterns

Testing:

Testing Guide - Unit and integration testing with TestContainers

Front-End Development:

Vue.js Development Guide - Vue.js 3 with Vite (default)
React Development Guide - React 19 with Vite
Angular Development Guide - Angular 21 with Angular CLI
Vanilla JS Development Guide - Pure ES6+ with Vite

Project Setup:

Project Setup & Dotfiles - .gitignore, .env.sample, .editorconfig, .gitattributes, .dockerignore, .devcontainer/

Deployment:

Docker Deployment Guide - Docker, Docker Compose, development automation
GraalVM Native Images Guide - Docker-based native builds, optimization
Azure Deployment Guide - Azure Container Apps, PostgreSQL Flexible Server, GitHub Container Registry (GHCR) image push/pull, Container Apps secrets for DB password, GitHub Actions OIDC
Weekly Installs
48
Repository
jdubois/dr-jskill
GitHub Stars
208
First Seen
Feb 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn