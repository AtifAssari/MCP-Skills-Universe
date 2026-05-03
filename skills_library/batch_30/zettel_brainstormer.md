---
title: zettel-brainstormer
url: https://skills.sh/hxy9243/skills/zettel-brainstormer
---

# zettel-brainstormer

skills/hxy9243/skills/zettel-brainstormer
zettel-brainstormer
Installation
$ npx skills add https://github.com/hxy9243/skills --skill zettel-brainstormer
SKILL.md
Zettel Brainstormer

Run this workflow in order. Keep each stage separate so relevance decisions happen before drafting.

Configure Once
Run setup:
python zettel-brainstormer/scripts/setup.py

Confirm zettel-brainstormer/config/models.json contains:
zettel_dir
output_dir
models and agent_models
retrieval.link_depth and retrieval.max_links
Stage 1: Retrieval

Goal: retrieve candidate notes from the seed note.

Required order for this stage:

Read retrieval limits from config and target candidate count using retrieval.max_links.
Check if the external zettel-link skill is available. If it exists, run semantic retrieval via its scripts/search.py command using the seed note's topic or title. If it doesn't exist, warn the user and skip this step.
Run local retrieval with scripts/find_links.py to gather exact wikilinks and tag-overlap notes.
Merge and deduplicate candidates from both sources. Prioritize semantic candidates first, and trim to the configured count.
Exclude the seed note itself.

Local retrieval command:

python zettel-brainstormer/scripts/find_links.py \
  --input "/absolute/path/to/Seed Note.md" \
  --output /tmp/zettel_candidates.json


Treat /tmp/zettel_candidates.json as the candidate pool for preprocessing.

Stage 2: Preprocess (Subagent Per Note)

Goal: preprocess each candidate note and decide relevance to the seed note.

Read agents/preprocess.md as the per-note instruction.
Spawn one subagent per candidate note.
For each note, require:
Relevance score against the seed note topic.
Concise summary.
Distinct key points.
Short evidence quotes when useful.
Save each subagent output as markdown (one file per source note).

Quality rules:

Reject notes with weak relevance.
Prefer concrete claims and non-duplicated points.
Keep outputs compact and structured for downstream merge.
Stage 3: Draft (Synthesis Subagent)

Goal: gather only relevant preprocess outputs and generate a referenced draft.

Run the aggregation helper:
python zettel-brainstormer/scripts/compile_preprocess.py \
  --seed "/absolute/path/to/Seed Note.md" \
  --preprocess-dir /tmp/zettel_preprocess \
  --output /tmp/zettel_draft_packet.json

Read agents/draft.md.
Use one drafting subagent with:
Seed note content
Filtered relevant notes from /tmp/zettel_draft_packet.json
Required citation mapping from the packet
Produce a draft that cites source notes inline and preserves traceability.
Stage 4: Publish (Publisher Subagent)

Goal: rewrite the draft into natural long-form writing while preserving evidence quality.

Read agents/publisher.md.
Use one publisher subagent to rewrite the draft with these constraints:
Remove generic AI phrasing.
Use natural language and a coherent author voice.
Organize points with clear tiered argument structure.
Remove irrelevant points.
Do not force weak connections between notes.
Keep explicit citations for all retained claims.
Do not publish the draft's internal "Argument Spine" section.
Append valid frontmatter properties, including article-relevant tags.
Always end with a ## References section listing every cited note.
Stage 5: Delivery

Goal: Present the final output to the user.

Deliver or summarize the published draft for the user.
Crucial: When responding to the user, ALWAYS include the final list of references/notes that were actually used and cited in the brainstorm.
Bundled Resources
agents/retriever.md: retrieval-stage instructions
agents/preprocess.md: per-note preprocessing instruction
agents/draft.md: synthesis drafting instruction
agents/publisher.md: publication rewrite instruction
scripts/find_links.py: retrieval script for wikilinks + tag overlap
scripts/compile_preprocess.py: filter and merge preprocess outputs into a draft packet
scripts/obsidian_utils.py: wikilink and tag helpers
scripts/config_manager.py: shared config loader
scripts/setup.py: interactive config setup
Maintenance Rules
Keep stage boundaries strict: retrieval -> preprocess -> draft -> publish.
Keep prompts in agents/ and scripts in scripts/.
Remove deprecated scripts instead of keeping parallel legacy paths.
Weekly Installs
15
Repository
hxy9243/skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass