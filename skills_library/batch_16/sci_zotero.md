---
title: sci-zotero
url: https://skills.sh/shzhao27208/aut_sci_write/sci-zotero
---

# sci-zotero

skills/shzhao27208/aut_sci_write/sci-zotero
sci-zotero
Installation
$ npx skills add https://github.com/shzhao27208/aut_sci_write --skill sci-zotero
SKILL.md
Sci-Zotero — Zotero Library Integration

Interact with your Zotero library to sync references, add citations by DOI/ISBN/PMID, and manage PDFs.

Triggers
"sync zotero library"
"add citation [identifier]"
"check pdfs in zotero"
"fetch pdfs for zotero items"
"search zotero for [query]"
Usage

This skill wraps the zotero.py standalone CLI tool located in ../../scripts/zotero.py.

Environment Variables
ZOTERO_API_KEY: Your Zotero API key.
ZOTERO_USER_ID: Your Zotero User ID (for personal libraries).
ZOTERO_GROUP_ID: Your Zotero Group ID (for group libraries).
Commands
items: List top-level items.
add-doi [DOI]: Add an item by DOI.
add-isbn [ISBN]: Add an item by ISBN.
fetch-pdfs: Automatically find and attach open-access PDFs.
© License & Copyright

Aut_Sci_Write — Autonomous Scientific Writer

Author: Shuo Zhao
License: MIT License
Copyright: © 2026 Shuo Zhao. All rights reserved.
Original Work: This is an original work created by the author. No reproduction, redistribution, or commercial use without explicit permission. Permission is hereby granted, free of charge, to any person obtaining a copy of this software... (See the LICENSE file in the root directory for the full MIT terms.)
This skill is part of the Aut_Sci_Write suite. For full license terms, see the LICENSE file in the project root.
Weekly Installs
32
Repository
shzhao27208/aut…ci_write
GitHub Stars
37
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn