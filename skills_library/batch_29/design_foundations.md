---
title: design-foundations
url: https://skills.sh/kazdenc/builder-skills/design-foundations
---

# design-foundations

skills/kazdenc/builder-skills/design-foundations
design-foundations
Installation
$ npx skills add https://github.com/kazdenc/builder-skills --skill design-foundations
SKILL.md
The Five Planes of User Experience

A product's user experience is built in layers, from abstract to concrete. Each plane builds on the one below it. Decisions made on lower planes constrain and inform decisions on higher planes.

┌─────────────────────────────────┐
│          SURFACE                │  Visual/sensory design
│  ┌───────────────────────────┐  │
│  │        SKELETON           │  │  Layout, navigation, information design
│  │  ┌─────────────────────┐  │  │
│  │  │     STRUCTURE        │  │  │  Interaction design, information architecture
│  │  │  ┌───────────────┐   │  │  │
│  │  │  │    SCOPE       │  │  │  │  Features, content requirements
│  │  │  │  ┌─────────┐   │  │  │  │
│  │  │  │  │STRATEGY │   │  │  │  │  User needs, product objectives
│  │  │  │  └─────────┘   │  │  │  │
│  │  │  └───────────────┘   │  │  │
│  │  └─────────────────────┘  │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘

The Duality

Every product has two dimensions that run through all five planes:

Functionality side — The product as a tool (tasks, features, interaction)
Information side — The product as information (content, structure, presentation)
Plane	Functionality	Information
Strategy	Product objectives	User needs
Scope	Functional specifications	Content requirements
Structure	Interaction design	Information architecture
Skeleton	Interface design	Navigation + information design
Surface	Sensory design	Sensory design
How to Use This Framework
Diagnosing Problems

When something feels wrong with a product, identify which plane the problem lives on:

Users don't understand what the product is for → Strategy
Features are missing, bloated, or misaligned with goals → Scope
Users get lost, confused by flows, or can't find things → Structure
Users see the right content but can't interact with it effectively → Skeleton
The interface looks bad, feels cheap, or sends wrong signals → Surface

Common mistake: Trying to fix a lower-plane problem with a higher-plane solution. Redesigning the visual surface won't fix broken information architecture. Adding navigation won't fix a scope problem.

Building Products

Work bottom-to-top, but not strictly sequentially. Planes overlap — you can start structure work before scope is fully locked. But decisions should flow upward: strategy informs scope, scope informs structure, and so on.

Each plane should be mostly resolved before the plane above it is finalized. Changing strategy after the skeleton is built means rework cascades through every layer.

Evaluating Products

Walk through each plane and ask:

Strategy — Do we know who this is for and what it should accomplish?
Scope — Does the feature set match the strategy? Is anything missing or unnecessary?
Structure — Can users navigate the system and complete tasks without confusion?
Skeleton — Is the interface effective? Can users find controls, understand layout?
Surface — Does the visual design reinforce the brand, hierarchy, and experience?

→ Consult individual plane references for deep dives:

Strategy — Product objectives, user needs, personas, success metrics
Scope — Functional specs, content requirements, prioritization
Structure — Interaction design, information architecture
Skeleton — Interface design, navigation design, wireframes
Surface — Sensory design, color, typography, contrast, consistency
Weekly Installs
10
Repository
kazdenc/builder-skills
GitHub Stars
35
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass