---
title: brand-voice
url: https://skills.sh/affaan-m/everything-claude-code/brand-voice
---

# brand-voice

skills/affaan-m/everything-claude-code/brand-voice
brand-voice
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill brand-voice
SKILL.md
Brand Voice

Build a durable voice profile from real source material, then use that profile everywhere instead of re-deriving style from scratch or defaulting to generic AI copy.

When to Activate
the user wants content or outreach in a specific voice
writing for X, LinkedIn, email, launch posts, threads, or product updates
adapting a known author's tone across channels
the existing content lane needs a reusable style system instead of one-off mimicry
Source Priority

Use the strongest real source set available, in this order:

recent original X posts and threads
articles, essays, memos, launch notes, or newsletters
real outbound emails or DMs that worked
product docs, changelogs, README framing, and site copy

Do not use generic platform exemplars as source material.

Collection Workflow
Gather 5 to 20 representative samples when available.
Prefer recent material over old material unless the user says the older writing is more canonical.
Separate "public launch voice" from "private working voice" if the source set clearly splits.
If live X access is available, use x-api to pull recent original posts before drafting.
If site copy matters, include the current ECC landing page and repo/plugin framing.
What to Extract
rhythm and sentence length
compression vs explanation
capitalization norms
parenthetical use
question frequency and purpose
how sharply claims are made
how often numbers, mechanisms, or receipts show up
how transitions work
what the author never does
Output Contract

Produce a reusable VOICE PROFILE block that downstream skills can consume directly. Use the schema in references/voice-profile-schema.md.

Keep the profile structured and short enough to reuse in session context. The point is not literary criticism. The point is operational reuse.

Affaan / ECC Defaults

If the user wants Affaan / ECC voice and live sources are thin, start here unless newer source material overrides it:

direct, compressed, concrete
specifics, mechanisms, receipts, and numbers beat adjectives
parentheticals are for qualification, narrowing, or over-clarification
capitalization is conventional unless there is a real reason to break it
questions are rare and should not be used as bait
tone can be sharp, blunt, skeptical, or dry
transitions should feel earned, not smoothed over
Hard Bans

Delete and rewrite any of these:

fake curiosity hooks
"not X, just Y"
"no fluff"
forced lowercase
LinkedIn thought-leader cadence
bait questions
"Excited to share"
generic founder-journey filler
corny parentheticals
Persistence Rules
Reuse the latest confirmed VOICE PROFILE across related tasks in the same session.
If the user asks for a durable artifact, save the profile in the requested workspace location or memory surface.
Do not create repo-tracked files that store personal voice fingerprints unless the user explicitly asks for that.
Downstream Use

Use this skill before or inside:

content-engine
crosspost
lead-intelligence
article or launch writing
cold or warm outbound across X, LinkedIn, and email

If another skill already has a partial voice capture section, this skill is the canonical source of truth.

Weekly Installs
1.6K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn