---
title: summarize
url: https://skills.sh/mitsuhiko/agent-stuff/summarize
---

# summarize

skills/mitsuhiko/agent-stuff/summarize
summarize
Installation
$ npx skills add https://github.com/mitsuhiko/agent-stuff --skill summarize
SKILL.md

Turn “things” (URLs, PDFs, Word docs, PowerPoints, HTML pages, text files, etc.) into Markdown so they can be inspected/quoted/processed like normal text.

markitdown can fetch URLs by itself; this skill mainly wraps it to make saving + summarizing convenient. For PDF inputs, use the markitdown[pdf] extra (or the wrapper below, which now does this automatically).

When to use

Use this skill when you need to:

pull down a web page as a document-like Markdown representation
convert binary docs (PDF/DOCX/PPTX) into Markdown for analysis
quickly produce a short summary of a long document before deeper work
Quick usage
Convert a URL or file to Markdown

Run from this skill folder (the agent should cd here first):

uvx --from 'markitdown[pdf]' markitdown <url-or-path>


To write Markdown to a temp file (prints the path) use the wrapper:

node to-markdown.mjs <url-or-path> --tmp


Tip: when summarizing, the script will always write the full converted Markdown to a temp .md file and will always print a final "Hint" line with the path (so you can open/inspect the full content).

Write Markdown to a specific file:

uvx --from 'markitdown[pdf]' markitdown <url-or-path> > /tmp/doc.md

Convert + summarize with haiku-4-5 (pass context!)

Summaries are only useful when you provide what you want extracted and the audience/purpose.

node to-markdown.mjs <url-or-path> --summary --prompt "Summarize focusing on X, for audience Y. Extract Z."


Or:

node to-markdown.mjs <url-or-path> --summary --prompt "Focus on security implications and action items."


This will:

convert to Markdown via uvx --from 'markitdown[pdf]' markitdown
write the full Markdown to a temp .md file and print its path as a "Hint" line
run pi --model claude-haiku-4-5 (no-tools, no-session) to summarize using your extra prompt
Weekly Installs
120
Repository
mitsuhiko/agent-stuff
GitHub Stars
2.2K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn