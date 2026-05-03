---
title: google-image-search
url: https://skills.sh/glebis/claude-skills/google-image-search
---

# google-image-search

skills/glebis/claude-skills/google-image-search
google-image-search
Installation
$ npx skills add https://github.com/glebis/claude-skills --skill google-image-search
SKILL.md
Google Image Search Skill

Search for images using Google Custom Search API with intelligent scoring and LLM-based selection.

When to Use
Finding images to illustrate technical articles or research
Adding visuals to presentations
Enriching Obsidian notes with relevant images
Batch image search for multiple topics
Generating image search configs from plain text lists
Requirements
Google Custom Search API key and Search Engine ID
OpenRouter API key (for LLM selection)
llm CLI installed at /opt/homebrew/bin/llm

Store credentials in .env:

Google-Custom-Search-JSON-API-KEY=your_key
Google-Custom-Search-CX=your_cx
OPENROUTER_API_KEY=your_openrouter_key

Modes of Operation
1. Simple Query

Search for a single term:

python3 ~/.claude/skills/google-image-search/scripts/google_image_search.py \
  --query "neural interface wearable device" \
  --output-dir ./images \
  --num-results 5

2. Batch Processing

Process multiple queries from JSON config:

python3 ~/.claude/skills/google-image-search/scripts/google_image_search.py \
  --config image_queries.json \
  --output-dir ./images \
  --llm-select

3. Generate Config from Terms

Create JSON config from a list of terms using LLM:

python3 ~/.claude/skills/google-image-search/scripts/google_image_search.py \
  --generate-config \
  --terms "AlterEgo wearable" "sEMG electrodes" "BCI headset" \
  --output my_queries.json

4. Enrich Obsidian Note

Extract visual terms from note, find images, and insert below headings:

python3 ~/.claude/skills/google-image-search/scripts/google_image_search.py \
  --enrich-note ~/Brains/brain/Research/neural-interfaces.md


This mode:

Detects Obsidian vault and attachments folder
Uses LLM to extract visual-worthy terms from note
Searches for images for each term
Downloads best images to attachments folder
Inserts image embeds below relevant headings
Creates backup before modifying note
Key Options
Option	Description
--query TEXT	Simple single query
--config FILE	JSON config for batch
--generate-config	Generate config from --terms
--enrich-note FILE	Enrich Obsidian note
--output-dir DIR	Where to save images
--urls-only	Return URLs only, no download
--llm-select	Use LLM to pick best image (default: on)
--no-llm-select	Disable LLM selection
--num-results N	Results per query (default: 5)
--dry-run	Show what would be done
JSON Config Format

Each entry supports:

{
  "id": "unique-id",
  "heading": "Display Heading",
  "description": "Context for what image to find",
  "query": "Google search query",
  "numResults": 5,
  "selectionCriteria": "What makes a good image",
  "requiredTerms": ["must", "have"],
  "optionalTerms": ["bonus", "terms"],
  "excludeTerms": ["stock", "clipart"],
  "preferredHosts": ["official-site.com"],
  "selectionCount": 2
}


See references/api_config_reference.md for full documentation.

Scoring System

Images are scored based on:

Required terms: -80 if missing, +30 if all present
Optional terms: +5 per match
Exclude terms: -50 per match
Preferred hosts: +25 if trusted, -5 if unknown
MIME type: +5 for PNG/JPEG, -10 for GIF
Resolution: +10 for high res, -10 for low res
File size: -5 if very small
LLM Selection

After scoring, LLM picks the best image from top candidates based on:

Title and URL metadata
Scoring reasons
Selection criteria

The LLM evaluates authenticity, clarity, and relevance for technical audiences.

Obsidian Integration

When in an Obsidian vault:

Auto-detects vault root via .obsidian folder
Uses configured attachments folder (default: Attachments)
Generates Obsidian-style embeds: ![[image.png|alt text]]
Creates backup before modifying notes
Script Files
File	Purpose
google_image_search.py	Main entry point
api.py	Google Custom Search API
config.py	Credentials and config handling
download.py	Image download with magic bytes
evaluate.py	Keyword-based scoring
llm_select.py	LLM selection and term extraction
obsidian.py	Vault detection and enrichment
output.py	Markdown output generation
Weekly Installs
333
Repository
glebis/claude-skills
GitHub Stars
152
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn