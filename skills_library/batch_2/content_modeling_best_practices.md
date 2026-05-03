---
title: content-modeling-best-practices
url: https://skills.sh/sanity-io/agent-toolkit/content-modeling-best-practices
---

# content-modeling-best-practices

skills/sanity-io/agent-toolkit/content-modeling-best-practices
content-modeling-best-practices
Installation
$ npx skills add https://github.com/sanity-io/agent-toolkit --skill content-modeling-best-practices
Summary

Structured content modeling guidance for schema design, reusability, and multi-channel delivery.

Covers core principles: treating content as data rather than pages, maintaining single sources of truth, designing for future channels, and optimizing for editor workflows
Includes decision frameworks for references versus embedded objects, separation of concerns, and content reuse patterns
Provides taxonomy and classification guidance for flat, hierarchical, and faceted approaches
Applies to Sanity and other headless CMSes, with Sanity-specific implementation notes included
SKILL.md
Content Modeling Best Practices

Principles for designing structured content that's flexible, reusable, and maintainable. These concepts apply to any headless CMS but include Sanity-specific implementation notes.

When to Apply

Reference these guidelines when:

Starting a new project and designing the content model
Evaluating whether content should be structured or free-form
Deciding between references and embedded content
Planning for multi-channel content delivery
Refactoring existing content structures
Core Principles
Content is data, not pages — Structure content for meaning, not presentation
Single source of truth — Avoid content duplication
Future-proof — Design for channels that don't exist yet
Editor-centric — Optimize for the people creating content
References

Start with the reference that matches the modeling decision in front of you, instead of loading every topic at once. See references/ for detailed guidance on specific topics:

references/separation-of-concerns.md — Separating content from presentation
references/reference-vs-embedding.md — When to use references vs embedded objects
references/content-reuse.md — Content reuse patterns and the reuse spectrum
references/taxonomy-classification.md — Flat, hierarchical, and faceted classification
Weekly Installs
1.7K
Repository
sanity-io/agent-toolkit
GitHub Stars
129
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass