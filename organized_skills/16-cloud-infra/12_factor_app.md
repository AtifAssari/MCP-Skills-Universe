---
rating: ⭐⭐
title: 12-factor-app
url: https://skills.sh/pproenca/dot-skills/12-factor-app
---

# 12-factor-app

skills/pproenca/dot-skills/12-factor-app
12-factor-app
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill 12-factor-app
SKILL.md
Community Cloud-Native Applications Best Practices

Comprehensive methodology for building modern software-as-a-service applications that are portable, scalable, and maintainable. Contains 51 rules across 12 categories, covering the entire application lifecycle from codebase management to production operations.

When to Apply

Reference these guidelines when:

Designing new backend services or APIs
Containerizing applications for Kubernetes or Docker
Setting up CI/CD pipelines
Managing configuration across environments
Implementing logging and monitoring
Planning application scaling strategy
Debugging deployment or environment issues
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Codebase & Version Control	CRITICAL	code-
2	Dependencies	CRITICAL	dep-
3	Configuration	CRITICAL	config-
4	Backing Services	HIGH	svc-
5	Build, Release, Run	HIGH	build-
6	Processes & State	HIGH	proc-
7	Concurrency & Scaling	HIGH	scale-
8	Disposability	HIGH	disp-
9	Port Binding	MEDIUM	port-
10	Dev/Prod Parity	MEDIUM	parity-
11	Logging	MEDIUM	log-
12	Admin Processes	MEDIUM	admin-
Quick Reference
1. Codebase & Version Control (CRITICAL)
code-single-codebase - Maintain one codebase per application in version control
code-one-app-one-repo - Enforce one-to-one correlation between codebase and application
code-deploys-not-branches - Use deploys not branches to represent environments
code-shared-as-libraries - Factor shared code into libraries managed by dependency manager
2. Dependencies (CRITICAL)
dep-explicit-declaration - Declare all dependencies explicitly in a manifest file
dep-isolate-execution - Isolate dependencies to prevent system package leakage
dep-no-system-tools - Never rely on implicit system tools being available
dep-deterministic-builds - Use lockfiles for deterministic dependency resolution
3. Configuration (CRITICAL)
config-separate-from-code - Strictly separate configuration from code
config-use-env-vars - Store configuration in environment variables
config-no-env-groups - Treat environment variables as granular controls not grouped environments
config-validate-on-startup - Validate required configuration at application startup
config-never-commit-secrets - Never commit secrets or credentials to version control
4. Backing Services (HIGH)
svc-as-attached-resources - Treat backing services as attached resources
svc-connection-strings - Reference all backing services via connection URLs in config
svc-no-local-vs-remote - Make no distinction between local and third-party services
svc-detach-attach-without-code - Design services to be detachable and attachable without code changes
5. Build, Release, Run (HIGH)
build-separate-stages - Strictly separate build, release, and run stages
build-immutable-releases - Create immutable releases with unique identifiers
build-no-runtime-changes - Never modify code at runtime - changes require new release
build-complexity-in-build - Push complexity into build stage keep run stage minimal
build-artifact-per-commit - Generate one build artifact per commit deploy same artifact everywhere
6. Processes & State (HIGH)
proc-stateless-processes - Execute the application as stateless processes
proc-no-sticky-sessions - Never use sticky sessions - store session data in backing services
proc-no-local-filesystem - Never assume local filesystem persists between requests
proc-compile-at-build - Perform asset compilation and bundling at build time not runtime
proc-share-nothing - Design processes to share nothing with each other
7. Concurrency & Scaling (HIGH)
scale-process-model - Scale out via the process model with multiple process types
scale-process-types - Assign workloads to appropriate process types
scale-no-daemonize - Never daemonize or write PID files let process manager handle it
scale-horizontal-not-vertical - Design for horizontal scaling over vertical scaling
scale-process-formation - Define process formation as declarative configuration
8. Disposability (HIGH)
disp-disposable-processes - Design processes to be disposable started or stopped at any moment
disp-fast-startup - Minimize startup time to enable rapid scaling and recovery
disp-graceful-shutdown - Implement graceful shutdown on SIGTERM
disp-crash-only - Design for crash-only software that recovers from sudden death
disp-idempotent-operations - Make operations idempotent to safely retry after failures
9. Port Binding (MEDIUM)
port-self-contained - Make the application completely self-contained with embedded server
port-export-via-binding - Export services via port binding using PORT environment variable
port-any-protocol - Use port binding to export any protocol not just HTTP
10. Dev/Prod Parity (MEDIUM)
parity-minimize-gaps - Minimize gaps between development and production environments
parity-same-backing-services - Use the same type and version of backing services in all environments
parity-deploy-frequently - Deploy frequently to minimize the time gap
parity-developers-deploy - Involve developers in deployment to minimize personnel gap
11. Logging (MEDIUM)
log-event-streams - Treat logs as event streams not files
log-no-routing - Never route or store logs from within the application
log-structured-format - Use structured logging for machine-readable event streams
log-unbuffered-stdout - Write logs unbuffered to stdout for real-time streaming
12. Admin Processes (MEDIUM)
admin-one-off-processes - Run admin tasks as one-off processes not special scripts
admin-same-environment - Run admin processes against a release with same codebase and config
admin-repl-access - Provide REPL access for debugging and data inspection
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
146
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass