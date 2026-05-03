---
rating: ⭐⭐⭐
title: skill-authoring
url: https://skills.sh/microsoft/github-copilot-for-azure/skill-authoring
---

# skill-authoring

skills/microsoft/github-copilot-for-azure/skill-authoring
skill-authoring
Installation
$ npx skills add https://github.com/microsoft/github-copilot-for-azure --skill skill-authoring
Summary

Guidelines and validation for writing Agent Skills compliant with agentskills.io specification.

Covers skill structure (SKILL.md, references/, scripts/), frontmatter constraints (name format, description limits), and token budgets (SKILL.md <5000 tokens, references <1000 each)
Enforces metadata best practices: use WHEN: trigger phrases in descriptions, avoid DO NOT USE FOR: keywords, keep descriptions under 60 words
Implements progressive disclosure with just-in-time reference loading: only explicitly linked files load on activation, not on startup
Includes validation tools (npm scripts) for checking broken links, token limits, and orphaned references before submission
SKILL.md
Skill Authoring Guide

This skill provides guidance for writing Agent Skills that comply with the agentskills.io specification.

When to Use
Creating a new skill for this repository
Reviewing a skill PR for compliance
Checking if an existing skill follows best practices
Understanding token budgets and progressive disclosure
Constraints
name: 1-64 chars, lowercase + hyphens, match directory
description: 1-1024 chars, ≤60 words, explain WHAT and WHEN
Use WHEN: with quoted trigger phrases (preferred over USE FOR:)
Avoid DO NOT USE FOR: unless the skill has trigger overlap with a broader skill (see frontmatter guidelines)
Use inline double-quoted strings (not >- folded scalars)
SKILL.md: <500 tokens (soft), <5000 (hard)
references/*.md: <1000 tokens each
Structure
SKILL.md (required) - Instructions
references/ (optional) - Detailed docs
scripts/ (optional) - Executable code

Frontmatter: name (lowercase-hyphens), description (WHAT + WHEN)

Progressive Disclosure

Metadata (~100 tokens) loads at startup. SKILL.md (<5000 tokens) loads on activation. References load only when explicitly linked (not on activation). Keep SKILL.md lean.

Reference Loading

References are JIT (just-in-time) loaded:

Only files explicitly linked via [text](references/file.md) load
Link to files, not folders - [Recipes](references/recipes/README.md) not [Recipes](references/recipes/)
Each file loads in full (not sections)
No caching between requests - write self-contained files
Use recipes/services patterns for multi-option skills

See REFERENCE-LOADING.md for details.

Validation
# Run from the scripts directory
cd scripts
npm run references              # Validate all skill links
npm run tokens -- check         # Check token limits

Integrity Checks

When reviewing or authoring skills, verify:

No broken links - All referenced files exist
No orphaned references - All reference files are linked
Token budgets - References under 1000 tokens (split if exceeded)
No duplicates - Consolidate repeated content
No out-of-place guidance - Service-specific content belongs in service-specific references

See Validation for detailed procedures.

Reference Documentation
Guidelines - Detailed writing guidelines
Token Budgets - Limits and splitting guidance
Reference Loading - How references load
Checklist - Pre-submission checklist
Validation - Link and reference validation
agentskills.io/specification - Official spec
Weekly Installs
1.1K
Repository
microsoft/githu…or-azure
GitHub Stars
202
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass