---
title: rest-api-design
url: https://skills.sh/aj-geddes/useful-ai-prompts/rest-api-design
---

# rest-api-design

skills/aj-geddes/useful-ai-prompts/rest-api-design
rest-api-design
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill rest-api-design
Summary

RESTful API design guidance covering resource modeling, HTTP methods, status codes, versioning, and documentation.

Covers resource naming conventions, HTTP method usage, query parameters, response formats, and status code selection with clear do's and don'ts
Includes reference guides for OpenAPI documentation, request/response examples, API versioning, authentication, rate limiting, and a complete Express.js implementation example
Emphasizes consistency through plural resource names, appropriate status codes, pagination, filtering, and ISO 8601 date formatting
Provides best practices for security (HTTPS, authentication), backward compatibility, error messaging, and avoiding common pitfalls like verb-based endpoints and over-nested resources
SKILL.md
REST API Design
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Design REST APIs that are intuitive, consistent, and follow industry best practices for resource-oriented architecture.

When to Use
Designing new RESTful APIs
Creating endpoint structures
Defining request/response formats
Implementing API versioning
Documenting API specifications
Refactoring existing APIs
Quick Start

Minimal working example:

✅ Good Resource Names (Nouns, Plural)
GET    /api/users
GET    /api/users/123
GET    /api/users/123/orders
POST   /api/products
DELETE /api/products/456

❌ Bad Resource Names (Verbs, Inconsistent)
GET    /api/getUsers
POST   /api/createProduct
GET    /api/user/123  (inconsistent singular/plural)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Resource Naming	Resource Naming, HTTP Methods & Operations
Request Examples	Request Examples
Query Parameters	Query Parameters
Response Formats	Response Formats
HTTP Status Codes	HTTP Status Codes, API Versioning, Authentication & Security, Rate Limiting Headers
OpenAPI Documentation	OpenAPI Documentation
Complete Example: Express.js	const express = require("express");
Best Practices
✅ DO
Use nouns for resources, not verbs
Use plural names for collections
Be consistent with naming conventions
Return appropriate HTTP status codes
Include pagination for collections
Provide filtering and sorting options
Version your API
Document thoroughly with OpenAPI
Use HTTPS
Implement rate limiting
Provide clear error messages
Use ISO 8601 for dates
❌ DON'T
Use verbs in endpoint names
Return 200 for errors
Expose internal IDs unnecessarily
Over-nest resources (max 2 levels)
Use inconsistent naming
Forget authentication
Return sensitive data
Break backward compatibility without versioning
Weekly Installs
898
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass