---
rating: ⭐⭐⭐
title: layerchart-svelte5
url: https://skills.sh/spences10/svelte-skills-kit/layerchart-svelte5
---

# layerchart-svelte5

skills/spences10/svelte-skills-kit/layerchart-svelte5
layerchart-svelte5
Installation
$ npx skills add https://github.com/spences10/svelte-skills-kit --skill layerchart-svelte5
SKILL.md
LayerChart Svelte 5

Docs: next.layerchart.com (NOT layerchart.com - that's Svelte 4)

Install
npm i layerchart@next d3-scale


CRITICAL: Use @next tag. Stable (1.x) is Svelte 4 only.

Quick Start
<Chart {data} x="date" y="value" tooltip={{ mode: 'bisect-x' }}>
	<Svg><Area class="fill-primary/20" /><Highlight points /></Svg>
	<Tooltip.Root>{#snippet children({ data })}{data.value}{/snippet}</Tooltip.Root>
</Chart>

Core Patterns
Tooltip: {#snippet children({ data })} - NOT let:data
Chart context: {#snippet children({ context })}
Gradient: {#snippet children({ gradient })}
Enable tooltip: tooltip={{ mode: 'band' | 'bisect-x' }}
Type data: {#snippet children({ data }: { data: MyType })}
Tooltip Modes
Mode	Use Case
band	Bar charts (scaleBand)
bisect-x	Time-series area/line
quadtree-x	Area (nearest x)
quadtree	Scatter plots
References
full-patterns.md - Area, Bar, Pie, Calendar
tooltip-modes.md - All modes
graph-patterns.md - ForceGraph, zoom/pan
Weekly Installs
130
Repository
spences10/svelt…ills-kit
GitHub Stars
77
First Seen
8 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass