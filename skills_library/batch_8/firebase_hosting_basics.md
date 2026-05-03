---
title: firebase-hosting-basics
url: https://skills.sh/firebase/agent-skills/firebase-hosting-basics
---

# firebase-hosting-basics

skills/firebase/agent-skills/firebase-hosting-basics
firebase-hosting-basics
Installation
$ npx skills add https://github.com/firebase/agent-skills --skill firebase-hosting-basics
Summary

Deploy static sites, SPAs, and microservices to a global CDN with zero-config SSL.

Supports static sites, single-page apps (React, Vue, etc.), and dynamic content via Cloud Functions or Cloud Run integration
Includes preview channels for testing changes on temporary URLs before live deployment, with GitHub Actions automation
Configure routing, redirects, rewrites, and headers via firebase.json; emulate locally at http://localhost:5000 before deploying
Not intended for full-stack frameworks requiring server-side rendering; use Firebase App Hosting for Next.js, Angular, or similar
SKILL.md
hosting-basics

This skill provides instructions and references for working with Firebase Hosting, a fast and secure hosting service for your web app, static and dynamic content, and microservices.

Overview

Firebase Hosting provides production-grade web content hosting for developers. With a single command, you can deploy web apps and serve both static and dynamic content to a global CDN (content delivery network).

Key Features:

Fast Content Delivery: Files are cached on SSDs at CDN edges around the world.
Secure by Default: Zero-configuration SSL is built-in.
Preview Channels: View and test changes on temporary preview URLs before deploying live.
GitHub Integration: Automate previews and deploys with GitHub Actions.
Dynamic Content: Serve dynamic content and microservices using Cloud Functions or Cloud Run.
Hosting vs App Hosting

Choose Firebase Hosting if:

You are deploying a static site (HTML/CSS/JS).
You are deploying a simple SPA (React, Vue, etc. without SSR).
You want full control over the build and deploy process via CLI.

Choose Firebase App Hosting if:

You are using a supported full-stack framework like Next.js or Angular.
You need Server-Side Rendering (SSR) or ISR.
You want an automated "git push to deploy" workflow with zero configuration.
Instructions
1. Configuration (firebase.json)

For details on configuring Hosting behavior, including public directories, redirects, rewrites, and headers, see configuration.md.

2. Deploying

For instructions on deploying your site, using preview channels, and managing releases, see deploying.md.

3. Emulation

To test your app locally:

npx -y firebase-tools@latest emulators:start --only hosting


This serves your app at http://localhost:5000 by default.

Weekly Installs
39.3K
Repository
firebase/agent-skills
GitHub Stars
264
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass