---
title: technical-doc-creator
url: https://skills.sh/mhattingpete/claude-skills-marketplace/technical-doc-creator
---

# technical-doc-creator

skills/mhattingpete/claude-skills-marketplace/technical-doc-creator
technical-doc-creator
Installation
$ npx skills add https://github.com/mhattingpete/claude-skills-marketplace --skill technical-doc-creator
SKILL.md
Technical Documentation Creator

Create comprehensive HTML technical documentation with code examples and API workflows.

When to Use
"Create API documentation for [endpoints]"
"Generate technical docs for [system]"
"Document API reference"
"Create developer documentation"
Components
Overview: purpose, key features, tech stack
Getting Started: installation, setup, quick start
API Reference: endpoints with request/response examples
Code Examples: syntax-highlighted code blocks
Architecture: system diagram (SVG)
Workflows: step-by-step processes
HTML Structure
<!DOCTYPE html>
<html>
<head>
  <title>[API/System] Documentation</title>
  <style>
    body { font-family: system-ui; max-width: 1000px; margin: 0 auto; }
    pre { background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 4px; overflow-x: auto; }
    .endpoint { background: #f7fafc; padding: 15px; margin: 10px 0; border-left: 4px solid #4299e1; }
    code { background: #e2e8f0; padding: 2px 6px; border-radius: 3px; }
  </style>
</head>
<body>
  <h1>[System] Documentation</h1>
  <!-- Overview, Getting Started, API Reference, Examples -->
</body>
</html>

API Endpoint Pattern
<div class="endpoint">
  <h3><span style="color: #48bb78;">GET</span> /api/users/{id}</h3>
  <p>Retrieve user by ID</p>

  <h4>Request</h4>
  <pre><code>curl -X GET https://api.example.com/users/123</code></pre>

  <h4>Response</h4>
  <pre><code>{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com"
}</code></pre>
</div>

Code Block Pattern
<pre><code>// Installation
npm install package-name

// Usage
import { feature } from 'package-name';
const result = feature.doSomething();</code></pre>

Workflow
Extract API endpoints, methods, parameters
Create overview and getting started sections
Document each endpoint with examples
Add code snippets for common operations
Include architecture diagram if relevant
Write to [system]-docs.html

Use semantic colors for HTTP methods: GET (green), POST (blue), DELETE (red).

Weekly Installs
91
Repository
mhattingpete/cl…ketplace
GitHub Stars
563
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass