---
rating: ⭐⭐
title: dockerfile-optimise
url: https://skills.sh/pproenca/dot-skills/dockerfile-optimise
---

# dockerfile-optimise

skills/pproenca/dot-skills/dockerfile-optimise
dockerfile-optimise
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill dockerfile-optimise
SKILL.md
Dockerfile Optimization Best Practices

Comprehensive Dockerfile optimization guide sourced exclusively from official Docker documentation. Contains 48 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

When to Apply

Reference these guidelines when:

Writing new Dockerfiles or modifying existing ones
Optimizing Docker build times (layer caching, cache mounts, context management)
Reducing Docker image size (multi-stage builds, minimal base images)
Hardening container security (secret mounts, non-root users, attestations)
Setting up CI/CD pipelines with Docker builds
Reviewing Dockerfiles for anti-patterns
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Layer Caching & Ordering	CRITICAL	cache-
2	Multi-Stage Builds	CRITICAL	stage-
3	Base Image Selection	HIGH	base-
4	Build Context Management	HIGH	ctx-
5	Security & Secrets	HIGH	sec-
6	Dependency Management	MEDIUM-HIGH	dep-
7	Instruction Patterns	MEDIUM	inst-
8	Quality & Validation	MEDIUM	lint-
Quick Reference
1. Layer Caching & Ordering (CRITICAL)
cache-layer-order - Order layers by change frequency
cache-copy-deps-first - Copy dependency files before source code
cache-copy-link - Use COPY --link for cache-efficient layer copying
cache-mount-package - Use cache mounts for package managers
cache-apt-combine - Combine apt-get update with install
cache-external - Use external cache for CI/CD builds
cache-invalidation - Avoid unnecessary cache invalidation
cache-minimize-layers - Consolidate related RUN instructions
2. Multi-Stage Builds (CRITICAL)
stage-separate-build-runtime - Separate build and runtime stages
stage-named-stages - Use named build stages
stage-parallel-branches - Exploit parallel stage execution
stage-target-builds - Use target builds for dev/prod
stage-copy-artifacts-only - Copy only final artifacts between stages
stage-reusable-base - Create reusable base stages
3. Base Image Selection (HIGH)
base-minimal-image - Use minimal base images
base-official-images - Use Docker Official Images
base-pin-versions - Pin base image versions with digests
base-arg-version - Use ARG before FROM to parameterize base images
base-rebuild-regularly - Rebuild images regularly with --pull
base-distroless - Use distroless or scratch images for production
4. Build Context Management (HIGH)
ctx-dockerignore - Use .dockerignore to exclude unnecessary files
ctx-bind-mounts - Use bind mounts instead of COPY for build-only files
ctx-minimize-context - Keep build context small
ctx-syntax-directive - Use syntax directive for latest BuildKit features (prerequisite for cache mounts, secret mounts, heredocs, COPY --link)
5. Security & Secrets (HIGH)
sec-secret-mounts - Use secret mounts for sensitive data
sec-non-root-user - Run as non-root user
sec-no-secrets-in-args - Never pass secrets via ARG or ENV
sec-ssh-mounts - Use SSH mounts for private repository access
sec-attestations - Enable SBOM and provenance attestations
sec-no-unnecessary-packages - Avoid installing unnecessary packages
sec-ephemeral-containers - Design ephemeral, stateless containers
6. Dependency Management (MEDIUM-HIGH)
dep-cache-mount-apt - Use cache mount for apt package manager
dep-cache-mount-npm - Use cache mount for npm, yarn, and pnpm
dep-cache-mount-pip - Use cache mount for pip
dep-version-pin - Pin package versions for reproducibility
dep-cleanup-caches - Clean package manager caches in the same layer
7. Instruction Patterns (MEDIUM)
inst-json-cmd - Use JSON form for CMD and ENTRYPOINT
inst-healthcheck - Define HEALTHCHECK for container orchestration
inst-heredoc-scripts - Use heredocs for multi-line scripts
inst-entrypoint-exec - Use exec in entrypoint scripts
inst-workdir-absolute - Use absolute paths with WORKDIR
inst-copy-over-add - Prefer COPY over ADD
8. Quality & Validation (MEDIUM)
lint-build-checks - Enable Docker build checks
lint-pipefail - Use pipefail for piped RUN commands
lint-labels - Use standard labels for image metadata
lint-sort-arguments - Sort multi-line arguments alphabetically
lint-single-concern - One concern per container
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
156
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