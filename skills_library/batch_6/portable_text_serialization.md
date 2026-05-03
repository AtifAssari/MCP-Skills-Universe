---
title: portable-text-serialization
url: https://skills.sh/sanity-io/agent-toolkit/portable-text-serialization
---

# portable-text-serialization

skills/sanity-io/agent-toolkit/portable-text-serialization
portable-text-serialization
Installation
$ npx skills add https://github.com/sanity-io/agent-toolkit --skill portable-text-serialization
SKILL.md
Portable Text Serialization

Render Portable Text content across frameworks using the @portabletext/* library family. Each library follows the same component-mapping pattern: you provide a components object that maps PT node types to framework-specific renderers.

Portable Text Structure (Quick Reference)

PT is an array of blocks. Each block has _type, optional style, children (spans), markDefs, listItem, and level.

Root array
├── block (_type: "block")
│   ├── style: "normal" | "h1" | "h2" | "blockquote" | ...
│   ├── children: [span, span, ...]
│   │   └── span: { _type: "span", text: "...", marks: ["strong", "<markDefKey>"] }
│   ├── markDefs: [{ _key, _type: "link", href: "..." }, ...]
│   ├── listItem: "bullet" | "number" (optional)
│   └── level: 1, 2, 3... (optional, for nested lists)
├── custom block (_type: "image" | "code" | any custom type)
└── ...more blocks


Marks come in two forms:

Decorators: string values in marks[] like "strong", "em", "underline", "code"
Annotations: keys in marks[] referencing entries in markDefs[] (e.g., links, internal references)
Component Mapping Pattern (All Frameworks)

Every @portabletext/* library accepts a components object with these keys:

Key	Renders	Props/Data
types	Custom block/inline types (image, code, CTA)	value (the block data)
marks	Decorators + annotations	children + value (mark data)
block	Block styles (h1, normal, blockquote)	children
list	List wrappers (ul, ol)	children
listItem	List items	children
hardBreak	Line breaks within a block	—
Framework-Specific Rules

Read the rule file matching your framework:

React / Next.js: rules/react.md — @portabletext/react or next-sanity
Svelte / SvelteKit: rules/svelte.md — @portabletext/svelte
Vue / Nuxt: rules/vue.md — @portabletext/vue
Astro: rules/astro.md — astro-portabletext
HTML (server-side): rules/html.md — @portabletext/to-html
Markdown: rules/markdown.md — @portabletext/markdown
Plain text extraction: rules/plain-text.md — @portabletext/toolkit
Additional Community Serializers

These are listed on portabletext.org but don't have dedicated rule files:

Target	Package
React Native	@portabletext/react-native-portabletext
React PDF	@portabletext/react-pdf-portabletext
Solid	solid-portabletext
Qwik	portabletext-qwik
Shopify Liquid	portable-text-to-liquid
PHP	sanity-php (SanityBlockContent class)
Python	portabletext-html
C# / .NET	dotnet-portable-text
Dart / Flutter	flutter_sanity_portable_text
Common Patterns (All Frameworks)
Custom Types Need Explicit Components

PT renderers only handle standard blocks by default. Custom types (image, code, callToAction, etc.) require explicit component mappings — they won't render otherwise.

Keep Components Object Stable

In React/Vue, define components outside the render function or memoize it. Recreating on every render causes unnecessary re-renders.

Handle Missing Components Gracefully

All libraries accept onMissingComponent to control behavior when encountering unknown types:

false — suppress warnings
Custom function — log or report
Querying PT with GROQ

Always expand references inside custom blocks:

body[]{
  ...,
  _type == "image" => {
    ...,
    asset->
  },
  markDefs[]{
    ...,
    _type == "internalLink" => {
      ...,
      "slug": @.reference->slug.current
    }
  }
}

Weekly Installs
266
Repository
sanity-io/agent-toolkit
GitHub Stars
129
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass