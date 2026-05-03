---
title: writing-style
url: https://skills.sh/lout33/writing-style-skill/writing-style
---

# writing-style

skills/lout33/writing-style-skill/writing-style
writing-style
Installation
$ npx skills add https://github.com/lout33/writing-style-skill --skill writing-style
SKILL.md
Writing Style

Transform text to match a personal voice. Designed for converting AI-generated responses into authentic personal communication.

Available Styles
my-style: Your personal writing style — see references/my-style.md
Process
Load the style profile from references/my-style.md
Infer language from input text
Infer context from text patterns:
Short, no greeting → Casual/messaging
Has greeting, multiple paragraphs → Email/professional
Technical terms, specifics → Technical writing
Apply all style rules from the profile
Output ONLY the transformed text
Usage

Natural language triggers:

"rewrite in my style"
"make this sound like me"
"my style"
"make it mine"
"transform this"
"rewrite as me"
"sound like me"
"use my voice"

Or use the command: /my-style [text]

Output Rules
Return ONLY the rewritten text
No preamble ("Here's the rewritten version:")
No postamble ("Let me know if you need changes")
No explanation of changes made
Ready to copy-paste directly
Customization

Edit references/my-style.md with YOUR patterns:

Your tone (casual? formal? mix?)
Your sentence structure
Your greetings and closings
Your language preferences
Things you NEVER say
Before/after examples

The more specific your examples, the better the output.

Context Detection

The skill automatically detects context from the input:

Pattern	Detected Context	Style Applied
Short text, no greeting	Casual/messaging	Very short, fragments ok
"Dear/Hi [Name]", paragraphs	Email/professional	Complete sentences, direct
Technical terms, code refs	Technical	Dense, specific
Weekly Installs
8
Repository
lout33/writing-…le-skill
GitHub Stars
3
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn