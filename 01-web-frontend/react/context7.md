---
title: context7
url: https://skills.sh/trancong12102/ccc/context7
---

# context7

skills/trancong12102/ccc/context7
context7
Installation
$ npx skills add https://github.com/trancong12102/ccc --skill context7
SKILL.md
Context7 Documentation Lookup

Retrieve current documentation and code examples for any programming library directly from the source.

Usage

Use the Python script at scripts/context7.py.

Get Documentation
# Text format (default)
python scripts/context7.py docs \
  --library-id /facebook/react --query "useEffect cleanup function"

# Specific version
python scripts/context7.py docs \
  --library-id /vercel/next.js/v15.1.8 --query "app router middleware"

Search Libraries

Use search only when the library ID is unknown:

python scripts/context7.py search \
  --library react --query "hooks"

Query Tips
Use detailed, natural language queries for better results
Good: "How to implement authentication with middleware"
Bad: "auth"
Common Library IDs
Library	ID
React	/facebook/react
Next.js	/vercel/next.js
TailwindCSS	/tailwindlabs/tailwindcss
Expo	/expo/expo
ORPC	middleapi/orpc
Rules
Query docs directly when you know the library ID
Use search only if unsure about the library ID
Use specific version IDs for consistent results (e.g., /vercel/next.js/v15.1.8)
Use --format json for structured output
Weekly Installs
10
Repository
trancong12102/ccc
GitHub Stars
3
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn