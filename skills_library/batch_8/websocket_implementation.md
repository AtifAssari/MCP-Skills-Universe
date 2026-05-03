---
title: websocket-implementation
url: https://skills.sh/aj-geddes/useful-ai-prompts/websocket-implementation
---

# websocket-implementation

skills/aj-geddes/useful-ai-prompts/websocket-implementation
websocket-implementation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill websocket-implementation
SKILL.md
WebSocket Implementation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build scalable WebSocket systems for real-time communication with proper connection management, message routing, error handling, and horizontal scaling support.

When to Use
Building real-time chat and messaging
Implementing live notifications
Creating collaborative editing tools
Broadcasting live data updates
Building real-time dashboards
Streaming events to clients
Live multiplayer games
Quick Start

Minimal working example:

const express = require("express");
const http = require("http");
const socketIo = require("socket.io");
const redis = require("redis");

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: { origin: "*" },
  transports: ["websocket", "polling"],
  reconnection: true,
  reconnectionDelay: 1000,
  reconnectionDelayMax: 5000,
  reconnectionAttempts: 5,
});

// Redis adapter for horizontal scaling
const redisClient = redis.createClient();
const { createAdapter } = require("@socket.io/redis-adapter");

io.adapter(createAdapter(redisClient, redisClient.duplicate()));

// Connection management
const connectedUsers = new Map();

// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Node.js WebSocket Server (Socket.IO)	Node.js WebSocket Server (Socket.IO)
Browser WebSocket Client	Browser WebSocket Client
Python WebSocket Server (aiohttp)	Python WebSocket Server (aiohttp)
Message Types and Protocols	Message Types and Protocols
Scaling with Redis	Scaling with Redis
Best Practices
✅ DO
Implement proper authentication
Handle reconnection gracefully
Manage rooms/channels effectively
Persist messages appropriately
Monitor active connections
Implement presence features
Use Redis for scaling
Add message acknowledgment
Implement rate limiting
Handle errors properly
❌ DON'T
Send unencrypted sensitive data
Keep unlimited message history in memory
Allow arbitrary room/channel creation
Forget to clean up disconnected connections
Send large messages frequently
Ignore network failures
Store passwords in messages
Skip authentication/authorization
Create unbounded growth of connections
Ignore scalability from day one
Weekly Installs
403
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn