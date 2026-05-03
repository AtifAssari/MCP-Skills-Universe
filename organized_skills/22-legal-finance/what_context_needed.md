---
rating: ⭐⭐⭐
title: what-context-needed
url: https://skills.sh/github/awesome-copilot/what-context-needed
---

# what-context-needed

skills/github/awesome-copilot/what-context-needed
what-context-needed
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill what-context-needed
Summary

Ask an AI assistant what files it needs before answering your question.

Prompts the assistant to identify required and optional files for context before attempting to answer
Structures output into four categories: must-see files, helpful files, already-seen files, and remaining uncertainties
Helps developers avoid incomplete answers by ensuring the assistant has examined relevant code upfront
Reduces back-and-forth by clarifying dependencies and gaps in context before the actual question is answered
SKILL.md
What Context Do You Need?

Before answering my question, tell me what files you need to see.

My Question

{{question}}

Instructions
Based on my question, list the files you would need to examine
Explain why each file is relevant
Note any files you've already seen in this conversation
Identify what you're uncertain about
Output Format
## Files I Need

### Must See (required for accurate answer)
- `path/to/file.ts` — [why needed]

### Should See (helpful for complete answer)
- `path/to/file.ts` — [why helpful]

### Already Have
- `path/to/file.ts` — [from earlier in conversation]

### Uncertainties
- [What I'm not sure about without seeing the code]


After I provide these files, I'll ask my question again.

Weekly Installs
8.4K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass