---
title: ez-hn
url: https://skills.sh/araa47/ez-news/ez-hn
---

# ez-hn

skills/araa47/ez-news/ez-hn
ez-hn
Installation
$ npx skills add https://github.com/araa47/ez-news --skill ez-hn
SKILL.md
ez-hn - Hacker News CLI

Simple typer CLI for browsing Hacker News. No authentication required.

Usage

Run uv run skills/ez-hn/scripts/hn.py <command>. All commands support --json for raw JSON output.

Browse Stories
uv run skills/ez-hn/scripts/hn.py top              # top/trending (default 10)
uv run skills/ez-hn/scripts/hn.py top --limit 20    # more results
uv run skills/ez-hn/scripts/hn.py new               # newest
uv run skills/ez-hn/scripts/hn.py best              # highest rated
uv run skills/ez-hn/scripts/hn.py ask               # Ask HN
uv run skills/ez-hn/scripts/hn.py show              # Show HN
uv run skills/ez-hn/scripts/hn.py jobs              # job postings

View Item Details and Comments
uv run skills/ez-hn/scripts/hn.py item 12345678
uv run skills/ez-hn/scripts/hn.py comments 12345678
uv run skills/ez-hn/scripts/hn.py comments 12345678 --limit 10 --depth 2

User Profiles
uv run skills/ez-hn/scripts/hn.py user dang

Search
uv run skills/ez-hn/scripts/hn.py search "rust programming"
uv run skills/ez-hn/scripts/hn.py search "LLM" --type story --sort date --period week --limit 5

Who is Hiring
uv run skills/ez-hn/scripts/hn.py whoishiring
uv run skills/ez-hn/scripts/hn.py whoishiring --limit 20

Common Workflows
User asks	Command
"What's trending on HN?"	hn.py top
"Latest Ask HN posts"	hn.py ask
"Search HN for X"	hn.py search "X"
"Show comments on story Y"	hn.py comments Y
"Who is hiring?"	hn.py whoishiring
"Tell me about HN user Z"	hn.py user Z
Weekly Installs
9
Repository
araa47/ez-news
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn