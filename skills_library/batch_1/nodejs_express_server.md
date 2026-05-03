---
title: nodejs-express-server
url: https://skills.sh/aj-geddes/useful-ai-prompts/nodejs-express-server
---

# nodejs-express-server

skills/aj-geddes/useful-ai-prompts/nodejs-express-server
nodejs-express-server
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill nodejs-express-server
Summary

Production-ready Express.js servers with routing, middleware, authentication, and database integration.

Covers core Express patterns including middleware chains, RESTful routing with CRUD operations, and error handling middleware
Supports authentication via JWT, database integration with PostgreSQL and Sequelize, and environment-based configuration
Includes best practices for input validation, async/await patterns, rate limiting, and HTTPS in production
Reference guides provided for basic setup, middleware implementation, database connections, and logging strategies
SKILL.md
Node.js Express Server
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Create robust Express.js applications with proper routing, middleware chains, authentication mechanisms, and database integration following industry best practices.

When to Use
Building REST APIs with Node.js
Implementing server-side request handling
Creating middleware chains for cross-cutting concerns
Managing authentication and authorization
Connecting to databases from Node.js
Implementing error handling and logging
Quick Start

Minimal working example:

const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get("/health", (req, res) => {
  res.json({ status: "OK", timestamp: new Date().toISOString() });
});

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(err.status || 500).json({
    error: err.message,
    requestId: req.id,
  });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Basic Express Setup	Basic Express Setup
Middleware Chain Implementation	Middleware Chain Implementation
Database Integration (PostgreSQL with Sequelize)	Database Integration (PostgreSQL with Sequelize)
Authentication with JWT	Authentication with JWT
RESTful Routes with CRUD Operations	RESTful Routes with CRUD Operations
Error Handling Middleware	Error Handling Middleware
Environment Configuration	Environment Configuration
Best Practices
✅ DO
Use middleware for cross-cutting concerns
Implement proper error handling
Validate input data before processing
Use async/await for async operations
Implement authentication on protected routes
Use environment variables for configuration
Add logging and monitoring
Use HTTPS in production
Implement rate limiting
Keep route handlers focused and small
❌ DON'T
Handle errors silently
Store sensitive data in code
Use synchronous operations in routes
Forget to validate user input
Implement authentication in route handlers
Use callback hell (use promises/async-await)
Expose stack traces in production
Trust client-side validation only
Weekly Installs
2.2K
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail