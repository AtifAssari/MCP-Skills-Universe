---
rating: ⭐⭐⭐
title: xmind-generator
url: https://skills.sh/site/skills.volces.com/xmind-generator
---

# xmind-generator

skills/skills.volces.com/xmind-generator
xmind-generator
$ npx skills add https://skills.volces.com/skills/clawhub/geoion
SKILL.md
XMind Generator

Generate .xmind files from Markdown outlines or plain text using the XMind SDK.

Script

scripts/generate_xmind.js — main generator. Requires Node.js and the xmind npm package.

Installation

Install dependencies before first use:

cd <skill_dir>
npm install

Usage
# From Markdown outline file
node scripts/generate_xmind.js --input outline.md --output /path/to/output.xmind

# From inline text (use \n for newlines)
node scripts/generate_xmind.js --text "# Root\n- Branch 1\n  - Leaf\n- Branch 2" --output output.xmind

# From stdin
echo "..." | node scripts/generate_xmind.js --output output.xmind


Always run from the skill directory:

cd <skill_dir>


Default output location: the OpenClaw workspace directory.

Input Format

Both formats are supported:

Markdown outline:

# Root Topic
- Main Branch 1
  - Sub topic 1
  - Sub topic 2
- Main Branch 2
  - Sub topic 3
    - Leaf node


Plain text / free-form description: When user provides a description instead of an outline, first convert it to Markdown outline structure, then pass to the script.

Workflow
If user provides a Markdown outline → pass directly to script via --text or --input
If user provides a plain text description → convert to Markdown outline first, then generate
Output file goes to workspace directory unless user specifies otherwise
Confirm the output path to the user after generation
Weekly Installs
13
Source
skills.volces.c…b/geoion
First Seen
Today