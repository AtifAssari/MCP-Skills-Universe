---
rating: ⭐⭐
title: debug
url: https://skills.sh/lobehub/lobehub/debug
---

# debug

skills/lobehub/lobehub/debug
debug
Installation
$ npx skills add https://github.com/lobehub/lobehub --skill debug
Summary

Debug logging utility with namespace-based filtering across desktop, server, and client environments.

Follows strict namespace conventions (e.g., lobe-server:[module], lobe-desktop:[module]) to organize logs by platform and module
Supports format specifiers including %O for expanded objects, %s for strings, and %d for numbers
Enable output via localStorage.debug in browsers, DEBUG environment variable in Node.js, or process.env.DEBUG in Electron
Wildcard filtering (e.g., lobe-*) allows selective log visibility across the entire codebase
SKILL.md
Debug Package Usage Guide
Basic Usage
import debug from 'debug';

// Format: lobe-[module]:[submodule]
const log = debug('lobe-server:market');

log('Simple message');
log('With variable: %O', object);
log('Formatted number: %d', number);

Namespace Conventions
Desktop: lobe-desktop:[module]
Server: lobe-server:[module]
Client: lobe-client:[module]
Router: lobe-[type]-router:[module]
Format Specifiers
%O - Object expanded (recommended for complex objects)
%o - Object
%s - String
%d - Number
Enable Debug Output
Browser
localStorage.debug = 'lobe-*';

Node.js
DEBUG=lobe-* npm run dev
DEBUG=lobe-* pnpm dev

Electron
process.env.DEBUG = 'lobe-*';

Example
// src/server/routers/edge/market/index.ts
import debug from 'debug';

const log = debug('lobe-edge-router:market');

log('getAgent input: %O', input);

Weekly Installs
819
Repository
lobehub/lobehub
GitHub Stars
75.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass