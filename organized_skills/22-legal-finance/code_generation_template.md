---
rating: ⭐⭐⭐
title: code-generation-template
url: https://skills.sh/aj-geddes/useful-ai-prompts/code-generation-template
---

# code-generation-template

skills/aj-geddes/useful-ai-prompts/code-generation-template
code-generation-template
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill code-generation-template
SKILL.md
Code Generation & Templates
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Comprehensive guide to code generation techniques including template engines, AST manipulation, code scaffolding, and automated boilerplate generation for increased productivity and consistency.

When to Use
Scaffolding new projects or components
Generating repetitive boilerplate code
Creating CRUD operations automatically
Generating API clients from OpenAPI specs
Building code from templates
Creating database models from schemas
Generating TypeScript types from JSON Schema
Building custom CLI generators
Quick Start

Minimal working example:

// templates/component.hbs
import React from 'react';

export interface {{pascalCase name}}Props {
  {{#each props}}
  {{this.name}}{{#if this.optional}}?{{/if}}: {{this.type}};
  {{/each}}
}

export const {{pascalCase name}}: React.FC<{{pascalCase name}}Props> = ({
  {{#each props}}{{this.name}},{{/each}}
}) => {
  return (
    <div className="{{kebabCase name}}">
      {/* Component implementation */}
    </div>
  );
};

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Template Engines	Template Engines
AST-Based Code Generation	AST-Based Code Generation
Project Scaffolding	Project Scaffolding
OpenAPI Client Generation	OpenAPI Client Generation
Database Model Generation	Database Model Generation
GraphQL Code Generation	GraphQL Code Generation
Plop.js Generator	Plop.js Generator
Best Practices
✅ DO
Use templates for repetitive code patterns
Generate TypeScript types from schemas
Include tests in generated code
Follow project conventions in templates
Add comments to explain generated code
Version control your templates
Make templates configurable
Generate documentation alongside code
Validate inputs before generating
Use consistent naming conventions
Keep templates simple and maintainable
Provide CLI for easy generation
❌ DON'T
Over-generate (avoid unnecessary complexity)
Generate code that's hard to maintain
Forget to validate generated code
Hardcode values in templates
Generate code without documentation
Create generators for one-off use cases
Mix business logic in templates
Generate code without formatting
Skip error handling in generators
Create overly complex templates
Weekly Installs
326
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass