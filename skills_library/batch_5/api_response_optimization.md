---
title: api-response-optimization
url: https://skills.sh/aj-geddes/useful-ai-prompts/api-response-optimization
---

# api-response-optimization

skills/aj-geddes/useful-ai-prompts/api-response-optimization
api-response-optimization
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill api-response-optimization
SKILL.md
API Response Optimization
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Fast API responses improve overall application performance and user experience. Optimization focuses on payload size, caching, and query efficiency.

When to Use
Slow API response times
High server CPU/memory usage
Large response payloads
Performance degradation
Scaling bottlenecks
Quick Start

Minimal working example:

// Inefficient response (unnecessary data)
GET /api/users/123
{
  "id": 123,
  "name": "John",
  "email": "john@example.com",
  "password_hash": "...", // ❌ Should never send
  "ssn": "123-45-6789", // ❌ Sensitive data
  "internal_id": "xyz",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-02T00:00:00Z",
  "meta_data": {...}, // ❌ Unused fields
  "address": {
    "street": "123 Main",
    "city": "City",
    "state": "ST",
    "zip": "12345",
    "geo": {...} // ❌ Not needed
  }
}

// Optimized response (only needed fields)
GET /api/users/123
{
  "id": 123,
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Response Payload Optimization	Response Payload Optimization
Caching Strategies	Caching Strategies
Compression & Performance	Compression & Performance
Optimization Checklist	Optimization Checklist
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
301
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