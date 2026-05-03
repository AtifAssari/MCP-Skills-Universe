---
rating: ⭐⭐
title: google-docstring-assistant
url: https://skills.sh/dmitriiweb/extract-emails/google-docstring-assistant
---

# google-docstring-assistant

skills/dmitriiweb/extract-emails/google-docstring-assistant
google-docstring-assistant
Installation
$ npx skills add https://github.com/dmitriiweb/extract-emails --skill google-docstring-assistant
SKILL.md
Google Docstring Assistant
Quick start
Write docstrings using the Google Python Style Guide structure (Args, Returns, Raises, Examples, Attributes, etc.).
Keep sections as headers followed by indented blocks; break sections by resuming unindented text.
When types are annotated in code, omit them in docstrings unless clarity is improved.
Use Examples blocks with literal blocks (::) for commands or code snippets.
Document module-level variables consistently (all in Attributes or inline), and list TODOs in a Todo section.
See references/google_docstring_rules.md for full guidance and examples.
Workflow

Choose sections

Functions: include Args, Returns, and Raises as needed.
Modules/classes: use Attributes and Todo when relevant; keep formatting consistent.

Write clearly

One docstring per object; keep it concise and informative.
Use indentation under each section header; separate sections by returning to unindented text.
Prefer Google-style wording; avoid duplicating annotated types unless helpful.

Examples and scripts

Use Examples: with indented literal blocks for shell commands or code snippets.
Include multi-line descriptions when needed; keep formatting readable.
Reference
references/google_docstring_rules.md: full style description and examples.
Weekly Installs
9
Repository
dmitriiweb/extr…t-emails
GitHub Stars
108
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass