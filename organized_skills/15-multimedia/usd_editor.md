---
rating: ⭐⭐
title: usd-editor
url: https://skills.sh/tomkrikorian/visionosagents/usd-editor
---

# usd-editor

skills/tomkrikorian/visionosagents/usd-editor
usd-editor
Installation
$ npx skills add https://github.com/tomkrikorian/visionosagents --skill usd-editor
SKILL.md
USD Editor
Quick Start

Use this skill for minimal, text-level USD or USDA edits. Keep the change small and preserve existing composition unless the task explicitly says otherwise.

If the change is material- or shader-specific for RealityKit, prefer shadergraph-editor.

Load References When
Reference	When to Use
usd-syntax	When you need a refresher on .usda syntax, values, and path formats.
prims-properties	When adding or editing prims, attributes, or relationships.
composition-variants	When touching sublayers, references, payloads, or variant sets.
transforms-units	When editing transforms, xformOps, or stage units and up-axis metadata.
time-samples	When modifying animated or time-sampled properties.
command-line-tools	When you need a quick reference for common USD command-line tools.
usdcat	When converting, flattening, or inspecting USD files.
usdchecker	When validating USD or USDZ assets, including RealityKit-focused checks.
usdrecord	When rendering images from USD files.
usdtree	When inspecting the prim hierarchy of a USD file.
usdzip	When creating or inspecting USDZ packages.
usdedit	When you need the official text-editing workflow for a USD-readable file.
visionos-runtime-loading.md	When the question is how the authored USD or USDZ actually loads and behaves in a visionOS app.
Workflow
Inspect the stage with usdtree, usdcat --loadOnly, or usdcat --flatten before editing, depending on the risk.
Locate the exact prim path and layer that owns the opinion.
Choose over, def, or a list edit deliberately.
Apply the minimum change needed.
Re-check paths, transforms, or composition edges that were touched.
Run the narrowest validation tool that matches the change, then run usdchecker --arkit for shipping visionOS USDZ assets.
Guardrails
Do not replace a prim with def when over is the correct edit.
Avoid composition-arc changes unless they are explicitly requested.
Do not hand-edit a .usdz package in place; inspect or unpack it, edit the source layer, rebuild the package, and validate the result.
Preserve existing formatting and comments when possible.
Output Expectations

Provide:

the prim or path edited
which reference files were used
the exact class of USD change made
the validation step used
routing to shadergraph-editor or runtime testing if needed
Weekly Installs
31
Repository
tomkrikorian/vi…osagents
GitHub Stars
49
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass