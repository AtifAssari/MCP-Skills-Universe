---
title: firebase-app-hosting-basics
url: https://skills.sh/firebase/agent-skills/firebase-app-hosting-basics
---

# firebase-app-hosting-basics

skills/firebase/agent-skills/firebase-app-hosting-basics
firebase-app-hosting-basics
Installation
$ npx skills add https://github.com/firebase/agent-skills --skill firebase-app-hosting-basics
Summary

Deploy and manage full-stack web apps with Firebase App Hosting using Next.js, Angular, and other supported frameworks.

Requires Firebase project on Blaze pricing plan; supports Server-Side Rendering (SSR) and Incremental Static Regeneration (ISR) workflows
Deploy via firebase.json configuration with optional apphosting.yaml for backend setup, or enable automated "git push to deploy" through GitHub integration
Includes secret management via CLI commands for secure access to sensitive keys and local testing through Firebase Local Emulator Suite
Best suited for full-stack applications; use Firebase Hosting instead for static sites or simple SPAs without SSR
SKILL.md
App Hosting Basics
Description

This skill enables the agent to deploy and manage modern, full-stack web applications (Next.js, Angular, etc.) using Firebase App Hosting.

Important: In order to use App Hosting, your Firebase project must be on the Blaze pricing plan. Direct the user to https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered to upgrade their plan.

Hosting vs App Hosting

Choose Firebase Hosting if:

You are deploying a static site (HTML/CSS/JS).
You are deploying a simple SPA (React, Vue, etc. without SSR).
You want full control over the build and deploy process via CLI.

Choose Firebase App Hosting if:

You are using a supported full-stack framework like Next.js or Angular.
You need Server-Side Rendering (SSR) or ISR.
You want an automated "git push to deploy" workflow with zero configuration.
Deploying to App Hosting
Deploy from Source

This is the recommended flow for most users.

Configure firebase.json with an apphosting block.
{
  "apphosting": {
    "backendId": "my-app-id",
    "rootDir": "/",
    "ignore": [
      "node_modules",
      ".git",
      "firebase-debug.log",
      "firebase-debug.*.log",
      "functions"
    ]
  }
}

Create or edit apphosting.yaml- see Configuration for more information on how to do so.
If the app needs safe access to sensitive keys, use npx -y firebase-tools@latest apphosting:secrets commands to set and grant access to secrets.
Run npx -y firebase-tools@latest deploy when you are ready to deploy.
Automated deployment via GitHub (CI/CD)

Alternatively, set up a backend connected to a GitHub repository for automated deployments "git push" deployments. This is only recommended for more advanced users, and is not required to use App Hosting. See CLI Commands for more information on how to set this up using CLI commands.

Emulation

See Emulation for more information on how to test your app locally using the Firebase Local Emulator Suite.

Weekly Installs
39.1K
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