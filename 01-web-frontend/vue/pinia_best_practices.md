---
rating: ⭐⭐
title: pinia-best-practices
url: https://skills.sh/hyf0/vue-skills/pinia-best-practices
---

# pinia-best-practices

skills/hyf0/vue-skills/pinia-best-practices
pinia-best-practices
Installation
$ npx skills add https://github.com/hyf0/vue-skills --skill pinia-best-practices
Summary

TypeScript configuration and type safety patterns for Pinia stores in Vue 3.

Addresses storeToRefs type inference issues, particularly nested ref type loss in Vue 3.5+
Resolves circular type references and any type errors in getters that use this
Provides setup store patterns and best practices for type-safe store configuration
Covers common debugging scenarios when working with Pinia in TypeScript projects
SKILL.md
Pinia Best Practices

TypeScript configuration and common pitfalls for Pinia stores in Vue 3 applications.

When to Apply
Working with Pinia stores in TypeScript projects
Debugging storeToRefs type issues
Fixing getter circular type references
Setting up type-safe store patterns
Capability Rules

Rules that enable AI to solve problems it cannot solve without the skill.

Rule	Impact	Description
storeToRefs-type-loss	HIGH	Fix incorrect nested ref types with Vue 3.5+
Efficiency Rules

Rules that help AI solve problems more effectively and consistently.

Rule	Impact	Description
getters-circular-types	MEDIUM	Fix TypeScript any or circular errors in getters using this
Reference
Pinia Documentation
Pinia TypeScript Guide
Weekly Installs
350
Repository
hyf0/vue-skills
GitHub Stars
2.3K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass