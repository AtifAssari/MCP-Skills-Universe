---
title: portable-text-conversion
url: https://skills.sh/sanity-io/agent-toolkit/portable-text-conversion
---

# portable-text-conversion

skills/sanity-io/agent-toolkit/portable-text-conversion
portable-text-conversion
Installation
$ npx skills add https://github.com/sanity-io/agent-toolkit --skill portable-text-conversion
SKILL.md
Portable Text Conversion

Convert external content (HTML, Markdown) into Portable Text for Sanity. Three main approaches:

markdownToPortableText — Convert Markdown directly using @portabletext/markdown (recommended for Markdown)
htmlToBlocks — Parse HTML into PT blocks using @portabletext/block-tools (for HTML migration)
Manual construction — Build PT blocks directly from any source (APIs, databases, etc.)
Portable Text Specification

Understand the target format before converting. PT is an array of blocks:

[
  {
    "_type": "block",
    "_key": "abc123",
    "style": "normal",
    "children": [
      {"_type": "span", "_key": "def456", "text": "Hello ", "marks": []},
      {"_type": "span", "_key": "ghi789", "text": "world", "marks": ["strong"]}
    ],
    "markDefs": []
  },
  {
    "_type": "block",
    "_key": "jkl012",
    "style": "h2",
    "children": [
      {"_type": "span", "_key": "mno345", "text": "A heading", "marks": []}
    ],
    "markDefs": []
  },
  {
    "_type": "image",
    "_key": "pqr678",
    "asset": {"_type": "reference", "_ref": "image-abc-200x200-png"}
  }
]


Key rules:

Every block and span needs _key (unique within the array)
_type: "block" is for text blocks; custom types use their own _type
markDefs holds annotation data; marks on spans reference markDefs[*]._key or are decorator strings
Lists use listItem ("bullet" | "number") and level (1, 2, 3...) on regular blocks
Conversion Rules

Read the rule file matching your source format:

Markdown → Portable Text: rules/markdown-to-pt.md — @portabletext/markdown with markdownToPortableText (recommended)
HTML → Portable Text: rules/html-to-pt.md — @portabletext/block-tools with htmlToBlocks
Manual PT Construction: rules/manual-construction.md — build blocks programmatically from any source

Note: @sanity/block-tools is the legacy package name. Always use @portabletext/block-tools for new projects. The API is the same.

Weekly Installs
266
Repository
sanity-io/agent-toolkit
GitHub Stars
129
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn