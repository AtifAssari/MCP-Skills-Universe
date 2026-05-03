---
title: walking-through-the-grove
url: https://skills.sh/autumnsgrove/groveengine/walking-through-the-grove
---

# walking-through-the-grove

skills/autumnsgrove/groveengine/walking-through-the-grove
walking-through-the-grove
Installation
$ npx skills add https://github.com/autumnsgrove/groveengine --skill walking-through-the-grove
SKILL.md
Walking Through the Grove

A naming ritual for the Grove ecosystem. Use this when you need to find a name that fits—not just a clever pun, but something that belongs in this forest.

When to Activate
Naming a new service, feature, or concept for Grove
Renaming something that doesn't feel right
Called from the grove-ui-design skill when new UI needs a name
Any time you're adding something to the Grove ecosystem
The Process

This is a journey, not a checklist. Take your time.

Step 1: Read the Naming Philosophy
# Always start here
cat docs/philosophy/grove-naming.md


Read the entire document. Don't skim. Let it sink in:

"A forest of voices. Every user is a tree in the grove."
Names aren't branding—they're the language of an ecosystem
Things that grow, shelter, connect
Not about trees directly—about what happens in and around the forest
Step 2: Create a Scratchpad

Create a markdown file for your journey:

# Create: docs/philosophy/naming-research/{concept}-naming-journey.md


This scratchpad is where you think out loud. Include:

ASCII art visualizations
Questions you're asking yourself
Rejected ideas and why
The moment when something clicks
Step 3: Visualize the Grove

In your scratchpad, draw the grove. ASCII art helps:

                              ☀️
                           🌲   🌲   🌲
                        🌲    🌳    🌲
    ═══════════════════════════════════════════════
               ROOTS CONNECT BENEATH
                  (mycelium network)


Place the existing services in the visualization:

Where is Meadow? (the open social space)
Where is Heartwood? (the core identity)
Where is Ivy? (climbing, connecting)
Where is Pantry? (the warm kitchen cupboard)
Step 4: Ask "What IS This Thing?"

Don't ask "where does it go?" first. Ask:

What is it, fundamentally?

Is it a place? (Meadow, Nook, Clearing)
Is it an object/process? (Amber, Bloom, Patina)
Is it a feature of the tree? (Foliage, Heartwood, Rings)
Is it a connection? (Ivy, Mycelium, Reeds)

What does it DO in the user's life?

Protect? (Shade, Patina)
Connect? (Ivy, Meadow, Reeds)
Store? (Amber, Trove)
Guide? (Waystone, Trails)
Create? (Terrarium, Foliage)

What emotion should it evoke?

Warmth?
Safety?
Discovery?
Community?
Privacy?
Step 5: Walk Through the Forest

Imagine you're a user walking through the grove. Write this in your scratchpad:

## Walking Through...

I enter the grove. I see...
I walk past the Meadow where others gather.
I find my tree—my blog, my space.
I check my Rings (private growth).
I see my Foliage (how others see me).

Now I need [THE NEW THING]. Where do I find it?
What does it look like? Who's there? How does it feel?


Let the scene guide you to the name.

Step 6: Generate Candidates

Based on your walk, list 5-10 candidates. For each:

**[Name]** - `[name].grove.place`

- What it means in nature
- Why it fits this concept
- The vibe/feeling
- Potential issues

Step 7: Test the Tagline

A good Grove name should complete this sentence naturally:

"[Name] is where you **___**."

Or:

"[Name] is the **___**."

If you can't write a poetic one-liner, the name might not fit.

Step 8: Write the Entry

Once you've found the name, write it in Grove style:

## [Name]

**[Tagline]** · `[domain].grove.place`

[2-3 sentences explaining what this thing IS in the real world—
the natural metaphor. Then 2-3 sentences explaining what it does
in Grove. End with the feeling it should evoke.]

_[A poetic one-liner in italics]_

Step 9: Check for Conflicts

Before finalizing:

Search the codebase for the name
Check if the subdomain concept conflicts with existing services
Make sure it's not too similar to existing names
Consider how it sounds spoken aloud
Step 10: Implement

Update all the files:

docs/grove-naming.md — Add the full entry
docs/philosophy/grove-naming.md — Update source (generates manifest)
services/grove-router/src/index.ts — Claim subdomain
plant/src/routes/api/check-username/+server.ts — Reserve username
Workshop page if applicable
Icons if applicable
Regenerate the GroveTerm manifest — Run scripts/generate/grove-term-manifest.ts to rebuild grove-term-manifest.json with the new term. This manifest powers all GroveTerm components (GroveTerm, GroveSwap, GroveText, etc.) that automatically switch between standard and Grove terminology based on the user's Grove Mode setting.
Philosophy Reminders

From the naming document:

"These names share common ground: nature, shelter, things that grow. But none of them are about trees directly. They're about what happens in and around the forest."

"The Grove is the place. These are the things you find there."

The name should feel inevitable—like it was always there, waiting to be discovered.

Example Journey: Finding "Porch"

The problem: We need a name for support tickets.

First attempts (rejected):

Echo → "echo chamber" feels like shouting into void, no one listening
Feather, Flare, Dove → These are about sending something
But support isn't about sending—it's about connecting

The walk:

I'm in the grove. Something's wrong with my tree. I need help. Waystone gives me self-service guides. Clearing shows me status. But I need to actually talk to someone.

What do I do?

I walk to... a cabin. There's a porch. Someone's there. I sit down. We talk about what's going on.

The realization: Support isn't a ticket system. It's a porch conversation.

The name: Porch

A porch on a cabin in the woods. You come up the steps. You sit down. The grove keeper comes out. You talk.

"Have a seat on the porch. We'll figure it out together."

Integration with Other Skills
grove-ui-design

When the grove-ui-design skill encounters something that needs naming:

Pause the UI work
Invoke this skill
Complete the naming journey
Return to UI work with the new name

This keeps the naming intentional rather than rushed.

grove-documentation

After finding the right name, you'll need to write its description. Invoke the grove-documentation skill when:

Writing the entry for docs/grove-naming.md
Crafting the tagline
Writing the poetic one-liner

The naming document entries should follow Grove's voice: warm, direct, avoiding AI patterns. The grove-documentation skill has the full guidelines.

The Journey Files are Sacred

Keep your naming journey files. They're documentation of how we think about Grove:

docs/philosophy/naming-research/
  grove-journey.md                    ← The original Porch discovery
  {feature}-naming-journey.md         ← All naming journeys


These become part of Grove's story.

Weekly Installs
63
Repository
autumnsgrove/groveengine
GitHub Stars
5
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass