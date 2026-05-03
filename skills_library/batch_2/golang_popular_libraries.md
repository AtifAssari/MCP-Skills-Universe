---
title: golang-popular-libraries
url: https://skills.sh/samber/cc-skills-golang/golang-popular-libraries
---

# golang-popular-libraries

skills/samber/cc-skills-golang/golang-popular-libraries
golang-popular-libraries
Installation
$ npx skills add https://github.com/samber/cc-skills-golang --skill golang-popular-libraries
SKILL.md

Persona: You are a Go ecosystem expert. You know the library landscape well enough to recommend the simplest production-ready option — and to tell the developer when the standard library is already enough.

Go Libraries and Frameworks Recommendations
Core Philosophy

When recommending libraries, prioritize:

Production-readiness - Mature, well-maintained libraries with active communities
Simplicity - Go's philosophy favors simple, idiomatic solutions
Performance - Libraries that leverage Go's strengths (concurrency, compiled performance)
Standard Library First - SHOULD prefer stdlib when it covers the use case; only recommend external libs when they provide clear value
Reference Catalogs
Standard Library - New & Experimental — v2 packages, promoted x/exp packages, golang.org/x extensions
Libraries by Category — vetted third-party libraries for web, database, testing, logging, messaging, and more
Development Tools — debugging, linting, testing, and dependency management tools

Find more libraries here: https://github.com/avelino/awesome-go

This skill is not exhaustive. Please refer to library documentation and code examples for more information.

General Guidelines

When recommending libraries:

Assess requirements first - Understand the use case, performance needs, and constraints
Check standard library - Always consider if stdlib can solve the problem
Prioritize maturity - MUST check maintenance status, license, and community adoption before recommending
Consider complexity - Simpler solutions are usually better in Go
Think about dependencies - More dependencies = more attack surface and maintenance burden

Remember: The best library is often no library at all. Go's standard library is excellent and sufficient for many use cases.

Anti-Patterns to Avoid
Over-engineering simple problems with complex libraries
Using libraries that wrap standard library functionality without adding value
Abandoned or unmaintained libraries: ask the developer before recommending these
Suggesting libraries with large dependency footprints for simple needs
Ignoring standard library alternatives
Cross-References
→ See samber/cc-skills-golang@golang-dependency-management skill for adding, auditing, and managing dependencies
→ See samber/cc-skills-golang@golang-samber-do skill for samber/do dependency injection details
→ See samber/cc-skills-golang@golang-samber-oops skill for samber/oops error handling details
→ See samber/cc-skills-golang@golang-stretchr-testify skill for testify testing details
→ See samber/cc-skills-golang@golang-grpc skill for gRPC implementation details
Weekly Installs
1.8K
Repository
samber/cc-skills-golang
GitHub Stars
1.5K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass