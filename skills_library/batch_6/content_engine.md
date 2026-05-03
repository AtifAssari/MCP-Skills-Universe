---
title: content-engine
url: https://skills.sh/affaan-m/everything-claude-code/content-engine
---

# content-engine

skills/affaan-m/everything-claude-code/content-engine
content-engine
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill content-engine
Summary

Transform one idea into platform-native content across X, LinkedIn, TikTok, YouTube, and newsletters without cross-posting.

Adapts source assets (articles, videos, demos, docs) into distinct platform variants with native hooks, pacing, and CTAs
Covers five platforms with specific guidance: X (fast opens, one idea per post), LinkedIn (strong first lines, explicit lessons), short video (attention-grabbing first 3 seconds), YouTube (early results, visual refresh every 20-30 seconds), and newsletters (skimmable sections, working opening)
Follows a repurposing flow: extract atomic ideas from anchor asset, write platform variants, trim repetition, align CTAs to platform intent
Enforces quality gates: native reads per platform, strong specific hooks, no generic hype, no duplicate copy across platforms
SKILL.md
Content Engine

Build platform-native content without flattening the author's real voice into platform slop.

When to Activate
writing X posts or threads
drafting LinkedIn posts or launch updates
scripting short-form video or YouTube explainers
repurposing articles, podcasts, demos, docs, or internal notes into public content
building a launch sequence or ongoing content system around a product, insight, or narrative
Non-Negotiables
Start from source material, not generic post formulas.
Adapt the format for the platform, not the persona.
One post should carry one actual claim.
Specificity beats adjectives.
No engagement bait unless the user explicitly asks for it.
Source-First Workflow

Before drafting, identify the source set:

published articles
notes or internal memos
product demos
docs or changelogs
transcripts
screenshots
prior posts from the same author

If the user wants a specific voice, build a voice profile from real examples before writing. Use brand-voice as the canonical workflow when voice consistency matters across more than one output.

Voice Handling

brand-voice is the canonical voice layer.

Run it first when:

there are multiple downstream outputs
the user explicitly cares about writing style
the content is launch, outreach, or reputation-sensitive

Reuse the resulting VOICE PROFILE here instead of rebuilding a second voice model. If the user wants Affaan / ECC voice specifically, still treat brand-voice as the source of truth and feed it the best live or source-derived material available.

Hard Bans

Delete and rewrite any of these:

"In today's rapidly evolving landscape"
"game-changer", "revolutionary", "cutting-edge"
"here's why this matters" unless it is followed immediately by something concrete
ending with a LinkedIn-style question just to farm replies
forced casualness on LinkedIn
fake engagement padding that was not present in the source material
Platform Adaptation Rules
X
open with the strongest claim, artifact, or tension
keep the compression if the source voice is compressed
if writing a thread, each post must advance the argument
do not pad with context the audience does not need
LinkedIn
expand only enough for people outside the immediate niche to follow
do not turn it into a fake lesson post unless the source material actually is reflective
no corporate inspiration cadence
no praise-stacking, no "journey" filler
Short Video
script around the visual sequence and proof points
first seconds should show the result, problem, or punch
do not write narration that sounds better on paper than on screen
YouTube
show the result or tension early
organize by argument or progression, not filler sections
use chaptering only when it helps clarity
Newsletter
open with the point, conflict, or artifact
do not spend the first paragraph warming up
every section needs to add something new
Repurposing Flow
Pick the anchor asset.
Extract 3 to 7 atomic claims or scenes.
Rank them by sharpness, novelty, and proof.
Assign one strong idea per output.
Adapt structure for each platform.
Strip platform-shaped filler.
Run the quality gate.
Deliverables

When asked for a campaign, return:

a short voice profile if voice matching matters
the core angle
platform-native drafts
posting order only if it helps execution
gaps that must be filled before publishing
Quality Gate

Before delivering:

every draft sounds like the intended author, not the platform stereotype
every draft contains a real claim, proof point, or concrete observation
no generic hype language remains
no fake engagement bait remains
no duplicated copy across platforms unless requested
any CTA is earned and user-approved
Related Skills
brand-voice for source-derived voice profiles
crosspost for platform-specific distribution
x-api for sourcing recent posts and publishing approved X output
Weekly Installs
2.9K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass