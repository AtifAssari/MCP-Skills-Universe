---
title: astro
url: https://skills.sh/astrolicious/agent-skills/astro
---

# astro

skills/astrolicious/agent-skills/astro
astro
Installation
$ npx skills add https://github.com/astrolicious/agent-skills --skill astro
Summary

CLI commands, project structure conventions, and deployment adapters for Astro web projects.

Core CLI includes dev server, build, type checking, integration management, and TypeScript sync commands
Standard project structure uses src/pages for routes, src/components for reusable components, and public/ for static assets
Deploy via adapters for Node.js, Cloudflare, Netlify, Vercel, or community-maintained platforms using npx astro add
Configuration file (astro.config.js or variants) supports core options like site URL for sitemap and canonical URL generation
SKILL.md
Astro Usage Guide

Always consult docs.astro.build for code examples and latest API.

Astro is the web framework for content-driven websites.

Quick Reference
File Location

CLI looks for astro.config.js, astro.config.mjs, astro.config.cjs, and astro.config.ts in: ./. Use --config for custom path.

CLI Commands
npx astro dev - Start the development server.
npx astro build - Build your project and write it to disk.
npx astro check - Check your project for errors.
npx astro add - Add an integration.
npx astro sync - Generate TypeScript types for all Astro modules.

Re-run after adding/changing plugins.

Project Structure

Reference project structure docs.

src/* - Project source code (components, pages, styles, images, etc.)
src/pages - Required. Defines all pages and routes.
src/components - Components (convention, not required).
src/layouts - Layout components (convention, not required).
src/styles - CSS/Sass files (convention, not required).
public/* - Non-code, unprocessed assets (fonts, icons, etc.); copied as-is to build output.
package.json - Project manifest.
astro.config.{js,mjs,cjs,ts} - Astro configuration file. (recommended)
tsconfig.json - TypeScript configuration file. (recommended)
Core Config Options
Option	Notes
site	Your final, deployed URL. Used to generate sitemaps and canonical URLs.
Example astro.config.ts
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://example.com',
});

Common Workflows
Creating a Basic Page

Add a file to src/pages/ — the filename becomes the route:

---
// src/pages/index.astro
const title = 'Hello, Astro!';
---
<html>
  <head><title>{title}</title></head>
  <body>
    <h1>{title}</h1>
  </body>
</html>

Creating a Component
---
// src/components/Card.astro
const { title, body } = Astro.props;
---
<div class="card">
  <h2>{title}</h2>
  <p>{body}</p>
</div>

Deploying with an Adapter
Add the adapter: npx astro add vercel --yes (or node, cloudflare, netlify)
Run npx astro check to catch type and configuration errors before building.
Run npx astro build to produce the deployment artifact.
Verify the build output directory (e.g. dist/) exists and is non-empty before proceeding.
Deploy the output per the adapter's documentation.
Adapters

Deploy to your favorite server, serverless, or edge host with build adapters. Use an adapter to enable on-demand rendering in your Astro project.

Add Node.js adapter using astro add:

npx astro add node --yes


Add Cloudflare adapter using astro add:

npx astro add cloudflare --yes


Add Netlify adapter using astro add:

npx astro add netlify --yes


Add Vercel adapter using astro add:

npx astro add vercel --yes


Other Community adapters

Resources
Docs
Config Reference
llms.txt
GitHub
Weekly Installs
5.4K
Repository
astrolicious/ag…t-skills
GitHub Stars
5
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass