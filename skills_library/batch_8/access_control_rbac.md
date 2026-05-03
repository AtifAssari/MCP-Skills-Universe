---
title: access-control-rbac
url: https://skills.sh/aj-geddes/useful-ai-prompts/access-control-rbac
---

# access-control-rbac

skills/aj-geddes/useful-ai-prompts/access-control-rbac
access-control-rbac
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill access-control-rbac
SKILL.md
Access Control & RBAC
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive Role-Based Access Control systems with permissions management, attribute-based policies, and least privilege principles.

When to Use
Multi-tenant applications
Enterprise access management
API authorization
Admin dashboards
Data access controls
Compliance requirements
Quick Start

Minimal working example:

// rbac-system.js
class Permission {
  constructor(resource, action) {
    this.resource = resource;
    this.action = action;
  }

  toString() {
    return `${this.resource}:${this.action}`;
  }
}

class Role {
  constructor(name, description) {
    this.name = name;
    this.description = description;
    this.permissions = new Set();
    this.inherits = new Set();
  }

  addPermission(permission) {
    this.permissions.add(permission.toString());
  }

  removePermission(permission) {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Node.js RBAC System	Node.js RBAC System
Python ABAC (Attribute-Based Access Control)	Python ABAC (Attribute-Based Access Control)
Java Spring Security RBAC	Java Spring Security RBAC
Best Practices
✅ DO
Implement least privilege
Use role hierarchies
Audit access changes
Regular access reviews
Separate duties
Document permissions
Test access controls
Use attribute-based policies
❌ DON'T
Grant excessive permissions
Share accounts
Skip access reviews
Hardcode permissions
Ignore audit logs
Use role explosion
Weekly Installs
401
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