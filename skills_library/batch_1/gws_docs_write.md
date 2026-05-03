---
title: gws-docs-write
url: https://skills.sh/googleworkspace/cli/gws-docs-write
---

# gws-docs-write

skills/googleworkspace/cli/gws-docs-write
gws-docs-write
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-docs-write
Summary

Append plain text to the end of a Google Docs document.

Requires a document ID and text string; inserts content at the end of the document body
Write operation that should be confirmed with the user before execution
For rich text formatting, use the raw batchUpdate API instead
SKILL.md
docs +write

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Append text to a document

Usage
gws docs +write --document <ID> --text <TEXT>

Flags
Flag	Required	Default	Description
--document	✓	—	Document ID
--text	✓	—	Text to append (plain text)
Examples
gws docs +write --document DOC_ID --text 'Hello, world!'

Tips
Text is inserted at the end of the document body.
For rich formatting, use the raw batchUpdate API instead.

[!CAUTION] This is a write command — confirm with the user before executing.

See Also
gws-shared — Global flags and auth
gws-docs — All read and write google docs commands
Weekly Installs
19.6K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass