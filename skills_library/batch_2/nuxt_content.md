---
title: nuxt-content
url: https://skills.sh/onmax/nuxt-skills/nuxt-content
---

# nuxt-content

skills/onmax/nuxt-skills/nuxt-content
nuxt-content
Installation
$ npx skills add https://github.com/onmax/nuxt-skills --skill nuxt-content
Summary

Typed content collections and SQL-backed queries for Nuxt apps with markdown, MDC, and remote sources.

Supports local markdown files, remote GitHub repositories, and external APIs as content sources via defineCollection and defineCollectionSource
Query content with a fluent SQL-like API (queryCollection) for filtering, navigation, and search across typed collections
Render markdown with Vue component support (MDC syntax) using ContentRenderer and customizable prose components
Integrates with NuxtStudio for live editing, preview mode, and multi-language content patterns
Database-agnostic configuration supporting SQLite, PostgreSQL, D1, and LibSQL with markdown plugin and renderer customization
SKILL.md
Nuxt Content v3

Progressive guidance for content-driven Nuxt apps with typed collections and SQL-backed queries.

When to Use

Working with:

Content collections (content.config.ts, defineCollection)
Remote sources (GitHub repos, external APIs via defineCollectionSource)
Content queries (queryCollection, navigation, search)
MDC rendering (<ContentRenderer>, prose components)
Database configuration (SQLite, PostgreSQL, D1, LibSQL)
Content hooks (content:file:beforeParse, content:file:afterParse)
i18n multi-language content
NuxtStudio or preview mode
LLMs integration (nuxt-llms)

For writing documentation: use document-writer skill For Nuxt basics: use nuxt skill For NuxtHub deployment: use nuxthub skill (NuxtHub v1 compatible)

Available Guidance

Read specific files based on current work:

references/collections.md - defineCollection, schemas, sources, content.config.ts
references/querying.md - queryCollection, navigation, search, surroundings
references/rendering.md - ContentRenderer, MDC syntax, prose components, Shiki
references/config.md - Database setup, markdown plugins, renderer options
references/studio.md - NuxtStudio integration, preview mode, live editing
Loading Files

Consider loading these reference files based on your task:

 references/collections.md - if setting up collections, schemas, or content.config.ts
 references/querying.md - if using queryCollection, navigation, or search
 references/rendering.md - if rendering markdown/MDC or working with ContentRenderer
 references/config.md - if configuring database, markdown plugins, or renderer options
 references/studio.md - if integrating NuxtStudio or preview mode

DO NOT load all files at once. Load only what's relevant to your current task.

Key Concepts
Concept	Purpose
Collections	Typed content groups with schemas
Page vs Data	page = routes + body, data = structured data only
Remote sources	source.repository for GitHub, defineCollectionSource for APIs
queryCollection	SQL-like fluent API for content
MDC	Vue components inside markdown
ContentRenderer	Renders parsed markdown body
Quick Start
// content.config.ts
import { defineCollection, defineContentConfig, z } from '@nuxt/content'

export default defineContentConfig({
  collections: {
    blog: defineCollection({
      type: 'page',
      source: 'blog/**',
      schema: z.object({
        title: z.string(),
        date: z.date(),
      }),
    }),
  },
})

<!-- pages/blog/[...slug].vue -->
<script setup lang="ts">
const { data: page } = await useAsyncData(
  () => queryCollection('blog').path(useRoute().path).first()
)
</script>

<template>
  <ContentRenderer v-if="page" :value="page" />
</template>


Verify setup: Run npx nuxi typecheck to confirm collection types resolve. If queryCollection returns empty, check that content files exist in the path matching your source glob.

Directory Structure
project/
├── content/                    # Content files
│   ├── blog/                   # Maps to 'blog' collection
│   └── .navigation.yml         # Navigation metadata
├── components/content/         # MDC components
└── content.config.ts           # Collection definitions

Official Documentation
Nuxt Content: https://content.nuxt.com
MDC syntax: https://content.nuxt.com/docs/files/markdown#mdc-syntax
Collections: https://content.nuxt.com/docs/collections/collections
Token Efficiency

Main skill: ~300 tokens. Each sub-file: ~800-1200 tokens. Only load files relevant to current task.

Weekly Installs
1.4K
Repository
onmax/nuxt-skills
GitHub Stars
649
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn