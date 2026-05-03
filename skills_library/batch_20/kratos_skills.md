---
title: kratos-skills
url: https://skills.sh/lwx-cloud/kratos-skills/kratos-skills
---

# kratos-skills

skills/lwx-cloud/kratos-skills/kratos-skills
kratos-skills
Installation
$ npx skills add https://github.com/lwx-cloud/kratos-skills --skill kratos-skills
SKILL.md
Kratos Skills for AI Agents

This skill provides comprehensive go-kratos microservices framework knowledge, optimized for AI agents helping developers build production-ready services.

🎯 When to Use This Skill

Invoke this skill when working with go-kratos:

Creating services: REST APIs, gRPC services, or microservices architectures
Layered architecture: Implementing Service → Biz → Data layers with DDD
Dependency injection: Using Wire for compile-time DI
Production hardening: Circuit breakers, rate limiting, middleware
Debugging: Understanding errors, fixing configuration, or resolving issues
Learning: Understanding kratos patterns and best practices
📚 Knowledge Structure

Load specific guides as needed rather than reading everything at once:

Quick Start

Link: Official Kratos Documentation Contains: Installation, project creation, basic commands, hello-world examples

Pattern Guides
API & Transport
File	When to Load
references/api-patterns.md	Defining Protobuf APIs, generating HTTP/gRPC code
references/transport-patterns.md	HTTP/gRPC server/client configuration
references/encoding-patterns.md	Custom serialization, content negotiation
references/openapi-guide.md	OpenAPI/Swagger documentation generation
Architecture & Design
File	When to Load
references/architecture-patterns.md	DDD layers, repository pattern, Wire DI
references/error-patterns.md	Error definition, assertions, proto errors
references/middleware-patterns.md	Custom middleware, request filtering
Infrastructure
File	When to Load
references/config-patterns.md	Configuration loading, hot reload, config centers
references/registry-patterns.md	Service discovery (etcd, consul, nacos, k8s)
references/selector-patterns.md	Load balancing (P2C, WRR, random)
Resilience & Reliability
File	When to Load
references/circuit-breaker-patterns.md	Fault tolerance, SRE circuit breaker
references/ratelimit-patterns.md	Token bucket, BBR rate limiting
references/recovery-patterns.md	Panic recovery, stack trace logging
Observability
File	When to Load
references/logging-patterns.md	Structured logging, Zap/Logrus adapters
references/metrics-patterns.md	Prometheus metrics collection
references/tracing-patterns.md	OpenTelemetry, Jaeger/Zipkin tracing
references/metadata-patterns.md	Context propagation, trace IDs
Security & Validation
File	When to Load
references/auth-patterns.md	JWT authentication, claims, token generation
references/validate-patterns.md	Proto field validation, protoc-gen-validate
Data & Tools
File	When to Load
references/ent-patterns.md	Ent ORM integration, schema design
references/cli-guide.md	kratos CLI, code generation commands
Supporting Resources
File	When to Load
best-practices/overview.md	Production deployment, code review checklist
troubleshooting/common-issues.md	Debugging errors, protoc/wire issues
getting-started/claude-code-guide.md	Claude Code integration, advanced features
🚀 Common Workflows
Creating a New Service
Create project: kratos new <project-name>
Define API: Create .proto with google.api.http annotations
Generate code: kratos proto client api/demo/v1/demo.proto
Generate service: kratos proto server api/demo/v1/demo.proto -t internal/service
Implement layers: Biz logic in internal/biz/, data access in internal/data/
Configure Wire: Update cmd/server/wire.go with provider sets
Run: go generate ./... && kratos run

Details: references/api-patterns.md

Implementing Layered Architecture
Define interfaces in internal/biz/ (biz layer)
Implement repositories in internal/data/ (data layer)
Write use cases in internal/biz/ (biz layer)
Implement handlers in internal/service/ (service layer)
Create ProviderSets: data.ProviderSet, biz.ProviderSet, service.ProviderSet
Wire together in cmd/server/wire.go

Details: references/architecture-patterns.md

Adding Middleware
http.Middleware(
    recovery.Recovery(),           // 1. Catch panics first
    validate.Validator(),          // 2. Validate requests
    jwt.Server(keyFunc),           // 3. Authentication
    ratelimit.Server(limiter),     // 4. Rate limiting
    logging.Server(logger),        // 5. Logging
)


Details: references/middleware-patterns.md

Configuring Service Discovery
// Server-side
reg := etcd.New(client)
app := kratos.New(kratos.Registrar(reg))

// Client-side
dis := etcd.New(client)
conn, _ := grpc.DialInsecure(
    context.Background(),
    grpc.WithEndpoint("discovery:///service-name"),
    grpc.WithDiscovery(dis),
)


Details: references/registry-patterns.md

⚡ Key Principles
✅ Always Follow
Layer separation: Service (API) → Biz (Business) → Data (Persistence)
Dependency Inversion: Interfaces in biz, implementations in data
Protobuf-first: Define APIs and errors in .proto files
Wire injection: Compile-time DI, no global state
Context propagation: Pass ctx context.Context through all layers
Interface-based design: Program to interfaces, not implementations
Error codes: Structured errors with code, reason, message, metadata
❌ Never Do
Put business logic in service handlers (violates layered architecture)
Skip interface definition and use concrete types directly
Use global variables for dependencies
Define HTTP handlers manually (use generated code from proto)
Hard-code configuration values
Skip validation or forget to check err != nil
Modify generated .pb.go files
📖 Progressive Learning Path
🟢 New to kratos?
Official Quick Start - Install CLI, create first project
references/architecture-patterns.md - Understand Service → Biz → Data
references/api-patterns.md - Learn Protobuf API definition
🟡 Building production services?
best-practices/overview.md - Production checklist
references/circuit-breaker-patterns.md + references/ratelimit-patterns.md - Add resilience
references/registry-patterns.md - Service discovery
troubleshooting/common-issues.md - Avoid pitfalls
🔵 Extending capabilities?
getting-started/claude-code-guide.md - Advanced Claude Code features
Kratos Examples - Example projects
🔗 Kratos Ecosystem
Project	Purpose
kratos	Framework core, CLI tools
kratos-layout	Official project template
contrib	Plugins for config, registry, log, metrics
aegis	Availability algorithms
gateway	API Gateway
examples	Example code
📝 Version Compatibility
Target version: kratos v2.0.0+
Go version: Go 1.19 or later recommended
Protoc: 3.0+

Quick invocation: Use /kratos-skills or ask "How do I [task] with kratos?"

Weekly Installs
35
Repository
lwx-cloud/kratos-skills
GitHub Stars
1
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass