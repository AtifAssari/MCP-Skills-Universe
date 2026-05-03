---
title: uptime-monitoring
url: https://skills.sh/aj-geddes/useful-ai-prompts/uptime-monitoring
---

# uptime-monitoring

skills/aj-geddes/useful-ai-prompts/uptime-monitoring
uptime-monitoring
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill uptime-monitoring
SKILL.md
Uptime Monitoring
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Set up comprehensive uptime monitoring with health checks, status pages, and incident tracking to ensure visibility into service availability.

When to Use
Service availability tracking
Health check implementation
Status page creation
Incident management
SLA monitoring
Quick Start

Minimal working example:

// Node.js health check
const express = require("express");
const app = express();

app.get("/health", (req, res) => {
  res.json({
    status: "ok",
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
  });
});

app.get("/health/deep", async (req, res) => {
  const health = {
    status: "ok",
    checks: {
      database: "unknown",
      cache: "unknown",
      externalApi: "unknown",
    },
  };

  try {
    const dbResult = await db.query("SELECT 1");
    health.checks.database = dbResult ? "ok" : "error";
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Health Check Endpoints	Health Check Endpoints
Python Health Checks	Python Health Checks
Uptime Monitor with Heartbeat	Uptime Monitor with Heartbeat
Public Status Page API	Public Status Page API
Kubernetes Health Probes	Kubernetes Health Probes
Best Practices
✅ DO
Implement comprehensive health checks
Check all critical dependencies
Use appropriate timeout values
Track response times
Store check history
Monitor uptime trends
Alert on status changes
Use standard HTTP status codes
❌ DON'T
Check only application process
Ignore external dependencies
Set timeouts too low
Alert on every failure
Use health checks for load balancing
Expose sensitive information
Weekly Installs
294
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