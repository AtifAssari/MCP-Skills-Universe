---
rating: ⭐⭐
title: remove-ai-style
url: https://skills.sh/zc277584121/marketing-skills/remove-ai-style
---

# remove-ai-style

skills/zc277584121/marketing-skills/remove-ai-style
remove-ai-style
Installation
$ npx skills add https://github.com/zc277584121/marketing-skills --skill remove-ai-style
SKILL.md
Remove AI Style

Review and adjust the writing style of an article to reduce obvious AI-generated patterns, making the text read more naturally and human-like.

When to Use

Use this skill when the user asks to:

Remove AI style from an article
Make AI-generated text sound more natural
Polish writing to reduce robotic or formulaic patterns
Intensity Levels

The user can specify how aggressively to remove AI patterns. If they don't specify, default to "heavy".

Level	Description
Moderate (中等)	Only fix the most obvious AI patterns. Preserve most of the original structure and phrasing. Light touch.
Heavy (尽力去除)	Actively rewrite AI-ish sentences, restructure overly formulaic paragraphs, and replace robotic transitions. This is the default.
Full (完全彻底)	Treat the entire text as a draft and rewrite it from scratch in a natural human voice, while preserving the original meaning and key information. The output should read as if a human wrote it from the start.
Instructions
Determine the language of the article (Chinese or English).
Determine the intensity level — check if the user specified moderate / heavy / full. Default to heavy.
Load the corresponding reference document:
Chinese articles: references/chinese.md
English articles: references/english.md
Run the quick-scan scripts provided in the reference document (if any) to locate symbol-level issues first. This gives you a fast overview of problem spots without reading line by line.
Review the article against the style guidelines in the reference document. The script results are just a starting point — you still need to read through the full text for patterns that scripts can't detect (e.g., overuse of metaphors, formulaic structure, robotic transitions).
Apply fixes according to the intensity level:
Moderate: only fix what the scripts flagged + the most glaring patterns.
Heavy: fix everything the guidelines call out, rewrite awkward sentences.
Full: rewrite the text from scratch preserving meaning.
Preserve the original meaning and tone — even at "full" intensity, the core message should remain intact.
Weekly Installs
484
Repository
zc277584121/mar…g-skills
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass