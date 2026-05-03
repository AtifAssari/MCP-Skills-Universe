---
rating: ⭐⭐
title: web-clipper
url: https://skills.sh/dandcg/claude-skills/web-clipper
---

# web-clipper

skills/dandcg/claude-skills/web-clipper
web-clipper
Installation
$ npx skills add https://github.com/dandcg/claude-skills --skill web-clipper
SKILL.md
Web Clipper

Save any web page as clean markdown with YAML frontmatter. Optionally search your clips or ingest them into repo-search for semantic search.

Prerequisites
Python 3 with venv
Setup
First-Time Setup
~/.claude/skills/web-clipper/setup.sh


This creates a .venv and installs dependencies (trafilatura, requests, python-slugify, pyyaml).

Usage
Clip a URL
~/.claude/skills/web-clipper/.venv/bin/python ~/.claude/skills/web-clipper/scripts/clip.py <url>


With tags:

~/.claude/skills/web-clipper/.venv/bin/python ~/.claude/skills/web-clipper/scripts/clip.py <url> --tags "python,web-dev"


JSON output:

~/.claude/skills/web-clipper/.venv/bin/python ~/.claude/skills/web-clipper/scripts/clip.py <url> -f json


Clips are saved to ~/web-clips/ as markdown files with YAML frontmatter (title, url, domain, author, date, tags).

List Clips
~/.claude/skills/web-clipper/.venv/bin/python ~/.claude/skills/web-clipper/scripts/list.py


Filter by domain, tag, or date:

~/.claude/skills/web-clipper/.venv/bin/python ~/.claude/skills/web-clipper/scripts/list.py --domain "example.com"
~/.claude/skills/web-clipper/.venv/bin/python ~/.claude/skills/web-clipper/scripts/list.py --tag "python"
~/.claude/skills/web-clipper/.venv/bin/python ~/.claude/skills/web-clipper/scripts/list.py --after 2026-01-01 --before 2026-02-01
~/.claude/skills/web-clipper/.venv/bin/python ~/.claude/skills/web-clipper/scripts/list.py -f json

Search Clips

Full-text search across all clips:

~/.claude/skills/web-clipper/.venv/bin/python ~/.claude/skills/web-clipper/scripts/search.py "search terms"
~/.claude/skills/web-clipper/.venv/bin/python ~/.claude/skills/web-clipper/scripts/search.py "search terms" -f json

Delete a Clip
~/.claude/skills/web-clipper/.venv/bin/python ~/.claude/skills/web-clipper/scripts/delete.py <filename>
~/.claude/skills/web-clipper/.venv/bin/python ~/.claude/skills/web-clipper/scripts/delete.py --url "https://example.com/article"

Ingest into Repo Search (semantic search)

Requires the repo-search skill. Pushes all clips into ChromaDB:

~/.claude/skills/web-clipper/.venv/bin/python ~/.claude/skills/web-clipper/scripts/ingest.py


After ingestion, clips are searchable via repo-search:

~/.claude/skills/repo-search/.venv/bin/python ~/.claude/skills/repo-search/query.py "query" --collection web-clips

Error Handling
Error	Cause	Fix
Could not extract article content	Page has no extractable article text (e.g., SPA, login wall)	JS-rendered pages may not be extractable
repo-search skill not found	repo-search not installed	Run ./install.sh repo-search
Limitations
Extracts article text only — does not preserve images, videos, or interactive elements
JavaScript-rendered SPAs may not be fully extractable
Login-walled content cannot be accessed
Weekly Installs
23
Repository
dandcg/claude-skills
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn