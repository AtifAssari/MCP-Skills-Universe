---
title: markdown-formatter
url: https://skills.sh/beshkenadze/claude-skills-marketplace/markdown-formatter
---

# markdown-formatter

skills/beshkenadze/claude-skills-marketplace/markdown-formatter
markdown-formatter
Installation
$ npx skills add https://github.com/beshkenadze/claude-skills-marketplace --skill markdown-formatter
SKILL.md
Markdown Formatter
Overview

Transforms unstructured content into clean, well-organized Markdown with proper headings, lists, code blocks, and formatting.

Instructions

When formatting content to Markdown:

Analyze the content to identify structure (headings, lists, code, etc.)
Apply hierarchy using appropriate heading levels (H1 for title, H2 for sections)
Format code with proper language-specific syntax highlighting
Create lists for related items (bullet for unordered, numbers for sequential)
Add tables for structured data comparisons
Formatting Rules
Headings
H1 (#) - Document title only
H2 (##) - Major sections
H3 (###) - Subsections
H4+ - Avoid unless necessary
Code Blocks
Inline code: Single backticks for short references
Fenced blocks: Triple backticks with language identifier
Lists
Bullet lists: Related but unordered items
Numbered lists: Sequential steps or ranked items
Nested lists: Maximum 2 levels deep
Examples
Example: Format API Documentation

Input: "Document the getUser function that takes userId string and returns User object with name email and createdAt fields"

Output:

## `getUser(userId)`

Retrieves a user by their unique identifier.

### Parameters

| Name | Type | Description |
|------|------|-------------|
| `userId` | `string` | The unique user identifier |

### Returns

`User` object with the following properties:

- `name` - User's display name
- `email` - User's email address
- `createdAt` - Account creation timestamp

Guidelines
Do
Keep line length under 100 characters
Use blank lines to separate sections
Prefer ATX-style headings (#) over Setext
Use reference-style links for repeated URLs
Include language identifier in fenced code blocks
Don't
Use more than 3 heading levels unless necessary
Mix heading styles in same document
Create deeply nested lists (max 2 levels)
Use HTML tags when Markdown suffices
Weekly Installs
8
Repository
beshkenadze/cla…ketplace
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass