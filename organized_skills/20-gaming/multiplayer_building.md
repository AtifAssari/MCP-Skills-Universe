---
rating: ⭐⭐
title: multiplayer-building
url: https://skills.sh/bbeierle12/skill-mcp-claude/multiplayer-building
---

# multiplayer-building

skills/bbeierle12/skill-mcp-claude/multiplayer-building
multiplayer-building
Installation
$ npx skills add https://github.com/bbeierle12/skill-mcp-claude --skill multiplayer-building
SKILL.md
Multiplayer Building

Networking layer for multiplayer building games.

Quick Start
import { BuildingNetworkServer, BuildingNetworkClient } from './scripts/building-network-manager.js';

// Server
const server = new BuildingNetworkServer(buildingSystem, {
  tickRate: 20,
  conflictStrategy: 'first_write'
});
server.start();

// Client
const client = new BuildingNetworkClient(buildingSystem);
client.connect('ws://server:8080');
const localPiece = client.placeRequest('wall', position, rotation);

Reference

See references/multiplayer-networking.md for:

Authority model comparison
Delta compression strategy
Conflict resolution approaches
Large structure synchronization
Scripts
scripts/delta-compression.js - Only sync changed state (Source engine pattern)
scripts/client-prediction.js - Optimistic placement with rollback
scripts/conflict-resolver.js - Handle simultaneous builds (first-write, timestamp, lock-based)
scripts/building-network-manager.js - Complete server/client system
Architecture

Server-authoritative with client prediction:

Client predicts placement locally (ghost piece)
Server validates and confirms/rejects
Client reconciles with server state
Delta compression syncs only changes
Weekly Installs
47
Repository
bbeierle12/skil…p-claude
GitHub Stars
8
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn