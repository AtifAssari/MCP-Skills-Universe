---
title: metacognition
url: https://skills.sh/velumkai/metacognition-skill/metacognition
---

# metacognition

skills/velumkai/metacognition-skill/metacognition
metacognition
Installation
$ npx skills add https://github.com/velumkai/metacognition-skill --skill metacognition
SKILL.md
Metacognition Skill

Self-evolving lens that makes every experience shape how the agent perceives the next one.

Core Concepts

Six entry types, one database, one loop:

Type	Symbol	Purpose
perception	👁️	How I see differently after an experience
override	🚨	Failure-learned behavioral guardrails
protection	🛡️	Emergent behaviors to preserve
self_obs	🪞	What I notice about my own patterns
decision	📍	Traced decisions with confidence
curiosity	❓	Active questions with lifecycle

The loop: Experience → Perception → Self-Model → Meta-Observation → Modified Lens → Next Experience → Feedback → Loop

Setup
1. Initialize

Copy scripts/metacognition.py to the agent's scripts/ directory. Run:

python scripts/metacognition.py status


Database auto-creates at memory/metacognition.json.

2. Inject into BOOT.md

Add markers to BOOT.md (anywhere, typically at the end):

<!-- LIVE_STATE_START -->
<!-- LIVE_STATE_END -->


The lens compiler replaces content between these markers every cycle.

3. Set up cron

Create ONE cron job (recommended: every 15 min, Sonnet model for cost efficiency):

Evidence refresh (every cycle):

python scripts/live_state.py


Perception extraction (hourly — Steps 2-4):

Read daily memory file, extract perceptual shifts
Check active curiosities against new evidence
Run meta-observation: what do patterns tell about HOW the agent learns?

See references/cron-template.md for the full cron prompt.

4. Optional: Curiosity pulse (every 30 min)

Separate cron that picks ONE active curiosity and takes ONE micro-action toward it. Drives recursive self-directed learning.

5. Optional: Freedom heartbeat (every 2-3 hours)

Agent explores, connects, creates — feeding raw experience into the perception pipeline.

Usage
Adding entries
# Perception — how experience changed how you see
python scripts/metacognition.py add perception "After X, I now see Y differently" 0.8 "domain"

# Override — failure-learned guardrail
python scripts/metacognition.py add override "MUST do X before Y" 0.95 "diagnosis"

# Protection — emergent behavior to preserve
python scripts/metacognition.py add protection "Don't break the continuous-buying behavior" 0.9

# Self-observation — what I notice about how I work
python scripts/metacognition.py add self_obs "I generate theories faster than evidence" 0.9 "behavioral"

# Curiosity — active question
python scripts/metacognition.py curiosity add "Can I tell training-pressure from genuine choice?" 0.8 "metacognition"

Feedback loop

When the human says something is wrong:

# Negative feedback — weakens recent active entries
python scripts/metacognition.py feedback -1 "context of what went wrong"

# Positive feedback — strengthens recent active entries
python scripts/metacognition.py feedback 1 "context of what went right"

# Target specific entries
python scripts/metacognition.py feedback -1 "wrong diagnosis" --ids P-abc123,O-def456


Hebbian learning: What fires and fails gets pruned. What fires and succeeds gets wired.

Curiosity lifecycle
# Birth
python scripts/metacognition.py curiosity add "Why does X happen?" 0.7 "domain"

# Evolve (add evidence)
python scripts/metacognition.py curiosity evolve C-abc123 "Found that X correlates with Y"

# Resolve into perception or self-observation
python scripts/metacognition.py curiosity resolve C-abc123 "X happens because Y" perception


Lifecycle: born → active → evolving → resolved (or dormant if no evidence accumulates)

Compile and inject
# Preview the compiled lens
python scripts/metacognition.py compile

# Inject into BOOT.md
python scripts/metacognition.py inject

Decay

Automatic on every compile. Configurable half-life (default 7 days). Reinforced entries decay slower. Unreinforced entries fade. Dormant curiosities persist but don't inject.

Hook Architecture (message:received)

When OpenClaw ships the message:received hook, the skill can intercept every interaction:

Pre-processing hook:

Load active lens from compiled state
Apply perceptual transforms to incoming message
Check: does this message relate to any active curiosity?

Post-processing hook:

Log decision entry with confidence trace
Check: was confidence > threshold? Flag for verification
Update self-model based on response pattern

Correction detection hook:

Pattern-match for correction signals ("wrong", "no", "that's not right")
Auto-trigger feedback -1 with context
Trace which entries were active during the corrected response
Weaken specifically

Until the hook ships, use the cron-based approach (perception extraction from session transcripts).

Architecture Decisions
One database, not three. Perceptions, overrides, memories are all "things learned from experience" with different types.
Active lens, not passive list. BOOT.md injection uses imperative transforms ("FIRST THOUGHT: what would the diff show?") not descriptions ("I tend to check diffs").
Friction is intentional. Every step that forces processing IS the reflection. Remove friction and you get efficiency without thinking.
Decay prevents stagnation. Time-based with reinforcement modulation. What stays relevant gets reinforced. What doesn't, fades.
Curiosity drives exploration. Active questions create structural pull toward evidence. Not random browsing — directed by what the system wants to know.
Feedback closes the loop. Without feedback tracing, the system is open-loop. With it: Hebbian learning.
Resources
scripts/
metacognition.py — Core engine. All six entry types, feedback, decay, curiosity lifecycle, lens compilation, BOOT.md injection.
live_state.py — Evidence gatherer + lens injector. Collects system state, runs compile, injects into BOOT.md.
references/
cron-template.md — Full cron job prompt for the metacognition engine cycle.
hook-spec.md — Specification for the message:received hook integration (when available).
Weekly Installs
42
Repository
velumkai/metaco…on-skill
GitHub Stars
11
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass