---
title: ez-lobsters
url: https://skills.sh/araa47/ez-news/ez-lobsters
---

# ez-lobsters

skills/araa47/ez-news/ez-lobsters
ez-lobsters
Installation
$ npx skills add https://github.com/araa47/ez-news --skill ez-lobsters
SKILL.md
ez-lobsters - Lobste.rs CLI

Simple typer CLI for browsing Lobste.rs. No authentication required.

Usage

Run uv run skills/ez-lobsters/scripts/lobsters.py <command>. All commands support --json for raw JSON output.

Browse Stories
uv run skills/ez-lobsters/scripts/lobsters.py hottest              # hot/trending (default 10)
uv run skills/ez-lobsters/scripts/lobsters.py hottest --limit 20    # more results
uv run skills/ez-lobsters/scripts/lobsters.py newest                # newest
uv run skills/ez-lobsters/scripts/lobsters.py tag rust              # by tag
uv run skills/ez-lobsters/scripts/lobsters.py tag security          # security stories

View Story Details and Comments
uv run skills/ez-lobsters/scripts/lobsters.py item abc123
uv run skills/ez-lobsters/scripts/lobsters.py comments abc123
uv run skills/ez-lobsters/scripts/lobsters.py comments abc123 --depth 3

Search
uv run skills/ez-lobsters/scripts/lobsters.py search "rust async"
uv run skills/ez-lobsters/scripts/lobsters.py search "nix" --limit 5

Common Workflows
User asks	Command
"What's trending on Lobsters?"	lobsters.py hottest
"Latest Lobsters posts"	lobsters.py newest
"Lobsters posts about Rust"	lobsters.py tag rust
"Search Lobsters for X"	lobsters.py search "X"
"Show comments on Lobsters story Y"	lobsters.py comments Y
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