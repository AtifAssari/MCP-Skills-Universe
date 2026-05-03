---
title: markstream-migration
url: https://skills.sh/simon-he95/markstream-vue/markstream-migration
---

# markstream-migration

skills/simon-he95/markstream-vue/markstream-migration
markstream-migration
Installation
$ npx skills add https://github.com/simon-he95/markstream-vue --skill markstream-migration
SKILL.md
Markstream Migration

Use this skill when a repo already renders Markdown and the task is to adopt Markstream safely.

Read references/adoption-checklist.md before changing code.

Workflow
Audit the repo's current renderer usage.
Search for markdown renderers, plugin chains, raw HTML handling, security props, and custom renderers.
List every call site that will be touched.
Classify the migration.
direct: simple string-in renderer swap.
renderer-custom: custom renderers but limited parser work.
plugin-heavy: remark, rehype, markdown-it, or other transform-heavy pipelines.
security-heavy: allow or deny lists, URL rewriting, sanitization, or raw HTML policies.
Swap the renderer first.
Introduce the correct Markstream package and CSS.
Preserve user-visible behavior before adding richer Markstream-only features.
Migrate custom renderers.
Convert tag-based renderers into node-type overrides with scoped setCustomComponents.
For trusted tag-like content, prefer customHtmlTags.
Review gaps honestly.
Do not claim 1:1 parity where none exists.
Call out parser, plugin, security, or HTML behavior that still needs manual review.
Treat streaming as a second pass unless clearly required now.
Move to nodes only when the app receives streaming or high-frequency updates.
Validate and summarize.
Run the smallest relevant tests or build.
Report direct mappings, TODOs, and remaining verification work.
Default Decisions
Renderer swap first, streaming optimization second.
Preserve safety over feature parity when HTML or security rules are involved.
Prefer explicit TODOs over vague claims.
Recommend against migration when the current stack depends heavily on transforms that Markstream does not mirror directly.
Useful Doc Targets
docs/guide/react-markdown-migration.md
docs/guide/react-markdown-migration-cookbook.md
docs/guide/installation.md
docs/guide/component-overrides.md
docs/guide/advanced.md
Weekly Installs
36
Repository
simon-he95/mark…ream-vue
GitHub Stars
2.3K
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass