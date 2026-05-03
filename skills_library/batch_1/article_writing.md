---
title: article-writing
url: https://skills.sh/affaan-m/everything-claude-code/article-writing
---

# article-writing

skills/affaan-m/everything-claude-code/article-writing
article-writing
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill article-writing
Summary

Craft distinctive long-form content that matches a specific voice or brand style, not generic AI output.

Captures and applies existing voice patterns from articles, newsletters, or style guides to maintain consistency across blog posts, guides, tutorials, and launch announcements
Enforces concrete-first writing: leads with examples, screenshots, code, or data before explanation, avoiding generic openings and filler transitions
Bans hype language and unsourced claims; requires factual verification against provided sources and rejects invented metrics or biographical details
Includes structured workflows for technical guides, essays, and newsletters with section-by-section quality checks to ensure every line earns its place
SKILL.md
Article Writing

Write long-form content that sounds like an actual person with a point of view, not an LLM smoothing itself into paste.

When to Activate
drafting blog posts, essays, launch posts, guides, tutorials, or newsletter issues
turning notes, transcripts, or research into polished articles
matching an existing founder, operator, or brand voice from examples
tightening structure, pacing, and evidence in already-written long-form copy
Core Rules
Lead with the concrete thing: artifact, example, output, anecdote, number, screenshot, or code.
Explain after the example, not before.
Keep sentences tight unless the source voice is intentionally expansive.
Use proof instead of adjectives.
Never invent facts, credibility, or customer evidence.
Voice Handling

If the user wants a specific voice, run brand-voice first and reuse its VOICE PROFILE. Do not duplicate a second style-analysis pass here unless the user explicitly asks for one.

If no voice references are given, default to a sharp operator voice: concrete, unsentimental, useful.

Banned Patterns

Delete and rewrite any of these:

"In today's rapidly evolving landscape"
"game-changer", "cutting-edge", "revolutionary"
"here's why this matters" as a standalone bridge
fake vulnerability arcs
a closing question added only to juice engagement
biography padding that does not move the argument
generic AI throat-clearing that delays the point
Writing Process
Clarify the audience and purpose.
Build a hard outline with one job per section.
Start sections with proof, artifact, conflict, or example.
Expand only where the next sentence earns space.
Cut anything that sounds templated, overexplained, or self-congratulatory.
Structure Guidance
Technical Guides
open with what the reader gets
use code, commands, screenshots, or concrete output in major sections
end with actionable takeaways, not a soft recap
Essays / Opinion
start with tension, contradiction, or a specific observation
keep one argument thread per section
make opinions answer to evidence
Newsletters
keep the first screen doing real work
do not front-load diary filler
use section labels only when they improve scanability
Quality Gate

Before delivering:

factual claims are backed by provided sources
generic AI transitions are gone
the voice matches the supplied examples or the agreed VOICE PROFILE
every section adds something new
formatting matches the intended medium
Weekly Installs
3.4K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass