---
title: obsidian-markdown
url: https://skills.sh/kepano/obsidian-skills/obsidian-markdown
---

# obsidian-markdown

skills/kepano/obsidian-skills/obsidian-markdown
obsidian-markdown
Installation
$ npx skills add https://github.com/kepano/obsidian-skills --skill obsidian-markdown
Summary

Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, and properties.

Covers Obsidian-specific syntax extensions: wikilinks ([[Note]]), embeds (![[Note]]), callouts (> [!type]), block IDs, and frontmatter properties
Supports internal vault linking with automatic rename tracking, plus embeds for notes, images, PDFs, and external media
Includes callout types (note, warning, tip, danger, etc.), inline and block comments, highlights, LaTeX math, and Mermaid diagrams
Assumes standard Markdown knowledge (headings, lists, tables, code blocks); focuses only on Obsidian extensions
SKILL.md
Obsidian Flavored Markdown Skill

Create and edit valid Obsidian Flavored Markdown. Obsidian extends CommonMark and GFM with wikilinks, embeds, callouts, properties, comments, and other syntax. This skill covers only Obsidian-specific extensions -- standard Markdown (headings, bold, italic, lists, quotes, code blocks, tables) is assumed knowledge.

Workflow: Creating an Obsidian Note
Add frontmatter with properties (title, tags, aliases) at the top of the file. See PROPERTIES.md for all property types.
Write content using standard Markdown for structure, plus Obsidian-specific syntax below.
Link related notes using wikilinks ([[Note]]) for internal vault connections, or standard Markdown links for external URLs.
Embed content from other notes, images, or PDFs using the ![[embed]] syntax. See EMBEDS.md for all embed types.
Add callouts for highlighted information using > [!type] syntax. See CALLOUTS.md for all callout types.
Verify the note renders correctly in Obsidian's reading view.

When choosing between wikilinks and Markdown links: use [[wikilinks]] for notes within the vault (Obsidian tracks renames automatically) and [text](url) for external URLs only.

Internal Links (Wikilinks)
[[Note Name]]                          Link to note
[[Note Name|Display Text]]             Custom display text
[[Note Name#Heading]]                  Link to heading
[[Note Name#^block-id]]                Link to block
[[#Heading in same note]]              Same-note heading link


Define a block ID by appending ^block-id to any paragraph:

This paragraph can be linked to. ^my-block-id


For lists and quotes, place the block ID on a separate line after the block:

> A quote block

^quote-id

Embeds

Prefix any wikilink with ! to embed its content inline:

![[Note Name]]                         Embed full note
![[Note Name#Heading]]                 Embed section
![[image.png]]                         Embed image
![[image.png|300]]                     Embed image with width
![[document.pdf#page=3]]               Embed PDF page


See EMBEDS.md for audio, video, search embeds, and external images.

Callouts
> [!note]
> Basic callout.

> [!warning] Custom Title
> Callout with a custom title.

> [!faq]- Collapsed by default
> Foldable callout (- collapsed, + expanded).


Common types: note, tip, warning, info, example, quote, bug, danger, success, failure, question, abstract, todo.

See CALLOUTS.md for the full list with aliases, nesting, and custom CSS callouts.

Properties (Frontmatter)
---
title: My Note
date: 2024-01-15
tags:
  - project
  - active
aliases:
  - Alternative Name
cssclasses:
  - custom-class
---


Default properties: tags (searchable labels), aliases (alternative note names for link suggestions), cssclasses (CSS classes for styling).

See PROPERTIES.md for all property types, tag syntax rules, and advanced usage.

Tags
#tag                    Inline tag
#nested/tag             Nested tag with hierarchy


Tags can contain letters, numbers (not first character), underscores, hyphens, and forward slashes. Tags can also be defined in frontmatter under the tags property.

Comments
This is visible %%but this is hidden%% text.

%%
This entire block is hidden in reading view.
%%

Obsidian-Specific Formatting
==Highlighted text==                   Highlight syntax

Math (LaTeX)
Inline: $e^{i\pi} + 1 = 0$

Block:
$$
\frac{a}{b} = c
$$

Diagrams (Mermaid)
```mermaid
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Do this]
    B -->|No| D[Do that]
```


To link Mermaid nodes to Obsidian notes, add class NodeName internal-link;.

Footnotes
Text with a footnote[^1].

[^1]: Footnote content.

Inline footnote.^[This is inline.]

Complete Example
---
title: Project Alpha
date: 2024-01-15
tags:
  - project
  - active
status: in-progress
---

# Project Alpha

This project aims to [[improve workflow]] using modern techniques.

> [!important] Key Deadline
> The first milestone is due on ==January 30th==.

## Tasks

- [x] Initial planning
- [ ] Development phase
  - [ ] Backend implementation
  - [ ] Frontend design

## Notes

The algorithm uses $O(n \log n)$ sorting. See [[Algorithm Notes#Sorting]] for details.

![[Architecture Diagram.png|600]]

Reviewed in [[Meeting Notes 2024-01-10#Decisions]].

References
Obsidian Flavored Markdown
Internal links
Embed files
Callouts
Properties
Weekly Installs
25.6K
Repository
kepano/obsidian-skills
GitHub Stars
28.1K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass