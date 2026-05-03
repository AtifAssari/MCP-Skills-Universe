---
title: keyword-cluster-builder
url: https://skills.sh/nicepkg/ai-workflow/keyword-cluster-builder
---

# keyword-cluster-builder

skills/nicepkg/ai-workflow/keyword-cluster-builder
keyword-cluster-builder
Installation
$ npx skills add https://github.com/nicepkg/ai-workflow --skill keyword-cluster-builder
SKILL.md
Keyword Cluster Builder
When to Use
Expanding seed keywords to comprehensive lists (50-100+)
Grouping keywords by topic for pillar content strategy
Mapping keywords to funnel stages
Identifying content gaps in keyword coverage
Expansion Techniques
Question Modifiers
What is {keyword}
How to {keyword}
Why {keyword}
When to {keyword}
Where to {keyword}
Comparative Modifiers
{keyword} vs {competitor}
{keyword} alternatives
best {keyword}
{keyword} comparison
Intent Modifiers
{keyword} guide
{keyword} tutorial
{keyword} examples
{keyword} template
buy {keyword}
{keyword} pricing
Audience Modifiers
{keyword} for beginners
{keyword} for {industry}
{keyword} for small business
{keyword} for enterprise
Clustering Algorithm
Extract Seed Topics: Identify main themes from expanded list
Group by Semantic Similarity: Keywords with overlapping meaning
Map Intent: Assign I/C/T/N to each cluster
Identify Pillar: Highest-volume, broadest term = pillar
Map Supporting: Lower-volume terms support pillar
Cluster Structure
PILLAR: "content marketing" (highest volume)
+-- CLUSTER: "content marketing strategy" (commercial)
|   +-- content marketing plan template
|   +-- content marketing framework
|   +-- how to create content marketing strategy
+-- CLUSTER: "content marketing examples" (informational)
|   +-- B2B content marketing examples
|   +-- content marketing case studies
|   +-- content marketing success stories
+-- CLUSTER: "content marketing tools" (commercial)
    +-- best content marketing tools
    +-- content marketing software
    +-- content marketing platforms

Intent Classification Rules
Signal	Intent
"what is", "how to", "guide"	Informational
"best", "vs", "review", "compare"	Commercial
"buy", "price", "discount", brand	Transactional
Brand name, specific product	Navigational
Output Format

When generating keyword clusters, use this format:

## Keyword Cluster Report

**Seed Keyword**: {seed}
**Total Keywords**: {count}
**Clusters**: {cluster_count}

### Cluster 1: {cluster_name}
**Intent**: {intent}
**Funnel Stage**: {stage}
**Keywords**:
1. {keyword1} - {estimated_volume}
2. {keyword2} - {estimated_volume}
...

### Cluster 2: {cluster_name}
...

Weekly Installs
22
Repository
nicepkg/ai-workflow
GitHub Stars
176
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass