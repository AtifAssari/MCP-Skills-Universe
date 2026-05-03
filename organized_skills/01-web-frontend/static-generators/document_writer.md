---
rating: ⭐⭐⭐
title: document-writer
url: https://skills.sh/onmax/nuxt-skills/document-writer
---

# document-writer

skills/onmax/nuxt-skills/document-writer
document-writer
Installation
$ npx skills add https://github.com/onmax/nuxt-skills --skill document-writer
Summary

Style guide and content patterns for Nuxt documentation and blog posts.

Enforces active voice, present tense, and grammatically correct prose without sacrificing clarity for brevity
Provides writing patterns (subject-first, imperative, contextual) and modal verb guidance (can/should/must) for consistent documentation voice
Includes MDC component patterns for callouts (note, tip, warning, important) and CTAs, with references to nuxt-content and nuxt-ui skills for syntax and props
Offers structured checklist covering voice, tense, paragraph length, code block labeling, and callout type appropriateness
SKILL.md
Documentation Writer for Nuxt Ecosystem

Writing guidance for blog posts and documentation following patterns from official Nuxt websites.

When to Use
Writing blog posts for Nuxt ecosystem projects
Creating or editing documentation pages
Ensuring consistent writing style across content
Writing Standard

Override: When writing documentation, maintain proper grammar and complete sentences. The "sacrifice grammar for brevity" rule does NOT apply here.

Documentation must be:

Grammatically correct
Clear and unambiguous
Properly punctuated
Complete sentences (not fragments)

Brevity is still valued, but never at the cost of clarity or correctness.

Related Skills

For component and syntax details, use these skills:

Skill	Use For
nuxt-content	MDC syntax, prose components, code highlighting
nuxt-ui	Component props, theming, UI patterns
Available References
Reference	Purpose
references/writing-style.md	Voice, tone, sentence structure
references/content-patterns.md	Blog frontmatter, structure, component patterns
Loading Files

Consider loading these reference files based on your task:

 references/writing-style.md - if writing prose, improving voice/tone, or structuring sentences
 references/content-patterns.md - if creating blog posts, setting up frontmatter, or using MDC components

DO NOT load all files at once. Load only what's relevant to your current task.

Quick Reference
Writing Patterns
Pattern	Example
Subject-first	"The useFetch composable handles data fetching."
Imperative	"Add the following to nuxt.config.ts."
Contextual	"When using authentication, configure..."
Modal Verbs
Verb	Meaning
can	Optional
should	Recommended
must	Required
Component Patterns (WHEN to use)
Need	Component
Info aside	::note
Suggestion	::tip
Caution	::warning
Required	::important
CTA	:u-button{to="..." label="..."}
Multi-source code	::code-group

For component props: see nuxt-ui skill

Headings
H1 (#): No backticks — they don't render properly
H2-H4: Backticks work fine
Workflow
Load relevant reference file (writing-style.md for prose, content-patterns.md for structure)
Draft content using active voice and present tense
Apply the checklist below to verify quality — if any item fails, revise and re-check
Verify callout types match intent (note/tip/warning/important)
Example
# Getting Started with Authentication

Nuxt Better Auth provides a simple way to add authentication to your application.
Configure the module in your `nuxt.config.ts` to get started.

::note
Authentication requires a database connection. See the [database setup](/docs/database) guide for details.
::

## Installation

Add the module to your project:

~~~bash [Terminal]
pnpm add @onmax/nuxt-better-auth
~~~

The module auto-imports the `useUserSession` composable. Access the current user session from any component.

Checklist
 Active voice (85%+)
 Present tense
 2-4 sentences per paragraph
 Explanation before code
 File path labels on code blocks
 Appropriate callout types
 No backticks in H1 headings
Weekly Installs
1.3K
Repository
onmax/nuxt-skills
GitHub Stars
649
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass