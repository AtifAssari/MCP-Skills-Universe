---
title: rsvp-reading
url: https://skills.sh/richfrem/agent-plugins-skills/rsvp-reading
---

# rsvp-reading

skills/richfrem/agent-plugins-skills/rsvp-reading
rsvp-reading
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill rsvp-reading
SKILL.md
Dependencies

This skill requires Python 3.8+ and standard library only. No external packages needed.

To install this skill's dependencies:

pip-compile ./requirements.in
pip install -r ./requirements.txt


See ./requirements.txt for the dependency lockfile (currently empty — standard library only).

RSVP Reading Skill

Rapid Serial Visual Presentation (RSVP) is a speed reading method popularized by tools like Spritz. Words are flashed one at a time in a fixed position, while one letter per word is highlighted (typically in red) as an eye anchor — the Optimal Recognition Point (ORP). This eliminates horizontal eye movement, the primary bottleneck of traditional reading, enabling speeds of 200-600+ WPM with solid comprehension.

This skill converts any document into an RSVP token stream: each word paired with its ORP index and a calibrated display delay based on your target WPM.

Full architecture: references/architecture.md Acceptance criteria: references/acceptance-criteria.md Fallback tree: references/fallback-tree.md Token stream schema: references/token-stream-schema.md

Trigger Conditions

Invoke this skill when the user:

Says "speed read [file]", "RSVP [file]", or "read [file] at [N] WPM"
Uploads or references a document and asks to "read it fast"
Requests a token stream or reading session from a document
Discovery Phase

Before executing, collect:

Input file path - What file should be parsed? (.txt, .md, .pdf, .docx)
WPM - Reading speed in words-per-minute. Default: 300. Range: 100-1000.
Output format - Where to save the token stream JSON? Default: ./rsvp_output.json

If any are missing, ask for them before proceeding.

Execution
Step 1: Parse the Document
python3 .agents/skills/rsvp-reading/scripts/parse_document.py \
  --input <file_path> \
  --output /tmp/rsvp_words.json

Step 2: Generate Token Stream
python3 .agents/skills/rsvp-reading/scripts/orp_engine.py \
  --input /tmp/rsvp_words.json \
  --wpm <wpm> \
  --output <output_path>

Step 3: Confirm Output

Report to the user:

Total word count
Estimated reading time at the chosen WPM
Output file path
Preview of first 5 tokens
Output Format

Each token in the stream follows the schema in references/token-stream-schema.md:

{"w": "Hello", "orp": 1, "delay_ms": 200, "is_sentence_end": false, "is_para_end": false}

Confirmation Gate

Before generating for files > 50,000 words, display:

This document contains ~{word_count} words.
At {wpm} WPM this will take ~{minutes} minutes to read.
Generating token stream (~{token_count} tokens) to {output_path}.
Proceed? [yes/no]

Next Actions

After successful generation, offer:

Open the reading session with the rsvp-comprehension-agent
Adjust WPM and regenerate
Parse a different document
Weekly Installs
20
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass