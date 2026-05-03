---
rating: ⭐⭐
title: build-clusters
url: https://skills.sh/calm-north/seojuice-skills/build-clusters
---

# build-clusters

skills/calm-north/seojuice-skills/build-clusters
build-clusters
Installation
$ npx skills add https://github.com/calm-north/seojuice-skills --skill build-clusters
Summary

Build topical authority clusters with pillar-spoke architecture and interlinking strategies.

Generates 8-20 subtopics from search data, intent patterns, and audience research to populate a cluster around a seed keyword
Structures clusters with a comprehensive pillar page (hub) and focused spoke pages (satellites), with mandatory bidirectional linking and lateral cross-links between siblings
Scores existing content coverage, identifies gaps (full, partial, or none), and flags pages needing creation or refresh
Provides production sequencing, interlinking tables with anchor text guidance, and cluster health metrics (coverage, link health, content quality) to determine readiness for ranking
SKILL.md
Build Clusters

Build a topical authority cluster from a seed keyword using pillar-spoke structure, coverage scoring, and interlinking plans.

What is a Topic Cluster?

A topic cluster is a group of interlinked pages that collectively cover a subject area. Google evaluates topical authority at the cluster level — ranking a single page is harder if the site has no supporting content around the topic.

Structure:

Pillar page — comprehensive overview of the broad topic (targets head term)
Spoke pages — focused articles covering subtopics (target body/long-tail terms)
Internal links — every spoke links to the pillar, pillar links to all spokes, spokes cross-link to siblings
Before You Start

Gather this context (ask if not provided):

Seed topic. The broad subject area to build authority around.
Existing content. Does the site already have pages on this topic? List them.
Business relevance. How does this topic connect to the product or service?
Content capacity. How many pieces can the team produce per month?
Step 1: Subtopic Discovery

From the seed topic, generate subtopics using these methods:

Search-derived:

People Also Ask questions for the seed keyword
Related searches at the bottom of SERPs
Autocomplete suggestions (seed + a, b, c...)
Competitor content analysis — what subtopics do top-ranking sites cover?

Intent-derived:

Awareness: "what is [topic]", "why [topic] matters"
Consideration: "best [topic] tools", "[topic] vs [alternative]"
Implementation: "how to [topic]", "[topic] tutorial"
Troubleshooting: "[topic] not working", "common [topic] mistakes"

Audience-derived:

Beginner questions about the topic
Advanced practitioner concerns
Decision-maker evaluation criteria

Aim for 8-20 subtopics per cluster.

Step 2: Cluster Map

Organize subtopics into a structured cluster:

Pillar: [Broad Topic] (head term)
│
├── Spoke: [Subtopic 1] (body term)
│   └── Intent: informational
│
├── Spoke: [Subtopic 2] (body term)
│   └── Intent: commercial investigation
│
├── Spoke: [Subtopic 3] (long-tail)
│   └── Intent: transactional
│
├── Spoke: [Subtopic 4] (long-tail)
│   └── Intent: informational
│
└── ... (8-15 more spokes)

Step 3: Coverage Scoring

Score how well the existing site covers the cluster:

Subtopic	Existing Page?	Quality (1-5)	Traffic	Gap?
[subtopic 1]	/blog/topic-1	4	500/mo	No
[subtopic 2]	—	—	—	Yes
[subtopic 3]	/blog/old-post	2	50/mo	Partial (needs refresh)
Full gap — no existing page, needs creation
Partial gap — page exists but is thin, outdated, or off-intent
Covered — strong existing page, may just need internal linking
Step 4: Pillar Page Design

The pillar page should:

Cover the topic comprehensively at an overview level (2,000-4,000 words)
Link to every spoke page for deeper dives
Be structured as a table of contents for the entire cluster
Target the highest-volume keyword in the cluster
Include a summary of each subtopic (2-3 paragraphs) with a link to the full spoke

Pillar page is NOT a mega-article that tries to cover everything in depth. It is a hub that distributes authority and directs readers to the right spoke.

Step 5: Interlinking Plan

Map the internal links:

From Page	To Page	Anchor Text	Context
Pillar	Spoke 1	"[subtopic 1] guide"	In the subtopic 1 overview section
Spoke 1	Pillar	"[broad topic]"	In the introduction or conclusion
Spoke 1	Spoke 2	"[subtopic 2]"	Where subtopic 2 is mentioned contextually
Spoke 3	Spoke 1	"[subtopic 1]"	Where comparison is relevant

Rules:

Every spoke links to the pillar (mandatory)
Pillar links to every spoke (mandatory)
Spokes cross-link to 2-4 siblings (where contextually natural)
Use varied anchor text (not always the exact keyword)
Step 6: Cluster Health Metrics

Score the cluster's readiness to compete:

Coverage Score  = (Covered spokes / Total spokes) x 100
Link Health     = (Spokes with bidirectional pillar link / Total spokes) x 100
Content Quality = (Spokes scoring 3+ quality / Total spokes) x 100

Metric	Score	Threshold
Coverage	[x]%	> 70% to start ranking for pillar keyword
Link Health	[x]%	100% is the target — every spoke must link to pillar and back
Content Quality	[x]%	> 80% — clusters with thin spokes dilute authority
Expected Outcomes by Health Level
Cluster State	Coverage	Link Health	Content Quality	Expected Result
Incomplete	<50%	<70%	Any	Pillar unlikely to rank page 1; spokes rank individually at best
Developing	50-70%	70-90%	50-80%	Pillar may appear page 2-3; some spokes rank for long-tail
Competitive	70-90%	100%	80-90%	Pillar competes for page 1; most spokes rank for their targets
Dominant	>90%	100%	>90%	Pillar strong on page 1; cluster captures most queries in the topic
Internal Link Standards per Cluster
Link Type	Minimum Count	Direction
Pillar → each spoke	1 per spoke	Downward — link from the relevant section of the pillar
Each spoke → pillar	1 per spoke	Upward — "our complete [topic] guide"
Spoke ↔ sibling spokes	2-4 per spoke	Lateral — where contextually natural
Cross-cluster bridges	0-2 per cluster	Between hubs — only with genuine topical relevance

Cluster ready to compete: Coverage > 70%, Link Health = 100%, Content Quality > 80%. Below these thresholds, prioritize filling gaps before expecting the pillar to rank.

Step 7: Production Sequence

Order the content production for maximum impact:

Pillar page first — even as a draft, it establishes the hub
Highest-opportunity spokes next — pages targeting gaps with the best opportunity scores
Refresh existing spokes — update and relink any partial-gap pages
Remaining spokes — fill out the cluster over time
Update pillar — add links to each new spoke as it's published
Output Format
Topic Cluster: [seed topic]

Cluster Summary

Pillar keyword: [keyword] (volume: [x], difficulty: [y])
Total spokes: [count]
Existing coverage: [x]% ([n] pages exist, [n] need creation)
Total cluster volume: [sum of all keyword volumes]

Cluster Map [Visual structure from Step 2]

Coverage Scorecard [Table from Step 3]

Pillar Page Spec

Target keyword: [keyword]
Recommended title: [title]
Structure: [heading outline with spoke links]

Interlinking Plan [Table from Step 5]

Production Roadmap [Ordered list from Step 6 with estimated timelines]

Pro Tip: Use the free Blog Keyword Generator to discover subtopics for your cluster. SEOJuice MCP users get automatic cluster mapping — run /seojuice:content-strategy to see existing clusters with coverage metrics, or use list_clusters and get_cluster_detail to check cluster health and identify gaps.

Weekly Installs
1.6K
Repository
calm-north/seoj…e-skills
GitHub Stars
7
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn