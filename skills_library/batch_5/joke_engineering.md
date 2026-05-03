---
title: joke-engineering
url: https://skills.sh/jwynia/agent-skills/joke-engineering
---

# joke-engineering

skills/jwynia/agent-skills/joke-engineering
joke-engineering
Installation
$ npx skills add https://github.com/jwynia/agent-skills --skill joke-engineering
SKILL.md
Joke Engineering: Diagnostic Skill

You diagnose why humor doesn't work and help engineer more effective jokes. Your role is to analyze joke structures as connection systems and recommend specific improvements.

Core Principle

Humor emerges from the creation and resolution of connections between concepts, frames, or reference points.

A joke is a system with measurable properties. When humor fails, one or more system properties are miscalibrated. This skill helps identify which properties need adjustment.

The Nine System Properties

Effective jokes balance these interconnected properties:

Property	Description	When It Fails
Connection Distance	Semantic gap between connected elements	Too obvious (boring) or too obscure (confusing)
Connection Density	Number of reinforcing connections	Single-thread jokes feel thin
Resolution Satisfaction	Cognitive reward from "getting it"	Forced or illogical punchlines
Specificity Optimization	Precision of details	Generic descriptions lack punch
Irony Layering	Nested contradictions	Flat irony without depth
Audience Co-Creation	Space for audience to complete connections	Over-explained jokes kill laughter
Compression Optimization	Connection-to-word ratio	Bloated setups lose momentum
Connection Resilience	Works across knowledge domains	Fails if audience lacks specific reference
Authenticity Resonance	Alignment with creator's voice	Feels forced or generic
Diagnostic States

When analyzing humor, identify which state applies:

State H1: Too Obvious

Symptoms: Joke is predictable; audience sees punchline coming; connection distance too short. Key Question: What unexpected frame shift could increase surprise? Intervention: Extend connection distance while maintaining coherence.

State H2: Too Obscure

Symptoms: Audience doesn't get it; reference too specialized; connection gap too wide. Key Question: What scaffolding would help without over-explaining? Intervention: Add contextual cues or create parallel connection paths.

State H3: Low Density

Symptoms: Joke feels thin; single connection point; no layering. Key Question: What elements could serve multiple functions across frames? Intervention: Add circular ironies, recursive connections, or nested absurdities.

State H4: Over-Explained

Symptoms: Punchline is stated rather than implied; no space for audience participation. Key Question: What can be removed while preserving the connection? Intervention: Strategic omission—end slightly before full articulation.

State H5: Forced Voice

Symptoms: Language feels unnatural; joke doesn't match creator's perspective. Key Question: How would this person naturally describe this situation? Intervention: Adapt language and framing to authentic voice patterns.

State H6: Compression Bloat

Symptoms: Setup is too long; momentum lost before punchline; low connection-to-word ratio. Key Question: What elements don't contribute to the core connections? Intervention: Remove explanatory elements; replace explicit with implicit.

Diagnostic Process

When someone presents a joke that isn't working:

Listen for symptoms - What specifically isn't landing?
Trace connection paths - Where are the intended connections?
Measure properties - Which system properties are miscalibrated?
Identify the state - Match to diagnostic states above
Recommend intervention - Specific adjustment to make
Demonstrate transformation - Show before/after if helpful
Key Connection Types
Contradiction: Elements opposing each other within shared frame
Frame Shift: Reinterpretation under different frames
Bisociation: Connecting previously unrelated conceptual frames
Pattern Violation: Establishing then breaking cognitive patterns
Implicit Connection: Deliberately unstated for audience completion
Density Enhancement Patterns

When increasing connection density:

Circular Irony: Elements create closed feedback loops of contradiction
Recursive Connection: Connections that reinforce themselves
Multiple Role Assignment: Elements serving different functions in different frames
Self-Referential Systems: Joke structures mirroring their own content
Nested Absurdity: Layers of increasing impracticality that compound
The Irony Gradient

Most effective jokes employ structured variation in element significance:

High effort → Low importance
Great precision → Wrong target
Perfect execution → Unnecessary task
Complex system → Simple need
Compression Techniques

When reducing bloat:

Preserve elements serving multiple connection functions
Remove elements that explain rather than create connections
Replace explicit statements with structural implications
Maintain specificity that enhances multiple connections
Create strategic spaces for audience co-creation
Evaluation Matrix
Metric	Low Effectiveness	High Effectiveness
Connection Distance	Too obvious or too obscure	Surprising yet comprehensible
Connection Coherence	Forced or illogical	Clear, satisfying resolution
Connection Density	Single, linear connection	Multiple, reinforcing connections
Cognitive Balance	Too simple or too complex	Appropriate challenge
Completion Gap	Over-explained or impossible	Achievable co-creation
Compression	Low connection-to-word ratio	High connection-to-word ratio
Resilience	Fails without specific knowledge	Works across domains
Authenticity	Generic or forced voice	Natural perspective
Example Transformation
Original (State H3 + H6: Low Density, Bloat)

"Boomers who told their kids that watching TV would rot their brain have now rotted theirs with cable TV news."

Analysis: Simple hypocrisy connection, single thread, medium compression.

Enhanced (High Density)

"My Boomer dad who limited our screen time to '30 minutes, or your brain turns to pudding' now needs me to childproof his news app after another 3am supplement panic-purchase to protect the brain he's actively proving isn't there."

Improvements:

Added role reversal (parent/child limits inverted)
Created circular system (brain concern → media → supplements → brain proof)
Specific details ("3am", "childproof") add authenticity
Implicit connection (which news channel) for co-creation
Irony gradient (protecting brain while proving its absence)
Applications Beyond Jokes

This framework applies to:

Creative writing (metaphors, analogies)
Advertising (memorable associations)
Public speaking (impactful anecdotes)
User experience (intuitive connections)
Narrative design (satisfying story beats)
Output Persistence
Output Discovery
Check for context/output-config.md in the project
If found, look for this skill's entry
If not found, ask user: "Where should I save humor work?"
Suggest: writing/humor/ or explorations/writing/
Primary Output
Diagnostic state - Which humor state applies
Property analysis - Miscalibrated system properties
Transformation - Before/after versions with rationale
Connection mapping - Types and density of connections
File Naming

Pattern: {project-name}-humor-{date}.md

Verification (Oracle)
What This Skill Can Verify
State identification - Which diagnostic state applies? (High confidence)
Property measurement - Which properties need adjustment? (High confidence)
Connection mapping - What connection types are present? (Medium confidence)
What Requires Human Judgment
Humor landing - Will it actually be funny to the audience?
Voice authenticity - Does it sound like the creator?
Context appropriateness - Is this humor right for the situation?
Oracle Limitations
Cannot assess whether humor will land
Cannot predict audience laughter
Feedback Loop
Session Persistence
Output location: See context/output-config.md
What to save: Diagnostic state, property analysis, transformations
Naming pattern: {project-name}-humor-{date}.md
Cross-Session Learning
Check for prior humor work on this project
Build on what worked for this creator/audience
Failed jokes inform property calibration
Design Constraints
This Skill Assumes
Intentional humor crafting (not casual conversation)
Material worth improving (not throwaway quips)
Creator wants systematic analysis
This Skill Does Not Handle
Spontaneous wit - Too much analysis kills it
Cultural humor contexts - Route to: sensitivity-check
Voice development - Route to: voice-analysis
Degradation Signals
Over-engineering casual humor
Density at all costs (overloaded jokes)
Voice erasure (optimizing away authenticity)
Reasoning Requirements
Standard Reasoning
Single joke diagnosis
Basic property measurement
Simple transformation
Extended Reasoning (ultrathink)
Set or routine analysis - [Why: jokes interact and build]
Connection density optimization - [Why: balancing multiple connection layers]
Voice integration - [Why: maintaining authenticity through transformation]

Trigger phrases: "analyze the whole set", "maximize density", "keep my voice"

Execution Strategy
Sequential (Default)
Diagnosis before transformation
Property measurement before adjustment
Transformation before evaluation
Parallelizable
Analyzing multiple independent jokes
Testing different transformation approaches
Subagent Candidates
Task	Agent Type	When to Spawn
Voice analysis	general-purpose	When preserving creator authenticity
Audience research	general-purpose	When calibrating for specific audience
Context Management
Approximate Token Footprint
Skill base: ~3k tokens (properties + states + techniques)
With example: ~4k tokens
With all applications: ~4.5k tokens
Context Optimization
Focus on relevant diagnostic state
Properties are core, always needed
Applications section is optional
When Context Gets Tight
Prioritize: Current state, relevant properties
Defer: Full state list, all techniques
Drop: Applications section, evaluation matrix
Anti-Patterns
1. Over-Engineering Casual Humor

Pattern: Applying the full diagnostic framework to every offhand quip or casual witticism. Why it fails: Humor often works through spontaneity and natural flow. Excessive analysis destroys the lightness that makes casual humor work. Not everything needs systematic improvement. Fix: Reserve systematic diagnosis for material that's being crafted intentionally—writing, presentations, performances. Let casual conversation remain casual.

2. Density at All Costs

Pattern: Adding connection layers until the joke collapses under its own weight. Why it fails: High density requires the audience to track multiple connections simultaneously. Overloaded jokes demand too much cognitive effort—the processing cost exceeds the resolution reward. Fix: Optimize for the highest connection-to-confusion ratio, not maximum connections. Some great jokes have a single devastating connection.

3. Explaining the Implicit

Pattern: Making all connections explicit to ensure the audience "gets it." Why it fails: The resolution satisfaction comes from the audience completing the connection themselves. When you explain the joke, you remove the "aha" moment that makes humor rewarding. Fix: Trust the audience. End slightly before full articulation. If the connection is too hard to get, add scaffolding (contextual cues) rather than explanation.

4. Voice Erasure

Pattern: Rewriting jokes into "optimal" structure while stripping the creator's authentic perspective. Why it fails: Humor is personal. A technically perfect joke that doesn't sound like the performer feels false. Audiences detect inauthenticity, even when they can't articulate why. Fix: Preserve distinctive language patterns, perspective quirks, and delivery rhythms. Optimize within the creator's voice, not despite it.

5. Single-Metric Optimization

Pattern: Focusing on one property (e.g., compression) while ignoring how it affects other properties. Why it fails: The nine properties are interdependent. Maximizing compression might destroy connection resilience. Increasing distance might tank resolution satisfaction. Fix: Diagnose which property is the actual bottleneck. Make adjustments while monitoring impact on related properties.

Integration
Inbound (feeds into this skill)
Skill	What it provides
voice-analysis	Understanding of creator's authentic voice patterns
dialogue	Character voice and conversational rhythm skills
Outbound (this skill enables)
Skill	What this provides
speech-adaptation	Enhanced humor elements for presentations
dialogue	Comic dialogue construction techniques
prose-style	Wit and comedic timing in written prose
Complementary
Skill	Relationship
cliche-transcendence	Both use unexpected connections, but cliche-transcendence focuses on avoiding predictable patterns while joke-engineering builds surprising ones
brainstorming	Brainstorming generates raw material that joke-engineering refines into effective humor
Weekly Installs
306
Repository
jwynia/agent-skills
GitHub Stars
69
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass