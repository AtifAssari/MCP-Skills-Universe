---
title: understand-knowledge
url: https://skills.sh/lum1104/understand-anything/understand-knowledge
---

# understand-knowledge

skills/lum1104/understand-anything/understand-knowledge
understand-knowledge
Installation
$ npx skills add https://github.com/lum1104/understand-anything --skill understand-knowledge
SKILL.md
/understand-knowledge

Analyzes a Karpathy-pattern LLM wiki — a three-layer knowledge base with raw sources, wiki markdown, and a schema file — and produces an interactive knowledge graph dashboard.

What It Detects

The Karpathy LLM wiki pattern (see https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):

Raw sources — immutable source documents (articles, papers, data files)
Wiki — LLM-generated markdown files with wikilinks ([[target]] syntax)
Schema — CLAUDE.md, AGENTS.md, or similar configuration file
index.md — content catalog organized by categories
log.md — chronological operation log

Detection signals: has index.md + multiple .md files with wikilinks. May have raw/ directory and schema file.

Instructions
Phase 1: DETECT

Determine the target directory:

If the user provided a path argument, use that
Otherwise, use the current working directory

Run the format detection script bundled with this skill:

python3 <SKILL_DIR>/parse-knowledge-base.py <TARGET_DIR>

If the script exits with an error, tell the user this doesn't appear to be a Karpathy-pattern wiki and explain what was expected
If successful, proceed. The script writes scan-manifest.json to <TARGET_DIR>/.understand-anything/intermediate/

Read the scan-manifest.json and announce the results:

"Detected Karpathy wiki: N articles, N sources, N topics, N wikilinks (N unresolved)"
List the categories found from index.md
Phase 2: SCAN (already done)

The parse script in Phase 1 already performed the deterministic scan. The scan-manifest.json contains:

Article nodes (one per wiki .md file) with extracted wikilinks, headings, frontmatter
Source nodes (one per raw/ file)
Topic nodes (from index.md section headings)
related edges (from wikilinks)
categorized_under edges (from index.md sections)

No additional scanning is needed. Proceed to Phase 3.

Phase 3: ANALYZE

Dispatch article-analyzer subagents to extract implicit knowledge:

Read the scan-manifest.json to get the article list

Prepare batches of 10-15 articles each, grouped by category when possible (articles in the same category are more likely to have implicit cross-references)

For each batch, dispatch an article-analyzer subagent with:

The batch of articles (id, name, summary, wikilinks, category, content from knowledgeMeta)
The full list of existing node IDs (so the agent can reference them)
The batch number for output file naming
The intermediate directory path: $INTERMEDIATE_DIR = <TARGET_DIR>/.understand-anything/intermediate

The agent will write analysis-batch-{N}.json to the intermediate directory.

Run up to 3 batches concurrently. Wait for all batches to complete.

If any batch fails, log a warning but continue — the scan-manifest provides a solid base graph even without LLM analysis.

Phase 4: MERGE

Run the merge script bundled with this skill:

python3 <SKILL_DIR>/merge-knowledge-graph.py <TARGET_DIR>


The script:

Combines scan-manifest.json + all analysis-batch-*.json files
Deduplicates entities (case-insensitive name matching)
Normalizes node/edge types via alias maps
Builds layers from index.md categories
Builds a tour from index.md section ordering
Writes assembled-graph.json to the intermediate directory

Read the merge report from stderr and announce:

Total nodes, edges, layers, tour steps
How many entities/claims the LLM analysis added
Phase 5: SAVE

Read the assembled-graph.json

Run basic validation:

Every edge source/target must reference an existing node
Every node must have: id, type, name, summary, tags, complexity
Remove any edges with dangling references

Copy the validated graph to <TARGET_DIR>/.understand-anything/knowledge-graph.json

Write metadata to <TARGET_DIR>/.understand-anything/meta.json:

{
  "lastAnalyzedAt": "<ISO timestamp>",
  "gitCommitHash": "<from git rev-parse HEAD or empty>",
  "version": "1.0.0",
  "analyzedFiles": <number of wiki articles>
}


Clean up intermediate files:

rm -rf <TARGET_DIR>/.understand-anything/intermediate


Report summary to the user:

"Knowledge graph saved: N articles, N entities, N topics, N claims, N sources"
"N edges (N wikilink, N categorized, N implicit)"
"N layers, N tour steps"

Auto-trigger the dashboard:

/understand-dashboard <TARGET_DIR>

Notes
The parse script handles ALL deterministic extraction (wikilinks, headings, frontmatter, categories from index.md). The LLM agents only add implicit knowledge that requires inference.
Categories and taxonomy come from index.md section headings, NOT from filename prefixes. The Karpathy spec is intentionally abstract about naming conventions.
The graph uses kind: "knowledge" to signal the dashboard to use force-directed layout instead of hierarchical dagre.
Source nodes from raw/ are lightweight (filename + size only) — we don't parse PDFs or binary files.
Weekly Installs
35
Repository
lum1104/underst…anything
GitHub Stars
10.2K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass