---
title: context_mastery
url: https://skills.sh/cityfish91159/maihouses/context_mastery
---

# context_mastery

skills/cityfish91159/maihouses/context_mastery
context_mastery
Installation
$ npx skills add https://github.com/cityfish91159/maihouses --skill context_mastery
SKILL.md
Context Mastery & Token Optimization Protocol
1. The "Grep-First" Rule (Token Saver)
Problem: read_file on a 2000-line file consumes ~500-1000 tokens instantly.
Solution: Always use grep or read_file_range first to inspect specific functions or imports.
Banned: cat or read_file on entire directories or massive files (e.g., package-lock.json, giant logs) unless absolutely necessary.
2. Incremental Summarization
Trigger: When the conversation exceeds ~20 turns or you feel the context window filling.
Action:
Summarize what has been achieved in the last 10 turns.
Write it to scratchpad.md or active_task.md.
Explicitly state "I am clearing internal context of validated steps" (if tool allows) or just rely on the scratchpad for future lookup.
3. Focused Context Loading
Don't: "Read all files in src/ to understand the project." (Too expensive).
Do:
Read CLAUDE.md / README.md.
Read directory listing ls -R.
Selectively read only the interfaces (types.ts) or entry points (index.ts) related to the current task.
4. Context Efficiency Checklist
 Did I use grep instead of reading the whole file?
 Did I check if I already have this info in MEMORY.md?
 Is my next prompt efficient? (Avoid repeating massive code blocks back to the user).
Weekly Installs
17
Repository
cityfish91159/maihouses
GitHub Stars
1
First Seen
Jan 25, 2026