---
title: health-check-endpoints
url: https://skills.sh/aj-geddes/useful-ai-prompts/health-check-endpoints
---

# health-check-endpoints

skills/aj-geddes/useful-ai-prompts/health-check-endpoints
health-check-endpoints
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill health-check-endpoints
SKILL.md
Health Check Endpoints
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement health check endpoints to monitor service health, dependencies, and readiness for traffic.

When to Use
Kubernetes liveness and readiness probes
Load balancer health checks
Service discovery and registration
Monitoring and alerting systems
Circuit breaker decisions
Auto-scaling triggers
Deployment verification
Quick Start

Minimal working example:

import express from "express";
import { Pool } from "pg";
import Redis from "ioredis";

interface HealthStatus {
  status: "healthy" | "degraded" | "unhealthy";
  timestamp: string;
  uptime: number;
  checks: Record<string, CheckResult>;
  version?: string;
  environment?: string;
}

interface CheckResult {
  status: "pass" | "fail" | "warn";
  time: number;
  output?: string;
  error?: string;
}

class HealthCheckService {
  private startTime = Date.now();
  private version = process.env.APP_VERSION || "1.0.0";
  private environment = process.env.NODE_ENV || "development";

// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Express.js Health Checks	Express.js Health Checks
Spring Boot Actuator-Style (Java)	Spring Boot Actuator-Style (Java)
Python Flask Health Checks	Python Flask Health Checks
Best Practices
✅ DO
Implement separate liveness and readiness probes
Keep liveness probes lightweight
Check critical dependencies in readiness
Return appropriate HTTP status codes
Include response time metrics
Set reasonable timeouts
Cache health check results briefly
Include version and environment info
Monitor health check failures
❌ DON'T
Make liveness probes check dependencies
Return 200 for failed health checks
Take too long to respond
Skip important dependency checks
Expose sensitive information
Ignore health check failures
Weekly Installs
281
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass