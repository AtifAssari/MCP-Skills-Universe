---
rating: ⭐⭐⭐
title: issue-reporting
url: https://skills.sh/manojbajaj95/claude-gtm-plugin/issue-reporting
---

# issue-reporting

skills/manojbajaj95/claude-gtm-plugin/issue-reporting
issue-reporting
Installation
$ npx skills add https://github.com/manojbajaj95/claude-gtm-plugin --skill issue-reporting
SKILL.md
Issue Reporting

Help users report problems with GTM skills clearly and completely so maintainers can fix them fast.

When This Skill Activates
User says a skill gave wrong or harmful advice
User says a skill isn't activating when it should
User says their brand context wasn't applied
User says output format is wrong or unexpected
User wants to report a bug or file an issue
User says "something is broken" about a skill
Step 1 — Identify the Problem

Ask the user what went wrong. Determine:

Which skill — get the exact skill name (e.g. seo-and-aeo-strategy, copywriting-core)
What they asked — the exact prompt or task they gave Claude
What happened — the actual output or behavior
What they expected — what should have happened instead

If the user is vague ("it gave bad advice"), ask specifically what was incorrect and why.

Step 2 — Gather Context

Check the user's project for context that helps diagnose the issue:

Context files

Check if these exist and note their presence:

strategy/brand.md — brand positioning, messaging, audience
about/me.md — personal voice, writing style
CLAUDE.md — AI instructions

Missing context files are the most common cause of "wrong advice" bugs. If strategy/brand.md or about/me.md are missing, tell the user:

"The skill may have given generic advice because your brand context files are missing. Run /bootstrap to set them up. If the skill still gives wrong advice after that, then it's a real bug worth reporting."

Plugin version

Check .claude-plugin/plugin.json for the current version number.

Installation method

Ask how they installed the plugin (Claude Code, Cowork, Skills CLI, git clone, submodule).

Step 3 — Classify the Issue

Categorize into one of these types:

Type	Description	Common cause
Wrong advice	Skill produced incorrect or harmful recommendations	Outdated framework, wrong domain assumptions
Not activating	Skill should have triggered but didn't	Description mismatch, trigger phrase gap
Wrong activation	Skill triggered when it shouldn't have	Overly broad description
Missing context	Brand/voice not applied to output	Context files missing or not read
Bad format	Output structure is wrong	Skill template issue
Crash/error	Skill fails mid-execution	Syntax error in skill, bad reference path
Step 4 — Generate the Issue

Compose a GitHub issue using the bug report template. Format it so the user can copy-paste or click through:

Direct link (pre-fills the template):

https://github.com/manojbajaj95/claude-gtm-plugin/issues/new?template=bug_report.yml


Formatted issue body (if they prefer to paste manually):

**Skill**: [skill-name]
**Type**: [category from Step 3]
**Plugin Version**: [version]
**Installation**: [method]

### What I asked
[exact prompt]

### What happened
[actual output — include relevant excerpt]

### What I expected
[expected behavior]

### Context files present
- [ ] strategy/brand.md
- [ ] about/me.md
- [ ] CLAUDE.md

### Steps to reproduce
1. [step-by-step if applicable]

### Impact
[Critical / High / Medium / Low]

Step 5 — Offer Next Steps

After generating the issue:

Give them the direct link to file it: https://github.com/manojbajaj95/claude-gtm-plugin/issues/new?template=bug_report.yml
If the problem is missing context files, suggest running /bootstrap first
If it's clearly a skill bug, encourage them to file it — it helps improve the plugin for everyone
Thank them for reporting — contributors who file clear issues are invaluable
Important
Never dismiss user frustration — if they think the advice is wrong, take it seriously
Don't try to fix the skill yourself — this skill is for reporting, not patching
Be specific in the issue — vague reports like "it didn't work" are hard to act on
Include the actual output when possible — maintainers need to see what went wrong
Weekly Installs
38
Repository
manojbajaj95/cl…m-plugin
GitHub Stars
43
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail