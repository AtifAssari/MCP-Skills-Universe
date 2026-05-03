---
title: graceful-shutdown
url: https://skills.sh/aj-geddes/useful-ai-prompts/graceful-shutdown
---

# graceful-shutdown

skills/aj-geddes/useful-ai-prompts/graceful-shutdown
graceful-shutdown
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill graceful-shutdown
SKILL.md
Graceful Shutdown
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement proper shutdown procedures to ensure all requests are completed, connections are closed, and resources are released before process termination.

When to Use
Kubernetes/Docker deployments
Rolling updates and deployments
Server restarts
Load balancer drain periods
Zero-downtime deployments
Process managers (PM2, systemd)
Long-running background jobs
Database connection cleanup
Quick Start

Minimal working example:

import express from "express";
import http from "http";

class GracefulShutdownServer {
  private app: express.Application;
  private server: http.Server;
  private isShuttingDown = false;
  private activeConnections = new Set<any>();
  private shutdownTimeout = 30000; // 30 seconds

  constructor() {
    this.app = express();
    this.server = http.createServer(this.app);
    this.setupMiddleware();
    this.setupRoutes();
    this.setupShutdownHandlers();
  }

  private setupMiddleware(): void {
    // Track active connections
    this.app.use((req, res, next) => {
      if (this.isShuttingDown) {
        res.set("Connection", "close");
        return res.status(503).json({
          error: "Server is shutting down",
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Express.js Graceful Shutdown	Express.js Graceful Shutdown
Kubernetes-Aware Shutdown	Kubernetes-Aware Shutdown
Worker Process Shutdown	Worker Process Shutdown
Database Connection Pool Shutdown	Database Connection Pool Shutdown
PM2 Graceful Shutdown	PM2 Graceful Shutdown
Python/Flask Graceful Shutdown	Python/Flask Graceful Shutdown
Best Practices
✅ DO
Handle SIGTERM and SIGINT signals
Stop accepting new requests immediately
Wait for in-flight requests to complete
Set reasonable shutdown timeouts
Close database connections properly
Flush logs and metrics
Fail health checks during shutdown
Test shutdown procedures
Log shutdown progress
Use graceful shutdown in containers
❌ DON'T
Ignore shutdown signals
Force kill processes without cleanup
Set unreasonably long timeouts
Skip resource cleanup
Forget to close connections
Block shutdown indefinitely
Weekly Installs
265
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