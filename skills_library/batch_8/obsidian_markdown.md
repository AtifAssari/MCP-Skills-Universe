---
title: obsidian-markdown
url: https://skills.sh/davila7/claude-code-templates/obsidian-markdown
---

# obsidian-markdown

skills/davila7/claude-code-templates/obsidian-markdown
obsidian-markdown
Originally fromkepano/obsidian-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill obsidian-markdown
SKILL.md
Obsidian Flavored Markdown Skill

This skill enables Claude Code to create and edit valid Obsidian Flavored Markdown, including all Obsidian-specific syntax extensions.

Overview

Obsidian uses a combination of Markdown flavors:

CommonMark
GitHub Flavored Markdown
LaTeX for math
Obsidian-specific extensions (wikilinks, callouts, embeds, etc.)
Basic Formatting
Paragraphs and Line Breaks
This is a paragraph.

This is another paragraph (blank line between creates separate paragraphs).

For a line break within a paragraph, add two spaces at the end  
or use Shift+Enter.

Headings
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

Text Formatting
Style	Syntax	Example	Output
Bold	**text** or __text__	**Bold**	Bold
Italic	*text* or _text_	*Italic*	Italic
Bold + Italic	***text***	***Both***	Both
Strikethrough	~~text~~	~~Striked~~	Striked
Highlight	==text==	==Highlighted==	==Highlighted==
Inline code	`code`	`code`	code
Escaping Formatting

Use backslash to escape special characters:

\*This won't be italic\*
\#This won't be a heading
1\. This won't be a list item


Common characters to escape: \*, \_, \#, \`, \|, \~

Internal Links (Wikilinks)
Basic Links
[[Note Name]]
[[Note Name.md]]
[[Note Name|Display Text]]

Link to Headings
[[Note Name#Heading]]
[[Note Name#Heading|Custom Text]]
[[#Heading in same note]]
[[##Search all headings in vault]]

Link to Blocks
[[Note Name#^block-id]]
[[Note Name#^block-id|Custom Text]]


Define a block ID by adding ^block-id at the end of a paragraph:

This is a paragraph that can be linked to. ^my-block-id


For lists and quotes, add the block ID on a separate line:

> This is a quote
> With multiple lines

^quote-id

Search Links
[[##heading]]     Search for headings containing "heading"
[[^^block]]       Search for blocks containing "block"

Markdown-Style Links
[Display Text](Note%20Name.md)
[Display Text](Note%20Name.md#Heading)
[Display Text](https://example.com)
[Note](obsidian://open?vault=VaultName&file=Note.md)


Note: Spaces must be URL-encoded as %20 in Markdown links.

Embeds
Embed Notes
![[Note Name]]
![[Note Name#Heading]]
![[Note Name#^block-id]]

Embed Images
![[image.png]]
![[image.png|640x480]]    Width x Height
![[image.png|300]]        Width only (maintains aspect ratio)

External Images
![Alt text](https://example.com/image.png)
![Alt text|300](https://example.com/image.png)

Embed Audio
![[audio.mp3]]
![[audio.ogg]]

Embed PDF
![[document.pdf]]
![[document.pdf#page=3]]
![[document.pdf#height=400]]

Embed Lists
![[Note#^list-id]]


Where the list has been defined with a block ID:

- Item 1
- Item 2
- Item 3

^list-id

Embed Search Results
```query
tag:#project status:done
```

Callouts
Basic Callout
> [!note]
> This is a note callout.

> [!info] Custom Title
> This callout has a custom title.

> [!tip] Title Only

Foldable Callouts
> [!faq]- Collapsed by default
> This content is hidden until expanded.

> [!faq]+ Expanded by default
> This content is visible but can be collapsed.

Nested Callouts
> [!question] Outer callout
> > [!note] Inner callout
> > Nested content

Supported Callout Types
Type	Aliases	Description
note	-	Blue, pencil icon
abstract	summary, tldr	Teal, clipboard icon
info	-	Blue, info icon
todo	-	Blue, checkbox icon
tip	hint, important	Cyan, flame icon
success	check, done	Green, checkmark icon
question	help, faq	Yellow, question mark
warning	caution, attention	Orange, warning icon
failure	fail, missing	Red, X icon
danger	error	Red, zap icon
bug	-	Red, bug icon
example	-	Purple, list icon
quote	cite	Gray, quote icon
Custom Callouts (CSS)
.callout[data-callout="custom-type"] {
  --callout-color: 255, 0, 0;
  --callout-icon: lucide-alert-circle;
}

Lists
Unordered Lists
- Item 1
- Item 2
  - Nested item
  - Another nested
- Item 3

* Also works with asterisks
+ Or plus signs

Ordered Lists
1. First item
2. Second item
   1. Nested numbered
   2. Another nested
3. Third item

1) Alternative syntax
2) With parentheses

Task Lists
- [ ] Incomplete task
- [x] Completed task
- [ ] Task with sub-tasks
  - [ ] Subtask 1
  - [x] Subtask 2

Quotes
> This is a blockquote.
> It can span multiple lines.
>
> And include multiple paragraphs.
>
> > Nested quotes work too.

Code
Inline Code
Use `backticks` for inline code.
Use double backticks for ``code with a ` backtick inside``.

Code Blocks
```
Plain code block
```

```javascript
// Syntax highlighted code block
function hello() {
  console.log("Hello, world!");
}
```

```python
# Python example
def greet(name):
    print(f"Hello, {name}!")
```

Nesting Code Blocks

Use more backticks or tildes for the outer block:

````markdown
Here's how to create a code block:
```js
console.log("Hello")
```
````

Tables
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

Alignment
| Left     | Center   | Right    |
|:---------|:--------:|---------:|
| Left     | Center   | Right    |

Using Pipes in Tables

Escape pipes with backslash:

| Column 1 | Column 2 |
|----------|----------|
| [[Link\|Display]] | ![[Image\|100]] |

Math (LaTeX)
Inline Math
This is inline math: $e^{i\pi} + 1 = 0$

Block Math
$$
\begin{vmatrix}
a & b \\
c & d
\end{vmatrix} = ad - bc
$$

Common Math Syntax
$x^2$              Superscript
$x_i$              Subscript
$\frac{a}{b}$      Fraction
$\sqrt{x}$         Square root
$\sum_{i=1}^{n}$   Summation
$\int_a^b$         Integral
$\alpha, \beta$    Greek letters

Diagrams (Mermaid)
```mermaid
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Do this]
    B -->|No| D[Do that]
    C --> E[End]
    D --> E
```

Sequence Diagrams
```mermaid
sequenceDiagram
    Alice->>Bob: Hello Bob
    Bob-->>Alice: Hi Alice
```

Linking in Diagrams
```mermaid
graph TD
    A[Biology]
    B[Chemistry]
    A --> B
    class A,B internal-link;
```

Footnotes
This sentence has a footnote[^1].

[^1]: This is the footnote content.

You can also use named footnotes[^note].

[^note]: Named footnotes still appear as numbers.

Inline footnotes are also supported.^[This is an inline footnote.]

Comments
This is visible %%but this is hidden%% text.

%%
This entire block is hidden.
It won't appear in reading view.
%%

Horizontal Rules
---
***
___
- - -
* * *

Properties (Frontmatter)

Properties use YAML frontmatter at the start of a note:

---
title: My Note Title
date: 2024-01-15
tags:
  - project
  - important
aliases:
  - My Note
  - Alternative Name
cssclasses:
  - custom-class
status: in-progress
rating: 4.5
completed: false
due: 2024-02-01T14:30:00
---

Property Types
Type	Example
Text	title: My Title
Number	rating: 4.5
Checkbox	completed: true
Date	date: 2024-01-15
Date & Time	due: 2024-01-15T14:30:00
List	tags: [one, two] or YAML list
Links	related: "[[Other Note]]"
Default Properties
tags - Note tags
aliases - Alternative names for the note
cssclasses - CSS classes applied to the note
Tags
#tag
#nested/tag
#tag-with-dashes
#tag_with_underscores

In frontmatter:
---
tags:
  - tag1
  - nested/tag2
---


Tags can contain:

Letters (any language)
Numbers (not as first character)
Underscores _
Hyphens -
Forward slashes / (for nesting)
HTML Content

Obsidian supports HTML within Markdown:

<div class="custom-container">
  <span style="color: red;">Colored text</span>
</div>

<details>
  <summary>Click to expand</summary>
  Hidden content here.
</details>

<kbd>Ctrl</kbd> + <kbd>C</kbd>

Complete Example
---
title: Project Alpha
date: 2024-01-15
tags:
  - project
  - active
status: in-progress
priority: high
---

# Project Alpha

## Overview

This project aims to [[improve workflow]] using modern techniques.

> [!important] Key Deadline
> The first milestone is due on ==January 30th==.

## Tasks

- [x] Initial planning
- [x] Resource allocation
- [ ] Development phase
  - [ ] Backend implementation
  - [ ] Frontend design
- [ ] Testing
- [ ] Deployment

## Technical Notes

The main algorithm uses the formula $O(n \log n)$ for sorting.

```python
def process_data(items):
    return sorted(items, key=lambda x: x.priority)
```

## Architecture

```mermaid
graph LR
    A[Input] --> B[Process]
    B --> C[Output]
    B --> D[Cache]
```

## Related Documents

- ![[Meeting Notes 2024-01-10#Decisions]]
- [[Budget Allocation|Budget]]
- [[Team Members]]

## References

For more details, see the official documentation[^1].

[^1]: https://example.com/docs

%%
Internal notes:
- Review with team on Friday
- Consider alternative approaches
%%

References
Basic formatting syntax
Advanced formatting syntax
Obsidian Flavored Markdown
Internal links
Embed files
Callouts
Properties
Weekly Installs
400
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass