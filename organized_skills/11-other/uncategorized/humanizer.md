---
rating: ⭐⭐
title: humanizer
url: https://skills.sh/hjewkes/agent-skills/humanizer
---

# humanizer

skills/hjewkes/agent-skills/humanizer
humanizer
Installation
$ npx skills add https://github.com/hjewkes/agent-skills --skill humanizer
SKILL.md
Humanizer

Clean AI-generated text by normalizing characters, flagging overused phrases, and following context-appropriate writing guidelines.

Workflow
Identify context — determine what you're writing: README, email, Slack message, commit message, or general documentation
Load the guide — read the appropriate reference file (see table below)
Write following the guide — apply tone, structure, and length guidelines as you draft
Run the script — pipe final text through humanize for mechanical cleanup and phrase flagging
Review flags — rewrite any flagged phrases naturally; don't just delete them, replace with plain language
Context Guides
Context	Reference	Key principle
README	references/readme-guide.md	Direct and factual, show the command first
Email	references/email-guide.md	State the ask in the first sentence
Slack	references/slack-guide.md	Terse — 1-2 sentences max
Commit	references/commit-guide.md	Imperative mood, explain why not what
General	Apply common sense from all guides	Prefer clarity over formality
CLI Reference
Command	Description
echo "text" | humanize	Clean text via stdin
humanize file.md	Clean text from file
humanize --report file.md	Verbose output with replacement counts
humanize --help	Show usage

Exit codes: 0 = clean, 1 = error, 2 = phrase flags found (text still cleaned)

What the Script Fixes Automatically
Em dashes → space-hyphen-space
Smart quotes → straight quotes
Unicode ellipsis → three periods
Non-breaking/invisible spaces → regular spaces
Invisible Unicode watermark characters → removed
Bullet characters → ASCII hyphens
What Gets Flagged (Not Auto-Fixed)

The script flags phrases that need human judgment to rewrite:

Red-flag words: delve, tapestry, seamless, robust, comprehensive, etc.
Hedging filler: "it's important to note", "it's worth noting"
Cliche openers/closers: "I hope this finds you well", "feel free to reach out"
Overused transitions: furthermore, moreover, additionally

Full pattern list: references/phrases.txt

Weekly Installs
9
Repository
hjewkes/agent-skills
GitHub Stars
3
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass