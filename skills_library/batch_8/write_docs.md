---
title: write-docs
url: https://skills.sh/tldraw/tldraw/write-docs
---

# write-docs

skills/tldraw/tldraw/write-docs
write-docs
Installation
$ npx skills add https://github.com/tldraw/tldraw --skill write-docs
SKILL.md
Write documentation

This skill covers how to write and update tldraw SDK documentation.

Location

All documentation lives in apps/docs/content/. The main categories are:

Directory	Purpose
docs/	SDK documentation articles
releases/	Release notes (see write-release-notes skill)
examples/	Example documentation
getting-started/	Quickstart and setup guides
Process
1. Understand the scope

Before writing:

Identify the target audience (new users, experienced developers, API reference)
Check existing docs that cover related topics
Look at relevant examples in apps/examples/
Read the API types and comments in the source code
2. Create the file

Create a new .mdx file in the appropriate directory with frontmatter:

---
title: Feature name
status: published
author: steveruizok
date: 3/22/2023
order: 1
keywords:
  - keyword1
  - keyword2
---

3. Write the content

Follow the structure:

Overview — 1-2 paragraphs on what and why
Basic usage — The simplest working example
Details — Deeper explanation with more examples
Edge cases — Advanced patterns, gotchas
Links — Related docs and examples
4. Use MDX components
API links

Use [ClassName](?) or [ClassName#methodName](?) for API references:

The [Editor](?) class has many methods. Use [Editor#createShapes](?) to create shapes.

Code highlighting

Use <FocusLines> to highlight specific lines:

<FocusLines lines={[2,6,10]}>

\`\`\`tsx
import { Tldraw } from 'tldraw'
import { useSyncDemo } from '@tldraw/sync'
\`\`\`

</FocusLines>

Images
<Image
	src="/images/api/events.png"
	alt="A diagram showing an event being sent to the editor."
	title="Caption text here."
/>

Tables for API documentation

Use tables for listing methods, options, or properties:

| Method                   | Description                                    |
| ------------------------ | ---------------------------------------------- |
| [Editor#screenToPage](?) | Convert a point in screen space to page space. |
| [Editor#pageToScreen](?) | Convert a point in page space to screen space. |

| Value     | Description                                          |
| --------- | ---------------------------------------------------- |
| `default` | Sets the initial zoom to 100%.                       |
| `fit-x`   | The x axis will completely fill the viewport bounds. |

5. Verify

Check that:

Code examples actually work
API links resolve correctly
Images have alt text
Headings use sentence case
No AI tells (see style guide)
References
Style guide: See ../shared/docs-guide.md for voice, tone, and formatting conventions.
Weekly Installs
315
Repository
tldraw/tldraw
GitHub Stars
46.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass