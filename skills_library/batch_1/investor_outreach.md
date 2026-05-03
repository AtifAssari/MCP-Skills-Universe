---
title: investor-outreach
url: https://skills.sh/affaan-m/everything-claude-code/investor-outreach
---

# investor-outreach

skills/affaan-m/everything-claude-code/investor-outreach
investor-outreach
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill investor-outreach
Summary

Draft personalized, low-friction investor communications for cold outreach, warm intros, follow-ups, and updates.

Structures cold emails with specific personalization hooks (portfolio companies, public thesis, mutual connections) and a single concrete ask
Provides templates for warm intro requests with forwardable blurbs under 100 words, follow-up cadence (day 4–5 and day 10–12), and post-meeting updates
Enforces core rules: proof over adjectives, no generic copy, explicit asks, and tight word counts
Requires personalization context upfront; flags templates awaiting investor-specific details before sending
SKILL.md
Investor Outreach

Write investor communication that is short, concrete, and easy to act on.

When to Activate
writing a cold email to an investor
drafting a warm intro request
sending follow-ups after a meeting or no response
writing investor updates during a process
tailoring outreach based on fund thesis or partner fit
Core Rules
Personalize every outbound message.
Keep the ask low-friction.
Use proof instead of adjectives.
Stay concise.
Never send copy that could go to any investor.
Voice Handling

If the user's voice matters, run brand-voice first and reuse its VOICE PROFILE. This skill should keep the investor-specific structure and ask discipline, not recreate its own parallel voice system.

Hard Bans

Delete and rewrite any of these:

"I'd love to connect"
"excited to share"
generic thesis praise without a real tie-in
vague founder adjectives
begging language
soft closing questions when a direct ask is clearer
Cold Email Structure
subject line: short and specific
opener: why this investor specifically
pitch: what the company does, why now, and what proof matters
ask: one concrete next step
sign-off: name, role, and one credibility anchor if needed
Personalization Sources

Reference one or more of:

relevant portfolio companies
a public thesis, talk, post, or article
a mutual connection
a clear market or product fit with the investor's focus

If that context is missing, state that the draft still needs personalization instead of pretending it is finished.

Follow-Up Cadence

Default:

day 0: initial outbound
day 4 or 5: short follow-up with one new data point
day 10 to 12: final follow-up with a clean close

Do not keep nudging after that unless the user wants a longer sequence.

Warm Intro Requests

Make life easy for the connector:

explain why the intro is a fit
include a forwardable blurb
keep the forwardable blurb under 100 words
Post-Meeting Updates

Include:

the specific thing discussed
the answer or update promised
one new proof point if available
the next step
Quality Gate

Before delivering:

the message is genuinely personalized
the ask is explicit
the proof point is concrete
filler praise and softener language are gone
word count stays tight
Weekly Installs
2.8K
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