---
title: progressive-web-app
url: https://skills.sh/aj-geddes/useful-ai-prompts/progressive-web-app
---

# progressive-web-app

skills/aj-geddes/useful-ai-prompts/progressive-web-app
progressive-web-app
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill progressive-web-app
SKILL.md
Progressive Web App
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build progressive web applications with offline support, installability, service workers, and web app manifests to deliver app-like experiences in the browser.

When to Use
App-like web experiences
Offline functionality needed
Mobile installation required
Push notifications
Fast loading experiences
Quick Start

Minimal working example:

// public/manifest.json
{
  "name": "My Awesome App",
  "short_name": "AwesomeApp",
  "description": "A progressive web application",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "orientation": "portrait-primary",
  "background_color": "#ffffff",
  "theme_color": "#007bff",
  "icons": [
    {
      "src": "/images/icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/images/icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any"
    },
    {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Web App Manifest	Web App Manifest
Service Worker Implementation	Service Worker Implementation
Install Prompt and App Installation	Install Prompt and App Installation
Offline Support with IndexedDB	Offline Support with IndexedDB
Push Notifications	Push Notifications
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
297
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass