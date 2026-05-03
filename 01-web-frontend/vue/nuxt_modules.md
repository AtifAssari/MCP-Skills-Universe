---
rating: ⭐⭐⭐
title: nuxt-modules
url: https://skills.sh/onmax/nuxt-skills/nuxt-modules
---

# nuxt-modules

skills/onmax/nuxt-skills/nuxt-modules
nuxt-modules
Installation
$ npx skills add https://github.com/onmax/nuxt-skills --skill nuxt-modules
Summary

Framework extensions through published npm packages, local modules, and runtime/server integrations.

Covers three module types: published npm packages (@nuxtjs/, nuxt-), local project modules in the modules/ directory, and inline hooks in nuxt.config.ts
Provides defineNuxtModule patterns, Kit utilities, and hook system for extending components, composables, plugins, API routes, and middleware
Includes E2E testing strategies, npm publishing workflows, and copy-paste CI/CD templates for automated releases
Quick-start scaffold via npx nuxi init -t module with playground for local development and testing
SKILL.md
Nuxt Module Development

Guide for creating Nuxt modules that extend framework functionality.

Related skills: nuxt (basics), vue (runtime patterns)

Quick Start
npx nuxi init -t module my-module
cd my-module && npm install
npm run dev        # Start playground
npm run dev:build  # Build in watch mode
npm run test       # Run tests

Available Guidance
references/development.md - Module anatomy, defineNuxtModule, Kit utilities, hooks
references/testing-and-publishing.md - E2E testing, best practices, releasing, publishing
references/ci-workflows.md - Copy-paste CI/CD workflow templates
Loading Files

Consider loading these reference files based on your task:

 references/development.md - if building module features, using defineNuxtModule, or working with Kit utilities
 references/testing-and-publishing.md - if writing E2E tests, publishing to npm, or following best practices
 references/ci-workflows.md - if setting up CI/CD workflows for your module

DO NOT load all files at once. Load only what's relevant to your current task.

Module Types
Type	Location	Use Case
Published	npm package	@nuxtjs/, nuxt- distribution
Local	modules/ dir	Project-specific extensions
Inline	nuxt.config.ts	Simple one-off hooks
Project Structure
my-module/
├── src/
│   ├── module.ts           # Entry point
│   └── runtime/            # Injected into user's app
│       ├── components/
│       ├── composables/
│       ├── plugins/
│       └── server/
├── playground/             # Dev testing
└── test/fixtures/          # E2E tests

Resources
Module Guide
Nuxt Kit
Module Starter
Weekly Installs
1.3K
Repository
onmax/nuxt-skills
GitHub Stars
649
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass