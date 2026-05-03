---
rating: ⭐⭐
title: markstream-custom-components
url: https://skills.sh/simon-he95/markstream-vue/markstream-custom-components
---

# markstream-custom-components

skills/simon-he95/markstream-vue/markstream-custom-components
markstream-custom-components
Installation
$ npx skills add https://github.com/simon-he95/markstream-vue --skill markstream-custom-components
SKILL.md
Markstream Custom Components

Use this skill when the task is to change how Markstream renders specific nodes or custom tags.

Read references/patterns.md before choosing an override strategy.

Workflow
Classify the request.
built-in override: replace an existing renderer such as image, link, code_block, mermaid, d2, or inline_code.
custom tag: support trusted HTML-like tags such as thinking.
parser-level: requires token transforms or AST reshaping. Only then should you leave this skill and use low-level parser hooks.
Prefer scoped mappings.
Use setCustomComponents(customId, mapping) instead of global mappings whenever practical.
Pass the same customId or custom-id to the renderer instance.
Start with the smallest safe override.
Leaf-like nodes (image, link, inline_code, mermaid) are easier than container nodes (heading, paragraph, list_item).
If the request only changes Mermaid, use mermaid, not code_block.
Preserve nested Markdown when needed.
For trusted custom tags with inner Markdown, render node.content with a nested renderer.
Pass the same custom-tag allowlist to nested renderers.
Keep props and cleanup intact.
Preserve node, loading, indexKey, customId, and isDark.
For mermaid and infographic overrides, preserve estimatedPreviewHeightPx so async preview shells keep stable height during remounts.
Remove temporary scoped mappings with removeCustomComponents(customId) when the scope is no longer needed.
Validate with the smallest useful check.
Prefer a local demo, targeted test, or docs build.
Call out whether the implementation is safe for repeated and nested custom tags.
Default Decisions
Scoped overrides first, global overrides only when the whole app truly needs them.
Leaf-node overrides before container-node overrides.
customHtmlTags plus scoped custom components before parser hooks.
Nested renderers for tag bodies that contain Markdown.
Useful Doc Targets
docs/guide/component-overrides.md
docs/guide/custom-components.md
docs/guide/components.md
docs/guide/advanced.md
Weekly Installs
47
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