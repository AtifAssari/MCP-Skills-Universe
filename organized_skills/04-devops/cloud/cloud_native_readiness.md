---
rating: ⭐⭐⭐
title: cloud-native-readiness
url: https://skills.sh/zjy365/seakills/cloud-native-readiness
---

# cloud-native-readiness

skills/zjy365/seakills/cloud-native-readiness
cloud-native-readiness
Installation
$ npx skills add https://github.com/zjy365/seakills --skill cloud-native-readiness
SKILL.md
Cloud Native Readiness Assessment Skill
Overview

This skill evaluates a repository's readiness for cloud-native microservice deployment through a 3-phase workflow:

Assess - Analyze the project against cloud-native criteria and produce a readiness report
Detect - Check if Docker artifacts already exist (Dockerfile, docker-compose, container images)
Route - If artifacts exist, return the result directly; if not, invoke dockerfile-skill to containerize
Workflow
cloud-native-readiness
  │
  ├─ Phase 1: Cloud-Native Assessment
  │    ├─ NOT suitable → Report reasons, suggest remediation, END
  │    └─ Suitable → Continue
  │
  ├─ Phase 2: Existing Artifacts Detection
  │    ├─ Found Dockerfile/docker-compose/image → Report existing setup, END
  │    └─ Not found → Continue
  │
  └─ Phase 3: Route to dockerfile-skill
       └─ Invoke /dockerfile to generate Docker configuration

Usage
/cloud-native-readiness              # Assess current directory
/cloud-native-readiness <path>       # Assess specific path
/cloud-native-readiness <github-url> # Clone and assess

Quick Start

When invoked, ALWAYS follow this sequence:

Read and execute modules/assess.md — Cloud-native readiness evaluation
Read and execute modules/detect.md — Existing Docker artifacts detection
Read and execute modules/route.md — Decision routing
Phase 1: Cloud-Native Readiness Assessment

Load and execute: modules/assess.md

Evaluates 6 dimensions (each scored 0-2):

Dimension	What to check
Statelessness	Does the app store state locally (sessions in memory, local file writes)?
Config Externalization	Are configs hardcoded or driven by env vars / config files?
Horizontal Scalability	Can multiple instances run without conflicts?
Startup/Shutdown	Does the app start fast and handle SIGTERM gracefully?
Observability	Does it have health checks, structured logging, metrics?
Service Boundaries	Is it a focused service or a tightly-coupled monolith?

Scoring:

10-12: Excellent — fully cloud-native ready
7-9: Good — ready with minor adjustments
4-6: Fair — needs some refactoring before containerization
0-3: Poor — significant rework needed, not recommended for containerization now

Output: Structured readiness report with score, findings, and recommendations.

Phase 2: Existing Artifacts Detection

Load and execute: modules/detect.md

Checks for:

Dockerfile / Dockerfile.* (multi-stage, multi-service)
docker-compose.yml / docker-compose.yaml / compose.yml
.dockerignore
DOCKER.md or docker-related documentation
Container registry references (ghcr.io, docker.io, ECR, GCR, ACR)
Kubernetes manifests (k8s/, kubernetes/, deploy/, helm/, charts/)
CI/CD pipeline with Docker build steps (.github/workflows/, .gitlab-ci.yml)

Output: Inventory of existing Docker/K8s artifacts with quality assessment.

Phase 3: Routing Decision

Load and execute: modules/route.md

Decision Matrix:

Readiness Score	Artifacts Exist	Action
≥ 7	Yes, complete	Report existing setup. Done.
≥ 7	Yes, partial	Report gaps, suggest improvements. Done.
≥ 7	No	Invoke dockerfile-skill to generate.
4-6	Any	Report issues + remediation steps. Optionally proceed with dockerfile-skill.
0-3	Any	Report blockers. Do NOT invoke dockerfile-skill.
Readiness Report Format

The final output MUST use this format:

# Cloud-Native Readiness Report

## Summary
- **Project**: {name}
- **Score**: {score}/12 ({rating})
- **Verdict**: {Ready | Ready with caveats | Needs work | Not recommended}

## Assessment Details

### ✅ Strengths
- {what's already cloud-native friendly}

### ⚠️ Concerns
- {issues that need attention}

### ❌ Blockers (if any)
- {critical issues preventing containerization}

## Dimension Scores

| Dimension | Score | Notes |
|-----------|-------|-------|
| Statelessness | {0-2} | {detail} |
| Config Externalization | {0-2} | {detail} |
| Horizontal Scalability | {0-2} | {detail} |
| Startup/Shutdown | {0-2} | {detail} |
| Observability | {0-2} | {detail} |
| Service Boundaries | {0-2} | {detail} |

## Existing Docker Artifacts
- {inventory or "None found"}

## Recommendation
- {next steps}

Supporting Resources
Assessment Criteria: knowledge/criteria.md — Detailed scoring rubrics
Anti-Patterns: knowledge/anti-patterns.md — Common cloud-native anti-patterns
Examples: examples/ — Sample readiness reports
Integration with dockerfile-skill

When routing to dockerfile-skill, pass the assessment context:

The readiness report findings inform Dockerfile generation decisions
Detected external services map directly to docker-compose.yml services
Identified concerns become Dockerfile comments / DOCKER.md caveats
The assessment's config externalization findings drive ENV/ARG setup

Handoff: When invoking dockerfile-skill, include a summary of:

Detected language/framework/package manager
External service dependencies
Config externalization status
Any special concerns (stateful components, long startup, etc.)
Weekly Installs
41
Repository
zjy365/seakills
GitHub Stars
1
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn