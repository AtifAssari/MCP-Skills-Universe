---
rating: ⭐⭐⭐
title: spring-boot-full-stack
url: https://skills.sh/mduongvandinh/skills-java-spring/spring-boot-full-stack
---

# spring-boot-full-stack

skills/mduongvandinh/skills-java-spring/spring-boot-full-stack
spring-boot-full-stack
Installation
$ npx skills add https://github.com/mduongvandinh/skills-java-spring --skill spring-boot-full-stack
SKILL.md
Spring Boot Full Stack Skill
Overview

This skill provides a complete, modular framework for building Java Spring Boot applications with enterprise-grade features.

Quick Start
# Minimal setup (PostgreSQL + JWT only)
mvn clean install -Pminimal

# With Redis caching
mvn clean install -Dmodule.redis.enabled=true

# Full stack (all modules)
mvn clean install -Pfull-stack

# Run application
mvn spring-boot:run -Dspring-boot.run.profiles=local

Module Selection
Module	Default	Enable Flag
PostgreSQL	ON	-Dmodule.postgresql.enabled=true
Redis	OFF	-Dmodule.redis.enabled=true
Kafka	OFF	-Dmodule.kafka.enabled=true
RabbitMQ	OFF	-Dmodule.rabbitmq.enabled=true
OAuth2	OFF	-Dmodule.oauth2.enabled=true
Development Workflow
Spec First: Define specifications in openspec/specs/
TDD: Write tests first (RED)
Implement: Write minimal code (GREEN)
Refactor: Improve code quality
Archive: Update specs after implementation
Docker Options
# Without Docker (services installed locally)
make dev

# With Docker infrastructure
make dev-docker

# Full Docker deployment
docker compose --profile with-app up -d

Skills Included
Core (Always enabled)
spring-project-init - Project initialization
spring-maven-modular - Maven profiles & BOM
spring-error-handling - Global exception handling
spring-validation - Request validation
spring-logging - Structured logging
spring-testing - Unit + Integration testing
spring-tdd-mockito - TDD with Mockito
spring-openspec - Spec-First Development
Optional
spring-redis - Redis caching
spring-kafka - Kafka messaging
spring-rabbitmq - RabbitMQ messaging
spring-oauth2 - OAuth2/OIDC
spring-rbac - Role-based access control
spring-docker - Docker containerization
spring-api-docs - OpenAPI/Swagger
spring-monitoring - Actuator + Prometheus
File Structure
src/
├── main/
│   ├── java/
│   │   └── com/company/app/
│   │       ├── config/           # Configuration classes
│   │       ├── controller/       # REST controllers
│   │       ├── service/          # Business logic
│   │       ├── repository/       # Data access
│   │       ├── domain/           # Entities
│   │       ├── dto/              # Data transfer objects
│   │       ├── exception/        # Custom exceptions
│   │       └── security/         # Security configuration
│   └── resources/
│       ├── application.yml
│       ├── application-local.yml
│       ├── application-dev.yml
│       ├── application-prod.yml
│       └── db/migration/         # Flyway migrations
├── test/
│   └── java/
│       └── com/company/app/
│           ├── unit/             # Unit tests
│           └── integration/      # Integration tests
└── openspec/
    ├── AGENTS.md
    ├── specs/                    # Feature specifications
    └── changes/                  # Proposed changes

References
Anthropic Skills Specification
OpenSpec - Spec-Driven Development
Spring Boot Documentation
Weekly Installs
107
Repository
mduongvandinh/s…a-spring
GitHub Stars
6
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass