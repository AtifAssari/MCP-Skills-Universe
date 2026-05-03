---
title: pavlo-markdown-editor
url: https://skills.sh/pavloglushko/ai-skills/pavlo-markdown-editor
---

# pavlo-markdown-editor

skills/pavloglushko/ai-skills/pavlo-markdown-editor
pavlo-markdown-editor
Installation
$ npx skills add https://github.com/pavloglushko/ai-skills --skill pavlo-markdown-editor
SKILL.md
Skill: Markdown Editor

Create, edit, or reformat any .md file on request, enforcing a 120-character line limit and meaning-boundary line wrapping throughout.

Line-Length & Wrapping Rules

These rules apply to all prose text produced or reformatted by this skill.

Hard Limit

No line may exceed 120 characters (including leading whitespace and punctuation).

Soft Wrapping — Break at Meaning Boundaries

Do not wrap at an arbitrary character count. Break lines at the nearest logical boundary that keeps the line ≤ 120 characters.

Preferred break points, in order of priority:

End of sentence — break after ., !, or ? followed by a space.
After a comma that separates two independent or semi-independent clauses (e.g., "if X is true, then Y follows" → break after the comma).
After a conjunction / transition word that starts a new clause: and, but, or, so, because, however, therefore, thus, then, when, while, although, etc.
After a colon or semicolon that introduces a list item or elaboration.
Between list items — each list item always starts on its own line.
Before a parenthetical — break just before ( if the phrase is long.

If none of the above boundaries exist within 120 characters, break at the last whitespace before the limit.

What NOT to Do
Do not split a word across lines.
Do not break inside a Markdown link [text](url), inline code `code`, or an emphasis span **bold** / _italic_.
Do not break inside a table cell; keep each cell on one line (tables are exempt from the 120-char limit if content cannot be shortened).
Do not add a hard break inside a fenced code block or YAML front matter.
Do not reflow headings (#, ##, etc.) — they stay on a single line even if > 120 chars.
Formatting Rules
Headings
Use ATX-style headings (#, ##, ###, …).
One blank line before and after every heading.
No trailing punctuation on headings.
Lists
Use - for unordered lists (not * or +).
Use 1. / 2. … for ordered lists.
Indent nested items with 2 spaces.
One blank line between list items that contain multiple sentences or sub-lists.
Emphasis
**bold** for important terms or key information.
_italic_ for titles, foreign words, or mild stress.
Do not combine bold and italic unless truly necessary.
Code
Inline code: single backticks `like this`.
Code blocks: triple backticks with a language tag (```python, ```yaml, ```json, etc.).
Tables
Align column separators (|) vertically when practical.
Include a header separator row (| --- | --- |).
Keep each row on one line.
Links & References
Prefer reference-style links [text][ref] for URLs that appear more than once.
Inline links [text](url) are fine for single-use URLs.
Blank Lines
Exactly one blank line between paragraphs.
Exactly one blank line before and after code blocks.
No trailing spaces at the end of lines.
File ends with exactly one newline.
Horizontal Rules
Never use horizontal rules (---, ***, or ___).
Use a heading to signal a new section instead.
Workflow
Read the existing file (if editing) to understand current structure and formatting.
Apply the changes requested by the user.
Reformat any prose that violates the line-length or wrapping rules above.
Do not change content that was not part of the requested edit — only reformat lines that were added or were already violating the rules.
Confirm the result to the user with a short summary of what changed.
Weekly Installs
11
Repository
pavloglushko/ai-skills
First Seen
Apr 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass